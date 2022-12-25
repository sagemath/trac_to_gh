# Issue 6106: [with patch, need review] Addition Indefinite Binary Quadratic Forms

archive/issues_006106.json:
```json
{
    "body": "Assignee: justin\n\nCC:  @ncalexan\n\nKeywords: binary quadratic forms\n\nI added functions to check for the reducibility of an indefinite binary quadratic form and reduce it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6106\n\n",
    "created_at": "2009-05-21T05:22:11Z",
    "labels": [
        "component: quadratic forms",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.4",
    "title": "[with patch, need review] Addition Indefinite Binary Quadratic Forms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6106",
    "user": "https://trac.sagemath.org/admin/accounts/users/aliashamieh"
}
```
Assignee: justin

CC:  @ncalexan

Keywords: binary quadratic forms

I added functions to check for the reducibility of an indefinite binary quadratic form and reduce it.

Issue created by migration from https://trac.sagemath.org/ticket/6106





---

archive/issue_comments_048682.json:
```json
{
    "body": "Attachment [6106binaryQuadraticPT2.patch](tarball://root/attachments/some-uuid/ticket6106/6106binaryQuadraticPT2.patch) by aliashamieh created at 2009-05-21 05:57:26\n\nadded missing doctests",
    "created_at": "2009-05-21T05:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48682",
    "user": "https://trac.sagemath.org/admin/accounts/users/aliashamieh"
}
```

Attachment [6106binaryQuadraticPT2.patch](tarball://root/attachments/some-uuid/ticket6106/6106binaryQuadraticPT2.patch) by aliashamieh created at 2009-05-21 05:57:26

added missing doctests



---

archive/issue_comments_048683.json:
```json
{
    "body": "Am changing this from \"need review\" to \"needs review\" so it shows up in the standard queries",
    "created_at": "2009-06-10T10:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48683",
    "user": "https://github.com/loefflerd"
}
```

Am changing this from "need review" to "needs review" so it shows up in the standard queries



---

archive/issue_comments_048684.json:
```json
{
    "body": "Review\n\nThe patch applied fine to 4.0.1, and it provides some functions which look useful.\n\nI think that not all new new functions have doctests.  Why are the new functions not implemented as member functions of the BinaryQF class?  That would be much better;  as it is anyone using them has to import them explicitly.  So I suggest that they are converted to be member functions (which is trivial to do).\n\nSecondly, the use of the python math functions sqrt and floor is not a good idea, since the coefficients of the form will be Sage integers.  For example:\n\n```\nsage: from sage.quadratic_forms.binary_qf import normalized_indefinite_form\nsage: f = BinaryQF([10^100,10^500,10^200])\nsage: f.discriminant()>0\nTrue\nsage: normalized_indefinite_form(f)\n---------------------------------------------------------------------------\nOverflowError                             Traceback (most recent call last)\n\n/home/john/.sage/temp/ubuntu/9768/_home_john__sage_init_sage_0.py in <module>()\n\n/home/john/sage-4.0.1/local/lib/python2.5/site-packages/sage/quadratic_forms/binary_qf.pyc in normalized_indefinite_form(f)\n    486         raise ValueError, \"This only works for indefinite forms\"\n    487     \n--> 488     if sqrt(delta) <= abs(a):\n    489         s=(a/abs(a))*floor(-1*b/(2*abs(a)))\n    490     else:\n\nOverflowError: math range error\n```\nFor example, the line if sqrt(delta) <= abs(a): could be replaced by if delta <= a**2: .\n\nThe docstring for this function should also say what the definition of \"normalised\" is.\n\nI also slightly amended the ticket's title to give a better description.",
    "created_at": "2009-06-11T16:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48684",
    "user": "https://github.com/JohnCremona"
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

archive/issue_comments_048685.json:
```json
{
    "body": "Alia and I are going to work on this in the next few days.",
    "created_at": "2009-07-01T17:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48685",
    "user": "https://github.com/ncalexan"
}
```

Alia and I are going to work on this in the next few days.



---

archive/issue_comments_048686.json:
```json
{
    "body": "Attachment [6106BinaryQF.patch](tarball://root/attachments/some-uuid/ticket6106/6106BinaryQF.patch) by aliashamieh created at 2009-07-17 19:07:05\n\n[with patch, needs review] Additional functions for Indefinite Binary Quadratic Forms",
    "created_at": "2009-07-17T19:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48686",
    "user": "https://trac.sagemath.org/admin/accounts/users/aliashamieh"
}
```

Attachment [6106BinaryQF.patch](tarball://root/attachments/some-uuid/ticket6106/6106BinaryQF.patch) by aliashamieh created at 2009-07-17 19:07:05

[with patch, needs review] Additional functions for Indefinite Binary Quadratic Forms



---

archive/issue_events_014364.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14364"
}
```



---

archive/issue_events_014365.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14365"
}
```



---

archive/issue_events_014366.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14366"
}
```



---

archive/issue_comments_048687.json:
```json
{
    "body": "This ticket seems to implement the same functionality as (part of) #4120, which has been inactive for a very long time, like this ticket.",
    "created_at": "2014-02-26T17:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48687",
    "user": "https://github.com/pjbruin"
}
```

This ticket seems to implement the same functionality as (part of) #4120, which has been inactive for a very long time, like this ticket.



---

archive/issue_events_014367.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14367"
}
```



---

archive/issue_events_014368.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14368"
}
```



---

archive/issue_events_014369.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14369"
}
```



---

archive/issue_events_014370.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14370"
}
```



---

archive/issue_comments_048688.json:
```json
{
    "body": "Replying to [comment:6 pbruin]:\n> This ticket seems to implement the same functionality as (part of) #4120, which has been inactive for a very long time, like this ticket.\n\nNow that #4120 has been merged, it would be good to check if this ticket still adds new functionality.  If not, we could also just add the examples from this ticket.",
    "created_at": "2018-06-19T11:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48688",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:6 pbruin]:
> This ticket seems to implement the same functionality as (part of) #4120, which has been inactive for a very long time, like this ticket.

Now that #4120 has been merged, it would be good to check if this ticket still adds new functionality.  If not, we could also just add the examples from this ticket.



---

archive/issue_events_014371.json:
```json
{
    "actor": "https://github.com/simonbrandhorst",
    "created_at": "2018-07-14T17:34:28Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14371"
}
```



---

archive/issue_events_014372.json:
```json
{
    "actor": "https://github.com/simonbrandhorst",
    "created_at": "2018-07-14T17:34:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14372"
}
```



---

archive/issue_comments_048689.json:
```json
{
    "body": "This ticket does not add anything new.",
    "created_at": "2018-07-14T17:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48689",
    "user": "https://github.com/simonbrandhorst"
}
```

This ticket does not add anything new.



---

archive/issue_comments_048690.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2018-07-14T17:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48690",
    "user": "https://github.com/simonbrandhorst"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_048691.json:
```json
{
    "body": "Replying to [comment:10 sbrandhorst]:\n> This ticket does not add anything new. \nOK.  It might still be useful to add the doctests from this ticket; what do you think?",
    "created_at": "2018-07-16T08:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48691",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:10 sbrandhorst]:
> This ticket does not add anything new. 
OK.  It might still be useful to add the doctests from this ticket; what do you think?



---

archive/issue_comments_048692.json:
```json
{
    "body": "If I recall correctly the reduction of an indefinite form is not unique but instead we get a cycle of forms. So we can add some doctests. But the results may be different.\n\nNote that we messed up a little for indefinite forms of square determinant #25861.",
    "created_at": "2018-07-16T09:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48692",
    "user": "https://github.com/simonbrandhorst"
}
```

If I recall correctly the reduction of an indefinite form is not unique but instead we get a cycle of forms. So we can add some doctests. But the results may be different.

Note that we messed up a little for indefinite forms of square determinant #25861.



---

archive/issue_comments_048693.json:
```json
{
    "body": "Here are some doctests from the patches.  I checked that they are mathematically correct.  The docstring for `reduced_form()` did not have any examples with `transformation=True` yet; now it does.",
    "created_at": "2018-07-16T09:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48693",
    "user": "https://github.com/pjbruin"
}
```

Here are some doctests from the patches.  I checked that they are mathematically correct.  The docstring for `reduced_form()` did not have any examples with `transformation=True` yet; now it does.



---

archive/issue_events_014373.json:
```json
{
    "actor": "https://github.com/pjbruin",
    "created_at": "2018-07-16T09:49:07Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14373"
}
```



---

archive/issue_events_014374.json:
```json
{
    "actor": "https://github.com/pjbruin",
    "created_at": "2018-07-16T09:49:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-8.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14374"
}
```



---

archive/issue_comments_048694.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-07-16T10:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48694",
    "user": "https://github.com/simonbrandhorst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_048695.json:
```json
{
    "body": "doc builds.",
    "created_at": "2018-07-16T10:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48695",
    "user": "https://github.com/simonbrandhorst"
}
```

doc builds.



---

archive/issue_events_014375.json:
```json
{
    "actor": "https://github.com/simonbrandhorst",
    "created_at": "2018-07-16T10:26:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-8.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14375"
}
```



---

archive/issue_events_014376.json:
```json
{
    "actor": "https://github.com/simonbrandhorst",
    "created_at": "2018-07-16T10:26:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14376"
}
```



---

archive/issue_events_014377.json:
```json
{
    "actor": "https://github.com/pjbruin",
    "created_at": "2018-08-22T12:29:04Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14377"
}
```



---

archive/issue_events_014378.json:
```json
{
    "actor": "https://github.com/pjbruin",
    "created_at": "2018-08-22T12:29:04Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "milestone": "sage-8.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14378"
}
```



---

archive/issue_comments_048696.json:
```json
{
    "body": "Replying to [comment:14 sbrandhorst]:\n> doc builds.\n\nFrom your other changes, it doesn't look like you really intended to delete the branch and change the milestone to *sage-duplicate/invalid/wontfix*...",
    "created_at": "2018-08-22T12:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48696",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:14 sbrandhorst]:
> doc builds.

From your other changes, it doesn't look like you really intended to delete the branch and change the milestone to *sage-duplicate/invalid/wontfix*...



---

archive/issue_comments_048697.json:
```json
{
    "body": "Ooops indeed. Thank you.",
    "created_at": "2018-08-24T11:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48697",
    "user": "https://github.com/simonbrandhorst"
}
```

Ooops indeed. Thank you.



---

archive/issue_comments_048698.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2018-08-25T11:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6106#issuecomment-48698",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_014379.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2018-08-25T11:01:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6106",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6106#event-14379"
}
```
