# Issue 3820: notebook -- sometimes published worksheets are listed as being published by pub.

archive/issues_003820.json:
```json
{
    "body": "Assignee: boothby\n\nnotebook -- sometimes published worksheets are listed as being published by pub; this should *never* be the case. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3820\n\n",
    "created_at": "2008-08-12T16:17:51Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "notebook -- sometimes published worksheets are listed as being published by pub.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3820",
    "user": "@williamstein"
}
```
Assignee: boothby

notebook -- sometimes published worksheets are listed as being published by pub; this should *never* be the case. 

Issue created by migration from https://trac.sagemath.org/ticket/3820





---

archive/issue_comments_027166.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-24T05:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3820#issuecomment-27166",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_027167.json:
```json
{
    "body": "I've added a test in the selenium suite for this.",
    "created_at": "2009-01-24T05:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3820#issuecomment-27167",
    "user": "@mwhansen"
}
```

I've added a test in the selenium suite for this.



---

archive/issue_comments_027168.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-01-24T05:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3820#issuecomment-27168",
    "user": "@mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_027169.json:
```json
{
    "body": "This patch needs to be rebased unless there is some dependency I am not aware of:\n\n```\nsage-3.3.alpha4/devel/sage$ patch -p1 < trac_3820.patch\\?format\\=raw \npatching file sage/server/notebook/templates/worksheet_listing.html\nHunk #1 succeeded at 130 (offset 1 line).\nHunk #2 FAILED at 178.\n1 out of 2 hunks FAILED -- saving rejects to file sage/server/notebook/templates/worksheet_listing.html.rej\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T05:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3820#issuecomment-27169",
    "user": "mabshoff"
}
```

This patch needs to be rebased unless there is some dependency I am not aware of:

```
sage-3.3.alpha4/devel/sage$ patch -p1 < trac_3820.patch\?format\=raw 
patching file sage/server/notebook/templates/worksheet_listing.html
Hunk #1 succeeded at 130 (offset 1 line).
Hunk #2 FAILED at 178.
1 out of 2 hunks FAILED -- saving rejects to file sage/server/notebook/templates/worksheet_listing.html.rej
```


Cheers,

Michael



---

archive/issue_comments_027170.json:
```json
{
    "body": "Attachment [trac_3820.patch](tarball://root/attachments/some-uuid/ticket3820/trac_3820.patch) by @mwhansen created at 2009-02-15 04:22:58",
    "created_at": "2009-02-15T04:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3820#issuecomment-27170",
    "user": "@mwhansen"
}
```

Attachment [trac_3820.patch](tarball://root/attachments/some-uuid/ticket3820/trac_3820.patch) by @mwhansen created at 2009-02-15 04:22:58



---

archive/issue_comments_027171.json:
```json
{
    "body": "I've put up a rebased patch which applies against rc0.",
    "created_at": "2009-02-15T04:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3820#issuecomment-27171",
    "user": "@mwhansen"
}
```

I've put up a rebased patch which applies against rc0.



---

archive/issue_comments_027172.json:
```json
{
    "body": "looks good\n\n* note that if original worksheet is deleted then the owner cell on the published worksheets page is blank",
    "created_at": "2009-03-16T20:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3820#issuecomment-27172",
    "user": "TimothyClemans"
}
```

looks good

* note that if original worksheet is deleted then the owner cell on the published worksheets page is blank



---

archive/issue_comments_027173.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T08:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3820#issuecomment-27173",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_027174.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T08:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3820#issuecomment-27174",
    "user": "mabshoff"
}
```

Resolution: fixed
