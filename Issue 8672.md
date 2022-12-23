# Issue 8672: SCIP support

archive/issues_008672.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nCC:  malb schilly r.gaia.cs\n\nBased upon Harald Schilly's SPKG for SCIP, here is a patch to enable the use of this solver through the usual interface for LP.\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8672\n\n",
    "created_at": "2010-04-11T12:32:06Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "title": "SCIP support",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8672",
    "user": "ncohen"
}
```
Assignee: jason, jkantor

CC:  malb schilly r.gaia.cs

Based upon Harald Schilly's SPKG for SCIP, here is a patch to enable the use of this solver through the usual interface for LP.

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8672





---

archive/issue_comments_078917.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-11T12:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8672#issuecomment-78917",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078918.json:
```json
{
    "body": "wow, thank you!! just one thing, is it possible to enable verbose output if enabled? i don't know which parameter you have to set in Sage's MIP interface, but it is  scip.solver(quiet=False) in scip.",
    "created_at": "2010-04-11T12:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8672#issuecomment-78918",
    "user": "schilly"
}
```

wow, thank you!! just one thing, is it possible to enable verbose output if enabled? i don't know which parameter you have to set in Sage's MIP interface, but it is  scip.solver(quiet=False) in scip.



---

archive/issue_comments_078919.json:
```json
{
    "body": "Fixed ! The corresponding argument in sage is log=# in the solve method. 0 for no output, and integers to have progressdively more (only GLPk has different levels of output though, the others only understand 0/1 or none at all )\n\nNathann",
    "created_at": "2010-04-11T12:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8672#issuecomment-78919",
    "user": "ncohen"
}
```

Fixed ! The corresponding argument in sage is log=# in the solve method. 0 for no output, and integers to have progressdively more (only GLPk has different levels of output though, the others only understand 0/1 or none at all )

Nathann



---

archive/issue_comments_078920.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-11T12:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8672#issuecomment-78920",
    "user": "ncohen"
}
```

Attachment



---

archive/issue_comments_078921.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-02T21:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8672#issuecomment-78921",
    "user": "malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078922.json:
```json
{
    "body": "Hi Nathann,\n\ntwo small things:\n\n* `solve_scip` has no documentation/doctests \n* \"the default solver is used (COIN if available, GLPK otherwise)\" seems to be inaccurate since you also try SCIP whether it is available",
    "created_at": "2010-06-02T21:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8672#issuecomment-78922",
    "user": "malb"
}
```

Hi Nathann,

two small things:

* `solve_scip` has no documentation/doctests 
* "the default solver is used (COIN if available, GLPK otherwise)" seems to be inaccurate since you also try SCIP whether it is available



---

archive/issue_comments_078923.json:
```json
{
    "body": "Changing component from numerical to linear programming.",
    "created_at": "2010-09-06T11:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8672#issuecomment-78923",
    "user": "ncohen"
}
```

Changing component from numerical to linear programming.



---

archive/issue_comments_078924.json:
```json
{
    "body": "Duplicate of #10879, so I'm marking this one as \"needs_review\" so it can be closed -- hoping this is the correct procedure.",
    "created_at": "2016-03-30T20:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8672#issuecomment-78924",
    "user": "mkoeppe"
}
```

Duplicate of #10879, so I'm marking this one as "needs_review" so it can be closed -- hoping this is the correct procedure.



---

archive/issue_comments_078925.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-03-30T20:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8672#issuecomment-78925",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078926.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-04-07T20:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8672#issuecomment-78926",
    "user": "vdelecroix"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078927.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-06-12T12:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8672#issuecomment-78927",
    "user": "vbraun"
}
```

Resolution: fixed
