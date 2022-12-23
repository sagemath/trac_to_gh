# Issue 5571: fast_callable improvements (followup for #5093)

archive/issues_005571.json:
```json
{
    "body": "Assignee: somebody\n\nThe code at #5093 is very good and ready to go in, but there are several improvements that have been suggested and agreed work on at a later date. They are posted here so we can merge and close the other ticket. \n\nSpecifically, \n\nNot fixed:\n\n* Robert's suggestion: an option that uses a fast domain, if it's there, but ignores the domain parameter if it's not (I don't mind the idea, and the implementation is easy; what should the syntax be? Part of my problem picking a syntax is that I don't want to promise that a specialized interpreter is always faster than the Python-object interpreter, so I don't particularly want to use the word \"fast\" in any option names.)\n\n* fast_callable on list,tuple,vector,matrix arguments\n\n* any interaction with #5413 (my plan is to wait until either #5093 or #5413 gets a positive review, then fix the other one to match)\n\n* fast_callable on constant arguments (waiting for a spec from Jason!)\n\n* fast_callable of a zero multivariate polynomial returns a zero of the base ring, without paying attention to the types of the arguments\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5571\n\n",
    "created_at": "2009-03-19T23:55:04Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "fast_callable improvements (followup for #5093)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5571",
    "user": "robertwb"
}
```
Assignee: somebody

The code at #5093 is very good and ready to go in, but there are several improvements that have been suggested and agreed work on at a later date. They are posted here so we can merge and close the other ticket. 

Specifically, 

Not fixed:

* Robert's suggestion: an option that uses a fast domain, if it's there, but ignores the domain parameter if it's not (I don't mind the idea, and the implementation is easy; what should the syntax be? Part of my problem picking a syntax is that I don't want to promise that a specialized interpreter is always faster than the Python-object interpreter, so I don't particularly want to use the word "fast" in any option names.)

* fast_callable on list,tuple,vector,matrix arguments

* any interaction with #5413 (my plan is to wait until either #5093 or #5413 gets a positive review, then fix the other one to match)

* fast_callable on constant arguments (waiting for a spec from Jason!)

* fast_callable of a zero multivariate polynomial returns a zero of the base ring, without paying attention to the types of the arguments



Issue created by migration from https://trac.sagemath.org/ticket/5571





---

archive/issue_comments_043407.json:
```json
{
    "body": "Duplicate of #5572",
    "created_at": "2009-03-20T06:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5571#issuecomment-43407",
    "user": "cwitty"
}
```

Duplicate of #5572



---

archive/issue_comments_043408.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-03-20T06:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5571#issuecomment-43408",
    "user": "cwitty"
}
```

Resolution: duplicate
