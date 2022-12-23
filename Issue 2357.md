# Issue 2357: make FLINT the default for ZZ['x']

Issue created by migration from https://trac.sagemath.org/ticket/2357

Original creator: mhansen

Original creation time: 2008-03-01 04:18:07

Assignee: malb




---

Comment by malb created at 2008-06-03 14:21:23

Changing assignee from malb to boothby.


---

Comment by malb created at 2008-06-03 14:21:23

I think Tom wanted to look into this.


---

Comment by burcin created at 2008-06-17 19:33:41

change ZZ[x] backend to FLINT


---

Attachment

attachment:trac2357_make_flint_default_for_ZZx.patch replaces `sage/rings/polynomial/polynomial_integer_dense_ntl.*` in the tree with `sage/rings/polynomial/polynomial_integer_dense_flint.*` and makes FLINT the default backend for ZZ[x] arithmetic.

FLINT 1.0.10 is required for the patch, you can get the spkg here:

http://sage.math.washington.edu/home/burcin/spkg/flint-1.0.10.spkg


---

Comment by burcin created at 2008-06-17 19:37:29

Changing priority from major to critical.


---

Comment by burcin created at 2008-06-17 19:37:29

Changing status from new to assigned.


---

Comment by burcin created at 2008-06-17 19:37:29

Changing assignee from boothby to burcin.


---

Comment by burcin created at 2008-06-17 19:37:29

Changing type from defect to enhancement.


---

Comment by burcin created at 2008-06-17 19:37:29

Changing component from commutative algebra to basic arithmetic.


---

Comment by craigcitro created at 2008-06-20 04:35:10

Changing keywords from "" to "editor_craigcitro".


---

Comment by dmharvey created at 2008-06-20 23:18:11

Now wait a second.... what if I *want* to use the NTL backend? Don't I even have that option any more? Why are we deleting all that code?


---

Comment by craigcitro created at 2008-06-21 01:00:19

No, no, we're not. Don't worry. There was some miscommunication about this at some point, but we're definitely keeping all the code, and we're going to have the polynomial ring constructor take a flag that lets you choose between FLINT and NTL, with FLINT being the new default.

I'm going to implement this soon (within a week, I think).


---

Comment by dmharvey created at 2008-06-21 01:39:25

Ok great.

(BTW the ticket number is so cool! Four consecutive primes!)


---

Comment by boothby created at 2008-06-24 08:20:09

Builds fine, all tests pass.  Coverage report:


```
Missing doctests:
         * div(self, other)


Possibly wrong (function name doesn't occur in doctests):
         * Integer content(self)
         * _repr(self, name=None, bint latex=False)
         * _latex_(self, name=None)
         * bint is_zero(self)
         * _pari_(self, variable=None)

```



---

Comment by craigcitro created at 2008-06-24 08:23:29

This needs someone (I'm going to do it soon, unless someone does it before me) to write some code that allows one to use `ZZ['x']` via NTL if one wishes, as a flag to the polynomial constructor.


---

Attachment


---

Comment by cwitty created at 2008-06-28 16:36:00

I've attached two patches.  The first, trac2357_make_flint_default_for_ZZx-edited.patch, is a hand-edited version of Burcin's patch that does not delete the NTL wrapper.  The second patch, trac2357-poly-ring-implementation.patch, adds an "implementation=" parameter to PolynomialRing, so that you get:

```
sage: PolynomialRing(ZZ, 'x')
Univariate Polynomial Ring in x over Integer Ring
sage: PolynomialRing(ZZ, 'x', implementation='NTL')
Univariate Polynomial Ring in x over Integer Ring (using NTL)
```

(the first version uses FLINT, which is the default).


---

Comment by dmharvey created at 2008-06-28 16:50:40

I haven't tried the code yet, but two comments just from glancing over it:

 * sparsenes => sparseness
 * Somewhere, possibly in the docstring for the polynomial ring constructor, should include a WARNING that FLINT's data representation is extremely bad for certain polynomials. It is a "more dense" representation than NTL, in the sense that each coefficient takes up the same amount of space, even zero coefficients. This means for example that you try to create the polynomial `2^10000000 x^10000000`, the NTL implementation is probably okay with that, but the FLINT one will run out of memory.


---

Comment by burcin created at 2008-06-30 10:00:48

revised patch adding FLINT wrappers for ZZ[x]


---

Attachment

attachment:trac2357_make_flint_default_for_ZZx-v2.patch fixes some problems with my previous patch. This version supersedes the older files.

Changes:
 - Add signal wrapper macros in various places to allow the user to interrupt the computation.
 - Handle division by zero in `__floordiv__`, which led to a crash with the previous patch.


---

Attachment

apply after burcin's v2 patch and carl's patch


---

Attachment

single bundle with all three relevant patches


---

Comment by craigcitro created at 2008-07-01 23:34:19

REFEREE REPORT:

This looks great! 

 * The FLINT wrapper is excellent. I haven't tried out too many corner cases beyond what the doctests do, but everything looks good. Of course, with FLINT, things are *really* fast: William and I tried out a benchmark that gets used in modular symbols code, and FLINT is something like 10-12X faster than NTL, and 2X as fast as Magma. And now it's in by default ...

 * Carl's work on setting up the `implementation='NTL'` is also great. It's very easy to use NTL if you choose, and Carl was also quite conscientious about this: notice the changes in the doctests, for instance.

Given how much work was already done, I've just gone ahead and fixed the small issues I ran into in another patch. There were a handful of small typos, and a few functions that weren't doctested, so I've added doctests for all of these. Both `polynomial_integer_dense_ntl.pyx` and `polynomial_integer_dense_flint.pyx` are now at 100% coverage. 

In doing this, I noticed that the `div` function has the same functionality as `//` (i.e. `__floordiv__`), so I removed it uniformly throughout sage. (I first removed it in this code, and then found out this was used elsewhere, so it had to go elsewhere, too.) In doing so, I also noticed that our convention for `a%b` in the case of `b<0` also went against all the standard conventions, so I fixed that. 

Someone should probably look over the changes I've made, and give them a positive review. Once that happens, this is ready to get merged. One can merge the three patches in order, or just use the bundle (which actually only has those three changesets) I've attached.


---

Comment by was created at 2008-07-02 18:31:08

I looked over the new patch added by Craig (the referee) and I'm happy with it.


---

Comment by mabshoff created at 2008-07-02 19:07:47

Merged default-flint-polys.hg in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-02 19:07:47

Resolution: fixed
