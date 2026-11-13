#!/usr/bin/env python3
"""Inject the editable core-development portfolio into the compressed portal build."""
from __future__ import annotations
import argparse
import os
from pathlib import Path
import re
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FRAGMENT = ROOT / "portal-src" / "core-development.html"
MARKER = "<!-- ULTRACORE_CORE_DEVELOPMENT_PORTFOLIO -->"
REQUIRED_TEXT = (
    'id="ultracore-core-development"',
    "RFT-QPU-Sierpinski",
    "SIRM Financial Infrastructure",
    "Evgeny's Theorem",
    "Phi-Genesis",
)

def inject(document: str, fragment: str) -> str:
    if MARKER in document:
        raise ValueError("The core-development portfolio is already present.")
    for required in REQUIRED_TEXT:
        if required not in fragment:
            raise ValueError(f"Portfolio fragment is missing required content: {required}")
    closing_tags = list(re.finditer(r"</body\s*>", document, flags=re.IGNORECASE))
    if len(closing_tags) != 1:
        raise ValueError(f"Expected exactly one closing </body> tag; found {len(closing_tags)}.")
    pos = closing_tags[0].start()
    return document[:pos] + "\n" + fragment.strip() + "\n" + document[pos:]

def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise

def self_test(fragment: str) -> None:
    fixture = "<!doctype html>\n<html><body><main>Research explorer fixture</main></body></html>\n"
    result = inject(fixture, fragment)
    if result.count(MARKER) != 1 or result.index(MARKER) > result.lower().rfind("</body>"):
        raise AssertionError("Portfolio marker was not injected exactly once inside the body.")
    if not all(required in result for required in REQUIRED_TEXT):
        raise AssertionError("One or more required project entries are missing.")
    try:
        inject(result, fragment)
    except ValueError as exc:
        if "already present" not in str(exc):
            raise
    else:
        raise AssertionError("Duplicate injection was not rejected.")

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", nargs="?", help="Decompressed interactive portal HTML file.")
    parser.add_argument("fragment", nargs="?", default=str(DEFAULT_FRAGMENT), help="HTML fragment.")
    parser.add_argument("--self-test", action="store_true", help="Run an in-memory insertion test.")
    args = parser.parse_args()
    fragment_path = Path(args.fragment) if not args.self_test else DEFAULT_FRAGMENT
    fragment = fragment_path.read_text(encoding="utf-8")
    if args.self_test:
        self_test(fragment)
        print("portal injection self-test: PASS")
        return 0
    if not args.html:
        parser.error("html is required unless --self-test is selected")
    html_path = Path(args.html)
    document = html_path.read_text(encoding="utf-8")
    result = inject(document, fragment)
    atomic_write(html_path, result)
    print(f"Injected core-development portfolio into {html_path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
