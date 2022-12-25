# Issue 2225: [with spkg, with positive review] sage-2.10.2.alpha1 -- genus2reduction is now completely broken (maybe caused by new spkg with makefile?)

archive/issues_002225.json:
```json
{
    "body": "Assignee: mabshoff\n\nI think Tim (the Debian guy) wrote a makefile for genus2reduction.  He possibly messed something up, since now it's completely broken:\n\n```\nsage -t  devel/sage-main/sage/interfaces/genus2reduction.py **********************************************************************\nFile \"genus2reduction.py\", line 197:\n    sage: R = genus2reduction(x^3 - 2*x^2 - 2*x + 1, -5*x^5)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[1]>\", line 1, in <module>\n        R = genus2reduction(x**Integer(3) - Integer(2)*x**Integer(2) - Integer(2)*x + Integer(1), -Integer(5)*x**Integer(5))###line 197:\n    sage: R = genus2reduction(x^3 - 2*x^2 - 2*x + 1, -5*x^5)\n      File \"/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/interfaces/genus2reduction.py\", line 358, in __call__\n        s, Q, P = self.raw(Q, P)\n      File \"/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/interfaces/genus2reduction.py\", line 349, in raw\n        raise ValueError, \"error in input; possibly singular curve? (Q=%s, P=%s)\"%(Q,P)\n    ValueError: error in input; possibly singular curve? (Q=x^3 - 2*x^2 - 2*x + 1, P=-5*x^5)\n**********************************************************************\nFile \"genus2reduction.py\", line 198:\n    sage: R.conductor\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[2]>\", line 1, in <module>\n        R.conductor###line 198:\n    sage: R.conductor\n    NameError: name 'R' is not defined\n**********************************************************************\nFile \"genus2reduction.py\", line 200:\n    sage: factor(R.conductor)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[3]>\", line 1, in <module>\n        factor(R.conductor)###line 200:\n    sage: factor(R.conductor)\n    NameError: name 'R' is not defined\n*\n...\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2225\n\n",
    "closed_at": "2008-02-21T19:18:19Z",
    "created_at": "2008-02-20T06:58:10Z",
    "labels": [
        "component: number theory",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with spkg, with positive review] sage-2.10.2.alpha1 -- genus2reduction is now completely broken (maybe caused by new spkg with makefile?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2225",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

I think Tim (the Debian guy) wrote a makefile for genus2reduction.  He possibly messed something up, since now it's completely broken:

```
sage -t  devel/sage-main/sage/interfaces/genus2reduction.py **********************************************************************
File "genus2reduction.py", line 197:
    sage: R = genus2reduction(x^3 - 2*x^2 - 2*x + 1, -5*x^5)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[1]>", line 1, in <module>
        R = genus2reduction(x**Integer(3) - Integer(2)*x**Integer(2) - Integer(2)*x + Integer(1), -Integer(5)*x**Integer(5))###line 197:
    sage: R = genus2reduction(x^3 - 2*x^2 - 2*x + 1, -5*x^5)
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/interfaces/genus2reduction.py", line 358, in __call__
        s, Q, P = self.raw(Q, P)
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/interfaces/genus2reduction.py", line 349, in raw
        raise ValueError, "error in input; possibly singular curve? (Q=%s, P=%s)"%(Q,P)
    ValueError: error in input; possibly singular curve? (Q=x^3 - 2*x^2 - 2*x + 1, P=-5*x^5)
**********************************************************************
File "genus2reduction.py", line 198:
    sage: R.conductor
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        R.conductor###line 198:
    sage: R.conductor
    NameError: name 'R' is not defined
**********************************************************************
File "genus2reduction.py", line 200:
    sage: factor(R.conductor)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        factor(R.conductor)###line 200:
    sage: factor(R.conductor)
    NameError: name 'R' is not defined
*
...
```

Issue created by migration from https://trac.sagemath.org/ticket/2225





---

archive/issue_comments_014711.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-02-20T14:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2225#issuecomment-14711",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_014712.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-20T14:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2225#issuecomment-14712",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014713.json:
```json
{
    "body": "I will look into this. Make sure to close #2175 once we have resolved this issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-20T14:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2225#issuecomment-14713",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I will look into this. Make sure to close #2175 once we have resolved this issue.

Cheers,

Michael



---

archive/issue_comments_014714.json:
```json
{
    "body": "New, working spkg by was at\n\nhttp://sage.math.washington.edu/home/was/patches/genus2reduction-0.3.p2.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T19:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2225#issuecomment-14714",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

New, working spkg by was at

http://sage.math.washington.edu/home/was/patches/genus2reduction-0.3.p2.spkg

Cheers,

Michael



---

archive/issue_comments_014715.json:
```json
{
    "body": "The spkg looks good. I added a `.hgignore` and also corrected some small issues in SPKG.txt\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T19:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2225#issuecomment-14715",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg looks good. I added a `.hgignore` and also corrected some small issues in SPKG.txt

Cheers,

Michael



---

archive/issue_comments_014716.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-21T19:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2225#issuecomment-14716",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014717.json:
```json
{
    "body": "Merged in Sage 2.10.2.rc0",
    "created_at": "2008-02-21T19:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2225#issuecomment-14717",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.rc0



---

archive/issue_events_005306.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-21T19:18:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2225",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2225#event-5306"
}
```
