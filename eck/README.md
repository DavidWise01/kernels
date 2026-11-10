# ECK-011 — Chrome-wheel evidence kernel

A four-wheel, chrome/neon interactive evidence visualization with append-only local demonstration.

## Invariant

If an inventory of length `m` is extended to `n >= m`, the old committed sequence must equal the first `m` records of the new sequence. The browser demonstration computes RFC 6962-style domain-separated Merkle roots but does **not** implement the compact RFC 6962 consistency-proof verification protocol. Its Verify Prefix control compares the recomputed SHA-256 Merkle root of the previously pinned in-memory prefix against the old checkpoint before advancing the head. This is a **linear-size local recomputation**, not a compact cryptographic consistency proof that can be independently checked from two signed roots alone. For production, pin the old authenticated root and verify a consistency proof against the new root, with independently operated witness receipt signatures.

## Wheel mappings

1. Position: 0-359 degrees (illustrative spatial phase)
2. Chroma: 0-359 degrees (hue)
3. Wavelength: 380-750 nm (illustrative visible light)
4. Chronos: 0-999 ms (illustrative sample interval)

The raw record is hashed before the calibration event; calibration is appended separately.

## Limitations

Three witness panels are labels; no real network witness or Ed25519 signing service is wired. Browser state is volatile. The displayed digest binds to local records but is not an external trusted checkpoint.

## Run

Open `index.html` from a secure HTTPS GitHub Pages origin. The cryptographic Web Crypto API requires a secure context.

## ECK-011: Chromatic Evidence Continuity

The wavelength wheel now has an independent calibration offset slider (-60 to +60 nm). Every calibration event references its parent sealed sample SHA-256 leaf, stores the exact offset and interpreted wavelength, and is appended without rewriting the original wavelength, hue, position or chronos sample. A calibration is rejected if it fails the pinned in-memory prefix check. The original measurements in this page are simulated slider inputs, not hardware spectroscopy or a metrologically calibrated sensor.

`python eck/test_eck011.py` runs the standard-library regression suite: two divergent calibrations from one root, mutation of time/hue/wavelength, spoofed parent, derived-value modification, out-of-range calibration, and raw reading range validation.

## Next bound — ECK-012

Commit and verify calibration *records themselves* in an append-only authenticated tree (not just raw observations); then add a compact RFC 6962 consistency verifier and independently operated witness receipts. The page's in-memory head is not external custody.
