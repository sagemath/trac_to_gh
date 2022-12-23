# Issue 4224: small error in new question-mark interval printing

archive/issues_004224.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  jason\n\nSome intervals were printing incorrectly in question-mark style (the printed result didn't always include the lower bound of the interval), as reported here: http://groups.google.com/group/sage-support/browse_thread/thread/844cde94499c42a1#\n\n(Thanks to Pong for reporting the problem, and Jason Grout for bringing it to my attention!)\n\nIt turns out that this is a single-character fix: I had RNDN (round-to-nearest) where I needed RNDD (round-down).  Unfortunately, lots of doctests recorded incorrect printing, so the actual patch is almost entirely doctest fixes.\n\nThis patch against 3.1.2 passes -testall.  I hand-checked several (but not all) of the doctest changes against .str(style='brackets').\n\nIssue created by migration from https://trac.sagemath.org/ticket/4224\n\n",
    "created_at": "2008-09-30T19:09:41Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "small error in new question-mark interval printing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4224",
    "user": "cwitty"
}
```
Assignee: cwitty

CC:  jason

Some intervals were printing incorrectly in question-mark style (the printed result didn't always include the lower bound of the interval), as reported here: http://groups.google.com/group/sage-support/browse_thread/thread/844cde94499c42a1#

(Thanks to Pong for reporting the problem, and Jason Grout for bringing it to my attention!)

It turns out that this is a single-character fix: I had RNDN (round-to-nearest) where I needed RNDD (round-down).  Unfortunately, lots of doctests recorded incorrect printing, so the actual patch is almost entirely doctest fixes.

This patch against 3.1.2 passes -testall.  I hand-checked several (but not all) of the doctest changes against .str(style='brackets').

Issue created by migration from https://trac.sagemath.org/ticket/4224





---

archive/issue_comments_030698.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-09-30T19:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4224",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4224#issuecomment-30698",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_030699.json:
```json
{
    "body": "Carl, \n\nI observed the following failure on a Core2 Quad running Solaris:\n\n```\nsage -t  devel/sage/sage/rings/qqbar.py                     \n**********************************************************************\nFile \"/home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/tmp/qqbar.py\", line 3770:\n    sage: cp.complex_roots(30, 1)\nExpected:\n    [1.189207115002721?,\n     -1.189207115002721?,\n     1.189207115002721?*I,\n     -1.189207115002721?*I]\nGot:\n    [1.189207115002721?, -1.1892071150027211?, 1.189207115002721?*I, -1.189207115002721?*I]\n**********************************************************************\n```\n\nCould this be related to this issue? I am reviewing the patch and will see what is going on on Solaris once I build 3.1.3 on it.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-01T10:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4224",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4224#issuecomment-30699",
    "user": "mabshoff"
}
```

Carl, 

I observed the following failure on a Core2 Quad running Solaris:

```
sage -t  devel/sage/sage/rings/qqbar.py                     
**********************************************************************
File "/home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/tmp/qqbar.py", line 3770:
    sage: cp.complex_roots(30, 1)
Expected:
    [1.189207115002721?,
     -1.189207115002721?,
     1.189207115002721?*I,
     -1.189207115002721?*I]
Got:
    [1.189207115002721?, -1.1892071150027211?, 1.189207115002721?*I, -1.189207115002721?*I]
**********************************************************************
```

Could this be related to this issue? I am reviewing the patch and will see what is going on on Solaris once I build 3.1.3 on it.

Cheers,

Michael



---

archive/issue_comments_030700.json:
```json
{
    "body": "Patch is good and passes doctests. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-01T11:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4224",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4224#issuecomment-30700",
    "user": "mabshoff"
}
```

Patch is good and passes doctests. Positive review.

Cheers,

Michael



---

archive/issue_comments_030701.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-01T11:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4224",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4224#issuecomment-30701",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030702.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha3",
    "created_at": "2008-10-01T11:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4224",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4224#issuecomment-30702",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha3



---

archive/issue_comments_030703.json:
```json
{
    "body": "I also looked at this patch, for the record, and it looked reasonable.  I did not have time to apply it and check it, though.",
    "created_at": "2008-10-01T16:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4224",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4224#issuecomment-30703",
    "user": "jason"
}
```

I also looked at this patch, for the record, and it looked reasonable.  I did not have time to apply it and check it, though.
