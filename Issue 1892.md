# Issue 1892: notebook -- uploading a data file should give some help about the DATA variable

archive/issues_001892.json:
```json
{
    "body": "Assignee: boothby\n\n```\n> The other option which some students tried was the upload a file\n> using Data.  It indeed uploads the file to a text cell, but we were\n> unable to find out how one accesses it. \n\nUpload it then access it by typing\n\nopen(DATA + 'chapitre.1.txt').read()\n\nThis DATA variable is documented in line three if you click on the Help button\nin the upper right of the worksheet.  It would also be good if it appeared any\ntime you upload a file in the confirmation message -- it doesn't right now.  I'll\nmake a ticket to add this (which will be very easy). \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1892\n\n",
    "created_at": "2008-01-23T14:02:10Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "notebook -- uploading a data file should give some help about the DATA variable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1892",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

```
> The other option which some students tried was the upload a file
> using Data.  It indeed uploads the file to a text cell, but we were
> unable to find out how one accesses it. 

Upload it then access it by typing

open(DATA + 'chapitre.1.txt').read()

This DATA variable is documented in line three if you click on the Help button
in the upper right of the worksheet.  It would also be good if it appeared any
time you upload a file in the confirmation message -- it doesn't right now.  I'll
make a ticket to add this (which will be very easy). 
```

Issue created by migration from https://trac.sagemath.org/ticket/1892





---

archive/issue_comments_011953.json:
```json
{
    "body": "Attachment [sage-1892.patch](tarball://root/attachments/some-uuid/ticket1892/sage-1892.patch) by @williamstein created at 2008-05-11 06:19:41",
    "created_at": "2008-05-11T06:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1892#issuecomment-11953",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-1892.patch](tarball://root/attachments/some-uuid/ticket1892/sage-1892.patch) by @williamstein created at 2008-05-11 06:19:41



---

archive/issue_comments_011954.json:
```json
{
    "body": "Patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-12T11:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1892#issuecomment-11954",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_011955.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-12T11:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1892#issuecomment-11955",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011956.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-12T11:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1892#issuecomment-11956",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha1



---

archive/issue_events_004554.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-12T11:22:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1892",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1892#event-4554"
}
```
