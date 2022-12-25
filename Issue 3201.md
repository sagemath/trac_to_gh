# Issue 3201: notebook -- bug in parsing \ at end of line in %latex mode

archive/issues_003201.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n\nA subtle problem with \"%latex\" cells is illustrated at\n<http://www-maths.swan.ac.uk/staff/fwc/sage-notebook-latex.tiff>\n\nWhen \"\\\\\" occurs at the end of a line it seems to gooble the first\ncharacter in the next line.\n\nI'm using Mac OS X 10.4.11, and the same thing happens both Firefox\nand Safari.\n\nFrancis\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3201\n\n",
    "created_at": "2008-05-14T01:18:07Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "notebook -- bug in parsing \\ at end of line in %latex mode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3201",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby


```

A subtle problem with "%latex" cells is illustrated at
<http://www-maths.swan.ac.uk/staff/fwc/sage-notebook-latex.tiff>

When "\\" occurs at the end of a line it seems to gooble the first
character in the next line.

I'm using Mac OS X 10.4.11, and the same thing happens both Firefox
and Safari.

Francis
```


Issue created by migration from https://trac.sagemath.org/ticket/3201





---

archive/issue_comments_022070.json:
```json
{
    "body": "I can confirm that this sort of bug is very likely to happen.  I think \\ parsing\ngets done before the code gets sent to latex.eval or something like that.  It's an\ninteresting bug, and definitely something that needs to get fixed.",
    "created_at": "2008-05-14T01:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22070",
    "user": "https://github.com/williamstein"
}
```

I can confirm that this sort of bug is very likely to happen.  I think \ parsing
gets done before the code gets sent to latex.eval or something like that.  It's an
interesting bug, and definitely something that needs to get fixed.



---

archive/issue_comments_022071.json:
```json
{
    "body": "This is caused by the line\n\n\n```\n        I = I.replace('\\\\\\n','')\n```\n\n\nin worksheet.py.  This should be cleaner to fix after some other changes I have planned.  This is here just as a reminder to me.",
    "created_at": "2009-01-19T22:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22071",
    "user": "https://github.com/mwhansen"
}
```

This is caused by the line


```
        I = I.replace('\\\n','')
```


in worksheet.py.  This should be cleaner to fix after some other changes I have planned.  This is here just as a reminder to me.



---

archive/issue_comments_022072.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-01-19T22:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22072",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_022073.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-19T22:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22073",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022074.json:
```json
{
    "body": "Attachment [trac_3201.patch](tarball://root/attachments/some-uuid/ticket3201/trac_3201.patch) by @mwhansen created at 2009-01-22 07:24:05",
    "created_at": "2009-01-22T07:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22074",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3201.patch](tarball://root/attachments/some-uuid/ticket3201/trac_3201.patch) by @mwhansen created at 2009-01-22 07:24:05



---

archive/issue_comments_022075.json:
```json
{
    "body": "Note that this patch depends on #5050.",
    "created_at": "2009-01-22T14:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22075",
    "user": "https://github.com/mwhansen"
}
```

Note that this patch depends on #5050.



---

archive/issue_comments_022076.json:
```json
{
    "body": "The patch works for me.  Where is the doctest?",
    "created_at": "2009-01-22T16:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22076",
    "user": "https://github.com/jasongrout"
}
```

The patch works for me.  Where is the doctest?



---

archive/issue_comments_022077.json:
```json
{
    "body": "I don't know a good way to add a doctest.  I've added a test to Selenium test suite.",
    "created_at": "2009-01-24T04:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22077",
    "user": "https://github.com/mwhansen"
}
```

I don't know a good way to add a doctest.  I've added a test to Selenium test suite.



---

archive/issue_comments_022078.json:
```json
{
    "body": "Positive review even though this skirts the doctesting rule.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T14:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22078",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review even though this skirts the doctesting rule.

Cheers,

Michael



---

archive/issue_comments_022079.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T15:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22079",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022080.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T15:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22080",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael
