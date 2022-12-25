# Issue 5539: "sage -docbuild" could use a better error message

archive/issues_005539.json:
```json
{
    "body": "Assignee: tba\n\n\n```\n$ sage -docbuild\nYou must specify the document name and the output format\n```\n\n\nIt would be nice if it at least gave a list of available documents to build. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5539\n\n",
    "created_at": "2009-03-17T00:21:15Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "\"sage -docbuild\" could use a better error message",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5539",
    "user": "https://github.com/robertwb"
}
```
Assignee: tba


```
$ sage -docbuild
You must specify the document name and the output format
```


It would be nice if it at least gave a list of available documents to build. 

Issue created by migration from https://trac.sagemath.org/ticket/5539





---

archive/issue_comments_043007.json:
```json
{
    "body": "It would also be nice if it gave a list of available output formats.",
    "created_at": "2009-03-17T00:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5539#issuecomment-43007",
    "user": "https://github.com/aghitza"
}
```

It would also be nice if it gave a list of available output formats.



---

archive/issue_comments_043008.json:
```json
{
    "body": "Here's a patch which doesn't do what you're asking, but tells you how to get the list.",
    "created_at": "2009-06-10T21:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5539#issuecomment-43008",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch which doesn't do what you're asking, but tells you how to get the list.



---

archive/issue_comments_043009.json:
```json
{
    "body": "Attachment [trac_5539.patch](tarball://root/attachments/some-uuid/ticket5539/trac_5539.patch) by @jhpalmieri created at 2009-06-10 21:58:02",
    "created_at": "2009-06-10T21:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5539#issuecomment-43009",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_5539.patch](tarball://root/attachments/some-uuid/ticket5539/trac_5539.patch) by @jhpalmieri created at 2009-06-10 21:58:02



---

archive/issue_comments_043010.json:
```json
{
    "body": "Yes, I agree that the command\n\n```\nsage -docbuild -help\n```\n\nprovides more help on building the documentation. The error message of \n\n```\nsage -docbuild\n```\n \nnow informs the user about that command. Positive review.",
    "created_at": "2009-06-13T11:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5539#issuecomment-43010",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Yes, I agree that the command

```
sage -docbuild -help
```

provides more help on building the documentation. The error message of 

```
sage -docbuild
```
 
now informs the user about that command. Positive review.



---

archive/issue_events_005786.json:
```json
{
    "actor": "@ncalexan",
    "created_at": "2009-06-13T22:57:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5539",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5539#event-5786"
}
```



---

archive/issue_comments_043011.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T22:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5539#issuecomment-43011",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed
