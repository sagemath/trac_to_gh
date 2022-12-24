# Issue 5045: sage's "make check" should check that the sage build flags (in sage-flags.txt) are right

archive/issues_005045.json:
```json
{
    "body": "Assignee: mabshoff\n\nSome people do \"make check\" but never even try to run sage.  Thus it is stupid that make check can run without ever verifying that sage-flags.txt is valid.  If it isn't, just stop the check.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5045\n\n",
    "created_at": "2009-01-21T06:00:52Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "sage's \"make check\" should check that the sage build flags (in sage-flags.txt) are right",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5045",
    "user": "was"
}
```
Assignee: mabshoff

Some people do "make check" but never even try to run sage.  Thus it is stupid that make check can run without ever verifying that sage-flags.txt is valid.  If it isn't, just stop the check.

Issue created by migration from https://trac.sagemath.org/ticket/5045





---

archive/issue_comments_038424.json:
```json
{
    "body": "Attachment [trac_5045_scripts-rep.patch](tarball://root/attachments/some-uuid/ticket5045/trac_5045_scripts-rep.patch) by was created at 2009-01-22 10:10:18",
    "created_at": "2009-01-22T10:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5045#issuecomment-38424",
    "user": "was"
}
```

Attachment [trac_5045_scripts-rep.patch](tarball://root/attachments/some-uuid/ticket5045/trac_5045_scripts-rep.patch) by was created at 2009-01-22 10:10:18



---

archive/issue_comments_038425.json:
```json
{
    "body": "To test this, edit SAGE_ROOT/local/lib/sage-flags.txt and add some madeup flags like x.  Then test by doing, e.g., \n\n```\nmake check\n```\n\nand seeing that the build process properly stops.",
    "created_at": "2009-01-22T10:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5045#issuecomment-38425",
    "user": "was"
}
```

To test this, edit SAGE_ROOT/local/lib/sage-flags.txt and add some madeup flags like x.  Then test by doing, e.g., 

```
make check
```

and seeing that the build process properly stops.



---

archive/issue_comments_038426.json:
```json
{
    "body": "Nice.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-22T10:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5045#issuecomment-38426",
    "user": "mabshoff"
}
```

Nice.

Cheers,

Michael



---

archive/issue_comments_038427.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T08:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5045#issuecomment-38427",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_comments_038428.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T08:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5045#issuecomment-38428",
    "user": "mabshoff"
}
```

Resolution: fixed
