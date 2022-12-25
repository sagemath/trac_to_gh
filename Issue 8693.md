# Issue 8693: QuadraticForm::basis_of_short_vectors may not return an actual basis.

archive/issues_008693.json:
```json
{
    "body": "Assignee: justin\n\nCC:  @yyyyx4\n\nKeywords: quadratic forms, basis, automorphisms\n\nQuadraticForm::basis_of_short_vectors does not actually ensure the list of vectors it returns is a basis, it only assures that it spans a full rank sub-lattice.\n\nIn particular in the following example (E8):\n\n\n```\nQ = QuadraticForm( matrix( [[2,0,0,0,0,0,0,1],\n                            [0,2,1,1,1,1,1,1],\n                            [0,1,2,1,1,1,1,1],\n                            [0,1,1,2,1,1,1,1],\n                            [0,1,1,1,2,1,1,1],\n                            [0,1,1,1,1,2,1,1],\n                            [0,1,1,1,1,1,2,0],\n                            [1,1,1,1,1,1,0,2]] ))\nB = Q.basis_of_short_vectors()\nmatrix(B).det()\n```\n\n\nThe result is -2, which indicates we did not get a basis.\nNote that the above means that sage likely returns incorrect results about the automorphism groups of a number of interesting lattices.\nI am attaching some sample code which (once properly merged {and tested}) could be used to correct the issue.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8693\n\n",
    "created_at": "2010-04-15T18:51:18Z",
    "labels": [
        "component: quadratic forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.9",
    "title": "QuadraticForm::basis_of_short_vectors may not return an actual basis.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8693",
    "user": "https://trac.sagemath.org/admin/accounts/users/afiori"
}
```
Assignee: justin

CC:  @yyyyx4

Keywords: quadratic forms, basis, automorphisms

QuadraticForm::basis_of_short_vectors does not actually ensure the list of vectors it returns is a basis, it only assures that it spans a full rank sub-lattice.

In particular in the following example (E8):


```
Q = QuadraticForm( matrix( [[2,0,0,0,0,0,0,1],
                            [0,2,1,1,1,1,1,1],
                            [0,1,2,1,1,1,1,1],
                            [0,1,1,2,1,1,1,1],
                            [0,1,1,1,2,1,1,1],
                            [0,1,1,1,1,2,1,1],
                            [0,1,1,1,1,1,2,0],
                            [1,1,1,1,1,1,0,2]] ))
B = Q.basis_of_short_vectors()
matrix(B).det()
```


The result is -2, which indicates we did not get a basis.
Note that the above means that sage likely returns incorrect results about the automorphism groups of a number of interesting lattices.
I am attaching some sample code which (once properly merged {and tested}) could be used to correct the issue.

Issue created by migration from https://trac.sagemath.org/ticket/8693





---

archive/issue_comments_079063.json:
```json
{
    "body": "Attachment [fix_basis.sage](tarball://root/attachments/some-uuid/ticket8693/fix_basis.sage) by afiori created at 2010-04-15 18:52:00\n\nSample code to correct a non-basis from basis_of_short_vectors",
    "created_at": "2010-04-15T18:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8693#issuecomment-79063",
    "user": "https://trac.sagemath.org/admin/accounts/users/afiori"
}
```

Attachment [fix_basis.sage](tarball://root/attachments/some-uuid/ticket8693/fix_basis.sage) by afiori created at 2010-04-15 18:52:00

Sample code to correct a non-basis from basis_of_short_vectors



---

archive/issue_comments_079064.json:
```json
{
    "body": "Isn't this just a matter of defining what \"basis\" means?",
    "created_at": "2015-08-30T10:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8693#issuecomment-79064",
    "user": "https://github.com/jdemeyer"
}
```

Isn't this just a matter of defining what "basis" means?



---

archive/issue_events_021096.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-08-30T10:55:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8693",
    "milestone": "sage-6.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8693#event-21096"
}
```



---

archive/issue_comments_079065.json:
```json
{
    "body": "I suppose someone might want a rational basis for the associated rational vector space which consists only of integral vectors... but that seems unlikely to be a common use case.\nIn any case, if I recall correctly... the code which computes automorphism groups of lattices uses this function, and consequently computes the automorphism group of E8 incorrectly.\nThe simplest stopgap would be to check if you are returning a basis, and if not just return the original basis. \nThe code I had posted before (before I had learned to build patches under the old system) probably works, though as I don't currently have a working sage install to test it in (and still haven't done anything with current system for building patches) I am not really in a position to do much testing.",
    "created_at": "2015-09-25T17:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8693#issuecomment-79065",
    "user": "https://trac.sagemath.org/admin/accounts/users/afiori"
}
```

I suppose someone might want a rational basis for the associated rational vector space which consists only of integral vectors... but that seems unlikely to be a common use case.
In any case, if I recall correctly... the code which computes automorphism groups of lattices uses this function, and consequently computes the automorphism group of E8 incorrectly.
The simplest stopgap would be to check if you are returning a basis, and if not just return the original basis. 
The code I had posted before (before I had learned to build patches under the old system) probably works, though as I don't currently have a working sage install to test it in (and still haven't done anything with current system for building patches) I am not really in a position to do much testing.



---

archive/issue_comments_079066.json:
```json
{
    "body": "It looks to me the well-defined notion here would be the \"successive minima\" of a lattice: a sequence of vectors in the lattice where each vector is of minimal length while being linearly independent from the previous ones. Such a set is indeed not necessarily a basis. So we should check that the routine actually computes this and then rename it.\n\nI think for most applications, the lengths themselves are usually more important than the vectors that attain them.\n\nNaturally, this notion needs a (positive) definite quadratic form.",
    "created_at": "2021-08-26T16:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8693#issuecomment-79066",
    "user": "https://github.com/nbruin"
}
```

It looks to me the well-defined notion here would be the "successive minima" of a lattice: a sequence of vectors in the lattice where each vector is of minimal length while being linearly independent from the previous ones. Such a set is indeed not necessarily a basis. So we should check that the routine actually computes this and then rename it.

I think for most applications, the lengths themselves are usually more important than the vectors that attain them.

Naturally, this notion needs a (positive) definite quadratic form.
