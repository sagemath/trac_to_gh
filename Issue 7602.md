# Issue 7602: bug in fpLLL

archive/issues_007602.json:
```json
{
    "body": "Assignee: was\n\nAndyNovo wrote on [sage-devel]:\n\n```\nWe've been working on factoring polynomials in FLINT very intensively the last couple months.  So we've been making floating point LLL in FLINT.  During the process I just discovered what I thought was my bug but is actually a bug in fpLLL which means it's a bug in SAGE too.\n\nHere's a simple lattice which triggers the bug on my 32 bit machine.\n(It's the zero rows which are not handled cleanly causing it to size\nreduce in very odd ways...)  For a 64 bit machine I have a much larger example which breaks it.\n\n[[0 0 0 0 0]\n[0 0 0 0 0]\n[1 0 0 0 11]\n[0 1 0 0 47]\n[0 0 1 0 3748]]\n\nTo test the bug in SAGE just run the following code:\n\nmatrix([[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,11],[0,1,0,0,47],\n[0,0,1,0,3748]]).LLL()\n\n(This was on SAGE 4-1-1 the August 14th version.)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7602\n\n",
    "created_at": "2009-12-04T11:13:19Z",
    "labels": [
        "linear algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in fpLLL",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7602",
    "user": "malb"
}
```
Assignee: was

AndyNovo wrote on [sage-devel]:

```
We've been working on factoring polynomials in FLINT very intensively the last couple months.  So we've been making floating point LLL in FLINT.  During the process I just discovered what I thought was my bug but is actually a bug in fpLLL which means it's a bug in SAGE too.

Here's a simple lattice which triggers the bug on my 32 bit machine.
(It's the zero rows which are not handled cleanly causing it to size
reduce in very odd ways...)  For a 64 bit machine I have a much larger example which breaks it.

[[0 0 0 0 0]
[0 0 0 0 0]
[1 0 0 0 11]
[0 1 0 0 47]
[0 0 1 0 3748]]

To test the bug in SAGE just run the following code:

matrix([[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,11],[0,1,0,0,47],
[0,0,1,0,3748]]).LLL()

(This was on SAGE 4-1-1 the August 14th version.)
```


Issue created by migration from https://trac.sagemath.org/ticket/7602





---

archive/issue_comments_064863.json:
```json
{
    "body": "AndyNovo on [sage-devel]:\n> OK found the bug.  There is a program called get_Shift which gets\n> confused by zero vectors.  In any call to Babai if you just add a line\n> setting n = the number of columns of B (I'm not sure his notation in\n> the C++ version) then it works again.",
    "created_at": "2009-12-04T11:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7602#issuecomment-64863",
    "user": "malb"
}
```

AndyNovo on [sage-devel]:
> OK found the bug.  There is a program called get_Shift which gets
> confused by zero vectors.  In any call to Babai if you just add a line
> setting n = the number of columns of B (I'm not sure his notation in
> the C++ version) then it works again.



---

archive/issue_comments_064864.json:
```json
{
    "body": "I can't reproduce/test due to lack of 32-bit machine, anyone still got one?",
    "created_at": "2014-06-25T00:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7602#issuecomment-64864",
    "user": "malb"
}
```

I can't reproduce/test due to lack of 32-bit machine, anyone still got one?



---

archive/issue_comments_064865.json:
```json
{
    "body": "The example that should fail on 64bit OS mentioned in the thread works for me.",
    "created_at": "2014-08-13T21:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7602#issuecomment-64865",
    "user": "aapitzsch"
}
```

The example that should fail on 64bit OS mentioned in the thread works for me.



---

archive/issue_comments_064866.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-13T21:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7602#issuecomment-64866",
    "user": "aapitzsch"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064867.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-08-19T15:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7602#issuecomment-64867",
    "user": "pbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064868.json:
```json
{
    "body": "The example in the ticket description also works fine on 32-bit ARM, so I think we can safely assume that this has been fixed.",
    "created_at": "2014-08-19T15:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7602#issuecomment-64868",
    "user": "pbruin"
}
```

The example in the ticket description also works fine on 32-bit ARM, so I think we can safely assume that this has been fixed.



---

archive/issue_comments_064869.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-08-20T20:32:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7602#issuecomment-64869",
    "user": "vbraun"
}
```

Resolution: fixed
