# Issue 2635: MAJOR NOTEBOOK BUG -- sending unevaluated cells back to the server is severly broken.

archive/issues_002635.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2635\n\n",
    "created_at": "2008-03-21T19:10:38Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "MAJOR NOTEBOOK BUG -- sending unevaluated cells back to the server is severly broken.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2635",
    "user": "@williamstein"
}
```
Assignee: boothby

CC:  boothby



Issue created by migration from https://trac.sagemath.org/ticket/2635





---

archive/issue_comments_018104.json:
```json
{
    "body": "\n```\n\nOn Fri, Mar 21, 2008 at 11:22 AM, Marshall Hampton <hamptonio@gmail.com> wrote:\n> \n>  If I kill my notebook session, and then restart, it seems that often\n>  the \"+\" character has been stripped from my worksheets.  However, this\n>  doesn't always happen.  It does happen frequently, using 2.10.4 on\n>  both ppc and intel macs.\n>  \n>  Can anyone else reproduce this?\n\nI think this is a ** MAJOR BUG ** introduced by a new feature that Tom Boothby\njust implemented in the notebook (and that I didn't catch in the referee process).  \nThis is definitely a block for 2.11.    Try the following to replicate it:\n   1. Create a new blank worksheet with several blank cells\n   2. Type 2+2 in the first cell -- do *NOT* press shift enter. \n   3. Simply move the cursor out of the first cell to the second one (use down arrow).\n   4. Now refresh the page -- or better leave the page and go back and refresh.\n  The plus sign vanishes!\n\nThe problem is that when you change a cell and move the cursor out,\nthe changed cell is incorrectly sent back to the server.   To avoid this\nfor now, never ever change a cell without shift-entering it. \n\nWilliam\n\n```\n",
    "created_at": "2008-03-21T19:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2635#issuecomment-18104",
    "user": "@williamstein"
}
```


```

On Fri, Mar 21, 2008 at 11:22 AM, Marshall Hampton <hamptonio@gmail.com> wrote:
> 
>  If I kill my notebook session, and then restart, it seems that often
>  the "+" character has been stripped from my worksheets.  However, this
>  doesn't always happen.  It does happen frequently, using 2.10.4 on
>  both ppc and intel macs.
>  
>  Can anyone else reproduce this?

I think this is a ** MAJOR BUG ** introduced by a new feature that Tom Boothby
just implemented in the notebook (and that I didn't catch in the referee process).  
This is definitely a block for 2.11.    Try the following to replicate it:
   1. Create a new blank worksheet with several blank cells
   2. Type 2+2 in the first cell -- do *NOT* press shift enter. 
   3. Simply move the cursor out of the first cell to the second one (use down arrow).
   4. Now refresh the page -- or better leave the page and go back and refresh.
  The plus sign vanishes!

The problem is that when you change a cell and move the cursor out,
the changed cell is incorrectly sent back to the server.   To avoid this
for now, never ever change a cell without shift-entering it. 

William

```




---

archive/issue_comments_018105.json:
```json
{
    "body": "Attachment [2635-save-the-plusses.patch](tarball://root/attachments/some-uuid/ticket2635/2635-save-the-plusses.patch) by boothby created at 2008-03-21 20:00:18\n\nDANG!  Sorry, guys.  This fixes it.",
    "created_at": "2008-03-21T20:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2635#issuecomment-18105",
    "user": "boothby"
}
```

Attachment [2635-save-the-plusses.patch](tarball://root/attachments/some-uuid/ticket2635/2635-save-the-plusses.patch) by boothby created at 2008-03-21 20:00:18

DANG!  Sorry, guys.  This fixes it.



---

archive/issue_comments_018106.json:
```json
{
    "body": "It works!",
    "created_at": "2008-03-22T00:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2635#issuecomment-18106",
    "user": "@williamstein"
}
```

It works!



---

archive/issue_comments_018107.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-22T00:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2635#issuecomment-18107",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha1



---

archive/issue_comments_018108.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-22T00:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2635#issuecomment-18108",
    "user": "mabshoff"
}
```

Resolution: fixed
