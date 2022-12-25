# Issue 962: automatic precision extension for long decimal literals does very strange things

archive/issues_000962.json:
```json
{
    "body": "Assignee: somebody\n\nLong decimal literals become floating-point numbers whose precision depends on the length of the input literal *in characters*.  See this script for some of the confusing (and, in my opinion, wrong) behavior that results.\n\n```\nsage: (1.10000000000000000000).prec()\n73\nsage: (1.10000000000000000000e0).prec()\n79\nsage: (1e-25).prec()\n53\nsage: (0.0000000000000000000000001).prec()\n89\nsage: (00000000.0000000000000000000000001).prec()\n112\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/962\n\n",
    "created_at": "2007-10-21T15:09:21Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "automatic precision extension for long decimal literals does very strange things",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/962",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: somebody

Long decimal literals become floating-point numbers whose precision depends on the length of the input literal *in characters*.  See this script for some of the confusing (and, in my opinion, wrong) behavior that results.

```
sage: (1.10000000000000000000).prec()
73
sage: (1.10000000000000000000e0).prec()
79
sage: (1e-25).prec()
53
sage: (0.0000000000000000000000001).prec()
89
sage: (00000000.0000000000000000000000001).prec()
112
```



Issue created by migration from https://trac.sagemath.org/ticket/962





---

archive/issue_comments_005840.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2007-10-23T22:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5840",
    "user": "https://github.com/malb"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_005841.json:
```json
{
    "body": "Changing assignee from cwitty to @mwhansen.",
    "created_at": "2007-10-24T20:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5841",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from cwitty to @mwhansen.



---

archive/issue_comments_005842.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-24T20:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5842",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005843.json:
```json
{
    "body": "Attachment [962.patch](tarball://root/attachments/some-uuid/ticket962/962.patch) by @mwhansen created at 2007-11-13 03:20:25\n\nInitial version",
    "created_at": "2007-11-13T03:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5843",
    "user": "https://github.com/mwhansen"
}
```

Attachment [962.patch](tarball://root/attachments/some-uuid/ticket962/962.patch) by @mwhansen created at 2007-11-13 03:20:25

Initial version



---

archive/issue_comments_005844.json:
```json
{
    "body": "I posted an initial patch which fixes some of the major issues.  I would like others to comment on it to make sure the final version of this patch does the \"right thing\" since it will break lots of doctests.",
    "created_at": "2007-11-13T03:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5844",
    "user": "https://github.com/mwhansen"
}
```

I posted an initial patch which fixes some of the major issues.  I would like others to comment on it to make sure the final version of this patch does the "right thing" since it will break lots of doctests.



---

archive/issue_comments_005845.json:
```json
{
    "body": "Here is the behavior of the above examples after the patch:\n\n```\nsage: sage: (1.10000000000000000000).prec()\n74\nsage: sage: (1.10000000000000000000e0).prec()\n74\nsage: sage: (1e-25).prec()\n87\nsage: sage: (0.0000000000000000000000001).prec()\n87\nsage: sage: (00000000.0000000000000000000000001).prec()\n87\n```\n",
    "created_at": "2007-11-13T03:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5845",
    "user": "https://github.com/mwhansen"
}
```

Here is the behavior of the above examples after the patch:

```
sage: sage: (1.10000000000000000000).prec()
74
sage: sage: (1.10000000000000000000e0).prec()
74
sage: sage: (1e-25).prec()
87
sage: sage: (0.0000000000000000000000001).prec()
87
sage: sage: (00000000.0000000000000000000000001).prec()
87
```




---

archive/issue_comments_005846.json:
```json
{
    "body": "Actually, I think that all of the last three examples should give 53 (that is, leading zeroes shouldn't affect the precision).  I think that matches the rules for significant figures I learned in grade school...",
    "created_at": "2007-11-13T05:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5846",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Actually, I think that all of the last three examples should give 53 (that is, leading zeroes shouldn't affect the precision).  I think that matches the rules for significant figures I learned in grade school...



---

archive/issue_comments_005847.json:
```json
{
    "body": "NOT YET -- note that I think many doctests will (and should) break after applying this patch, so this isn't being posted to actually include in the next release.  It's being posted for feedback.   After people like it, then Mike will post an additional patch that fixes all failing doctests. \n\nI also think I agree with Carl witty's remark above about significant figures.",
    "created_at": "2007-11-18T04:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5847",
    "user": "https://github.com/williamstein"
}
```

NOT YET -- note that I think many doctests will (and should) break after applying this patch, so this isn't being posted to actually include in the next release.  It's being posted for feedback.   After people like it, then Mike will post an additional patch that fixes all failing doctests. 

I also think I agree with Carl witty's remark above about significant figures.



---

archive/issue_comments_005848.json:
```json
{
    "body": "Patch updated that now gives the following results:\n\n```\nsage: sage: sage: (1.10000000000000000000).prec()\n74\nsage: sage: sage: (1.10000000000000000000e0).prec()\n74\nsage: sage: sage: (1e-25).prec()\n53\nsage: sage: sage: (0.0000000000000000000000001).prec()\n53\nsage: sage: sage: (00000000.0000000000000000000000001).prec()\n53\n```\n",
    "created_at": "2007-12-01T18:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5848",
    "user": "https://github.com/mwhansen"
}
```

Patch updated that now gives the following results:

```
sage: sage: sage: (1.10000000000000000000).prec()
74
sage: sage: sage: (1.10000000000000000000e0).prec()
74
sage: sage: sage: (1e-25).prec()
53
sage: sage: sage: (0.0000000000000000000000001).prec()
53
sage: sage: sage: (00000000.0000000000000000000000001).prec()
53
```




---

archive/issue_comments_005849.json:
```json
{
    "body": "Attachment [962-2.patch](tarball://root/attachments/some-uuid/ticket962/962-2.patch) by cwitty created at 2007-12-01 21:54:33\n\nLooks good to me!  Thank you for making so many changes at my request.",
    "created_at": "2007-12-01T21:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5849",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [962-2.patch](tarball://root/attachments/some-uuid/ticket962/962-2.patch) by cwitty created at 2007-12-01 21:54:33

Looks good to me!  Thank you for making so many changes at my request.



---

archive/issue_comments_005850.json:
```json
{
    "body": "This causes the following doctest failures:\n\n\n```\n        sage -t  devel/sage-main/sage/modular/dirichlet.py\n        sage -t  devel/sage-main/sage/gsl/dft.py\n        sage -t  devel/sage-main/sage/functions/constants.py\n        sage -t  devel/sage-main/sage/calculus/calculus.py\n        sage -t  devel/sage-main/sage/calculus/wester.py\n        sage -t  devel/sage-main/sage/interfaces/gp.py\n        sage -t  devel/sage-main/sage/misc/functional.py\n        sage -t  devel/sage-main/sage/rings/real_mpfr.pyx\n        sage -t  devel/sage-main/sage/rings/fraction_field_element.py\n        sage -t  devel/sage-main/sage/rings/rational.pyx\n        sage -t  devel/sage-main/sage/rings/arith.py\n        sage -t  devel/sage-main/sage/rings/integer.pyx\n        sage -t  devel/sage-main/sage/rings/contfrac.py\n        sage -t  devel/sage-main/sage/rings/qqbar.py\n        sage -t  devel/sage-main/sage/rings/number_field/number_field.py\n        sage -t  devel/sage-main/sage/rings/complex_number.pyx\n        sage -t  devel/sage-main/sage/rings/complex_interval.pyx\n        sage -t  devel/sage-main/sage/rings/polynomial/real_roots.pyx\n        sage -t  devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\n        sage -t  devel/sage-main/sage/rings/polynomial/complex_roots.py\n        sage -t  devel/sage-main/sage/rings/real_mpfi.pyx\n```\n\n\nI will post a patch in a bit fixing this.",
    "created_at": "2007-12-02T01:15:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5850",
    "user": "https://github.com/mwhansen"
}
```

This causes the following doctest failures:


```
        sage -t  devel/sage-main/sage/modular/dirichlet.py
        sage -t  devel/sage-main/sage/gsl/dft.py
        sage -t  devel/sage-main/sage/functions/constants.py
        sage -t  devel/sage-main/sage/calculus/calculus.py
        sage -t  devel/sage-main/sage/calculus/wester.py
        sage -t  devel/sage-main/sage/interfaces/gp.py
        sage -t  devel/sage-main/sage/misc/functional.py
        sage -t  devel/sage-main/sage/rings/real_mpfr.pyx
        sage -t  devel/sage-main/sage/rings/fraction_field_element.py
        sage -t  devel/sage-main/sage/rings/rational.pyx
        sage -t  devel/sage-main/sage/rings/arith.py
        sage -t  devel/sage-main/sage/rings/integer.pyx
        sage -t  devel/sage-main/sage/rings/contfrac.py
        sage -t  devel/sage-main/sage/rings/qqbar.py
        sage -t  devel/sage-main/sage/rings/number_field/number_field.py
        sage -t  devel/sage-main/sage/rings/complex_number.pyx
        sage -t  devel/sage-main/sage/rings/complex_interval.pyx
        sage -t  devel/sage-main/sage/rings/polynomial/real_roots.pyx
        sage -t  devel/sage-main/sage/rings/polynomial/polynomial_element.pyx
        sage -t  devel/sage-main/sage/rings/polynomial/complex_roots.py
        sage -t  devel/sage-main/sage/rings/real_mpfi.pyx
```


I will post a patch in a bit fixing this.



---

archive/issue_comments_005851.json:
```json
{
    "body": "Excellent!  I read through 962-doctests.patch (yes, I really did), and I only saw one issue: on real_mpfr.pyx line 21, we will need to change:\n\n```\n    2147483647.00000         # 32-bit\n```\n\nto\n\n```\n    2.14748364700000e9       # 32-bit\n```\n",
    "created_at": "2007-12-02T02:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5851",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Excellent!  I read through 962-doctests.patch (yes, I really did), and I only saw one issue: on real_mpfr.pyx line 21, we will need to change:

```
    2147483647.00000         # 32-bit
```

to

```
    2.14748364700000e9       # 32-bit
```




---

archive/issue_comments_005852.json:
```json
{
    "body": "The patches should be applied in this order:\n1) 962-2.patch\n2) 962-doctests.patch",
    "created_at": "2007-12-02T02:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5852",
    "user": "https://github.com/mwhansen"
}
```

The patches should be applied in this order:
1) 962-2.patch
2) 962-doctests.patch



---

archive/issue_comments_005853.json:
```json
{
    "body": "Attachment [962-doctests.patch](tarball://root/attachments/some-uuid/ticket962/962-doctests.patch) by @mwhansen created at 2007-12-02 02:48:04",
    "created_at": "2007-12-02T02:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5853",
    "user": "https://github.com/mwhansen"
}
```

Attachment [962-doctests.patch](tarball://root/attachments/some-uuid/ticket962/962-doctests.patch) by @mwhansen created at 2007-12-02 02:48:04



---

archive/issue_comments_005854.json:
```json
{
    "body": "Merged in 2.8.15.alpha2.",
    "created_at": "2007-12-02T03:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5854",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha2.



---

archive/issue_events_001084.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-02T03:06:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/962#event-1084"
}
```



---

archive/issue_comments_005855.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T03:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/962#issuecomment-5855",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
