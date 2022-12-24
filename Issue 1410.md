# Issue 1410: fix leftover issues from removal of mwrank.spkg

archive/issues_001410.json:
```json
{
    "body": "Assignee: mabshoff\n\nToDo:\n* delete $SAGE_LOCAL/include/mwrank\n* strip the mwrank binaries? Also make them link dynamically?\n  mwrank unstripped: 12 mb, stripped 2.2MB\n* delete $SAGE_LOCAL/lib/libmwrank.[so|dylib]\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1410\n\n",
    "created_at": "2007-12-06T13:17:34Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "fix leftover issues from removal of mwrank.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1410",
    "user": "mabshoff"
}
```
Assignee: mabshoff

ToDo:
* delete $SAGE_LOCAL/include/mwrank
* strip the mwrank binaries? Also make them link dynamically?
  mwrank unstripped: 12 mb, stripped 2.2MB
* delete $SAGE_LOCAL/lib/libmwrank.[so|dylib]

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1410





---

archive/issue_comments_009096.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T13:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1410#issuecomment-9096",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009097.json:
```json
{
    "body": "As far as I can tell the spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/cremona-20071124.p4.spkg\n\nfixes all the above issues. But it certainly can stand some more testing.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-06T16:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1410#issuecomment-9097",
    "user": "mabshoff"
}
```

As far as I can tell the spkg at

http://sage.math.washington.edu/home/mabshoff/cremona-20071124.p4.spkg

fixes all the above issues. But it certainly can stand some more testing.

Cheers,

Michael



---

archive/issue_comments_009098.json:
```json
{
    "body": "The patch isn't very clean, but it works ;)",
    "created_at": "2007-12-06T16:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1410#issuecomment-9098",
    "user": "mabshoff"
}
```

The patch isn't very clean, but it works ;)



---

archive/issue_comments_009099.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T17:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1410#issuecomment-9099",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009100.json:
```json
{
    "body": "Attachment [cremona-link-binaries-dynamically.patch](tarball://root/attachments/some-uuid/ticket1410/cremona-link-binaries-dynamically.patch) by mabshoff created at 2007-12-06 17:46:59\n\nMerged in 2.9.alpha1. Doctests and builds fine in Linux and OSX.",
    "created_at": "2007-12-06T17:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1410#issuecomment-9100",
    "user": "mabshoff"
}
```

Attachment [cremona-link-binaries-dynamically.patch](tarball://root/attachments/some-uuid/ticket1410/cremona-link-binaries-dynamically.patch) by mabshoff created at 2007-12-06 17:46:59

Merged in 2.9.alpha1. Doctests and builds fine in Linux and OSX.
