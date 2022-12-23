# Issue 5772: notebook -- typo in twist.py causes Internal Server Error

archive/issues_005772.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n\t  File \"/Users/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/server/notebook/twist.py\", line 379, in callback\n\t    return HTMLRespone(stream = message(s, '/'))\n\texceptions.NameError: global name 'HTMLRespone' is not defined\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5772\n\n",
    "created_at": "2009-04-13T04:10:42Z",
    "labels": [
        "notebook",
        "critical",
        "bug"
    ],
    "title": "notebook -- typo in twist.py causes Internal Server Error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5772",
    "user": "was"
}
```
Assignee: boothby


```
	  File "/Users/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 379, in callback
	    return HTMLRespone(stream = message(s, '/'))
	exceptions.NameError: global name 'HTMLRespone' is not defined
```


Issue created by migration from https://trac.sagemath.org/ticket/5772





---

archive/issue_comments_045147.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-13T04:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5772#issuecomment-45147",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_045148.json:
```json
{
    "body": "I give this a positie review. :)",
    "created_at": "2009-04-13T04:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5772#issuecomment-45148",
    "user": "ddrake"
}
```

I give this a positie review. :)



---

archive/issue_comments_045149.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T05:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5772#issuecomment-45149",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045150.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T05:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5772#issuecomment-45150",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
