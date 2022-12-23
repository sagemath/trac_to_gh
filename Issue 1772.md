# Issue 1772: bug somewhere in the symbolics

archive/issues_001772.json:
```json
{
    "body": "Assignee: was\n\nThis is from Hector:\n\n\n```\nI also hit this bug while doing this (taken from the \"piecewise\"\ndocumentation):\n\nsage: f1 = lambda x:-1\nsage: f2 = lambda x:2\nsage: f = Piecewise([[(0,pi/2),f1],[(pi/2,pi),f2]])\nsage: P = f.plot_fourier_series_partial_sum(15,pi,-5,5)   # long time\nboom\n...\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/calculus/calculus.py in <lambda>(i)\n   3607             # We need to do this maximum to correctly handle the case where\n   3608             # self is something like (sin+1)\n-> 3609             n = max( max(map(lambda i: i.number_of_arguments(), self._operands)+[0]), len(variables) )\n   3610         self.__number_of_args = n\n   3611         return n\n\n<type 'exceptions.AttributeError'>: 'Pi' object has no attribute 'number_of_arguments'\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1772\n\n",
    "created_at": "2008-01-14T05:58:16Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "bug somewhere in the symbolics",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1772",
    "user": "was"
}
```
Assignee: was

This is from Hector:


```
I also hit this bug while doing this (taken from the "piecewise"
documentation):

sage: f1 = lambda x:-1
sage: f2 = lambda x:2
sage: f = Piecewise([[(0,pi/2),f1],[(pi/2,pi),f2]])
sage: P = f.plot_fourier_series_partial_sum(15,pi,-5,5)   # long time
boom
...

/Users/was/s/local/lib/python2.5/site-packages/sage/calculus/calculus.py in <lambda>(i)
   3607             # We need to do this maximum to correctly handle the case where
   3608             # self is something like (sin+1)
-> 3609             n = max( max(map(lambda i: i.number_of_arguments(), self._operands)+[0]), len(variables) )
   3610         self.__number_of_args = n
   3611         return n

<type 'exceptions.AttributeError'>: 'Pi' object has no attribute 'number_of_arguments'
```




Issue created by migration from https://trac.sagemath.org/ticket/1772





---

archive/issue_comments_011203.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-15T01:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1772#issuecomment-11203",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011204.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2008-01-15T01:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1772#issuecomment-11204",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_011205.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-18T21:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1772#issuecomment-11205",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_011206.json:
```json
{
    "body": "I also fixed this in the same way earlier today (as part of one my other patches), but my patch was just a few lines to actually fix the listed problem.  The patch attached to this ticket, fixes the problem and does a HUGE amount more to vastly improve doctesting in some files, etc.  I.e., this is _great_. \n\nI have not fully reviewed the patch yet, though I've looked it over by eye and it looks very good.",
    "created_at": "2008-01-18T21:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1772#issuecomment-11206",
    "user": "was"
}
```

I also fixed this in the same way earlier today (as part of one my other patches), but my patch was just a few lines to actually fix the listed problem.  The patch attached to this ticket, fixes the problem and does a HUGE amount more to vastly improve doctesting in some files, etc.  I.e., this is _great_. 

I have not fully reviewed the patch yet, though I've looked it over by eye and it looks very good.



---

archive/issue_comments_011207.json:
```json
{
    "body": "Attachment\n\nFixes the one doctest failure in constant.py",
    "created_at": "2008-01-20T00:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1772#issuecomment-11207",
    "user": "rlm"
}
```

Attachment

Fixes the one doctest failure in constant.py



---

archive/issue_comments_011208.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-20T01:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1772#issuecomment-11208",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011209.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-20T01:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1772#issuecomment-11209",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha0
