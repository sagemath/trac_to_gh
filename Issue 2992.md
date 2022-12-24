# Issue 2992: notebook -- help(foo) in the notebook should not word wrap

archive/issues_002992.json:
```json
{
    "body": "Assignee: boothby\n\nThis is *very* easy to implement:\n\n1. Make it so help is a wrapper around internal help.  (Already true?)\n\n2. If in notebook then display the result using html and pre.  Done.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2992\n\n",
    "created_at": "2008-04-21T17:50:20Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "notebook -- help(foo) in the notebook should not word wrap",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2992",
    "user": "@williamstein"
}
```
Assignee: boothby

This is *very* easy to implement:

1. Make it so help is a wrapper around internal help.  (Already true?)

2. If in notebook then display the result using html and pre.  Done.



Issue created by migration from https://trac.sagemath.org/ticket/2992





---

archive/issue_comments_020585.json:
```json
{
    "body": "Attachment [sage-2992.patch](tarball://root/attachments/some-uuid/ticket2992/sage-2992.patch) by @williamstein created at 2008-05-11 05:44:17",
    "created_at": "2008-05-11T05:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2992#issuecomment-20585",
    "user": "@williamstein"
}
```

Attachment [sage-2992.patch](tarball://root/attachments/some-uuid/ticket2992/sage-2992.patch) by @williamstein created at 2008-05-11 05:44:17



---

archive/issue_comments_020586.json:
```json
{
    "body": "The attached patch does this:\n\n```\n\n  1. Wrote new version of help command for the notebook.\n  2. Slightly modified how truncation is done to account for 1.\t While I was at\tit, I fixed another\n     but where reloading a page would put multiple \"output truncated\" messages at the top of the page.\n\n```\n",
    "created_at": "2008-05-11T05:44:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2992#issuecomment-20586",
    "user": "@williamstein"
}
```

The attached patch does this:

```

  1. Wrote new version of help command for the notebook.
  2. Slightly modified how truncation is done to account for 1.	 While I was at	it, I fixed another
     but where reloading a page would put multiple "output truncated" messages at the top of the page.

```




---

archive/issue_comments_020587.json:
```json
{
    "body": "This is ugly -- scroll down:\n\n```\nhelp(interact)\n```\n\n\nI don't know if this is worth a fully negative review, but I think this looks like crap.  Perhaps a pre tag would make it all better?",
    "created_at": "2008-05-12T05:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2992#issuecomment-20587",
    "user": "boothby"
}
```

This is ugly -- scroll down:

```
help(interact)
```


I don't know if this is worth a fully negative review, but I think this looks like crap.  Perhaps a pre tag would make it all better?



---

archive/issue_comments_020588.json:
```json
{
    "body": "Attachment [sage-2992-part2.patch](tarball://root/attachments/some-uuid/ticket2992/sage-2992-part2.patch) by @williamstein created at 2008-05-15 02:04:36\n\nI completely rewrote help(...) to address the referee remark and to make help(...) vastly more robust when the output is MASSIVE (which it often is).  Try, e.g., \n\n\n```\nimport numpy\nhelp(numpy)\n```\n\n\nwith the new version, and your browser will *not* get killed.  I had my browser\ncrash in class when teaching with the old version.\n\nOf course the issues with help(interact) are also fixed. \n\nApply both patches, in order.",
    "created_at": "2008-05-15T02:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2992#issuecomment-20588",
    "user": "@williamstein"
}
```

Attachment [sage-2992-part2.patch](tarball://root/attachments/some-uuid/ticket2992/sage-2992-part2.patch) by @williamstein created at 2008-05-15 02:04:36

I completely rewrote help(...) to address the referee remark and to make help(...) vastly more robust when the output is MASSIVE (which it often is).  Try, e.g., 


```
import numpy
help(numpy)
```


with the new version, and your browser will *not* get killed.  I had my browser
crash in class when teaching with the old version.

Of course the issues with help(interact) are also fixed. 

Apply both patches, in order.



---

archive/issue_comments_020589.json:
```json
{
    "body": "Failed to apply :(",
    "created_at": "2008-05-15T04:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2992#issuecomment-20589",
    "user": "boothby"
}
```

Failed to apply :(



---

archive/issue_comments_020590.json:
```json
{
    "body": "Works for me.",
    "created_at": "2008-05-17T19:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2992#issuecomment-20590",
    "user": "boothby"
}
```

Works for me.



---

archive/issue_comments_020591.json:
```json
{
    "body": "Merged both patches in in Sage 3.0.2.alpha1. The dependecy tree is borked since part 2 depends on #3024 being merged. D'oh",
    "created_at": "2008-05-17T19:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2992#issuecomment-20591",
    "user": "mabshoff"
}
```

Merged both patches in in Sage 3.0.2.alpha1. The dependecy tree is borked since part 2 depends on #3024 being merged. D'oh



---

archive/issue_comments_020592.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-17T19:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2992#issuecomment-20592",
    "user": "mabshoff"
}
```

Resolution: fixed
