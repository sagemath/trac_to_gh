
 When a comparison `obj1 rel obj2` (`rel` in `==,!=,<,>,<=,>=`) is requested Python / Sage delegates the query to member functions of the object(s). The symbolic ring is special in that to get a final answer it may be necessary to attempt a mathematical proof or simplification, which itself may even not be possible mathematically, let alone implementable. To still provide an answer the possible answers must be extended to three: `True/False/Unknown` (note #24345); and the computations to get the answer must be stacked with the fastest and most decisive procedures first.

On the other hand in many occasions users or Sage itself wants to know if an object is identical (without simplification) to the ring zero (`SR.zero()`) or any other object, which is the same as comparing the identity of `obj1-obj2` with `0`. There is a member of `Expression` namely `is_trivial_zero()` which does this and is very fast.

Up to March 2018 all `bool(obj1 rel obj2)` queries, with one of the objects a symbolic expression were delegated to `Expression.__nonzero__` that tried every trick to get a final answer. This situation is not satisfactory because users writing `if ex==0:` do not expect it. Even more hidden, generic code that tries to be helpful uses it and slows down unnecessarily in consequence.

The ticket #19162 outlines an interface that solves the problem. The roadmap to it however is unclear, even if there were interested reviewers. This page tries to collect all available information.


## Modules using `Expression.__nonzero__`

About 320 files under `src/sage` have doctests that, directly or indirectly, call `Expression.__nonzero__`. Notable unaffected major sections are finance, game_theory, homology, logic, matroids, monoids, probability, quadratic_forms, quivers, and sat. This is not surprising because usually it works, and performance is only a secondary consideration. Also the fact that equality has several different meanings with expressions is not widely appreciated.


## Relevant tickets

 * #17700 - wrong symbolic results in case the answer is not known
 * #19040 - defuse bool(x!=0) performance bomb
 * #19162 - symbolic relations metaticket
 * #21201 - Add a global is_trivial_zero function
 * #21862 - Symbolic methods work inconsistently on relational expressions
 * #24440 - Infinite loop from proving an expression
 * #24658 - Don't call Maxima with no-variable symbolic relation tests

