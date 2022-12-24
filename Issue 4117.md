# Issue 4117: number_field_* leaks caused by gen.pyx's type(gen self)

archive/issues_004117.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe leak medium to massive amount of memory in a lot of number field related code. This is caused by\n\n```\n     def type(gen self):\n        return str(type_name(typ(self.g)))\n```\n\nin gen.pyx. The regular and obvious fix causes segfualts in other places (i.e. due to integer.pyx), so I am attaching a workaround fix that has some performance penalty.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4117\n\n",
    "created_at": "2008-09-14T09:54:26Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "number_field_* leaks caused by gen.pyx's type(gen self)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4117",
    "user": "mabshoff"
}
```
Assignee: mabshoff

We leak medium to massive amount of memory in a lot of number field related code. This is caused by

```
     def type(gen self):
        return str(type_name(typ(self.g)))
```

in gen.pyx. The regular and obvious fix causes segfualts in other places (i.e. due to integer.pyx), so I am attaching a workaround fix that has some performance penalty.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4117





---

archive/issue_comments_029811.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-14T09:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4117#issuecomment-29811",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029812.json:
```json
{
    "body": "Attachment [trac_4117.patch](tarball://root/attachments/some-uuid/ticket4117/trac_4117.patch) by mabshoff created at 2008-09-14 09:55:26\n\nThis is a diff with some work around code",
    "created_at": "2008-09-14T09:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4117#issuecomment-29812",
    "user": "mabshoff"
}
```

Attachment [trac_4117.patch](tarball://root/attachments/some-uuid/ticket4117/trac_4117.patch) by mabshoff created at 2008-09-14 09:55:26

This is a diff with some work around code



---

archive/issue_comments_029813.json:
```json
{
    "body": "Different fix for the same problem",
    "created_at": "2008-09-14T10:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4117#issuecomment-29813",
    "user": "craigcitro"
}
```

Different fix for the same problem



---

archive/issue_comments_029814.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-14T11:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4117#issuecomment-29814",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029815.json:
```json
{
    "body": "Attachment [trac-4117.patch](tarball://root/attachments/some-uuid/ticket4117/trac-4117.patch) by mabshoff created at 2008-09-14 11:02:46\n\nMerged trac-4117.patch in Sage 3.1.2.rc3",
    "created_at": "2008-09-14T11:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4117#issuecomment-29815",
    "user": "mabshoff"
}
```

Attachment [trac-4117.patch](tarball://root/attachments/some-uuid/ticket4117/trac-4117.patch) by mabshoff created at 2008-09-14 11:02:46

Merged trac-4117.patch in Sage 3.1.2.rc3



---

archive/issue_comments_029816.json:
```json
{
    "body": "I wonder why this was a memleak. The original code looks correct, so either there was a bug in PARI/GP, a bug in Cython or a mis-identified memleak.\n\nAfter 9 years, I am reverting this is in https://github.com/defeo/cypari2/commit/8f8ec558fd2864ea72f10068ed4f11843731199d",
    "created_at": "2017-09-19T13:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4117#issuecomment-29816",
    "user": "jdemeyer"
}
```

I wonder why this was a memleak. The original code looks correct, so either there was a bug in PARI/GP, a bug in Cython or a mis-identified memleak.

After 9 years, I am reverting this is in https://github.com/defeo/cypari2/commit/8f8ec558fd2864ea72f10068ed4f11843731199d
