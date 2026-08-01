# agave-abiv2-memory-contexts

Alternative ABIv2 `MemoryContexts` implementation for Agave SVM focused on safer permission handling, cleaner region management, and future-proof memory mapping behavior.

## Overview

This repository contains an experimental refinement of the Agave SVM ABIv2 memory context implementation.

![ABIv2 MemoryContexts Architecture](./agave-abiv2-rift-architecture.png)

The primary focus is improving correctness and safety around writable account permission handling during nested CPI execution flows while preserving compatibility with the existing ABIv2 execution model.

The implementation introduces:

* Per-frame writable permission rollback
* Safer region initialization and bounds validation
* Dynamic region count calculation instead of hardcoded constants
* Improved error propagation
* Cleaner ABIv2 region construction flow
* Better isolation between nested execution frames

The goal is not to redesign the SVM memory model, but to improve correctness and robustness of the existing architecture.

---

# Motivation

In the current ABIv2 flow, writable permissions can be updated dynamically during instruction execution.

However, under nested CPI scenarios, writable permission changes may persist across instruction frames unless explicitly restored.

This can potentially create:

* permission leakage between nested calls
* inconsistent writable state visibility
* harder-to-debug execution behavior
* future maintenance complexity for deeper ABIv2 integrations

This repository explores a rollback-safe approach where writable account permissions are restored automatically when execution frames are popped.

---

# Key Improvements

## 1. Per-Frame Writable Permission Rollback

The original implementation updates writable permissions in-place.

This implementation stores writable state snapshots before mutation and restores them automatically during frame teardown.

### Benefits

* Prevents writable permission leakage
* Improves nested CPI isolation
* Keeps execution frame boundaries deterministic
* Makes permission transitions explicit and reversible

---

## 2. Dynamic Region Count

Instead of relying on a hardcoded region count (`392`), region sizing is derived dynamically from VM address layout boundaries.

### Benefits

* Better future compatibility
* Safer against VM layout evolution
* Reduces hidden assumptions in memory mapping logic

---

## 3. Safer Error Handling

The implementation replaces several panic-prone paths (`unwrap`, `expect`) with structured error propagation using `InstructionError`.

### Benefits

* Prevents unexpected validator panics
* Improves robustness under malformed states
* Easier debugging and testing

---

## 4. Cleaner ABIv2 Region Construction

ABIv2 region creation is reorganized into a safer and more explicit initialization flow.

### Benefits

* Easier auditing
* Better maintainability
* Reduced implicit assumptions
* Clearer separation of memory regions

---

# Design Goals

This repository intentionally avoids introducing architectural changes to the SVM execution model.

The objective is:

* preserve compatibility
* improve execution safety
* reduce state leakage risks
* simplify future ABIv2 evolution

The implementation is designed as a minimal invasive refinement rather than a scheduler or runtime rewrite.

---

# Relation to Scheduler Research

This work was developed alongside experiments involving contention-aware transaction scheduling for Agave banking_stage.

Although independent from scheduling itself, safer memory isolation becomes increasingly important when execution batching and dependency-aware scheduling strategies are introduced.

In particular:

* deterministic batching
* reduced lock churn
* independent execution groups
* trusted execution paths

all benefit from stricter execution-frame memory correctness.

---

# Current Status

Experimental / research implementation.

The repository is intended for:

* architecture discussion
* ABIv2 experimentation
* nested CPI safety analysis
* scheduler + memory interaction research

It is not production-ready validator code.

---

# Potential Future Work

Possible areas for future exploration:

* per-frame region allocators
* immutable sysvar snapshots
* trusted batch memory fast-paths
* arena-based allocation strategies
* tighter scheduler ↔ memory integration
* lock-aware memory locality optimizations

---

# Testing Focus

The implementation was tested primarily against:

* nested CPI flows
* writable permission restoration
* repeated instruction frame transitions
* ABIv2 region initialization consistency

Additional stress testing and benchmarking are still required.

---

# Repository Purpose

This repository exists primarily as a technical exploration of safer ABIv2 memory semantics inside Agave SVM.

Feedback, corrections, and architecture discussion are welcome.
