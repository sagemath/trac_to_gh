# Issue 8988: Add support for toric varieties

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2010-05-18 09:07:51

Assignee: AlexGhitza

CC:  vbraun davidloeffler




---

Comment by novoselt created at 2010-05-18 09:46:12

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-05-18 10:04:47

I have marked this ticket as "needs review" despite of the broken doctest. Since that doctest seems to be unrelated, please review the ticket and state your opinion independently of it, without actually switching to "positive review". If nobody objects, I will shortly post a patch changing that doctest to the new output. As I understand, the purpose of that function is to actually try to "create some mess" and so there is no any meaning in a particular output.


---

Attachment

Oops, forgot to click replace existing file. Only the second patch should be applied. I have added a more formal reference to "Toric Varieties" book (and I checked with David Cox that it is OK to put a link to the draft). I have also moved the `kaehler_cone` function from Fano toric varieties to this patch.


---

Comment by novoselt created at 2010-05-21 03:59:54

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2010-05-21 03:59:54

I will make some adjustments to modules on which this patch depends, which may cause some changes in this patch as well. See
http://groups.google.com/group/sage-devel/browse_thread/thread/17743e17d67838ae


---

Comment by novoselt created at 2010-05-29 03:53:58

A couple little changes to account for changes in previous patches. Plus the fix for the broken doctest in symbolic.


---

Comment by novoselt created at 2010-05-29 19:25:24

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2010-06-03 03:46:39

Fixed errors caused previously by the code of `affine_patch` of subschemes and removed `NotImplementedError` from the beginning of this function.


---

Comment by vbraun created at 2010-06-03 18:46:50

I think the change in the random_test is because the patched sage/schemes/generic/algebraic_scheme now imports latex which imports random which changes the random seed. So it is all right, and fixing the random_test doctest is the right thing to do (TM).


---

Comment by vbraun created at 2010-06-13 21:38:03

I've read through the code and it looks good. 

One minor issue is that the `_repr_()` is not very descriptive. For example

```
sage: p0 = P1xP1.affine_patch(0)
sage: p0
Toric variety of dimension 2
sage: p0.embedding_morphism()
Scheme morphism:
  From: Toric variety of dimension 2
  To:   Toric variety of dimension 2
  Defn: Defined on coordinates by sending [z0 : z3] to
        [z0 : 1 : 1 : z3]
```

Maybe we could return `Toric variety (dim=2, #cones=4)` or so and include the number of generating cones to be able to distinguish the different varieties.

Apart from that I'd be happy to review it positively once the rewritten `Fan` is incorporated!


---

Comment by novoselt created at 2010-06-13 21:58:27

How about this?

```
Toric variety of dimension 2 with 4 affine patches
```

I would like to have a description in "plain English" and also patches seem to be more intrinsic to varieties than cones.

It may be good also to add an option for "extra" name, so that varieties from a named database (which is not there yet but I hope to have it eventually based on your code) can print as 

```
Toric variety of dimension 2 with 4 affine patches (P1xP1)
```

or maybe

```
P1xP1 (Toric variety of dimension 2 with 4 affine patches)
```

will be better. There is a way to rename anything in Sage, so

```
P1xP1
```

is very easy to do, but seems to be too different from the default one. Which one of three do you prefer?

It is also possible to print the base field, but I deliberately didn't do it so far because I always think of toric varieties as being defined over complex field. Plus, when the base field is a fraction field of a multivariable polynomial ring (as is the case with ambient spaces of anticanonical hypersurfaces in the next patch), the the description of the field gets really big and distracts from the toric variety itself.


---

Comment by novoselt created at 2010-06-13 21:59:43

And in your example the first variety should probably print as

```
Affine toric variety of dimension 2
```



---

Comment by vbraun created at 2010-06-14 00:33:59

Since there you can cover any given space always with more patches I'm a bit hesitant; The notation `Toric variety of dimension 2 with 4 affine patches` only makes sense once you translate it back into toric geometry. But plain English is definitely preferable.

I agree that the base field shouldn't be printed. Usually, it is going to be the same for all varieties the user constructs, so it is not a differentiating feature.


---

Comment by novoselt created at 2010-06-14 00:46:08

I agree... How about "Toric variety of dimension 2 covered by 4 affine patches"? Such a description a little more clearly refers to some particular cover, rather than arbitrary affine patches, and we do have a "canonical" one, returned by method `affine_patch(i)`.


---

Comment by novoselt created at 2010-06-17 06:46:13

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2010-06-17 06:53:42

In the spirit of planned changes to cones and fans I propose printing toric varieties as

```
2-d toric variety covered by 4 affine patches
```

and

```
2-d affine toric variety
```

for those generated by a single cone.


---

Comment by novoselt created at 2010-06-17 20:56:13

I've started a discussion
http://groups.google.com/group/sage-devel/browse_thread/thread/763d9ac5634bf8f3
as `symbolic/random_tests.py` gives now more grief (I am using 4.4.4.alpha0). Meanwhile I will update the doctest patch with new output...

Toric varieties are pretty much unchanged except for renaming fan-related functions and changing the representation.


---

Comment by novoselt created at 2010-06-17 20:56:13

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2010-06-17 22:50:21

Apply after the main patch. Broken doctests are fixed by setting random seed.


---

Attachment

Looks good now. One final nitpick is that the Kaehler cone lives in some `ToricLattice` which is somewhat confusing. I propose a `ToricVariety_field.Pic()` method returning a suitable lattice for the Kahler cone to live in. For now thats just `ZZ^k` but in the future we could be more fancy. Also, rename `kaehler_cone` -> `Kaehler_cone` since it is a name. Patch is attached, let me know what you think.


---

Comment by vbraun created at 2010-06-22 19:50:29

In the singular case the `Kaehler_cone` method actually computes the cone in the rational (Weyl) divisor class group = `A_{n-1}(X) \otimes_\ZZ \QQ`, and not in the Picard group. The updated patch changes the names accordingly.


---

Comment by vbraun created at 2010-06-23 14:31:39

Another thought: It would be nice if `ToricVariety_field.fan()` would take an optional argument and pass it on to the fan so one could write

```
X = ToricVariety(...)
X.fan(dim=1)
```

instead of

```
X.fan()(dim=1)
```



---

Comment by novoselt created at 2010-06-23 16:50:18

Neat idea! Will do in a few days ;-)


---

Comment by vbraun created at 2010-06-23 17:28:27

Yet another minor note: we might want to rename `ToricVariety.is_complete` to `ToricVariety.is_compact`. Not a big deal, but probably the better term in that context.


---

Comment by novoselt created at 2010-06-23 18:23:16

I think I used `is_complete` since compact does not quite make sense for arbitrary fields.

Regarding Kaehler cone - maybe the best option for now is just to remove it until divisors are actually implemented? The reason why it is here now is that I had to compute it for several varieties, so I wrote a quick function based on existing code without worrying too much about how well does it fit into the current picture. It seems that not very well...


---

Comment by vbraun created at 2010-06-24 10:32:28

I think we can't do much better for `Kaehler_cone`. I'll send a patch for divisors soon, maybe that'll help to make a more informed decision. In the meantime, here is a   patch with documentation fixes.


---

Comment by vbraun created at 2010-06-25 15:18:45

Added a Mori_vectors() method while I'm at it.


---

Attachment

Added parameters to `fan` method and changed the behaviour of `__call__` for fans in the case of no parameters at all - it seems more natural to return the fan in this case rather than all cones of all dimensions (which is what `cones` does).


---

Attachment

Apply this patch and doctest fix.


---

Attachment

Code to be included later.


---

Comment by novoselt created at 2010-06-29 06:07:05

Hi Volker,

I have done some work on the documentation from your patch and got completely stuck at `Mori_vectors`. Problems from smaller to bigger ones:

 * Are we allowed to use non-standard characters? I mean "a with dots" in Kaehler. I vaguely remember some discussion about it, but don't recall the result. Personally I prefer to use only characters that are easy to type and display for everyone. It does mean that some names are not accurately represented, but having one of such names I can vote in favour of it ;-) 

 * Your doctest uses toric varieties library which depends on this patch. It is a good non-trivial doctest, so I have no desire to remove it.

 * Why does it return vectors rather than cone (in the same way as `Kaehler_cone`)?

 * Kaehler and Mori cones are supposed to be dual, but they are not. Because Kaehler cone is given in some coordinates on the class group and Mori cone is given embedded into a higher dimensional space without a choice of a basis for its "real space". Both representations are probably useful and should be available, but it should be done consistently.

So:

 * I have removed my `kaehler_cone` method from the main patch, hopefully now you can give it a positive review together with symbolic doctest fixes only.

 * I have uploaded a new patch which contains your rebased changes and my edits to the documentation. It should NOT be applied here, I just wanted to save this code. As a patch it now just contains three new functions and can be easily moved to other tickets, where the library of toric varieties will be available to use in doctests. We will also need to take care of the last two points above.

Let me know what you think of all this.

Andrey


---

Comment by vbraun created at 2010-06-29 13:20:14

* I searched the sage-devel group but did not find any discussion. I think unicode docstrings are fine, but should be marked as `u"""documentation"""` which I did not do. Method names are and should be 7bit only.
  * For those than can't dualize the Kaehler cone manually I envision a `Mori_cone` method. Note that the `Mori_vectors` are (nrays+1)-component vectors, so this will never match the Kaehler cone. If you think that thats too confusing it could be renamed to `GLsM_charge_vectors()`, for example.
  * So shall we agree that Kahler/Mori cones should live in `QQ^nrays`? The advantage is that there is a canonical basis given by the rays, as you said.


---

Comment by novoselt created at 2010-06-29 14:21:59

I think (strongly ;-)) that `Kaehler_cone` method should return a cone in the class group in some basis, since such cones with some additions form a complete fan of the GKZ decomposition.

We should, however, have a clear way of going from divisors associated to rays to this basis and, perhaps, a way to go back. The first is easy, the i-th ray is represented by the i-th column of the Gale transform matrix. However, it may not be obvious and does not feel natural, since one has to involve functions of the fan, rather than toric variety directly.

For `Mori_cone` I would prefer to get the "traditional dual" of the `Kaehler_cone`, i.e. just the cone formed by facet normals, because it is confusing otherwise.

Again, there should be a clean way to go from any vector in the ambient space of `Mori_cone` to the longer vector with clear interpretation of each entry. I am OK with having a special function for the generators of the Mori cone and your proposed name is fine (although I have always seen this abbreviation as GLSM and would prefer all-capital version).

*Regarding this ticket*, my main point is that these functions require some more work and since they operate with divisors, perhaps we can move them to the ticket implementing divisors? Or, in order to avoid adding more stuff there and therefore potentially delaying it, I can create a new ticket for implementing all of the above (including, finally, `cone.dual` to make `Mori_cone` trivial).


---

Comment by vbraun created at 2010-06-29 15:05:02

In #9337 I did implement a `divisor.rational_class()` method that returns what you want. But there is no canonical way to go from divisor class -> divisor, so the computation of Kahler cones does not depend on the implementation of toric divisors.

I agree that `Mori_cone()` should return just `Kahler_cone().dual()` and we can implement that later.

GLSM is fine with me, too.

If you want to split off the Kahler cone computation from this ticket then thats fine with me. But we should then make it an independent ticket and not lump into toric divisors.


---

Comment by novoselt created at 2010-06-29 19:42:06

Moved cones to #9380. Patches remaining relevant to this ticket:

 * trac_8988_add_support_for_toric_varieties.patch (same as before, except that `kaehler_cone` is gone)

 * trac_8988_doctest_fix_for_symbolic_random_tests.patch

Any issues you still see with these two?


---

Comment by vbraun created at 2010-06-29 20:09:08

The rest is uncontroversial. The two patches apply cleanly to sage 4.4.4. Positive review!


---

Comment by vbraun created at 2010-06-29 20:09:08

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-07-01 08:36:31

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2010-07-01 08:36:31

I couldn't get this patch to apply unless I applied #9062, #8986, #9188 and #8987 beforehand. With these installed on top of 4.5.alpha1 (and no others), I got a doctest failure:

```
> sage -hg qapplied
trac_9062_add_support_for_toric_lattices.patch
trac_8986_add_support_for_convex_rational_polyhedral_cones.patch
trac_9188_fix_facet_normal.patch
trac_9188_fix_facet_normal_reviewer.patch
trac_8987_add_support_for_rational_polyhedral_fans.patch
trac_8987_add_enhanced_cones_and_fans.patch
trac_8987_review_changes.patch
trac_8987_repr_changes.patch
trac_8988_add_support_for_toric_varieties.patch
trac_8988_doctest_fix_for_symbolic_random_tests.patch
> sage -t sage/misc/sageinspect.py
sage -t  "devel/sage-reviewing/sage/misc/sageinspect.py"
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/misc/sageinspect.py", line 983:
    sage: sage_getvariablename(A)
Expected:
    ['A', 'B']
Got:
    ['B', 'A']
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_22
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_sageinspect.py
         [2.9 s]

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage-reviewing/sage/misc/sageinspect.py"
Total time for all tests: 2.9 seconds
```


I have not got the foggiest clue why toric varieties can possibly have anything to do with this; it just looks like the doctests for sageinspect are sensitive to exactly what memory addresses things get stored at. I will put this back to "needs review" for now, but upload a tiny patch that sorts the variable name list; if you folks agree that it looks harmless, then we can go back to positive review.


---

Comment by davidloeffler created at 2010-07-01 08:37:14

fix a broken doctest in sageinspect


---

Comment by davidloeffler created at 2010-07-01 08:37:38

Changing status from needs_work to needs_review.


---

Attachment

Here's the fix.


---

Comment by vbraun created at 2010-07-01 09:35:43

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2010-07-01 09:35:43

The order of the output of `sage_getvariablename` is in the memory order of some python `dict`, so the doctest had to fail at one point. I grepped through the sage library and the only use of `sage_getvariablename` is in `sage/matrix/matrix0.pyx` where the order of items is actually not used. 

So davidloeffler's fix of sorting the output of `sage_getvariablename` is safe and the right thing to do to return a deterministic output. I give it a positive review.


---

Comment by novoselt created at 2010-07-01 16:28:31

I made a systematic mistake in doctests of `__cmp__`  methods of all patches, discovered in #9062. So now I am posting these one-line patches to fix them, please review!


---

Comment by novoselt created at 2010-07-01 16:28:31

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by novoselt created at 2010-07-01 16:28:58

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2010-07-01 16:32:31

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2010-07-01 16:32:31

Positive review of the doctest fix!


---

Comment by davidloeffler created at 2010-07-01 17:55:20

These patches won't apply without #8986, which is currently at "needs work", so it can't be merged at present.


---

Comment by davidloeffler created at 2010-07-01 17:55:20

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2010-07-02 10:03:12

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-07-02 10:03:20

Changing status from needs_review to positive_review.


---

Comment by cwitty created at 2010-07-16 04:34:02

See #9514 for a patch that fixes the random_tests doctest issue.


---

Comment by novoselt created at 2010-07-16 15:33:08

It will be better to pre-merge #9514 instead of the doctest fix from this ticket. Then the following patches must be applied:

 * trac_8988_add_support_for_toric_varieties.patch
 * trac_8988-sageinspect_doctest_fix.patch
 * trac_8988_cmp_fix.patch


---

Comment by mpatel created at 2010-07-20 08:57:02

Resolution: fixed


---

Comment by mpatel created at 2010-07-20 08:57:02

There's a doctest failure in SageNB's `sageinspect.py`:

```python
$ ./sage -t -long  local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py
sage -t -long "local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py"
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.1-rm/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py", line 997:
    sage: sage_getvariablename(A)
Expected:
    ['A', 'B']
Got:
    ['B', 'A']
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_22
***Test Failed*** 1 failures.
```

I'm closing this ticket as fixed but have opened #9554 as a blocker for 4.5.2.
