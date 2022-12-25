# Issue 2494: bugs in evaluation of spherical bessel function

archive/issues_002494.json:
```json
{
    "body": "Assignee: jkantor\n\n\n```\nBUG 1:\n\nHi,\nI was just trying to calculate some stuff with spherical Bessel\nfunctions and got this error message:\n\nsage: spherical_bessel_J(3,.1)\n\n\n....\n6823         return x\n  6824     except SyntaxError:\n-> 6825         raise TypeError, \"unable to make sense of Maxima\nexpression '%s' in SAGE\"%s\n  6826     finally:\n  6827         is_simplified = False\n\n<type 'exceptions.TypeError'>: unable to make sense of Maxima\nexpression '9.5185197208655641L-6' in SAGE\nsage:\nKeyboardInterrupt\n\nI checked it, it happens for small values of the argument x.\nDoes anyone has a solution or work around?\n\nGreets,\n\nschorsch\n```\n\n\nBUG2\n\n```\nsage: spherical_bessel_J(3,.1, algorithm='scipy')\n---------------------------------------------------------------------------\n<type 'exceptions.NameError'>             Traceback (most recent call last)\n\n/Users/was/Downloads/z/<ipython console> in <module>()\n\n/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/functions/special.py in spherical_bessel_J(n, var, algorithm)\n    782         ans = ans.replace(\")\",\"\")\n    783         ans = ans.replace(\"j\",\"*I\")\n--> 784         return sage_eval(ans)\n    785     elif algorithm == 'maxima':\n    786         _init()\n\n/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/misc/sage_eval.py in sage_eval(source, locals)\n    108     p = preparse(source)\n    109     try:\n--> 110         return eval(p, sage.all.__dict__, locals)\n    111     except SyntaxError, msg:\n    112         raise SyntaxError, \"%s\\nError using SAGE to evaluate '%s'\"%(msg, p)\n\n/Users/was/Downloads/z/<string> in <module>()\n\n<type 'exceptions.NameError'>: name 'array' is not defined\n```\n\n\nProbably many of the special functions in functions/special.py have similar bugs. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2494\n\n",
    "created_at": "2008-03-12T14:44:25Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "bugs in evaluation of spherical bessel function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2494",
    "user": "https://github.com/williamstein"
}
```
Assignee: jkantor


```
BUG 1:

Hi,
I was just trying to calculate some stuff with spherical Bessel
functions and got this error message:

sage: spherical_bessel_J(3,.1)


....
6823         return x
  6824     except SyntaxError:
-> 6825         raise TypeError, "unable to make sense of Maxima
expression '%s' in SAGE"%s
  6826     finally:
  6827         is_simplified = False

<type 'exceptions.TypeError'>: unable to make sense of Maxima
expression '9.5185197208655641L-6' in SAGE
sage:
KeyboardInterrupt

I checked it, it happens for small values of the argument x.
Does anyone has a solution or work around?

Greets,

schorsch
```


BUG2

```
sage: spherical_bessel_J(3,.1, algorithm='scipy')
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/Users/was/Downloads/z/<ipython console> in <module>()

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/functions/special.py in spherical_bessel_J(n, var, algorithm)
    782         ans = ans.replace(")","")
    783         ans = ans.replace("j","*I")
--> 784         return sage_eval(ans)
    785     elif algorithm == 'maxima':
    786         _init()

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/misc/sage_eval.py in sage_eval(source, locals)
    108     p = preparse(source)
    109     try:
--> 110         return eval(p, sage.all.__dict__, locals)
    111     except SyntaxError, msg:
    112         raise SyntaxError, "%s\nError using SAGE to evaluate '%s'"%(msg, p)

/Users/was/Downloads/z/<string> in <module>()

<type 'exceptions.NameError'>: name 'array' is not defined
```


Probably many of the special functions in functions/special.py have similar bugs. 

Issue created by migration from https://trac.sagemath.org/ticket/2494





---

archive/issue_comments_016861.json:
```json
{
    "body": "Changing assignee from jkantor to @mwhansen.",
    "created_at": "2009-06-04T21:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2494#issuecomment-16861",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from jkantor to @mwhansen.



---

archive/issue_comments_016862.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-04T21:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2494#issuecomment-16862",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016863.json:
```json
{
    "body": "Note that BUG 1 has disappeared in sage-4.1.1:\n\n\n```\nsage: spherical_bessel_J(3,.1)\n9.51851972087e-06\n```\n\n\nBUG 2 is still there.",
    "created_at": "2009-08-24T09:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2494#issuecomment-16863",
    "user": "https://github.com/aghitza"
}
```

Note that BUG 1 has disappeared in sage-4.1.1:


```
sage: spherical_bessel_J(3,.1)
9.51851972087e-06
```


BUG 2 is still there.



---

archive/issue_comments_016864.json:
```json
{
    "body": "Attachment [trac_2494.patch](tarball://root/attachments/some-uuid/ticket2494/trac_2494.patch) by @mwhansen created at 2010-01-17 06:08:48",
    "created_at": "2010-01-17T06:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2494#issuecomment-16864",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_2494.patch](tarball://root/attachments/some-uuid/ticket2494/trac_2494.patch) by @mwhansen created at 2010-01-17 06:08:48



---

archive/issue_comments_016865.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T06:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2494#issuecomment-16865",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_016866.json:
```json
{
    "body": "Looks good and passes tests.",
    "created_at": "2010-01-23T02:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2494#issuecomment-16866",
    "user": "https://github.com/aghitza"
}
```

Looks good and passes tests.



---

archive/issue_comments_016867.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-23T02:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2494#issuecomment-16867",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_016868.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-24T12:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2494#issuecomment-16868",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_002673.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-24T12:01:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2494",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2494#event-2673"
}
```
