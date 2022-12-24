# Issue 2627: Integer(abs(gamma(n+1))) is not always equal to factorial(n) for n a positive integer

archive/issues_002627.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: gamma function, factorial\n\n`Integer(abs(gamma(n+1))) - factorial(n)` should be zero for all positive integers, but on 2.10.3, I get:\n\n\n```\nsage: [ Integer(abs(gamma(n+1))) - factorial(n) for n in range(20, 30) ]\n\n[0,\n 0,\n 0,\n 1572864,\n -29360128,\n 71303168,\n 14738784256,\n -220528115712,\n 11417398804480,\n -55923527647232]\n```\n\n\nI'm guessing this is due to some numerical noise. There should be some type-checking done in the gamma function.\n\nI would also like to see, for instance, gamma(1/2) return sqrt(pi) instead of a floating point number, although I think the above issue is more pressing and easier to deal with.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2627\n\n",
    "created_at": "2008-03-21T06:59:01Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "Integer(abs(gamma(n+1))) is not always equal to factorial(n) for n a positive integer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2627",
    "user": "ddrake"
}
```
Assignee: cwitty

Keywords: gamma function, factorial

`Integer(abs(gamma(n+1))) - factorial(n)` should be zero for all positive integers, but on 2.10.3, I get:


```
sage: [ Integer(abs(gamma(n+1))) - factorial(n) for n in range(20, 30) ]

[0,
 0,
 0,
 1572864,
 -29360128,
 71303168,
 14738784256,
 -220528115712,
 11417398804480,
 -55923527647232]
```


I'm guessing this is due to some numerical noise. There should be some type-checking done in the gamma function.

I would also like to see, for instance, gamma(1/2) return sqrt(pi) instead of a floating point number, although I think the above issue is more pressing and easier to deal with.

Issue created by migration from https://trac.sagemath.org/ticket/2627





---

archive/issue_comments_018051.json:
```json
{
    "body": "The right fix would probably be to add a .gamma() method to the integers, and then also make the generic gamma use interval arithmetic.",
    "created_at": "2008-03-21T07:04:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2627#issuecomment-18051",
    "user": "mhansen"
}
```

The right fix would probably be to add a .gamma() method to the integers, and then also make the generic gamma use interval arithmetic.



---

archive/issue_comments_018052.json:
```json
{
    "body": "Attachment [2627-exact-gamma.patch](tarball://root/attachments/some-uuid/ticket2627/2627-exact-gamma.patch) by robertwb created at 2008-03-26 11:17:51\n\n\n```\nsage: sage: [ Integer(abs(gamma(n+1))) - factorial(n) for n in range(20, 30) ]\n[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\nsage: gamma(1/2)\nsqrt(pi)\nsage: gamma(-101/2)\n-2251799813685248*sqrt(pi)/275264606114823679801052037785492781962370429385126144787167211167753726318359375\n```\n",
    "created_at": "2008-03-26T11:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2627#issuecomment-18052",
    "user": "robertwb"
}
```

Attachment [2627-exact-gamma.patch](tarball://root/attachments/some-uuid/ticket2627/2627-exact-gamma.patch) by robertwb created at 2008-03-26 11:17:51


```
sage: sage: [ Integer(abs(gamma(n+1))) - factorial(n) for n in range(20, 30) ]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sage: gamma(1/2)
sqrt(pi)
sage: gamma(-101/2)
-2251799813685248*sqrt(pi)/275264606114823679801052037785492781962370429385126144787167211167753726318359375
```




---

archive/issue_comments_018053.json:
```json
{
    "body": "The patch applies cleanly and works as advertised. I tested with integers as large as 500000 and had no troubles. The half-integer and multifactorial stuff works too. Positive review for functionality; I'm not familiar enough with the Pyrex code to review that, although it looks pretty straightforward.\n\nThe doctests also pass for me.",
    "created_at": "2008-03-27T08:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2627#issuecomment-18053",
    "user": "ddrake"
}
```

The patch applies cleanly and works as advertised. I tested with integers as large as 500000 and had no troubles. The half-integer and multifactorial stuff works too. Positive review for functionality; I'm not familiar enough with the Pyrex code to review that, although it looks pretty straightforward.

The doctests also pass for me.



---

archive/issue_comments_018054.json:
```json
{
    "body": "I looked at the Cython code.  Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-27T08:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2627#issuecomment-18054",
    "user": "mabshoff"
}
```

I looked at the Cython code.  Positive review.

Cheers,

Michael



---

archive/issue_comments_018055.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-27T09:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2627#issuecomment-18055",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_comments_018056.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-27T09:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2627#issuecomment-18056",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018057.json:
```json
{
    "body": "The is one doctest failure:\n\n```\nsage -t  devel/sage-main/sage/functions/transcendental.py\n**********************************************************************\nFile \"transcendental.py\", line 102:\n    sage: gamma(6)\nExpected:\n    120.000000000000\nGot:\n    120\n**********************************************************************\n```\n\nTrivial fix coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-27T09:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2627#issuecomment-18057",
    "user": "mabshoff"
}
```

The is one doctest failure:

```
sage -t  devel/sage-main/sage/functions/transcendental.py
**********************************************************************
File "transcendental.py", line 102:
    sage: gamma(6)
Expected:
    120.000000000000
Got:
    120
**********************************************************************
```

Trivial fix coming up.

Cheers,

Michael



---

archive/issue_comments_018058.json:
```json
{
    "body": "Attachment [trac_2627_doctest-fix.patch](tarball://root/attachments/some-uuid/ticket2627/trac_2627_doctest-fix.patch) by mabshoff created at 2008-03-27 09:35:49\n\nMerged trac_2627_doctest-fix.patch in Sage 2.11.alpha2",
    "created_at": "2008-03-27T09:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2627#issuecomment-18058",
    "user": "mabshoff"
}
```

Attachment [trac_2627_doctest-fix.patch](tarball://root/attachments/some-uuid/ticket2627/trac_2627_doctest-fix.patch) by mabshoff created at 2008-03-27 09:35:49

Merged trac_2627_doctest-fix.patch in Sage 2.11.alpha2
