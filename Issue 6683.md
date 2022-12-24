# Issue 6683: notebook worksheet rating_info link leads to error page

archive/issues_006683.json:
```json
{
    "body": "Assignee: wstein\n\nKeywords: notebook worksheet rating_info error\n\nClicking on a rating_info link in a  list of notebook worksheets produces a blank page titled \"Error | Sage Notebook\".\n\nDiagnosis and suggested solution found in this [thread](http://groups.google.com/group/sage-support/browse_frm/thread/4d2524b7ae5dd26c#) on sage-support.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6683\n\n",
    "created_at": "2009-08-07T09:29:50Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook worksheet rating_info link leads to error page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6683",
    "user": "khorton"
}
```
Assignee: wstein

Keywords: notebook worksheet rating_info error

Clicking on a rating_info link in a  list of notebook worksheets produces a blank page titled "Error | Sage Notebook".

Diagnosis and suggested solution found in this [thread](http://groups.google.com/group/sage-support/browse_frm/thread/4d2524b7ae5dd26c#) on sage-support.

Issue created by migration from https://trac.sagemath.org/ticket/6683





---

archive/issue_comments_054953.json:
```json
{
    "body": "Attachment [twist.py](tarball://root/attachments/some-uuid/ticket6683/twist.py) by NoSyu created at 2009-08-07 21:29:33\n\nDelete message in Worksheet_rating_info and Worksheet_rate class from Sage 4.1 original source file server/notebook/twist.py",
    "created_at": "2009-08-07T21:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6683#issuecomment-54953",
    "user": "NoSyu"
}
```

Attachment [twist.py](tarball://root/attachments/some-uuid/ticket6683/twist.py) by NoSyu created at 2009-08-07 21:29:33

Delete message in Worksheet_rating_info and Worksheet_rate class from Sage 4.1 original source file server/notebook/twist.py



---

archive/issue_comments_054954.json:
```json
{
    "body": "In the Worksheet_rating_info and Worksheet_rate class in *server/notebook/twist.py*, it return the HTMLResponse that argument is stream and all return stream use message function. But message function in *twist.py* is used for error page to use *error_message.html* templete file. Unless the return is not error page, it use message function. So it always show the error page titled \"Error | Sage Notebook\".",
    "created_at": "2009-08-07T21:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6683#issuecomment-54954",
    "user": "NoSyu"
}
```

In the Worksheet_rating_info and Worksheet_rate class in *server/notebook/twist.py*, it return the HTMLResponse that argument is stream and all return stream use message function. But message function in *twist.py* is used for error page to use *error_message.html* templete file. Unless the return is not error page, it use message function. So it always show the error page titled "Error | Sage Notebook".



---

archive/issue_comments_054955.json:
```json
{
    "body": "This has already been fixed in #7786.",
    "created_at": "2010-01-19T16:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6683#issuecomment-54955",
    "user": "@TimDumol"
}
```

This has already been fixed in #7786.



---

archive/issue_comments_054956.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T16:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6683#issuecomment-54956",
    "user": "@TimDumol"
}
```

Resolution: duplicate
