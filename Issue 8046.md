# Issue 8046: Add matrix/matrix_double_dense.py to documentation

archive/issues_008046.json:
```json
{
    "body": "Assignee: mvngu\n\nThe source file `matrix/matrix_double_dense.py` is not included in the documentation.  It appears that it should be, since it has functions that are of interest to users.  Patch simply adds it to the right place in the documentation tree.\n\nThe file itself needs some love.  After #4756 goes in, the following four functions should be in good shape.  The remainder needs work.\n\n\n```\nleft_eigenvectors()\nright_eigenvectors()\neigenspaces_left()\neigenspaces_right()\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8046\n\n",
    "created_at": "2010-01-23T23:03:56Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "Add matrix/matrix_double_dense.py to documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8046",
    "user": "rbeezer"
}
```
Assignee: mvngu

The source file `matrix/matrix_double_dense.py` is not included in the documentation.  It appears that it should be, since it has functions that are of interest to users.  Patch simply adds it to the right place in the documentation tree.

The file itself needs some love.  After #4756 goes in, the following four functions should be in good shape.  The remainder needs work.


```
left_eigenvectors()
right_eigenvectors()
eigenspaces_left()
eigenspaces_right()
```


Issue created by migration from https://trac.sagemath.org/ticket/8046





---

archive/issue_comments_070325.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2011-02-24T05:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8046#issuecomment-70325",
    "user": "jason"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_070326.json:
```json
{
    "body": "Attachment [trac_8046_matrix_double_doc_add.patch](tarball://root/attachments/some-uuid/ticket8046/trac_8046_matrix_double_doc_add.patch) by jason created at 2011-02-24 05:47:58\n\nI get some errors on 4.6.1 when building the docs:\n\n\n```\ndocstring of sage.matrix.matrix_double_dense.Matrix_double_dense.condition:11: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\ndocstring of sage.matrix.matrix_double_dense:7: (ERROR/3) Unexpected indentation.\ndocstring of sage.matrix.matrix_double_dense.Matrix_double_dense.numpy:11: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\ndocstring of sage.matrix.matrix_double_dense:13: (ERROR/3) Unexpected indentation.\ndocstring of sage.matrix.matrix_double_dense:13: (ERROR/3) Unexpected indentation.\n<autodoc>:0: (ERROR/3) Unexpected indentation.\n```\n",
    "created_at": "2011-02-24T05:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8046#issuecomment-70326",
    "user": "jason"
}
```

Attachment [trac_8046_matrix_double_doc_add.patch](tarball://root/attachments/some-uuid/ticket8046/trac_8046_matrix_double_doc_add.patch) by jason created at 2011-02-24 05:47:58

I get some errors on 4.6.1 when building the docs:


```
docstring of sage.matrix.matrix_double_dense.Matrix_double_dense.condition:11: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
docstring of sage.matrix.matrix_double_dense:7: (ERROR/3) Unexpected indentation.
docstring of sage.matrix.matrix_double_dense.Matrix_double_dense.numpy:11: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
docstring of sage.matrix.matrix_double_dense:13: (ERROR/3) Unexpected indentation.
docstring of sage.matrix.matrix_double_dense:13: (ERROR/3) Unexpected indentation.
<autodoc>:0: (ERROR/3) Unexpected indentation.
```




---

archive/issue_comments_070327.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n\nYes, the file \"needs_work\".  I went through it a couple days ago and cleaned up lots of little things (documentation mostly), but then went off and made a few patches with code changes.  I'll get back to it very soon and insert into the other work I'm doing.",
    "created_at": "2011-02-24T06:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8046#issuecomment-70327",
    "user": "rbeezer"
}
```

Replying to [comment:1 jason]:

Yes, the file "needs_work".  I went through it a couple days ago and cleaned up lots of little things (documentation mostly), but then went off and made a few patches with code changes.  I'll get back to it very soon and insert into the other work I'm doing.



---

archive/issue_comments_070328.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner sd35.5\".",
    "created_at": "2012-01-11T16:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8046#issuecomment-70328",
    "user": "kcrisman"
}
```

Changing keywords from "" to "beginner sd35.5".



---

archive/issue_comments_070329.json:
```json
{
    "body": "I made a new patch. This one includes the matrix double dense to the documentation like the last one, and it also edits the file a lot to get rid of almost all of the syntax errors. I am still getting 2 warnings however:\n\nOne is:\n\ndocstring of sage.matrix.matrix_double_dense:8: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n\nI cannot, however find what the error message is talking about, even after multiple people examined it for quite a while.\n\nThe other one is:\n\nWARNING: dvipng command 'dvipng' cannot be run (needed for math display), check the pngmath_dvipng setting\n\nwhich I am told can be ignored.\n\nSo really there is just one warning that could still be fixed.",
    "created_at": "2012-01-11T20:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8046#issuecomment-70329",
    "user": "ksmith"
}
```

I made a new patch. This one includes the matrix double dense to the documentation like the last one, and it also edits the file a lot to get rid of almost all of the syntax errors. I am still getting 2 warnings however:

One is:

docstring of sage.matrix.matrix_double_dense:8: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.

I cannot, however find what the error message is talking about, even after multiple people examined it for quite a while.

The other one is:

WARNING: dvipng command 'dvipng' cannot be run (needed for math display), check the pngmath_dvipng setting

which I am told can be ignored.

So really there is just one warning that could still be fixed.



---

archive/issue_comments_070330.json:
```json
{
    "body": "Attachment [trac_8046_matrix_double_dense.patch](tarball://root/attachments/some-uuid/ticket8046/trac_8046_matrix_double_dense.patch) by jhpalmieri created at 2012-01-12 06:42:50\n\nI'm attaching a 'referee' patch to fix up some docstrings.  The first change in that patch fixes the warning message about the unexpected unindent; the others just tidy some things up.",
    "created_at": "2012-01-12T06:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8046#issuecomment-70330",
    "user": "jhpalmieri"
}
```

Attachment [trac_8046_matrix_double_dense.patch](tarball://root/attachments/some-uuid/ticket8046/trac_8046_matrix_double_dense.patch) by jhpalmieri created at 2012-01-12 06:42:50

I'm attaching a 'referee' patch to fix up some docstrings.  The first change in that patch fixes the warning message about the unexpected unindent; the others just tidy some things up.



---

archive/issue_comments_070331.json:
```json
{
    "body": "Attachment [trac_8046-ref.patch](tarball://root/attachments/some-uuid/ticket8046/trac_8046-ref.patch) by jhpalmieri created at 2012-01-12 06:43:02",
    "created_at": "2012-01-12T06:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8046#issuecomment-70331",
    "user": "jhpalmieri"
}
```

Attachment [trac_8046-ref.patch](tarball://root/attachments/some-uuid/ticket8046/trac_8046-ref.patch) by jhpalmieri created at 2012-01-12 06:43:02



---

archive/issue_comments_070332.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-01-12T14:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8046#issuecomment-70332",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070333.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-12T14:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8046#issuecomment-70333",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070334.json:
```json
{
    "body": "Looks great!  Thanks for catching this, John.",
    "created_at": "2012-01-12T14:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8046#issuecomment-70334",
    "user": "kcrisman"
}
```

Looks great!  Thanks for catching this, John.



---

archive/issue_comments_070335.json:
```json
{
    "body": "If you build the documentation with \"-j\", it will use jsmath, and should not give the error about dvipng: `sage -docbuild reference html -j`",
    "created_at": "2012-01-12T15:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8046#issuecomment-70335",
    "user": "jason"
}
```

If you build the documentation with "-j", it will use jsmath, and should not give the error about dvipng: `sage -docbuild reference html -j`



---

archive/issue_comments_070336.json:
```json
{
    "body": "> If you build the documentation with \"-j\", it will use jsmath, and should not give the error about dvipng: `sage -docbuild reference html -j`\nInteresting.  In any case, that was clearly an unrelated error.",
    "created_at": "2012-01-12T15:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8046#issuecomment-70336",
    "user": "kcrisman"
}
```

> If you build the documentation with "-j", it will use jsmath, and should not give the error about dvipng: `sage -docbuild reference html -j`
Interesting.  In any case, that was clearly an unrelated error.



---

archive/issue_comments_070337.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-01-18T08:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8046#issuecomment-70337",
    "user": "jdemeyer"
}
```

Resolution: fixed
