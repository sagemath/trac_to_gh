# Issue 358: padic_height_pairing_matrix computes too many heights

archive/issues_000358.json:
```json
{
    "body": "Assignee: was\n\nThe function `padic_height_pairing_matrix()` is a bit lazy. It should do less work along the diagonal. e.g. for rank 2, if the generators are P and Q, it computes h(P), h(Q), h(P+Q), h(P+P), h(Q+Q). Clearly the last two are silly.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/358\n\n",
    "created_at": "2007-04-25T22:39:16Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "enhancement"
    ],
    "title": "padic_height_pairing_matrix computes too many heights",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/358",
    "user": "dmharvey"
}
```
Assignee: was

The function `padic_height_pairing_matrix()` is a bit lazy. It should do less work along the diagonal. e.g. for rank 2, if the generators are P and Q, it computes h(P), h(Q), h(P+Q), h(P+P), h(Q+Q). Clearly the last two are silly.


Issue created by migration from https://trac.sagemath.org/ticket/358





---

archive/issue_comments_001726.json:
```json
{
    "body": "Attachment [trac_358.patch](tarball://root/attachments/some-uuid/ticket358/trac_358.patch) by cremona created at 2008-04-06 14:56:05\n\nDone.  Patch based on 3.0.alpha1",
    "created_at": "2008-04-06T14:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/358#issuecomment-1726",
    "user": "cremona"
}
```

Attachment [trac_358.patch](tarball://root/attachments/some-uuid/ticket358/trac_358.patch) by cremona created at 2008-04-06 14:56:05

Done.  Patch based on 3.0.alpha1



---

archive/issue_comments_001727.json:
```json
{
    "body": "Actually, it looks like someone has already fixed this ticket a while ago. John, I don't think your patch actually does anything significantly different, it just looks like a code rearrangement? (Although I do prefer the way you have written it to what was there before.)",
    "created_at": "2008-04-06T15:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/358#issuecomment-1727",
    "user": "dmharvey"
}
```

Actually, it looks like someone has already fixed this ticket a while ago. John, I don't think your patch actually does anything significantly different, it just looks like a code rearrangement? (Although I do prefer the way you have written it to what was there before.)



---

archive/issue_comments_001728.json:
```json
{
    "body": "Replying to [comment:4 dmharvey]:\n> Actually, it looks like someone has already fixed this ticket a while ago. John, I don't think your patch actually does anything significantly different, it just looks like a code rearrangement? (Although I do prefer the way you have written it to what was there before.)\n\nOK, you are right.  I thought it was pointless to store the heights in a separate array and then put them in the matrix diagonal later.  So you can decide whether or not this patch should get used, and either way the ticket can be closed!",
    "created_at": "2008-04-06T16:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/358#issuecomment-1728",
    "user": "cremona"
}
```

Replying to [comment:4 dmharvey]:
> Actually, it looks like someone has already fixed this ticket a while ago. John, I don't think your patch actually does anything significantly different, it just looks like a code rearrangement? (Although I do prefer the way you have written it to what was there before.)

OK, you are right.  I thought it was pointless to store the heights in a separate array and then put them in the matrix diagonal later.  So you can decide whether or not this patch should get used, and either way the ticket can be closed!



---

archive/issue_comments_001729.json:
```json
{
    "body": "I agree. Passes tests for me, so let's merge it.",
    "created_at": "2008-04-06T16:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/358#issuecomment-1729",
    "user": "dmharvey"
}
```

I agree. Passes tests for me, so let's merge it.



---

archive/issue_comments_001730.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T17:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/358#issuecomment-1730",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_comments_001731.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T17:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/358#issuecomment-1731",
    "user": "mabshoff"
}
```

Resolution: fixed
