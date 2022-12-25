# Issue 4098: "T1 =  M1.hecke_operator(13^9)" blows up on 32 bit builds

archive/issues_004098.json:
```json
{
    "body": "Assignee: @craigcitro\n\nRaouf reports in http://groups.google.com/group/sage-support/browse_thread/thread/cf22177234f605a4\n\n```\nvarro:~/sage-3.1.2.rc1 mabshoff$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.2.rc1, Release Date: 2008-09-08                   |\n| Type notebook() for the GUI, and license() for information.        |\nsage: M1 =  ModularSymbols(21,2)\nsage: T1 =  M1.hecke_operator(13^8)\nsage: trace1=T1.trace()\nsage: print trace1\n2651076189\nsage: M1 =  ModularSymbols(21,2) \nsage: T1 =  M1.hecke_operator(13^9) \n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/mabshoff/sage-3.1.2.rc1/<ipython console> in <module>()\n\n/Users/mabshoff/sage-3.1.2.rc1/local/lib/python2.5/site-packages/sage/modular/hecke/module.py in hecke_operator(self, n)\n    858            int n -- an integer at least 1.\n    859         \"\"\"\n--> 860         return self.hecke_algebra().hecke_operator(n)\n    861 \n    862     def T(self, n):\n\n/Users/mabshoff/sage-3.1.2.rc1/local/lib/python2.5/site-packages/sage/modular/hecke/algebra.py in hecke_operator(self, n)\n    184             pass\n    185         n = int(n)\n--> 186         T = hecke_operator.HeckeOperator(self, n)\n    187         self.__hecke_operator[n] = T \n    188         return T\n\n/Users/mabshoff/sage-3.1.2.rc1/local/lib/python2.5/site-packages/sage/modular/hecke/hecke_operator.py in __init__(self, parent, n)\n    360         HeckeAlgebraElement.__init__(self, parent)\n    361         if not isinstance(n, int):\n--> 362             raise TypeError, \"n must be an int\"\n    363         self.__n = n\n    364 \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4098\n\n",
    "created_at": "2008-09-10T20:55:18Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "\"T1 =  M1.hecke_operator(13^9)\" blows up on 32 bit builds",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4098",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @craigcitro

Raouf reports in http://groups.google.com/group/sage-support/browse_thread/thread/cf22177234f605a4

```
varro:~/sage-3.1.2.rc1 mabshoff$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.2.rc1, Release Date: 2008-09-08                   |
| Type notebook() for the GUI, and license() for information.        |
sage: M1 =  ModularSymbols(21,2)
sage: T1 =  M1.hecke_operator(13^8)
sage: trace1=T1.trace()
sage: print trace1
2651076189
sage: M1 =  ModularSymbols(21,2) 
sage: T1 =  M1.hecke_operator(13^9) 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/mabshoff/sage-3.1.2.rc1/<ipython console> in <module>()

/Users/mabshoff/sage-3.1.2.rc1/local/lib/python2.5/site-packages/sage/modular/hecke/module.py in hecke_operator(self, n)
    858            int n -- an integer at least 1.
    859         """
--> 860         return self.hecke_algebra().hecke_operator(n)
    861 
    862     def T(self, n):

/Users/mabshoff/sage-3.1.2.rc1/local/lib/python2.5/site-packages/sage/modular/hecke/algebra.py in hecke_operator(self, n)
    184             pass
    185         n = int(n)
--> 186         T = hecke_operator.HeckeOperator(self, n)
    187         self.__hecke_operator[n] = T 
    188         return T

/Users/mabshoff/sage-3.1.2.rc1/local/lib/python2.5/site-packages/sage/modular/hecke/hecke_operator.py in __init__(self, parent, n)
    360         HeckeAlgebraElement.__init__(self, parent)
    361         if not isinstance(n, int):
--> 362             raise TypeError, "n must be an int"
    363         self.__n = n
    364 
```


Issue created by migration from https://trac.sagemath.org/ticket/4098





---

archive/issue_comments_029513.json:
```json
{
    "body": "Attachment [trac-4098.patch](tarball://root/attachments/some-uuid/ticket4098/trac-4098.patch) by @williamstein created at 2008-09-10 21:10:49",
    "created_at": "2008-09-10T21:10:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4098#issuecomment-29513",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-4098.patch](tarball://root/attachments/some-uuid/ticket4098/trac-4098.patch) by @williamstein created at 2008-09-10 21:10:49



---

archive/issue_comments_029514.json:
```json
{
    "body": "Nice and quick fix. Doctests pass on 32 bits, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-10T21:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4098#issuecomment-29514",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice and quick fix. Doctests pass on 32 bits, positive review.

Cheers,

Michael



---

archive/issue_comments_029515.json:
```json
{
    "body": "You got there before me but I agree.",
    "created_at": "2008-09-10T21:25:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4098#issuecomment-29515",
    "user": "https://github.com/JohnCremona"
}
```

You got there before me but I agree.



---

archive/issue_events_004335.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-10T21:25:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4098",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4098#event-4335"
}
```



---

archive/issue_comments_029516.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-10T21:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4098#issuecomment-29516",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029517.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc2",
    "created_at": "2008-09-10T21:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4098#issuecomment-29517",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc2
