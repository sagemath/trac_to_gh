
# Joint Sage-Combinat / Chevie workshop report
This is a report on the [joint Sage-Combinat / Chevie](http://wiki.sagemath.org/combinat/SageCombinatChevieWorkshopOrsay2010) workshop in Orsay, June 14-18th of 2010.

Participants:

 * Nicolas Borie, graduate student, Orsay
 * Adrien Boussicault, ATER, LIGM, Université Paris-Est
 * Tom Denton, graduate student, UC Davis
 * Florent Hivert, Prof, LITIS, Université de Rouen
 * Cédric Lecouvey, Prof, Université de Tours
 * Frank Lübeck, Aachen
 * Andrew Mathas, Associate Prof, University of Sydney
 * Jean Michel, DR, CNRS, Université Paris 7
 * Viviane Pons, graduate student, LIGM, Université Paris-Est
 * Nicolas M. Thiéry, MdC, Orsay


## Sage introduction
On Monday, Nicolas made a general presentation of Sage in the Math department in Orsay, followed by tutorials all day ran by Florent; not a great success, with only about 15 persons in the audience, but the tutorials were useful to the Sage newcomers in the workshop, and were also attended by four people from INRIA's [Algo project](http://www.inria.fr/recherche/equipes/algo.fr.html). The tutorials went from basic Sage usage to using and implementing algebraic structures. Two more tutorials (more on implementing algebraic structures; mercurial) were run later in the week.

At the end of the afternoon, all the workshop participants moved to Cernay. Here is what kept them busy all week.


## Combinatorial operators on polynomials
Adrien Boussicault, Vivianne Pons, and Nicolas Borie have been working hard on the design of "combinatorial operators on polynomials" (divided differences, schubert / demazure / grothendieck / key polynomials, ...), with all the variants (type A or other types, finite or infinite polynomials). In the process, they took advantage of the expertise of Florent, Cédric and Jean.

They also helped much the newcomers.


## Crystals
Tom Denton polished his FPSAC paper (and managed to get Nicolas to proofread it :-)), and started his work on his summer project on affine crystals. As a first step in this direction, he implemented (and pushed on the Sage-Combinat server!) a generic test for Stembridge rules. This feature was long desired, as it provides a very strong sanity check (or even, in many cases, a certificate of correctness).


## GAP and Sage
Many discussions, in particular with Frank Lübeck, went around  the differences in the design and development strategy between GAP and Sage. In very very short: Sage goes further in the modeling of mathematics at the potential price of complexity. GAP's development is of cathedral type, with an emphasis on packages, whereas Sage's goes for bazaar and shared ownership of the code. Everybody agrees on the relative merits of both strategies; everybody has his own belief about which one is more likely to succeed in the long run.

Also the release strategies are different. New GAP code can sometimes  take  time to become available to the user community, while Sage  has frequent releases containing a lot of very new code.  The Sage approach is good for people who want to use the new code, but it is more likely that code and interfaces will change later.

A fine point is GAP's position with respect to Sage.  Sage seems to consider GAP mainly as a library providing some algorithms  to compute with groups. But GAP has nowadays a much wider  functionality, it is a full system with a fairly sophisticated programming and user interface, it has a package concept that allows development of substantial extensions of GAP functionality without need for any changes of the core system. Also GAP has an interesting dynamic  type sytem  and method selection strategy (which does not map easily onto the more traditional object oriented concept of Python/Sage).

Therefore, for people who want to start a new software project and are looking for an appropriate platform, Sage and GAP may be competitors. By all means this should remain a sane reciprocal emulation, not a rivalry. Some thoughts in this direction: good interfaces and good reciprocal knowledge to minimize code duplication and foster cross pollination, proper acknowledgment, ...


## Sage's documentation
As pointed out by Frank Sage lacks overview documentation. The Sage community is well aware of this, and works in this direction, in particular with the ongoing effort around thematic tutorials (#8470), but there is still much work to do!

The feedback from Andrew, Frank, and Jean was most useful for improving the tutorial on implementing algebraic structures.

Documentation tickets created / worked on:

 * #9262 (Conversion from ReST markup to online text) created by nthiery
 * #9259 (Wrong markup on the documentation of CombinatorialClass.map) created by hivert

Florent worked hard on improving the rendering of the Sage documentation by mean of Sphinx; this includes better support for cross links (including to Python's online documentation), warnings upon broken links, ...

Florent also spent much time helping others, worked on the prereview of #9065: facade parents, and had long design discussions about them and related matters with Nicolas. Finally, he worked on the following tickets:

 * #9251: Lazy attribute does not properly handles the doc of Cython methods
 * #9256: Put Set in the category Sets()
 * #8924: __call__ for categories sets / enumeratedsets


## Future of Chevie
Much time was spent during the workshop (and previously during Sage Days 20) discussing, directly or indirectly, the future of Chevie.

 * The development of GAP3 stopped in 1997. It still compiles and runs well, and since the code base is simple and robust, it is likely to do so for the next ten years (with one caveat: it has to be compiled in 32 bits, which puts a limit on the amount of memory used by computations). There is still a lot of activity around Chevie by mathematicians in the area (e.g. Meinolf Geck, Gunter Malle, Cedric Bonnafé, Maria Chlouveraki, etc...); however, besides Jean, there are very few developers of the core system (actually every change to it goes through Jean);  there are  still quite some users of Chevie (notable ones have been at various times Lusztig, Serre, Shoji, Broué, etc...)

  Altogether, there is no urgency in porting code from Chevie just for the sake of making it run; however the difficulty of e.g. having a 64-bit version of GAP3 means that a port will become necessary some day  (in a few years?); when a complete port exists to another system one can expect the new developments to occur there.

  A remark on the license of GAP 3: the usage conditions of GAP 3 are more restrictive than GPL (see the doc/manual.* in GAP 3), and Frank evaluated that it would be close to impossible to change this. We suggest to make GAP 3 with Chevie an optional Sage spkg.

 * A variant of the core code for reflection groups and their representations will at some stage also become available in GAP 4 (and much more on representations of algebraic groups and groups of Lie type, ...). Some functionality in this direction is already available in the context of Lie algebras, see, e.g., http://www.gap-system.org/Manuals/doc/htm/ref/CHAP061.htm#SECT007.

 * Sage already has a native implementation of root systems and coxeter groups, including some unique features (and caveats, and slowness!). It also has a community of regular contributors (Daniel Bump, Mike Hansen, Nicolas Thiéry, ...) and regular users and occasional/potential contributors (Nicolas Borie, Tom Denton, Brant Jones, Steven Pon, Marco Robado, Franco Saliola, Anne Schilling, Justin Walker, ...). For many aspect, a native implementation is also desirable for tight integration with other features of Sage.

 * It seemed therefore unavoidable to get some duplication of efforts and features between Sage and GAP 4 (alas!). Much care should be taken to cross pollinate as much as possible, and share those features that can be wrapped naturally while they become available in GAP 4. Both sides are very much willing to go in this direction!

 * Some missing or underdeveloped features in Sage's Coxeter groups/root systems:

 * Invariants, fake degrees, conjugacy classes, representations

 * #9290: Coxeter groups implemented using their geometric representation

 * Type recognition for a dynkin diagram (algorithm? mostly graph isomorphism test against standard Cartan types)

 * Coxeter elements (algorithm?)

 * RootSystem and CartanType seem mostly redundant and should be merged.

 * #9291: Constructing a root system / coxeter group from a pair of matrices

 * Indexation of the positive/negative roots which depends only on the Cartan matrix (of the ambient group for parabolic subgroups), up to diagonal renormalization

 * #9292: Parabolic / Reflection subgroups

 * Fusion map: conjugacy class of W' => conjugacy class of W Special cases for S_n, hyperoctahedral group; otherwise, delegate to GAP, using permutation rep.

 * #9288: General (complex) reflection groups: the current implementation of Coxeter groups in Sage is in principle designed to open the door for such generalizations. In fact, even if this is not directly apparent, much of Sage's design was directly inspired from Chevie's. This should be better acknowledged.

  Jean is interested in this feature, and generally speaking about exploring the possibility of porting parts of Chevie to Sage and/or of making the design of these features in Sage compatible enough with Chevie to allow a port.

 * Representation theory of Coxeter/reflection groups: porting Chevie's data collections (and/or smoothly interfacing to them as a temporary measure) would definitely make sense. On the other hand algorithms for representations of general groups really belong to GAP 4. Much needs to be done to better expose such features in Sage, in particular around character tables (see #9293)!

 * Braid groups:
```
       sage: B = BraidGroup(W)
       sage: B.from_reduced_word(1,2,3)
```
   * Community?
   * Potential collaboration with Dehornoy
   * A notion of braid group exists for every finite complex reflection group
   * Implementation: Braid group elements have a canonical normal form, which is a concatenation of reduced words for the corresponding Coxeter group (because they are unique quotients of elements of the braid monoid, and each of them as a unique maximal factor).

 * GarsideWords (generalization of braid monoids)

 * Hecke algebras: once the fundamentals of Coxeter groups are available, the implementation thereof in Chevie takes just a couple pages of code (plus a database for the representation theory). As there are many people interested in this in Sage, it seems both natural and easy to port this to Sage (see also the current IwahoriHeckeAlgebraT HeckeAlgebraSymmetricGroupT, and http://wiki.sagemath.org/HeckeAlgebras). Andrew has general interest in that, but no current need; so he won't get immediately involved. We need a volunteer!

 * #9289: Puiseux polynomials.

 * Specht: Andrew wants to port his package to Sage. The main aim of this package is to provide a mechanism for computing the      decomposition matrices of symmetric groups and the degenerate and non-degenerate cyclotomic Hecke algebras of type G(r,1,n) and, more recently, of the cyclotomic quiver Hecke algebras of type A. This involves developing:
   * tableaux combinatorics of the symmetric groups, particularly that used in modular representation theory, and generalizations to multipartitions, multitableaux, ...
   * implementing the Grothendieck groups of these algebras. These Grothendieck groups, or rather the direct sum of them for n\ge0,  are known as the combinatorial Fock spaces and they are naturally integrable highest weight modules for the affine special  linear group. In characteristic zero the canonical, semi-canonical, ... bases of the Fock spaces correspond in a natural way to the bases of the Grothendieck groups given by the PIMs, the Specht modules, simple modules, Young modules, ...  The associated crystal graphs are easy to describe combinatorially.
   * generalizations of this combinatorics to the associated Schur algebras is also in Specht. 

The way that I have these working in gap is that I have, in python speak, a class -- which I call a "combinatorial crystal" --  which describes the categories that I am working with
   * symmetric groups in characteristic p, for all n
   * Hecke algebra of the symmetric group at an eth root of unity in characteristic p, for all n
   * (degenerate or non-degenerate_ cyclotomic Hecke algebra with "integral parameters" in characteristic p, for all n
   * various (cyclotomic) Schur algebras There are various choices encoded in the  can be here which amount to choosing the labelling of the crystal (e.g. whether the simples are labelled by restricted or regular partitions) and it is useful to allow for all of these different labellings.

  My main aim to to compute the decomposition matrices of these algebras. This is closely related to computing the (semi/quasi/...) canonical bases  in the combinatorial Fock spaces. I view the (images of the) PIMs, Specht modules, Young modules and simple modules as special cases of the Fock spaces/Grothendieck group and the decomposition matrices give the transition matirces between them. One of the main "achivements" of the Specht package was that it could, within limits, inductively compute the decomposition matrices of the symmetric groups and its Hecke algebras. It  did this by inducing the simple and projective modules in the Fock space and then using a lot of representation theory to decompose these modules. Now that these algebras are known to be Z-graded this adds some extra traction to these computations.

  As I already have a working platform for these calculations in gap, and time is short, my plan is to re-implement this code in Sage as I need it. So it might be quite a slow project. Implementing the Fock spaces is very quick. Computing the canonical bases in level 1 is almost trivial, whereas for higher levels this will require more work. The crystal graph machinery I can write very quickly. Implementing decomposition matrices as labelled matrices is again easy, but Sage probably provides a better mechanism for displaying them than this.

  In addition to working with the Grothendieck groups I would also like to work with the algebras and their modules directly. In gap I have code for doing this both inside chevie and in unpublished code. During the workshop I started writing some new code in Sage for computing with  the graded Specht modules. I have an implementation of this inside my working version of specht but it is a little clunky and difficult to  extend from type A to arbitrary level. The version that I have in Sage will generalise very easily once I write the necessary code  for multipartitions (PartitionTuples) and tableaux whose shape is a multipartition. The workshop was very helpful in letting me see how Sage worked and helping to motivate me to write something. In particular, I finally learnt, with some help from Nicolas and Florent, how to interface with gap3 which is essential for what I am currently doing as I need some specialized combinatorial functions that I  have in gap. At some point I will submit this for review and incorporation into Sage...

  In any case, following the workshop I am quite enthusiastic about Sage and I am now close to having some working code which is more succinct than the corresponding code in gap. More importantly this code is very easy to extend. It would be nice is permutations in Sage worked better, that   the general framework was more complete and really good if tab stops were two spaces rather than four. Apart from these quibbles Sage is rapidly growing on me and I expect to start pushing code to the patch server soon!

 * Frank pointed out several spots where Sage's code is much slower than it should be. For example, listing or iterating through the elements of a Coxeter group is ridiculously slow. The following challenge will be a good measure of Sage's progress in this area: running through all elements of the Coxeter group of type E8 in  less than 3 hours as GAP can do (see #9285).

  Other weak points he found is computations of Weyl characters (compare with `DominantCharacter` in GAP), or the enumerations of all roots (say of a root system of type E8, compare with Chevie).


## GAP3 interface
Jean and Nicolas worked on the gap3 distribution and spkg, merging in Marco's work to make it compilable from source on Macos and linux (windows/cygwin still to be tested). Using feedback from Jean and Andrew, Nicolas improved a bit the gap3 (and gap4) interface (introspection, help). The gap3/gap4 interfaces need further work to better convert back gap objects to Sage. Related tickets: #7890, #8327, #9293.

Jean and Nicolas also implemented a prototype of (parabolic) subgroups of Coxeter groups. Along the way, Nicolas made some little improvements to the Coxeter group code, and rebased Mike's Coxeter 3 patch.

Further work from Nicolas includes:

 * #7980: Implement generic support for parents with (multiple) realizations
 * Polishing Jason's tutorial on implementing algebraic structure
 * Reorganizing the various demos/tutorial for Sage-Combinat
 * Proof of concept for #9291


## Food!
And last, but not least, we enjoyed the cooking talents of all the participants, with gratin de quenelles_, crèpes_, ratatouille confite_, tartiflette_, gratin de pâtes au vin_, lentils curry, yummy pizzas, lots of good cheese (and wine accordingly :-) ), and cakes, tarte tatin, sorbet au coulis fruit rouge. And a nice mirabelle. Andrew commented that he had never eaten so well in a conference :-)_

This, together with good spirit from all, created a friendly, hard working, and cooperative atmosphere; this was far from trivial with most participants strongly involved in different, and potentially competing, projects, with quite different approaches in design and development strategies.
