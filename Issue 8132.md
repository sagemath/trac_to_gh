# Issue 8132: fix documentation related to ODE solvers

archive/issues_008132.json:
```json
{
    "body": "Assignee: mvngu\n\nThe documentation to ODE solvers is not written in harmony with Sage developers guide and the Sage Constructions are outdated. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8132\n\n",
    "created_at": "2010-01-31T00:32:02Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "fix documentation related to ODE solvers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8132",
    "user": "robert.marik"
}
```
Assignee: mvngu

The documentation to ODE solvers is not written in harmony with Sage developers guide and the Sage Constructions are outdated. 

Issue created by migration from https://trac.sagemath.org/ticket/8132





---

archive/issue_comments_071501.json:
```json
{
    "body": "Attachment [trac_8132.patch](tarball://root/attachments/some-uuid/ticket8132/trac_8132.patch) by robert.marik created at 2010-01-31 00:34:33",
    "created_at": "2010-01-31T00:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8132#issuecomment-71501",
    "user": "robert.marik"
}
```

Attachment [trac_8132.patch](tarball://root/attachments/some-uuid/ticket8132/trac_8132.patch) by robert.marik created at 2010-01-31 00:34:33



---

archive/issue_comments_071502.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-31T00:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8132#issuecomment-71502",
    "user": "robert.marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071503.json:
```json
{
    "body": "this patch\n\n* fixes indentation in sage/gsl/ode.pyx from 3 spaces to 4 spaces\n\n* fixes documentation",
    "created_at": "2010-01-31T00:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8132#issuecomment-71503",
    "user": "robert.marik"
}
```

this patch

* fixes indentation in sage/gsl/ode.pyx from 3 spaces to 4 spaces

* fixes documentation



---

archive/issue_comments_071504.json:
```json
{
    "body": "Attachment [trac_8132_fixed_doctests.patch](tarball://root/attachments/some-uuid/ticket8132/trac_8132_fixed_doctests.patch) by robert.marik created at 2010-01-31 08:26:03\n\nfixes one failed doctest, apply on the top of previous poatch",
    "created_at": "2010-01-31T08:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8132#issuecomment-71504",
    "user": "robert.marik"
}
```

Attachment [trac_8132_fixed_doctests.patch](tarball://root/attachments/some-uuid/ticket8132/trac_8132_fixed_doctests.patch) by robert.marik created at 2010-01-31 08:26:03

fixes one failed doctest, apply on the top of previous poatch



---

archive/issue_comments_071505.json:
```json
{
    "body": "This seems to be an excellent and extremely welcomed collection of docstring fixes related to solving differential equations in Sage.\n\n Am I missing something or is it odd that calculus/desolver is not listed http://www.sagemath.org/doc/reference/modindex.html? Using\nhttp://www.sagemath.org/doc/developer/sage_manuals.html#building-the-manuals\nI see how to rebuild the manual but how do I see what the changes in the patch look like if \ndesolver isn't even in the manual in the first place?\n\nCan a patch be added to include desolver in the manual?",
    "created_at": "2010-01-31T14:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8132#issuecomment-71505",
    "user": "wdj"
}
```

This seems to be an excellent and extremely welcomed collection of docstring fixes related to solving differential equations in Sage.

 Am I missing something or is it odd that calculus/desolver is not listed http://www.sagemath.org/doc/reference/modindex.html? Using
http://www.sagemath.org/doc/developer/sage_manuals.html#building-the-manuals
I see how to rebuild the manual but how do I see what the changes in the patch look like if 
desolver isn't even in the manual in the first place?

Can a patch be added to include desolver in the manual?



---

archive/issue_comments_071506.json:
```json
{
    "body": "Fixed thanks. Thanks for the links how to do it.\nTwo new chapters are at the end of Symbolic Calculus.\n\nPDF manual does not build, partly due to #8036, patly due to another problem not related to this ticket (unknown command \\cross used in some file related to polynomials). The ODE part of PDF manual looks good, anyway.\n\nHtml version looks good for me.",
    "created_at": "2010-01-31T16:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8132#issuecomment-71506",
    "user": "robert.marik"
}
```

Fixed thanks. Thanks for the links how to do it.
Two new chapters are at the end of Symbolic Calculus.

PDF manual does not build, partly due to #8036, patly due to another problem not related to this ticket (unknown command \cross used in some file related to polynomials). The ODE part of PDF manual looks good, anyway.

Html version looks good for me.



---

archive/issue_comments_071507.json:
```json
{
    "body": "apply on the top of the previous two patches",
    "created_at": "2010-01-31T16:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8132#issuecomment-71507",
    "user": "robert.marik"
}
```

apply on the top of the previous two patches



---

archive/issue_comments_071508.json:
```json
{
    "body": "Attachment [trac_8132_fixed_reference_manual.patch](tarball://root/attachments/some-uuid/ticket8132/trac_8132_fixed_reference_manual.patch) by robert.marik created at 2010-01-31 16:38:06\n\nbtw: the second problem which caused pdf not to build has been fixed by #8021",
    "created_at": "2010-01-31T16:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8132#issuecomment-71508",
    "user": "robert.marik"
}
```

Attachment [trac_8132_fixed_reference_manual.patch](tarball://root/attachments/some-uuid/ticket8132/trac_8132_fixed_reference_manual.patch) by robert.marik created at 2010-01-31 16:38:06

btw: the second problem which caused pdf not to build has been fixed by #8021



---

archive/issue_comments_071509.json:
```json
{
    "body": "Three patches apply fine to 4.3.2.a0 and passes sage -testall, except for apparently unrelated failures already reported, on a mac 10.6.2.\n\nVery nice docstring patch Robert!\n\nPositive review.",
    "created_at": "2010-01-31T22:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8132#issuecomment-71509",
    "user": "wdj"
}
```

Three patches apply fine to 4.3.2.a0 and passes sage -testall, except for apparently unrelated failures already reported, on a mac 10.6.2.

Very nice docstring patch Robert!

Positive review.



---

archive/issue_comments_071510.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T22:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8132#issuecomment-71510",
    "user": "wdj"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071511.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-02T02:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8132#issuecomment-71511",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_071512.json:
```json
{
    "body": "Merged in the following order:\n\n1. [trac_8132.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8132/trac_8132.patch)\n2. [trac_8132_fixed_doctests.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8132/trac_8132_fixed_doctests.patch)\n3. [trac_8132_fixed_reference_manual.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8132/trac_8132_fixed_reference_manual.patch)",
    "created_at": "2010-02-02T02:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8132#issuecomment-71512",
    "user": "mvngu"
}
```

Merged in the following order:

1. [trac_8132.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8132/trac_8132.patch)
2. [trac_8132_fixed_doctests.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8132/trac_8132_fixed_doctests.patch)
3. [trac_8132_fixed_reference_manual.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8132/trac_8132_fixed_reference_manual.patch)
