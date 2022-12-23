# Issue 79: Create a framework for numerical computation in SAGE

archive/issues_000079.json:
```json
{
    "body": "Assignee: somebody\n\nGood support in SAGE for numerical computation is crucial to our success.  Ignoring serious numerical computation has crippled numerous other systems (e.g., GAP).  \nThe primary audience of SAGE is not engineers or big-lab researchers.  \nThe target audience of SAGE is mainly undergraduate mathematics majors,\nmathematics graduate students, and researchers in mathematics and cryptography.\n\n\nSAGE's unique approach to numerics will be to focus from the ground up on connections between algrebraic and numerical computation.  This means:\n\n* The numerical objects in SAGE will be very algebraically structured, just like objects are in Magma and the rest of SAGE.  Matrices, vectors, etc., will be mathematical objects, with all the accomanying structure. \n\n* There will be substantial support for transforming objects from numerical to algebraic and from algebraic to numerical.  For example, there should be very fast transformations of matrices (vectors, polynomials, etc.) over the rationals to matrices with floating point entries, implemented at the compiled level.  And the supported transformations should make sense mathematically.  Also, there should be transformations like \"give me the best rational coefficient approximation to this polynomial\", etc.   There are likely interesting problems here that could lead to a paper. \n\n\n  * The numerical libraries should be build-able 100% with no dependencies, so that users can understand all numerical code in SAGE with just knowledge of C and Python.   We are not targeting engineers who are happy with black boxes -- we are targeting curious talented mathematicians, who we can reasonably expect might want to crack open the box and look inside.  Of course, for speed one should also be able to build against standard optimized (sometimes closed source) BLAS implementations.  GSL nicely satisfies this requirement. \n\n  * When possible, available functions, their layout, conventions, and function names should be similar to what is in MATLAB, since that's what many people use for numerical computation and know well, and MATLAB is well designed.  This will make it easier for people to use both SAGE and MATLAB. \n\n  * Plotting is very important.   We should put huge effort in to make plotting of numerical objects integrate nicely with what SAGE offers via the notebook, i.e., via matplotlib, tachyon, etc.   For local-GUI plotting, vtk already does an excellent job and SAGE has little to add.  But for plotting in a notebook, there are still many interesting difficult problems. \n\nIssue created by migration from https://trac.sagemath.org/ticket/79\n\n",
    "created_at": "2006-09-23T00:37:23Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "Create a framework for numerical computation in SAGE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/79",
    "user": "was"
}
```
Assignee: somebody

Good support in SAGE for numerical computation is crucial to our success.  Ignoring serious numerical computation has crippled numerous other systems (e.g., GAP).  
The primary audience of SAGE is not engineers or big-lab researchers.  
The target audience of SAGE is mainly undergraduate mathematics majors,
mathematics graduate students, and researchers in mathematics and cryptography.


SAGE's unique approach to numerics will be to focus from the ground up on connections between algrebraic and numerical computation.  This means:

* The numerical objects in SAGE will be very algebraically structured, just like objects are in Magma and the rest of SAGE.  Matrices, vectors, etc., will be mathematical objects, with all the accomanying structure. 

* There will be substantial support for transforming objects from numerical to algebraic and from algebraic to numerical.  For example, there should be very fast transformations of matrices (vectors, polynomials, etc.) over the rationals to matrices with floating point entries, implemented at the compiled level.  And the supported transformations should make sense mathematically.  Also, there should be transformations like "give me the best rational coefficient approximation to this polynomial", etc.   There are likely interesting problems here that could lead to a paper. 


  * The numerical libraries should be build-able 100% with no dependencies, so that users can understand all numerical code in SAGE with just knowledge of C and Python.   We are not targeting engineers who are happy with black boxes -- we are targeting curious talented mathematicians, who we can reasonably expect might want to crack open the box and look inside.  Of course, for speed one should also be able to build against standard optimized (sometimes closed source) BLAS implementations.  GSL nicely satisfies this requirement. 

  * When possible, available functions, their layout, conventions, and function names should be similar to what is in MATLAB, since that's what many people use for numerical computation and know well, and MATLAB is well designed.  This will make it easier for people to use both SAGE and MATLAB. 

  * Plotting is very important.   We should put huge effort in to make plotting of numerical objects integrate nicely with what SAGE offers via the notebook, i.e., via matplotlib, tachyon, etc.   For local-GUI plotting, vtk already does an excellent job and SAGE has little to add.  But for plotting in a notebook, there are still many interesting difficult problems. 

Issue created by migration from https://trac.sagemath.org/ticket/79





---

archive/issue_comments_000395.json:
```json
{
    "body": "This should be broken up into smaller tickets. Some of this has already happened/is covered by other tickets.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-10T03:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/79",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/79#issuecomment-395",
    "user": "mabshoff"
}
```

This should be broken up into smaller tickets. Some of this has already happened/is covered by other tickets.

Cheers,

Michael



---

archive/issue_comments_000396.json:
```json
{
    "body": "Josh did this with integrating in scipy, etc.",
    "created_at": "2007-09-20T13:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/79",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/79#issuecomment-396",
    "user": "was"
}
```

Josh did this with integrating in scipy, etc.



---

archive/issue_comments_000397.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-20T13:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/79",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/79#issuecomment-397",
    "user": "was"
}
```

Resolution: fixed
