Splitting of the review of the categories

Here are the categories/files which still need a review. They are all
essentially empty and already 100% doctested, so the review should be
super quick. David Kohel, Javier, or whoever please go ahead!

```
groupoid                       (positive prereview - Florent; Robert: please double check)
```

Everything below has a positive review.

---
Franco Saliola:

```
semigroups                       (positive review)
examples/semigroups              (positive review)
examples/semigroups_cythonx      (positive review as a proof of concept - Florent)
monoids                          (positive review)
examples/monoids                 (positive review)
examples/finite_semigroups       (positive review)
finite_semigroups                (positive review)
```

```
finite_monoids                           (positive review - Florent)
examples/finite_monoids                  (positive review - Florent)
commutative_additive_semigroups          (positive review - Florent)
examples/commutative_additive_semigroups (positive review - Florent)
commutative_additive_monoids             (positive review - Florent)
examples/commutative_additive_monoids    (positive review - Florent)
commutative_additive_groups              (positive review - Florent)
```

---
Nicolas (code by Florent)

```
examples/sets_cat                 (positive review)

enumerated_sets                   (positive review)
finite_enumerated_sets            (positive review)
examples/finite_enumerated_sets   (positive review)
infinite_enumerated_sets          (positive review)
examples/infinite_enumerated_sets (positive review)
```

---
Jason Bandlow:

```
modules_with_basis                (positive review)
```

---
Florent:

```
all                                         (positive review - Florent)
basic                                       (positive review - Florent)
sets_cat                                    (positive review)
algebras                                    (positive review - Anne)
algebras_with_basis                         (positive review)
examples/algebras_with_basis                (positive review)

hopf_algebras                               (positive review)
hopf_algebras_with_basis                    (positive review)
examples/hopf_algebras_with_basis           (positive review)

coalgebras                                  (positive review)
coalgebras_with_basis                       (positive review)

bialgebras                                  (positive review -- Essentially empty)
bialgebras_with_basis                       (positive review -- Essentially empty)

finite_dimensional_algebras_with_basis      (positive review)
finite_dimensional_bialgebras_with_basis    (positive review -- Essentially empty)
finite_dimensional_coalgebras_with_basis    (positive review -- Essentially empty)
finite_dimensional_hopf_algebras_with_basis (positive review -- Essentially empty)
finite_dimensional_modules_with_basis       (positive review -- Essentially empty)

graded_algebras                             (positive review -- Essentially empty)
graded_algebras_with_basis                  (positive review -- Essentially empty)
graded_bialgebras                           (positive review -- Essentially empty)
graded_bialgebras_with_basis                (positive review -- Essentially empty)
graded_coalgebras                           (positive review -- Essentially empty)
graded_coalgebras_with_basis                (positive review -- Essentially empty)
graded_hopf_algebras                        (positive review -- Essentially empty)
graded_hopf_algebras_with_basis             (positive review)
graded_modules                              (positive review -- Essentially empty)
graded_modules_with_basis                   (positive review -- Essentially empty)

group_algebras                              (Positive review -- Essentially empty)
```

David and Javier:

```
algebra_ideals                 (positive review - Javier)
algebra_modules                (positive review - Javier)
bimodules                      (positive review - Javier)
commutative_algebra_ideals     (positive review - Javier)
commutative_algebras           (positive review - Javier)
commutative_ring_ideals        (positive review - Javier)
commutative_rings              (positive review - Javier)
division_rings                 (positive review - Javier)
domains                        (positive review - Javier)
euclidean_domains              (positive review - Javier)
fields                         (positive review - David K)
finite_fields                  (positive review - David K)
g_sets                         (positive review - Florent)
gcd_domains                    (positive review - Javier)
integral_domains               (positive review - Javier)
left_modules                   (positive review - Javier)
matrix_algebras                (positive review - David K)
modular_abelian_varieties      (positive review - David K)
modules                        (positive review - David K)
monoid_algebras                (positive review - Javier)
number_fields                  (positive review - William Stein)
objects                        (positive review - David K)
partially_ordered_monoids      (positive review - Javier)
partially_ordered_sets         (positive review - Javier)
pointed_sets                   (positive review - David K)
principal_ideal_domains        (positive review - Javier)
quotient_fields                (positive review - Javier)
right_modules                  (positive review - Javier)
ring_ideals                    (positive review - Javier)
rings                          (positive review - Javier)
rngs                           (positive review - Javier)
sets_with_partial_maps         (positive review - David K)
schemes                        (positive review - David K)
unique_factorization_domains   (positive review - Javier)
vector_space                   (positive review - Javier)
```

Florent: The two following aim to define operads over some ring. I
marked them to be discussed since they are essentially empty and that
if we want to have operads say in the category of sets then we will
run into trouble with the naming convention... The proper setting
would maybe to define operads as functorial constructions like tensor
product...

Nicolas: Ok. Those were just the straightforward translations of the
corresponding categories in MuPAD-Combinat, but indeed the new
framework may allow for a better design. I'll split them out in a
separate patch, and we will see in the future what we will do with
them when we will have concrete examples.

```
operads                       (100% doctest)     (postponed for later)
operads_with_basis            (100% doctest)     (postponed for later)
```
