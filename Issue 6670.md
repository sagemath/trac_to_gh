# Issue 6670: [with patch, needs work] Port group algebras to the current coercion system

Issue created by migration from Trac.

Original creator: mraum

Original creation time: 2009-08-03 20:41:36

Assignee: mraum

This upgrades the group algebras to the current coercion system and fixes some issues of multiplication of group algebras A and B, satisfying A == B but not admitting coercion of elements.
This depends on #6669, which concerns homomorphisms from matrix group to other objects.


---

Attachment


---

Attachment

This is a rebase to 4.1.2


---

Comment by mraum created at 2009-10-22 16:52:04

Changing status from needs_work to needs_review.


---

Comment by mraum created at 2009-10-22 16:52:04

A patch for #6669 has been uploaded. This patch depends on it.


---

Comment by robertwb created at 2009-11-20 05:20:21

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2009-11-20 05:20:21

There's a lot of new code here, but it all looks good, and the doctests are fine too. 

Given the amount of category code that went into 4.3, we should make sure all tests pass when applied against that as well. (I tested against 4.2.)


---

Comment by mhansen created at 2009-11-29 07:10:00

Changing status from positive_review to needs_work.


---

Comment by mhansen created at 2009-11-29 07:10:00

Needs some work/rebasing for 4.3


---

Attachment

This is a rebase to 4.3alpha0 .


---

Comment by mraum created at 2009-12-01 16:48:02

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2010-01-20 09:30:37


```
	sage -t  devel/sage-main/sage/modular/modsym/space.py # Segfault
	sage -t  devel/sage-main/sage/algebras/group_algebra.py # 5 doctests failed
	sage -t  devel/sage-main/sage/interfaces/sage0.py # 1 doctests failed
```



---

Comment by robertwb created at 2010-01-20 09:30:37

Changing status from needs_review to needs_work.


---

Attachment

This applies cleanly to a fresh 4.3.1


---

Comment by mraum created at 2010-01-21 10:26:28

Changing status from needs_work to needs_review.


---

Comment by roed created at 2010-02-15 19:56:48

I'm hoping to take a look at this, but if someone else has time soon and wants to beat me to it, go for it.


---

Comment by pierre created at 2010-02-26 17:42:03

-- This patch does not apply on sage 4.3.3. Mercurial error message :

applying trac-6670-group_algebra-4.patch
patching file sage/algebras/group_algebra.py
Hunk #1 FAILED at 27
Hunk #7 succeeded at 358 with fuzz 2 (offset 9 lines).
Hunk #8 FAILED at 361
2 out of 10 hunks FAILED -- saving rejects to file sage/algebras/group_algebra.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac-6670-group_algebra-4.patch

-- You may want to have a look at the following related bug :

sage: G= SymmetricGroup(5); x, y= G.gens()
sage: A= GroupAlgebra(G)
sage: A( A(x) )

...fails. This bug may or may not be automatically fixed by your patch.

-- The docstring on line 367 of group_algebra.py mentions GroupAlgebra.__call__(), even though this method has been suppressed.


---

Comment by pierre created at 2010-02-26 17:42:03

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2010-07-03 09:47:16

I spent quite a while rebasing this to 4.5.alpha1. I will upload the rebased patch; but I was disappointed to find that there is still a serious issue that needs to be addressed.

The problem is that unpickling elements of group algebras created using the old code fails; you can't replace a class name with a function name and expect it to unpickle seamlessly. It ends up expecting `sage.algebras.group_algebra.GroupAlgebraElement` to be a class which can just be filled in with the pickled `__dict__` values, not a callable. This is what I get if I pickle a group algebra element without the patch, apply the patch and try to unpickle:

```
sage: load("/home/masiao/gpalg.sobj")
---------------------------------------------------------------------------
UnpicklingError                           Traceback (most recent call last)

/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/algebras/<ipython console> in <module>()

/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.load (sage/structure/sage_object.c:7577)()

/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:9175)()

UnpicklingError: NEWOBJ class argument isn't a type object
```



---

Attachment

Apply only this -- rebased against 4.5.alpha1 and docstrings ReSTified


---

Attachment


---

Attachment


---

Comment by mraum created at 2011-03-23 01:36:59

I added a completely new file containing the new implementation. The old one is deprecated now, but it still exists and pickling works. William suggested to remove the old implementation in 5.0, which I will open a ticket for as soon as this ticket is merged.


---

Comment by mraum created at 2011-03-23 01:36:59

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2011-06-25 08:09:58

For the bot:

Apply trac-6670-group_algebra-6.patch, trac-6670-group_algebra-7.patch


---

Comment by jhpalmieri created at 2011-07-22 20:29:55

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2011-07-22 20:29:55

Some minor comments:

 - The first line of the new file is redundant: "Group algebra of a group".  Maybe it should just be "Group algebras"?
 - The new file should be added to the reference manual, by adding an appropriate line to `sage/doc/en/reference/algebras.rst`.

More interesting:

 - Can you implement coercion from R[H] to R[G] if H is a subgroup of G, or more generally from R[H] to S[G] if there is a coercion from H to G and from R to S?  Then coercing from the base ring R to R[G] would just be the special case where R=S and H is the trivial group.

A more important issue: I'm not sure that I agree with the implementation.  I would have it inherit from `CombinatorialFreeModule`, and then unique representation is built in nicely so you don't have to cache the results as you do now.  You can also implement the Hopf algebra structure on the group algebra pretty easily.  For reference, you should look at the files

 - `sage/categories/examples/hopf_algebras_with_basis.py` for a simple (not very full-featured) implementation of group algebras.

 - `sage/algebras/steenrod/steenrod_algebra.py` for the implementation of the Steenrod algebra, including all of its Hopf algebra structure, inheriting from `CombinatorialFreeModule`.  This has a lot of things you don't need, but if you want to base the implementation on the first file, or if you want to modify the print representation of elements (which I recommend), you might be able to use this one to help fill in some details.


---

Comment by jhpalmieri created at 2011-07-28 22:46:11

Here's a new version, which makes the changes I suggested, and also adds some documentation at the top of the file.  I think I preserved all of the tests from the previous version, so we're not losing any functionality.  There are some new things, like an antipode and a comultiplication for elements.


---

Comment by jhpalmieri created at 2011-07-28 22:46:11

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by mraum created at 2011-07-29 16:54:14

I'm afraid the new version is quite similar to the original (though much better), so that I wouldn't be a legitimate reviewer. On the other hand, since the changes that you introduced are located in some function that you added I could review this part, as soon as I am back from holidays and you could review the other part. Do you think this is a legitimate solution?

One thing: The functor needs to be modified, using the new apply methods, that are available thanks to Simon's work. I will do this, if you don't do it first.


---

Comment by mraum created at 2011-07-31 19:57:07

I think it is important to note that on #11318 it is suggested unifying GroupAlgebra(G, A) and G.algebra(A). But I think we should still get this patch into Sage to have at least some more modern construction until we finally have the implementation anticipated in #11318.


---

Attachment

I attached a patch that changes the way functors are called.

Also I reviewed the parts that you implemented. That is, the transition to CombinatorialFreeModule. I would give this a positive review. So if you agree with the procedure that I described above and are fine with the rest of the code you can give this a positive review as a whole.


---

Comment by jhpalmieri created at 2011-08-02 16:55:51

Looks good to me.  The point about #11318 is a good one, although I don't like the way elements of `G.algebra(R)` are printed, compared to elements of `GroupAlgebra(G,R)`.


---

Comment by jhpalmieri created at 2011-08-02 16:55:51

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-08-18 22:01:43

Resolution: fixed
