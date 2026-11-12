# ECK-031 — Boomerang Spin and Recursive Generational Iteration

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
