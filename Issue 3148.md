# Issue 3148: improved orthogonal functions

archive/issues_003148.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: orthogonal polynomials Maxima\n\n\nThe defects in the code for the hermite function in\nsage/functions/orthogonal_polys.py which were noted and corrected in \n#2336 apply equally to the other functions in that file.\n\nThe attached patch applies the same fix that worked for hermite to the \nfollowing functions:\n\nchebyshev_T,\nchebyshev_U,\ngen_laguerre,\ngen_legendre_P,\ngen_legendre_Q,\njacobi_P,\nlaguerre,\nlegendre_P,\nlegendre_Q,\nultraspherical\n\nThis allows these polynomials to take much more general \narguments; see the examples given for legendre_P.\n\nThe functions:\n\ngen_legendre_P,\ngen_legendre_Q,\nlegendre_Q\n\nno longer yield a string representing a Maxima expression when the \nargument is a variable.   \n\nFor m > n the function gen_legendre_Q(n, m, x)\nhas to be computed independently of Maxima.  This part of the code may \nneed improving.\n\nThe introductory documentation has not been changed.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3148\n\n",
    "created_at": "2008-05-10T12:08:12Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "improved orthogonal functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3148",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```
Assignee: @williamstein

Keywords: orthogonal polynomials Maxima


The defects in the code for the hermite function in
sage/functions/orthogonal_polys.py which were noted and corrected in 
#2336 apply equally to the other functions in that file.

The attached patch applies the same fix that worked for hermite to the 
following functions:

chebyshev_T,
chebyshev_U,
gen_laguerre,
gen_legendre_P,
gen_legendre_Q,
jacobi_P,
laguerre,
legendre_P,
legendre_Q,
ultraspherical

This allows these polynomials to take much more general 
arguments; see the examples given for legendre_P.

The functions:

gen_legendre_P,
gen_legendre_Q,
legendre_Q

no longer yield a string representing a Maxima expression when the 
argument is a variable.   

For m > n the function gen_legendre_Q(n, m, x)
has to be computed independently of Maxima.  This part of the code may 
need improving.

The introductory documentation has not been changed.



Issue created by migration from https://trac.sagemath.org/ticket/3148





---

archive/issue_comments_021791.json:
```json
{
    "body": "Attachment [sage-3148.patch](tarball://root/attachments/some-uuid/ticket3148/sage-3148.patch) by fwclarke created at 2008-05-10 12:09:32",
    "created_at": "2008-05-10T12:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3148#issuecomment-21791",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [sage-3148.patch](tarball://root/attachments/some-uuid/ticket3148/sage-3148.patch) by fwclarke created at 2008-05-10 12:09:32



---

archive/issue_comments_021792.json:
```json
{
    "body": "Looks good to me.  All the tests pass, and the patch definitely simplifies the code.",
    "created_at": "2008-05-23T07:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3148#issuecomment-21792",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  All the tests pass, and the patch definitely simplifies the code.



---

archive/issue_comments_021793.json:
```json
{
    "body": "Merged in Sage 3.0.2.rc0",
    "created_at": "2008-05-23T07:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3148#issuecomment-21793",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.rc0



---

archive/issue_comments_021794.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-23T07:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3148#issuecomment-21794",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
