# Issue 4827: [with patch, needs review] add L-BFGS-B bound constraint solver to minimize_constraint

archive/issues_004827.json:
```json
{
    "body": "Assignee: jkantor\n\nadding [scipy's l-bfgs-b](http://www.scipy.org/doc/api_docs/SciPy.optimize.lbfgsb.html#fmin_l_bfgs_b) large scale bound constraint solver, small change in docstring: bounds are better off in tuples.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4827\n\n",
    "created_at": "2008-12-18T17:31:56Z",
    "labels": [
        "numerical",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] add L-BFGS-B bound constraint solver to minimize_constraint",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4827",
    "user": "schilly"
}
```
Assignee: jkantor

adding [scipy's l-bfgs-b](http://www.scipy.org/doc/api_docs/SciPy.optimize.lbfgsb.html#fmin_l_bfgs_b) large scale bound constraint solver, small change in docstring: bounds are better off in tuples.

Issue created by migration from https://trac.sagemath.org/ticket/4827





---

archive/issue_comments_036596.json:
```json
{
    "body": "Attachment [lbfgsb-v1.patch](tarball://root/attachments/some-uuid/ticket4827/lbfgsb-v1.patch) by schilly created at 2008-12-18 17:32:43\n\nadds lbfgsb to minimize_constraint",
    "created_at": "2008-12-18T17:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4827#issuecomment-36596",
    "user": "schilly"
}
```

Attachment [lbfgsb-v1.patch](tarball://root/attachments/some-uuid/ticket4827/lbfgsb-v1.patch) by schilly created at 2008-12-18 17:32:43

adds lbfgsb to minimize_constraint



---

archive/issue_comments_036597.json:
```json
{
    "body": "Attachment [trac_4827-optimize-doc.patch](tarball://root/attachments/some-uuid/ticket4827/trac_4827-optimize-doc.patch) by jason created at 2009-01-28 19:32:32\n\napply on top of previous patch",
    "created_at": "2009-01-28T19:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4827#issuecomment-36597",
    "user": "jason"
}
```

Attachment [trac_4827-optimize-doc.patch](tarball://root/attachments/some-uuid/ticket4827/trac_4827-optimize-doc.patch) by jason created at 2009-01-28 19:32:32

apply on top of previous patch



---

archive/issue_comments_036598.json:
```json
{
    "body": "Looks good to me.\n\nFor another ticket: the minimize_constrained arguments should have x0 before cons to parallel the argument structure of the other minimze functions.  Also, we should maybe look into using openopt at some point since the syntax is then unified.\n\nThe small doc patch I attached makes the documentation of the function arguments in the same order as the function arguments.  I don't think it needs to be reviewed.",
    "created_at": "2009-01-28T19:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4827#issuecomment-36598",
    "user": "jason"
}
```

Looks good to me.

For another ticket: the minimize_constrained arguments should have x0 before cons to parallel the argument structure of the other minimze functions.  Also, we should maybe look into using openopt at some point since the syntax is then unified.

The small doc patch I attached makes the documentation of the function arguments in the same order as the function arguments.  I don't think it needs to be reviewed.



---

archive/issue_comments_036599.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n>  Also, we should maybe look into using openopt at some point since the syntax is then unified.\n\nyeahr, tell me if somebody is working on that or you need help. maybe i can look into it. probably the most difficult part is to detect/register optional solvers inside sage, or talking to installed ones...\n\n> \n> The small doc patch I attached makes the documentation of the function arguments in the same order as the function arguments.  I don't think it needs to be reviewed.\n\nwell, fwiw, +1 from me ;)",
    "created_at": "2009-01-28T20:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4827#issuecomment-36599",
    "user": "schilly"
}
```

Replying to [comment:1 jason]:
>  Also, we should maybe look into using openopt at some point since the syntax is then unified.

yeahr, tell me if somebody is working on that or you need help. maybe i can look into it. probably the most difficult part is to detect/register optional solvers inside sage, or talking to installed ones...

> 
> The small doc patch I attached makes the documentation of the function arguments in the same order as the function arguments.  I don't think it needs to be reviewed.

well, fwiw, +1 from me ;)



---

archive/issue_comments_036600.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T00:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4827#issuecomment-36600",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036601.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T00:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4827#issuecomment-36601",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.3.alpha3.

Cheers,

Michael
