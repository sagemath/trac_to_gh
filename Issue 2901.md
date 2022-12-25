# Issue 2901: rewrite load_session and save_session to use much better modern techniques (in particular merge the notebook and non-notebook implementations)

archive/issues_002901.json:
```json
{
    "body": "Assignee: cwitty\n\nBasically, I know a lot more about how to write Python/Cython code than I used to, so i can write these functions in a way that is (1) vastly better, and (2) will be easily doctested, and (3) work in (almost) the same way in the notebook or command line. \n\nThis depends on the patch up at #2883.  #2883 should be applied then the code attached to this patch, once this patch is accepted.\n\nI've separated this out from #2883, since #2883 really *must* get applied, and the code here should be, but it's really a separate issue, and more nontrivial.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2901\n\n",
    "created_at": "2008-04-13T01:42:04Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "rewrite load_session and save_session to use much better modern techniques (in particular merge the notebook and non-notebook implementations)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2901",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

Basically, I know a lot more about how to write Python/Cython code than I used to, so i can write these functions in a way that is (1) vastly better, and (2) will be easily doctested, and (3) work in (almost) the same way in the notebook or command line. 

This depends on the patch up at #2883.  #2883 should be applied then the code attached to this patch, once this patch is accepted.

I've separated this out from #2883, since #2883 really *must* get applied, and the code here should be, but it's really a separate issue, and more nontrivial.

Issue created by migration from https://trac.sagemath.org/ticket/2901





---

archive/issue_comments_019952.json:
```json
{
    "body": "Attachment [sage-2901.patch](tarball://root/attachments/some-uuid/ticket2901/sage-2901.patch) by @williamstein created at 2008-04-13 04:00:56",
    "created_at": "2008-04-13T04:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2901#issuecomment-19952",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2901.patch](tarball://root/attachments/some-uuid/ticket2901/sage-2901.patch) by @williamstein created at 2008-04-13 04:00:56



---

archive/issue_comments_019953.json:
```json
{
    "body": "Patch is up.   This basically replaces a bunch of terrifying ugly undocumented miserable scary code (umh, that I wrote) by nice modern well-documented code.",
    "created_at": "2008-04-13T04:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2901#issuecomment-19953",
    "user": "https://github.com/williamstein"
}
```

Patch is up.   This basically replaces a bunch of terrifying ugly undocumented miserable scary code (umh, that I wrote) by nice modern well-documented code.



---

archive/issue_comments_019954.json:
```json
{
    "body": "I am not enough of a notebook user to test this thoroughly, but the code is good and the documentation is good.  I say apply immediately!\n\nOne quibble: could the module comment make it clear why this is in Cython and not Python?  I think there's a locals() trick at play, but it should be made clear none-the-less.",
    "created_at": "2008-04-13T04:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2901#issuecomment-19954",
    "user": "https://github.com/ncalexan"
}
```

I am not enough of a notebook user to test this thoroughly, but the code is good and the documentation is good.  I say apply immediately!

One quibble: could the module comment make it clear why this is in Cython and not Python?  I think there's a locals() trick at play, but it should be made clear none-the-less.



---

archive/issue_comments_019955.json:
```json
{
    "body": "Ok, I tracked down the issue for the reject of hunk two in worksheet.py. It expects:\n\n```\nif t.startswith('load_session'):\n    filename = self.hunt_file(filename)\n```\nBut the file contains:\n\n```\nfilename = self.hunt_file(filename)\n```\nI am deleting hunk two as is and then apply the rest of the patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T16:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2901#issuecomment-19955",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, I tracked down the issue for the reject of hunk two in worksheet.py. It expects:

```
if t.startswith('load_session'):
    filename = self.hunt_file(filename)
```
But the file contains:

```
filename = self.hunt_file(filename)
```
I am deleting hunk two as is and then apply the rest of the patch.

Cheers,

Michael



---

archive/issue_comments_019956.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-13T16:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2901#issuecomment-19956",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha5



---

archive/issue_events_006641.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-13T16:35:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2901",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2901#event-6641"
}
```



---

archive/issue_comments_019957.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-13T16:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2901#issuecomment-19957",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
