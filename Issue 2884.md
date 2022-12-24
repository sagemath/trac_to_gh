# Issue 2884: notebook -- bug; @interact cell eval doesn't clear out the old html output (easy to fix?)

archive/issues_002884.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2884\n\n",
    "created_at": "2008-04-11T23:50:22Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- bug; @interact cell eval doesn't clear out the old html output (easy to fix?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2884",
    "user": "was"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/2884





---

archive/issue_comments_019837.json:
```json
{
    "body": "Attachment [sage-2884.patch](tarball://root/attachments/some-uuid/ticket2884/sage-2884.patch) by was created at 2008-05-11 08:21:50",
    "created_at": "2008-05-11T08:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2884#issuecomment-19837",
    "user": "was"
}
```

Attachment [sage-2884.patch](tarball://root/attachments/some-uuid/ticket2884/sage-2884.patch) by was created at 2008-05-11 08:21:50



---

archive/issue_comments_019838.json:
```json
{
    "body": "The following is now broken:\n\n\n```\nplot(sin,0,1).show()\n@interact\ndef foo(a=\"1\"):\n    a\n```\n",
    "created_at": "2008-05-12T05:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2884#issuecomment-19838",
    "user": "boothby"
}
```

The following is now broken:


```
plot(sin,0,1).show()
@interact
def foo(a="1"):
    a
```




---

archive/issue_comments_019839.json:
```json
{
    "body": "Hi,\n\nYour only reason for giving a negative review was a claim that\n\n```\nplot(sin,0,1).show()\n@interact\ndef foo(a=\"1\"):\n    a\n```\n\nis now \"broken\".  However, this never did what you thought it\ndid.  The behavior in fact hasn't changed at all from how it was\nbefore, except to remove the bug where old graphics from\nthe previous version of the cell remained. \n\n`@`interact *by design* is only supposed to work when it is\nthe only thing in a cell. \n\nHaving multiple interacts in a cell, having additional graphics in\na cell, having nested interacts -- none of that should work at present,\nsince none of it has been implemented. \nThey're all things that would possibly be very nice to implement,\nbut they were not part of the design goals for the first version\nof interact.",
    "created_at": "2008-05-15T05:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2884#issuecomment-19839",
    "user": "was"
}
```

Hi,

Your only reason for giving a negative review was a claim that

```
plot(sin,0,1).show()
@interact
def foo(a="1"):
    a
```

is now "broken".  However, this never did what you thought it
did.  The behavior in fact hasn't changed at all from how it was
before, except to remove the bug where old graphics from
the previous version of the cell remained. 

`@`interact *by design* is only supposed to work when it is
the only thing in a cell. 

Having multiple interacts in a cell, having additional graphics in
a cell, having nested interacts -- none of that should work at present,
since none of it has been implemented. 
They're all things that would possibly be very nice to implement,
but they were not part of the design goals for the first version
of interact.



---

archive/issue_comments_019840.json:
```json
{
    "body": "Attachment [2884-docfix.patch](tarball://root/attachments/some-uuid/ticket2884/2884-docfix.patch) by boothby created at 2008-05-15 06:02:30",
    "created_at": "2008-05-15T06:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2884#issuecomment-19840",
    "user": "boothby"
}
```

Attachment [2884-docfix.patch](tarball://root/attachments/some-uuid/ticket2884/2884-docfix.patch) by boothby created at 2008-05-15 06:02:30



---

archive/issue_comments_019841.json:
```json
{
    "body": "It was not clear to me, even upon rereading the documentation, that `@`interact had to be alone in a cell.  The attached \"fixes\" the issue.  :)",
    "created_at": "2008-05-15T06:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2884#issuecomment-19841",
    "user": "boothby"
}
```

It was not clear to me, even upon rereading the documentation, that `@`interact had to be alone in a cell.  The attached "fixes" the issue.  :)



---

archive/issue_comments_019842.json:
```json
{
    "body": "Merged both patches in Sage 3.0.2.alpha1",
    "created_at": "2008-05-17T18:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2884#issuecomment-19842",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.0.2.alpha1



---

archive/issue_comments_019843.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-17T18:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2884#issuecomment-19843",
    "user": "mabshoff"
}
```

Resolution: fixed
