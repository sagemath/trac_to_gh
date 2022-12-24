# Issue 6106: [with patch, need review] Addition Indefinite Binary Quadratic Forms

archive/issues_006106.json:
```json
{
    "body": "Assignee: justin\n\nCC:  @ncalexan\n\nKeywords: binary quadratic forms\n\nI added functions to check for the reducibility of an indefinite binary quadratic form and reduce it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6106\n\n",
    "created_at": "2009-05-21T05:22:11Z",
    "labels": [
        "quadratic forms",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.4",
    "title": "[with patch, need review] Addition Indefinite Binary Quadratic Forms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6106",
    "user": "aliashamieh"
}
```
Assignee: justin

CC:  @ncalexan

Keywords: binary quadratic forms

I added functions to check for the reducibility of an indefinite binary quadratic form and reduce it.

Issue created by migration from https://trac.sagemath.org/ticket/6106





---

archive/issue_comments_048777.json:
```json
{
    "body": "Attachment [6106binaryQuadraticPT2.patch](tarball://root/attachments/some-uuid/ticket6106/6106binaryQuadraticPT2.patch) by aliashamieh created at 2009-05-21 05:57:26\n\nadded missing doctests",
    "created_at": "2009-05-21T05:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48777",
    "user": "aliashamieh"
}
```

Attachment [6106binaryQuadraticPT2.patch](tarball://root/attachments/some-uuid/ticket6106/6106binaryQuadraticPT2.patch) by aliashamieh created at 2009-05-21 05:57:26

added missing doctests



---

archive/issue_comments_048778.json:
```json
{
    "body": "Am changing this from \"need review\" to \"needs review\" so it shows up in the standard queries",
    "created_at": "2009-06-10T10:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48778",
    "user": "@loefflerd"
}
```

Am changing this from "need review" to "needs review" so it shows up in the standard queries



---

archive/issue_comments_048779.json:
```json
{
    "body": "Review\n\nThe patch applied fine to 4.0.1, and it provides some functions which look useful.\n\nI think that not all new new functions have doctests.  Why are the new functions not implemented as member functions of the BinaryQF class?  That would be much better;  as it is anyone using them has to import them explicitly.  So I suggest that they are converted to be member functions (which is trivial to do).\n\nSecondly, the use of the python math functions sqrt and floor is not a good idea, since the coefficients of the form will be Sage integers.  For example:\n\n```\nsage: from sage.quadratic_forms.binary_qf import normalized_indefinite_form\nsage: f = BinaryQF([10^100,10^500,10^200])\nsage: f.discriminant()>0\nTrue\nsage: normalized_indefinite_form(f)\n---------------------------------------------------------------------------\nOverflowError                             Traceback (most recent call last)\n\n/home/john/.sage/temp/ubuntu/9768/_home_john__sage_init_sage_0.py in <module>()\n\n/home/john/sage-4.0.1/local/lib/python2.5/site-packages/sage/quadratic_forms/binary_qf.pyc in normalized_indefinite_form(f)\n    486         raise ValueError, \"This only works for indefinite forms\"\n    487     \n--> 488     if sqrt(delta) <= abs(a):\n    489         s=(a/abs(a))*floor(-1*b/(2*abs(a)))\n    490     else:\n\nOverflowError: math range error\n```\n\nFor example, the line if sqrt(delta) <= abs(a): could be replaced by if delta <= a**2: .\n\nThe docstring for this function should also say what the definition of \"normalised\" is.\n\nI also slightly amended the ticket's title to give a better description.",
    "created_at": "2009-06-11T16:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48779",
    "user": "@JohnCremona"
}
```

Review

The patch applied fine to 4.0.1, and it provides some functions which look useful.

I think that not all new new functions have doctests.  Why are the new functions not implemented as member functions of the BinaryQF class?  That would be much better;  as it is anyone using them has to import them explicitly.  So I suggest that they are converted to be member functions (which is trivial to do).

Secondly, the use of the python math functions sqrt and floor is not a good idea, since the coefficients of the form will be Sage integers.  For example:

```
sage: from sage.quadratic_forms.binary_qf import normalized_indefinite_form
sage: f = BinaryQF([10^100,10^500,10^200])
sage: f.discriminant()>0
True
sage: normalized_indefinite_form(f)
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)

/home/john/.sage/temp/ubuntu/9768/_home_john__sage_init_sage_0.py in <module>()

/home/john/sage-4.0.1/local/lib/python2.5/site-packages/sage/quadratic_forms/binary_qf.pyc in normalized_indefinite_form(f)
    486         raise ValueError, "This only works for indefinite forms"
    487     
--> 488     if sqrt(delta) <= abs(a):
    489         s=(a/abs(a))*floor(-1*b/(2*abs(a)))
    490     else:

OverflowError: math range error
```

For example, the line if sqrt(delta) <= abs(a): could be replaced by if delta <= a**2: .

The docstring for this function should also say what the definition of "normalised" is.

I also slightly amended the ticket's title to give a better description.



---

archive/issue_comments_048780.json:
```json
{
    "body": "Alia and I are going to work on this in the next few days.",
    "created_at": "2009-07-01T17:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48780",
    "user": "@ncalexan"
}
```

Alia and I are going to work on this in the next few days.



---

archive/issue_comments_048781.json:
```json
{
    "body": "Attachment [6106BinaryQF.patch](tarball://root/attachments/some-uuid/ticket6106/6106BinaryQF.patch) by aliashamieh created at 2009-07-17 19:07:05\n\n[with patch, needs review] Additional functions for Indefinite Binary Quadratic Forms",
    "created_at": "2009-07-17T19:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48781",
    "user": "aliashamieh"
}
```

Attachment [6106BinaryQF.patch](tarball://root/attachments/some-uuid/ticket6106/6106BinaryQF.patch) by aliashamieh created at 2009-07-17 19:07:05

[with patch, needs review] Additional functions for Indefinite Binary Quadratic Forms



---

archive/issue_comments_048782.json:
```json
{
    "body": "This ticket seems to implement the same functionality as (part of) #4120, which has been inactive for a very long time, like this ticket.",
    "created_at": "2014-02-26T17:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48782",
    "user": "@pjbruin"
}
```

This ticket seems to implement the same functionality as (part of) #4120, which has been inactive for a very long time, like this ticket.



---

archive/issue_comments_048783.json:
```json
{
    "body": "Replying to [comment:6 pbruin]:\n> This ticket seems to implement the same functionality as (part of) #4120, which has been inactive for a very long time, like this ticket.\nNow that #4120 has been merged, it would be good to check if this ticket still adds new functionality.  If not, we could also just add the examples from this ticket.",
    "created_at": "2018-06-19T11:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48783",
    "user": "@pjbruin"
}
```

Replying to [comment:6 pbruin]:
> This ticket seems to implement the same functionality as (part of) #4120, which has been inactive for a very long time, like this ticket.
Now that #4120 has been merged, it would be good to check if this ticket still adds new functionality.  If not, we could also just add the examples from this ticket.



---

archive/issue_comments_048784.json:
```json
{
    "body": "This ticket does not add anything new.",
    "created_at": "2018-07-14T17:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48784",
    "user": "@simonbrandhorst"
}
```

This ticket does not add anything new.



---

archive/issue_comments_048785.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2018-07-14T17:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48785",
    "user": "@simonbrandhorst"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_048786.json:
```json
{
    "body": "Replying to [comment:10 sbrandhorst]:\n> This ticket does not add anything new. \nOK.  It might still be useful to add the doctests from this ticket; what do you think?",
    "created_at": "2018-07-16T08:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48786",
    "user": "@pjbruin"
}
```

Replying to [comment:10 sbrandhorst]:
> This ticket does not add anything new. 
OK.  It might still be useful to add the doctests from this ticket; what do you think?



---

archive/issue_comments_048787.json:
```json
{
    "body": "If I recall correctly the reduction of an indefinite form is not unique but instead we get a cycle of forms. So we can add some doctests. But the results may be different.\n\nNote that we messed up a little for indefinite forms of square determinant #25861.",
    "created_at": "2018-07-16T09:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48787",
    "user": "@simonbrandhorst"
}
```

If I recall correctly the reduction of an indefinite form is not unique but instead we get a cycle of forms. So we can add some doctests. But the results may be different.

Note that we messed up a little for indefinite forms of square determinant #25861.



---

archive/issue_comments_048788.json:
```json
{
    "body": "Here are some doctests from the patches.  I checked that they are mathematically correct.  The docstring for `reduced_form()` did not have any examples with `transformation=True` yet; now it does.",
    "created_at": "2018-07-16T09:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48788",
    "user": "@pjbruin"
}
```

Here are some doctests from the patches.  I checked that they are mathematically correct.  The docstring for `reduced_form()` did not have any examples with `transformation=True` yet; now it does.



---

archive/issue_comments_048789.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-07-16T10:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48789",
    "user": "@simonbrandhorst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_048790.json:
```json
{
    "body": "doc builds.",
    "created_at": "2018-07-16T10:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48790",
    "user": "@simonbrandhorst"
}
```

doc builds.



---

archive/issue_comments_048791.json:
```json
{
    "body": "Replying to [comment:14 sbrandhorst]:\n> doc builds.\nFrom your other changes, it doesn't look like you really intended to delete the branch and change the milestone to *sage-duplicate/invalid/wontfix*...",
    "created_at": "2018-08-22T12:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48791",
    "user": "@pjbruin"
}
```

Replying to [comment:14 sbrandhorst]:
> doc builds.
From your other changes, it doesn't look like you really intended to delete the branch and change the milestone to *sage-duplicate/invalid/wontfix*...



---

archive/issue_comments_048792.json:
```json
{
    "body": "Ooops indeed. Thank you.",
    "created_at": "2018-08-24T11:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48792",
    "user": "@simonbrandhorst"
}
```

Ooops indeed. Thank you.



---

archive/issue_comments_048793.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2018-08-25T11:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48793",
    "user": "@vbraun"
}
```

Resolution: fixed
