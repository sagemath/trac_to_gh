# Issue 3365: [with patch; needs review] add a %c mode to the notebook (like %fortran)

archive/issues_003365.json:
```json
{
    "body": "Assignee: cwitty\n\nMichael Schmitz -- a student in Math 480 -- created this code.  It makes it so you can do %c in a notebook cell and write pure C functions.  Very fun.  E.g., \n\n\n```\n%c\nint foo(int a, int b) { return(a*b);}\n```\n\n\n\n```\nfoo(2r,3r)\n///\n6\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3365\n\n",
    "created_at": "2008-06-04T18:39:54Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] add a %c mode to the notebook (like %fortran)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3365",
    "user": "was"
}
```
Assignee: cwitty

Michael Schmitz -- a student in Math 480 -- created this code.  It makes it so you can do %c in a notebook cell and write pure C functions.  Very fun.  E.g., 


```
%c
int foo(int a, int b) { return(a*b);}
```



```
foo(2r,3r)
///
6
```


Issue created by migration from https://trac.sagemath.org/ticket/3365





---

archive/issue_comments_023545.json:
```json
{
    "body": "Attachment [sage-3365.patch](tarball://root/attachments/some-uuid/ticket3365/sage-3365.patch) by was created at 2008-06-04 18:42:38",
    "created_at": "2008-06-04T18:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3365#issuecomment-23545",
    "user": "was"
}
```

Attachment [sage-3365.patch](tarball://root/attachments/some-uuid/ticket3365/sage-3365.patch) by was created at 2008-06-04 18:42:38



---

archive/issue_comments_023546.json:
```json
{
    "body": "this satandard python package must be installed with ' sage -python setup.py install'",
    "created_at": "2008-06-04T18:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3365#issuecomment-23546",
    "user": "was"
}
```

this satandard python package must be installed with ' sage -python setup.py install'



---

archive/issue_comments_023547.json:
```json
{
    "body": "Attachment [py_inline-0.03.tar.bz2](tarball://root/attachments/some-uuid/ticket3365/py_inline-0.03.tar.bz2) by was created at 2008-06-04 18:45:22",
    "created_at": "2008-06-04T18:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3365#issuecomment-23547",
    "user": "was"
}
```

Attachment [py_inline-0.03.tar.bz2](tarball://root/attachments/some-uuid/ticket3365/py_inline-0.03.tar.bz2) by was created at 2008-06-04 18:45:22



---

archive/issue_comments_023548.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-06-09T03:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3365#issuecomment-23548",
    "user": "TimothyClemans"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_023549.json:
```json
{
    "body": "This works on sage.math and doctests for c.py pass.",
    "created_at": "2008-06-09T03:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3365#issuecomment-23549",
    "user": "TimothyClemans"
}
```

This works on sage.math and doctests for c.py pass.



---

archive/issue_comments_023550.json:
```json
{
    "body": "Do we really want to merge this as is since we are adding a new python package? Creating a new spkg for 10kb Python code also seems like a waste\n\nThoughts?\n\n\nCheers,\n\nMichael",
    "created_at": "2008-06-09T06:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3365#issuecomment-23550",
    "user": "mabshoff"
}
```

Do we really want to merge this as is since we are adding a new python package? Creating a new spkg for 10kb Python code also seems like a waste

Thoughts?


Cheers,

Michael



---

archive/issue_comments_023551.json:
```json
{
    "body": "Attachment [fixedtheproblem.zip](tarball://root/attachments/some-uuid/ticket3365/fixedtheproblem.zip) by was created at 2008-06-09 20:56:30\n\nthis zip file contains both the patch and the new to-be-made spkg; it replaces the previous attached patches",
    "created_at": "2008-06-09T20:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3365#issuecomment-23551",
    "user": "was"
}
```

Attachment [fixedtheproblem.zip](tarball://root/attachments/some-uuid/ticket3365/fixedtheproblem.zip) by was created at 2008-06-09 20:56:30

this zip file contains both the patch and the new to-be-made spkg; it replaces the previous attached patches



---

archive/issue_comments_023552.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-06-20T05:01:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3365#issuecomment-23552",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_wstein".
