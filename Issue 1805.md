# Issue 1805: improve doctest coverage for structure/factorization.py

archive/issues_001805.json:
```json
{
    "body": "Assignee: failure\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1805\n\n",
    "created_at": "2008-01-17T19:58:11Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "improve doctest coverage for structure/factorization.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1805",
    "user": "was"
}
```
Assignee: failure



Issue created by migration from https://trac.sagemath.org/ticket/1805





---

archive/issue_comments_011407.json:
```json
{
    "body": "Before:\n\n```\nsage@modular:~/d/sage/sage/structure$ sage -coverage factorization.py \n----------------------------------------------------------------------\nfactorization.py\nSCORE factorization.py: 28% (6 of 21)\n\nMissing documentation:\n\t * __init__(self, x, unit=None, cr=False, sort=True)\n\t * _set_cr(self, cr)\n\t * sort(self)\n\t * _cmp(f,g)\n\t * _cmp(f,g)\n\t * _cmp(f,g)\n\t * __reduce__(self)\n\t * _cr(self)\n\t * _repr_(self)\n\t * _latex_(self)\n\t * __pow__(self, n)\n\t * __invert__(self)\n\t * Factorization_deduce_unit(x, mul)\n\n\nMissing doctests:\n\t * unit_part(self)\n\t * expand(self)\n\n```\n\n\nAfter:\n\n```\nteragon:structure was$ sage -coverage factorization.py\n----------------------------------------------------------------------\nfactorization.py\nSCORE factorization.py: 100% (22 of 22)\n----------------------------------------------------------------------\n```\n\n\nand I fixed numerous conceptual bugs/mistakes in that file.",
    "created_at": "2008-01-17T20:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11407",
    "user": "was"
}
```

Before:

```
sage@modular:~/d/sage/sage/structure$ sage -coverage factorization.py 
----------------------------------------------------------------------
factorization.py
SCORE factorization.py: 28% (6 of 21)

Missing documentation:
	 * __init__(self, x, unit=None, cr=False, sort=True)
	 * _set_cr(self, cr)
	 * sort(self)
	 * _cmp(f,g)
	 * _cmp(f,g)
	 * _cmp(f,g)
	 * __reduce__(self)
	 * _cr(self)
	 * _repr_(self)
	 * _latex_(self)
	 * __pow__(self, n)
	 * __invert__(self)
	 * Factorization_deduce_unit(x, mul)


Missing doctests:
	 * unit_part(self)
	 * expand(self)

```


After:

```
teragon:structure was$ sage -coverage factorization.py
----------------------------------------------------------------------
factorization.py
SCORE factorization.py: 100% (22 of 22)
----------------------------------------------------------------------
```


and I fixed numerous conceptual bugs/mistakes in that file.



---

archive/issue_comments_011408.json:
```json
{
    "body": "Changing assignee from failure to was.",
    "created_at": "2008-01-17T20:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11408",
    "user": "was"
}
```

Changing assignee from failure to was.



---

archive/issue_comments_011409.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-17T20:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11409",
    "user": "was"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011410.json:
```json
{
    "body": "Attachment [trac-1805.patch](tarball://root/attachments/some-uuid/ticket1805/trac-1805.patch) by was created at 2008-01-17 20:03:24\n\nThis is a preliminary patch.  I'm now doctesting all of sage-2.10 with this patch applied to see what else is broke.  I'll post another patch that fixes the problems later.",
    "created_at": "2008-01-17T20:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11410",
    "user": "was"
}
```

Attachment [trac-1805.patch](tarball://root/attachments/some-uuid/ticket1805/trac-1805.patch) by was created at 2008-01-17 20:03:24

This is a preliminary patch.  I'm now doctesting all of sage-2.10 with this patch applied to see what else is broke.  I'll post another patch that fixes the problems later.



---

archive/issue_comments_011411.json:
```json
{
    "body": "Attachment [trac-1805-part2.patch](tarball://root/attachments/some-uuid/ticket1805/trac-1805-part2.patch) by was created at 2008-01-17 21:47:11\n\nthis part 2 fixes some additional issues, typos, etc., I saw when proofreading my patch.",
    "created_at": "2008-01-17T21:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11411",
    "user": "was"
}
```

Attachment [trac-1805-part2.patch](tarball://root/attachments/some-uuid/ticket1805/trac-1805-part2.patch) by was created at 2008-01-17 21:47:11

this part 2 fixes some additional issues, typos, etc., I saw when proofreading my patch.



---

archive/issue_comments_011412.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-01-20T06:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11412",
    "user": "ncalexan"
}
```

Changing status from assigned to new.



---

archive/issue_comments_011413.json:
```json
{
    "body": "Changing assignee from was to ncalexan.",
    "created_at": "2008-01-20T06:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11413",
    "user": "ncalexan"
}
```

Changing assignee from was to ncalexan.



---

archive/issue_comments_011414.json:
```json
{
    "body": "I fixed 1804 not knowing that 1805 did a lot of the same work.  Damn!  They should both be applied but of course they need to be merged.  I'll try to do it tomorrow.",
    "created_at": "2008-01-20T06:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11414",
    "user": "ncalexan"
}
```

I fixed 1804 not knowing that 1805 did a lot of the same work.  Damn!  They should both be applied but of course they need to be merged.  I'll try to do it tomorrow.



---

archive/issue_comments_011415.json:
```json
{
    "body": "Nick, can you give this another review?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-18T14:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11415",
    "user": "mabshoff"
}
```

Nick, can you give this another review?

Cheers,

Michael



---

archive/issue_comments_011416.json:
```json
{
    "body": "Yes, please review it.  My patch fixes a number of subtle serious bugs involving pickling factorizations, which could cause people problems.",
    "created_at": "2008-02-18T23:58:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11416",
    "user": "was"
}
```

Yes, please review it.  My patch fixes a number of subtle serious bugs involving pickling factorizations, which could cause people problems.



---

archive/issue_comments_011417.json:
```json
{
    "body": "These patches don't import cleanly against current.  They also need the bug doctest removed.",
    "created_at": "2008-03-01T22:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11417",
    "user": "gfurnish"
}
```

These patches don't import cleanly against current.  They also need the bug doctest removed.



---

archive/issue_comments_011418.json:
```json
{
    "body": "I've attached a brand new rebased patch which also fixes a critical bug in factorization (!) which may expose a bug in totallyrealfield, by the way.\n\nI also changed factorizations to be immutable, as suggested by the referee, and they now no longer derive from list, so that __cmp__ works correctly.",
    "created_at": "2008-03-02T00:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11418",
    "user": "was"
}
```

I've attached a brand new rebased patch which also fixes a critical bug in factorization (!) which may expose a bug in totallyrealfield, by the way.

I also changed factorizations to be immutable, as suggested by the referee, and they now no longer derive from list, so that __cmp__ works correctly.



---

archive/issue_comments_011419.json:
```json
{
    "body": "new rebased version",
    "created_at": "2008-03-02T00:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11419",
    "user": "was"
}
```

new rebased version



---

archive/issue_comments_011420.json:
```json
{
    "body": "Attachment [sage-1805-part2-rebased.patch](tarball://root/attachments/some-uuid/ticket1805/sage-1805-part2-rebased.patch) by was created at 2008-03-02 02:49:13",
    "created_at": "2008-03-02T02:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11420",
    "user": "was"
}
```

Attachment [sage-1805-part2-rebased.patch](tarball://root/attachments/some-uuid/ticket1805/sage-1805-part2-rebased.patch) by was created at 2008-03-02 02:49:13



---

archive/issue_comments_011421.json:
```json
{
    "body": "Attachment [sage-1805-rebase_part3.patch](tarball://root/attachments/some-uuid/ticket1805/sage-1805-rebase_part3.patch) by was created at 2008-03-02 02:52:59",
    "created_at": "2008-03-02T02:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11421",
    "user": "was"
}
```

Attachment [sage-1805-rebase_part3.patch](tarball://root/attachments/some-uuid/ticket1805/sage-1805-rebase_part3.patch) by was created at 2008-03-02 02:52:59



---

archive/issue_comments_011422.json:
```json
{
    "body": "sage -t  devel/sage-patch1805/build/sage/structure/factorization.py**********************************************************************\nFile \"factorization.py\", line 602:\n    sage: F = factor(-2*x^2 - 1); F\nExpected:\n    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)\nGot:\n    (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)\n**********************************************************************\n\nPositive review pending fix.",
    "created_at": "2008-03-02T06:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11422",
    "user": "gfurnish"
}
```

sage -t  devel/sage-patch1805/build/sage/structure/factorization.py**********************************************************************
File "factorization.py", line 602:
    sage: F = factor(-2*x^2 - 1); F
Expected:
    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)
Got:
    (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)
**********************************************************************

Positive review pending fix.



---

archive/issue_comments_011423.json:
```json
{
    "body": "\n```\nsage -t  devel/sage-patch1805/build/sage/structure/factorization.py\n**********************************************************************\nFile \"factorization.py\", line 602:\n    sage: F = factor(-2*x^2 - 1); F\nExpected:\n    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)\nGot:\n    (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)\n**********************************************************************\n```\n",
    "created_at": "2008-03-02T06:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11423",
    "user": "gfurnish"
}
```


```
sage -t  devel/sage-patch1805/build/sage/structure/factorization.py
**********************************************************************
File "factorization.py", line 602:
    sage: F = factor(-2*x^2 - 1); F
Expected:
    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)
Got:
    (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)
**********************************************************************
```




---

archive/issue_comments_011424.json:
```json
{
    "body": "[[[\nsage -t  devel/sage-patch1805/build/sage/structure/factorization.py\n**********************************************************************\nFile \"factorization.py\", line 602:\n    sage: F = factor(-2*x^2 - 1); F\nExpected:\n    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)\nGot:\n    (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)\n**********************************************************************\n]]]",
    "created_at": "2008-03-02T06:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11424",
    "user": "gfurnish"
}
```

[[[
sage -t  devel/sage-patch1805/build/sage/structure/factorization.py
**********************************************************************
File "factorization.py", line 602:
    sage: F = factor(-2*x^2 - 1); F
Expected:
    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)
Got:
    (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)
**********************************************************************
]]]



---

archive/issue_comments_011425.json:
```json
{
    "body": "\n```\nsage -t  devel/sage-patch1805/build/sage/structure/factorization.py**********************************************************************\nFile \"factorization.py\", line 602:\n    sage: F = factor(-2*x^2 - 1); F\nExpected:\n    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)\nGot:\n    (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)\n**********************************************************************\n```\n",
    "created_at": "2008-03-02T06:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11425",
    "user": "gfurnish"
}
```


```
sage -t  devel/sage-patch1805/build/sage/structure/factorization.py**********************************************************************
File "factorization.py", line 602:
    sage: F = factor(-2*x^2 - 1); F
Expected:
    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)
Got:
    (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)
**********************************************************************
```




---

archive/issue_comments_011426.json:
```json
{
    "body": "this should be the final of four patches; it fixes one problem found by the referee (gfurnish)",
    "created_at": "2008-03-02T08:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11426",
    "user": "was"
}
```

this should be the final of four patches; it fixes one problem found by the referee (gfurnish)



---

archive/issue_comments_011427.json:
```json
{
    "body": "Attachment [sage-1805-part4-make_ref_happy.patch](tarball://root/attachments/some-uuid/ticket1805/sage-1805-part4-make_ref_happy.patch) by was created at 2008-03-02 08:09:24\n\nI attached the one small change requested.",
    "created_at": "2008-03-02T08:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11427",
    "user": "was"
}
```

Attachment [sage-1805-part4-make_ref_happy.patch](tarball://root/attachments/some-uuid/ticket1805/sage-1805-part4-make_ref_happy.patch) by was created at 2008-03-02 08:09:24

I attached the one small change requested.



---

archive/issue_comments_011428.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-02T20:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11428",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011429.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc1",
    "created_at": "2008-03-02T20:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1805#issuecomment-11429",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc1
