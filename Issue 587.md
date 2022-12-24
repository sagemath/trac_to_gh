# Issue 587: bug in floating point complex number creation

archive/issues_000587.json:
```json
{
    "body": "Assignee: somebody\n\nThis was found by Markus Fraczek:\n\n```\nsage: 1e8\n100000000.000000\nsage: 1e8*I\nboom -- typeerror\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/587\n\n",
    "created_at": "2007-09-04T15:16:50Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "bug in floating point complex number creation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/587",
    "user": "@williamstein"
}
```
Assignee: somebody

This was found by Markus Fraczek:

```
sage: 1e8
100000000.000000
sage: 1e8*I
boom -- typeerror
```


Issue created by migration from https://trac.sagemath.org/ticket/587





---

archive/issue_comments_003025.json:
```json
{
    "body": "Changing assignee from somebody to @mwhansen.",
    "created_at": "2007-09-04T19:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/587#issuecomment-3025",
    "user": "@mwhansen"
}
```

Changing assignee from somebody to @mwhansen.



---

archive/issue_comments_003026.json:
```json
{
    "body": "There problem was that SAGE doesn't like strings such as \"1.0E+8*I\" in symbolic_expression_from_maxima_string() , and the fix to replace all such occurrences of scientific notation with expanded notation (or at least on that doesn't involved pluses.\n\n587.patch patches the calculus.py file.\n587-2.patches adds the problem as a doctest",
    "created_at": "2007-09-04T19:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/587#issuecomment-3026",
    "user": "@mwhansen"
}
```

There problem was that SAGE doesn't like strings such as "1.0E+8*I" in symbolic_expression_from_maxima_string() , and the fix to replace all such occurrences of scientific notation with expanded notation (or at least on that doesn't involved pluses.

587.patch patches the calculus.py file.
587-2.patches adds the problem as a doctest



---

archive/issue_comments_003027.json:
```json
{
    "body": "patch for calculus.py",
    "created_at": "2007-09-04T19:37:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/587#issuecomment-3027",
    "user": "@mwhansen"
}
```

patch for calculus.py



---

archive/issue_comments_003028.json:
```json
{
    "body": "Attachment [587-2.patch](tarball://root/attachments/some-uuid/ticket587/587-2.patch) by @mwhansen created at 2007-09-04 19:37:42\n\npatch for constants.py",
    "created_at": "2007-09-04T19:37:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/587#issuecomment-3028",
    "user": "@mwhansen"
}
```

Attachment [587-2.patch](tarball://root/attachments/some-uuid/ticket587/587-2.patch) by @mwhansen created at 2007-09-04 19:37:42

patch for constants.py



---

archive/issue_comments_003029.json:
```json
{
    "body": "fixed by mike hansen.",
    "created_at": "2007-09-04T21:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/587#issuecomment-3029",
    "user": "@williamstein"
}
```

fixed by mike hansen.



---

archive/issue_comments_003030.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-04T21:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/587#issuecomment-3030",
    "user": "@williamstein"
}
```

Resolution: fixed
