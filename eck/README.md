# ECK-059 — Independent Continuous-Phase Evaluation Surface

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

## ECK-043 — Reversal checkpoint vs fresh model on cyclic rotation

Extend the 27-node three-generation neural cube `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]` and 729 distinct ordered-address examples to a **different transformation objective**. The fixed 3-bit feature extraction and time-unrolled four-carrier matrix representation are retained from ECK-042.

- Reversal `R(a,b,c)=(c,b,a)` is order two: `R²=identity`.
- Cyclic rotation `C(a,b,c)=(b,c,a)` is order three: `C³=identity`.
- These are distinct **tasks on the same address distribution**, so this is *cross-task transfer*, not an independently unseen data distribution.
- Freeze a revision of the learned reversal routing matrices; train the rotation task twice from **warm reversal weights** and **fresh initial weights**, always using the same 438 training and 146 validation cases and withholding the 145 final-test cases until sealing.
- Candidate updates require decreasing training MSE without increasing validation MSE. Each accepted update archives a parent-linked immutable 4×9 carrier-weight snapshot; the fixed singlet `(0=-.)` is external to learned weights. The source reversal checkpoint is not overwritten.

The Canvas2D panel **CROSS-TASK NEURAL TRANSFER** provides **FREEZE REVERSAL CHECKPOINT**, **TRAIN BOTH ×100**, **ABLATE CARRIERS**, **TEST CARRIER EQUIVALENCE**, **SEAL + TEST**, and **NEW TRANSFER**. The user must first train the reversal route on the prior panel to obtain a learned checkpoint; otherwise the “warm” source may be an untrained initial version, which is reported by its version number.

### Direct source-model results

Using the committed JavaScript: (1) train the ECK-042 reversal model until saturation (63 accepted updates); (2) freeze version 63; (3) compare the two rotation initializations; (4) execute 63 paired rotation rounds (both runs stop when no further improvements are accepted). No final-test examples were evaluated in this run.

| Rotation validation | Warm reversal checkpoint | Fresh initialization |
|---|---:|---:|
| Initial exact decoded targets | 16/146 | 2/146 |
| Initial MSE | 0.0040381423 | 0.0282670146 |
| Final exact decoded targets | 146/146 | 146/146 |
| Final MSE | 2.14412e−15 | 2.13698e−15 |
| Accepted checkpoints | 58 | 62 |
| Total attempts | 63 | 63 |

The warm initialization starts substantially closer to the target and requires fewer **accepted revisions**, but both solve this engineered family. This is not evidence of unique carrier roles, generalized transfer to unrepresented tasks, or faster wall-clock training.

**Carrier ablation after training:** disabling any of the four weighted channels increases rotation validation MSE (positive loss delta). For the warm model, the deltas in WEAK/MEDIUM/STRONG/FUSION order were `0.00199181, 0.00337711, 0.00544011, 0.00337711`.

**Critical equivalence witness:** the four carrier outputs are summed linearly using gains `(0.20,0.25,0.30,0.25)`. Increasing the WEAK weight at one phase-matrix entry by `+0.10` and decreasing MEDIUM at that same entry by `−0.08` gives an *identical effective routing matrix* for all inputs. The direct JS validation check saw **zero maximum output difference** despite changed channel parameters. Hence the four carriers are **not separately identifiable** from output behavior in this architecture. Channel ablation establishes dependence on the chosen parameterization, not irreducible causal specialization.

The exact task algebra and carrier-equivalence checks have an accompanying Python suite `eck/test_eck043.py` (committed, not independently run). JavaScript syntax, actual training, ablation and equivalence were executed in an extracted source-level harness. Browser integration and live GitHub Pages deployment remain unverified.

### ECK-044 — Next natural bound

Remove the redundant linear-carrier factorization by giving carrier channels **non-interchangeable computations or constraints**: e.g. gated input selection, distinct temporal memory, sparse local routing, and fusion as a learned nonlinear interaction. Evaluate against a fresh order-dependent transformation, report exact accuracy and ablation *after retraining*, and require fresh held-out evidence before claiming genuine carrier specialization.

## ECK-044 — Four computationally different force-carrier channels

The previous ECK-043 established an identifiability problem: the four additive carrier matrices could trade weight contributions and leave all outputs unchanged. ECK-044 implements a **new diagnostic learner** that gives each named carrier a different operator over the 3×3×3 cubed-address structure.

For each of the 729 ordered address triples, exact 1:2:4 positional code extraction supplies three 3×3 Boolean planes, corresponding to the 27 indexed address/phase cells. The singlet `(0=-.)` remains external.

- **WEAK / LOCAL** computes a mean over orthogonally adjacent positions in the first bit plane (spatial neighborhood; boundaries have fewer neighbors).
- **MEDIUM / MEMORY** reads the middle positional bit plane (the carried intermediate temporal phase).
- **STRONG / ROUTE** reads the final positional bit plane at the current address (directed final-phase signal).
- **FUSION / NONLINEAR** computes the product of the first and final positional bits at an address (coincidence; not generally expressible as a single linear combination of the other three features).

A supervised diagnostic output is explicitly defined by `target = 0.20·WEAK + 0.20·MEDIUM + 0.20·STRONG + 0.40·FUSION`. The target is **engineered from these features on purpose**; it is not a naturally occurring external task or new science. Four scalar coefficients are trainable by full-batch gradient descent and accepted only when train MSE strictly decreases and validation MSE does not increase. The comparison learner has **Fusion disabled from the start, but retrains the other three coefficients** under the same train-validation gates. This is a real nonlinear-feature necessity experiment, not an ordinary frozen-weight ablation.

The user-facing **NEURAL FORCE CARRIER SPECIALIZATION** Canvas2D panel shows the four coefficients, train and validation losses for both trained models, a per-carrier intervention test, and an explicit seal before evaluating the existing 145 final-test examples. The split remains 438 train / 146 validation / 145 final test, with the 165 permutation families kept together. The run stores immutable coefficient snapshots with ancestry and preserves the external fixed singlet.

### Direct committed JavaScript results

The new diagnostic learner ran up to 600 iteration attempts from zero-initialized coefficients. The direct source harness obtained:

| Model | Accepted parameter revisions | Validation MSE |
|---|---:|---:|
| All four specialized carriers | 552 | 2.77764209×10⁻¹² |
| Fusion disabled, other carriers retrained | 144 | 0.00172769084 |

The learned all-carrier coefficients were approximately `(0.1999992, 0.2000001, 0.2000020, 0.3999840)`, converging to the deliberately constructed target. Fusion-off coefficients were approximately `(0.1868559, 0.2020002, 0.2450771, 0)`. Thus a retrained linear comparator did not fit this nonlinear diagnostic target. The final-test set remained unopened.

Individual frozen-model ablation deltas in validation MSE were approximately:
`WEAK 0.00176918`, `MEDIUM 0.00444445`, `STRONG 0.00444453`, `FUSION 0.00194823`. These interventions measure dependence on this learned representation; they are *not* independent identification of physical carrier forces.

**Crucial qualification:** this new ECK-044 four-feature diagnostic is **not the entire older 9→9→9 trained network**, nor does it establish that each operator has learned its features from raw sensory input. The 27 address cells and phase tensors are retained, but engineered feature transforms do much of the work. The coefficients are trained. A useful next stage would make the local, memory and nonlinear operators themselves adaptable and compare them against expressive nonlinear baselines on fresh tasks.

The implementation and regression live in `eck/index.html` and `eck/test_eck044.py`. Actual committed JavaScript syntax and direct model execution were checked. The standalone Python regression and browser deployment were not independently verified.

### ECK-045 — Next natural bound

Train nontrivial **per-address or per-time carrier parameters** rather than four scalar readout coefficients, while maintaining function-specific operators. Introduce task families with unseen interaction rules and compare to a generic nonlinear neural baseline; otherwise an engineered target matching an engineered architecture would exaggerate the evidence. Add gradient checks, retained failure witnesses and verified runtime tests.

## ECK-045 — Train the per-address carrier readouts

ECK-044 introduced distinct engineered operations for WEAK, MEDIUM, STRONG, and FUSION, but trained only one scalar readout coefficient per carrier. ECK-045 retains the 27 indexed 3×3×3 address cells, 729 ordered input triples, the fixed singlet `(0=-.)`, and the original models, while adding a **new 36-parameter address-adaptive carrier learner**. At each of the nine addresses it trains a separate coefficient for each of the four operator signals. This is not a learned convolution kernel or a learned feature extractor: the neighborhood/memory/phase/product features are still supplied by the model designer.

Its synthetic spatial-temporal pulse target is *predeclared*, with a location-dependent weight on the local and final-phase signals plus a fifth nonlinear interaction missing from the four-channel model. The training task is deliberately not an exact linear combination of four *shared* readouts, so the comparison can reveal the usefulness of address-specific parameters without implying unexplained intelligence.

The code compares three independent, trainable readouts:
- **ADAPTIVE FOUR:** 4 operators × 9 per-address coefficients = 36 trainable parameters.
- **SHARED FOUR:** the same operators with 4 globally shared coefficients.
- **NONLINEAR FIVE:** five globally shared coefficients, including the otherwise missing interaction. This is a nonlinear-*feature* reference, not a generic MLP.

Each model uses the same frozen permutation-family partition: 438 training examples and 146 validation examples; 145 final-test examples are excluded from training/validation and are only evaluated when **SEAL + FINAL TEST** is explicitly clicked. Each accepted gradient step strictly decreases training MSE and does not increase validation MSE. The checkpoint archives are immutable, parent linked, and include the singlet marker.

### Actual committed JavaScript checks

After up to **500 training rounds**, the extracted committed JavaScript reported:

| Model | Accepted updates | Validation MSE |
|---|---:|---:|
| Adaptive four (36 parameters) | 500 | 0.000127329053 |
| Shared four (4 parameters) | 407 | 0.000297661746 |
| Nonlinear five (5 parameters) | 417 | 0.000217746650 |

The adaptive readout fit this known synthetic task better, but it uses much greater parameter capacity. Therefore no parameter-matched superiority, autonomous operator invention, or broad transfer claim follows.

A five-coordinate gradient check directly compared analytic gradients with central finite differences (`eps = 1e-5`) at representative parameters from all four channels; the maximum absolute discrepancy was `4.8461×10^-13`, verifying the implemented gradient calculations to numerical precision at those sample points.

The new Canvas2D panel **ADAPTIVE CARRIER OPERATORS** shows training, validation, model comparisons, checkpoint counts and test sealing. The regression file `eck/test_eck045.py` was committed but has not been independently executed in Python. The HTML JavaScript passed a source syntax check, and the training and gradient tests used actual extracted committed functions. Full browser integration and GitHub Pages deployment have not been independently verified.

### ASCII mesh

```text
    [[ 3×3×3 :: {[(3×3)3]} :: {{3×3}}³ ]]
      GEN 0              GEN 1             GEN 2
     00 01 02           09 10 11          18 19 20
     03 04 05   ---->   12 13 14   ---->  21 22 23
     06 07 08           15 16 17          24 25 26
                         |
         WEAK / MEDIUM / STRONG / FUSION
             9 learned coefficients each
                         |
              COMPARE 36 / 4 / 5
                         |
                    (0=-.)
```

### ECK-046 — Next natural bound

Learn the **feature operators themselves** (e.g. per-address attention weights over spatial neighbors, temporal decay, directed phase gates, and trainable fusion inputs), not just their readouts. Use matched-capacity nonlinear baselines and a new held-out task to distinguish genuine learned operator adaptation from increased parameter count.

## ECK-046 — Train the internal operators, not only their outputs

The user-specified cubed geometry remains `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]`: 27 indexed spatial/temporal cells and 729 ordered address configurations, with the fixed, non-trainable singlet `(0=-.)`. The four names WEAK, MEDIUM, STRONG and FUSION remain symbolic computational channels—not Standard Model force assignments.

ECK-046 adds an **Operator Forge** instrument and a new trainable four-channel model over three 3×3 bit phases. Prior fixed inputs/labels and the 438 training / 146 validation / 145 final-test family-preserving split are unchanged.

### Actual trainable channel internals

- **WEAK:** 24 separate weights on directed valid orthogonal-neighbor links within one 3×3 address plane. Each edge's own coefficient learns the local readout.
- **MEDIUM:** 18 trainable temporal mixing coefficients, two per address, combining the first and intermediate positional bits.
- **STRONG:** 18 trainable route coefficients, two per address, combining the final positional bit with the local average of neighbors' final bits.
- **FUSION:** 27 trainable bilinear gate parameters, three per address. The nonlinear product of a learned first-bit gate with a learned mixture of second and third bits is differentiable and has manually implemented gradients.

Together: **24 + 18 + 18 + 27 = 87 learnable scalar parameters**. This new model is separate from the ECK-045 36-scalar adaptive readout and the earlier 648-weight dense neural student. The address/phase features and task are still **engineered inputs**. These parameters change each operator's internal computation, but this is not a demonstrated autonomous discovery of an entirely new architecture.

A bounded full-batch gradient update (learning rate 1.8; weights clamped to [-2,+2]) is accepted only if it strictly decreases 438-case training MSE and does not increase 146-case validation MSE. Immutable parent-linked snapshots preserve all 87 weights and record losses and singlet provenance; rejected attempts are tracked. A separate **SEAL + FINAL TEST** action locks the training run before exposing the 145 final cases.

### Direct source execution

The actual committed HTML JS was syntax-checked and its model/gradient code was executed directly in the JS harness. Results after 500 accepted updates:

| Measure | Before | After |
|---|---:|---:|
| Training MSE | 0.001630685966 | 0.000023518669 |
| Validation MSE | 0.001626881918 | 0.000024432244 |

- 24 valid directed-neighbor links.
- All 87 parameters accounted for: 24 / 18 / 18 / 27.
- The seven central finite-difference derivative checks (eps=1e-5) each passed; maximal absolute error **1.75673×10^-13**.
- 501 frozen ancestry versions (baseline plus 500 accepted changes); all carry `(0=-.)`.
- Final-test partition remained unopened.

This is a meaningful implementation improvement on a **known synthetic task**. It does not show a parameter-matched comparison against generic nonlinear networks, and the nonlinear fusion gates have their own non-identifiability issues (paired product factors can compensate for one another). Gradient accuracy and a lower MSE do not establish unique causal specializations or discovery of new physics.

The source is at `eck/index.html`; the standalone Python regression `eck/test_eck046.py` is committed but has not been independently executed. GitHub Pages deployment and browser Canvas2D interaction have not been independently verified.

### ASCII mesh

```text
       [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]
        GEN 0           GEN 1           GEN 2
       00 01 02        09 10 11        18 19 20
       03 04 05  --->  12 13 14  --->  21 22 23
       06 07 08        15 16 17        24 25 26
                         |
          WEAK  24 learned neighbor routes
          MEDIUM 18 learned temporal mixtures
          STRONG 18 learned phase routes
          FUSION 27 learned bilinear gates
                         |
                 87 parameters
                         |
            gradient → witness → freeze
                         |
                      (0=-.)
```

### ECK-047 — Next natural boundary

Test against **matched-capacity nonlinear baselines** and new tasks with different operator structure. Audit feature/gate identifiability with constructive parameter-compensation counterexamples, probe whether learned parameters survive input transformations, and test a fresh, explicitly sealed final partition only after committing the new evaluation rules.

## ECK-047 — Necessity versus identifiability

The cubed invariant is unchanged: `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]`, 27 indexed phase/address cells, 729 ordered configurations, four symbolic carrier operators and the fixed singlet `(0=-.)`.

ECK-047 adds a distinct **NECESSITY LAB** to the existing Canvas2D GitHub Pages console. It compares the existing ECK-046 **87-parameter structured operator Forge** (24 weak local edges, 18 medium temporal coefficients, 18 strong phase-route coefficients, 27 fusion bilinear gate factors) against a **generic 85-parameter tanh MLP** (5 derived input features × 12 hidden, 12 hidden biases, 12 output weights, 1 output bias = 85). The MLP sees a spatial-neighbor feature and three positional bits plus an additional near-neighbor final-bit feature, but does not receive a fixed Fusion coincidence product feature. Both models use the same predeclared ECK-045 spatial-temporal pulse target and identical 438 training / 146 validation / 145 sealed test configurations. This is a **matched-scale but not fully matched-compute or matched-features** comparison; neither model automatically discovers a raw sensory representation.

Both models learn real parameters from training-only gradients. Each step is accepted only when training MSE strictly decreases and validation MSE does not increase. MLP updates are archived in frozen, parent-linked snapshots; the Forge comparison weights are held in separate run state and its accepted/rejected per-step results are logged. Each run is sealed before evaluating its 145 final-test configurations.

**Executed directly from committed JavaScript:** after 100 paired optimization rounds (100 accepted for each), validation Forge MSE **0.001626881918 → 0.000109544400** and MLP MSE **0.022081270216 → 0.001331370863**. The Forge starts from a more favorable informed initialization, and the MLP is not shown to have converged after 100 epochs; this does **not establish an ultimate model advantage**. A five-coordinate central-difference gradient check of the MLP produced maximum absolute discrepancy **2.91646×10^-11**, checking two hidden weights, hidden bias, output weight and final bias.

### Constructive Fusion gate non-identifiability

Per address, the Fusion term is

```text
F = (w0 * bit0) * (w1 * bit1 + w2 * bit2)
```

Thus the compensated transformation `(w0,w1,w2) → (1.25w0, w1/1.25, w2/1.25)` gives exactly the same **effective computation** for any input, despite changed trainable gate values. The ECK-047 source-level validation check measured maximum prediction delta **5.551115123125783×10^-17** across its 146 validation configurations. This proves an internal scaling gauge ambiguity: the learned gate factors are not individually identifiable from outputs. The existence of non-identifiability must not be confused with lack of predictive usefulness.

**ASCII mesh:**

```text
  [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]

      GEN 0             GEN 1             GEN 2
     00 01 02          09 10 11          18 19 20
     03 04 05    ==>   12 13 14    ==>   21 22 23
     06 07 08          15 16 17          24 25 26

   WEAK:   24 directed local neighbors
   MEDIUM: 18 temporal mix parameters
   STRONG: 18 phase route parameters
   FUSION: 27 bilinear gate factors
                  |
        87-OPERATOR vs 85-MLP
                  |
        gradient / validation
                  |
          FUSION GAUGE AUDIT
                  |
                (0=-.)
```

Standalone Python regression `eck/test_eck047.py` records 729 algebraic compensation checks and parameter inventory (committed, not separately executed). Actual committed JavaScript passed syntax, training, gradient and gauge checks via direct extraction. The final-test cases remained unopened. Live Pages deployment and browser rendering have not been independently verified.

### ECK-048 — Next natural bound

Use a **fair learning-curve comparison** with standardized initializations, train all models until stable or a fixed computational budget, and test fresh shift tasks with different nonlinear interactions. Audit fusion-gauge invariance under parameter bounds and compare feature-matched baselines, not only similar parameter counts.

## ECK-048 — Matched update rounds and changed-target validation

Keep the nested `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]` topology (27 addressed cells), 729 ordered address configurations, symbolic WEAK / MEDIUM / STRONG / FUSION channels, append-only parent-linked neural checkpoint records and external singlet `(0=-.)`.

The new ECK-048 **Learning Curve and Task-Shift Audit** Canvas2D panel compares the existing **87-parameter structured Operator Forge** against the **85-parameter tanh MLP**. Both train on the original, predeclared synthetic spatial-temporal pulse target under the same 438 training examples, 146 validation examples and attempted-update count; the final 145 examples stay unopened. It records validation learning curves at baseline and every 25 rounds, and runs zero-shot evaluation against an **independently specified changed target** on the validation partition. The changed task reverses the address-dependent gradient, adjusts base mixing and replaces/adds coincidence interactions involving medium and strong phases; no changed-target labels are used for gradient updates.

### Deterministic 200-round results from the committed JavaScript

| Validation MSE | Structured 87 | Nonlinear MLP 85 |
|---|---:|---:|
| Source target at step 0 | 0.001626881918 | 0.022081270216 |
| Changed target at step 0 | 0.001606299769 | 0.019935606613 |
| Source target after 200 rounds | 0.000075132549 | 0.000856326862 |
| Zero-shot changed target after 200 rounds | 0.001371095990 | 0.001055284244 |

Both models received the same number of update opportunities. The structured Forge was more accurate on the source task; the nonlinear MLP had lower changed-task MSE. They differ in initialization, starting loss, engineered features, and computational cost, so **this is a controlled-budget observation but not a proof of architectural superiority** for either one. The changed target is synthetic and evaluated on the same input families, so this is *target shift*, not unseen-distribution generalization.

The Fusion bilinear compensation symmetry remains: scale each first multiplicative gate by 1.25 and divide both second-factor gate weights by 1.25. The output is invariant up to floating-point rounding. The control **CHECK FUSION GAUGE** evaluates this with validation inputs and retains the maximum discrepancy, without opening final-test cases.

The implementation is in `eck/index.html` with the regression `eck/test_eck048.py`. Source JavaScript syntax and the real 200-iteration source-model calculation were verified. The standalone Python regression, browser Canvas2D integration, and live Pages deployment have not been independently verified.

### ASCII neural mesh

```text
     [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]

       GEN 0           GEN 1           GEN 2
      00 01 02        09 10 11        18 19 20
      03 04 05  --->  12 13 14  --->  21 22 23
      06 07 08        15 16 17        24 25 26
                         |
         WEAK / MEDIUM / STRONG / FUSION
                         |
                 87-parameter FORGE
                         |
                  85-parameter MLP
                         |
                same training budget
                         |
              source / target-shift
                         |
                       (0=-.)
```

### ECK-049 — Next natural bound

Introduce independent external or generated-but-precommitted task families, training seeds, and a computational-cost audit. Normalize starting conditions where scientifically appropriate, separate *input distribution shift* from *target shift*, and compare full learning curves across multiple seeds rather than selecting a single favorable run. Keep the 145-case final-test seal intact until model choice is frozen.

## ECK-049 — Three reproducible starts; repeated-address vs distinct-address inputs

The cubed neural invariant is preserved: `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]`, 27 indexed address/phase cells, 729 ordered triple configurations, four symbolic carrier channels and external fixed singlet `(0=-.)`. The source target, engineered features, and train/validation/final permutation-family split remain unchanged: 438 / 146 / 145.

The **THREE-SEED ROBUSTNESS × ADDRESS-COHORT SHIFT** Canvas2D panel runs **three deterministic starting conditions** (seeds 0, 1, 2) for the 87-parameter structured Operator Forge and the 85-parameter tanh MLP, each under a fixed **100 attempted-update** budget, recording validation learning curves at steps 0,25,50,75,100. The model starts are deterministic sine/cosine offsets rather than random draws from a probabilistic initialization distribution. Separate initializations vary within a narrow predefined range. No seed is selected post hoc as "best".

**Validation-cohort distribution reweighting:** examples whose `(a,b,c)` contain repeated addresses vs those with three distinct addresses. These are two different **subsets of the existing validation partition**, not truly external OOD data. The full final-test partition is not evaluated by this source run. The cohort labels and membership are computed independently of the model's learned weights.

### Source-level executed deterministic results

| Seed | Forge validation MSE | MLP validation MSE | Forge accepted | MLP accepted |
|---|---:|---:|---:|---:|
| 0 | 0.000110831086 | 0.001703121232 | 100 | 100 |
| 1 | 0.000111120332 | 0.001586446267 | 100 | 100 |
| 2 | 0.000111124907 | 0.001641940138 | 100 | 100 |
| **Mean** | **0.000111025441** | **0.001643835879** | — | — |

Validation cohorts: **44 repeated-address** examples and **102 distinct-address** examples.

| Seed | Forge repeated | Forge distinct | MLP repeated | MLP distinct |
|---|---:|---:|---:|---:|
| 0 | 0.0003063990 | 0.0000264685 | 0.0034937250 | 0.0009307039 |
| 1 | 0.0003075041 | 0.0000264057 | 0.0032430170 | 0.0008718471 |
| 2 | 0.0003077533 | 0.0000263048 | 0.0033963646 | 0.0008851296 |

Both models have notably higher mean squared error on repeated-address triples. This is a useful **failure-mode cohort**: the aggregate score obscures the repeated-case difficulty. The Forge had lower validation error than this MLP at all three starts, but their feature priors, architectures, learning rates, and favorable starting conditions are still different. Three deliberately small deterministic perturbations do not establish broad seed robustness or model superiority.

The source-level JS test confirmed exact cohort counts, 100 accepted updates for each model and seed, and reproducible deterministic calculations. A standalone Python regression `eck/test_eck049.py` has been committed for seed generation, cohort partition, family split and parameter checks; it has not been independently run. Live Pages integration remains unverified.

### ASCII mesh

```text
     [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]

       GEN 0           GEN 1           GEN 2
      00 01 02        09 10 11        18 19 20
      03 04 05  -->   12 13 14  -->   21 22 23
      06 07 08        15 16 17        24 25 26
                          |
                 WEAK MEDIUM STRONG FUSION
                          |
                   87 Forge / 85 MLP
                          |
                    seed 0 / 1 / 2
                          |
                    100 matched rounds
                          |
                  repeated / distinct
                          |
                        (0=-.)
```

### ECK-050 — Next natural bound

Stress truly altered *input distributions* by reserving precommitted new address frequencies or synthetic corruption operators that preserve a clear ground-truth target. Keep repeated-address cohorts separately monitored, and compare improvements against matched compute and new initialization distributions without selecting only favorable runs. Before trying to close the final-test seal, freeze models and evaluation thresholds.

## ECK-050 — Repeated-address collision correction

The address/phase cube remains `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]`: 27 indexed nodes, 729 ordered triples, WEAK/MEDIUM/STRONG/FUSION computational carrier operators, and external fixed singlet `(0=-.)`.

ECK-049 found higher validation error on repeated-address inputs (44 examples) than on all-distinct triples (102 examples). This new experiment makes that error case an explicit test. Two models begin with **identical ECK-046 Operator Forge parameters**: (a) a baseline with 87 learned weights and (b) a collision-repair candidate with 87 Forge weights plus **nine additional trainable, address-specific coincidence weights** (96 total). These new coefficients multiply the engineered `bit0×bit1` phase-collision feature at each address. Both run with the same 438 train / 146 validation partition and identical per-epoch budget. This is a deliberately designed correction: the known synthetic task already contains a `bit0×bit1` term, so no claim is made that the network spontaneously invented the feature.

The accepted-update gate requires decreasing full-training MSE and non-increasing **aggregate** validation MSE. It does **not** prevent a regression within the distinct-address validation cohort; that regression is explicitly measured. Versions are frozen parent-linked records, and the 145 final-test cases are held out until `SEAL + FINAL TEST`.

### Executed committed-JavaScript results

| After rounds | Model | Aggregate validation MSE | Repeated-address MSE | Distinct-address MSE |
|---|---|---:|---:|---:|
| 100 | 87 baseline | 0.000109544400 | 0.000303623593 | 0.000025823963 |
| 100 | 96 repaired | 0.000110469322 | 0.000306577446 | 0.000025873661 |
| 600 | 87 baseline | 0.000016611960 | 0.000047577468 | 0.000003254289 |
| 600 | 96 repaired | 0.000016021281 | 0.000045001299 | 0.000003520097 |

**Important:** after 100 rounds the repair is *worse on all three metrics*. After 600 rounds it modestly improves aggregate validation and repeated-address error, but **makes distinct-address validation slightly worse**. Thus the objective of improving the harder cohort *without sacrificing the easier cohort* is **not achieved**. This is an open counterexample, not a success claim. The new model has nine extra parameters and still does not dominate the simpler model across cohorts.

An analytic-vs-central finite-difference gradient audit of three collision coefficients after 20 training updates produced maximum difference `1.50×10^-15`, confirming the appended coincidence gradient at those coordinates. It is not a comprehensive gradient audit of all 96 parameters.

### Mesh sketch

```text
   [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]

      GEN 0          GEN 1          GEN 2
     00 01 02       09 10 11       18 19 20
     03 04 05  -->  12 13 14  -->  21 22 23
     06 07 08       15 16 17       24 25 26
                    |
       87 OPERATOR FORGE WEIGHTS
                    |
          BIT0 & BIT1 COINCIDENCE
                    |
       +9 TRAINABLE ADDRESS WEIGHTS
                    |
            87 BASELINE vs 96 REPAIR
                    |
           44 REPEATED / 102 DISTINCT
                    |
                  (0=-.)
```

The implementation is `eck/index.html`; a Python structural regression `eck/test_eck050.py` was committed but has not been independently run. Direct extraction of the actual committed JavaScript passed syntax, both 100- and 600-iteration numerical comparisons, and the three sampled gradient checks. Browser end-to-end behavior and GitHub Pages deployment remain unverified.

### ECK-051 — Next natural bound

Introduce a **per-cohort acceptance gate** that refuses collision-repair updates when distinct-address validation worsens, and separately evaluate whether loss reweighting improves repeated-address performance under that constraint. Avoid optimizing on one fixed validation partition indefinitely; preserve a new independent evaluation split before making a generalization claim.

## ECK-051 — Dual-cohort acceptance policy

Preserve 27 indexed cube nodes, 729 ordered address configurations, the four computational channels WEAK/MEDIUM/STRONG/FUSION, the external fixed singlet `(0=-.)`, and the 438/146/145 training/validation/final partition by unordered permutation family.

The previous ECK-050 repair (96 weights: 87 operator parameters plus nine address collision coefficients) improved repeated-address validation late in training but worsened distinct-address validation. ECK-051 creates **two independent, identical-initialized 96-weight collision learners** with a matched learning rate and iteration budget. The standard learner accepts an iteration when train MSE decreases and *aggregate* validation MSE does not rise. The **dual-cohort learner** applies the same condition and additionally requires non-increasing validation MSE independently in the **44 repeated-address** and **102 all-distinct-address** validation cohorts. All accepted revisions freeze their entire model coefficients with parent-linked ancestry; rejected attempt packets preserve before/candidate training, validation and cohort losses.

The actual acceptance predicate is:

```text
accept =
  (new_train < old_train - 1e-13)
  AND (new_validation <= old_validation + 1e-12)
  AND (
       NOT dual_gate
       OR (
            new_repeated <= old_repeated + 1e-12
            AND new_distinct <= old_distinct + 1e-12
          )
      )
```

### Executed source-level tests

A 600-iteration extracted-JavaScript trial (without consulting the final partition) gave **600/600 accepted updates to both learners**, ending in **identical** metrics:

| MSE | Aggregate-gated 96 | Dual-cohort-gated 96 |
|---|---:|---:|
| Training | 0.00001504926939 | 0.00001504926939 |
| Aggregate validation | 0.00001602128085 | 0.00001602128085 |
| Repeated-address validation | 0.00004500129879 | 0.00004500129879 |
| Distinct-address validation | 0.00000352009664 | 0.00000352009664 |

The **strict gate did not trigger** on the ordinary 600-round path. This is not a demonstrated learning improvement or proof that the strict model can outperform the aggregate model. The stricter gate cannot reduce the validation losses of accepted checkpoints, relative to *its own* immediately previous checkpoint, but it may stagnate and does not guarantee beating the ordinary learner.

A separately specified, **mathematically consistent loss-vector counterexample** directly exercised the exact committed gate policy:

```text
                       BEFORE      PROPOSED
  training loss         0.020       0.019     improves
  repeated loss         0.010       0.005     improves
  distinct loss         0.010       0.011     WORSENS
  aggregate validation  0.010       0.0091917808 improves

  ordinary policy = ACCEPT
  dual cohort     = REJECT
```

The aggregate proposed value is weighted exactly by the validation membership `(44×0.005+102×0.011)/146`. These numerical values are a **synthetic policy unit test**, not a candidate produced by the trained neural model. No behavior is fabricated. This proves that the strict gate would reject a cohort-harming update even if aggregate validation and training improve.

**Mesh sketch**

```text
  [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]

  GEN 0             GEN 1              GEN 2
  00 01 02          09 10 11           18 19 20
  03 04 05   ===>   12 13 14    ===>   21 22 23
  06 07 08          15 16 17           24 25 26
                       |
                FOUR CARRIERS
           WEAK MEDIUM STRONG FUSION
                       |
               87 operator weights
                 +9 collision gates
                       |
              96-weight candidate
                       |
            TRAIN 438 → VALIDATE 146
                        /      \
                repeated 44   distinct 102
                        \      /
                  BOTH NONWORSENING?
                   YES /     \ NO
                FREEZE        REJECT
                       |
                     (0=-.)
```

Implementation: `eck/index.html`, executable standalone regression `eck/test_eck051.py`. The committed JavaScript was syntax-checked, directly executed over 600 optimization rounds, and its explicit adverse policy counterexample was verified. The Python regression has been committed but not separately executed. Final-test 145 remains withheld. Live browser/GitHub Pages deployment has not been independently verified.

### ECK-052 — Next natural bound

Challenge the dual gate with a real gradient candidate on a precommitted altered training objective or cohort-reweighted rate, and preserve a **model-derived** disagreement witness. Compare gating with constrained multi-objective optimization, freezing the untouched test partition throughout. Do not claim improvement until it appears on a task not used to design the gate.

## ECK-052 — Actual gradient conflict, ordinary acceptance vs strict rejection

The 27-address/phase-node 3×3×3 cube, 729 ordered inputs, 96-parameter collision learner, four computational carriers, immutable checkpoints, and fixed singlet `(0=-.)` remain unchanged. The training/validation/test split remains **438 / 146 / 145**, by permutation family. The final 145-case test partition was **not evaluated**.

ECK-051 established a **synthetic loss-vector** example of the dual-cohort gate's semantics but the ordinary 600-epoch model path produced zero disagreements. ECK-052 goes farther: it replays an **actual model-derived full-batch gradient candidate** from its existing weights.

### Reproducible real neural witness

1. Reset the 96-parameter collision-repair model to its canonical ECK-050 initialization.
2. Accept **20 ordinary updates** at the original learning rate `1.8`, reaching frozen source checkpoint version 20.
3. Make two independent copies of *exactly* those trained 96 weights (Forge 87 + collision 9).
4. Calculate the 21st update using the **same real gradient and loss functions**, with a deliberately aggressive challenge learning rate of `70` (an audit stress rate, not a recommended routine learning rate).
5. Present the same candidate to the aggregate-only and dual-cohort acceptance policies.

| Loss | Frozen checkpoint 20 | Real gradient candidate |
|---|---:|---:|
| Training | 0.000340620764690859 | 0.000295112352507506 |
| Aggregate validation | 0.000342605451784201 | 0.000296001404586946 |
| Repeated-address validation (44 examples) | 0.000662069126206552 | 0.000439127266405867 |
| Distinct-address validation (102 examples) | 0.000204797592229461 | **0.000234260836743489** |

Training, aggregate validation, and repeated-address error **improve**, while distinct-address error **gets worse**. The normal gate returns **ACCEPT** and advances to version 21. The dual-cohort gate returns **REJECT** and retains version 20.

This is **not** a synthetic hand-chosen loss table: the candidate comes from the trained model's actual gradient update and the listed losses from model prediction on the pre-existing train/validation sets. The stress-test learning rate was discovered through a bounded search over candidate rates and intermediate ordinary checkpoints; it is a targeted *counterexample*, not a representative outcome of the default optimizer. The learning rate and checkpoint were frozen into the reproducible test. Model versions remain independent between the two policies, and the source checkpoint is not mutated.

### UI and regression

The Canvas2D console's ECK-051 Dual Gate section now includes **REPLAY REAL GRADIENT CONFLICT** alongside the earlier symbolic policy counterexample. It records before/candidate losses, outcome of both gates, retained/accepted version numbers, the singlet provenance, and keeps the final-test partition unopened. The executable Node regression is `eck/test_eck052.cjs`, runnable with `node eck/test_eck052.cjs`, which reads the actual repository HTML source and extracts the mathematical functions without browser DOM access. It verifies the model-derived adverse step, policy disagreement, checkpoint ancestry, and split sizes.

**Verification completed:** the final committed JavaScript passed syntax parsing; the direct extraction harness replayed the exact candidate and confirmed the expected outputs, including `ordinary=true`, `strict=false`, and checkpoint versions `20→21` vs `20→20`. The new standalone Node regression was committed but not independently run; live Pages/browser integration was not independently verified.

### ASCII mesh

```text
 [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]
       GEN 0           GEN 1           GEN 2
      00 01 02        09 10 11        18 19 20
      03 04 05  --->  12 13 14  --->  21 22 23
      06 07 08        15 16 17        24 25 26
                         |
                FOUR FORCE CARRIERS
                 87 ROUTING WEIGHTS
                 +9 COLLISION GATES
                         |
                 TRAIN 20 × LR 1.8
                         |
                CHECKPOINT #20 FROZEN
                         |
             21ST CANDIDATE @ LR 70
                         |
              TRAIN ↓  AGGREGATE ↓
             REPEATED ↓  DISTINCT ↑
                         |
                 /---------------\
        ORDINARY ACCEPT       DUAL REJECT
              VERSION 21       VERSION 20
                 \---------------/
                         |
                PRESERVE WITNESS
                         |
                       (0=-.)
```

### ECK-053 — Next natural bound

Compare multiple bounded step-size searches or line-search constraints to see whether the **model-derived conflict can be avoided** without stopping all learning. Search for a candidate that decreases training, aggregate validation and **both** validation cohorts at the same trained checkpoint. Preserve the adverse case as a regression and explicitly report if no feasible step exists within the declared search.

## ECK-053 — Recover a safe model-derived step after an adverse one

This experiment preserves the user-specified `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]` mesh, 27 address/phase cells, 729 ordered triple codes, WEAK/MEDIUM/STRONG/FUSION symbolic operators, 96-parameter collision learner (87 Forge + 9 collision gates), source-vs-final data partition 438 training / 146 validation / 145 withheld final, and immutable singlet `(0=-.)`.

ECK-052 found a **real gradient-derived adverse candidate** at checkpoint 20 with learning rate `70`. It lowered training, aggregate validation and repeated-address errors but worsened distinct-address validation error. The ordinary gate accepted it and the dual-cohort gate rejected it.

ECK-053 now **recovers a safe update from that very same frozen checkpoint** by testing a predeclared *descending grid of 21 rates*:

```text
[70, 60, 50, 40, 35, 30, 25, 20, 15, 12, 10, 8, 6,
 4, 3, 2, 1.8, 1, 0.5, 0.25, 0.1]
```

For every rate: clone the same version-20 96-weight state, calculate an actual full-batch gradient candidate using the existing model/loss code, measure training and both validation cohorts, and apply the **dual-cohort gate**. Store all candidate packets without mutating the source. Select the *first accepted rate* from the descending list. This is the **largest accepted rate among those 21**, not necessarily the globally optimal or largest real-valued safe step.

### Source-executed neural results

| Loss | Source checkpoint 20 | Candidate at rate 70 | Recovered candidate at rate 60 |
|---|---:|---:|---:|
| Training | 0.000340620764691 | 0.000295112352508 | **0.000220830414715** |
| Aggregate validation | 0.000342605451784 | 0.000296001404587 | **0.000222340099973** |
| Repeated-address validation (44) | 0.000662069126207 | 0.000439127266406 | **0.000386329590954** |
| Distinct-address validation (102) | 0.000204797592229 | **0.000234260836743** (worse) | **0.000151599535236** |

The rate-70 candidate passes the **ordinary** gate, but fails the **dual-cohort** gate. The rate-60 candidate passes both; it decreases training, aggregate validation, repeated-address validation and distinct-address validation from the frozen source. Thus **checkpoint 20 → 21** can proceed without taking the original harmful step. There were **20 feasible candidates of the 21 tested**. The rate search uses validation information and must not be reported as an unbiased estimate of held-out generalization.

This recovery is a **single-checkpoint, targeted audit** based on the ECK-052 failure, not a general convergence theorem. The two cohort losses are averages, not per-example guarantees. The learning rate grid was fixed for this replay, and the fact that rate 60 works does not guarantee any future checkpoint will have a safe positive step.

The ECK-051 dual-gate Canvas2D instrument now offers **RECOVER SAFE STEP**. The replay records the parent version, all 21 candidate metrics, the rejected rate-70 packet, the selected rate-60 weights, the singlet, and the unopened final-test status. The standalone Node regression `eck/test_eck053.cjs` runs against the actual HTML source: `node eck/test_eck053.cjs`.

**Verification:** committed JavaScript syntax passed and the new recovery function was directly executed from that source, confirming rate 70 rejection, rate 60 acceptance, 21 trials / 20 feasible, and the exact source and recovered loss values. The Node regression was committed but has not been separately executed. Live Pages/Canvas2D interaction was not independently verified. The final 145 test cases remain unopened.

### ASCII mesh

```text
    [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]

        GEN 0             GEN 1             GEN 2
       00 01 02          09 10 11          18 19 20
       03 04 05    ==>   12 13 14    ==>   21 22 23
       06 07 08          15 16 17          24 25 26
                            |
              FOUR LEARNED FORCE CARRIERS
                 87 operator + 9 gate
                            |
                     CHECKPOINT #20
                            |
                  DESCENDING LR GRID
                       70 -> 60
                       |      |
                    REJECT   ACCEPT
                       |      |
              distinct loss ↑  both losses ↓
                       |      |
                  preserve  VERSION #21
                       \      /
                     WITNESS LEDGER
                            |
                         (0=-.)
```

### ECK-054 — Next natural bound

Replace the fixed descending search by a **deterministic safeguarded line search** with bounded backtracking, explicit termination, and a feasibility certificate. Demonstrate it can recover from multiple real adverse candidate steps without tuning the rates to one witness, while preserving a distinct independent evaluation surface. Keep final test sealed until selection and stop rules are frozen.

## ECK-054 — Automatic geometric step-size recovery and bounded termination

The 27-address `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]` neural cube, 729 ordered configuration codes, 96-weight collision-repair network (87 operator weights + 9 collision gates), four named computational carriers, and the external nonlearned singlet `(0=-.)` are preserved. The model's 438 training / 146 validation / 145 final-test split remains unchanged, and **no final-test predictions are evaluated in the backtracking controller**.

ECK-053 used a manually declared 21-rate descending search from trained checkpoint 20. ECK-054 adds a **reusable, deterministic bounded geometric line-search** controller. It clones a frozen checkpoint, computes an *actual full-batch neural gradient candidate*, tests the **train + aggregate validation + repeated validation + distinct validation** acceptance rule, and halves the learning rate on failure. A source checkpoint is never overwritten; each attempted step stores its candidate loss metrics and accepted/rejected result.

The run configuration is:
- Initial trial rate `70`
- Geometric shrink factor `0.5`
- Maximum `9` candidate trials
- Minimum rate `0.1`
- Independently replayed source checkpoints `0`, `20`, `100`

The controller terminates with **SAFE_ACCEPT**, **RATE_FLOOR**, or **BOUNDED_EXHAUSTION**. This search chooses the *first acceptable rate* on a declared geometric sequence. It makes no claim to find a global line-search optimum or the largest feasible continuous rate. The search uses validation loss for update acceptance and must not be conflated with unseen-test generalization.

### Executed source-level checkpoint results

| Source checkpoint | First rate trial | Second rate trial | Result | Number of attempts |
|---|---|---|---|---:|
| 0 | 70 rejected | **35 accepted** | SAFE_ACCEPT | 2 |
| 20 | 70 rejected (cohort conflict) | **35 accepted** | SAFE_ACCEPT | 2 |
| 100 | **70 accepted** | — | SAFE_ACCEPT | 1 |

Checkpoint 20: before → accepted rate-35 candidate:

| Error metric | Frozen checkpoint 20 | Accepted candidate |
|---|---:|---:|
| Training MSE | 0.000340620764691 | 0.000152940652950 |
| Aggregate validation MSE | 0.000342605451784 | 0.000155324670140 |
| Repeated-address validation MSE | 0.000662069126207 | 0.000377797874489 |
| Distinct-address validation MSE | 0.000204797592229 | 0.000059355836891 |

The ECK-053 rate-60 candidate is also safe at checkpoint 20; this geometric search **does not try 60** and accordingly selects 35. The checkpoint-0 and checkpoint-100 recoveries demonstrate that the identical bounded procedure works at multiple learned stages, but are not a mathematical convergence guarantee.

**Failure-path test:** set maxTrials=1 at checkpoint 20 with rate 70. The controller terminates with `BOUNDED_EXHAUSTION`, no accepted candidate, one rejected trial, and the frozen checkpoint remains version 20. This is a real model-derived failed search, not a synthetic loss vector.

### Implementation and evidence

The ECK-051 dual-cohort Canvas2D panel now includes **RUN BOUNDED BACKTRACKING**, which shows per-checkpoint termination states and accepted step sizes while preserving all attempted rate packets. Its functions are `dgBacktrackAtCheckpoint()`, `dgBacktrackingAudit()`, and the frozen `dgBacktrackSpec` configuration. The independent executable Node regression `eck/test_eck054.cjs` reads `eck/index.html`, executes the neural model functions and asserts the three successes, cohort constraints, and bounded exhaustion while keeping the 145-case final partition unopened.

Actual committed source JavaScript was syntax-checked and the three successful checkpoint runs plus the real bounded failure were executed directly. The new standalone Node regression has been committed but not independently run. Live Pages and browser interaction remain unverified.

### ASCII diagram

```text
  [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]

    GEN 0            GEN 1            GEN 2
   00 01 02         09 10 11         18 19 20
   03 04 05   ==>   12 13 14   ==>   21 22 23
   06 07 08         15 16 17         24 25 26
                       |
            87 OPERATOR + 9 COLLISION
                       |
                 FROZEN STATE
                       |
                TRY LEARNING RATE
                       |
             VALIDATE TRAIN/COHORTS
                    /      \
                 PASS      FAIL
                  |          |
                ACCEPT     RATE /= 2
                  |          |
                FREEZE     TRIES LEFT?
                  |          |
                ADVANCE    YES → RETRY
                  |          |
                  |         NO → TERMINATE
                  \          /
                    EVIDENCE LEDGER
                         |
                       (0=-.)
```

### ECK-055 — Next natural bound

Use adaptive backtracking on **successive learned checkpoints**, rather than fixed independent replays, and compare total accepted progress, rejected trials and computational cost against a fixed-rate baseline. Include a finite stopping certificate for constrained training plateaus; avoid indefinite validation-set reuse and freeze a new independent evaluation protocol before any generalization claim.

## ECK-055 — Continuous neural checkpoints under a candidate-proposal budget

Preserve `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]`, 27 addressed temporal cells, 729 ordered triple configurations, four symbolic learned carriers, 96 trainable parameters (87 Forge + 9 collision correction), and immutable singlet `(0=-.)`. The 438/146/145 training/validation/final data separation remains unchanged; the 145 final cases are not evaluated by ECK-055.

Unlike ECK-054's independently replayed checkpoints, this experiment carries **successive accepted learned weights** forward. The fixed comparison receives an update at rate `1.8`. The adaptive learner starts each step at `70` and halves on failure (`70,35,17.5,...`) with at most nine candidate proposals per step and a rate floor of `0.1`. Both begin at the **same 96-weight initialization** and use the same dual-cohort policy: training must strictly improve, and aggregate, repeated and distinct validation losses must not worsen. Each model receives a maximum **40 real gradient proposals** (including rejected proposals); the cost measure is candidate model-update evaluations, not wall-clock time or mathematical FLOPs. Each attempt packet preserves the current checkpoint, rate, candidate metrics and outcome. Each accepted checkpoint has a monotonically increasing version.

A complete zero-feasible-step backtracking search ends in a finite **NO_FEASIBLE_STEP** stop. This means no feasible candidate in that finite geometric rate grid from those weights; it is **not** a proof that no safe step exists at any learning rate or in any direction.

### Directly executed committed JavaScript results

| Measure | Adaptive (70 / geometric backtracking) | Fixed (1.8) |
|---|---:|---:|
| Allowed proposal budget | 40 | 40 |
| Proposals actually used | 22 | 40 |
| Accepted updates | 7 | 40 |
| Rejected candidates | 15 | 0 |
| Stop | NO_FEASIBLE_STEP | BUDGET_EXHAUSTED |
| Training MSE | 0.000077716414 | 0.000171257032 |
| Aggregate validation MSE | **0.000080955279** | 0.000173828318 |
| Repeated-address validation MSE | **0.000232934085** | 0.000428955826 |
| Distinct-address validation MSE | **0.000015395794** | 0.000063773314 |

**Interpretation:** the adaptive path reached lower loss in this particular experiment using only 22 proposals, but terminated after seven accepted checkpoints. The fixed path completed 40 accepted smaller updates without rejections. Because the adaptive controller stops early, it does not consume exactly the same compute despite the common cap. The controller also uses the same validation cohorts repeatedly for step acceptance. Neither observation proves a general convergence advantage or an unbiased test-set improvement. All 145 final configurations remain sealed.

The new Canvas2D **CONTINUOUS SAFEGUARDED LEARNING** instrument plots validation curves against *candidate proposals evaluated*, rather than epochs or accepted checkpoints, so rejected gradient evaluations are visible in the computational budget. The source is `eck/index.html`; its Node regression is `eck/test_eck055.cjs` and can be invoked by `node eck/test_eck055.cjs`. The committed JavaScript passed parsing and the actual successive model comparison was executed directly from its functions. The standalone Node regression has been committed but not separately executed, and live browser/Pages integration has not been independently verified.

### ASCII cube

```text
  [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]

      GEN 0            GEN 1            GEN 2
     00 01 02         09 10 11         18 19 20
     03 04 05   ==>   12 13 14   ==>   21 22 23
     06 07 08         15 16 17         24 25 26
                        |
              FOUR LEARNED CARRIERS
                 87 + 9 = 96 weights
                        |
                IDENTICAL START
                /             \
      ADAPTIVE BACKTRACK      FIXED RATE
          INITIAL LR 70          LR 1.8
          7 accepted             40 accepted
          15 rejected             0 rejected
          22 proposals           40 proposals
                \             /
            COUNT REAL CANDIDATES
                        |
           DUAL-COHORT VALIDATION
                        |
                      (0=-.)
```

### ECK-056 — Next natural boundary

Address the finite *NO_FEASIBLE_STEP* stall by adding deterministic recovery policies that do not silently change the acceptance constraints: (a) restart at a lower bounded rate, (b) use a verified alternative descent direction, or (c) preserve a plateau certificate and terminate. Compare against the 40-proposal baseline and keep the model-selection and final-test boundaries separate.

## ECK-056 — Recover after a dual-cohort full-gradient plateau

Preserve the user-specified `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]` neural cube, 27 addressed phase cells, 729 ordered triple codes, the symbolic WEAK / MEDIUM / STRONG / FUSION carrier operators, 96 trainable coefficients (87 Forge + 9 collision repair), fixed singlet `(0=-.)`, and training/validation/final split 438 / 146 / **145 final withheld**.

ECK-055 demonstrated a 40-proposal continuous dual-cohort backtracking controller that accepted seven updates then stopped after 22 proposals: no feasible **full-gradient** step in its finite nine-rate geometric grid. ECK-056 asks whether that is a limitation of the *full-gradient direction*, rather than a generalized impossibility of improvement.

The baseline training operation `collisionEpoch(run,rate,dualGate,activeBlock)` now accepts an optional trainable parameter block. When `activeBlock=null`, its existing full 96-parameter gradient behavior is preserved. When one of `weak, medium, strong, fusion, repair` is chosen, **only that block's parameters move**, but the gradients, predictions and dual-cohort acceptance gate still come from the full real model. This is block-coordinate descent on the same task, not a new label feature. A proposed block-specific update must improve training and not worsen aggregate, repeated or distinct validation losses.

ECK-056 runs a deterministic continuous experiment with a **maximum of 40 real candidate-gradient proposals**:

1. Start at the canonical 96-weight initialization.
2. Attempt full-gradient updates with halved learning rates, beginning at 70, nine trials maximum.
3. On exhaustive rejection, freeze the stalled checkpoint and test the five carrier blocks in the declared order `weak, medium, strong, fusion, repair`, each with rate 70 and the same strict gate.
4. If a block update is accepted, append the new version and resume ordinary full-gradient backtracking.
5. If all blocks fail or the 40-proposal budget is exhausted, terminate with the complete failure ledger. Do **not** inspect the final-test partition.

### Verified committed-JavaScript run

The actual source-extracted model produced **40 proposals = 13 accepted + 27 rejected**, ending with:

| Measure | ECK-055 full-gradient only | ECK-056 full-gradient + block recovery |
|---|---:|---:|
| Proposals consumed | 22 | 40 |
| Accepted checkpoints | 7 | 13 |
| Rejected proposals | 15 | 27 |
| Training MSE | 0.000077716414 | **0.000035767288** |
| Aggregate validation MSE | 0.000080955279 | **0.000037771772** |
| Repeated-address validation MSE | 0.000232934085 | **0.000106243275** |
| Distinct-address validation MSE | 0.000015395794 | **0.000008235046** |

Two separate real full-gradient stalls and two real block-specific recoveries were preserved:

- **Stall 1:** after 22 proposals at checkpoint 7, all nine allowed full-gradient rates rejected. The **WEAK-only** gradient at rate 70 was accepted and advanced checkpoint **7 → 8**, with validation MSE `0.000080955279 → 0.000080707999`.
- **Stall 2:** after 32 proposals at checkpoint 8, all nine allowed full-gradient rates rejected. WEAK, MEDIUM, STRONG block candidates were rejected, and **FUSION-only** gradient at rate 70 was accepted. It advanced checkpoint **8 → 9**, with validation MSE `0.000080707999 → 0.000069510072`.
- Subsequent full-gradient updates resumed, reaching checkpoint 13 on the 40th total proposal.

The source includes an append-only `stalls` record for **both** distinct stalled checkpoints, an immutable `recoveries` record, all candidate before/proposed loss metrics, and a parent-indexed sequence of accepted checkpoint metrics.

**Interpretation:** this is an actual improvement at two previously blocked model states. A lack of a feasible **full** gradient step did not mean a lack of a feasible **coordinate-block** step. ECK-056 consumes the full 40-proposal budget and therefore has more computation than the ECK-055 stopped path; it is not a parameter-matched or compute-normalized architecture superiority claim. Its validation data still participate in every acceptance decision. The 145 final cases are not evaluated.

The Canvas2D **CARRIER-BLOCK PLATEAU RECOVERY** panel displays the training path and both recovery witnesses. The executable Node regression `eck/test_eck056.cjs` extracts the actual neural functions directly from `eck/index.html`, checks both stall/recovery sequences, counts and loss invariants, and avoids final-test prediction. The committed HTML JavaScript parsed and its numerical model was executed; the standalone Node file was committed but has not been separately run, and the deployed GitHub Pages page and browser interaction have not been independently verified.

### ASCII: recovered neural cube

```text
  [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]

       GEN 0            GEN 1            GEN 2
      00 01 02         09 10 11         18 19 20
      03 04 05   ==>   12 13 14   ==>   21 22 23
      06 07 08         15 16 17         24 25 26
                         |
            WEAK MEDIUM STRONG FUSION
                         |
             87 routes + 9 collision gates
                         |
               FULL GRADIENT / 9 RATES
                         |
               FAIL at CHECKPOINT 7
                         |
           WEAK-only SAFE: 7 --> 8
                         |
               FULL GRADIENT / 9 RATES
                         |
               FAIL at CHECKPOINT 8
                         |
      WEAK FAIL / MEDIUM FAIL / STRONG FAIL
                         |
           FUSION-only SAFE: 8 --> 9
                         |
                   FULL GRADIENT
                         |
                    VERSION 13
                         |
                        (0=-.)
```

### ECK-057 — Next natural bound

Audit the real gradient behavior at the two rescued checkpoints and derive a **general deterministic block-selection rule** based on measured expected improvement per candidate evaluation. Compare automatic block choice with fixed order, count its extra screening cost and preserve all rejected packets. Keep final-test evaluation and performance claims separated from validation-selected updates.

## ECK-057 — Spend candidate evaluations to choose the better safe carrier

This boundary retains the user-defined `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]` neural mesh, 27 indexed address/phase cells, 729 ordered input configurations, four symbolic carrier operators (WEAK, MEDIUM, STRONG, FUSION), nine collision correction coefficients (96 total trainable scalars), external fixed singlet `(0=-.)`, and the unchanged 438 train / 146 validation / 145 sealed final split.

ECK-056 established that a full-gradient plateau can be escaped using carrier-block updates. Its **fixed-order** rule tested `WEAK, MEDIUM, STRONG, FUSION, repair` and accepted the first feasible candidate. ECK-057 tests an **evidence-ranked** policy, which, at each plateau, evaluates each of those five candidate blocks against the **same frozen learned checkpoint** with the same rate 70 and model-derived gradients. Every probe consumes one candidate-evaluation unit, whether accepted or not. The policy chooses the *feasible* block with the greatest reduction in **aggregate validation MSE per single probe** (each probe has equal cost in this experiment); ties are resolved by the declared block order. Neither policy changes the acceptance constraints: training must improve, and both repeated-address and distinct-address validation cohorts must not worsen.

The ranking policy uses validation outcomes to make its selection, and accordingly cannot be interpreted as an unbiased estimate of unseen generalization. All rejected packets, candidate metrics and selection decisions remain in the audit ledger. A candidate is *feasible* only if the existing dual-cohort gate accepts it; the MSE ranking is applied after feasibility filtering. Both policies receive a maximum of **40 actual candidate gradient evaluations**, including every full-gradient backtracking attempt and every screened block. No zero-cost lookahead.

### Direct execution from committed HTML JavaScript

| Metric | Fixed first-feasible order | Evidence-ranked safe candidate |
|---|---:|---:|
| Candidate evaluations | 40 | 40 |
| Accepted checkpoints | 13 | **17** |
| Full-gradient stalls | 2 | 1 |
| Training MSE | 0.000035767288 | **0.000021258318** |
| Aggregate validation MSE | 0.000037771772 | **0.000022604191** |
| Repeated-address MSE | 0.000106243275 | **0.000064156113** |
| Distinct-address MSE | 0.000008235046 | **0.000004679832** |

At the shared first full-gradient stall, checkpoint 7, the screened blocks yielded:

| Carrier block | Safe according to dual cohort gate? | Immediate aggregate validation MSE improvement |
|---|---|---:|
| WEAK | YES | 0.000000247280 |
| MEDIUM | NO | 0.000000251431 |
| STRONG | NO | 0.000000256059 |
| FUSION | **YES** | **0.000011197927** |
| REPAIR | NO | -0.000000046374 |

Only WEAK and FUSION passed the *complete* gate. The fixed-order policy spends one probe and chooses WEAK, whereas the ranked policy spends five probes and chooses FUSION because its measured safe improvement is much larger. The ranked trajectory then continues without another full-gradient stall within the 40-proposal budget and reaches checkpoint 17. The fixed-order trajectory encounters a second stall, needs another recovery sequence, and reaches checkpoint 13.

**Scientific boundary:** this demonstrates a useful payoff from evidence-based *carrier selection* on the known engineered validation task. It does not establish a new neural architecture, general intelligence, generalization to other tasks, or a physics-force interpretation. The ranking has higher screening cost at the first stall but lower downstream cost in this particular deterministic path. Its score is selected on validation and the sealed 145-case final test remains unopened. Candidate-count parity does not imply equal wall-clock time or computational FLOPs.

### ASCII witness mesh

```text
  [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]

      GEN 0             GEN 1             GEN 2
     00 01 02          09 10 11          18 19 20
     03 04 05   ===>   12 13 14   ===>   21 22 23
     06 07 08          15 16 17          24 25 26
                         |
                87 ROUTES + 9 COLLISIONS
                         |
                 FULL-GRADIENT STALL
                      VERSION 7
                         |
          +--------------+--------------+
          |                             |
     FIXED PRIORITY                EVIDENCE RANK
     WEAK = first safe             probe all 5 blocks
          |                             |
     WEAK ACCEPTED                FUSION ACCEPTED
          |                             |
     another stall                no second stall
          |                             |
     VERSION 13                   VERSION 17
          +--------------+--------------+
                         |
               40 CANDIDATES EACH
                         |
                WITNESS / FREEZE
                         |
                       (0=-.)
```

Implementation: `eck/index.html`, additional Canvas2D **EVIDENCE-RANKED CARRIER SELECTION** panel, and runnable Node regression `eck/test_eck057.cjs` (`node eck/test_eck057.cjs`). The committed JavaScript parsed and the actual dual-policy model functions were executed from source; the separate Node regression was committed but has not been independently executed. Live Pages/browser behavior has not been independently verified.

### ECK-058 — Next natural bound

Audit selection robustness using multiple deterministic initializations and a genuinely changed task while explicitly accounting for *screening cost* and *validation reuse*. Compare ranking, first-feasible order, and a carrier-gradient heuristic that does not examine validation results for every candidate. Preserve the 145-case final-test seal until the selection policy is frozen.

## ECK-058 — Test ranking versus fixed order and a cheaper training-gradient heuristic

Preserve `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]`, 27 addressed cells, 729 ordered address triples, four named carrier operations (WEAK/MEDIUM/STRONG/FUSION), 87 operator weights and nine trainable collision corrections (96 total), fixed singlet `(0=-.)`, and the 438 training / 146 validation / 145 withheld final partition.

ECK-057 demonstrated evidence-ranked Fusion selection over fixed-order Weak selection from one canonical initialization. ECK-058 compares **three distinct block selectors across three deterministic starting perturbations** `0,1,2`, with each run receiving at most **40 actual candidate-gradient evaluations**:

- **FIXED**: at each full-gradient plateau, try WEAK, MEDIUM, STRONG, FUSION, REPAIR in that order, stopping at the first safely accepted candidate.
- **RANKED**: at each full-gradient plateau, test all five block candidates from the same frozen checkpoint, count all probes, and choose the safe candidate with the highest measured reduction in aggregate **validation** MSE. Screening costs five candidate evaluations if budget allows.
- **GRADIENT HEURISTIC**: calculate an additional source-training-gradient-norm score for each carrier block, sort candidates by decreasing squared gradient norm and try them in that order until one passes the exact same dual-cohort gate. The heuristic's score computation performs two passes over source-training configurations (a Forge-gradient pass and a collision-residual correction pass), reported as one additional **gradient-scoring operation**, not a candidate trial; therefore candidate-count parity does **not** imply equal computation in FLOPs or wall time. Its final chosen model is still validated by the protected acceptance rule.

All policies use the same predeclared source target, learning rates, source-train gradients, immutable checkpoints, and dual-cohort acceptance conditions. The deterministic perturbations change the 87 Forge operator initialization; the nine collision correction weights begin at zero in all runs. This is a small seeded stress test, not a representative random-seed uncertainty estimate.

### Executed committed-source results

Each run consumed exactly 40 gradient candidate proposals.

| Seed | Fixed validation MSE | Ranked validation MSE | Gradient heuristic validation MSE |
|---|---:|---:|---:|
| 0 | 0.000042223153 | 0.000033465441 | **0.000024541055** |
| 1 | **0.000020293618** | 0.000033672445 | 0.000024713931 |
| 2 | **0.000020456121** | 0.000033901469 | 0.000024889880 |

The per-seed accepted checkpoint counts were:

| Seed | Fixed | Ranked | Gradient |
|---|---:|---:|---:|
| 0 | 13 | 15 | 17 |
| 1 | 19 | 15 | 17 |
| 2 | 19 | 15 | 17 |

At the first stalled checkpoint in **each** seeded comparison, fixed order selected WEAK after one safe probe; ranked evaluated all five blocks and selected FUSION, while the training-gradient heuristic selected FUSION with one candidate probe **plus one extra gradient-scoring pass**. Ranking is **not consistently better**: fixed order has lower validation error on seeds 1 and 2, whereas the gradient heuristic is best on seed 0. No selector dominates the nine runs.

### Zero-shot target shift, same validation input configurations

The models train only on the unchanged original synthetic target. Each is also scored on a predeclared changed nonlinear target with different location gradient and middle×final coincidence weights. This target shift uses the **same 146 validation inputs**, not independently collected new input distributions. Shift scores are descriptive and must not be interpreted as sealed-test generalization.

| Seed | Fixed shifted MSE | Ranked shifted MSE | Gradient shifted MSE |
|---|---:|---:|---:|
| 0 | 0.001346649166 | 0.001349337154 | 0.001345986525 |
| 1 | 0.001353228487 | 0.001349153181 | 0.001345559265 |
| 2 | 0.001353795101 | 0.001349513083 | 0.001345645226 |

These shifted-target errors are much larger than source-task errors and differ only modestly among the methods; they provide no strong support for robust transfer. The 145 withheld final examples remain unopened, and the accepted source checkpoints are still selected using validation.

### ASCII kernel

```text
  [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]

      GEN 0             GEN 1             GEN 2
     00 01 02          09 10 11          18 19 20
     03 04 05    ==>   12 13 14   ==>   21 22 23
     06 07 08          15 16 17          24 25 26
                         |
             WEAK MEDIUM STRONG FUSION
                  87 + 9 = 96
                         |
          +--------------+----------------+
          |              |                |
      FIRST SAFE     RANK FIVE         GRADIENT NORM
      fixed order   validation MSE     train-only scores
          |              |                |
      1+ probes      5 probes        1+ probes + score
          |              |                |
          +--------------+----------------+
                         |
              SEEDS 0 / 1 / 2
                 40 candidates
                         |
             SOURCE + TASK SHIFT
                         |
                RETAIN EVIDENCE
                         |
                       (0=-.)
```

### Implementation / limitations

Source: `eck/index.html` with the new Canvas2D **CARRIER SELECTION ROBUSTNESS** panel and helper methods `robustRunOne`, `robustGradientScores`, `robustCompare`. The executable standalone regression is `eck/test_eck058.cjs` (`node eck/test_eck058.cjs`), which extracts committed neural source blocks, reruns the nine comparisons and verifies model selection, candidate cost, validation constraints and the closed final-test partition.

The committed JavaScript was syntax-checked and all nine comparisons were executed directly from source, with the reported results. A follow-up audit corrected the heuristic to include the full collision-repair residual in the gradients of all 96 parameters, and rerunning the nine comparisons produced the same decisions and numeric results. The extra scoring operation therefore costs roughly two training-data passes, which is not reflected in the candidate-proposal count. The separate standalone Node test was committed but not independently executed, and live GitHub Pages/browser interactions remain unverified.

**Methodological limitation:** this experiment evaluates on validation cases used repeatedly for cohort gates, so selection is susceptible to validation overfitting. The heuristic's extra gradient scoring passes and different block count mean the shared 40-candidate cap is not a strict equality of training computation.

### ECK-059 — Next natural bound

Freeze a **precommitted evaluation protocol** distinguishing cohort-protection data from model-selection data. Create a new *task-generator seed / transfer task* that is locked before comparing selectors. Prefer a reproducible compute-cost estimate including the extra heuristic gradient-scoring pass. Treat the existing 145 final-test examples as sealed until model choice, checkpoints and acceptance/stop rules are fixed.

## ECK-059 — Separate training governance from post-freeze evidence

The persistent tensor `[[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]` remains 27 addressed phase cells, 729 ordered discrete input triples, WEAK/MEDIUM/STRONG/FUSION symbolic carriers, 87 operator parameters + nine collision weights, and fixed external singlet `(0=-.)`. The previous 438 training / 146 validation / **145 never-opened final** split remains untouched.

### Precommitted synthetic evaluation specification

Protocol identifier: `ECK059_CONTINUOUS_PHASE_TRANSFER_V1`. A deterministic generator creates **81 synthetic probes**, each containing **3×9 continuous occupancy values** within (0,1), rather than the discrete one-hot binary phases used by the original 729-address neural training domain. Values come from a declared sine/modulo expression indexed only by `probe, phase, address`, not model weights. There is no new gradient learning or checkpoint selection based on these probes. The declared synthetic transfer target uses a new spatial-gradient, phase-weight and phase-interaction mixture on these same continuous inputs.

Each of the nine fixed/ranked/gradient × seed 0/1/2 models is trained exactly as in ECK-058, then its final 96 weights are included in a frozen source-model packet. The new evaluator is permitted to read those frozen weights and its 81 probes **only after policy training is finished**. No optimizer, validation acceptance gate or carrier ranking function calls this evaluator. This is a genuinely new **synthetic continuous input domain** and new **synthetic target**, but not an independent real-world dataset or scientific proof. Its generator and target were defined in the committed code before source execution returned new-task scores. They remain one designed benchmark and should not be iteratively tuned against these measured results.

### Executed model results

| Seed | Fixed-order new-task MSE | Validation-ranked new-task MSE | Gradient-heuristic new-task MSE |
|---|---:|---:|---:|
| 0 | **0.000376064048** | 0.000379239499 | 0.000386293493 |
| 1 | 0.000389782310 | **0.000380111165** | 0.000386736059 |
| 2 | 0.000389501719 | **0.000380117963** | 0.000386395231 |
| **Mean** | 0.000385116025 | **0.000379822876** | 0.000386474927 |

The ranked policy has the lowest mean new-task error across these three deterministic starts, but **fixed order wins seed 0**, so none uniformly dominates. The new-task differences are small and the benchmark is constructed from the same families of spatial and temporal features as the source task. No out-of-family performance claim is justified.

### Enforcement boundary

- **Train**: the previously defined 438 training configurations; deterministic starting perturbations; source-task target only
- **Accept/reject training candidates**: the existing 146 source validation configurations, split into 44 repeated-address and 102 all-distinct-address groups
- **Select carriers**: each frozen policy uses its existing rule; only ranked policy inspects validation error across all five candidate blocks; the gradient heuristic uses training gradient norms to choose an order
- **Audit after freeze**: 81 novel continuous-phase arrays and their newly defined synthetic transfer labels; scoring only, no resulting model modification
- **Final**: the 145-case original held-out test split remains **WITHHELD**

The source `eck/index.html` includes a Canvas2D **INDEPENDENT EVIDENCE SURFACE** panel and code functions `evidencePredict`, `evidenceTarget`, `evidenceMSE`, `evidenceAudit`. The separate standalone regression `eck/test_eck059.cjs` (`node eck/test_eck059.cjs`) verifies the nine frozen outputs, 81 strictly continuous probes, source/validation/final counts and the reproducible new-task MSE figures. Direct extraction of the GitHub JavaScript passed syntax and produced all nine measured scores. The standalone Node regression has been committed but not independently executed; live browser and GitHub Pages behavior remain unverified.

### ASCII mesh

```text
  [[3×3×3 :: {[(3×3)3]} :: {{3×3}}³]]

      GEN 0              GEN 1              GEN 2
     00 01 02           09 10 11           18 19 20
     03 04 05    ==>    12 13 14    ==>    21 22 23
     06 07 08           15 16 17           24 25 26
                         |
               WEAK / MEDIUM / STRONG / FUSION
                         |
                  87 + 9 = 96 WEIGHTS
                         |
              TRAIN 438 / VALIDATE 146
                         |
              3 SEEDS × 3 FROZEN POLICIES
                         |
                  FREEZE CHECKPOINT
                         |
            +------------+-------------+
            |                          |
      81 CONTINUOUS PROBES       145 FINAL TRIPLES
      NEW SYNTHETIC TARGET           SEALED
            |
       POST-FREEZE SCORE
            |
        APPEND EVIDENCE
            |
          (0=-.)
```

### ECK-060 — Next natural bound

With all policies frozen, define independent *replicate transfer generators* by a predeclared task-seed sequence before computing their labels. Compare performance across several transfer tasks and account for uncertainty from both starting seeds and target-generator seeds. Preserve this ECK-059 result as an immutable audit record; do not tune the carrier policies to one transfer generator.
