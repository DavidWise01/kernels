# ECK-010 — Chrome-wheel evidence kernel

A four-wheel, chrome/neon interactive evidence visualization with append-only local demonstration.

## Invariant

If an inventory of length `m` is extended to `n >= m`, the old committed sequence must equal the first `m` records of the new sequence. The browser demonstration computes RFC 6962-style domain-separated Merkle roots but does **not** implement the compact RFC 6962 consistency-proof verification protocol. Its Verify Prefix control only checks the length progression of the current in-memory array, so it is **not** a cryptographic proof of prefix consistency. For production, pin the old authenticated root and verify a consistency proof against the new root, with independently operated witness receipt signatures.

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

## Planned ECK-011

Implement compact RFC 6962 consistency proofs, independent receipt custody, persistent verification and two-of-three witnessed append certification.
