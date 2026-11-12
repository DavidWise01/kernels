# ECK-039 — Tested ASCII Neural Mesh and Boomerang Reversal Witness

## Exact mesh

```text
  [[ 3×3×3 :: {[(3×3)3]} :: {{3×3}}³ ]]

    GENERATION 0          GENERATION 1           GENERATION 2
    INPUT / 9             HIDDEN / 9             OUTPUT / 9

     00--01--02           09--10--11            18--19--20
     |   |   |            |   |   |             |   |   |
     03--04--05     ==>   12--13--14      ==>   21--22--23
     |   |   |            |   |   |             |   |   |
     06--07--08           15--16--17            24--25--26

     ===== two transitions, 33 directed synapses each =====
     W = WEAK      66 weights
     M = MEDIUM    66 weights
     S = STRONG    66 weights
     F = FUSION    66 weights
                   264 trainable weights

     729 ordered address states = (3×3)^3
     (a,b,c) -> positional encoding -> network -> target (c,b,a)
                                       (0=-.) fixed singlet
```

Important: horizontal/vertical lines within each square are planar coordinate guides, not additional feedforward synapses. Actual directed neural synapses connect the corresponding and four Manhattan-adjacent positions between consecutive 3×3 generations: 33 per transition, 66 overall. The singlet is an external symbolic anchor, not a neuron.

## Executed source-model tests

Executed by extracting the committed ECK-038 JavaScript model and running the actual functions in a JS harness. No modification of neural weights or training target was needed to obtain this result.

| Invariant | Result |
|---|---|
| Unique indexed neurons | 27 |
| Sparse directed neural synapses | 66 (33 + 33) |
| Carrier weights | 264 (66 × 4) |
| Unique ordered neural inputs | 729 |
| Distinct unordered permutation families | 165 |
| Train / validation / sealed final-test examples | 438 / 146 / 145 |
| Encode -> decode of every cubed ID | PASS |
| Apply address reversal twice gives original ID | PASS |
| All order permutations remain in same split | PASS |
| Identity path across both neural transitions for each address | PASS |

**Validation-order pair witness:** 65 unique (a,b,c) vs (c,b,a) pairs, no output collapse below 1e-8 after training. Output/input separation ratio was 0.4415036591456795.

**Reconstruction vs boomerang reversal.** A network trained for input reconstruction was assessed without retraining on the reverse target. The target for reversal is the 9-vector of positional weights 1:2:4/7 applied to (c,b,a).

| Metric (MSE) | Initial weights | After 24 accepted reconstruction iterations |
|---|---:|---:|
| Reconstruction, training | 0.016040253546982637 | 0.015973711397331836 |
| Reconstruction, validation | 0.016062412493932116 | 0.015995980158581256 |
| Reversal target, training | 0.03196481176522887 | 0.03193659589512802 |
| Reversal target, validation | 0.03199781212490777 | 0.03196977584528011 |

**Boundary:** although the network preserves a measurable distinction between order-reversed inputs, it is not trained to perform the reversal operator. The operator itself is an involution at the address-code level; the neural network does not yet realize it accurately. No final-test partition was measured by this harness. These are synthetic fixed-task observations, not experimentally validated physical force carrier claims.

**Next natural bound:** train with the explicit order-reversal target and retain input/output snapshots; freeze a baseline; evaluate generalization to genuinely new permutation families; test four-carrier ablations after training and preserve errors as witness packets.
