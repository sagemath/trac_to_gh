# Issue 2715: sage -coverage currently counts functions that are defined in doctests

archive/issues_002715.json:
```json
{
    "body": "Assignee: cwitty\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2715\n\n",
    "created_at": "2008-03-29T02:41:45Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "title": "sage -coverage currently counts functions that are defined in doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2715",
    "user": "mhansen"
}
```
Assignee: cwitty



Issue created by migration from https://trac.sagemath.org/ticket/2715





---

archive/issue_comments_018711.json:
```json
{
    "body": "Attachment [2715.patch](tarball://root/attachments/some-uuid/ticket2715/2715.patch) by mhansen created at 2008-03-29 02:42:50",
    "created_at": "2008-03-29T02:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2715#issuecomment-18711",
    "user": "mhansen"
}
```

Attachment [2715.patch](tarball://root/attachments/some-uuid/ticket2715/2715.patch) by mhansen created at 2008-03-29 02:42:50



---

archive/issue_comments_018712.json:
```json
{
    "body": "Looks good.  (I looked at the diff of coverage runs before and after the patch, and it looks like it works correctly; and raises coverage 0.2%.  There is at least one function it should ignore but does not: \"mumble\" in sage/misc/python.py; I looked at fixing this but couldn't see an easy fix.  Anyway, the patch is definitely an improvement and should be applied.)",
    "created_at": "2008-03-29T21:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2715#issuecomment-18712",
    "user": "cwitty"
}
```

Looks good.  (I looked at the diff of coverage runs before and after the patch, and it looks like it works correctly; and raises coverage 0.2%.  There is at least one function it should ignore but does not: "mumble" in sage/misc/python.py; I looked at fixing this but couldn't see an easy fix.  Anyway, the patch is definitely an improvement and should be applied.)



---

archive/issue_comments_018713.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T21:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2715#issuecomment-18713",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.rc0



---

archive/issue_comments_018714.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T21:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2715#issuecomment-18714",
    "user": "mabshoff"
}
```

Resolution: fixed
