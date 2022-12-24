# Issue 3262: interact selector breaks if there are too many options

archive/issues_003262.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: interact, notebook\n\nWhen the lists of values of multiple selectors are too long, the output is truncated, causing nasty bugs.  Here's an example:\n\n\n```\n@interact\ndef test(q1 = selector(range(100)), q2 = selector(range(1000)+['None'], default ='None'), q3 = selector(['hi']+range(1000)+['None'], default=127)):\n    show([q1,q2,q3])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3262\n\n",
    "created_at": "2008-05-20T21:07:09Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "interact selector breaks if there are too many options",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3262",
    "user": "mhampton"
}
```
Assignee: somebody

Keywords: interact, notebook

When the lists of values of multiple selectors are too long, the output is truncated, causing nasty bugs.  Here's an example:


```
@interact
def test(q1 = selector(range(100)), q2 = selector(range(1000)+['None'], default ='None'), q3 = selector(['hi']+range(1000)+['None'], default=127)):
    show([q1,q2,q3])
```


Issue created by migration from https://trac.sagemath.org/ticket/3262





---

archive/issue_comments_022562.json:
```json
{
    "body": "only truncates if `@`interact is not input",
    "created_at": "2008-05-20T23:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22562",
    "user": "mhampton"
}
```

only truncates if `@`interact is not input



---

archive/issue_comments_022563.json:
```json
{
    "body": "Attachment [trac_3262_try1.patch](tarball://root/attachments/some-uuid/ticket3262/trac_3262_try1.patch) by mhampton created at 2008-05-20 23:39:29\n\nThis might be considered a hack: output is only truncated if \"`@`interact\" is not in a cell's input, which prevents mangling of long html/javascript output.",
    "created_at": "2008-05-20T23:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22563",
    "user": "mhampton"
}
```

Attachment [trac_3262_try1.patch](tarball://root/attachments/some-uuid/ticket3262/trac_3262_try1.patch) by mhampton created at 2008-05-20 23:39:29

This might be considered a hack: output is only truncated if "`@`interact" is not in a cell's input, which prevents mangling of long html/javascript output.



---

archive/issue_comments_022564.json:
```json
{
    "body": "REFEREE REPORT:\n\n1. good idea\n\n2. This line\n\n```\nif self.__in.find('@interact') == -1: \n```\n\nwould read better as\n\n```\nif '@interact' not in self.__in\n```\n\n\n3. There should be a big comment right before or next to the loop that\nwe are being *VERY HACKISH* doing this, since e.g. it will cause us to\nthink that\n\n```\n print \"@interact\"\n```\n\nis an interact cell, even though it isn't, and this could must be rewritten\nto more intelligently determine whether a cell is an interact cell. \nACTUALLY, *much* better would be for you to just replace that if by\na cell to `self.is_interactive_cell()`, which I wrote, and which\ndoes things right(er).",
    "created_at": "2008-05-21T13:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22564",
    "user": "@williamstein"
}
```

REFEREE REPORT:

1. good idea

2. This line

```
if self.__in.find('@interact') == -1: 
```

would read better as

```
if '@interact' not in self.__in
```


3. There should be a big comment right before or next to the loop that
we are being *VERY HACKISH* doing this, since e.g. it will cause us to
think that

```
 print "@interact"
```

is an interact cell, even though it isn't, and this could must be rewritten
to more intelligently determine whether a cell is an interact cell. 
ACTUALLY, *much* better would be for you to just replace that if by
a cell to `self.is_interactive_cell()`, which I wrote, and which
does things right(er).



---

archive/issue_comments_022565.json:
```json
{
    "body": "addressed review comments",
    "created_at": "2008-05-21T16:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22565",
    "user": "mhampton"
}
```

addressed review comments



---

archive/issue_comments_022566.json:
```json
{
    "body": "Attachment [trac_3262_try2.patch](tarball://root/attachments/some-uuid/ticket3262/trac_3262_try2.patch) by mhampton created at 2008-05-21 17:07:52\n\nThe new patch uses self.is_interactive_cell().  Someone just needs to double-check that this works and it can be merged.",
    "created_at": "2008-05-21T17:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22566",
    "user": "mhampton"
}
```

Attachment [trac_3262_try2.patch](tarball://root/attachments/some-uuid/ticket3262/trac_3262_try2.patch) by mhampton created at 2008-05-21 17:07:52

The new patch uses self.is_interactive_cell().  Someone just needs to double-check that this works and it can be merged.



---

archive/issue_comments_022567.json:
```json
{
    "body": "Changing keywords from \"interact, notebook\" to \"interact, notebook, editor_wstein\".",
    "created_at": "2008-06-15T21:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22567",
    "user": "@craigcitro"
}
```

Changing keywords from "interact, notebook" to "interact, notebook, editor_wstein".



---

archive/issue_comments_022568.json:
```json
{
    "body": "apply *only* this patch",
    "created_at": "2008-06-15T23:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22568",
    "user": "@williamstein"
}
```

apply *only* this patch



---

archive/issue_comments_022569.json:
```json
{
    "body": "Attachment [sage-3262-final.patch](tarball://root/attachments/some-uuid/ticket3262/sage-3262-final.patch) by @williamstein created at 2008-06-15 23:09:39",
    "created_at": "2008-06-15T23:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22569",
    "user": "@williamstein"
}
```

Attachment [sage-3262-final.patch](tarball://root/attachments/some-uuid/ticket3262/sage-3262-final.patch) by @williamstein created at 2008-06-15 23:09:39



---

archive/issue_comments_022570.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T11:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22570",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022571.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T11:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22571",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha0



---

archive/issue_comments_022572.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-07-10T08:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22572",
    "user": "@williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_022573.json:
```json
{
    "body": "1. The patch sage-3262-final.patch  I attached has nothing to do with this tick and simply introduces a bug that totally breaks using interact in sage.\n\n2. The patches by mhampton on this ticket never got applied in sage.\n\nso I'm re-opening this.",
    "created_at": "2008-07-10T08:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22573",
    "user": "@williamstein"
}
```

1. The patch sage-3262-final.patch  I attached has nothing to do with this tick and simply introduces a bug that totally breaks using interact in sage.

2. The patches by mhampton on this ticket never got applied in sage.

so I'm re-opening this.



---

archive/issue_comments_022574.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-07-10T08:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22574",
    "user": "@williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_022575.json:
```json
{
    "body": "Attachment [sage-3262-undo.patch](tarball://root/attachments/some-uuid/ticket3262/sage-3262-undo.patch) by mabshoff created at 2008-07-11 04:12:34\n\nSo, for the record: which patch(es) should be applied in which order?\n\nCheers,\n\nMichael",
    "created_at": "2008-07-11T04:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22575",
    "user": "mabshoff"
}
```

Attachment [sage-3262-undo.patch](tarball://root/attachments/some-uuid/ticket3262/sage-3262-undo.patch) by mabshoff created at 2008-07-11 04:12:34

So, for the record: which patch(es) should be applied in which order?

Cheers,

Michael



---

archive/issue_comments_022576.json:
```json
{
    "body": "Ok, sage-3262-undo.patch has already been applied to the official 3.0.4 repo.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-11T04:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22576",
    "user": "mabshoff"
}
```

Ok, sage-3262-undo.patch has already been applied to the official 3.0.4 repo.

Cheers,

Michael



---

archive/issue_comments_022577.json:
```json
{
    "body": "This ticket is always showing up at report 11, so let's change the title :)\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T00:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22577",
    "user": "mabshoff"
}
```

This ticket is always showing up at report 11, so let's change the title :)

Cheers,

Michael



---

archive/issue_comments_022578.json:
```json
{
    "body": "Why is this still open? Since #3854, it shouldn't be a problem.",
    "created_at": "2008-08-30T02:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22578",
    "user": "@itolkov"
}
```

Why is this still open? Since #3854, it shouldn't be a problem.



---

archive/issue_comments_022579.json:
```json
{
    "body": "Changing component from notebook to interact.",
    "created_at": "2008-08-30T02:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22579",
    "user": "@itolkov"
}
```

Changing component from notebook to interact.



---

archive/issue_comments_022580.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-30T02:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22580",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022581.json:
```json
{
    "body": "You are right. Fixed via #3854.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T02:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22581",
    "user": "mabshoff"
}
```

You are right. Fixed via #3854.

Cheers,

Michael
