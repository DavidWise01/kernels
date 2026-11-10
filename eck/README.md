# ECK-012 — Four Chrome Wheels / Calibrations as Evidence

One primitive; position, chroma, wavelength, chronos; three witness **display slots**. The UI is a testbed, not a live independent witness quorum.

## New invariant

Every observation **and every calibration** is appended as a typed leaf in the same domain-separated SHA-256 Merkle tree. After pinning a head in memory, the prefix through its recorded leaf count must still rehash to that root before another event or checkpoint can be accepted.

`event_root(N)` binds the complete sequence of typed records. The raw observation contains the four wheel positions and its own SHA-256 leaf digest. A calibration leaf binds the original observation index and parent digest, the wheel name/key, original value, signed offset and derived result. It never changes the raw sample.

### Four wheels

- POSITION, degrees: spatial-phase illustrative calibration
- CHROMA, degrees: hue illustrative calibration
- WAVELENGTH, nm: illustrative wavelength offset (not hardware spectroscopy)
- CHRONOS, ms: illustrative sample-time offset (not a clock synchronization standard)

### Test coverage

`python eck/test_eck012.py`: authenticated current prefix, append extension, mutation of all four calibration offsets, deletion of each calibration, substitution of derived values, raw mutation, event reorder, truncation, stale head, unchanged raw and permitted append.

## Security boundary

The demo's checkpoint and data coexist inside one volatile browser tab; a hostile actor controlling *both* can replace both. This is **not independent custody**. The browser recomputes the old prefix (linear-size); it does **not** implement RFC 6962 compact consistency proofs. The three witness labels are not actual key-bearing witnesses. Browser controls demonstrate continuity without claiming trusted sensor measurements.

## Next invariant — ECK-013

Bind the entire event history to externally signed 2-of-3 custody receipts and a compact append-only consistency proof. Check each calibration's semantic parent linkage during verification, in addition to its Merkle membership.
