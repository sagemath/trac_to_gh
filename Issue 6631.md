# Issue 6631: speed up is_lyndon method for words

archive/issues_006631.json:
```json
{
    "body": "Assignee: Franco Saliola\n\nCC:  @seblabbe\n\nKeywords: words\n\nThe current implementation of the method `is_lyndon` is too slow\n\n```\nsage: c = words.ChristoffelWord(380447,34369)\nsage: c\nLower Christoffel word of slope 380447/34369 over Ordered Alphabet [0, 1]\nsage: c.length()\n414816\nsage: time c.is_lyndon()\nCPU times: user 84.15 s, sys: 0.17 s, total: 84.33 s\nWall time: 84.52 s\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6631\n\n",
    "created_at": "2009-07-26T22:04:26Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "speed up is_lyndon method for words",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6631",
    "user": "https://github.com/saliola"
}
```
Assignee: Franco Saliola

CC:  @seblabbe

Keywords: words

The current implementation of the method `is_lyndon` is too slow

```
sage: c = words.ChristoffelWord(380447,34369)
sage: c
Lower Christoffel word of slope 380447/34369 over Ordered Alphabet [0, 1]
sage: c.length()
414816
sage: time c.is_lyndon()
CPU times: user 84.15 s, sys: 0.17 s, total: 84.33 s
Wall time: 84.52 s
True
```


Issue created by migration from https://trac.sagemath.org/ticket/6631





---

archive/issue_comments_054239.json:
```json
{
    "body": "Attachment [trac_6631-is_lyndon.2.patch](tarball://root/attachments/some-uuid/ticket6631/trac_6631-is_lyndon.2.patch) by @saliola created at 2009-07-26 22:13:10\n\nDO NOT APPLY!",
    "created_at": "2009-07-26T22:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6631#issuecomment-54239",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_6631-is_lyndon.2.patch](tarball://root/attachments/some-uuid/ticket6631/trac_6631-is_lyndon.2.patch) by @saliola created at 2009-07-26 22:13:10

DO NOT APPLY!



---

archive/issue_comments_054240.json:
```json
{
    "body": "Don't apply `trac_6631-is_lyndon.2.patch`, it is a copy of the other, and should be deleted.",
    "created_at": "2009-07-26T22:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6631#issuecomment-54240",
    "user": "https://github.com/saliola"
}
```

Don't apply `trac_6631-is_lyndon.2.patch`, it is a copy of the other, and should be deleted.



---

archive/issue_comments_054241.json:
```json
{
    "body": "Here is the new timing: \n\n```\nsage: c = words.ChristoffelWord(380447,34369)\nsage: time c.is_lyndon()\nCPU times: user 1.15 s, sys: 0.00 s, total: 1.15 s\nWall time: 1.15 s\nTrue\n```\n\nThat's much better.",
    "created_at": "2009-07-26T22:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6631#issuecomment-54241",
    "user": "https://github.com/saliola"
}
```

Here is the new timing: 

```
sage: c = words.ChristoffelWord(380447,34369)
sage: time c.is_lyndon()
CPU times: user 1.15 s, sys: 0.00 s, total: 1.15 s
Wall time: 1.15 s
True
```

That's much better.



---

archive/issue_comments_054242.json:
```json
{
    "body": "The end of the loop can be simplified (there is no break statement in the loop, and we know that j==n at the end).\n\n\n```\nwhile j < n:\n    [...]\nelse:\n    return j - i == n\n```\n\n\ncould become:\n\n\n```\nwhile j < n:\n    [...]\nreturn i == 0\n```\n",
    "created_at": "2009-07-27T09:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6631#issuecomment-54242",
    "user": "https://github.com/videlec"
}
```

The end of the loop can be simplified (there is no break statement in the loop, and we know that j==n at the end).


```
while j < n:
    [...]
else:
    return j - i == n
```


could become:


```
while j < n:
    [...]
return i == 0
```




---

archive/issue_comments_054243.json:
```json
{
    "body": "Attachment [trac_6631-is_lyndon.patch](tarball://root/attachments/some-uuid/ticket6631/trac_6631-is_lyndon.patch) by @saliola created at 2009-07-27 10:02:08\n\ndepends on #6627;",
    "created_at": "2009-07-27T10:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6631#issuecomment-54243",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_6631-is_lyndon.patch](tarball://root/attachments/some-uuid/ticket6631/trac_6631-is_lyndon.patch) by @saliola created at 2009-07-27 10:02:08

depends on #6627;



---

archive/issue_comments_054244.json:
```json
{
    "body": "Replying to [comment:4 vdelecroix]:\n> The end of the loop can be simplified (there is no break statement in the loop, and we know that j==n at the end).\n> \n> {{{\n> while j < n:\n>     [...]\n> else:\n>     return j - i == n\n> }}}\n> \n> could become:\n> \n> {{{\n> while j < n:\n>     [...]\n> return i == 0\n> }}}\n\nDone in the new patch. (If you give this new patch a positive review, then change 'needs review' to 'positive review'.)",
    "created_at": "2009-07-27T10:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6631#issuecomment-54244",
    "user": "https://github.com/saliola"
}
```

Replying to [comment:4 vdelecroix]:
> The end of the loop can be simplified (there is no break statement in the loop, and we know that j==n at the end).
> 
> {{{
> while j < n:
>     [...]
> else:
>     return j - i == n
> }}}
> 
> could become:
> 
> {{{
> while j < n:
>     [...]
> return i == 0
> }}}

Done in the new patch. (If you give this new patch a positive review, then change 'needs review' to 'positive review'.)



---

archive/issue_comments_054245.json:
```json
{
    "body": "reviewer patch: fixes typo",
    "created_at": "2009-08-25T00:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6631#issuecomment-54245",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

reviewer patch: fixes typo



---

archive/issue_comments_054246.json:
```json
{
    "body": "Attachment [trac_6631-reviewer.patch](tarball://root/attachments/some-uuid/ticket6631/trac_6631-reviewer.patch) by mvngu created at 2009-08-25 00:27:34\n\nThe patch `trac_6631-reviewer.patch` fixes a typo introduced by `trac_6631-is_lyndon.patch`.",
    "created_at": "2009-08-25T00:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6631#issuecomment-54246",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6631-reviewer.patch](tarball://root/attachments/some-uuid/ticket6631/trac_6631-reviewer.patch) by mvngu created at 2009-08-25 00:27:34

The patch `trac_6631-reviewer.patch` fixes a typo introduced by `trac_6631-is_lyndon.patch`.



---

archive/issue_events_006870.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-08-25T00:43:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6631",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6631#event-6870"
}
```



---

archive/issue_comments_054247.json:
```json
{
    "body": "Merged:\n\n1. `trac_6631-is_lyndon.patch`\n2. `trac_6631-reviewer.patch`",
    "created_at": "2009-08-25T00:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6631#issuecomment-54247",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged:

1. `trac_6631-is_lyndon.patch`
2. `trac_6631-reviewer.patch`



---

archive/issue_comments_054248.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-25T00:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6631#issuecomment-54248",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
