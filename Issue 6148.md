# Issue 6148: functions involving ceil and floor are plotted incorrectly

archive/issues_006148.json:
```json
{
    "body": "In sage-4.0.rc1 if I define:\n\n\n\n```\nsage: r(u) = floor(u) - 2*floor(u/2)\nsage: s(u) = ceil(u) - 2*ceil(u/2)\n```\n\n\nThe following gives an incorrect plot:\n\n\n```\nsage: plot(r, (0, 10))\n```\n\n\nbut\n\n\n```\nsage: plot([r], (0, 10))\n```\n\n\ngives the correct plot.\n\nFor ceil it is even worse\n\n\n```\nsage: plot([s], (0, 10))\n```\n\n\ngives the correct plot, but\n\n\n```\nsage: plot(s, (0, 10))\n```\n\n\ngives a runtime error:\n\n\n```\nRuntimeError: maximum recursion depth exceeded\n```\n\n\nAll of this works correctly in sage-3.4.2, so it is probably\nrelated to the new symbolics.\n\nAdditionally\n\n\n```\nsage: r(0)\n-2*floor(0)\n```\n\n\nbut\n\n```\nsage: s(0)\n0\n```\n\n\nas expected.\n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6148\n\n",
    "created_at": "2009-05-28T12:27:21Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "functions involving ceil and floor are plotted incorrectly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6148",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```
In sage-4.0.rc1 if I define:



```
sage: r(u) = floor(u) - 2*floor(u/2)
sage: s(u) = ceil(u) - 2*ceil(u/2)
```


The following gives an incorrect plot:


```
sage: plot(r, (0, 10))
```


but


```
sage: plot([r], (0, 10))
```


gives the correct plot.

For ceil it is even worse


```
sage: plot([s], (0, 10))
```


gives the correct plot, but


```
sage: plot(s, (0, 10))
```


gives a runtime error:


```
RuntimeError: maximum recursion depth exceeded
```


All of this works correctly in sage-3.4.2, so it is probably
related to the new symbolics.

Additionally


```
sage: r(0)
-2*floor(0)
```


but

```
sage: s(0)
0
```


as expected.


```


Issue created by migration from https://trac.sagemath.org/ticket/6148





---

archive/issue_comments_048977.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-28T18:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6148#issuecomment-48977",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_048978.json:
```json
{
    "body": "Set assignee to @mwhansen.",
    "created_at": "2009-05-28T18:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6148#issuecomment-48978",
    "user": "https://github.com/mwhansen"
}
```

Set assignee to @mwhansen.



---

archive/issue_comments_048979.json:
```json
{
    "body": "Attachment [trac_6148.patch](tarball://root/attachments/some-uuid/ticket6148/trac_6148.patch) by @mwhansen created at 2009-05-28 18:27:03",
    "created_at": "2009-05-28T18:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6148#issuecomment-48979",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6148.patch](tarball://root/attachments/some-uuid/ticket6148/trac_6148.patch) by @mwhansen created at 2009-05-28 18:27:03



---

archive/issue_comments_048980.json:
```json
{
    "body": "This patch fixes the stated problems; both graphs are the same for me now.",
    "created_at": "2009-05-29T04:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6148#issuecomment-48980",
    "user": "https://github.com/jasongrout"
}
```

This patch fixes the stated problems; both graphs are the same for me now.



---

archive/issue_comments_048981.json:
```json
{
    "body": "I also read the patch and tried things and it looks fine to me.",
    "created_at": "2009-05-29T13:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6148#issuecomment-48981",
    "user": "https://github.com/williamstein"
}
```

I also read the patch and tried things and it looks fine to me.



---

archive/issue_comments_048982.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-29T17:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6148#issuecomment-48982",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_048983.json:
```json
{
    "body": "Merged in 4.0.rc2.",
    "created_at": "2009-05-29T17:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6148#issuecomment-48983",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.rc2.
