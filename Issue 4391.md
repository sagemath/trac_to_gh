# Issue 4391: [with patch, needs review] Sage 3.1.4: optional doctest failure in sage/schemes/elliptic_curves/ell_finite_field.py

archive/issues_004391.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t -long -optional devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/ell_finite_field.py\", line 102:\n    sage: magma(E) # optional -- requires Magma\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[3]>\", line 1, in <module>\n        magma(E) # optional -- requires Magma###line 102:\n    sage: magma(E) # optional -- requires Magma\n    NameError: name 'E' is not defined\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4391\n\n",
    "created_at": "2008-10-30T06:41:42Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] Sage 3.1.4: optional doctest failure in sage/schemes/elliptic_curves/ell_finite_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4391",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
sage -t -long -optional devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/ell_finite_field.py", line 102:
    sage: magma(E) # optional -- requires Magma
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        magma(E) # optional -- requires Magma###line 102:
    sage: magma(E) # optional -- requires Magma
    NameError: name 'E' is not defined
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4391





---

archive/issue_comments_032315.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-30T06:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4391#issuecomment-32315",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032316.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-10-30T07:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4391#issuecomment-32316",
    "user": "@craigcitro"
}
```

Looks good.



---

archive/issue_comments_032317.json:
```json
{
    "body": "I had to rebase t my own patch for Saeg 3.2.alpha1, oh well :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T07:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4391#issuecomment-32317",
    "user": "mabshoff"
}
```

I had to rebase t my own patch for Saeg 3.2.alpha1, oh well :)

Cheers,

Michael



---

archive/issue_comments_032318.json:
```json
{
    "body": "Attachment [trac_4391.patch](tarball://root/attachments/some-uuid/ticket4391/trac_4391.patch) by mabshoff created at 2008-10-30 07:42:24",
    "created_at": "2008-10-30T07:42:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4391#issuecomment-32318",
    "user": "mabshoff"
}
```

Attachment [trac_4391.patch](tarball://root/attachments/some-uuid/ticket4391/trac_4391.patch) by mabshoff created at 2008-10-30 07:42:24



---

archive/issue_comments_032319.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-30T07:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4391#issuecomment-32319",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032320.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-30T07:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4391#issuecomment-32320",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2
