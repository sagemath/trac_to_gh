# Issue 630: [with patch] mhansen's big combinatorics update

archive/issues_000630.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nIncludes C interface for symmetrica.\n\nIssue created by migration from https://trac.sagemath.org/ticket/630\n\n",
    "closed_at": "2007-09-20T23:16:43Z",
    "created_at": "2007-09-09T19:18:16Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "[with patch] mhansen's big combinatorics update",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/630",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

CC:  sage-combinat

Includes C interface for symmetrica.

Issue created by migration from https://trac.sagemath.org/ticket/630





---

archive/issue_comments_003230.json:
```json
{
    "body": "Attachment [combinat.hg](tarball://root/attachments/some-uuid/ticket630/combinat.hg) by @mwhansen created at 2007-09-20 20:48:10",
    "created_at": "2007-09-20T20:48:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/630#issuecomment-3230",
    "user": "https://github.com/mwhansen"
}
```

Attachment [combinat.hg](tarball://root/attachments/some-uuid/ticket630/combinat.hg) by @mwhansen created at 2007-09-20 20:48:10



---

archive/issue_comments_003231.json:
```json
{
    "body": "Bundle attached.",
    "created_at": "2007-09-20T20:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/630#issuecomment-3231",
    "user": "https://github.com/mwhansen"
}
```

Bundle attached.



---

archive/issue_comments_003232.json:
```json
{
    "body": "Attachment [tut.patch](tarball://root/attachments/some-uuid/ticket630/tut.patch) by @williamstein created at 2007-09-20 23:03:47\n\nNOTE:\n\nThe old partitions function (copied below), was vastly faster than the new\nPartitions(n).list() for n=30...\n\n```\ndef partitions(n):\n    r\"\"\"\n    Generator of all the partitions of the integer $n$.\n\n    INPUT:\n        n -- int\n\n    To compute the number of partitions of $n$ use\n    \\code{number_of_partitions(n)}.\n\n    EXAMPLES:\n        sage.: partitions(3)\n        <generator object at 0xab3b3eac>\n        sage: list(partitions(3))\n        [(1, 1, 1), (1, 2), (3,)]\n\n\n    AUTHOR: Adapted from David Eppstein, Jan Van lent, George Yoshida;\n    Python Cookbook 2, Recipe 19.16.\n    \"\"\"\n    n == ZZ(n)\n    # base case of the recursion: zero is the sum of the empty tuple\n    if n == 0:\n        yield ( )\n        return\n    # modify the partitions of n-1 to form the partitions of n\n    for p in partitions(n-1):\n        yield (1,) + p\n        if p and (len(p) < 2 or p[1] > p[0]):\n            yield (p[0] + 1,) + p[1:]\nsage: time v=list(partitions(30))\nCPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s\n\n\n--\n[15:59] <william_stein> mhansen -- interestingly the *old* partitions function is way faster than your new one...??\n[15:59] <william_stein> old:\n[15:59] <william_stein> sage: time v=list(partitions(30))\n[15:59] <william_stein> CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s\n[15:59] <millster> aha\n[15:59] <william_stein> new:\n[15:59] <william_stein> sage: time v=Partitions(30).list()\n[15:59] <william_stein> CPU times: user 0.46 s, sys: 0.02 s, total: 0.48 s\n```",
    "created_at": "2007-09-20T23:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/630#issuecomment-3232",
    "user": "https://github.com/williamstein"
}
```

Attachment [tut.patch](tarball://root/attachments/some-uuid/ticket630/tut.patch) by @williamstein created at 2007-09-20 23:03:47

NOTE:

The old partitions function (copied below), was vastly faster than the new
Partitions(n).list() for n=30...

```
def partitions(n):
    r"""
    Generator of all the partitions of the integer $n$.

    INPUT:
        n -- int

    To compute the number of partitions of $n$ use
    \code{number_of_partitions(n)}.

    EXAMPLES:
        sage.: partitions(3)
        <generator object at 0xab3b3eac>
        sage: list(partitions(3))
        [(1, 1, 1), (1, 2), (3,)]


    AUTHOR: Adapted from David Eppstein, Jan Van lent, George Yoshida;
    Python Cookbook 2, Recipe 19.16.
    """
    n == ZZ(n)
    # base case of the recursion: zero is the sum of the empty tuple
    if n == 0:
        yield ( )
        return
    # modify the partitions of n-1 to form the partitions of n
    for p in partitions(n-1):
        yield (1,) + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield (p[0] + 1,) + p[1:]
sage: time v=list(partitions(30))
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s


--
[15:59] <william_stein> mhansen -- interestingly the *old* partitions function is way faster than your new one...??
[15:59] <william_stein> old:
[15:59] <william_stein> sage: time v=list(partitions(30))
[15:59] <william_stein> CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
[15:59] <millster> aha
[15:59] <william_stein> new:
[15:59] <william_stein> sage: time v=Partitions(30).list()
[15:59] <william_stein> CPU times: user 0.46 s, sys: 0.02 s, total: 0.48 s
```



---

archive/issue_events_001679.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-20T23:16:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/630",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/630#event-1679"
}
```



---

archive/issue_comments_003233.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-20T23:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/630#issuecomment-3233",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_003234.json:
```json
{
    "body": "Attachment [combinat.patch](tarball://root/attachments/some-uuid/ticket630/combinat.patch) by @mwhansen created at 2007-09-21 00:05:12",
    "created_at": "2007-09-21T00:05:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/630#issuecomment-3234",
    "user": "https://github.com/mwhansen"
}
```

Attachment [combinat.patch](tarball://root/attachments/some-uuid/ticket630/combinat.patch) by @mwhansen created at 2007-09-21 00:05:12



---

archive/issue_comments_003235.json:
```json
{
    "body": "Attachment [combinat2.patch](tarball://root/attachments/some-uuid/ticket630/combinat2.patch) by @nthiery created at 2009-04-14 02:22:54",
    "created_at": "2009-04-14T02:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/630#issuecomment-3235",
    "user": "https://github.com/nthiery"
}
```

Attachment [combinat2.patch](tarball://root/attachments/some-uuid/ticket630/combinat2.patch) by @nthiery created at 2009-04-14 02:22:54
