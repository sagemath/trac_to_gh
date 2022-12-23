# Issue 4471: name worksheet when creating a new worksheet

archive/issues_004471.json:
```json
{
    "body": "Assignee: boothby\n\nIt would be better, I think, to have the worksheet named when it is created. Right now it is given the name 'untitled' and one needs to click on the title or select 'rename' from the menu. This ends up in a lot of worksheets being left named 'untitled'.\n\nSo please change so that the user is given a naming window when creating a new worksheet which can default to 'untitled' if the user doesn't enter a name.\n\nWilliam agrees that this would be a good idea.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4471\n\n",
    "created_at": "2008-11-08T21:36:12Z",
    "labels": [
        "notebook",
        "trivial",
        "enhancement"
    ],
    "title": "name worksheet when creating a new worksheet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4471",
    "user": "mrubinst"
}
```
Assignee: boothby

It would be better, I think, to have the worksheet named when it is created. Right now it is given the name 'untitled' and one needs to click on the title or select 'rename' from the menu. This ends up in a lot of worksheets being left named 'untitled'.

So please change so that the user is given a naming window when creating a new worksheet which can default to 'untitled' if the user doesn't enter a name.

William agrees that this would be a good idea.

Issue created by migration from https://trac.sagemath.org/ticket/4471





---

archive/issue_comments_033026.json:
```json
{
    "body": "Better luck in 3.2.1+\n\nCheers,\n\nMichael",
    "created_at": "2008-11-09T00:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-33026",
    "user": "mabshoff"
}
```

Better luck in 3.2.1+

Cheers,

Michael



---

archive/issue_comments_033027.json:
```json
{
    "body": "+1.  It's crazy how many \"Untitled\" worksheets I have.",
    "created_at": "2008-11-09T02:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-33027",
    "user": "jason"
}
```

+1.  It's crazy how many "Untitled" worksheets I have.



---

archive/issue_comments_033028.json:
```json
{
    "body": "Just found the following in notebook.Notebook.html\n\n\n```\n# Uncomment this to force rename when the worksheet is opened (annoying!)\n#if W and W.name() == \"Untitled\":\n#    head += '<script  type=\"text/javascript\">setTimeout(\"rename_worksheet()\",1)</script>'\n```\n",
    "created_at": "2008-12-06T05:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-33028",
    "user": "TimothyClemans"
}
```

Just found the following in notebook.Notebook.html


```
# Uncomment this to force rename when the worksheet is opened (annoying!)
#if W and W.name() == "Untitled":
#    head += '<script  type="text/javascript">setTimeout("rename_worksheet()",1)</script>'
```




---

archive/issue_comments_033029.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-06T21:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-33029",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_033030.json:
```json
{
    "body": "With this ticket you're forced to rename any worksheet with the title \"Untitled\". You should only have to rename new worksheets.",
    "created_at": "2008-12-08T17:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-33030",
    "user": "TimothyClemans"
}
```

With this ticket you're forced to rename any worksheet with the title "Untitled". You should only have to rename new worksheets.



---

archive/issue_comments_033031.json:
```json
{
    "body": "Hasn't some other ticket (or this one) already been merged to fix this?",
    "created_at": "2009-11-01T01:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-33031",
    "user": "mpatel"
}
```

Hasn't some other ticket (or this one) already been merged to fix this?



---

archive/issue_comments_033032.json:
```json
{
    "body": "This is now fixed.",
    "created_at": "2009-11-03T21:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-33032",
    "user": "was"
}
```

This is now fixed.



---

archive/issue_comments_033033.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-03T21:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4471#issuecomment-33033",
    "user": "was"
}
```

Resolution: fixed
