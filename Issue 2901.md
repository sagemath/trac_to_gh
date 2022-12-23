# Issue 2901: rewrite load_session and save_session to use much better modern techniques (in particular merge the notebook and non-notebook implementations)

archive/issues_002901.json:
```json
{
    "body": "Assignee: cwitty\n\nBasically, I know a lot more about how to write Python/Cython code than I used to, so i can write these functions in a way that is (1) vastly better, and (2) will be easily doctested, and (3) work in (almost) the same way in the notebook or command line. \n\nThis depends on the patch up at #2883.  #2883 should be applied then the code attached to this patch, once this patch is accepted.\n\nI've separated this out from #2883, since #2883 really *must* get applied, and the code here should be, but it's really a separate issue, and more nontrivial.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2901\n\n",
    "created_at": "2008-04-13T01:42:04Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "rewrite load_session and save_session to use much better modern techniques (in particular merge the notebook and non-notebook implementations)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2901",
    "user": "was"
}
```
Assignee: cwitty

Basically, I know a lot more about how to write Python/Cython code than I used to, so i can write these functions in a way that is (1) vastly better, and (2) will be easily doctested, and (3) work in (almost) the same way in the notebook or command line. 

This depends on the patch up at #2883.  #2883 should be applied then the code attached to this patch, once this patch is accepted.

I've separated this out from #2883, since #2883 really *must* get applied, and the code here should be, but it's really a separate issue, and more nontrivial.

Issue created by migration from https://trac.sagemath.org/ticket/2901





---

archive/issue_comments_019993.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-13T04:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2901#issuecomment-19993",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_019994.json:
```json
{
    "body": "Patch is up.   This basically replaces a bunch of terrifying ugly undocumented miserable scary code (umh, that I wrote) by nice modern well-documented code.",
    "created_at": "2008-04-13T04:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2901#issuecomment-19994",
    "user": "was"
}
```

Patch is up.   This basically replaces a bunch of terrifying ugly undocumented miserable scary code (umh, that I wrote) by nice modern well-documented code.



---

archive/issue_comments_019995.json:
```json
{
    "body": "I am not enough of a notebook user to test this thoroughly, but the code is good and the documentation is good.  I say apply immediately!\n\nOne quibble: could the module comment make it clear why this is in Cython and not Python?  I think there's a locals() trick at play, but it should be made clear none-the-less.",
    "created_at": "2008-04-13T04:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2901#issuecomment-19995",
    "user": "ncalexan"
}
```

I am not enough of a notebook user to test this thoroughly, but the code is good and the documentation is good.  I say apply immediately!

One quibble: could the module comment make it clear why this is in Cython and not Python?  I think there's a locals() trick at play, but it should be made clear none-the-less.



---

archive/issue_comments_019996.json:
```json
{
    "body": "Ok, I tracked down the issue for the reject of hunk two in worksheet.py. It expects:\n\n```\nif t.startswith('load_session'):\n    filename = self.hunt_file(filename)\n```\n\nBut the file contains:\n\n```\nfilename = self.hunt_file(filename)\n```\n\nI am deleting hunk two as is and then apply the rest of the patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T16:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2901#issuecomment-19996",
    "user": "mabshoff"
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

archive/issue_comments_019997.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-13T16:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2901#issuecomment-19997",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha5



---

archive/issue_comments_019998.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-13T16:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2901#issuecomment-19998",
    "user": "mabshoff"
}
```

Resolution: fixed
