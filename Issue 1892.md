# Issue 1892: notebook -- uploading a data file should give some help about the DATA variable

archive/issues_001892.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n> The other option which some students tried was the upload a file\n> using Data.  It indeed uploads the file to a text cell, but we were\n> unable to find out how one accesses it. \n\nUpload it then access it by typing\n\nopen(DATA + 'chapitre.1.txt').read()\n\nThis DATA variable is documented in line three if you click on the Help button\nin the upper right of the worksheet.  It would also be good if it appeared any\ntime you upload a file in the confirmation message -- it doesn't right now.  I'll\nmake a ticket to add this (which will be very easy). \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1892\n\n",
    "created_at": "2008-01-23T14:02:10Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- uploading a data file should give some help about the DATA variable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1892",
    "user": "was"
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

archive/issue_comments_011982.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-11T06:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1892#issuecomment-11982",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_011983.json:
```json
{
    "body": "Patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-12T11:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1892#issuecomment-11983",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_011984.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-12T11:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1892#issuecomment-11984",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011985.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-12T11:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1892#issuecomment-11985",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha1
