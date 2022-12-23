# Issue 5615: [with patch, not ready for review] use labels-as-values for fast_callable under gcc

archive/issues_005615.json:
```json
{
    "body": "Assignee: cwitty\n\nThis patch uses gcc's labels-as-values extension to (theoretically) speed up the instruction dispatch.  Unfortunately, on my 32-bit x86 laptop, it's about the same speed as before the patch (maybe a little slower).  I think this is due to poor instruction scheduling (that gcc can't fix with -fno-strict-aliasing), but trying to move the instructions around by hand makes the problem worse (it adds register pressure, which makes the register allocator do very bad things on 32-bit x86).\n\nDoctests do NOT pass, and the patch is not fully documented. (I believe the patch works; the doctests that fail are looking at fast_callable internals that changed.) \n\nIssue created by migration from https://trac.sagemath.org/ticket/5615\n\n",
    "created_at": "2009-03-26T06:55:34Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "[with patch, not ready for review] use labels-as-values for fast_callable under gcc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5615",
    "user": "cwitty"
}
```
Assignee: cwitty

This patch uses gcc's labels-as-values extension to (theoretically) speed up the instruction dispatch.  Unfortunately, on my 32-bit x86 laptop, it's about the same speed as before the patch (maybe a little slower).  I think this is due to poor instruction scheduling (that gcc can't fix with -fno-strict-aliasing), but trying to move the instructions around by hand makes the problem worse (it adds register pressure, which makes the register allocator do very bad things on 32-bit x86).

Doctests do NOT pass, and the patch is not fully documented. (I believe the patch works; the doctests that fail are looking at fast_callable internals that changed.) 

Issue created by migration from https://trac.sagemath.org/ticket/5615





---

archive/issue_comments_043852.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-26T06:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5615#issuecomment-43852",
    "user": "cwitty"
}
```

Attachment
