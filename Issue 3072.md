# Issue 3072: sage -i numeric-24.2 (and all other experimental packages) fails

archive/issues_003072.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe problem is in local/bin/sage-download_package which checks for an error in the download very stupidly.  This needs to be rewritten.  The basic question is how to use urllib to tell whether a URL is valid or is a 404 not found. \n\nThe thing that triggered this problem is that sagemath.org's server configuration somehow changed, which changed the error page displayed on failure. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3072\n\n",
    "created_at": "2008-05-01T14:20:19Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "title": "sage -i numeric-24.2 (and all other experimental packages) fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3072",
    "user": "was"
}
```
Assignee: mabshoff

The problem is in local/bin/sage-download_package which checks for an error in the download very stupidly.  This needs to be rewritten.  The basic question is how to use urllib to tell whether a URL is valid or is a 404 not found. 

The thing that triggered this problem is that sagemath.org's server configuration somehow changed, which changed the error page displayed on failure. 

Issue created by migration from https://trac.sagemath.org/ticket/3072





---

archive/issue_comments_021205.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-05-01T14:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3072#issuecomment-21205",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_021206.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-01T15:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3072#issuecomment-21206",
    "user": "wjp"
}
```

Attachment



---

archive/issue_comments_021207.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-02T11:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3072#issuecomment-21207",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021208.json:
```json
{
    "body": "Merged in Sage 3.0.1.rc0",
    "created_at": "2008-05-02T11:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3072#issuecomment-21208",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.rc0
