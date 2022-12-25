# Issue 4471: [with patch; needs work] name worksheet when creating a new worksheet

archive/issues_004471.json:
```json
{
    "body": "Assignee: boothby\n\nIt would be better, I think, to have the worksheet named when it is created. Right now it is given the name 'untitled' and one needs to click on the title or select 'rename' from the menu. This ends up in a lot of worksheets being left named 'untitled'.\n\nSo please change so that the user is given a naming window when creating a new worksheet which can default to 'untitled' if the user doesn't enter a name.\n\nWilliam agrees that this would be a good idea.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4471\n\n",
    "closed_at": "2009-11-03T21:03:14Z",
    "created_at": "2008-11-08T21:36:12Z",
    "labels": [
        "component: notebook",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "[with patch; needs work] name worksheet when creating a new worksheet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4471",
    "user": "https://trac.sagemath.org/admin/accounts/users/mrubinst"
}
```
Assignee: boothby

It would be better, I think, to have the worksheet named when it is created. Right now it is given the name 'untitled' and one needs to click on the title or select 'rename' from the menu. This ends up in a lot of worksheets being left named 'untitled'.

So please change so that the user is given a naming window when creating a new worksheet which can default to 'untitled' if the user doesn't enter a name.

William agrees that this would be a good idea.

Issue created by migration from https://trac.sagemath.org/ticket/4471





---

archive/issue_events_010102.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-09T00:22:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "milestone": "sage-3.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4471#event-10102"
}
```



---

archive/issue_comments_032961.json:
```json
{
    "body": "Better luck in 3.2.1+\n\nCheers,\n\nMichael",
    "created_at": "2008-11-09T00:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-32961",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Better luck in 3.2.1+

Cheers,

Michael



---

archive/issue_comments_032962.json:
```json
{
    "body": "+1.  It's crazy how many \"Untitled\" worksheets I have.",
    "created_at": "2008-11-09T02:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-32962",
    "user": "https://github.com/jasongrout"
}
```

+1.  It's crazy how many "Untitled" worksheets I have.



---

archive/issue_comments_032963.json:
```json
{
    "body": "Just found the following in notebook.Notebook.html\n\n```\n# Uncomment this to force rename when the worksheet is opened (annoying!)\n#if W and W.name() == \"Untitled\":\n#    head += '<script  type=\"text/javascript\">setTimeout(\"rename_worksheet()\",1)</script>'\n```",
    "created_at": "2008-12-06T05:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-32963",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Just found the following in notebook.Notebook.html

```
# Uncomment this to force rename when the worksheet is opened (annoying!)
#if W and W.name() == "Untitled":
#    head += '<script  type="text/javascript">setTimeout("rename_worksheet()",1)</script>'
```



---

archive/issue_comments_032964.json:
```json
{
    "body": "Attachment [trac_4471.patch](tarball://root/attachments/some-uuid/ticket4471/trac_4471.patch) by @williamstein created at 2008-12-06 21:09:49",
    "created_at": "2008-12-06T21:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-32964",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4471.patch](tarball://root/attachments/some-uuid/ticket4471/trac_4471.patch) by @williamstein created at 2008-12-06 21:09:49



---

archive/issue_comments_032965.json:
```json
{
    "body": "With this ticket you're forced to rename any worksheet with the title \"Untitled\". You should only have to rename new worksheets.",
    "created_at": "2008-12-08T17:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-32965",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

With this ticket you're forced to rename any worksheet with the title "Untitled". You should only have to rename new worksheets.



---

archive/issue_comments_032966.json:
```json
{
    "body": "Hasn't some other ticket (or this one) already been merged to fix this?",
    "created_at": "2009-11-01T01:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-32966",
    "user": "https://github.com/qed777"
}
```

Hasn't some other ticket (or this one) already been merged to fix this?



---

archive/issue_events_010103.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-11-03T21:03:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4471#event-10103"
}
```



---

archive/issue_comments_032967.json:
```json
{
    "body": "This is now fixed.",
    "created_at": "2009-11-03T21:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-32967",
    "user": "https://github.com/williamstein"
}
```

This is now fixed.



---

archive/issue_comments_032968.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-03T21:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-32968",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
