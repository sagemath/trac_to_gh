# Categories for the working mathematics programmer (status and roadmap)

This page describes the status and roadmap for the category framework
in Sage

With special thanks to Robert Bradshaw, Volker Braun, Nils Bruin,
Peter Bruin, Teresa Gomez-Diaz, Darij Grinberg, Mike Hansen, Florent
Hivert, Simon King, David Roe, Travis Scrimshaw, William Stein, and so
many others ... for design discussions. Special kudos go to Simon King
for all his work on the category infrastructure, in particular toward
optimizations.

## References

- Quickref card: sage.categories?
- [Primer](http://www.sagemath.org/doc/reference/categories/sage/categories/primer.html): sage.categories.primer?
- [Technical background](http://www.sagemath.org/doc/reference/categories/sage/categories/category.html#sage.categories.category.Category): Category?
- [Tutorial: How to implement new algebraic structures in Sage](http://www.sagemath.org/doc/thematic_tutorials/coercion_and_categories.html)

Design discussions:
- [Discussion on sage-devel, November 2009](http://groups.google.com/group/sage-devel/msg/d4065154e2e8cbd9)
- Long series of comments on [#10963](https://trac.sagemath.org/ticket/10963)
- ... TODO ...

## Technical dependencies

- abstract methods: [#6097](https://trac.sagemath.org/ticket/6097), [#6809](https://trac.sagemath.org/ticket/6809)
- lazy attributes: [#4371](https://trac.sagemath.org/ticket/4371), [#5793](https://trac.sagemath.org/ticket/5793)
- cached methods: ..., [#11115](https://trac.sagemath.org/ticket/11115), [#15759](https://trac.sagemath.org/ticket/15759)
- support for nested classes and dynamic classes: [#5483](https://trac.sagemath.org/ticket/5483), [#5985](https://trac.sagemath.org/ticket/5985), [#5986](https://trac.sagemath.org/ticket/5986), [#5991](https://trac.sagemath.org/ticket/5991), [#9107](https://trac.sagemath.org/ticket/9107)
- support for dynamic classes: [#5783](https://trac.sagemath.org/ticket/5783)
- support for lazy import: [#11224](https://trac.sagemath.org/ticket/11224), [#14722](https://trac.sagemath.org/ticket/14722), [#15648](https://trac.sagemath.org/ticket/15648)
- support for large hierarchy of classes and C3: [#11943](https://trac.sagemath.org/ticket/11943), [#13589](https://trac.sagemath.org/ticket/13589)
- unique representation: [#5120](https://trac.sagemath.org/ticket/5120)
- testsuites: [#6343](https://trac.sagemath.org/ticket/6343), [#7478](https://trac.sagemath.org/ticket/7478), [#8001](https://trac.sagemath.org/ticket/8001), [#16244](https://trac.sagemath.org/ticket/16244)
- misc: [#5449](https://trac.sagemath.org/ticket/5449), [#5598](https://trac.sagemath.org/ticket/5598), [#5967](https://trac.sagemath.org/ticket/5967), [#5979](https://trac.sagemath.org/ticket/5979), [#6000](https://trac.sagemath.org/ticket/6000), [#7251](https://trac.sagemath.org/ticket/7251), [#7259](https://trac.sagemath.org/ticket/7259), [#7420](https://trac.sagemath.org/ticket/7420), [#7421](https://trac.sagemath.org/ticket/7421)
- cache and memory management: [#15069](https://trac.sagemath.org/ticket/15069), [#13394](https://trac.sagemath.org/ticket/13394), [#13901](https://trac.sagemath.org/ticket/13901), [#15506](https://trac.sagemath.org/ticket/15506), ...

## Original ticket: [#5891](https://trac.sagemath.org/ticket/5891) (2009)

## Typical use cases

- Combinatorial Hopf algebras and generalizations of symmetric functions:
  [#8899](https://trac.sagemath.org/ticket/8899), [#11929](https://trac.sagemath.org/ticket/11929), [#15150](https://trac.sagemath.org/ticket/15150), [#6889](https://trac.sagemath.org/ticket/6889)
- [#6812](https://trac.sagemath.org/ticket/6812) Enumerate integer list up to the action of a Permutation Group
- Semigroups (upcoming), [#11111](https://trac.sagemath.org/ticket/11111)

## Categorification tickets

- polynomial rings: [#9944](https://trac.sagemath.org/ticket/9944)
- (combinatorial) modules and algebras: [#6136](https://trac.sagemath.org/ticket/6136), [#6137](https://trac.sagemath.org/ticket/6137), [#6138](https://trac.sagemath.org/ticket/6138)
- enumerated sets: [#7403](https://trac.sagemath.org/ticket/7403), [#7395](https://trac.sagemath.org/ticket/7395), [#7396](https://trac.sagemath.org/ticket/7396), [#7397](https://trac.sagemath.org/ticket/7397), [#10193](https://trac.sagemath.org/ticket/10193)
- families: [#7208](https://trac.sagemath.org/ticket/7208)
- root systems: [#4326](https://trac.sagemath.org/ticket/4326), [#3663](https://trac.sagemath.org/ticket/3663), [#5794](https://trac.sagemath.org/ticket/5794)
- rings: [#9138](https://trac.sagemath.org/ticket/9138)
- misc: [#7921](https://trac.sagemath.org/ticket/7921), [#8001](https://trac.sagemath.org/ticket/8001), [#8044](https://trac.sagemath.org/ticket/8044), [#8562](https://trac.sagemath.org/ticket/8562), [#8576](https://trac.sagemath.org/ticket/8576), [#8911](https://trac.sagemath.org/ticket/8911), [#9138](https://trac.sagemath.org/ticket/9138), [#9944](https://trac.sagemath.org/ticket/9944), [#12877](https://trac.sagemath.org/ticket/12877)

TODO:

- make a census of the parents that are not yet categorified
- Document that the old hierarchy of abstract classes (Ring, Field,
  ...) is deprecated (except for some of the element classes whose
  presence is critical for the performance of arithmetic)
- Actually start deprecating it. This requires all/most parents to be
  categorified.
  - [#804](https://trac.sagemath.org/ticket/804) Matrix should not inherit from AlgebraElement
  - [#15947](https://trac.sagemath.org/ticket/15947): Weaken types for _rmul_ and _lmul_  (Element instead of RingElement)
  - ...
- Move a lot of methods like base_ring, list, ... from Parent,
  Element, SageObject to the categories #????

## Category hierarchy

The current hierarchy includes all the mathematical categories of
Axiom and MuPAD (courtesy of Teresa Gomez Diaz)

TODO: add link to there + to the category graph

- [#15696](https://trac.sagemath.org/ticket/15696) Implement an_instance for more categories, and extend
  category_sample. This could benefit from [#15801](https://trac.sagemath.org/ticket/15801).
- Add more examples of parents (HELP!):
  Ultimately, this should be for all categories.
  Those are needed urgently:
  - Modules (for doctests for __mul__ / __rmul__ / ...)
  - Algebras (for doctests for __mul__ / __rmul__ / ...)

## Functorial constructions

- TensorProducts, Algebras, Quotients, Subquotients, Subobjects,
  IsomorphicImages: [#8881](https://trac.sagemath.org/ticket/8881), [#10963](https://trac.sagemath.org/ticket/10963)
- WithRealizations: [#7980](https://trac.sagemath.org/ticket/7980)
- Dual, graded dual: [#8881](https://trac.sagemath.org/ticket/8881), [#10963](https://trac.sagemath.org/ticket/10963), [#15647](https://trac.sagemath.org/ticket/15647)
- Graded: [#8881](https://trac.sagemath.org/ticket/8881), [#10963](https://trac.sagemath.org/ticket/10963), [#11688](https://trac.sagemath.org/ticket/11688)
- Cartesian products: [#8881](https://trac.sagemath.org/ticket/8881), [#16269](https://trac.sagemath.org/ticket/16269), [#10963](https://trac.sagemath.org/ticket/10963), [#15425](https://trac.sagemath.org/ticket/15425)
- Upcoming: CharacterRings

## Axioms

[Axioms primer](http://www.sagemath.org/doc/reference/categories/sage/categories/primer.html#axioms)


```
    sage: Groups() & Sets().Finite()
	Category of finite groups
	sage: (CommutativeAdditiveGroups() & Monoids()).Distributive().Division()
	Category of division rings
	sage: _ & Sets().Finite()
	Category of finite fields
```


- Original infrastructure: [#10963](https://trac.sagemath.org/ticket/10963)
- Alternative infrastructure proposal: [#15701](https://trac.sagemath.org/ticket/15701)
- Finite, Infinite, Associative, Unital, Commutative, Inverse (and
  additive variants), Division, Distributive, ...: [#10963](https://trac.sagemath.org/ticket/10963)
- FiniteDimensional: [#10963](https://trac.sagemath.org/ticket/10963), [#11111](https://trac.sagemath.org/ticket/11111)
- [#15475](https://trac.sagemath.org/ticket/15475) Reenable broken doctests in [#15473](https://trac.sagemath.org/ticket/15473) and [#15476](https://trac.sagemath.org/ticket/15476) when [#10963](https://trac.sagemath.org/ticket/10963) is merged

## Morphisms, homsets

- favor *_generators over gens(): [#15381](https://trac.sagemath.org/ticket/15381)

- Support for homsets: [#12876](https://trac.sagemath.org/ticket/12876), [#14793](https://trac.sagemath.org/ticket/14793), [#16275](https://trac.sagemath.org/ticket/16275), 

  use cached_function for handling the cache of Hom?

- Hom is *not* a covariant functorial construction. This kind of
  works for now, but the design and user interface needs to be
  discussed for the long run implementation. See [#10668](https://trac.sagemath.org/ticket/10668).

- Support for multivariate morphisms, i.e. morphisms (A x B) -> C
  where the specializations (A x b) -> C and and (a x B) -> C are
  morphisms for possibly different categories (see also [#8900](https://trac.sagemath.org/ticket/8900))

- Defining new inline operators, at least within the sage interpreter

## Handling of the category hierarchy

- Support for subcategory methods: [#12895](https://trac.sagemath.org/ticket/12895)
- Refinement of the category of a parent: ..., [#14471](https://trac.sagemath.org/ticket/14471)
- Support for full subcategories: [#16340](https://trac.sagemath.org/ticket/16340)
- Improve the terminology for the hierarchy relation between
  categories: [#16183](https://trac.sagemath.org/ticket/16183)

- join and meet are misnomers: since we speak of subcategories, then
  the implicit order is A <= B if A is a subcategory of B. So join and
  meet should be exchanged. Maybe it's too late for backward
  compatibility. Then maybe we could use "intersect" instead of
  join. For meet, there does not seem to be an obvious name, but it's
  also very seldom used at the user interface, so the backward
  compatibility issue is not that relevant.

  As a first step, [#10963](https://trac.sagemath.org/ticket/10963) implements the shortcuts & and | for join
  and meet.

## Containment

- Clarify in the doc and implement systematically the distinction
  between `P in MyCategory()` and `P.is_...()`

## Support for modules and algebras

- Modules(field) returns VectorSpaces(field): [#8881](https://trac.sagemath.org/ticket/8881)

- Mantra `P in Algebras` for testing if P is an algebra (over whatever
  ring): done; TODO: find the ticket that implemented that!
- Categories over base ring categories: [#15801](https://trac.sagemath.org/ticket/15801)

- Make modules, algebras, polynomial algebra (free commutative
  algebra?), free algebra, exterior algebras, ... into covariant
  functorial constructions.

- Clarification of the specifications of modules: [#16247](https://trac.sagemath.org/ticket/16247)
  - Modules(R) should be restricted to R commutative, with r * m = m * r ???
  - Algebras(R) should be a subcategory of Bimodules, not Modules???
  - What about ModulesWithBasis?
- [#15043](https://trac.sagemath.org/ticket/15043): Rename MagmaticAlgebras? to Algebras and Algebras to AssociativeUnitalAlgebras?
- The handling of multiplication (__mul__, ...) should be lifted to left / right modules
- Rings() could be a subcategory of Algebras(ZZ) (or coincide with
  it). CommutativeAdditiveGroups() could coincide with Modules(ZZ). In a similar vein, a field F could be
  in the category Modules(F). However, this can cause some trouble by
  introducing cross dependencies: ZZ involves constructing the
  category Rings() which uses Modules(ZZ) which itself uses ZZ. To
  avoid this, the current setup makes the basic categories (Groups(),
  Rings(), Modules(Rings())...) independent of any parent. This should probably be
  fixable later on by introducing more lazyness.

 - [#11068](https://trac.sagemath.org/ticket/11068) Basic implementation of one- and twosided ideals of non-commutative rings, and quotients by twosided ideals. Since there are rings that do not inherit from sage.rings.rings.Ring, it involves moving stuff to `sage.categories.rings.Rings.ParentMethods` (depends on [#9138](https://trac.sagemath.org/ticket/9138) and [#11115](https://trac.sagemath.org/ticket/11115))


TODO: reference the related discussions on sage-devel

## Optimization of the infrastructre

- [#11900](https://trac.sagemath.org/ticket/11900), [#11935](https://trac.sagemath.org/ticket/11935):
- [#15801](https://trac.sagemath.org/ticket/15801): categories over base ring categories
- [#16296](https://trac.sagemath.org/ticket/16296): Speed improvements for categories with axioms 

## Support for extension types

Works, up to some caveats (isinstance checks, ...). See also
sage.categories.examples.semigroups_cython for further experiments.

- [#7921](https://trac.sagemath.org/ticket/7921): Original approach via __getattr__
- [#20686](https://trac.sagemath.org/ticket/20686): optimizing
- Better would-be approach: treat extension types like the others

  This would require to add support for multiple inheritance from
  abstract classes in Cython (Robert Bradshaw: there is no theoretical
  obstructions; just someone needs to take care of it).
- [#15718](https://trac.sagemath.org/ticket/15718): __init_extra__ for Cython classes
## Documentation

- Main index page: [#7443](https://trac.sagemath.org/ticket/7443) TODO: refactor it (maybe as in [#16256](https://trac.sagemath.org/ticket/16256)); in
  particular emphasize the quickref
- Primer: [#5891](https://trac.sagemath.org/ticket/5891), [#10963](https://trac.sagemath.org/ticket/10963)
- Make sure that ? and ?? on categories / examples / ... point to the right place
  e.g.: Semigroups??, Semigroups().example()??
  Semigroups().parent_class?, Semigroups.element_class?
- Improve the documentation of the implementation of axioms: [#15643](https://trac.sagemath.org/ticket/15643)
- Explain category: Autogenerated overview documentation of a
  category: [#16363](https://trac.sagemath.org/ticket/16363)
- Writing and linking to generic documentation???

## Misc

- Add ObjectMethods for category objects that are not parents?

- Allow for super classes to also provide .Element?

- Infrastructure for sharing code between the following features:

  - Calculating whether an object provably belongs to a category
    (is_* methods)
  - Testing whether an object is in the category it claims to belong
    to (_test_* methods)

- Inheritance from existing parents
- How to specify the category of a parent (overloading of method / argument to __init__)
  See [#7921](https://trac.sagemath.org/ticket/7921)

- [#15303](https://trac.sagemath.org/ticket/15303) Coercion discovery fails to be transitive

---

Attachments:
 * [sage-category-graph.pdf](CategoriesRoadMap/sage-category-graph.pdf)
