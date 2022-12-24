# Issue 4572: [with patch, needs review] maxima output has misleading precision

archive/issues_004572.json:
```json
{
    "body": "Assignee: burcin\n\nInternally, maxima uses floating point numbers internally unless explicitly told to use bigfloats (which we don't, and there's only one global precision in maxima so it will be non-trivial to try and do this consistantly). This patch changes the parsing code to use RDF instead, which is a better reflection of the underlying precision.\n\nIn addition, this has the benefit of removing the trailing zeros in calculus expressions involving real numbers (as they didn't really contain any information). \n\nIssue created by migration from https://trac.sagemath.org/ticket/4572\n\n",
    "created_at": "2008-11-20T22:00:37Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] maxima output has misleading precision",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4572",
    "user": "robertwb"
}
```
Assignee: burcin

Internally, maxima uses floating point numbers internally unless explicitly told to use bigfloats (which we don't, and there's only one global precision in maxima so it will be non-trivial to try and do this consistantly). This patch changes the parsing code to use RDF instead, which is a better reflection of the underlying precision.

In addition, this has the benefit of removing the trailing zeros in calculus expressions involving real numbers (as they didn't really contain any information). 

Issue created by migration from https://trac.sagemath.org/ticket/4572





---

archive/issue_comments_034257.json:
```json
{
    "body": "Attachment [4572-maxima-float.patch](tarball://root/attachments/some-uuid/ticket4572/4572-maxima-float.patch) by robertwb created at 2008-11-20 22:03:56",
    "created_at": "2008-11-20T22:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4572#issuecomment-34257",
    "user": "robertwb"
}
```

Attachment [4572-maxima-float.patch](tarball://root/attachments/some-uuid/ticket4572/4572-maxima-float.patch) by robertwb created at 2008-11-20 22:03:56



---

archive/issue_comments_034258.json:
```json
{
    "body": "Applies and passes tests.",
    "created_at": "2008-11-21T17:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4572#issuecomment-34258",
    "user": "mhansen"
}
```

Applies and passes tests.



---

archive/issue_comments_034259.json:
```json
{
    "body": "This patch seems to cause a boat load of small and annoying doctest failures:\n\n```\n        sage -t -long devel/sage/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/rings/real_rqdf.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/rings/real_double.pyx # 2 doctests failed\n        sage -t -long devel/sage/sage/rings/real_mpfr.pyx # 2 doctests failed\n        sage -t -long devel/sage/sage/rings/complex_double.pyx # 3 doctests failed\n        sage -t -long devel/sage/sage/plot/plot.py # 1 doctests failed\n        sage -t -long devel/sage/sage/misc/parser.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/misc/prandom.py # 1 doctests failed\n        sage -t -long devel/sage/sage/matrix/tests.py # 1 doctests failed\n        sage -t -long devel/sage/sage/interfaces/maxima.py # 3 doctests failed\n        sage -t -long devel/sage/sage/functions/special.py # 7 doctests failed\n        sage -t -long devel/sage/sage/functions/constants.py # 1 doctests failed\n        sage -t -long devel/sage/sage/functions/piecewise.py # 3 doctests failed\n        sage -t -long devel/doc/tut/tut.tex # 1 doctests failed\n```\n\nI will make 100% sure this can all be blamed on this patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T19:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4572#issuecomment-34259",
    "user": "mabshoff"
}
```

This patch seems to cause a boat load of small and annoying doctest failures:

```
        sage -t -long devel/sage/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/rings/real_rqdf.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/rings/real_double.pyx # 2 doctests failed
        sage -t -long devel/sage/sage/rings/real_mpfr.pyx # 2 doctests failed
        sage -t -long devel/sage/sage/rings/complex_double.pyx # 3 doctests failed
        sage -t -long devel/sage/sage/plot/plot.py # 1 doctests failed
        sage -t -long devel/sage/sage/misc/parser.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/misc/prandom.py # 1 doctests failed
        sage -t -long devel/sage/sage/matrix/tests.py # 1 doctests failed
        sage -t -long devel/sage/sage/interfaces/maxima.py # 3 doctests failed
        sage -t -long devel/sage/sage/functions/special.py # 7 doctests failed
        sage -t -long devel/sage/sage/functions/constants.py # 1 doctests failed
        sage -t -long devel/sage/sage/functions/piecewise.py # 3 doctests failed
        sage -t -long devel/doc/tut/tut.tex # 1 doctests failed
```

I will make 100% sure this can all be blamed on this patch.

Cheers,

Michael



---

archive/issue_comments_034260.json:
```json
{
    "body": "Yep, someone needs to fix those doctests :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T20:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4572#issuecomment-34260",
    "user": "mabshoff"
}
```

Yep, someone needs to fix those doctests :)

Cheers,

Michael



---

archive/issue_comments_034261.json:
```json
{
    "body": "Attachment [4572-maxima-float-fixes.patch](tarball://root/attachments/some-uuid/ticket4572/4572-maxima-float-fixes.patch) by robertwb created at 2008-11-25 11:26:57",
    "created_at": "2008-11-25T11:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4572#issuecomment-34261",
    "user": "robertwb"
}
```

Attachment [4572-maxima-float-fixes.patch](tarball://root/attachments/some-uuid/ticket4572/4572-maxima-float-fixes.patch) by robertwb created at 2008-11-25 11:26:57



---

archive/issue_comments_034262.json:
```json
{
    "body": "Attachment [4572-maxima-float-fixes-tut.patch](tarball://root/attachments/some-uuid/ticket4572/4572-maxima-float-fixes-tut.patch) by robertwb created at 2008-11-25 11:27:21\n\napply to docs repo",
    "created_at": "2008-11-25T11:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4572#issuecomment-34262",
    "user": "robertwb"
}
```

Attachment [4572-maxima-float-fixes-tut.patch](tarball://root/attachments/some-uuid/ticket4572/4572-maxima-float-fixes-tut.patch) by robertwb created at 2008-11-25 11:27:21

apply to docs repo



---

archive/issue_comments_034263.json:
```json
{
    "body": "All doctest failures were due to precision printing differences. Apply all attached patches.",
    "created_at": "2008-11-25T11:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4572#issuecomment-34263",
    "user": "robertwb"
}
```

All doctest failures were due to precision printing differences. Apply all attached patches.



---

archive/issue_comments_034264.json:
```json
{
    "body": "Positive review to the doctest fixes, so a cumulative positive review :)\n\nCheers,\n\nMichae",
    "created_at": "2008-11-25T11:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4572#issuecomment-34264",
    "user": "mabshoff"
}
```

Positive review to the doctest fixes, so a cumulative positive review :)

Cheers,

Michae



---

archive/issue_comments_034265.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-25T12:29:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4572#issuecomment-34265",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034266.json:
```json
{
    "body": "Merged both patches in Sage 3.2.1.alpha1",
    "created_at": "2008-11-25T12:29:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4572#issuecomment-34266",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.1.alpha1
