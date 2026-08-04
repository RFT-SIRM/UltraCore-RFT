/*
 * RFT-SIRM CDT Fuzzer for seL4
 * Document ID: RFT-EXP-SELC4-2026-001
 * Laboratory: RFT-SIRM / UltraCore-RFT
 * License: Apache-2.0
 *
 * Single-file drop-in module for sel4test.
 * Place in: projects/sel4test/apps/sel4test-tests/src/tests/
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sel4/sel4.h>
#include <sel4test/test.h>
#include <vka/object.h>
#include <vka/capops.h>

#define N 512

struct C {
    seL4_CPtr c;
    int t;
    int orig;
    int ok;
    vka_object_t obj;
};

struct S {
    vka_t *v;
    struct C c[N];
    int n;
    uint32_t r;
    int ok;
    int bad;
};

static uint32_t rnd(struct S *s) {
    s->r = s->r * 1103515245u + 12345u;
    return s->r;
}

static int get(struct S *s) {
    for (int i = 4; i < N; i++) {
        if (!s->c[i].ok) {
            s->c[i].ok = 1;
            s->c[i].orig = 0;
            s->c[i].c = seL4_CapNull;
            memset(&s->c[i].obj, 0, sizeof(vka_object_t));
            s->n++;
            return i;
        }
    }
    return -1;
}

static void put(struct S *s, int i) {
    if (i >= 0 && i < N && s->c[i].ok) {
        s->c[i].ok = 0;
        s->c[i].orig = 0;
        s->c[i].c = seL4_CapNull;
        s->n--;
    }
}

static int any(struct S *s) {
    if (!s->n) return -1;
    for (int k = 0; k < 512; k++) {
        int i = rnd(s) % N;
        if (s->c[i].ok) return i;
    }
    return -1;
}

static int retype(struct S *s) {
    int x = rnd(s) % 3;
    int t, b;
    switch (x) {
        case 0: t = seL4_EndpointObject; b = seL4_EndpointBits; break;
        case 1: t = seL4_NotificationObject; b = seL4_NotificationBits; break;
        default: t = seL4_TCBObject; b = seL4_TCBBits; break;
    }
    vka_object_t o;
    int e = vka_alloc_object(s->v, t, b, &o);
    if (e) return e;
    int i = get(s);
    if (i < 0) {
        vka_free_object(s->v, &o);
        return -1;
    }
    s->c[i].c = o.cptr;
    s->c[i].t = t;
    s->c[i].orig = 1;
    s->c[i].obj = o;
    return 0;
}

static int copy(struct S *s) {
    int a = any(s);
    if (a < 0) return -1;
    seL4_CPtr d;
    int e = vka_cspace_alloc(s->v, &d);
    if (e) return e;
    cspacepath_t p, q;
    vka_cspace_make_path(s->v, s->c[a].c, &p);
    vka_cspace_make_path(s->v, d, &q);
    e = vka_cnode_copy(&q, &p, seL4_AllRights);
    if (!e) {
        int b = get(s);
        if (b < 0) {
            vka_cnode_delete(&q);
            vka_cspace_free(s->v, d);
            return -1;
        }
        s->c[b].c = d;
        s->c[b].t = s->c[a].t;
    } else {
        vka_cspace_free(s->v, d);
    }
    return e;
}

static int del(struct S *s) {
    int a = any(s);
    if (a < 0) return -1;
    if (s->c[a].orig) {
        vka_free_object(s->v, &s->c[a].obj);
    } else {
        cspacepath_t p;
        vka_cspace_make_path(s->v, s->c[a].c, &p);
        vka_cnode_delete(&p);
        vka_cspace_free(s->v, s->c[a].c);
    }
    put(s, a);
    return 0;
}

static int run(env_t env, int n, uint32_t seed) {
    struct S s;
    memset(&s, 0, sizeof(s));
    s.v = &env->vka;
    s.r = seed ? seed : 0x52465453;

    for (int i = 0; i < n; i++) {
        int op = rnd(&s) % 4;
        int e = -1;
        switch (op) {
            case 0: e = retype(&s); break;
            case 1: e = copy(&s); break;
            case 2: e = del(&s); break;
            case 3: e = del(&s); break;
        }
        if (!e) s.ok++;
        else s.bad++;
    }

    printf("\n========== RFT-SIRM CDT FUZZ REPORT ==========\n");
    printf("Total ops OK:   %d\n", s.ok);
    printf("Total ops FAIL: %d\n", s.bad);
    printf("Final caps:     %d\n", s.n);
    printf("============================================\n\n");

    for (int i = 0; i < N; i++) {
        if (s.c[i].ok) {
            if (s.c[i].orig) {
                vka_free_object(s.v, &s.c[i].obj);
            } else {
                cspacepath_t p;
                vka_cspace_make_path(s.v, s.c[i].c, &p);
                vka_cnode_delete(&p);
                vka_cspace_free(s.v, s.c[i].c);
            }
            put(&s, i);
        }
    }
    return 0;
}

/* ========== Test Definitions ========== */

static int t1(env_t env, void *a) {
    printf("\n[RFT-SIRM] CDT Fuzzer v6\n");
    return run(env, 200, 0x52465453);
}
DEFINE_TEST(RFT_CDT_0001, "RFT-SIRM: CDT fuzzer basic v6", t1, true)

static int t20(env_t env, void *a) {
    printf("\n[RFT-SIRM] CDT 20min\n");
    int e = 0;
    for (int i = 0; i < 200; i++) {
        if (run(env, 10000, 0x52465453 + i) != 0) e++;
        printf("[RFT] batch %d done\n", i);
    }
    return e;
}
DEFINE_TEST(RFT_CDT_20MIN, "RFT-SIRM: CDT fuzzer 20-minute run", t20, true)

static int tM(env_t env, void *a) {
    printf("\n[RFT-SIRM] CDT MARATHON (10M ops)\n");
    int e = 0;
    for (int i = 0; i < 1000; i++) {
        if (run(env, 10000, 0x52465453 + i) != 0) e++;
        if (i % 100 == 0) printf("[RFT] Marathon progress: %d/1000\n", i);
    }
    return e;
}
DEFINE_TEST(RFT_CDT_MARATHON, "RFT-SIRM: CDT fuzzer marathon (10M ops, ~1 hour)", tM, true)
