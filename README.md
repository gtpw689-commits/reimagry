# Reimagry

Reimagry is a Termux-native AI processing framework designed to run
reliably on Android without native Python compilation.

## Design Principles

- Standard-library cryptography only
- Deterministic hashing
- No pip native extensions
- Optional decentralised sync
- GitHub used for coordination, not runtime dependency

## Runtime

- Platform: Termux (Android)
- Python: 3.12+
- Hashing: hashlib.blake2b
- Imaging: Pillow (Termux package)

## Status

This repository represents a stable, reproducible baseline build.
