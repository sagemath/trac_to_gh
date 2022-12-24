# Issue 8981: Adding support for param attribute of GSL ode solver

archive/issues_008981.json:
```json
{
    "body": "Assignee: tba\n\nCurrently it isn't possible to pass parameters to a compiled function used for the GSL ode solver. There are some comments in place to indicate what needs to be changed. I implemented those pieces.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8981\n\n",
    "created_at": "2010-05-17T02:02:16Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Adding support for param attribute of GSL ode solver",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8981",
    "user": "Moredread"
}
```
Assignee: tba

Currently it isn't possible to pass parameters to a compiled function used for the GSL ode solver. There are some comments in place to indicate what needs to be changed. I implemented those pieces.

Issue created by migration from https://trac.sagemath.org/ticket/8981





---

archive/issue_comments_082855.json:
```json
{
    "body": "Attachment [trac_8981_param_gsl_ode.patch](tarball://root/attachments/some-uuid/ticket8981/trac_8981_param_gsl_ode.patch) by Moredread created at 2010-05-17 12:50:30",
    "created_at": "2010-05-17T12:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8981#issuecomment-82855",
    "user": "Moredread"
}
```

Attachment [trac_8981_param_gsl_ode.patch](tarball://root/attachments/some-uuid/ticket8981/trac_8981_param_gsl_ode.patch) by Moredread created at 2010-05-17 12:50:30



---

archive/issue_comments_082856.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-17T12:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8981#issuecomment-82856",
    "user": "Moredread"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082857.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-29T19:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8981#issuecomment-82857",
    "user": "wdj"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082858.json:
```json
{
    "body": "I don't see any examples in the patch. If you make a change in the code (even one I don't understand) you need to add examples to the docstring testing the new functionality.",
    "created_at": "2010-06-29T19:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8981#issuecomment-82858",
    "user": "wdj"
}
```

I don't see any examples in the patch. If you make a change in the code (even one I don't understand) you need to add examples to the docstring testing the new functionality.



---

archive/issue_comments_082859.json:
```json
{
    "body": "There is an example of the usage. I changed the existing one so that I matches the new API, including an example how to use it. (See changes between left hand side line number 295 and 315) Is this not enough?",
    "created_at": "2010-06-29T22:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8981#issuecomment-82859",
    "user": "Moredread"
}
```

There is an example of the usage. I changed the existing one so that I matches the new API, including an example how to use it. (See changes between left hand side line number 295 and 315) Is this not enough?



---

archive/issue_comments_082860.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-20T21:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8981#issuecomment-82860",
    "user": "Moredread"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082861.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-20T22:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8981#issuecomment-82861",
    "user": "Moredread"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082862.json:
```json
{
    "body": "I'll check if the patch still works and maybe improve the documentation first.",
    "created_at": "2010-11-20T22:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8981#issuecomment-82862",
    "user": "Moredread"
}
```

I'll check if the patch still works and maybe improve the documentation first.
