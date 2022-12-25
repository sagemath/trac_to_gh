# Issue 9754: Add random unimodular and subspaces matrices to matrix/constructor.py

archive/issues_009754.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @rbeezer @wdjoyner @mwhansen\n\nThis depends on #9720, so first apply the v3 patch from there.  Two routines are added.  One generates matrices (using methods from the v3 patch) whose right and left null spaces, row space, and column space have desirable properties.  The other creates random unimodular matrices. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9754\n\n",
    "created_at": "2010-08-17T00:02:37Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Add random unimodular and subspaces matrices to matrix/constructor.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9754",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```
Assignee: jason, was

CC:  @rbeezer @wdjoyner @mwhansen

This depends on #9720, so first apply the v3 patch from there.  Two routines are added.  One generates matrices (using methods from the v3 patch) whose right and left null spaces, row space, and column space have desirable properties.  The other creates random unimodular matrices. 

Issue created by migration from https://trac.sagemath.org/ticket/9754





---

archive/issue_comments_095357.json:
```json
{
    "body": "Attachment [trac_9754-random-subspaces-unimodular-matrices.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspaces-unimodular-matrices.patch) by bwonderly created at 2010-08-17 00:10:40",
    "created_at": "2010-08-17T00:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95357",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Attachment [trac_9754-random-subspaces-unimodular-matrices.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspaces-unimodular-matrices.patch) by bwonderly created at 2010-08-17 00:10:40



---

archive/issue_comments_095358.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-17T00:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95358",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095359.json:
```json
{
    "body": "revised to fit generalization of random_matrix constructor.  Apply v4 from #9720 and v2 from #9803 and go from there.",
    "created_at": "2010-08-27T23:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95359",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

revised to fit generalization of random_matrix constructor.  Apply v4 from #9720 and v2 from #9803 and go from there.



---

archive/issue_comments_095360.json:
```json
{
    "body": "Attachment [trac_9754-random-subspace-unimodular-matrix-v2.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspace-unimodular-matrix-v2.patch) by bwonderly created at 2010-08-28 17:36:01\n\nThe most recent patch is independent of #9802.  There are some revisions to the documentation, but the majority of the work is to fit the routines to #9803.  Once this ticket, or #9802 gets a positive review, I will rebase the other to have all the routines included in one patch.",
    "created_at": "2010-08-28T17:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95360",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Attachment [trac_9754-random-subspace-unimodular-matrix-v2.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspace-unimodular-matrix-v2.patch) by bwonderly created at 2010-08-28 17:36:01

The most recent patch is independent of #9802.  There are some revisions to the documentation, but the majority of the work is to fit the routines to #9803.  Once this ticket, or #9802 gets a positive review, I will rebase the other to have all the routines included in one patch.



---

archive/issue_comments_095361.json:
```json
{
    "body": "Applies and passes sage -testall. Does what it says it does. Again, looks like a very useful addition for teachers of linear algebra.\n\nPositive review from me.",
    "created_at": "2010-08-30T00:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95361",
    "user": "https://github.com/wdjoyner"
}
```

Applies and passes sage -testall. Does what it says it does. Again, looks like a very useful addition for teachers of linear algebra.

Positive review from me.



---

archive/issue_comments_095362.json:
```json
{
    "body": "Attachment [trac_9754-random-subspaces-unimodular-matrix-v3.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspaces-unimodular-matrix-v3.patch) by bwonderly created at 2010-08-30 00:45:44\n\nrebased to go on top of #9802.  So apply v4 from #9720, v2 from #9803, and v2 from #9802",
    "created_at": "2010-08-30T00:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95362",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Attachment [trac_9754-random-subspaces-unimodular-matrix-v3.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspaces-unimodular-matrix-v3.patch) by bwonderly created at 2010-08-30 00:45:44

rebased to go on top of #9802.  So apply v4 from #9720, v2 from #9803, and v2 from #9802



---

archive/issue_comments_095363.json:
```json
{
    "body": "The v3 patch is a rebase to include #9802.  First apply v4 from #9720, then v2 from #9803, and finally v2 from #9802 and go from there.",
    "created_at": "2010-08-30T00:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95363",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

The v3 patch is a rebase to include #9802.  First apply v4 from #9720, then v2 from #9803, and finally v2 from #9802 and go from there.



---

archive/issue_comments_095364.json:
```json
{
    "body": "I've applied the rebased version successfully and am running tests right now, so I'll report back here.\n\nDavid - thanks for looking at these!  They are good enough that I almost wish I had a section of linear algebra this term.\n\nMike - Do you want to look over any of this?  #9803 is where I made the changes to accomodate the non-global-namespace versions, so that is the place where your comments were addressed.  If not, I'll have Billy get these marked up for the release manager.\n\nThanks,\nRob",
    "created_at": "2010-08-30T03:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95364",
    "user": "https://github.com/rbeezer"
}
```

I've applied the rebased version successfully and am running tests right now, so I'll report back here.

David - thanks for looking at these!  They are good enough that I almost wish I had a section of linear algebra this term.

Mike - Do you want to look over any of this?  #9803 is where I made the changes to accomodate the non-global-namespace versions, so that is the place where your comments were addressed.  If not, I'll have Billy get these marked up for the release manager.

Thanks,
Rob



---

archive/issue_comments_095365.json:
```json
{
    "body": "Fixed bug making all output matrices square.",
    "created_at": "2010-08-30T05:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95365",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Fixed bug making all output matrices square.



---

archive/issue_comments_095366.json:
```json
{
    "body": "Attachment [trac_9754-random-subspaces-unimodular-matrix-v4.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspaces-unimodular-matrix-v4.patch) by bwonderly created at 2010-08-30 05:04:47\n\nThere was a bug in the v3 patch making all output matrices square, which is now fixed in the v4 patch.",
    "created_at": "2010-08-30T05:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95366",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Attachment [trac_9754-random-subspaces-unimodular-matrix-v4.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspaces-unimodular-matrix-v4.patch) by bwonderly created at 2010-08-30 05:04:47

There was a bug in the v3 patch making all output matrices square, which is now fixed in the v4 patch.



---

archive/issue_comments_095367.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-30T18:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95367",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095368.json:
```json
{
    "body": "I was in the process of adding some doctests to be sure the row/column bug was fixed, and also homed in on:\n\n```\nif nullity>rows:\n    raise ValueError(\"nullity cannot exceed the number of rows or columns.\")\n```\n\nsince there should be two conditions to check:  rank < nrows,  rank < ncols.\n\nI got mightly confused since I forgot that `nullity()` is the *left* nullity.  Your other routines specify rank as an input, and for consistency I think this one should as well.  Maybe you think nullity as you design the matrix, and that is fine, but inputs and error messages would be clearer if you avoided the distinction between left and right kernels.  (This change in inputs also stopped me once.)\n\nCan you change the input to have `rank=` and adjust tests (doctests and actual error-checks in the code) accordingly?  You can keep your `nullity_generator` in the code, but lets label it as `left_nullity_generator` to make it clear that  rank + nullity  is the number of *rows* not the number of columns.\n\nSo there really isn't anything wrong here, but we have a chance to not add further to Sage's left/right, row/column dichotomy/confusion.  It'll be worth the effort.\n\nHere are the doctests I was adding for the `B` matrix of `random_subspaces_matrix()`:\n\n```\n        sage: (B.nrows(), B.ncols())\n        (6, 8)\n        sage: all([x in ZZ for x in A.list()])\n        True\n```\n\n```\n        sage: all([x in ZZ for x in B_expanded.list()])\n```\n\nRob",
    "created_at": "2010-08-30T18:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95368",
    "user": "https://github.com/rbeezer"
}
```

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

archive/issue_comments_095369.json:
```json
{
    "body": "Attachment [trac_9754-random-subspaces-unimodular-matrix-v5.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspaces-unimodular-matrix-v5.patch) by bwonderly created at 2010-08-30 21:40:30\n\nRevisions to random_subspaces_matrix to make to replace ``nullity`` input with ``rank``.",
    "created_at": "2010-08-30T21:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95369",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Attachment [trac_9754-random-subspaces-unimodular-matrix-v5.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspaces-unimodular-matrix-v5.patch) by bwonderly created at 2010-08-30 21:40:30

Revisions to random_subspaces_matrix to make to replace ``nullity`` input with ``rank``.



---

archive/issue_comments_095370.json:
```json
{
    "body": "I made the suggested changes in the v5 patch (making rank the input, changing the test to rank<rows, rank<columns, documentation stuff).  Let me know if i missed anything.",
    "created_at": "2010-08-30T21:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95370",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

I made the suggested changes in the v5 patch (making rank the input, changing the test to rank<rows, rank<columns, documentation stuff).  Let me know if i missed anything.



---

archive/issue_comments_095371.json:
```json
{
    "body": "Attachment [trac_9754_allow_zero_rank.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754_allow_zero_rank.patch) by @rbeezer created at 2010-08-31 05:17:31\n\n1.  With v5 patch:\n\n```\nsage: A=random_matrix(QQ, 5,9,algorithm='subspaces',rank=5)\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n<snip>\n\n/sage/dev/local/lib/python2.6/site-packages/sage/matrix/constructor.pyc in random_matrix(ring, nrows, ncols, algorithm, *args, **kwds)\n   1160         return A\n   1161     elif algorithm == 'echelon_form':\n-> 1162         return random_rref_matrix(parent, *args, **kwds)\n   1163     elif algorithm == 'echelonizable':\n   1164         return random_echelonizable_matrix(parent, *args, **kwds)\n\n/sage/dev/local/lib/python2.6/site-packages/sage/matrix/constructor.pyc in random_rref_matrix(parent, num_pivots)\n   1689         raise TypeError(\"the number of pivots must be an integer.\")\n   1690     if num_pivots<=0:\n-> 1691         raise ValueError(\"the number of pivots must be greater than zero.\")\n   1692     ring = parent.base_ring()\n   1693     if not ring.is_exact():\n\nValueError: the number of pivots must be greater than zero.\n```\n\nWith `rank=rows` the L matrix is empty (ie no rows), which is an interesting case (and often the source of student questions).  It seems to fail since your routines will not build a matrix in echelon form with no pivots.  Nor will it build an echelonizable matrix with zero rank.\n\nHowever, both are possible - a matrix with no pivots must be totally zeros.  A matrix of rank zero is totally zeros.  Since you have coded this carefully, I think everything works - if you just let it happen.\n\nPatch shows how to do this.  Apply it to experiment, and read the patch, then pop it off and make the necessary changes yourself if you believe it is OK.  I've only tested this a little bit, so don't presume it has my seal-of-approval.  Adjust error messages and tests.\n\n2.  In 'subspaces\" routine near the end.  Do you need to augment B to form N, and then strip out parts of M?  Seems you just produce the identity in the right \"half\" and then throw it away.  Will the following work?\n\n```\nJ=K.stack(L)\nreturn J.inverse()*B\n```\n\nWhat you have is clearer, but a comment or two in the source could replace the extra statements.",
    "created_at": "2010-08-31T05:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95371",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9754_allow_zero_rank.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754_allow_zero_rank.patch) by @rbeezer created at 2010-08-31 05:17:31

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

archive/issue_comments_095372.json:
```json
{
    "body": "Changed random_rref_matrix routine to allow for input of rank=0",
    "created_at": "2010-08-31T19:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95372",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Changed random_rref_matrix routine to allow for input of rank=0



---

archive/issue_comments_095373.json:
```json
{
    "body": "Attachment [trac_9754-random-subspaces-unimodular-matrix-v6.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspaces-unimodular-matrix-v6.patch) by bwonderly created at 2010-08-31 19:20:13\n\nv6 has the changes to allow for rank=0 input in random_rref_matrices, as well as changes to the doctests.  The end of the subspaces routine was also altered.  It tests and builds fine on my end, let me know if there is anything else.",
    "created_at": "2010-08-31T19:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95373",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Attachment [trac_9754-random-subspaces-unimodular-matrix-v6.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspaces-unimodular-matrix-v6.patch) by bwonderly created at 2010-08-31 19:20:13

v6 has the changes to allow for rank=0 input in random_rref_matrices, as well as changes to the doctests.  The end of the subspaces routine was also altered.  It tests and builds fine on my end, let me know if there is anything else.



---

archive/issue_comments_095374.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-02T02:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95374",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095375.json:
```json
{
    "body": "Attachment [trac_9754-random-subspaces-unimodular-matrix-v7.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspaces-unimodular-matrix-v7.patch) by @rbeezer created at 2010-09-02 02:15:10\n\nThe v6 patch looks real good - corrects rows/columns bug, fixes up the rank-nullity-confusion, and streamlines the end of the code for the \"subspaces\" routine (with comments replacing code for explanation).  Works well, passes all tests and docs look good.\n\nI noticed one test in the \"echelonizable\" routine that talks about \"just building a zero matrix\" if you need it (I'd added that verbiage earlier).  Its gone in v7, that's the only change.  v7 patch still has Billy's name in it and is the full patch otherwise.\n\nI think this is done, at least I am checking-off on the changes leading to the v6 patch.\n\nBilly - you could/should sign off on the little change to make v7.\n\nDavid - you can weigh-in further if you like, or not.  If so, we can leave this open for a few days.  If not, we'll wrap this all up.  Thanks so much for all your help and encouragement reviewing Billy's summer project.",
    "created_at": "2010-09-02T02:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95375",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9754-random-subspaces-unimodular-matrix-v7.patch](tarball://root/attachments/some-uuid/ticket9754/trac_9754-random-subspaces-unimodular-matrix-v7.patch) by @rbeezer created at 2010-09-02 02:15:10

The v6 patch looks real good - corrects rows/columns bug, fixes up the rank-nullity-confusion, and streamlines the end of the code for the "subspaces" routine (with comments replacing code for explanation).  Works well, passes all tests and docs look good.

I noticed one test in the "echelonizable" routine that talks about "just building a zero matrix" if you need it (I'd added that verbiage earlier).  Its gone in v7, that's the only change.  v7 patch still has Billy's name in it and is the full patch otherwise.

I think this is done, at least I am checking-off on the changes leading to the v6 patch.

Billy - you could/should sign off on the little change to make v7.

David - you can weigh-in further if you like, or not.  If so, we can leave this open for a few days.  If not, we'll wrap this all up.  Thanks so much for all your help and encouragement reviewing Billy's summer project.



---

archive/issue_comments_095376.json:
```json
{
    "body": "The v7 patch looks fine to me.  Thanks to everyone who helped out on this.",
    "created_at": "2010-09-03T06:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95376",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

The v7 patch looks fine to me.  Thanks to everyone who helped out on this.



---

archive/issue_comments_095377.json:
```json
{
    "body": "Does this only depend on #9720? There are some inconsistent statements with regard to the dependencies in the comments above.",
    "created_at": "2010-09-04T00:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95377",
    "user": "https://github.com/wdjoyner"
}
```

Does this only depend on #9720? There are some inconsistent statements with regard to the dependencies in the comments above.



---

archive/issue_comments_095378.json:
```json
{
    "body": "Replying to [comment:13 wdj]:\n> Does this only depend on #9720? There are some inconsistent statements with regard to the dependencies in the comments above.\n\n\nHi David,\n\nNo, it needs all the prior patches.  The full chain is:\n\n#9720, #9803, #9802, #9754\n\neach one depends on the previous one in the list, so you'll have to apply three patches to test this one.  But this should be the end (ie you could use these to prepare for class, etc).\n\nThanks,\nRob",
    "created_at": "2010-09-04T00:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95378",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:13 wdj]:
> Does this only depend on #9720? There are some inconsistent statements with regard to the dependencies in the comments above.


Hi David,

No, it needs all the prior patches.  The full chain is:

#9720, #9803, #9802, #9754

each one depends on the previous one in the list, so you'll have to apply three patches to test this one.  But this should be the end (ie you could use these to prepare for class, etc).

Thanks,
Rob



---

archive/issue_comments_095379.json:
```json
{
    "body": "I could not get this sequence to apply to 4.5.3.a0. What version of sage did you use? I'll try again later.",
    "created_at": "2010-09-05T09:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95379",
    "user": "https://github.com/wdjoyner"
}
```

I could not get this sequence to apply to 4.5.3.a0. What version of sage did you use? I'll try again later.



---

archive/issue_comments_095380.json:
```json
{
    "body": "Hi David,\n\nMy development version is at 4.5.2 and I think Billy has upgraded to that as well.  So I tested this all on a fresh 4.5.3.rc0.  Applied the four patches below in the order given:\n\ntrac_9720-random-echelonizable-matrices-v4.patch\n\ntrac_9803-random-matrix-constructor-v2.patch\n\ntrac_9802-random-diagonalizable-matrix-v2.patch\n\ntrac_9754-random-subspaces-unimodular-matrix-v7.patch\n\nApplies and builds fine, passes all tests in sage/matrix and sage/groups.  I'd be surprised if 4.5.3.alpha0 were much different - almost all the code is just additions into matrix/constructor.py.  But it is critical that the order be right - each patch builds on the previous one.\n\nDo you want to post details if a second attempt has problems?\n\nThanks,\nRob",
    "created_at": "2010-09-05T18:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95380",
    "user": "https://github.com/rbeezer"
}
```

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

archive/issue_comments_095381.json:
```json
{
    "body": "All patches apply fine to a freshly built sage-4.5.3.rc0 and passes sage -testall on a 10.6.4 mac.\nLots of nicely documented examples. Seems like a very useful addition for linear algebra teachers.\n\nPositive review from me.",
    "created_at": "2010-09-06T11:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95381",
    "user": "https://github.com/wdjoyner"
}
```

All patches apply fine to a freshly built sage-4.5.3.rc0 and passes sage -testall on a 10.6.4 mac.
Lots of nicely documented examples. Seems like a very useful addition for linear algebra teachers.

Positive review from me.



---

archive/issue_comments_095382.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-06T21:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95382",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095383.json:
```json
{
    "body": "Hi David,\n\nI think everybody is happy with this now, so I'll mark it positive review now.  Thanks for all your help getting this ready to be merged quickly.  Feedback on classroom use might make it even better.  I'll probably be using it all myself in a few weeks for a short Sage course I'm teaching.\n\nBilly - please add the instructions for the release manager, perhaps indicating that all four patches now have a positive review.\n\nRob",
    "created_at": "2010-09-06T21:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95383",
    "user": "https://github.com/rbeezer"
}
```

Hi David,

I think everybody is happy with this now, so I'll mark it positive review now.  Thanks for all your help getting this ready to be merged quickly.  Feedback on classroom use might make it even better.  I'll probably be using it all myself in a few weeks for a short Sage course I'm teaching.

Billy - please add the instructions for the release manager, perhaps indicating that all four patches now have a positive review.

Rob



---

archive/issue_comments_095384.json:
```json
{
    "body": "Again, thanks to everyone who helped out on these, I really hope it proves to be useful.",
    "created_at": "2010-09-07T00:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95384",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Again, thanks to everyone who helped out on these, I really hope it proves to be useful.



---

archive/issue_comments_095385.json:
```json
{
    "body": "# Release Manager\n\n#9720, #9803, #9802, #9754 is each dependent on the predecessor, merge in this order.",
    "created_at": "2010-09-07T00:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95385",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

# Release Manager

#9720, #9803, #9802, #9754 is each dependent on the predecessor, merge in this order.



---

archive/issue_comments_095386.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T09:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95386",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_024432.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T09:54:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9754#event-24432"
}
```



---

archive/issue_comments_095387.json:
```json
{
    "body": "I just noticed that this patch has a doctest marked #random.  It probably shouldn't be marked #random, as the seed should be fixed when doing doctests.",
    "created_at": "2010-10-12T09:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9754#issuecomment-95387",
    "user": "https://github.com/jasongrout"
}
```

I just noticed that this patch has a doctest marked #random.  It probably shouldn't be marked #random, as the seed should be fixed when doing doctests.
