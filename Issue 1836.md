# Issue 1836: [with patch] return reduced Groebner bases by default

archive/issues_001836.json:
```json
{
    "body": "Assignee: @malb\n\n... to avoid ambiguousness\n\nIssue created by migration from https://trac.sagemath.org/ticket/1836\n\n",
    "created_at": "2008-01-18T19:28:42Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch] return reduced Groebner bases by default",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1836",
    "user": "@malb"
}
```
Assignee: @malb

... to avoid ambiguousness

Issue created by migration from https://trac.sagemath.org/ticket/1836





---

archive/issue_comments_011620.json:
```json
{
    "body": "Attachment [redSB-doc.patch](tarball://root/attachments/some-uuid/ticket1836/redSB-doc.patch) by @malb created at 2008-01-18 19:29:29",
    "created_at": "2008-01-18T19:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1836#issuecomment-11620",
    "user": "@malb"
}
```

Attachment [redSB-doc.patch](tarball://root/attachments/some-uuid/ticket1836/redSB-doc.patch) by @malb created at 2008-01-18 19:29:29



---

archive/issue_comments_011621.json:
```json
{
    "body": "There are an awful lot of places that Groebner bases are computed.  (complete_prime_decomposition, etc).  I'd really like to guarantee that *all* such bases are reduced.  Is that unreasonable?",
    "created_at": "2008-01-20T03:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1836#issuecomment-11621",
    "user": "@ncalexan"
}
```

There are an awful lot of places that Groebner bases are computed.  (complete_prime_decomposition, etc).  I'd really like to guarantee that *all* such bases are reduced.  Is that unreasonable?



---

archive/issue_comments_011622.json:
```json
{
    "body": "updated patch which uses Python techniques to implement reduction of Groebner bases, and forces all GB calculations to be reduced",
    "created_at": "2008-01-20T22:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1836#issuecomment-11622",
    "user": "@malb"
}
```

updated patch which uses Python techniques to implement reduction of Groebner bases, and forces all GB calculations to be reduced



---

archive/issue_comments_011623.json:
```json
{
    "body": "Attachment [redSB-sage.patch](tarball://root/attachments/some-uuid/ticket1836/redSB-sage.patch) by @malb created at 2008-01-20 22:28:12\n\nReplying to [comment:1 ncalexan]:\n> There are an awful lot of places that Groebner bases are computed.  (complete_prime_decomposition, etc).  I'd really like to guarantee that *all* such bases are reduced.  Is that unreasonable?\n\nThe updated patch is supposed to implement that.",
    "created_at": "2008-01-20T22:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1836#issuecomment-11623",
    "user": "@malb"
}
```

Attachment [redSB-sage.patch](tarball://root/attachments/some-uuid/ticket1836/redSB-sage.patch) by @malb created at 2008-01-20 22:28:12

Replying to [comment:1 ncalexan]:
> There are an awful lot of places that Groebner bases are computed.  (complete_prime_decomposition, etc).  I'd really like to guarantee that *all* such bases are reduced.  Is that unreasonable?

The updated patch is supposed to implement that.



---

archive/issue_comments_011624.json:
```json
{
    "body": "Patch looks good to me. I think that all of Nick's concerns have been addressed.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-22T00:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1836#issuecomment-11624",
    "user": "mabshoff"
}
```

Patch looks good to me. I think that all of Nick's concerns have been addressed.

Cheers,

Michael



---

archive/issue_comments_011625.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-22T00:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1836#issuecomment-11625",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011626.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-22T00:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1836#issuecomment-11626",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha1
