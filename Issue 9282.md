# Issue 9282: Sage doctest failures

archive/issues_009282.json:
```json
{
    "body": "Assignee: mvngu\n\nsage -testall fails at:\n\nsage -t \u00a0\"devel/sage/sage/modular/hecke/submodule.py\"\n\nsage -t \u00a0\"devel/sage/sage/modular/abvar/abvar.py\"\n\nsage -t \u00a0\"devel/sage/sage/lfunctions/sympow.py\"\n\nsage -t \u00a0\"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"\n\nsage -t \u00a0\"devel/sage/sage/interfaces/qepcad.py\"\n\n\n\nCompiled with: GCC 4.5.0\n\nDistribution: Arch Linux 32 bit\n\nIssue created by migration from https://trac.sagemath.org/ticket/9282\n\n",
    "created_at": "2010-06-20T12:58:22Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage doctest failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9282",
    "user": "retry"
}
```
Assignee: mvngu

sage -testall fails at:

sage -t  "devel/sage/sage/modular/hecke/submodule.py"

sage -t  "devel/sage/sage/modular/abvar/abvar.py"

sage -t  "devel/sage/sage/lfunctions/sympow.py"

sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"

sage -t  "devel/sage/sage/interfaces/qepcad.py"



Compiled with: GCC 4.5.0

Distribution: Arch Linux 32 bit

Issue created by migration from https://trac.sagemath.org/ticket/9282





---

archive/issue_comments_087441.json:
```json
{
    "body": "sage -testall log, with tracebacks.",
    "created_at": "2010-06-20T12:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9282#issuecomment-87441",
    "user": "retry"
}
```

sage -testall log, with tracebacks.



---

archive/issue_comments_087442.json:
```json
{
    "body": "Attachment [test.log](tarball://root/attachments/some-uuid/ticket9282/test.log) by retry created at 2010-06-22 07:45:38\n\nRecompiled sage - no more problems.",
    "created_at": "2010-06-22T07:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9282#issuecomment-87442",
    "user": "retry"
}
```

Attachment [test.log](tarball://root/attachments/some-uuid/ticket9282/test.log) by retry created at 2010-06-22 07:45:38

Recompiled sage - no more problems.



---

archive/issue_comments_087443.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-06-22T07:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9282#issuecomment-87443",
    "user": "retry"
}
```

Resolution: invalid
