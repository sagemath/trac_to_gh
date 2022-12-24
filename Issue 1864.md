# Issue 1864: simple notebook bug -- typing ? in a comment yields introspection but shouldn't (easy to fix in worksheet.py, probably)

archive/issues_001864.json:
```json
{
    "body": "Assignee: boothby\n\nTry this in the notebook\n\n```\n# This is a question?\n```\n\nand hit shift enter.  You get introspection on the word \"question\".  \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1864\n\n",
    "created_at": "2008-01-20T16:40:44Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "simple notebook bug -- typing ? in a comment yields introspection but shouldn't (easy to fix in worksheet.py, probably)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1864",
    "user": "@williamstein"
}
```
Assignee: boothby

Try this in the notebook

```
# This is a question?
```

and hit shift enter.  You get introspection on the word "question".  


Issue created by migration from https://trac.sagemath.org/ticket/1864





---

archive/issue_comments_011803.json:
```json
{
    "body": "I can't reproduce this in Firefox or Opera -- has it been fixed?",
    "created_at": "2008-03-16T19:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1864#issuecomment-11803",
    "user": "boothby"
}
```

I can't reproduce this in Firefox or Opera -- has it been fixed?



---

archive/issue_comments_011804.json:
```json
{
    "body": "This is easy to reproduce in firefox and has not been fixed.\nSee this screenshot:\n\nhttp://sage.math.washington.edu/home/was/tmp/screenshot-comment.png",
    "created_at": "2008-03-16T20:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1864#issuecomment-11804",
    "user": "@williamstein"
}
```

This is easy to reproduce in firefox and has not been fixed.
See this screenshot:

http://sage.math.washington.edu/home/was/tmp/screenshot-comment.png



---

archive/issue_comments_011805.json:
```json
{
    "body": "Attachment [sage-1864.patch](tarball://root/attachments/some-uuid/ticket1864/sage-1864.patch) by @williamstein created at 2008-05-11 06:06:32",
    "created_at": "2008-05-11T06:06:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1864#issuecomment-11805",
    "user": "@williamstein"
}
```

Attachment [sage-1864.patch](tarball://root/attachments/some-uuid/ticket1864/sage-1864.patch) by @williamstein created at 2008-05-11 06:06:32



---

archive/issue_comments_011806.json:
```json
{
    "body": "This breaks previously supported functionality (that I won't miss).  It used to be, one could type\n\n\n```\nfoo?\n```\n\n\nand press shift-enter to introspect.  I give this a positive review *if* that was an intended change.",
    "created_at": "2008-05-12T05:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1864#issuecomment-11806",
    "user": "boothby"
}
```

This breaks previously supported functionality (that I won't miss).  It used to be, one could type


```
foo?
```


and press shift-enter to introspect.  I give this a positive review *if* that was an intended change.



---

archive/issue_comments_011807.json:
```json
{
    "body": "The referee claims that say\n\n```\nlog?[shift-enter]\n```\n\ndoesn't work.  \n\nHowever it *does* work fine with this patch.  The referee needs to try again.",
    "created_at": "2008-05-15T02:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1864#issuecomment-11807",
    "user": "@williamstein"
}
```

The referee claims that say

```
log?[shift-enter]
```

doesn't work.  

However it *does* work fine with this patch.  The referee needs to try again.



---

archive/issue_comments_011808.json:
```json
{
    "body": "Weird. Works now.",
    "created_at": "2008-05-17T19:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1864#issuecomment-11808",
    "user": "boothby"
}
```

Weird. Works now.



---

archive/issue_comments_011809.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-17T19:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1864#issuecomment-11809",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011810.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-17T19:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1864#issuecomment-11810",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha1
