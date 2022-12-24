# Issue 4179: [with patch, needs review] ell_finite_field.py "long" doctest fails

archive/issues_004179.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nIn the file \"ell_finite_field.py\" change the line 1013 from\n\n            sage: for p in prime_range(10000):           #long time (~20s)\n\nto\n\n            sage: for p in prime_range(32768, 42768):           #long time (~20s)\n\nto achieve the same intended amount of testing for the elliptic cirves code as such.\n(But do not run into an --- as of this writing --- outstanding bug related to 16-Bit signed integers on Mac OS X 10.4.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/4179\n\n",
    "created_at": "2008-09-23T22:07:17Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] ell_finite_field.py \"long\" doctest fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4179",
    "user": "GeorgSWeber"
}
```
Assignee: GeorgSWeber

In the file "ell_finite_field.py" change the line 1013 from

            sage: for p in prime_range(10000):           #long time (~20s)

to

            sage: for p in prime_range(32768, 42768):           #long time (~20s)

to achieve the same intended amount of testing for the elliptic cirves code as such.
(But do not run into an --- as of this writing --- outstanding bug related to 16-Bit signed integers on Mac OS X 10.4.)

Issue created by migration from https://trac.sagemath.org/ticket/4179





---

archive/issue_comments_030321.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-23T22:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4179#issuecomment-30321",
    "user": "GeorgSWeber"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030322.json:
```json
{
    "body": "Georg,\n\nare you planning to post an actual hg patch?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-23T22:09:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4179#issuecomment-30322",
    "user": "mabshoff"
}
```

Georg,

are you planning to post an actual hg patch?

Cheers,

Michael



---

archive/issue_comments_030323.json:
```json
{
    "body": "I'm not so keen on making this change, since this test was put in originally to show that a previous bug was fixed.  It is natural to use a sequence of primes starting at 2, but not so natural to use a sequence like prime_range(32768, 42768).\n\nGiven that we are tracking the root problem anyway, can we not live with this one doctest failure which only occurs on one type of machine with the long option anyway?",
    "created_at": "2008-09-24T08:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4179#issuecomment-30323",
    "user": "cremona"
}
```

I'm not so keen on making this change, since this test was put in originally to show that a previous bug was fixed.  It is natural to use a sequence of primes starting at 2, but not so natural to use a sequence like prime_range(32768, 42768).

Given that we are tracking the root problem anyway, can we not live with this one doctest failure which only occurs on one type of machine with the long option anyway?



---

archive/issue_comments_030324.json:
```json
{
    "body": "PS this ticket also duplicates #3760.",
    "created_at": "2008-09-24T08:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4179#issuecomment-30324",
    "user": "cremona"
}
```

PS this ticket also duplicates #3760.



---

archive/issue_comments_030325.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-09-24T08:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4179#issuecomment-30325",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_030326.json:
```json
{
    "body": "Replying to [comment:4 cremona]:\n> PS this ticket also duplicates #3760.\n\nOk, I agree with John here and am closing this as a duplicate of #3760. I did comment on that ticket and mentioned this ticket, so the info should not get lost.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T08:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4179#issuecomment-30326",
    "user": "mabshoff"
}
```

Replying to [comment:4 cremona]:
> PS this ticket also duplicates #3760.

Ok, I agree with John here and am closing this as a duplicate of #3760. I did comment on that ticket and mentioned this ticket, so the info should not get lost.

Cheers,

Michael
