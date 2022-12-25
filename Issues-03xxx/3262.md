# Issue 3262: [with patch; needs work] interact selector breaks if there are too many options

archive/issues_003262.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: interact, notebook, editor_wstein\n\nWhen the lists of values of multiple selectors are too long, the output is truncated, causing nasty bugs.  Here's an example:\n\n```\n@interact\ndef test(q1 = selector(range(100)), q2 = selector(range(1000)+['None'], default ='None'), q3 = selector(['hi']+range(1000)+['None'], default=127)):\n    show([q1,q2,q3])\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3262\n\n",
    "closed_at": "2008-08-30T02:15:26Z",
    "created_at": "2008-05-20T21:07:09Z",
    "labels": [
        "component: interact",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch; needs work] interact selector breaks if there are too many options",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3262",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: somebody

Keywords: interact, notebook, editor_wstein

When the lists of values of multiple selectors are too long, the output is truncated, causing nasty bugs.  Here's an example:

```
@interact
def test(q1 = selector(range(100)), q2 = selector(range(1000)+['None'], default ='None'), q3 = selector(['hi']+range(1000)+['None'], default=127)):
    show([q1,q2,q3])
```

Issue created by migration from https://trac.sagemath.org/ticket/3262





---

archive/issue_comments_022515.json:
```json
{
    "body": "only truncates if `@`interact is not input",
    "created_at": "2008-05-20T23:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22515",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

only truncates if `@`interact is not input



---

archive/issue_comments_022516.json:
```json
{
    "body": "Attachment [trac_3262_try1.patch](tarball://root/attachments/some-uuid/ticket3262/trac_3262_try1.patch) by mhampton created at 2008-05-20 23:39:29\n\nThis might be considered a hack: output is only truncated if \"`@`interact\" is not in a cell's input, which prevents mangling of long html/javascript output.",
    "created_at": "2008-05-20T23:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22516",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_3262_try1.patch](tarball://root/attachments/some-uuid/ticket3262/trac_3262_try1.patch) by mhampton created at 2008-05-20 23:39:29

This might be considered a hack: output is only truncated if "`@`interact" is not in a cell's input, which prevents mangling of long html/javascript output.



---

archive/issue_comments_022517.json:
```json
{
    "body": "REFEREE REPORT:\n\n1. good idea\n\n2. This line\n\n```\nif self.__in.find('@interact') == -1: \n```\nwould read better as\n\n```\nif '@interact' not in self.__in\n```\n\n3. There should be a big comment right before or next to the loop that\nwe are being *VERY HACKISH* doing this, since e.g. it will cause us to\nthink that\n\n```\n print \"@interact\"\n```\nis an interact cell, even though it isn't, and this could must be rewritten\nto more intelligently determine whether a cell is an interact cell. \nACTUALLY, *much* better would be for you to just replace that if by\na cell to `self.is_interactive_cell()`, which I wrote, and which\ndoes things right(er).",
    "created_at": "2008-05-21T13:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22517",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_022518.json:
```json
{
    "body": "addressed review comments",
    "created_at": "2008-05-21T16:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22518",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

addressed review comments



---

archive/issue_comments_022519.json:
```json
{
    "body": "Attachment [trac_3262_try2.patch](tarball://root/attachments/some-uuid/ticket3262/trac_3262_try2.patch) by mhampton created at 2008-05-21 17:07:52\n\nThe new patch uses self.is_interactive_cell().  Someone just needs to double-check that this works and it can be merged.",
    "created_at": "2008-05-21T17:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22519",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_3262_try2.patch](tarball://root/attachments/some-uuid/ticket3262/trac_3262_try2.patch) by mhampton created at 2008-05-21 17:07:52

The new patch uses self.is_interactive_cell().  Someone just needs to double-check that this works and it can be merged.



---

archive/issue_comments_022520.json:
```json
{
    "body": "Changing keywords from \"interact, notebook\" to \"interact, notebook, editor_wstein\".",
    "created_at": "2008-06-15T21:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22520",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "interact, notebook" to "interact, notebook, editor_wstein".



---

archive/issue_comments_022521.json:
```json
{
    "body": "apply *only* this patch",
    "created_at": "2008-06-15T23:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22521",
    "user": "https://github.com/williamstein"
}
```

apply *only* this patch



---

archive/issue_comments_022522.json:
```json
{
    "body": "Attachment [sage-3262-final.patch](tarball://root/attachments/some-uuid/ticket3262/sage-3262-final.patch) by @williamstein created at 2008-06-15 23:09:39",
    "created_at": "2008-06-15T23:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22522",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3262-final.patch](tarball://root/attachments/some-uuid/ticket3262/sage-3262-final.patch) by @williamstein created at 2008-06-15 23:09:39



---

archive/issue_events_007342.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-23T11:06:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3262#event-7342"
}
```



---

archive/issue_events_007343.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-23T11:06:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3262#event-7343"
}
```



---

archive/issue_comments_022523.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T11:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22523",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022524.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T11:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22524",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha0



---

archive/issue_comments_022525.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-07-10T08:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22525",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_events_007344.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-07-10T08:04:04Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3262#event-7344"
}
```



---

archive/issue_events_007345.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-07-10T08:04:04Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "milestone": "sage-3.0.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3262#event-7345"
}
```



---

archive/issue_comments_022526.json:
```json
{
    "body": "1. The patch sage-3262-final.patch  I attached has nothing to do with this tick and simply introduces a bug that totally breaks using interact in sage.\n\n2. The patches by mhampton on this ticket never got applied in sage.\n\nso I'm re-opening this.",
    "created_at": "2008-07-10T08:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22526",
    "user": "https://github.com/williamstein"
}
```

1. The patch sage-3262-final.patch  I attached has nothing to do with this tick and simply introduces a bug that totally breaks using interact in sage.

2. The patches by mhampton on this ticket never got applied in sage.

so I'm re-opening this.



---

archive/issue_comments_022527.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-07-10T08:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22527",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_007346.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-07-10T08:04:04Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3262#event-7346"
}
```



---

archive/issue_comments_022528.json:
```json
{
    "body": "Attachment [sage-3262-undo.patch](tarball://root/attachments/some-uuid/ticket3262/sage-3262-undo.patch) by mabshoff created at 2008-07-11 04:12:34\n\nSo, for the record: which patch(es) should be applied in which order?\n\nCheers,\n\nMichael",
    "created_at": "2008-07-11T04:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22528",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-3262-undo.patch](tarball://root/attachments/some-uuid/ticket3262/sage-3262-undo.patch) by mabshoff created at 2008-07-11 04:12:34

So, for the record: which patch(es) should be applied in which order?

Cheers,

Michael



---

archive/issue_comments_022529.json:
```json
{
    "body": "Ok, sage-3262-undo.patch has already been applied to the official 3.0.4 repo.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-11T04:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22529",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, sage-3262-undo.patch has already been applied to the official 3.0.4 repo.

Cheers,

Michael



---

archive/issue_comments_022530.json:
```json
{
    "body": "This ticket is always showing up at report 11, so let's change the title :)\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T00:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22530",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This ticket is always showing up at report 11, so let's change the title :)

Cheers,

Michael



---

archive/issue_comments_022531.json:
```json
{
    "body": "Why is this still open? Since #3854, it shouldn't be a problem.",
    "created_at": "2008-08-30T02:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22531",
    "user": "https://github.com/itolkov"
}
```

Why is this still open? Since #3854, it shouldn't be a problem.



---

archive/issue_comments_022532.json:
```json
{
    "body": "Changing component from notebook to interact.",
    "created_at": "2008-08-30T02:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22532",
    "user": "https://github.com/itolkov"
}
```

Changing component from notebook to interact.



---

archive/issue_events_007347.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-30T02:15:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3262#event-7347"
}
```



---

archive/issue_comments_022533.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-30T02:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22533",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022534.json:
```json
{
    "body": "You are right. Fixed via #3854.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T02:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3262#issuecomment-22534",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

You are right. Fixed via #3854.

Cheers,

Michael
