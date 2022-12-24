# Issue 4777: Sage is_prime_power is seriously buggy, because pari's ispower is BROKEN

archive/issues_004777.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\n18:18 < wstein> sage: n = \n3089265681159475043336839581081873360674602365963130114355701114591322241990483812812582393906477998611814245513881\n18:18 < wstein> sage: factor(n)\n18:18 < wstein> 150607571^14\n18:18 < wstein> sage: sage.rings.arith.is_prime_power(n)False\n18:18 < wstein> sage: n.is_prime_power()\n18:18 < wstein> False\n18:18 < wstein> sage: is_prime(150607571)\n18:18 < wstein> True\n18:19 < wstein> Yep, Sage's is_prime_power function is just plain wrong.\n18:19 < wstein> Great.\n18:19 < wstein> I wrote that, I think... :-(\n18:20 < wstein> sage: k = pari(n); k.ispower()\n18:20 < wstein> (2, 1757630701017558763141032341047742794506161527817537960891)\n18:20 < wstein> Oh, it's a bug in pari, actually.\n18:20 < wstein> Since pari's ispower is guaranteed to give the maximal k such that x=n^k according\n18:20 < wstein> to the docs.\n18:20 < wstein> But it doesn't.\n```\n\n\nPari's docs say this:\n\n```\n    ispower(x,{k},{&n}): true (1) if x is a k-th power, false (0) if not. If n is \n    given and a k-th root was computed in the process, put that in n. If k is \n    omitted, return the maximal k >= 2 such that x = n^k is a perfect power, or 0 \n    if no such k exist.\n```\n\n\nSo this is a bug in pari.  The short-term solution is to I think just factor that damned number at the end.  This obviously could be slow in general, but at least it will be right.  Plus add a note to the docs and post a bugreport upstream (but check latest svn pari first, since we use an ancient pari).  I've reported bugs in this ispower function in pari before, by the way, so it's a known offender. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4777\n\n",
    "created_at": "2008-12-13T02:31:36Z",
    "labels": [
        "basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Sage is_prime_power is seriously buggy, because pari's ispower is BROKEN",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4777",
    "user": "was"
}
```
Assignee: somebody


```
18:18 < wstein> sage: n = 
3089265681159475043336839581081873360674602365963130114355701114591322241990483812812582393906477998611814245513881
18:18 < wstein> sage: factor(n)
18:18 < wstein> 150607571^14
18:18 < wstein> sage: sage.rings.arith.is_prime_power(n)False
18:18 < wstein> sage: n.is_prime_power()
18:18 < wstein> False
18:18 < wstein> sage: is_prime(150607571)
18:18 < wstein> True
18:19 < wstein> Yep, Sage's is_prime_power function is just plain wrong.
18:19 < wstein> Great.
18:19 < wstein> I wrote that, I think... :-(
18:20 < wstein> sage: k = pari(n); k.ispower()
18:20 < wstein> (2, 1757630701017558763141032341047742794506161527817537960891)
18:20 < wstein> Oh, it's a bug in pari, actually.
18:20 < wstein> Since pari's ispower is guaranteed to give the maximal k such that x=n^k according
18:20 < wstein> to the docs.
18:20 < wstein> But it doesn't.
```


Pari's docs say this:

```
    ispower(x,{k},{&n}): true (1) if x is a k-th power, false (0) if not. If n is 
    given and a k-th root was computed in the process, put that in n. If k is 
    omitted, return the maximal k >= 2 such that x = n^k is a perfect power, or 0 
    if no such k exist.
```


So this is a bug in pari.  The short-term solution is to I think just factor that damned number at the end.  This obviously could be slow in general, but at least it will be right.  Plus add a note to the docs and post a bugreport upstream (but check latest svn pari first, since we use an ancient pari).  I've reported bugs in this ispower function in pari before, by the way, so it's a known offender. 

Issue created by migration from https://trac.sagemath.org/ticket/4777





---

archive/issue_comments_036200.json:
```json
{
    "body": "BEFORE patch:\n\n```\nteragon-2:~ wstein$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: n = 150607571^14\nsage: n.is_prime_power()\nFalse\n```\n\n| Sage Version 3.2.1, Release Date: 2008-12-01                       |\n| Type notebook() for the GUI, and license() for information.        |\nAFTER patch:\n\n```\nsage: n = 150607571^14\nsage: n.is_prime_power()\nTrue\n```\n\n\nAnd I'm making this a blocker, since it is a situation where one can silently get very wrong answers.",
    "created_at": "2008-12-13T02:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4777#issuecomment-36200",
    "user": "was"
}
```

BEFORE patch:

```
teragon-2:~ wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: n = 150607571^14
sage: n.is_prime_power()
False
```

| Sage Version 3.2.1, Release Date: 2008-12-01                       |
| Type notebook() for the GUI, and license() for information.        |
AFTER patch:

```
sage: n = 150607571^14
sage: n.is_prime_power()
True
```


And I'm making this a blocker, since it is a situation where one can silently get very wrong answers.



---

archive/issue_comments_036201.json:
```json
{
    "body": "Attachment [trac_4777.patch](tarball://root/attachments/some-uuid/ticket4777/trac_4777.patch) by was created at 2008-12-13 02:41:24",
    "created_at": "2008-12-13T02:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4777#issuecomment-36201",
    "user": "was"
}
```

Attachment [trac_4777.patch](tarball://root/attachments/some-uuid/ticket4777/trac_4777.patch) by was created at 2008-12-13 02:41:24



---

archive/issue_comments_036202.json:
```json
{
    "body": "In the line `See trac #4777`, you should put a backslash before the #.",
    "created_at": "2008-12-13T04:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4777#issuecomment-36202",
    "user": "jhpalmieri"
}
```

In the line `See trac #4777`, you should put a backslash before the #.



---

archive/issue_comments_036203.json:
```json
{
    "body": "Patch looks good, except for the missing backslash noted by John Palmieri above. Beyond that, we just need to make sure that someone makes a note to test this in pari 2.4.2, and send a bug report upstream if it's really broken ...",
    "created_at": "2008-12-13T09:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4777#issuecomment-36203",
    "user": "craigcitro"
}
```

Patch looks good, except for the missing backslash noted by John Palmieri above. Beyond that, we just need to make sure that someone makes a note to test this in pari 2.4.2, and send a bug report upstream if it's really broken ...



---

archive/issue_comments_036204.json:
```json
{
    "body": "I am taking care of the problem pointed out by John.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-13T09:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4777#issuecomment-36204",
    "user": "mabshoff"
}
```

I am taking care of the problem pointed out by John.

Cheers,

Michael



---

archive/issue_comments_036205.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-13T10:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4777#issuecomment-36205",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha2



---

archive/issue_comments_036206.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-13T10:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4777#issuecomment-36206",
    "user": "mabshoff"
}
```

Resolution: fixed
