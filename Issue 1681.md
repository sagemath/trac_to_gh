# Issue 1681: serious bug when raising complex(0,1) to the power of the Sage integer 2.

archive/issues_001681.json:
```json
{
    "body": "Assignee: somebody\n\nNotice getting +1 instead of -1:\n\n\n```\nsage: z = complex(0,1)\nsage: z\n1j\nsage: z*z\n(-1+0j)\nsage: z^2\n(1+1.973601453121677e-310j)\nsage: z^float(2)\n(-1+0j)\nsage: z^int(2)\n(-1+0j)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1681\n\n",
    "created_at": "2008-01-04T17:42:31Z",
    "labels": [
        "basic arithmetic",
        "critical",
        "bug"
    ],
    "title": "serious bug when raising complex(0,1) to the power of the Sage integer 2.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1681",
    "user": "was"
}
```
Assignee: somebody

Notice getting +1 instead of -1:


```
sage: z = complex(0,1)
sage: z
1j
sage: z*z
(-1+0j)
sage: z^2
(1+1.973601453121677e-310j)
sage: z^float(2)
(-1+0j)
sage: z^int(2)
(-1+0j)
```


Issue created by migration from https://trac.sagemath.org/ticket/1681





---

archive/issue_comments_010662.json:
```json
{
    "body": "\n```\nmabshoff: is #1681 the fault of the maxime interface?\n[09:44am] william_stein: no\n[09:44am] william_stein: I don't know\n[09:44am] mabshoff: ok\n[09:44am] william_stein: It probably has nothing to do with maxima.\n[09:44am] william_stein: complex(0,1) is built into python\n[09:44am] william_stein: probably the problem is in __pow__ in integer.pyx\n```\n",
    "created_at": "2008-01-04T17:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1681#issuecomment-10662",
    "user": "was"
}
```


```
mabshoff: is #1681 the fault of the maxime interface?
[09:44am] william_stein: no
[09:44am] william_stein: I don't know
[09:44am] mabshoff: ok
[09:44am] william_stein: It probably has nothing to do with maxima.
[09:44am] william_stein: complex(0,1) is built into python
[09:44am] william_stein: probably the problem is in __pow__ in integer.pyx
```




---

archive/issue_comments_010663.json:
```json
{
    "body": "Changing assignee from somebody to robertwb.",
    "created_at": "2008-01-04T21:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1681#issuecomment-10663",
    "user": "robertwb"
}
```

Changing assignee from somebody to robertwb.



---

archive/issue_comments_010664.json:
```json
{
    "body": "This is a bug in Python \n\n```\nsage: complex(0,1).__pow__(2r)\n(1+2.0489322973043257e-310j)\n```\n\n\nI've changed the Integer.__pow__ function to use ** (which should be faster too).",
    "created_at": "2008-01-04T21:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1681#issuecomment-10664",
    "user": "robertwb"
}
```

This is a bug in Python 

```
sage: complex(0,1).__pow__(2r)
(1+2.0489322973043257e-310j)
```


I've changed the Integer.__pow__ function to use ** (which should be faster too).



---

archive/issue_comments_010665.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-04T21:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1681#issuecomment-10665",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010666.json:
```json
{
    "body": "Attachment [1681-complex-pow.diff](tarball://root/attachments/some-uuid/ticket1681/1681-complex-pow.diff) by robertwb created at 2008-01-04 21:10:21",
    "created_at": "2008-01-04T21:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1681#issuecomment-10666",
    "user": "robertwb"
}
```

Attachment [1681-complex-pow.diff](tarball://root/attachments/some-uuid/ticket1681/1681-complex-pow.diff) by robertwb created at 2008-01-04 21:10:21



---

archive/issue_comments_010667.json:
```json
{
    "body": "positive review by was in IRC.",
    "created_at": "2008-01-05T02:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1681#issuecomment-10667",
    "user": "mabshoff"
}
```

positive review by was in IRC.



---

archive/issue_comments_010668.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-05T02:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1681#issuecomment-10668",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010669.json:
```json
{
    "body": "Merged in 2.9.2.rc1.",
    "created_at": "2008-01-05T02:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1681#issuecomment-10669",
    "user": "mabshoff"
}
```

Merged in 2.9.2.rc1.
