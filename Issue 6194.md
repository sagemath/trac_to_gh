# Issue 6194: [with patch, needs review] fixes for sage.symbolic.pynac.py_mod

archive/issues_006194.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  mhansen\n\nOur version of GiNaC's mod function doesn't match the behavior of the original and fails silently when there is an error. This stops some simplifications such as `exp(2*pi*I) -> 1` to work.\n\nAttached patch fixes these issues.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6194\n\n",
    "created_at": "2009-06-03T15:16:05Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] fixes for sage.symbolic.pynac.py_mod",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6194",
    "user": "burcin"
}
```
Assignee: burcin

CC:  mhansen

Our version of GiNaC's mod function doesn't match the behavior of the original and fails silently when there is an error. This stops some simplifications such as `exp(2*pi*I) -> 1` to work.

Attached patch fixes these issues.

Issue created by migration from https://trac.sagemath.org/ticket/6194





---

archive/issue_comments_049469.json:
```json
{
    "body": "Attachment [trac_6194-pynac_py_mod.patch](tarball://root/attachments/some-uuid/ticket6194/trac_6194-pynac_py_mod.patch) by burcin created at 2009-06-03 15:17:33\n\nfix to sage.symbolic.pynac.py_mod",
    "created_at": "2009-06-03T15:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6194#issuecomment-49469",
    "user": "burcin"
}
```

Attachment [trac_6194-pynac_py_mod.patch](tarball://root/attachments/some-uuid/ticket6194/trac_6194-pynac_py_mod.patch) by burcin created at 2009-06-03 15:17:33

fix to sage.symbolic.pynac.py_mod



---

archive/issue_comments_049470.json:
```json
{
    "body": "Looks good to me.\n\nMerged in 4.0.1.rc2.",
    "created_at": "2009-06-05T02:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6194#issuecomment-49470",
    "user": "mhansen"
}
```

Looks good to me.

Merged in 4.0.1.rc2.



---

archive/issue_comments_049471.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-05T02:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6194#issuecomment-49471",
    "user": "mhansen"
}
```

Resolution: fixed
