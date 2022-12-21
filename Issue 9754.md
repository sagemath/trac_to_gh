# Issue 9754: Add random unimodular and subspaces matrices to matrix/constructor.py

Issue created by migration from Trac.

Original creator: bwonderly

Original creation time: 2010-08-17 00:02:37

Assignee: jason, was

CC:  rbeezer wdj mhansen

This depends on #9720, so first apply the v3 patch from there.  Two routines are added.  One generates matrices (using methods from the v3 patch) whose right and left null spaces, row space, and column space have desirable properties.  The other creates random unimodular matrices. 


---

Attachment


---

Comment by bwonderly created at 2010-08-17 00:10:40

Changing status from new to needs_review.


---

Comment by bwonderly created at 2010-08-27 23:24:50

revised to fit generalization of random_matrix constructor.  Apply v4 from #9720 and v2 from #9803 and go from there.


---

Attachment

The most recent patch is independent of #9802.  There are some revisions to the documentation, but the majority of the work is to fit the routines to #9803.  Once this ticket, or #9802 gets a positive review, I will rebase the other to have all the routines included in one patch.


---

Comment by wdj created at 2010-08-30 00:16:51

Applies and passes sage -testall. Does what it says it does. Again, looks like a very useful addition for teachers of linear algebra.

Positive review from me.


---

Attachment

rebased to go on top of #9802.  So apply v4 from #9720, v2 from #9803, and v2 from #9802


---

Comment by bwonderly created at 2010-08-30 00:49:02

The v3 patch is a rebase to include #9802.  First apply v4 from #9720, then v2 from #9803, and finally v2 from #9802 and go from there.


---

Comment by rbeezer created at 2010-08-30 03:42:14

I've applied the rebased version successfully and am running tests right now, so I'll report back here.

David - thanks for looking at these!  They are good enough that I almost wish I had a section of linear algebra this term.

Mike - Do you want to look over any of this?  #9803 is where I made the changes to accomodate the non-global-namespace versions, so that is the place where your comments were addressed.  If not, I'll have Billy get these marked up for the release manager.

Thanks,
Rob


---

Comment by bwonderly created at 2010-08-30 05:02:26

Fixed bug making all output matrices square.


---

Attachment

There was a bug in the v3 patch making all output matrices square, which is now fixed in the v4 patch.


---

Comment by rbeezer created at 2010-08-30 18:07:02

Changing status from needs_review to needs_work.


---

Comment by rbeezer created at 2010-08-30 18:07:02

I was in the process of adding some doctests to be sure the row/column bug was fixed, and also homed in on:


```
if nullity>rows:
    raise ValueError("nullity cannot exceed the number of rows or columns.")
```


since there should be two conditions to check:  rank < nrows,  rank < ncols.

I got mightly confused since I forgot that `nullity()` is the *left* nullity.  Your other routines specify rank as an input, and for consistency I think this one should as well.  Maybe you think nullity as you design the matrix, and that is fine, but inputs and error messages would be clearer if you avoided the distinction between left and right kernels.  (This change in inputs also stopped me once.)

Can you change the input to have `rank=` and adjust tests (doctests and actual error-checks in the code) accordingly?  You can keep your `nullity_generator` in the code, but lets label it as `left_nullity_generator` to make it clear that  rank + nullity  is the number of *rows* not the number of columns.

So there really isn't anything wrong here, but we have a chance to not add further to Sage's left/right, row/column dichotomy/confusion.  It'll be worth the effort.

Here are the doctests I was adding for the `B` matrix of `random_subspaces_matrix()`:


```
        sage: (B.nrows(), B.ncols())
        (6, 8)
        sage: all([x in ZZ for x in A.list()])
        True
```



```
        sage: all([x in ZZ for x in B_expanded.list()])
```


Rob


---

Attachment

Revisions to random_subspaces_matrix to make to replace ``nullity`` input with ``rank``.


---

Comment by bwonderly created at 2010-08-30 21:43:16

I made the suggested changes in the v5 patch (making rank the input, changing the test to rank<rows, rank<columns, documentation stuff).  Let me know if i missed anything.


---

Attachment

1.  With v5 patch:


```
sage: A=random_matrix(QQ, 5,9,algorithm='subspaces',rank=5)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<snip>

/sage/dev/local/lib/python2.6/site-packages/sage/matrix/constructor.pyc in random_matrix(ring, nrows, ncols, algorithm, *args, **kwds)
   1160         return A
   1161     elif algorithm == 'echelon_form':
-> 1162         return random_rref_matrix(parent, *args, **kwds)
   1163     elif algorithm == 'echelonizable':
   1164         return random_echelonizable_matrix(parent, *args, **kwds)

/sage/dev/local/lib/python2.6/site-packages/sage/matrix/constructor.pyc in random_rref_matrix(parent, num_pivots)
   1689         raise TypeError("the number of pivots must be an integer.")
   1690     if num_pivots<=0:
-> 1691         raise ValueError("the number of pivots must be greater than zero.")
   1692     ring = parent.base_ring()
   1693     if not ring.is_exact():

ValueError: the number of pivots must be greater than zero.
```


With `rank=rows` the L matrix is empty (ie no rows), which is an interesting case (and often the source of student questions).  It seems to fail since your routines will not build a matrix in echelon form with no pivots.  Nor will it build an echelonizable matrix with zero rank.

However, both are possible - a matrix with no pivots must be totally zeros.  A matrix of rank zero is totally zeros.  Since you have coded this carefully, I think everything works - if you just let it happen.

Patch shows how to do this.  Apply it to experiment, and read the patch, then pop it off and make the necessary changes yourself if you believe it is OK.  I've only tested this a little bit, so don't presume it has my seal-of-approval.  Adjust error messages and tests.

2.  In 'subspaces" routine near the end.  Do you need to augment B to form N, and then strip out parts of M?  Seems you just produce the identity in the right "half" and then throw it away.  Will the following work?


```
J=K.stack(L)
return J.inverse()*B
```


What you have is clearer, but a comment or two in the source could replace the extra statements.


---

Comment by bwonderly created at 2010-08-31 19:18:25

Changed random_rref_matrix routine to allow for input of rank=0


---

Attachment

v6 has the changes to allow for rank=0 input in random_rref_matrices, as well as changes to the doctests.  The end of the subspaces routine was also altered.  It tests and builds fine on my end, let me know if there is anything else.


---

Comment by rbeezer created at 2010-09-02 02:15:10

Changing status from needs_work to needs_review.


---

Attachment

The v6 patch looks real good - corrects rows/columns bug, fixes up the rank-nullity-confusion, and streamlines the end of the code for the "subspaces" routine (with comments replacing code for explanation).  Works well, passes all tests and docs look good.

I noticed one test in the "echelonizable" routine that talks about "just building a zero matrix" if you need it (I'd added that verbiage earlier).  Its gone in v7, that's the only change.  v7 patch still has Billy's name in it and is the full patch otherwise.

I think this is done, at least I am checking-off on the changes leading to the v6 patch.

Billy - you could/should sign off on the little change to make v7.

David - you can weigh-in further if you like, or not.  If so, we can leave this open for a few days.  If not, we'll wrap this all up.  Thanks so much for all your help and encouragement reviewing Billy's summer project.


---

Comment by bwonderly created at 2010-09-03 06:34:56

The v7 patch looks fine to me.  Thanks to everyone who helped out on this.


---

Comment by wdj created at 2010-09-04 00:26:39

Does this only depend on #9720? There are some inconsistent statements with regard to the dependencies in the comments above.


---

Comment by rbeezer created at 2010-09-04 00:43:23

Replying to [comment:13 wdj]:
> Does this only depend on #9720? There are some inconsistent statements with regard to the dependencies in the comments above.

Hi David,

No, it needs all the prior patches.  The full chain is:

#9720, #9803, #9802, #9754

each one depends on the previous one in the list, so you'll have to apply three patches to test this one.  But this should be the end (ie you could use these to prepare for class, etc).

Thanks,
Rob


---

Comment by wdj created at 2010-09-05 09:42:59

I could not get this sequence to apply to 4.5.3.a0. What version of sage did you use? I'll try again later.


---

Comment by rbeezer created at 2010-09-05 18:31:46

Hi David,

My development version is at 4.5.2 and I think Billy has upgraded to that as well.  So I tested this all on a fresh 4.5.3.rc0.  Applied the four patches below in the order given:

trac_9720-random-echelonizable-matrices-v4.patch

trac_9803-random-matrix-constructor-v2.patch

trac_9802-random-diagonalizable-matrix-v2.patch

trac_9754-random-subspaces-unimodular-matrix-v7.patch

Applies and builds fine, passes all tests in sage/matrix and sage/groups.  I'd be surprised if 4.5.3.alpha0 were much different - almost all the code is just additions into matrix/constructor.py.  But it is critical that the order be right - each patch builds on the previous one.

Do you want to post details if a second attempt has problems?

Thanks,
Rob


---

Comment by wdj created at 2010-09-06 11:11:38

All patches apply fine to a freshly built sage-4.5.3.rc0 and passes sage -testall on a 10.6.4 mac.
Lots of nicely documented examples. Seems like a very useful addition for linear algebra teachers.

Positive review from me.


---

Comment by rbeezer created at 2010-09-06 21:25:41

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-09-06 21:25:41

Hi David,

I think everybody is happy with this now, so I'll mark it positive review now.  Thanks for all your help getting this ready to be merged quickly.  Feedback on classroom use might make it even better.  I'll probably be using it all myself in a few weeks for a short Sage course I'm teaching.

Billy - please add the instructions for the release manager, perhaps indicating that all four patches now have a positive review.

Rob


---

Comment by bwonderly created at 2010-09-07 00:29:41

Again, thanks to everyone who helped out on these, I really hope it proves to be useful.


---

Comment by bwonderly created at 2010-09-07 00:29:57

# Release Manager

#9720, #9803, #9802, #9754 is each dependent on the predecessor, merge in this order.


---

Comment by mpatel created at 2010-09-15 09:54:11

Resolution: fixed


---

Comment by jason created at 2010-10-12 09:22:47

I just noticed that this patch has a doctest marked #random.  It probably shouldn't be marked #random, as the seed should be fixed when doing doctests.
