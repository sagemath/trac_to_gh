# Issue 3201: notebook -- bug in parsing \ at end of line in %latex mode

archive/issues_003201.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n\nA subtle problem with \"%latex\" cells is illustrated at\n<http://www-maths.swan.ac.uk/staff/fwc/sage-notebook-latex.tiff>\n\nWhen \"\\\\\" occurs at the end of a line it seems to gooble the first\ncharacter in the next line.\n\nI'm using Mac OS X 10.4.11, and the same thing happens both Firefox\nand Safari.\n\nFrancis\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3201\n\n",
    "created_at": "2008-05-14T01:18:07Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- bug in parsing \\ at end of line in %latex mode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3201",
    "user": "was"
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

archive/issue_comments_022117.json:
```json
{
    "body": "I can confirm that this sort of bug is very likely to happen.  I think \\ parsing\ngets done before the code gets sent to latex.eval or something like that.  It's an\ninteresting bug, and definitely something that needs to get fixed.",
    "created_at": "2008-05-14T01:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22117",
    "user": "was"
}
```

I can confirm that this sort of bug is very likely to happen.  I think \ parsing
gets done before the code gets sent to latex.eval or something like that.  It's an
interesting bug, and definitely something that needs to get fixed.



---

archive/issue_comments_022118.json:
```json
{
    "body": "This is caused by the line\n\n\n```\n        I = I.replace('\\\\\\n','')\n```\n\n\nin worksheet.py.  This should be cleaner to fix after some other changes I have planned.  This is here just as a reminder to me.",
    "created_at": "2009-01-19T22:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22118",
    "user": "mhansen"
}
```

This is caused by the line


```
        I = I.replace('\\\n','')
```


in worksheet.py.  This should be cleaner to fix after some other changes I have planned.  This is here just as a reminder to me.



---

archive/issue_comments_022119.json:
```json
{
    "body": "Changing assignee from boothby to mhansen.",
    "created_at": "2009-01-19T22:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22119",
    "user": "mhansen"
}
```

Changing assignee from boothby to mhansen.



---

archive/issue_comments_022120.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-19T22:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22120",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022121.json:
```json
{
    "body": "Attachment [trac_3201.patch](tarball://root/attachments/some-uuid/ticket3201/trac_3201.patch) by mhansen created at 2009-01-22 07:24:05",
    "created_at": "2009-01-22T07:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22121",
    "user": "mhansen"
}
```

Attachment [trac_3201.patch](tarball://root/attachments/some-uuid/ticket3201/trac_3201.patch) by mhansen created at 2009-01-22 07:24:05



---

archive/issue_comments_022122.json:
```json
{
    "body": "Note that this patch depends on #5050.",
    "created_at": "2009-01-22T14:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22122",
    "user": "mhansen"
}
```

Note that this patch depends on #5050.



---

archive/issue_comments_022123.json:
```json
{
    "body": "The patch works for me.  Where is the doctest?",
    "created_at": "2009-01-22T16:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22123",
    "user": "jason"
}
```

The patch works for me.  Where is the doctest?



---

archive/issue_comments_022124.json:
```json
{
    "body": "I don't know a good way to add a doctest.  I've added a test to Selenium test suite.",
    "created_at": "2009-01-24T04:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22124",
    "user": "mhansen"
}
```

I don't know a good way to add a doctest.  I've added a test to Selenium test suite.



---

archive/issue_comments_022125.json:
```json
{
    "body": "Positive review even though this skirts the doctesting rule.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T14:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22125",
    "user": "mabshoff"
}
```

Positive review even though this skirts the doctesting rule.

Cheers,

Michael



---

archive/issue_comments_022126.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T15:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22126",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022127.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T15:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3201#issuecomment-22127",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael
