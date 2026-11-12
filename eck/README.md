# ECK-042 — Time-Unrolled Four-Carrier Bit-Plane Neural Reversal

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

## ECK-013: Wheels before witnesses

The centerpiece is now a live 3-panel coupling instrument:

- **Spectral estimate:** approximate RGB representation of the wavelength wheel (380–750 nm), with visible-band intensity taper. This is screen RGB, not a spectrometer, and not guaranteed to reproduce a physically accurate perceived color.
- **Chroma:** independent HSL hue wheel. The same hue can correspond to many spectra; a monochromatic wavelength is not interchangeable with a display hue.
- **Position × Chronos:** explicit illustrative phase composition `(position_degrees + (chronos_ms mod 360)) mod 360`. This is a demo visualization convention, not a physical conversion of milliseconds to angles.

All four wheel sliders update these views immediately; the prior authenticated event ledger remains below the instrument.

## Next natural invariant — ECK-014

Make coupling user-selectable, with independent, derived and latched modes. Record coupling model/version alongside derived state so an observer can reproduce exactly how a visual was produced. No silent physical assumptions.

## ECK-014 geometry correction

**Canonical layout:** four Chrome wheels orbit a single central singlet. The singlet is the shared reference point; the wheels are coordinates/dimensions of one observation, not four separate instruments or four separate evidence roots.

```text
                    POSITION
                       O
                       |
           CHRONOS O-- . --O CHROMA
                       |
                       O
                   WAVELENGTH

                   . = SINGLET
```

The browser visualization now places Position north, Chroma east, Wavelength south, Chronos west around a chrome-lit central dot. Updating the wheels updates central glow and derived display phase. This is graphical coupling, not evidence of physical causation or numerical identity between hue and wavelength. Earlier evidence event structures are retained.

## ECK-015: Three visual field-strength bands

Four independently adjustable **lobe intensity** controls surround the invariant central singlet. Each lobe receives a qualitative band: weak (< 1/3; cyan), medium (1/3 to < 2/3; amber), strong (>= 2/3; magenta). This is a user-defined field-intensity visualization, **not** a mapping of physical weak/strong nuclear interactions or a scientifically derived medium fundamental force.

Each wheel's glow and border reflect its field strength; the central dot stays at the same location and changes visual emphasis as aggregate intensity changes. Balanced means max-minus-min intensity below 0.08. Polarized means a larger spread. The existing evidence ledger remains below.

## Next natural invariant — ECK-016

Conserve total normalized field intensity as the four lobes exchange weight around the singlet, while permitting an explicitly tagged external excitation event to add or remove intensity.

## ECK-016 — Closed-field transfer and explicit excitation

- Four integer lobe-strength controls are constrained to 0..100, starting at [35,35,35,35], sum 140.
- **CLOSED / CONSERVED:** increasing a chosen lobe draws integer units from other lobes in a fixed rotational order; decreasing distributes them to neighbors in the same order. If neighboring lobes lack capacity, the requested change is partially fulfilled, not silently created/destroyed. The total is preserved exactly.
- **EXCITATION:** turning a slider changes the total explicitly; this models an *open* system, not a conserved transfer.
- **BALANCE FIELD:** distributes the existing total across four lobes using quotient/remainder, leaving the total unchanged.
- Visual weak/medium/strong bands remain display categories only; their names are not claims about the physics of weak and strong interactions.

The singlet remains geometrically centered. The reference suite `python eck/test_eck016.py` checks 6,450 assertions across ordinary transfers, saturation, requested overflows and rebalancing. The in-browser implementation is an illustrative user interface, not a validated physical simulation.

### ECK-017 next natural invariant

For a closed system, does a complete cycle of reversible transfers return to its initial distribution? Distinguish invertible phase paths from saturated/clipped paths, which can lose information.

## ECK-017 canonical Quantum Chrome address frame

The machine has **nine named directional positions plus one fixed singlet**, not merely four UI wheels. The nine addresses, in canonical supplied order, are:

```text
{{ upperleftback{{n}},
   lowerleftback{{n}},
   centerback{{n}},
   centerupper{{n}},
   center{{n}},
   centerlower{{n}},
   upperrightfront{{n}},
   centerrightfront{{n}},
   lowerrightfront{{n}} }}^{{n}}^{{n}} || repeat

                         .  = singlet (10th)
```

The nine named positions and the singlet must remain distinct, even though `center{{n}}` is geometrically near the singlet. The page positions labels for legibility, not as authoritative 3D coordinates. `n` is a bounded UI symbolic parameter from 1 to 9. `|| repeat` records a symbolic iteration of the nine-position frame, **not** a direct materialization of a tower-sized state space, and the exponent grouping is not yet given numerical execution semantics.

The cloverleaf's four fields are an outer visualization of this address frame; weak, medium and strong continue to mean illustrative intensity bands. Neither orbital electron probability density nor force strength is asserted to be physically derived from the symbolic lattice.

Test: `python eck/test_eck017.py` checks nine unique address labels, singlet as tenth, preserved appearance for each `n` from 1 to 9 and bounded repeat notation.

### ECK-018 next natural question

Determine a **single reversible address mapping** from the nine named positions to the four cloverleaf fields while leaving the tenth singlet invariant. A mapping that drops positions or treats the singlet as one of nine fails.

## ECK-018 — Canonical nested pyramid foundation

Original notation, deliberately preserved verbatim including the nonstandard 17.5 closing delimiter:

```text
[[ {{27}}^{{24}}^{{21}}^{{17.5))^{{13}}^{{8}}^{{5}}^{{3}}^{{2}} ]]^[[ {{1}}^{{1}} ]]
```

Interpretation for this release: eleven **ordered nested levels** (nine body/foundation values `[27,24,21,17.5,13,8,5,3,2]` followed by two unit caps `[1,1]`). They have **no assumed numerical exponent semantics**; the markup is a nesting/address language and the caret is a symbolic layering operator. The suffix `17.5))` is retained as textual evidence; the numeric model uses decimal 17.5. Every level has a distinct index, including the two equal-valued caps.

The browser now offers a layered pyramid SVG with an eleven-step slider, a preserved original expression, and one fixed central singlet. Layers are not eleven experimentally discovered physical dimensions, nor evidence of M-theory; the correspondence to the 11-dimensional concept is only an inspiration.

Invariant: `length(levels)==11`, `levels[0]==27`, `levels[8]==2`, `levels[9:]==[1,1]`, and each displayed level remains a member of the same ordered nested frame.

Next natural test: define an invertible, layer-indexed transport between `{{n}}^{{n}}^{{n}}` and this eleven-level frame, including how the fractional 17.5 level acts as a boundary.

## ECK-019 — Living pyramid / Hamilton cycle

The nested pyramid is now interpreted as a biological-inspired **ordered cycle of transitions**, not merely eleven exponents.

Original state marks (preserved as notation):

\`\`\`text
(0=-.)
[1+1, single cell mito]
[2 || 3 || 5 || 8, mito complete]
[ \\\13//, emergence ]
[ ||\\\17//.5||, division ]
[ || 21 ||, re-emergence {{13+8}}, diatom ]
[ ||| 24 |||, start walking Hamilton ]
[ ||\\\\\`27\`//||, one full Hamilton, return to (0=-.) ]
\`\`\`

There are 8 semantic macro-stages, expanded for the walk to **12 vertex IDs**:
\`0, 1a, 1b, 2, 3, 5, 8, 13, 17.5, 21, 24, 27\`, then return to \`0\`.
The two one-cells have equal numeric values but *different IDs*. The 9 non-unit numerical stages are kept distinct; origin 0 is not silently identified with the 1 levels. The defining edge set is the cyclic adjacency of this route.

### Invariants
- Singlet at origin \`(0=-.)\`; return to the same origin at completion.
- Identity matters even when values match: \`1a != 1b\`.
- Division at \`17.5\` is a decimal-valued boundary, not an integer.
- Re-emergence uses \`13 + 8 = 21\`.
- On the specified 12-vertex **cycle graph**, the route visits each vertex exactly once before returning, hence is a Hamiltonian cycle *on this graph*. It does not establish any Hamiltonian traversal of an unenumerated full spatial or Quantum Chrome address lattice.
- The biological terms are model metaphors, not mitochondrial/cell-division experimental findings.

### Controls

The ECK console adds a progression diagram with NEXT VERTEX, FULL HAMILTON CYCLE, and RETURN TO ORIGIN; ECK-018 nested levels remain visible below it.

Test: \`python eck/test_eck019.py\` checks unique identities, decimal division, \`21=13+8\`, valid tour, invalid repeated vertices, incomplete route, and broken edges.

**Next natural invariant — ECK-020:** distinguish a **Hamilton path** from a **Hamilton cycle**, and specify the return edge \`27→0\` as a reversible fold/unbind operation, then test whether the singlet and state ancestry survive repeated rounds.

## ECK-020 — `27 → }{ → (0=-.)` and generation ancestry

The existing 12-identity mitochondrial transition graph has an explicit return-fold operation. The user can advance from the origin through 27, then invoke `}{ FOLD / BEGIN NEXT CYCLE`. A fold before the terminal 27 state is rejected. On a valid fold:

1. The completed route `0 → 1a → 1b → 2 → 3 → 5 → 8 → 13 → 17.5 → 21 → 24 → 27 → 0` is saved in the in-memory generation archive.
2. The invariant singlet identifier remains `(0=-.)`.
3. The generation counter increments by exactly one.
4. The next cycle starts at step zero; prior completed cycles remain accessible in the UI.
5. The UI's `RESTART DISPLAY` control resets the current traversal position only, rather than deleting the completed-round archive.

The separately provided standard-library reference test `python eck/test_eck020.py` ran locally and passed **1005 of 1005 assertions over 100 completed rounds**. JavaScript syntax on the committed HTML was also verified. The browser itself has not been end-to-end tested.

**Scope:** the generation archive is only JavaScript memory. Browser reload can erase it. This is a demonstrative recurrence and history model, not durable immutable custody or proof of a Hamiltonian tour of the full unenumerated lattice. Completed round records are frozen shallow JS objects with a frozen route array, not an external audit record.

**ECK-021 next invariant:** make each cycle carry a reproducible phase signature across the four Chrome lobes and the 9-address frame. The singlet identity remains unchanged; state changes are described as a distinct, replayable phase record.

## ECK-021 — Cycle phase memory

A valid completed fold records a generation-indexed, frozen snapshot of:

- four wheel readings `[position, chroma, wavelength, chronos]`;
- four lobe strength units and their sum;
- all nine named Quantum Chrome addresses, selected address and symbolic `n`;
- eleven nested pyramid layers `[27,24,21,17.5,13,8,5,3,2,1,1]`;
- the distinct 12-vertex Hamilton cycle route and its closing edge to origin `(0=-.)`.

The singlet identity is invariant. Subsequent changes to wheel sliders, field strengths, symbolic nesting, or selected address do not alter completed-generation snapshots. The browser adds an export button that produces `eck021-phase-memory.json` containing the complete in-memory archive.

**Security limits:** the archive is volatile; export is manual; JavaScript `Object.freeze` is a programming guard, not durable or cryptographic immutability. The browser page was syntax checked but not end-to-end browser tested. The reference model was exercised locally across 100 generations, and the GitHub test source supplies reproducible assertions.

**ECK-022 natural bound:** the same origin plus distinct phase signatures must permit exact replay and measurable comparison between two generations, with the choice of coupling model stored explicitly.

## ECK-022 — Replay and compare completed generations

The living-cycle panel now has two generation selectors, **Compare Phases**, **Replay Gen A**, and **Replay Gen B**.

Comparisons are computed from saved snapshots, not from live slider values. They report:
- signed numeric deltas for all four wheel readings, in their original display units;
- signed field-unit deltas for four cloverleaf lobes and the field-total change;
- changes to the selected Quantum Chrome address and symbolic `n`;
- identity checks for singlet origin, Hamilton route, nine-address frame and eleven-tier nested pyramid.

Replay validates the snapshot's origin, physical slider bounds, integer field units, selected address, address frame and nested pyramid before copying values into the **live instrument only**. The saved archive is not rewritten by replay; replay does not create an observation/seal, does not change the generation counter, and does not advance the Hamilton cycle.

The comparison uses signed numeric differences, including hue differences; these are **not** modular angular shortest-path distances or claims of experimentally coupled wavelengths/hue. ECK-022 has no literal numerical exponent semantics for symbolic `n`.

**Verification:** HTML JavaScript parsed successfully. A reference JavaScript model completed 10,000 pairwise generation comparisons, and replay-copy immutability was checked. A Python standard-library regression suite is committed at `test_eck022.py` but was not executed in this run. Browser end-to-end integration and live Pages publication have not been verified.

### Next natural bound — ECK-023

Define a versioned transport model mapping a completed generation's nine addresses to four cloverleaf lobes *without discarding address identities*, then replay the complete derived color/phase projection deterministically.

## ECK-023 — Nine addresses in four cloverleaf transport channels

The console now implements a reversible packetization of the **nine distinct Quantum Chrome addresses** into four named Chrome channels, without identifying any address with the fixed singlet:

```text
POSITION    <- address indices 0,4,8
CHROMA      <- address indices 1,5
WAVELENGTH  <- address indices 2,6
CHRONOS     <- address indices 3,7

SINGLET = (0=-.) remains distinct.
```

The deterministic transport convention for this release is `channel = address_index % 4`. Each packet retains `{index, name, n}`, and each channel retains its own field identity. Reverse transport validates packet indices, channel assignment, uniqueness, complete coverage, identical symbolic nesting parameter, and the original canonical address names/order.

The UI includes **PACK 9 → 4**, **UNPACK 4 → 9**, and **TEST DROPPED PACKET**, making reversibility visible. The round trip and dropped-packet rejection have been executed in a JavaScript reference harness; full browser rendering is not yet verified. The Python regression suite `test_eck023.py` was committed; run it in a local environment with `python eck/test_eck023.py`.

**Boundary:** this is a lossless routing schema, not a claim that four real electromagnetic/nuclear physical fields encode nine quantum states. Numeric output phases and force labels remain illustrative. Unlike aggregating to four scalar strengths, four channels keep their packet contents for exact recovery.

### ECK-024 — Natural next bound

Add cyclic **transport through the eleven nested pyramid levels**. Verify that the nine address identities and their `n` values survive every level, including the two distinguishable `1` caps, before `27 → }{ → (0=-.)`.

## ECK-024 — Reversible transport through eleven nested layers

The nine named address packets are preserved in four indexed Chrome channels through exactly eleven indexed layers:

```text
L01 {{27}} → L02 {{24}} → L03 {{21}} → L04 {{17.5}}
    → L05 {{13}} → L06 {{8}} → L07 {{5}} → L08 {{3}}
    → L09 {{2}} → L10 {{1}} → L11 {{1}}
                                        → }{ → (0=-.)
```

The two unit caps `L10={{1}}` and `L11={{1}}` have **equal values but unequal layer identities**. Every hop copies the packet envelope and confirms exact recovery of nine identities and the symbolic `n`. The reverse control walks stored levels back toward the foundation; the fold control is enabled logically only at the last cap with a full eleven-level history. A fold archives a summary of level indices, values and packet fingerprints in volatile browser memory, then returns to the fixed origin without modifying the archived circuit.

The page adds **Load 9 into Foundation**, **Next Layer**, **Reverse**, **Fold to Origin**, and **Test Missing Packet** controls. A tampered packet is rejected. Loading a new foundation replaces only the active transport session, not previously archived completed circuits.

**Verification:** page JavaScript syntax passed; a direct reference exercise of the committed transport functions passed 414 assertions for `n=1..9`, including forward/reverse identity, skipped/reordered layer rejection, unique cap indices, and dropped packet detection. `test_eck024.py` is committed as a standalone Python regression; browser end-to-end interactions and live Pages publication were not verified.

**Scope:** level nesting is a symbolic address model, not established 11-dimensional M-theory physics. Current routing clones transport packets identically across layers: the layer label changes but the data payload does not undergo a physical transformation. Fingerprints here are serialized comparison strings, not cryptographic hashes. The archive is not durable across reload.

### ECK-025 — Next natural bound

Define an **invertible level-specific transform** `T_k` at each nested level rather than merely carrying the same packet unchanged. Test the inverse `T_k^{-1}`, retaining all nine address identities, distinct unit-cap indices, and the unchanged singlet at the return fold.

## ECK-025 — Level-specific reversible phase rotation

Each of the nine named address packets carries an integer phase in `Z/9Z`. At the foundation `L1={{27}}`, the phase of address `i` is `i`. The directed transition from nested level `Lk` to `L(k+1)`, for `k=1..10`, applies:

```text
T_k:      phase_i -> (phase_i + k) mod 9
T_k^-1:   phase_i -> (phase_i - k) mod 9

ID, original address index, channel index, nesting n, and singlet remain unchanged.
```

**What changes:** all nine phases rotate at every hop; each hop uses a distinct *layer index*, including transitions into `L10={{1}}` and `L11={{1}}`. **What does not change:** which of the nine address identities and which of four channels carry each packet.

The new nested-transport console performs actual reversible transformations rather than cloning an unchanged packet. Its **NEXT LAYER** button applies `T_k`; **REVERSE** independently computes the inverse before moving the cursor back; **}{ FOLD** computes all ten inverse transformations from the final layer and refuses closure unless the original foundation packets are recovered exactly. **TEST MISSING PACKET** in this version mutates a phase (not a packet count) and verifies rejection.

Every nested layer validates the entire chain, including each intervening transform, complete nine-address coverage, independent L10/L11 identities and fixed singlet. The first level is initialized from the canonical indexed phases.

**Verification:** the GitHub HTML's JavaScript passed syntax validation. A reference execution of its committed transport functions passed **207 assertions**, covering nine symbolic `n` settings, ten forward transformations and corresponding inverses, complete return to foundation and mutation rejection. `test_eck025.py` was committed but has not been executed as a separate Python suite in this turn. Browser end-to-end rendering and live GitHub Pages publication are unverified.

This is reversible **modular address-phase arithmetic**, not evidence that real electron orbital phases or physical forces follow this operation. Values are exact integers, so the inverse requires no floating-point approximation. As before, the archive is volatile and is not independent custody.

### ECK-026 — Natural bound

Allow an explicit phase coupling at each level that transfers phase between **different address packets** while remaining invertible, and test the inverse of the full 11-level stack. The current `T_k` shifts every phase by the same amount independently and does not model packet-to-packet interaction.

## ECK-026 — Invertible address-to-address coupling

Each of the nine indexed Quantum Chrome addresses carries an integer phase in `Z/9Z`; all four Chrome transport channels preserve address indices and identities. At the boundary between level `Lk` and `L(k+1)` for `k = 1..10`, define distinct packet indices:

```text
source = (k-1) mod 9
target = k mod 9

FORWARD:
  all phases p_i <- (p_i + k) mod 9
  p_target <- (p_target + p_source) mod 9

REVERSE:
  p_target <- (p_target - p_source) mod 9
  all phases p_i <- (p_i - k) mod 9
```

The reverse order is essential. The shear is invertible over modulus nine even though nine is composite, because its matrix has determinant one. Each nested transition therefore couples two distinct packet identities instead of merely applying independent uniform rotation.

The UI **NEXT LAYER** applies the forward transform, **REVERSE** checks the exact inverse, and **}{ FOLD** composes all ten inverses from the final unit cap. `L10={{1}}` and `L11={{1}}` remain separate indexed states. No numeric or identity information is lost; the singlet remains `(0=-.)`.

**Verification:** the committed HTML JavaScript passed syntax validation, and a direct harness exercising its actual transform code passed **297 assertions** across nine symbolic `n` settings (ten forward transforms, inverses, completeness checks, level-index checks and phase-mutation rejection). `test_eck026.py` was committed as a Python reference suite; full browser tests, Pages publication and separate Python execution remain unverified.

**Scope:** this is a chosen mathematical phase-coupling operator, not a validated model of measured electron orbitals, the Standard Model weak/strong forces or M-theory. The in-browser circuit archive is volatile.

### ECK-027 — Next natural bound

An interactive **coupling graph** should show which nine addresses exchange phase at each of the ten transitions. Test whether all nine addresses participate as both source and target over a complete traversal, and whether an explicit per-edge schedule and phase-history replay remain lossless.

## ECK-027 — Live Canvas2D neural-style mesh

A new Canvas2D instrument displays the nine Quantum Chrome address nodes in a directed coupling graph centered on the fixed singlet. Four overlapping colored elliptical fields visualize the Chrome carriers. **Next Edge**, **Reverse Edge**, **Show Full Ring**, and **Reset Mesh** update the drawn edge history and current highlighted pair.

This is a visual **graph/neural-style connection topology**, *not* a trained neural network: no learned weights, gradients, activations, backpropagation, or statistical claims are implemented. The underlying reversible mod-nine phase transport from ECK-026 remains active in the nested transport section.

### Important mathematical boundary

For transitions `k=1..10`, the selected source and target are `(k-1) mod 9` and `k mod 9`. The first **nine** transitions form the directed 9-cycle:

```text
0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 0
```

All nine nodes are sources and all nine are targets. **Transition 10 repeats edge `0→1`**; there are ten transition events but only nine distinct edges. This follows directly from the period-nine coupling schedule and has an explicit regression test in `eck/test_eck027.py`.

Browser JavaScript parsing passed. The node/edge cardinalities were evaluated independently. Full canvas rendering and live Pages deployment remain unverified. The user-defined weak/medium/strong color bands are abstract display-intensity states, not a scientifically established mapping to fundamental forces.

### ECK-028 natural boundary

Replace visual-only edge lights with a truly **operational neural-like update layer**: nine phase activations, a sparse directed adjacency matrix, optional learnable-but-versioned edge weights, and exact reversible transport as the baseline. Keep learned updates separate from reversible transforms because generic learning is not invertible.

## ECK-028 — Generational nodes

Canonical supplied notation:

```text
[[ 3x3x3 :: {[(3x3)3]} :: {{3x3}}^3 ]]
```

The implemented meaning is **three separately indexed generations**, each containing a `3×3` plane of the **nine existing named Quantum Chrome addresses**. Each node has an unambiguous identity `(g,r,c)` with `g,r,c∈{0,1,2}`; its address name is `names[3*r+c]`. There are 27 unique nodes, and **one separate invariant singlet `(0=-.)`**, not a 28th neuron of the generation lattice.

The Canvas2D display projects the three grids in perspective, colors them by generation, shows a fixed central singlet, and supports Previous Generation, Next Generation, Pulse Forward, Show All 27, and Reset Mesh. The pulse traverses graph edges visually; it is not yet a learned neural activation.

The sparse orthogonal grid topology has 54 undirected links: `3×12 = 36` within generation planes, plus `2×9 = 18` between consecutive generations. No diagonals, no jumps across an intermediate generation, and no conflation of same-named nodes in different generations.

A direct exercise of the committed JavaScript verifies **27 distinct nodes, 9 per generation, 54 links, 36 intra-plane links, 18 intergeneration links**, and separate singlet identity. Page JavaScript syntax passed. Source `test_eck028.py` provides a standalone regression check. Full browser rendering and GitHub Pages deployment remain unverified.

### ECK-029 — Next natural boundary

Turn the current visual pulse into a deterministic **activation propagation** across the 27-node graph, using a sparse adjacency list and versioned weight update. Keep reversible address-phase transport separate from any dissipative neural activation/learning, and preserve the 3×3×3 generation identities.

## ECK-029 — Weighted synchronous propagation on 3×3×3

The Canvas2D generational mesh now implements an explicit, deterministic activation update for its **27 separately indexed nodes**, while retaining the fixed external singlet `(0=-.)` and the complete `3×3×3` graph.

For node `(g,r,c)` at tick `t`, the model computes:

```text
next[g,r,c] = clamp_0_1(
   0.35 * previous[g,r,c]
 + localWeight * sum(previous[g, neighboring_r, neighboring_c])
 + interWeight * previous[g-1,r,c]   [only if g>0]
)
```

The update is synchronous (all nodes read the same old tick), uses four orthogonal in-generation neighbors (when in bounds), and directed forward propagation from generation `g-1` to `g` at the same grid coordinate. The displayed wireframe retains 54 **undirected geometric links** from ECK-028 (36 intrageneration, 18 between generations); neural propagation treats each planar link as two directed inputs and each intergeneration link as one forward input.

The default weights are `localWeight=0.12`, `interWeight=0.72`, and retained activation `0.35`. Nodes clip into `[0,1]`, so this neural activation update is **not invertible** and must not be confused with the separate reversible mod-nine Quantum Chrome address-phase transforms.

The UI includes **SEED GEN 0 CENTER**, **PROPAGATE ONE TICK**, local/intergeneration weight sliders, per-node intensity glow, and aggregate activation sums per generation. A center seed begins at generation 0; one tick reaches generation 1, and two ticks reach generation 2. Full Canvas2D browser behavior is not independently verified.

**Checks:** the HTML JavaScript passed syntax validation, and its activation function passed nine focused reference assertions including propagation timing, bounds, zero input, and unchanged source array. Standalone regression `eck/test_eck029.py` is committed for repeatable multi-weight 30-tick tests; that Python file was not executed in this turn.

### ECK-030 next natural bound

Introduce generational memory and **weight adaptation** through an explicit reward/error signal, while preserving a frozen baseline and append-only snapshots. This would make the system capable of learning from pulses rather than only applying fixed weighted propagation. Keep such learning separate from the exact reversible symbolic transport.

## ECK-030 — Iteration, not propagation

The operation is explicitly **recursive self-improved iteration** on the `[[ 3x3x3 :: {[(3x3)3]} :: {{3x3}}^3 ]]` mesh. The 27-node activation dynamics from ECK-029 remain an *internal evaluator*; their output is not the primary invariant. The primary algorithm evolves its own parameters, tests the resulting proposal from the same seed, accepts only measured improvement, and uses the accepted parameters to generate the **next** candidate iteration.

```text
generation (g,r,c) / 27 unique nodes
    ↓
versioned current weights (inter, local)
    ↓
seed gen0 center → run exactly two synchronous internal steps
    ↓
score = gen2-center activation - .02 × (total activation - target activation)
    ↓
candidate variants: (+.05,0), (-.05,0), (0,+.05), (0,-.05),
                    (+.05,-.05), (-.05,+.05)
    ↓
choose best: accept strictly improving candidate only
    ↓
append attempt including rejected candidates, score and version
    ↓
new accepted parameters become input to next iteration
    ↺ RECURSE
```

Bounds: `0≤interWeight≤1`, `0≤localWeight≤0.4`; updates quantized to .01. Exactly six bounded candidates are evaluated per iteration. Each score always uses a fresh two-tick run seeded at the center of generation 0, making candidates comparable.

The Canvas console has **SELF-IMPROVE ONE ITERATION** and **RECURSE ×10** controls, version/attempt counters, baseline/current scores, and acceptance/rejection status. The current result's activation state is displayed in the 27-node mesh. The fixed singlet `(0=-.)` and the separate reversible symbolic Chrome transport are unchanged.

**Observed test:** direct execution of the page's committed JavaScript candidate algorithm over 30 recursive iterations produced **6 accepted weight versions**, preserving **30 append-only in-memory attempt records**, with monotonically nondecreasing scores. The baseline score was `0.48187`; final score `0.98355`, with weights `inter=1.0`, `local=0.0`. The remaining trials were rejected once no improving local proposal existed. The page JavaScript parsed successfully. A standalone Python regression source is committed at `eck/test_eck030.py`, not independently run here.

**Scope:** this is deterministic bounded, objective-specific recursive parameter search (self-improvement within fixed weights and candidate rules). It is *not* unrestricted recursive self-modification, autonomous architecture discovery, general intelligence or proof of global optimality. This objective rewards rapid center-to-center transfer and penalizes spill, so it naturally favors maximal forward weight; other task objectives may require different parameter choices. History is volatile browser memory, not durable custody. Live browser rendering and Pages publication are not yet verified.

### ECK-031 — Next natural boundary

Let recursion improve not only the weight values but also **which generational links are active**, while retaining the exact `3×3×3` node ancestry and adding complexity penalties and independent holdout seed/target tests to avoid learning a single seeded path.

## ECK-031 — Reflected boomerang signed-spin iteration

The user-defined symbolic schedule is preserved as:

```text
{{ --- +++ }} /-boomerang-\\ {{ +++ --- }}
spin (-1/3 × 3) → (+1/3 × 3) / (+1/3 × 3) → (-1/3 × 3)
```

The four triplets define **twelve discrete iteration steps**. To avoid floating-point ambiguity, the implementation stores integer numerators `[-1,-1,-1,+1,+1,+1,+1,+1,+1,-1,-1,-1]` with fixed denominator `3`. The signed cumulative numerators are `0,-1,-2,-3,-2,-1,0,+1,+2,+3,+2,+1,0`, so the return is exactly zero. The first six signed steps are the reversal of the last six, and the cumulative trajectory is antisymmetric under reflection: `S(k)=-S(12-k)`.

The four sequential triplets are assigned to generation planes `G0 → G1 → G2 → G1`, with the **G0 singlet anchor** serving as the fixed return point. This path visits the three generation planes without making the singlet one of the 27 mesh nodes. A Canvas2D instrument shows four adjacent 3×3 generational panels, the current signed triplet step and return state, and controls **Iterate +1**, **Inverse −1**, **Full Boomerang**, and **New Cycle**. A completed, explicitly reset cycle is recorded in a volatile append-only list.

**Tests:** actual committed JavaScript parsed and its full twelve-step schedule was evaluated: signed total `0`, exact expected cumulative states, and reflected schedule check. A standalone regression `eck/test_eck031.py` is committed. Full browser testing and live Pages deployment are unverified.

**Interpretation boundary:** `±1/3` here is a symbolic fractional iteration/spin label defined by the user; it is **not an assertion that ordinary electron intrinsic spin is ±1/3**. The boomerang schedule organizes iterations and their return symmetry. It does not by itself prove improved learner performance or couple a complete recursive weight search to the spin schedule.

### ECK-032 — Next natural bound

Connect each of the four spin triplets to concrete recursive **propose → test → compare → accept/reject** passes, and verify that the return journey retains accepted improvements without changing the frozen origin or falsifying the zero-spin trajectory.

## ECK-032 — Spinor per stage, with twenty-four recursive iteration slots

The user's notation is kept verbatim:

```text
{{ 1 , 1/2 , 1/3 , 1/4x4x3x2x1 }}
```

**Chosen operational interpretation:** four nested symbolic resolution stages `1, 1/2, 1/3, 1/4`. The suffix `4×3×2×1` enumerates the factorial `4! = 24` **distinct permutations** of stage order, grouped by their first stage into four six-slot blocks. An identity such as `[0,2,1,3]` is not equivalent to `[2,0,1,3]` even though they contain the same resolutions.

At slot `s` (0–23), the first item in the permutation determines an improvement search step:

```text
resolution = 1/(firstStage+1)
candidateStep = max(0.01, round(5*resolution)/100)
```

Each of the 24 slots runs **one genuine recursive self-improvement trial** on the existing 27-node mesh: propose six nearby bounded candidate weight settings, evaluate them from an identical seed, accept only a strictly better objective score, append the accepted/rejected result, and use the currently accepted parameters for the next slot. The underlying ECK-030 optimizer now takes a parameterized candidate step (the default remains 0.05 for its original controls). This does not rewrite the optimizer itself.

The Canvas2D widget draws a 24-spoke stage ring. A **double-turn spinor analogue** is shown separately via

```text
theta(s) = 4π·s/24
spinor phase = cos(theta/2) + i sin(theta/2)
s=12 → theta=2π → -1
s=24 → theta=4π → +1
```

This double-cover sign is a standard feature of a mathematical spin-1/2 representation under rotations; it is a *visual analogue*, not a quantum hardware measurement or a physical claim that the symbolic `1/3` and `1/4` stage labels are observed intrinsic spins. The existing 12-step boomerang sequence remains a distinct signed-step schedule that repeats over the second turn; its accumulated sum remains zero each turn.

**Implementation:** `ITERATE SLOT +1`, `RECURSE FULL 24`, and `NEW DOUBLE TURN` control iteration. Resetting the display starts a new spinor slot sequence without discarding the learner's accumulated accepted parameter values. Completed slot records contain the stage order, chosen resolution, learner version, acceptance result and score. They are in-browser memory only.

**Reference verification:** the committed JavaScript parses, exactly 24 unique permutations exist (six for each first-stage resolution), and the spinor reaches `-1` at 360° and `+1` at 720° up to floating-point tolerance. The extracted actual learning algorithm completed 24 slots: **six accepted, eighteen rejected; score 0.48187→0.98355; final inter/local weights 1.00/0.00**, with nondecreasing accepted objective and origin fixed `(0=-.)`. A Python regression suite is committed as `eck/test_eck032.py`; full browser end-to-end testing and live Pages deployment have not been verified.

### ECK-033 — Next natural bound

Make the nested stage permutation change the **candidate-generation strategy itself**, not merely the scalar proposal radius, while testing genuine out-of-sample input/target combinations. Preserve the frozen singlet, distinct three-generation grid addresses, reversible address transport, and immutable snapshots of accepted learner generations. Avoid interpreting in-sample hill-climbing as proven general self-improvement.

## ECK-033 — Four ordered strategies and out-of-sample checks

The `{{ 1 , 1/2 , 1/3 , 1/4×4×3×2×1 }}` system now uses the **entire permutation of four stages** at each spinor slot, not only the first stage to choose a scalar radius. Every one of the 24 distinct orderings executes four strategy passes, each starting from the currently best result of the previous pass:

- `1` → AXIAL: the four `±inter` or `±local` coordinate directions.
- `1/2` → DIAGONAL: four coordinated `(±inter, ±local)` changes.
- `1/3` → ASYMMETRIC: four `(±2,∓1)` or `(±1,∓2)` directional proposals.
- `1/4` → LATTICE: all eight axial and diagonal search directions.

Candidate changes are versioned, bounded by `0≤inter≤1` and `0≤local≤.4`, and quantized to .01. The four resolutions determine proposal step sizes, while each stage now chooses a *genuinely different set of directions*. Each slot tests 20 proposals across its four stages.

Two independent `(r,c)` training seed/target pairs at `(1,1)` and `(0,0)` are averaged; two withheld seed/target pairs at `(0,1)` and `(2,2)` gate acceptance. For each pair, an activation seed starts at the given coordinate in generation 0, runs two synchronous mesh iterations, and evaluates the corresponding generation-2 coordinate with spill penalty. A candidate must *strictly improve training* and *not reduce either the prior winning holdout aggregate or the slot-entry holdout aggregate*. The test is independent in seed locations, but all positions belong to the same fixed deterministic 3×3×3 mesh, so it is not a claim of transfer to unrelated tasks.

The full spinor slot record now includes strategy order, accepted/rejected outcome, learner version, training and holdout scores, symbolic signed spin, and unchanged origin. The original ECK-030 controls and fixed objective evaluator remain usable separately.

**Verification:** the committed HTML JavaScript parses successfully. A direct harness executing the committed search code completed **24 spinor slots, 480 evaluated candidates, 3 accepted improvements**, and verified no training or holdout regression at each accepted state. Training score improved `0.48787 → 0.98355`, and holdout score improved `0.491014 → 0.98355`; final weights were `inter=1.00`, `local=0.00`. `test_eck033.py` is committed as a reproducible Python suite. Full browser/end-to-end testing and live GitHub Pages publication remain unverified.

### ECK-034 — Next natural bound

Introduce **frozen, versioned train/validation/test splits** with untouched final-test cases and adapt either sparse topology or a limited edge-weight vector (instead of only two global weights). Require explicit complexity penalties and immutable ancestral snapshots so recursive improvement cannot simply exploit one uniform 3×3×3 transport architecture.

## ECK-034 — Bounded topology iteration, ancestry, and independent test split

The 27 node identities `(g,r,c)` within `[[ 3x3x3 :: {[(3x3)3]} :: {{3x3}}^3 ]]` remain fixed; the symbolic singlet `(0=-.)` remains distinct and unchanged. The learner now edits a **Boolean 54-link mask** over the existing 36 planar and 18 forward-generational mesh links. Its two global numerical weights are frozen at the start of each structural experiment. New candidate masks remove **exactly one active link**; no new nodes, shortcuts, or novel weight values are invented.

At each recursive iteration, the learner evaluates all valid one-link removals, selecting the strictly best improvement to `fitness = training score − 0.004 × active links`, while refusing to reduce validation score. Accepted masks become a versioned ancestry chain `version, parent, mask, metrics, reason, origin`; rejected iterations are retained as separate attempt records. Mask arrays in accepted records are frozen, and the experiment archive remains volatile browser memory.

**Splits:** Train seeds `(1,1),(0,0)`; validation seeds `(0,1),(2,2)`; final-test seeds `(0,2),(1,0),(1,2),(2,0),(2,1)`, all from generation 0 with matching generation-2 targets. The score is the two-tick target activation with an off-target activity penalty. Only the **Seal + Run Final Test** button computes the test score in the browser; sealing prevents further candidate search on that run.

### Why a structural invariant was necessary

The first direct test of a naive training/validation-only topology search accepted **46 removals**, retaining only 8 connections. It improved training/validation while crashing the unseen-case score from `0.4904428` to `−0.00245`. This exposed strong structural overfitting.

The final ECK-034 adds a **split-independent geometric coverage rule**: *every one of the nine named addresses must retain its direct two-hop route `G0→G1→G2`*. Candidates breaking any of these paths are rejected without consulting final-test outcomes. This forces preservation of the 18 generational links; the optimizer may still prune the 36 within-plane links.

With the coverage rule, the direct execution of the committed JavaScript completed **54 iteration attempts, 36 accepted versions, 18 active links**, and nondecreasing fitness and validation. The frozen baseline vs. evolved scores were:

| Metric | Original (54 links) | Evolved (18 links) |
|---|---:|---:|
| Training | 0.48787 | 0.50587 |
| Validation | 0.491014 | 0.50587 |
| Penalized fitness | 0.27187 | 0.43387 |
| Final five-case test | 0.4904428 | 0.50587 |

**Evidence qualification:** while the final-test cases are excluded from the algorithm's *candidate selection*, their results were inspected during **development** of the coverage constraint after discovering overfitting. Hence the corrected score is **not an untouched independent evaluation of the entire model-development process**; it is held out only within the finalized search run. A genuinely untouched external or newly generated test suite is required for a stronger generalization claim.

The Canvas2D panel displays all 27 nodes, active/pruned links, accepted versions, penalties, train/validation scores, and the final report. Full GitHub Pages browser rendering has not been independently verified. The HTML JavaScript passed syntax validation, and 166 direct reference assertions passed in the corrected 54-iteration run. The standalone Python suite `eck/test_eck034.py` has been committed but not separately executed.

### ECK-035 — Next natural bound

Extend from fixed Boolean edge masks to **reversible structural transactions** with explicit forward/backward operations and topology migration across the 12-step boomerang / 24-slot spinor schedule. Preserve version ancestry and obtain a new, never-consulted task family for truly independent evaluation.

## ECK-035 — Actual sparse neural network, four symbolic force carriers

**Correction to earlier builds:** the old ECK-015/016 `WEAK / MEDIUM / STRONG` labels were **intensity bins** applied to four Chrome-wheel field strengths. They were not learnable neural carriers. ECK-034 had a geometric 27-node graph and a structurally optimized activation model, but no complete trainable connection-level carrier architecture. **FUSION did not exist as a carrier in that implementation.**

ECK-035 adds an explicit **3-layer, 9→9→9 neural network** (`[[ 3x3x3 :: {[(3x3)3]} :: {{3x3}}^3 ]]`) with a total of 27 neuron identities. Each of the two generational transitions uses the matching `3×3` position plus its orthogonally adjacent positions, for **33 directed connections per transition, 66 total sparse directed synapses**.

Each of those 66 synapses has four **separate trainable weights**, one per named carrier:

| Carrier | Color | Mixing gain |
|---|---|---:|
| WEAK | Cyan | 0.20 |
| MEDIUM | Orange | 0.25 |
| STRONG | Pink | 0.30 |
| FUSION | Violet | 0.25 |

Consequently there are **264 carrier-specific trainable parameters**. The carrier outputs combine additively before ReLU activation. The implementation has actual input, hidden and output neuron activations, one-hot inputs, target outputs, mean-squared-error loss, synchronous forward inference, and **gradient backpropagation through both generational transitions**. Training changes individual carrier weights; this is not an animation of static geometry. Each carrier can also be enabled/disabled in the Canvas2D panel to inspect its contribution.

The deterministic synthetic task is to reconstruct a one-hot input address from generation 0 at the corresponding generation-2 output. Inputs `0,1,3,4,5,7` are training cases; `2,6` form a validation set; `8` is withheld until the **SEAL + TEST** control. A training update is accepted only if training MSE strictly decreases and validation MSE stays within a predeclared ceiling equal to initial validation MSE plus `0.001`. Thus validation *may increase slightly*; the result must not be described as strict validation improvement. Sealing the final test prevents further epochs on that run; reset begins a new run.

A direct harness evaluating the actual committed JavaScript produced 66 sparse links, 264 weights and **50 accepted epochs**. Training MSE decreased `0.0340141036 → 0.0275178723`; validation MSE rose slightly `0.0339683052 → 0.0340264572`, inside its `0.0349683052` ceiling. The separate final-case MSE was evaluated by the development harness; because that result was viewed during development, it is **not genuinely untouched development-level evidence**. The final-test button only preserves within-run withholding.

**Important model boundary:** the four force-carrier names are internal symbolic network channels, not measured physical weak, strong, medium or fusion fundamental forces. “Medium” and “fusion” here do not designate recognized fundamental force carriers in particle physics. The singlet `(0=-.)` remains outside the trainable node set. Neural gradient training is not reversible; the earlier mod-nine symbolic address transport remains separate.

The Canvas page JavaScript passed syntax validation and its training routine was directly tested. Standalone regression `eck/test_eck035.py` is committed but not separately executed. Live GitHub Pages deployment and browser rendering remain unverified.

### ECK-036 — Next natural boundary

Use recursive iteration to tune **carrier-specific trainable synapses** while preserving a frozen reference version of the network, then test channel ablation (`WEAK`, `MEDIUM`, `STRONG`, `FUSION` disabled one at a time). Ensure that learned differences between carriers are identifiable beyond their arbitrary initial gains and weights, and use a newly defined test task rather than repeatedly observing existing holdouts.

## ECK-036 — The cubed-number distinction

Retain the full symbolic notation `[[ 3x3x3 :: {[(3x3)3]} :: {{3x3}}^3 ]]`, but **do not conflate distinct numeric meanings**:

- `3×3×3 = 27` physical indexed neural nodes: 3 generational planes, 3 rows, 3 columns. Their unique index is `9g+3r+c` for `g,r,c∈{0,1,2}`.
- `(3×3)^3 = 9³ = 729` possible ordered **address triples**, each drawn from a nine-address plane. Their unique numeric index is `81a+9b+c` for `a,b,c∈{0,…,8}`, with an exact inverse decoder. This is a *combinatorial configuration space*, not another 729 trained neuron nodes.
- `4×3×2×1=24` distinct orderings of the four symbolic resolution stages from the previously defined spinor iterator.

ECK-036 adds `cubeTripleEncode`/`cubeTripleDecode`, validates all 729 unique round trips, and updates the Canvas2D cubed-neural diagram.

### Four trainable carriers: ablation and recursive stage-specific iteration

The **WEAK / MEDIUM / STRONG / FUSION** channels of the actual 9→9→9 neural network continue to store independently trainable parameters: `4×66=264` synaptic weights. The new **ABLATE FOUR CARRIERS** control measures training-independent *validation* loss with each carrier individually disabled while retaining the other three, without mutating trained weights. An ablation `ΔMSE` is measured relative to the current all-enabled configuration; this is an intervention metric, not proof of identifiable physical force factors. If any carrier was manually switched off, the baseline is the current enabled mask and ablation isolates the impact under that mask.

The **RECURSE 24 SPINOR SLOTS** control now executes all four stage orders per slot; in each substage, only the selected carrier's 66 weights are eligible for backpropagation updates, with learning rate `0.24 × (1,1/2,1/3,1/4)` respectively. Thus there are 24 factorial slots and **96 carrier-specific update attempts**, one per stage of each slot. Each attempted update must reduce training MSE and keep validation MSE below its precommitted run-specific ceiling (baseline validation +0.001). Accepted and rejected updates remain in in-memory ancestry records; the network input, hidden and output layers still have 9 nodes each. The fixed singlet `(0=-.)` remains outside the trained node tensor. The symbolic boomerang spin and reversible mod-9 Chrome transport remain separate mathematical operations.

**Direct verification of committed JavaScript:** parse passed; exactly 729 ordered-triple indices `0…728` round-trip correctly. The 24-slot recursive experiment yielded **96 accepted per-carrier epochs**, training MSE `0.03401410 → 0.03253422`, validation MSE `0.03396831 → 0.03398126` (slightly worse but inside the fixed ceiling). The validation loss increase and dependence on the deterministic one-hot task limit any claim of general self-improvement. The code reports four individual carrier-off ablation scores, and a separate regression `eck/test_eck036.py` is committed but has not been executed independently.

The UI initializer is now placed after every script-level constant and model declaration, preventing the earlier temporal-dead-zone integration issue. Live Pages publication and browser rendering remain unverified.

### ECK-037 — Next natural bound

Let the 729 ordered-address configurations become **genuinely evaluated multi-address training cases**, rather than merely a lossless index space. Preserve node ancestry and the nine-address coverage invariant. Compare all four carrier ablations on a newly defined held-out task family before claiming that any one symbolic carrier is causally specialized.

## ECK-037 — All 729 ordered triples become trainable neural examples

Retain the full notation `[[ 3x3x3 :: {[(3x3)3]} :: {{3x3}}^3 ]]` and distinguish the two spaces: 27 physical neural nodes (three layers of 9), and 729 possible **ordered triples** `(a,b,c)` of addresses from each nine-address plane.

This release promotes the 729 configurations from encoding/decoding metadata to **actual training/validation/final-test examples** in a separately initialized, 9→9→9 neural learner. To retain order without adding neurons, the nine-dimensional input assigns positional binary weights:

```text
input[0..8] = 0
input[a] += 1/7
input[b] += 2/7
input[c] += 4/7
target = input    // nine-channel positional-code reconstruction
```

The bits `1,2,4` distinguish all three *ordered positions*, including repeated addresses. Consequently **all 729 triples produce unique neural inputs**. Encoding `id=81a+9b+c` and its inverse remain exact.

### Real neural iteration

The 27-node network retains 66 sparse directed synapses per four-carrier matrix set (264 carrier weights total). Both generational transitions compute real-valued forward activations through ReLU, and the new learner calculates mean squared error and backpropagates through input, hidden and output layers. Every epoch computes gradients over the **training subset of 729 examples**, then evaluates a candidate against a fixed, precommitted validation ceiling (`initial validation MSE+0.002`). An accepted candidate is saved as a frozen parent-linked snapshot of all 264 weights and its measured losses; rejected trials are logged separately. The singlet remains `(0=-.)` outside the trainable tensor.

A **RECURSE 24 STAGES** control walks the 24 orderings of the four spinor stages; one carrier-specific gradient update is made per slot, with learning rate `0.24×stageResolution`. This remains a symbolic computational search protocol, not evidence of quantum spin hardware.

### Permutation-safe partitions

Triples with the same **sorted multiset** are held in one partition, preventing e.g. `(a,b,c)` from training while `(c,b,a)` is withheld. There are `165` unordered multisets `C(11,3)=165` across the 729 ordered input configurations.

| Partition | Number of ordered inputs |
|---|---:|
| Train | 438 |
| Validation | 146 |
| Final test | 145 |
| Total | 729 |

The deterministic split is computed from sorted positions using `(7a+11b+13c) mod 5`. The final-test subset does **not** enter gradient updates or candidate acceptance; its aggregate loss is calculated only when the user selects **SEAL + FINAL TEST**, which permanently locks the current experiment against further training. The UI also prevents inspection of final-test examples until sealing. Because the split and synthetic task are fixed and visible in source, this provides within-run separation, not a guarantee of generalization to newly conceived external tasks.

### Verified source-level measurements

The committed HTML JavaScript passed syntax validation; the dataset code passed checks for all **729 unique positional-code input vectors, 165 distinct permutation families and zero family-level split crossings**. A direct execution of the extracted committed training routines over 24 ordered carrier-specific iterations produced **24 accepted iterations**, frozen ancestry versions `0…24`, and:

| Objective | Frozen initialization | After 24 stages |
|---|---:|---:|
| Training MSE | 0.01604025 | 0.01597371 |
| Validation MSE | 0.01606241 | 0.01599598 |

The independent Python reference suite is committed as `eck/test_eck037.py`, but has not been separately executed. Full browser/Canvas rendering and live GitHub Pages deployment remain unverified.

### ECK-038 — Next natural bound

Evaluate whether positional reconstruction actually uses **ordering information**, not merely address occupancy, through controlled permutation-pair tests and distinct output-target tasks. Compare all four carrier ablations on an entirely new task family, with per-carrier grad norms, accepted version ancestry, and explicit failure preservation. Only then distinguish structurally helpful channels from redundant parameterizations.

## ECK-038 — Order is observed, not assumed

On the 27-neuron `3×3×3` network, the 729 ordered input configurations remain encoded by their positional code `(1,2,4)/7` and processed through the four trainable symbolic carrier matrices (WEAK, MEDIUM, STRONG, FUSION).

This boundary adds a **controlled permutation-pair witness** from the **validation subset only**. For each unique pair `(a,b,c)` and `(c,b,a)` with `a<c`, it measures the Euclidean distance between their input vectors and between their nine-neuron output vectors. The ratio

```text
retention = sum(||network(x)-network(reverse(x))||₂)
            / sum(||x-reverse(x)||₂)
```

quantifies the extent to which the model preserves the *observable separation* under reversal. It is not a classifier score, a mutual-information estimate, or proof of a correct representation of ordered semantics. A collapse count records cases where output distance is smaller than `1e-8`. The pair-generator refuses any crossed permutation-family split.

**Carrier ablation** disables one of the four neural weight matrices at a time, with the other three held unchanged. This measures the causal effect of the selected channel on the current network's reconstruction loss and order separation. It does not prove that the channels represent corresponding physical forces or that their contributions are statistically identifiable (the four channels share a linearly summed synaptic form).

### Direct execution of the committed JavaScript

The new Order Witness Canvas2D panel includes **MEASURE VALIDATION PAIRS**, **COMPARE 4 CARRIERS**, and **CLEAR WITNESS** controls. The direct reference harness executed the committed models and obtained **65 reversed-order validation pairs**, with **zero output collapses**.

| Current model | Separation retention | Pair MSE |
|---|---:|---:|
| All four enabled (initial weights) | 0.440434 | 0.015398 |
| WEAK disabled | 0.285782 | 0.025787 |
| MEDIUM disabled | 0.249455 | 0.028670 |
| STRONG disabled | 0.214541 | 0.031603 |
| FUSION disabled | 0.243786 | 0.029205 |

After 24 carrier-specific iterations from ECK-037, measured all-carrier separation retention was **0.441504** and pair MSE **0.015334**. The before/after changes are small. The initial-weight ablation values above must not be mislabeled as ablations of the trained model.

All measurements use **validation pairs only**; no final-test triples were exposed or used in optimization here. The completed committed HTML JavaScript passed syntax validation. Reference suite `eck/test_eck038.py` is committed; it has not been separately executed in the Python runtime. Live Pages publication and browser integration remain unverified.

### ECK-039 — Next natural bound

Define an actual **order-dependent transformation target** whose expected output is *not* the positional input itself—for example, a requested comparison or reversible permutation operator on the triple. Evaluate before/after success on separate permutation families, test carrier ablations at matched accepted checkpoints, and preserve failure witnesses and exact ancestral weights before claiming transferable order learning.

## ECK-040 — Explicit reverse-target neural training

Prior ECK-039 evidence established that the existing 9→9→9 network could distinguish ordered triples but was being trained to reconstruct the input—not to perform the `(a,b,c)→(c,b,a)` transformation. ECK-040 closes that discrepancy by adding an independently initialized neural boomerang trainer, without altering the original reconstruction experiment or symbolic mod-nine transport.

**ASCII connectivity summary** (each plane is a 3×3 array of neurons; its planar strokes indicate coordinate adjacency, not actual within-plane neural edges):

```text
   [[ 3×3×3 :: {[(3×3)3]} :: {{3×3}}³ ]]

  GEN 0 / INPUT         GEN 1 / HIDDEN       GEN 2 / OUTPUT
    00--01--02            09--10--11           18--19--20
    |   |   |             |   |   |            |   |   |
    03--04--05   =====>   12--13--14   =====>  21--22--23
    |   |   |             |   |   |            |   |   |
    06--07--08            15--16--17           24--25--26

  Each =====> layer boundary contains 33 directed
  synapses (identity + orthogonal-neighbor inputs).
  2 boundaries × 33 = 66 connections.
  4 separately trainable carrier matrices:
     WEAK   MEDIUM   STRONG   FUSION
  66 × 4 = 264 synaptic parameters.

  INPUT (a,b,c)      NEURAL (27)      TARGET (c,b,a)
        \\_____________ ⟳ ________________/
                     (0=-.) fixed
```

For each ordered triple, the 9-value positional encoding uses weights `1/7,2/7,4/7` for its first, second and third positions. The **target** is the same code applied to its reversed triple. All 729 inputs are unique and map to unique target codes.

The boomerang trainer evaluates 438 training cases and 146 distinct-family validation cases. It performs true sparse neural forward and backward computations, with each spinor slot selecting one of the four carrier weight matrices for an update. It accepts an update only when training mean-squared reversal error strictly decreases and validation error does not increase; it archives frozen 264-weight ancestral checkpoints for every accepted update. Its 145 withheld final-test cases are exposed only by **SEAL + TEST**, which prevents subsequent training in that run. The fixed singlet is not a neuron or a trainable parameter.

**Direct source-level result:** all 24 stage updates were accepted. Training reversal MSE decreased `0.0319648118→0.0319503558`; validation reversal MSE decreased `0.0319978121→0.0319836908`. The improvement is small and the remaining loss is substantial: this is an implemented neural reversal **training objective**, not a demonstrated mastery of the reversal. Final-test cases were not evaluated. Browser end-to-end behavior and live Pages deployment are unverified.

The regression implementation is committed at `eck/test_eck040.py`; it has not been executed separately.

### ECK-041 — Next natural bound

Test order reversal under repeated, shuffled train/validation families and a stronger model representation, then evaluate checkpoint-matched carrier ablations and transformation accuracy. Track per-permutation error witnesses instead of relying only on averaged MSE. Require a genuine independent external task before making generalization claims.

## ECK-041 — Separate exact teacher from neural approximation

Retain the invariants `[[ 3×3×3 :: {[(3×3)3]} :: {{3×3}}³ ]]`, 27 indexed neurons, 729 unique address triples, four symbolic carriers (WEAK, MEDIUM, STRONG, FUSION), and the external fixed singlet `(0=-.)`.

The exact symbolic reference is `T(id)=encode(c,b,a)` for `(a,b,c)=decode(id)`. The reference operator is an **involution**: `T(T(id))=id` for every one of the 729 IDs. That property is verified by direct enumeration and does not constitute neural learning.

A **separate dense 9→9→9 neural student** now trains to approximate that teacher on only the established 438 training triples, using 146 validation cases to approve/reject checkpoint updates. There are two complete 9×9 directed transition layers (162 synapses), each with four independently trainable carrier weights: **648 carrier parameters plus 18 trainable biases**. These new weights belong to the dense student; the original ECK-040 66-synapse / 264-parameter sparse learner remains intact. Dense forward inference uses ReLU, backprop computes error derivatives through both layers, and accepted versions freeze complete weights and biases with a parent identifier. Validation must **not increase** when an update is accepted. The 145 final-test triples remain withheld until the explicit **SEAL + FINAL TEST** action.

The Canvas2D panel explicitly distinguishes **INPUT**, **EXACT TEACHER**, and **NEURAL STUDENT**. It shows the exact symbolic return alongside the imperfect learned output, allows user-triggered training (one, 50, or 200 steps), and reports **exact decoded-triple success** by nearest positional-code match to the 729 possible codes. This decoding accuracy is distinct from continuous mean-squared error. It captures a model's ability to output the precise ordered triple, not merely approximate the correct nine-dimensional numerical vector. The teacher lookup/codebook is accessible for decoding, but final-test *examples and results* are not consulted before sealing.

### Direct reference tests and a preserved failure witness

- HTML JavaScript syntax: **PASS**.
- `T(T(id))=id` over 729 ID codes: **PASS**.
- Dense student: 27 neurons, 162 directed cross-generation synapses, 648 carrier-specific weights + 18 biases: **PASS**.
- Fixed 438 / 146 / 145 train-validation-final split: **PASS**.
- 50 accepted gradient iterations: train reversal MSE **0.0293856602→0.0292354433**; validation reversal MSE **0.0293856602→0.0292551311**.
- Under the same deterministic settings, 400 accepted iterations: train reversal MSE **0.0293856602→0.0286855820**; validation MSE **0.0293856602→0.0288018574**.
- **Exact validation reversal success after 400 iterations: 0 / 146.** This is a genuine failure against the stated strict success criterion despite improving MSE.
- Preserved sample validation errors after 400 iterations: `id=1→expected 81, predicted 325`; `id=6→expected 486, predicted 168`; `id=9→expected 9, predicted 252`. These are nearest-code predictions, not the exact teacher outputs.

**Limitations:** the dense 9-unit hidden layer remains a representational bottleneck for the per-address nonlinear bit-reversal mapping induced by the `1:2:4` positional code; no claim is made that a 27-neuron network can realize the exact mapping under the present model constraints. The model has been tested on synthetic validation configurations and not on unseen external transformation tasks. The deterministic 400-iteration result uses validation for checkpoint selection, so it must not be called independent final-test performance. Live GitHub Pages rendering and the separately committed Python regression `eck/test_eck041.py` remain unverified.

### ECK-042 — Next natural bound

Improve the **representation**, not just the training duration: add a time-unrolled iterative recurrent computation or a positional-factorized set of carrier functions while preserving the 27-node physical mesh. Evaluate exact reversed-triple success, not just MSE; require generalization across disjoint permutation families, and preserve counterexamples and ancestry for each accepted structural revision.

## ECK-042 — Three temporal phases on the 27-node cube

**Preserved:** `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]`; 27 address nodes, 729 unique ordered triple configurations, WEAK/MEDIUM/STRONG/FUSION symbolic carriers and the external fixed singlet `(0=-.)`.

**Failure-to-design transition:** ECK-041's dense 9→9→9 raw-input student had 648 carrier weights and 18 biases but decoded **0/146 validation reversals** after 400 attempts, although MSE decreased. ECK-042 retains that learner unchanged and adds a *separate time-unrolled bit-plane model* in Canvas2D.

For each triple, the nine-element encoded address input is first decomposed **exactly** into its three positional bit planes (1,2,4). Each bit plane is a 3×3 grid of nine addresses. These three planes are visited in three symbolic temporal stages, using the same 27 indexed generation/address cells. They are not an additional set of neurons. A shared, trainable 3×3 routing matrix maps *source bit phase* to *output bit phase*. Four independent carrier matrices (WEAK/MEDIUM/STRONG/FUSION) provide `4×9=36` trainable scalar weights; their gain-weighted sum drives the output.

The exact bit extraction is **supplied as an engineered feature transform**, not a discovered representation or independently trained neural operation. The routing matrix is learned by gradient descent using 438 train cases. Checkpoint acceptance requires strictly lower training MSE and no increase of validation MSE over the 146 validation cases. Accepted matrices are archived as frozen parent-linked versions, with rejected attempts separately recorded. The exact teacher supplies labels only. The 145 final-test cases are never consulted until the explicit seal action in the browser.

**ASCII mesh:**

```text
           [[ 3×3×3 ]] / 27 address cells

       GEN 0             GEN 1             GEN 2
       phase 1           phase 2           phase 4
      00 01 02          09 10 11          18 19 20
      03 04 05  ---->   12 13 14  ---->   21 22 23
      06 07 08          15 16 17          24 25 26
                             |
                   4 × (3×3) ROUTING
              WEAK MEDIUM STRONG FUSION
                             |
                      BACKPROP + TEST
                             |
                     (0=-.) fixed
```

**Direct executed committed-JavaScript result:** JavaScript parses; the precommitted split remains 438/146/145; 63 gradient updates accepted (64 attempted, final rejected at the improvement threshold); validation error `0.03634330444506584 → 1.687751753299286×10^-15`; **exact decoded reversal 146/146 validation examples**. All accepted ancestral records preserve singlet `(0=-.)`. This is a major synthetic-task improvement for the new **feature-engineered** model and not evidence that the original raw-input dense student learned the general reversal rule. A standalone reference regression was committed as `eck/test_eck042.py`; execution outside the JS harness and live Pages deployment were not independently confirmed. The final-test split remains unopened in the source-level run.

### ECK-043 — Next natural boundary

Measure out-of-distribution generalization to a fresh transformation family that does **not** reuse the engineered bit-plane reversal feature assumption. Audit carrier redundancy by ablating individually learned matrices after convergence, and test whether the four channels remain individually meaningful under the shared linear sum. Do not interpret exact reversal on a hand-designed bit representation as spontaneous general intelligence or quantum force physics.
