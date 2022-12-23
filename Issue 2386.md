# Issue 2386: copy and pasting matrices doesn't work

archive/issues_002386.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe should be able to somehow get a printout of a matrix that is suitable for pasting into an input cell.\n\nI think that is what repr is supposed to do.  Currently, repr is the same as str, which seems like a bug considering the python convention.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2386\n\n",
    "created_at": "2008-03-04T16:21:12Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "title": "copy and pasting matrices doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2386",
    "user": "jason"
}
```
Assignee: mabshoff

We should be able to somehow get a printout of a matrix that is suitable for pasting into an input cell.

I think that is what repr is supposed to do.  Currently, repr is the same as str, which seems like a bug considering the python convention.

Issue created by migration from https://trac.sagemath.org/ticket/2386





---

archive/issue_comments_016107.json:
```json
{
    "body": "> I think that is what repr is supposed to do. Currently,\n> repr is the same as str, which seems like a bug considering the python convention.\n\nSAGE blatantly and *systematically* does not follow that Python convention.\n\nI am happy if we implement systematically a method _input_form_  (say -- after Mathematica's well chosen named InputForm) for objects which returns -- if possible (sometimes it isn't!) -- an expression that sage_evals to that object.  \n\nDiscuss!",
    "created_at": "2008-03-04T17:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2386#issuecomment-16107",
    "user": "was"
}
```

> I think that is what repr is supposed to do. Currently,
> repr is the same as str, which seems like a bug considering the python convention.

SAGE blatantly and *systematically* does not follow that Python convention.

I am happy if we implement systematically a method _input_form_  (say -- after Mathematica's well chosen named InputForm) for objects which returns -- if possible (sometimes it isn't!) -- an expression that sage_evals to that object.  

Discuss!



---

archive/issue_comments_016108.json:
```json
{
    "body": "This would be part of #2387.",
    "created_at": "2008-03-04T20:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2386#issuecomment-16108",
    "user": "jason"
}
```

This would be part of #2387.



---

archive/issue_comments_016109.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-04T20:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2386#issuecomment-16109",
    "user": "jason"
}
```

Resolution: duplicate
