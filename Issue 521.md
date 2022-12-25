# Issue 521: put a doctest for every single function schemes/elliptic_curves/monsky_washnitzer.py

archive/issues_000521.json:
```json
{
    "body": "Assignee: dmharvey\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/521\n\n",
    "created_at": "2007-08-29T22:22:07Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "put a doctest for every single function schemes/elliptic_curves/monsky_washnitzer.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/521",
    "user": "https://github.com/williamstein"
}
```
Assignee: dmharvey



Issue created by migration from https://trac.sagemath.org/ticket/521





---

archive/issue_comments_002628.json:
```json
{
    "body": "\n```\nbsd:sage-2.8.13.rc0 mabshoff$ ./sage -coverage  devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py\n----------------------------------------------------------------------\ndevel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py: 5% (6 of 107)\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-11-20T14:13:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/521#issuecomment-2628",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```


```
bsd:sage-2.8.13.rc0 mabshoff$ ./sage -coverage  devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py
----------------------------------------------------------------------
devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py: 5% (6 of 107)
```


Cheers,

Michael



---

archive/issue_comments_002629.json:
```json
{
    "body": "While you are at it:\n\n```\nERROR: Please define a s == loads(dumps(s)) doctest.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-12-26T02:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/521#issuecomment-2629",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

While you are at it:

```
ERROR: Please define a s == loads(dumps(s)) doctest.
```


Cheers,

Michael



---

archive/issue_comments_002630.json:
```json
{
    "body": "Changing component from basic arithmetic to algebraic geometry.",
    "created_at": "2008-01-24T23:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/521#issuecomment-2630",
    "user": "https://github.com/aghitza"
}
```

Changing component from basic arithmetic to algebraic geometry.



---

archive/issue_comments_002631.json:
```json
{
    "body": "Attachment [521.patch](tarball://root/attachments/some-uuid/ticket521/521.patch) by dmharvey created at 2008-01-28 01:32:20",
    "created_at": "2008-01-28T01:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/521#issuecomment-2631",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [521.patch](tarball://root/attachments/some-uuid/ticket521/521.patch) by dmharvey created at 2008-01-28 01:32:20



---

archive/issue_comments_002632.json:
```json
{
    "body": "I got started on writing doctests, see 521.patch. I'm not going to finish now, but still worth merging I guess. (Also there's a lot of code in there that robert wrote, which I'm not comfortable doctesting.)\n\nThe patch also makes some minor optimisations.",
    "created_at": "2008-01-28T01:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/521#issuecomment-2632",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I got started on writing doctests, see 521.patch. I'm not going to finish now, but still worth merging I guess. (Also there's a lot of code in there that robert wrote, which I'm not comfortable doctesting.)

The patch also makes some minor optimisations.



---

archive/issue_comments_002633.json:
```json
{
    "body": "I am getting some rejects with the current patch against 2.10.2.alpha0:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/devel/sage$ patch -p1 --dry-run < 521.patch\\?format\\=raw\npatching file sage/schemes/elliptic_curves/monsky_washnitzer.py\npatching file sage/schemes/elliptic_curves/monsky_washnitzer.py\nHunk #1 succeeded at 163 with fuzz 1 (offset -18 lines).\nHunk #2 succeeded at 200 (offset -52 lines).\nHunk #3 succeeded at 240 (offset -52 lines).\nHunk #4 succeeded at 267 (offset -52 lines).\nHunk #5 succeeded at 282 (offset -52 lines).\nHunk #6 succeeded at 311 (offset -52 lines).\nHunk #7 succeeded at 362 (offset -52 lines).\nHunk #8 succeeded at 381 (offset -52 lines).\nHunk #9 succeeded at 399 (offset -52 lines).\npatching file sage/schemes/elliptic_curves/monsky_washnitzer.py\nHunk #1 FAILED at 380.\nHunk #2 succeeded at 300 (offset -89 lines).\nHunk #3 succeeded at 317 (offset -89 lines).\nHunk #4 succeeded at 334 (offset -89 lines).\nHunk #5 succeeded at 362 with fuzz 1 (offset -89 lines).\nHunk #6 FAILED at 383.\nHunk #7 succeeded at 476 (offset -90 lines).\n2 out of 7 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/monsky_washnitzer.py.rej\n```\n\nHopefully this can be easily fixed since we really ought to merge this patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T22:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/521#issuecomment-2633",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am getting some rejects with the current patch against 2.10.2.alpha0:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/devel/sage$ patch -p1 --dry-run < 521.patch\?format\=raw
patching file sage/schemes/elliptic_curves/monsky_washnitzer.py
patching file sage/schemes/elliptic_curves/monsky_washnitzer.py
Hunk #1 succeeded at 163 with fuzz 1 (offset -18 lines).
Hunk #2 succeeded at 200 (offset -52 lines).
Hunk #3 succeeded at 240 (offset -52 lines).
Hunk #4 succeeded at 267 (offset -52 lines).
Hunk #5 succeeded at 282 (offset -52 lines).
Hunk #6 succeeded at 311 (offset -52 lines).
Hunk #7 succeeded at 362 (offset -52 lines).
Hunk #8 succeeded at 381 (offset -52 lines).
Hunk #9 succeeded at 399 (offset -52 lines).
patching file sage/schemes/elliptic_curves/monsky_washnitzer.py
Hunk #1 FAILED at 380.
Hunk #2 succeeded at 300 (offset -89 lines).
Hunk #3 succeeded at 317 (offset -89 lines).
Hunk #4 succeeded at 334 (offset -89 lines).
Hunk #5 succeeded at 362 with fuzz 1 (offset -89 lines).
Hunk #6 FAILED at 383.
Hunk #7 succeeded at 476 (offset -90 lines).
2 out of 7 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/monsky_washnitzer.py.rej
```

Hopefully this can be easily fixed since we really ought to merge this patch.

Cheers,

Michael



---

archive/issue_comments_002634.json:
```json
{
    "body": "I will take a look. Should have a new patch by tomorrow.",
    "created_at": "2008-02-15T23:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/521#issuecomment-2634",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I will take a look. Should have a new patch by tomorrow.



---

archive/issue_comments_002635.json:
```json
{
    "body": "Ummm this is weird.\n\nAll of the following on 2.10.2.alpha0:\n\nIf I try patching using the command you used above, I get the same failure.\n\nHowever, if I'm in the directory devel/sage/sage/schemes/elliptic_curves, and I just do `hg import 521.patch` then it works fine.",
    "created_at": "2008-02-16T02:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/521#issuecomment-2635",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Ummm this is weird.

All of the following on 2.10.2.alpha0:

If I try patching using the command you used above, I get the same failure.

However, if I'm in the directory devel/sage/sage/schemes/elliptic_curves, and I just do `hg import 521.patch` then it works fine.



---

archive/issue_comments_002636.json:
```json
{
    "body": "patch rebased on sage-2.10.2.alpha0",
    "created_at": "2008-02-17T02:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/521#issuecomment-2636",
    "user": "https://github.com/aghitza"
}
```

patch rebased on sage-2.10.2.alpha0



---

archive/issue_comments_002637.json:
```json
{
    "body": "Attachment [521_alt.patch](tarball://root/attachments/some-uuid/ticket521/521_alt.patch) by @aghitza created at 2008-02-17 16:56:00",
    "created_at": "2008-02-17T16:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/521#issuecomment-2637",
    "user": "https://github.com/aghitza"
}
```

Attachment [521_alt.patch](tarball://root/attachments/some-uuid/ticket521/521_alt.patch) by @aghitza created at 2008-02-17 16:56:00



---

archive/issue_comments_002638.json:
```json
{
    "body": "Ok, Alex's rebase of David's patch raises the score to:\n\n```\ndevel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py: 23% (25 of 107)\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T17:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/521#issuecomment-2638",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, Alex's rebase of David's patch raises the score to:

```
devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py: 23% (25 of 107)
```


Cheers,

Michael



---

archive/issue_comments_002639.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1. Even though the coverage is \"only\" up to 23% I am closing this. Please open another ticket if you come up with another patch to raise the doctest coverage.",
    "created_at": "2008-02-17T17:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/521#issuecomment-2639",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1. Even though the coverage is "only" up to 23% I am closing this. Please open another ticket if you come up with another patch to raise the doctest coverage.



---

archive/issue_events_000560.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-17T17:12:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/521#event-560"
}
```



---

archive/issue_comments_002640.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T17:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/521#issuecomment-2640",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
