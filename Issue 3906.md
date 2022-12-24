# Issue 3906: symbolic plotting bug

archive/issues_003906.json:
```json
{
    "body": "Assignee: gfurnish\n\nNo response on sage-support, so I deem this a bug, not a feature:\n\n\n```\nsage: plot(sin,0,pi)\n<plots fine>\nsage: plot(2*sin,0,pi)\n<boom>\n\nAlthough I suppose we should always include variables -\n\nsage: plot(2*sin(x),0,pi)\n<plots fine>\n\n- for consistency's (and ease of use's) sake both of the above should\nwork. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3906\n\n",
    "created_at": "2008-08-20T01:16:20Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "symbolic plotting bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3906",
    "user": "kcrisman"
}
```
Assignee: gfurnish

No response on sage-support, so I deem this a bug, not a feature:


```
sage: plot(sin,0,pi)
<plots fine>
sage: plot(2*sin,0,pi)
<boom>

Although I suppose we should always include variables -

sage: plot(2*sin(x),0,pi)
<plots fine>

- for consistency's (and ease of use's) sake both of the above should
work. 
```


Issue created by migration from https://trac.sagemath.org/ticket/3906





---

archive/issue_comments_027946.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-09-05T19:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3906#issuecomment-27946",
    "user": "rlm"
}
```

Resolution: duplicate



---

archive/issue_comments_027947.json:
```json
{
    "body": "Attachment [trac_3906.patch](tarball://root/attachments/some-uuid/ticket3906/trac_3906.patch) by rlm created at 2008-09-05 19:41:46\n\nThis patch is found also at #3907.",
    "created_at": "2008-09-05T19:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3906#issuecomment-27947",
    "user": "rlm"
}
```

Attachment [trac_3906.patch](tarball://root/attachments/some-uuid/ticket3906/trac_3906.patch) by rlm created at 2008-09-05 19:41:46

This patch is found also at #3907.
