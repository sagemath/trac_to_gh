# Issue 1983: [with patch; needs review] change 0^0, for 0 a Sage integer, to evaluate to 1 for consistency with Python, PARI, Magma, Maple, MPFR, GMP, etc.

archive/issues_001983.json:
```json
{
    "body": "Assignee: somebody\n\nAs justification that this is for *consistency*, everybody defines 0^0 to be 1, except Mathematica:\n\n\n```\n\nsage: gp('0^0')\n1\nsage: magma('0^0')\n1\nsage: mathematica('0^0')\n...\nMathematica ERROR:\n\t                                        0\nPower::indet: Indeterminate expression 0  encountered.\nsage: maple('0^0')\n1\nsage: int(0)^int(0)\n1\nsage: float(0)^float(0)\n1.0\nsage: 0.0^0.0\n1.00000000000000\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1983\n\n",
    "created_at": "2008-01-30T13:35:24Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch; needs review] change 0^0, for 0 a Sage integer, to evaluate to 1 for consistency with Python, PARI, Magma, Maple, MPFR, GMP, etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1983",
    "user": "was"
}
```
Assignee: somebody

As justification that this is for *consistency*, everybody defines 0^0 to be 1, except Mathematica:


```

sage: gp('0^0')
1
sage: magma('0^0')
1
sage: mathematica('0^0')
...
Mathematica ERROR:
	                                        0
Power::indet: Indeterminate expression 0  encountered.
sage: maple('0^0')
1
sage: int(0)^int(0)
1
sage: float(0)^float(0)
1.0
sage: 0.0^0.0
1.00000000000000
```


Issue created by migration from https://trac.sagemath.org/ticket/1983





---

archive/issue_comments_012848.json:
```json
{
    "body": "Attachment [trac-1983-0to0.patch](tarball://root/attachments/some-uuid/ticket1983/trac-1983-0to0.patch) by was created at 2008-01-30 13:36:17",
    "created_at": "2008-01-30T13:36:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1983#issuecomment-12848",
    "user": "was"
}
```

Attachment [trac-1983-0to0.patch](tarball://root/attachments/some-uuid/ticket1983/trac-1983-0to0.patch) by was created at 2008-01-30 13:36:17



---

archive/issue_comments_012849.json:
```json
{
    "body": "This works as described.",
    "created_at": "2008-02-01T05:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1983#issuecomment-12849",
    "user": "jkantor"
}
```

This works as described.



---

archive/issue_comments_012850.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-01T05:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1983#issuecomment-12850",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012851.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc4",
    "created_at": "2008-02-01T05:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1983#issuecomment-12851",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc4
