# Issue 8977: Bug in QuadraticForm.rational_diagonal_form()

archive/issues_008977.json:
```json
{
    "body": "Assignee: justin\n\nCC:  @tornaria @jonhanke\n\nKeywords: rational_diagonal_form()\n\nThe function rational_diagonal_form() fails in some quadratic forms. For example:\n\n```\nsage: Q = QuadraticForm(ZZ,2,[0,1,-1])\nsage: Q\nQuadratic form in 2 variables over Integer Ring with coefficients: \n[ 0 1 ]\n[ * -1 ]\n\n\nsage: Q.rational_diagonal_form()\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n\n/home/gustavo/<ipython console> in <module>()\n\n/home/gustavo/sage-4.3.3/local/lib/python2.6/site-packages/sage/quadratic_forms/quadratic_form__local_field_invariants.pyc in rational_diagonal_form(self, return_matrix)\n    113         for j in range(i+1, n):\n    114             if Q[i,j] != 0:\n--> 115                 temp[i,j] = -Q[i,j] / (Q[i,i] * 2)    ## This should only occur when Q[i,i] != 0, which the above step guarantees.\n    116 \n    117         Q = Q(temp)\n\n/home/gustavo/sage-4.3.3/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__div__ (sage/structure/element.c:11882)()\n\n/home/gustavo/sage-4.3.3/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational._div_ (sage/rings/rational.c:14641)()\n\nZeroDivisionError: Rational division by zero\n```\nWhen an element of the diagonal is zero the algorithm tries, with a tranformation, to eliminate it. But in the case that Q[i,i]=0, Q[i,j]!=0 and Q[j,j]=-Q[i,j] the tranformation brings the zero back.\n\nThe fix changes the transformation, in the case mentioned above, so that doesn't happen.\n\nApply trac_8977_rational_diagonal_form_fix2.patch\n\nIssue created by migration from https://trac.sagemath.org/ticket/8977\n\n",
    "closed_at": "2011-03-17T19:22:45Z",
    "created_at": "2010-05-16T01:16:41Z",
    "labels": [
        "component: quadratic forms",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "Bug in QuadraticForm.rational_diagonal_form()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8977",
    "user": "https://trac.sagemath.org/admin/accounts/users/gdrama"
}
```
Assignee: justin

CC:  @tornaria @jonhanke

Keywords: rational_diagonal_form()

The function rational_diagonal_form() fails in some quadratic forms. For example:

```
sage: Q = QuadraticForm(ZZ,2,[0,1,-1])
sage: Q
Quadratic form in 2 variables over Integer Ring with coefficients: 
[ 0 1 ]
[ * -1 ]


sage: Q.rational_diagonal_form()
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

/home/gustavo/<ipython console> in <module>()

/home/gustavo/sage-4.3.3/local/lib/python2.6/site-packages/sage/quadratic_forms/quadratic_form__local_field_invariants.pyc in rational_diagonal_form(self, return_matrix)
    113         for j in range(i+1, n):
    114             if Q[i,j] != 0:
--> 115                 temp[i,j] = -Q[i,j] / (Q[i,i] * 2)    ## This should only occur when Q[i,i] != 0, which the above step guarantees.
    116 
    117         Q = Q(temp)

/home/gustavo/sage-4.3.3/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__div__ (sage/structure/element.c:11882)()

/home/gustavo/sage-4.3.3/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational._div_ (sage/rings/rational.c:14641)()

ZeroDivisionError: Rational division by zero
```
When an element of the diagonal is zero the algorithm tries, with a tranformation, to eliminate it. But in the case that Q[i,i]=0, Q[i,j]!=0 and Q[j,j]=-Q[i,j] the tranformation brings the zero back.

The fix changes the transformation, in the case mentioned above, so that doesn't happen.

Apply trac_8977_rational_diagonal_form_fix2.patch

Issue created by migration from https://trac.sagemath.org/ticket/8977





---

archive/issue_comments_082685.json:
```json
{
    "body": "I think a short explanation of the bug (and the fix) here in trac would be useful. Also, adding an example to the docstring to test for this would be nice.\n\nOtherwise, the patch seems reasonable, asuming I understood it correctly (I *can* reproduce the bug, but I did *not* try the fix)",
    "created_at": "2010-05-18T20:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82685",
    "user": "https://github.com/tornaria"
}
```

I think a short explanation of the bug (and the fix) here in trac would be useful. Also, adding an example to the docstring to test for this would be nice.

Otherwise, the patch seems reasonable, asuming I understood it correctly (I *can* reproduce the bug, but I did *not* try the fix)



---

archive/issue_comments_082686.json:
```json
{
    "body": "Changed the patch to add the example given to the doctest, and fixed the doctest also.",
    "created_at": "2010-05-28T01:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82686",
    "user": "https://trac.sagemath.org/admin/accounts/users/gdrama"
}
```

Changed the patch to add the example given to the doctest, and fixed the doctest also.



---

archive/issue_comments_082687.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-12-03T11:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82687",
    "user": "https://github.com/tornaria"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082688.json:
```json
{
    "body": "The patch fails to apply (4.6.1.rc1).\nAlso, the INPUT and OUTPUT blocks should only have a single colon (see [here](http://www.sagemath.org/doc/developer/conventions.html))",
    "created_at": "2011-01-16T14:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82688",
    "user": "https://github.com/mstreng"
}
```

The patch fails to apply (4.6.1.rc1).
Also, the INPUT and OUTPUT blocks should only have a single colon (see [here](http://www.sagemath.org/doc/developer/conventions.html))



---

archive/issue_comments_082689.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-16T14:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82689",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082690.json:
```json
{
    "body": "Attachment [trac_8977_rational_diagonal_form_fix.patch](tarball://root/attachments/some-uuid/ticket8977/trac_8977_rational_diagonal_form_fix.patch) by gdrama created at 2011-02-05 15:30:58",
    "created_at": "2011-02-05T15:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82690",
    "user": "https://trac.sagemath.org/admin/accounts/users/gdrama"
}
```

Attachment [trac_8977_rational_diagonal_form_fix.patch](tarball://root/attachments/some-uuid/ticket8977/trac_8977_rational_diagonal_form_fix.patch) by gdrama created at 2011-02-05 15:30:58



---

archive/issue_comments_082691.json:
```json
{
    "body": "I fixed the patch for sage-4.6.1 and make the corrections mstreng told.",
    "created_at": "2011-02-05T15:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82691",
    "user": "https://trac.sagemath.org/admin/accounts/users/gdrama"
}
```

I fixed the patch for sage-4.6.1 and make the corrections mstreng told.



---

archive/issue_comments_082692.json:
```json
{
    "body": "Can anyone reproduce this? A seemingly unrelated doctest fails.\n\n```\nThe following tests failed:\n\n        sage -t -long devel/sage/sage/groups/matrix_gps/matrix_group.py # 4 doctests failed\n```\nAll 4 are of the following form:\n\n```\nFile \"/storage/marco/sage-4.6.1/devel/sage-main/sage/groups/matrix_gps/matrix_group.py\", line 668:\n    sage: G.random_element()\nExpected:\n    [2 1 1 1]\n    [1 0 2 1]\n    [0 1 1 0]\n    [1 0 0 1]\nGot:\n    [0 1 1 0]\n    [1 2 2 2]\n    [1 1 1 0]\n    [2 0 1 2]\n```\nI tried removing and reapplying the patch. All tests pass on an unpatched 4.6.2.alpha3, and 4 tests of the form `G.random_element()` fail with the patch applied. I've had problems like this before with other tickets, so I won't change this ticket to needs_work (yet).\n\nOops, it seems that the ticket still is needs_work. Was it not ready for review yet?",
    "created_at": "2011-02-06T23:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82692",
    "user": "https://github.com/mstreng"
}
```

Can anyone reproduce this? A seemingly unrelated doctest fails.

```
The following tests failed:

        sage -t -long devel/sage/sage/groups/matrix_gps/matrix_group.py # 4 doctests failed
```
All 4 are of the following form:

```
File "/storage/marco/sage-4.6.1/devel/sage-main/sage/groups/matrix_gps/matrix_group.py", line 668:
    sage: G.random_element()
Expected:
    [2 1 1 1]
    [1 0 2 1]
    [0 1 1 0]
    [1 0 0 1]
Got:
    [0 1 1 0]
    [1 2 2 2]
    [1 1 1 0]
    [2 0 1 2]
```
I tried removing and reapplying the patch. All tests pass on an unpatched 4.6.2.alpha3, and 4 tests of the form `G.random_element()` fail with the patch applied. I've had problems like this before with other tickets, so I won't change this ticket to needs_work (yet).

Oops, it seems that the ticket still is needs_work. Was it not ready for review yet?



---

archive/issue_comments_082693.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-07T00:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82693",
    "user": "https://github.com/tornaria"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082694.json:
```json
{
    "body": "I don't think the issue you reported above (about matrix groups `random_element()`) is related in any way to this ticket.\n\nThe patch is pretty straightforward, is almost one-liner, and clearly changes only the `rational_diagonal_form()` method.\n\nI've just tried on 4.6.1 and:\na. the bug is reproducible\nb. the doctest in the patch triggers the bug\nc. after applying the patch, the bug is fixed, and the doctest passes.\n\n---\n\nI also tried long-doctesting the `matrix_group.py` file (with the patch applied) but got no error.\n\nMaybe it's showing randomly for you (and you think it's correlated to the patch in this ticket, but is not). Or perhaps something in 4.6.2.alpha3 is affecting this.\n\n---\n\nIn my opinion, the patch is ready. I'll switch to \"needs_review\", in the hope that somebody else gives the positive review soon.",
    "created_at": "2011-02-07T00:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82694",
    "user": "https://github.com/tornaria"
}
```

I don't think the issue you reported above (about matrix groups `random_element()`) is related in any way to this ticket.

The patch is pretty straightforward, is almost one-liner, and clearly changes only the `rational_diagonal_form()` method.

I've just tried on 4.6.1 and:
a. the bug is reproducible
b. the doctest in the patch triggers the bug
c. after applying the patch, the bug is fixed, and the doctest passes.

---

I also tried long-doctesting the `matrix_group.py` file (with the patch applied) but got no error.

Maybe it's showing randomly for you (and you think it's correlated to the patch in this ticket, but is not). Or perhaps something in 4.6.2.alpha3 is affecting this.

---

In my opinion, the patch is ready. I'll switch to "needs_review", in the hope that somebody else gives the positive review soon.



---

archive/issue_comments_082695.json:
```json
{
    "body": "Fresh install, no more failing doctests.\n\nI already clicked \"positive_review\", and then noticed that the first line of the patch only says \"Trac\" instead of giving the ticket number and a description of the patch. I'm afraid it would only be set back to \"needs_work\" by the release manager, as happened [here](http://trac.sagemath.org/sage_trac/ticket/10702#comment:3).",
    "created_at": "2011-02-07T20:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82695",
    "user": "https://github.com/mstreng"
}
```

Fresh install, no more failing doctests.

I already clicked "positive_review", and then noticed that the first line of the patch only says "Trac" instead of giving the ticket number and a description of the patch. I'm afraid it would only be set back to "needs_work" by the release manager, as happened [here](http://trac.sagemath.org/sage_trac/ticket/10702#comment:3).



---

archive/issue_comments_082696.json:
```json
{
    "body": "Attachment [trac_8977_rational_diagonal_form_fix2.patch](tarball://root/attachments/some-uuid/ticket8977/trac_8977_rational_diagonal_form_fix2.patch) by @mstreng created at 2011-02-07 20:51:24\n\nadded ticket description to patch",
    "created_at": "2011-02-07T20:51:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82696",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_8977_rational_diagonal_form_fix2.patch](tarball://root/attachments/some-uuid/ticket8977/trac_8977_rational_diagonal_form_fix2.patch) by @mstreng created at 2011-02-07 20:51:24

added ticket description to patch



---

archive/issue_comments_082697.json:
```json
{
    "body": "Apply trac_8977_rational_diagonal_form_fix2.patch",
    "created_at": "2011-02-07T20:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82697",
    "user": "https://github.com/mstreng"
}
```

Apply trac_8977_rational_diagonal_form_fix2.patch



---

archive/issue_comments_082698.json:
```json
{
    "body": "Can we merge this, please?",
    "created_at": "2011-03-08T20:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82698",
    "user": "https://github.com/tornaria"
}
```

Can we merge this, please?



---

archive/issue_comments_082699.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-08T20:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82699",
    "user": "https://github.com/tornaria"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_021947.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-03-08T21:43:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "milestone": "sage-4.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8977#event-21947"
}
```



---

archive/issue_events_021948.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-03-17T19:22:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8977#event-21948"
}
```



---

archive/issue_comments_082700.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-17T19:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8977#issuecomment-82700",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
