# Issue 6515: assume doesn't interact well with solve

archive/issues_006515.json:
```json
{
    "body": "Assignee: burcin\n\nThis has been brought up several times on the mailing lists. As a specific example \n\n\n```\nsage: assume(x>0)\nsage: solve([x^2-1],x)\n[x == -1, x == 1]\n```\n\n\nAt the very least, we could probably filter out the \"solutions\" that violate the assumptions. \n\n\n\n```\nsage: [all(a.subs(s) for a in assumptions()) for s in solve(x^2-1==0, x)]\n[False, True]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6515\n\n",
    "created_at": "2009-07-12T04:22:28Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "assume doesn't interact well with solve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6515",
    "user": "robertwb"
}
```
Assignee: burcin

This has been brought up several times on the mailing lists. As a specific example 


```
sage: assume(x>0)
sage: solve([x^2-1],x)
[x == -1, x == 1]
```


At the very least, we could probably filter out the "solutions" that violate the assumptions. 



```
sage: [all(a.subs(s) for a in assumptions()) for s in solve(x^2-1==0, x)]
[False, True]
```


Issue created by migration from https://trac.sagemath.org/ticket/6515





---

archive/issue_comments_053074.json:
```json
{
    "body": "It sounds like Maxima (intentionally?) doesn't use assumptions in solve, see for instance [http://www.math.utexas.edu/pipermail/maxima/2008/013152.html](http://www.math.utexas.edu/pipermail/maxima/2008/013152.html) and other similar threads.  The above solution seems reasonable.",
    "created_at": "2009-09-30T18:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6515#issuecomment-53074",
    "user": "kcrisman"
}
```

It sounds like Maxima (intentionally?) doesn't use assumptions in solve, see for instance [http://www.math.utexas.edu/pipermail/maxima/2008/013152.html](http://www.math.utexas.edu/pipermail/maxima/2008/013152.html) and other similar threads.  The above solution seems reasonable.



---

archive/issue_comments_053075.json:
```json
{
    "body": "Update:  the solution above works well for single equations in one variable, but is tricky to implement for multiple equations (you can't subs x+y==3, for instance).  Also, one has to keep in mind how to check assumptions like 'x is Integer', which can't be subs'ed in.",
    "created_at": "2009-11-17T22:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6515#issuecomment-53075",
    "user": "kcrisman"
}
```

Update:  the solution above works well for single equations in one variable, but is tricky to implement for multiple equations (you can't subs x+y==3, for instance).  Also, one has to keep in mind how to check assumptions like 'x is Integer', which can't be subs'ed in.



---

archive/issue_comments_053076.json:
```json
{
    "body": "Attachment [6515-solve-assume.patch](tarball://root/attachments/some-uuid/ticket6515/6515-solve-assume.patch) by robertwb created at 2010-01-19 21:14:31",
    "created_at": "2010-01-19T21:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6515#issuecomment-53076",
    "user": "robertwb"
}
```

Attachment [6515-solve-assume.patch](tarball://root/attachments/some-uuid/ticket6515/6515-solve-assume.patch) by robertwb created at 2010-01-19 21:14:31



---

archive/issue_comments_053077.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T21:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6515#issuecomment-53077",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053078.json:
```json
{
    "body": "It doesn't catch everything, but is better than what we have now.",
    "created_at": "2010-01-19T21:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6515#issuecomment-53078",
    "user": "robertwb"
}
```

It doesn't catch everything, but is better than what we have now.



---

archive/issue_comments_053079.json:
```json
{
    "body": "Attachment [trac_6515-referee.patch](tarball://root/attachments/some-uuid/ticket6515/trac_6515-referee.patch) by burcin created at 2010-02-03 16:50:53\n\nminor documentation fixes",
    "created_at": "2010-02-03T16:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6515#issuecomment-53079",
    "user": "burcin"
}
```

Attachment [trac_6515-referee.patch](tarball://root/attachments/some-uuid/ticket6515/trac_6515-referee.patch) by burcin created at 2010-02-03 16:50:53

minor documentation fixes



---

archive/issue_comments_053080.json:
```json
{
    "body": "The patch looks good and doctests pass. There is one minor problem, the line\n\n\n```\nsage: GenericDeclaration(x, 'rational').contradicts(y==pi)\n```\n\n\nis repeated several times in the doctest for `sage.symbolic.assumptions.GenericDeclaration.contradicts()`.\n\nI attached a patch to change these lines and add an `INPUT` field to the docstring. Can you look over my patch and change the status to positive_review if you agree with the changes?",
    "created_at": "2010-02-03T16:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6515#issuecomment-53080",
    "user": "burcin"
}
```

The patch looks good and doctests pass. There is one minor problem, the line


```
sage: GenericDeclaration(x, 'rational').contradicts(y==pi)
```


is repeated several times in the doctest for `sage.symbolic.assumptions.GenericDeclaration.contradicts()`.

I attached a patch to change these lines and add an `INPUT` field to the docstring. Can you look over my patch and change the status to positive_review if you agree with the changes?



---

archive/issue_comments_053081.json:
```json
{
    "body": "Thanks for looking at this. Nice catches, I approve of your changes.",
    "created_at": "2010-02-03T20:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6515#issuecomment-53081",
    "user": "robertwb"
}
```

Thanks for looking at this. Nice catches, I approve of your changes.



---

archive/issue_comments_053082.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-03T20:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6515#issuecomment-53082",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053083.json:
```json
{
    "body": "For the record: Applying the patch to 4.3.2 + [a long queue](http://trac.sagemath.org/sage_trac/ticket/8186#comment:6) gives\n\n\n```\napplying 6515-solve-assume.patch\npatching file sage/symbolic/expression.pyx\nHunk #2 succeeded at 5952 with fuzz 2 (offset 40 lines).\nHunk #3 succeeded at 6037 with fuzz 1 (offset 83 lines).\n```\n\n\nPlease let us know (via sage-devel) about the best order in which to apply the symbolics and calculus patches.",
    "created_at": "2010-02-10T15:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6515#issuecomment-53083",
    "user": "mpatel"
}
```

For the record: Applying the patch to 4.3.2 + [a long queue](http://trac.sagemath.org/sage_trac/ticket/8186#comment:6) gives


```
applying 6515-solve-assume.patch
patching file sage/symbolic/expression.pyx
Hunk #2 succeeded at 5952 with fuzz 2 (offset 40 lines).
Hunk #3 succeeded at 6037 with fuzz 1 (offset 83 lines).
```


Please let us know (via sage-devel) about the best order in which to apply the symbolics and calculus patches.



---

archive/issue_comments_053084.json:
```json
{
    "body": "The first patch is missing a Mercurial header and the ticket number.  I've applied a refreshed patch to 4.3.3.alpha0.",
    "created_at": "2010-02-10T19:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6515#issuecomment-53084",
    "user": "mpatel"
}
```

The first patch is missing a Mercurial header and the ticket number.  I've applied a refreshed patch to 4.3.3.alpha0.



---

archive/issue_comments_053085.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6515#issuecomment-53085",
    "user": "mpatel"
}
```

Resolution: fixed
