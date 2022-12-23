# Issue 9772: Abelian groups

Issue created by migration from https://trac.sagemath.org/ticket/9773

Original creator: rbeezer

Original creation time: 2010-08-20 22:55:53

Assignee: AlexGhitza

CC:  davidloeffler cremona was nthiery boothby jason kcrisman mhansen justin alexghitza

This patch will implement abelian groups, both additive and multiplicative, finite and infinite, under a common abstract class, using machinery for quotients of modules over `ZZ`.  This will make subgroups, intersections of subgroups, isomorphism classes, and quotient groups possible.  Generators may be of any type, so long as they support the minimal operations required.


---

Attachment

AAG is the class of additive abelian groups.  This is an infinite group with a subgroup and a quotient.  (Typically quotients lose the generators and are "generic" but not in this example.)


```
sage: A=AAG([3,4,0])
sage: A.gens()
((2, 3, 0), (0, 0, 1))
sage: A.0.order()
12
sage: A.1.order()
+Infinity
sage: B=A.subgroup([A.1])
sage: B
Infinite additive abelian group isomorphic to Z with generator(s): (0, 0, 1)
sage: C=A/B
sage: C
Finite additive abelian group isomorphic to Z_12 with generator(s): (2, 3, 0)
```


GUN is a constructor of Groups of Units Mod n.  It employs MAG, the class of multiplicative abelian groups.  This is an intersection of two subgroups, and then a Cayley table is free (in the category of multiplicative groups).


```
sage: G=GUN(72)
sage: G.list()
[1, 65, 49, 17, 25, 41, 55, 47, 31, 71, 7, 23, 37, 29, 13, 53, 61, 5, 19, 11, 67, 35, 43, 59]
sage: G.subgroup([71,7])
Finite multiplicative abelian group isomorphic to Z_2 + Z_6 with generator(s): 55, 65
sage: K=G.subgroup([71,7])
sage: K.list()
[1, 65, 49, 17, 25, 41, 55, 47, 31, 71, 7, 23]
sage: L=G.subgroup([13,7])
sage: L
Finite multiplicative abelian group isomorphic to Z_2 + Z_6 with generator(s): 55, 61
sage: L.list()
[1, 61, 49, 37, 25, 13, 55, 43, 31, 19, 7, 67]
sage: M=K.intersection(L)
sage: M.list()
[1, 7, 49, 55, 25, 31]
sage: M
Finite multiplicative abelian group isomorphic to Z_6 with generator(s): 7
sage: M.cayley_table()
*  a b c d e f
 +------------
a| a b c d e f
b| b c d e f a
c| c d e f a b
d| d e f a b c
e| e f a b c d
f| f a b c d e
```


This is an example from the current additive abelian wrapper class.  It shows the generators keyword allowing arbitrary elements to form the group, so long as they know how to add.  GUN above is similar, but with multiplication.



```
sage: E = EllipticCurve('30a2')
sage: pts = [E(4,-7,1), E(7/4, -11/8, 1), E(3, -2, 1)]
sage: M=AAG([3,2,2], generators=pts)
sage: M.list()
[(0 : 1 : 0), (13 : -52 : 1), (4 : -7 : 1), (3 : -2 : 1), (4 : 2 : 1), (13 : 38 : 1), (7/4 : -11/8 : 1), (1 : -4 : 1), (-2 : -7 : 1), (-5 : 2 : 1), (-2 : 8 : 1), (1 : 2 : 1)]
sage: M.gens()
((7/4 : -11/8 : 1), (13 : -52 : 1))
sage: N=M.subgroup([M.1])
sage: N
Finite additive abelian group isomorphic to Z_6 with generator(s): (13 : -52 : 1)
sage: N.list()
[(0 : 1 : 0), (13 : -52 : 1), (4 : -7 : 1), (3 : -2 : 1), (4 : 2 : 1), (13 : 38 : 1)]
```


There is lots to do here still: different filenames, different class names, error-checking, doctests, comparisons, and so on.  But the code seems to be working.  I'm not 100% confident on the `__call__` method of the main abstract class and I don't know if I need some things to support coercion better.  Any advice or comments at this stage would be appreciated before I begin to clean this all up.


---

Comment by rbeezer created at 2010-08-20 23:14:32

Changing status from new to needs_info.


---

Comment by rbeezer created at 2010-08-20 23:14:32

Changing type from defect to enhancement.


---

Comment by jhpalmieri created at 2010-08-21 00:39:07

Will this interact at all with the class `CombinatorialFreeModule`?  I don't know what the long term plans are, or even if there are any, for connecting this with `FreeModule`, but the combinatorial version has some nice features.

Also, how do you define *R* or *Q* as additive abelian groups with this setup?


---

Comment by rbeezer created at 2010-08-21 01:35:26

Replying to [comment:2 jhpalmieri]:

Hi John,

Thanks for the good questions.  I began this when I tried to implement a multiplicative group in concert with the work at #6449.  So I really didn't even have groups like *R* and *Q* in mind.  Truth-in-advertising would suggest I sprinkle in some "finitely generated" qualifiers in class names and filenames.

I've plugged this into the categories framework as groups, but hadn't thought about modules.  I'll go take a look at all that to see how this might fit in.  Maybe Nicolas Thiery will have some ideas as well.

Thanks again,
Rob


---

Comment by rbeezer created at 2010-08-23 07:01:26

Replying to [comment:2 jhpalmieri]:
> Will this interact at all with the class `CombinatorialFreeModule`?  I don't know what the long term plans are, or even if there are any, for connecting this with `FreeModule`, but the combinatorial version has some nice features.

I looked at these two classes.  Generally they seem to require the same ring in each "component", whereas the FGP_Module class allows for diffferent rings in each component, such as in creating something like Z_3 x Z_4.  So I don't see an abvious way to leverage these, but maybe I'm missing something.

Rob


---

Comment by mpatel created at 2010-08-23 09:58:13

# To the release manager

Please close #9694 when this ticket is merged.


---

Attachment


---

Comment by rbeezer created at 2010-09-02 04:23:21

Code is stablizing in draft 2 patch, and I'm starting to write the doctests.  Still uncertain about `__call__` and now its interactions with `__contains__`.

There are liberal comments in the code and the `units_modn` module has a rather complete demo of functionality.


---

Comment by zimmerma created at 2010-10-28 09:29:33

Question: does this patch solve #10181?

Paul Zimmermann


---

Comment by jhpalmieri created at 2010-10-28 19:31:38

Replying to [comment:8 zimmerma]:
> Question: does this patch solve #10181?

While we're at it, how about #9940?


---

Comment by rbeezer created at 2010-10-31 17:41:16

Replying to [comment:8 zimmerma]:
> Question: does this patch solve #10181?

Short answer:  this could speed up `subgroups()` by a factor of 8, if my experiments are right.  We won't beat Magma, but we won't be embarassed on really small examples.  This patch does not have a `subgroups()` method yet, but could be easy to add.

Full details at #10181.  Thanks for asking.

Rob


---

Comment by rbeezer created at 2010-10-31 17:43:29

Replying to [comment:9 jhpalmieri]:
> While we're at it, how about #9940?

This patch has code that is in pretty good shape (IMHO).  It still needs doctests, plus things like an equality method.  So it could fix #9440 if the equality method is done right?


---

Comment by rbeezer created at 2011-03-23 20:55:31

Justin - no documentation to speak of, but look at the derived classes to get a feel for how this might work.

Any insights or ideas you might have would be helpful before I try to finish this off later this spring.

Rob


---

Attachment

Draft 3 patch is actually about a year old at time of posting (for safe-keeping).  Category code changed out from under me, so I had to start over last summer.  This applies on 5.0.rc0, builds, and simple testing of the abstract classes seems to be successful. 

Needs documentation, some changes, and practical derived classes, like totally abstract cyclic groups, the multiplicative subgroup of units mod n, etc.  IIRC, there are examples of these in the previous drafts.  I fully intend to work on this over the summer.


---

Comment by rbeezer created at 2012-07-16 03:05:37

I keep plugging away at this.  Some improvement by exploiting category code.  Totally reworked, so most of my comments above are obsolete.

Draft 4 patch is very functional, with the following caveats that I cannot figure out.  Assistance greatly appreciated if you can provide advice or specific pointers.  There is quite a bit of functionality demonstrated in the module-level doctests.  Little or no error-checking yet.

  1.  `_element_constructor()` works fine with module elements, which is to be expected, since it is copied verbatim from there.  I cannot seem to make it accept reasonable elements of the parent of the generators for subsequent processing without totally breaking extensive doctests.
  1.  The multiplicative version does not pass the `TestSuite` framework.  Likely the implementation of multiplicative operators on top of an additive class (FGP modules) is to blame?

I've tried to add copious comments to make it easier to navigate the code.  More specific problem areas are flagged with `*PROBLEM*`.


---

Attachment


---

Comment by rbeezer created at 2012-07-16 04:05:21

Just replaced the patch.  Realized the `_user_to_optimized()` method needed to be in the parent class, not the element class.  Then had some partial success getting `_element_constructor()` to work, but it still fails on subgroups - `.smith_form_gens()` for FGP modules is the suspect.

Test suite on the elliptic curve example was testing the wrong instance - as corrected one test fails, so it is commented out, but should be experimented with to determine root cause.


---

Attachment

draft-4 failed to include "__init__.py" in the patch - that has been corrected in draft-5.

David Roe helped me rework the initialization of the module class, so now the test suite is not doing additive tests on the multiplicative classes.  And I also believe I understand the problems with the element constructor (again with David's help).  So I think I'm over the hump on this one now.

Long list of tests at module level are all passing, except one test suite (which I think I understand and can correct).  A few other test suites commented-out, but I think they are correctable also.


---

Attachment


---

Comment by rbeezer created at 2012-08-08 03:56:25

draft-6 patch is darn close to functional.  Lots of doctests, all passing.  Lots of code pushed up to abstract class.  Much more to do on docstrings.

One *real* edit in `FGP_Module` code.  Remainder are stray print statements to be cleaned up.


---

Comment by AlexGhitza created at 2012-08-30 05:47:05

Hi Rob,

Just a quick note to say that I've played with draft-6 a bit (mainly with the `UnitsModmGroup`), and I very much like it.  Thanks for all the work you've put into this (and the patience!).


---

Comment by rbeezer created at 2012-08-30 21:20:56

Replying to [comment:18 AlexGhitza]:
> Just a quick note to say that I've played with draft-6 a bit (mainly with the `UnitsModmGroup`), and I very much like it.  Thanks for all the work you've put into this (and the patience!).

Thanks very much, Alex, for the encouragement.  Still lots of docstrings to work on, but making (slow) progress, since classes started recently.  Soon.  ;-)


---

Comment by zimmerma created at 2013-01-08 08:27:39

any progress on this? Which info is needed?

Paul


---

Comment by rbeezer created at 2013-11-09 05:51:08

Update: v6 patch will compain about one hunk not applying - just ignore it, it is no longer needed.  

On 5.12: compiles and passes all tests.

Basically I think the code is solid on this one, but it needs extensive work to fully document and doctest.  And then it would be a big effort to slowly integrate in.


---

Comment by kcrisman created at 2015-02-12 15:03:00

Hey Rob, what's the status here?  If one (say, me) were to have a student who knows some algebra and is a solid programmer, could they finish up what is remaining?  Could be really useful stuff.


---

Comment by mcognetta created at 2015-02-19 03:50:37

Replying to [comment:26 kcrisman]:
> Hey Rob, what's the status here?  If one (say, me) were to have a student who knows some algebra and is a solid programmer, could they finish up what is remaining?  Could be really useful stuff.

I am also interested in this. I am a student as well with algebra coursework under my belt. If there is still a need for this and you would like to work together, I am down.
