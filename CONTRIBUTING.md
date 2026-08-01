# Contributing to UltraCore RFT

Thank you for your interest in this project.

## What this repository is

UltraCore RFT is a **documentation and research reference repository**.
All executable code lives in the companion implementation repository:

**→ [RFT-SIRM/Rift-Network](https://github.com/RFT-SIRM/Rift-Network)**

## How to open an issue

1. Go to the [Issues tab](https://github.com/RFT-SIRM/UltraCore-RFT/issues).
2. Click **New issue**.
3. Describe the problem clearly: what page, what section, what is incorrect.
4. For implementation issues, open them in [Rift-Network](https://github.com/RFT-SIRM/Rift-Network/issues).

## How to propose a documentation change

1. Fork the repository.
2. Create a branch: `git checkout -b fix/your-description`.
3. Edit the relevant Markdown file under `docs/` or `README.md`.
4. Verify locally: `pip install -r requirements.txt && mkdocs build --strict`
5. Open a Pull Request against `main`.

## What we do not accept

- Changes to `RFT_MATHEMATICAL_FOUNDATIONS.md` — intentionally stable.
- Code contributions — those belong in Rift-Network.
