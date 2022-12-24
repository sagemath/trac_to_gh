# Issue 538: remove code duplication between sage/ext and c_lib

archive/issues_000538.json:
```json
{
    "body": "Assignee: @williamstein\n\nSome code duplication appeared as a result of the fix to #411. Remove all of the sage/ext stuff that now appears in `c_lib`.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/538\n\n",
    "created_at": "2007-08-31T01:19:10Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "remove code duplication between sage/ext and c_lib",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/538",
    "user": "dmharvey"
}
```
Assignee: @williamstein

Some code duplication appeared as a result of the fix to #411. Remove all of the sage/ext stuff that now appears in `c_lib`.


Issue created by migration from https://trac.sagemath.org/ticket/538





---

archive/issue_comments_002739.json:
```json
{
    "body": "the `c_lib` directory in 2.8.3.rc4 also has a spurious .so file in it, which should be removed",
    "created_at": "2007-08-31T01:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/538#issuecomment-2739",
    "user": "dmharvey"
}
```

the `c_lib` directory in 2.8.3.rc4 also has a spurious .so file in it, which should be removed



---

archive/issue_comments_002740.json:
```json
{
    "body": "I think I've fixed this, though I'd like to test it on more architectures just to make sure. The hg bundle is available at:\n\nhttp://sage.math.washington.edu/home/citro/patches/c_lib_fixes.hg\n\nI'll also try to attach it to this ticket, but we'll see. Let me know if anyone runs into trouble with this.",
    "created_at": "2007-09-01T06:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/538#issuecomment-2740",
    "user": "@craigcitro"
}
```

I think I've fixed this, though I'd like to test it on more architectures just to make sure. The hg bundle is available at:

http://sage.math.washington.edu/home/citro/patches/c_lib_fixes.hg

I'll also try to attach it to this ticket, but we'll see. Let me know if anyone runs into trouble with this.



---

archive/issue_comments_002741.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2007-09-01T06:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/538#issuecomment-2741",
    "user": "@craigcitro"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_002742.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-01T17:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/538#issuecomment-2742",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_002743.json:
```json
{
    "body": "Attachment [c_lib_fixes.hg](tarball://root/attachments/some-uuid/ticket538/c_lib_fixes.hg) by @williamstein created at 2007-09-01 17:45:45",
    "created_at": "2007-09-01T17:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/538#issuecomment-2743",
    "user": "@williamstein"
}
```

Attachment [c_lib_fixes.hg](tarball://root/attachments/some-uuid/ticket538/c_lib_fixes.hg) by @williamstein created at 2007-09-01 17:45:45
