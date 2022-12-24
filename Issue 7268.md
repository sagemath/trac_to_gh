# Issue 7268: GLPK : named constraints and variables, export functions ...

archive/issues_007268.json:
```json
{
    "body": "Assignee: tbd\n\nHello everybody !\n\nThis is an update of the GLPK package to match the changes in ``numerical.mip``. Here is the list of changes :\n\n* Names for the objective function, the whole problem, variables and constraints can be set through the newly exposed GLPK functions\n* A problem can be exported to MPS or LP files\n* GLPK now returns Exceptions when it fails ( it used to silently return the 0 solution ).\n* As solveGLPK, write_mps and write_lp all need the problem to be built as a GLPK structure, a new function  ``build_glp_prob`` does this job and is used by the three of them.\n\nComments have also been added when felt necessary. The code should be more efficient (and Cythonized) in this version ( this was the whole purpose of redefining the structure of ``numerical.mip`` )\n\nThe spkg is available on sagemath at : ~ncohen/glpk-4.38.p3.spkg\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7268\n\n",
    "created_at": "2009-10-23T15:26:10Z",
    "labels": [
        "packages: optional",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "GLPK : named constraints and variables, export functions ...",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7268",
    "user": "@nathanncohen"
}
```
Assignee: tbd

Hello everybody !

This is an update of the GLPK package to match the changes in ``numerical.mip``. Here is the list of changes :

* Names for the objective function, the whole problem, variables and constraints can be set through the newly exposed GLPK functions
* A problem can be exported to MPS or LP files
* GLPK now returns Exceptions when it fails ( it used to silently return the 0 solution ).
* As solveGLPK, write_mps and write_lp all need the problem to be built as a GLPK structure, a new function  ``build_glp_prob`` does this job and is used by the three of them.

Comments have also been added when felt necessary. The code should be more efficient (and Cythonized) in this version ( this was the whole purpose of redefining the structure of ``numerical.mip`` )

The spkg is available on sagemath at : ~ncohen/glpk-4.38.p3.spkg

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7268





---

archive/issue_comments_060391.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-23T15:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60391",
    "user": "@nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060392.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-25T03:58:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60392",
    "user": "mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060393.json:
```json
{
    "body": "The package installs OK on Sage 4.3.alpha0. Here are some documentation issues in the file `patch/mipGlpk.pyx` that I think need to be addressed:\n\n1. the function `solve_glpk()` --- document the input `log` and `objective_only`, and explain the expected output (if any).\n2. the function `write_mps()` --- document the input `filename`  and `modern`, and explain the expected output (if any).\n3. the function `write_lp()` --- document what this function does. Also document the input `filename` and explain the expected output (if any).",
    "created_at": "2009-11-25T03:58:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60393",
    "user": "mvngu"
}
```

The package installs OK on Sage 4.3.alpha0. Here are some documentation issues in the file `patch/mipGlpk.pyx` that I think need to be addressed:

1. the function `solve_glpk()` --- document the input `log` and `objective_only`, and explain the expected output (if any).
2. the function `write_mps()` --- document the input `filename`  and `modern`, and explain the expected output (if any).
3. the function `write_lp()` --- document what this function does. Also document the input `filename` and explain the expected output (if any).



---

archive/issue_comments_060394.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-25T07:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60394",
    "user": "@nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060395.json:
```json
{
    "body": "Sorry !! :-)\n\nI wrote these in the wrappers for these functions in class MixedIntegerLinearProgram but forgot to copy them there.... Both files updated ! :-)",
    "created_at": "2009-11-25T07:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60395",
    "user": "@nathanncohen"
}
```

Sorry !! :-)

I wrote these in the wrappers for these functions in class MixedIntegerLinearProgram but forgot to copy them there.... Both files updated ! :-)



---

archive/issue_comments_060396.json:
```json
{
    "body": "A new SPKG is available at\n\n   http://sage.math.washington.edu/home/malb/spkgs/glpk-4.38.p4.spkg\n\nI give Nathan's SPKG a positive review if my referee patch is accepted. The referee patch fixes a mem leak and makes some of the code in the Cython wrapper more Pythonic (I also reverted some pre-mature optimisation which wouldn't speed things up)\n\nI am attaching the patch here for convenience (it is applied in p4 linked above).",
    "created_at": "2009-12-01T17:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60396",
    "user": "@malb"
}
```

A new SPKG is available at

   http://sage.math.washington.edu/home/malb/spkgs/glpk-4.38.p4.spkg

I give Nathan's SPKG a positive review if my referee patch is accepted. The referee patch fixes a mem leak and makes some of the code in the Cython wrapper more Pythonic (I also reverted some pre-mature optimisation which wouldn't speed things up)

I am attaching the patch here for convenience (it is applied in p4 linked above).



---

archive/issue_comments_060397.json:
```json
{
    "body": "Your new spkg file contains a build/ directory and a file .cpp in the patch/ directory ( it seems you installed the patch then packaged it without removing these temporary files ). Coild you update it ?\n\nBesides, is there any way for me to get the diff files since the last version ? I am still not that used to mercurial :-)\n\nThank youuuuuuuuuu !!!\n\nNathann",
    "created_at": "2009-12-01T17:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60397",
    "user": "@nathanncohen"
}
```

Your new spkg file contains a build/ directory and a file .cpp in the patch/ directory ( it seems you installed the patch then packaged it without removing these temporary files ). Coild you update it ?

Besides, is there any way for me to get the diff files since the last version ? I am still not that used to mercurial :-)

Thank youuuuuuuuuu !!!

Nathann



---

archive/issue_comments_060398.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-01T17:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60398",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060399.json:
```json
{
    "body": "I've updated the SPKG and I'll attach the diff.",
    "created_at": "2009-12-01T17:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60399",
    "user": "@malb"
}
```

I've updated the SPKG and I'll attach the diff.



---

archive/issue_comments_060400.json:
```json
{
    "body": "Attachment [glpk_sage_free.patch](tarball://root/attachments/some-uuid/ticket7268/glpk_sage_free.patch) by @malb created at 2009-12-01 17:43:57",
    "created_at": "2009-12-01T17:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60400",
    "user": "@malb"
}
```

Attachment [glpk_sage_free.patch](tarball://root/attachments/some-uuid/ticket7268/glpk_sage_free.patch) by @malb created at 2009-12-01 17:43:57



---

archive/issue_comments_060401.json:
```json
{
    "body": "Looks good :-)\n\nTwo questions though :\n\n* Why do you replace == and != by is and is not ?\n* is enumerating range(500) faster than 0<= i< 500 or is there another reason ?\n* Why did you remove the leading 'r' before the docstrings ? I was under the impression they were requried for the docstring to display correctly...\n\nI knew nothing about enumerate()... I'll remember this one ! :-)\n\nNathann",
    "created_at": "2009-12-01T17:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60401",
    "user": "@nathanncohen"
}
```

Looks good :-)

Two questions though :

* Why do you replace == and != by is and is not ?
* is enumerating range(500) faster than 0<= i< 500 or is there another reason ?
* Why did you remove the leading 'r' before the docstrings ? I was under the impression they were requried for the docstring to display correctly...

I knew nothing about enumerate()... I'll remember this one ! :-)

Nathann



---

archive/issue_comments_060402.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2009-12-01T17:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60402",
    "user": "@nathanncohen"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_060403.json:
```json
{
    "body": "> Why do you replace == and != by is and is not ?\n\nFalse and None are unique objects thus it is sufficient to compare by checking identities. Feel free to change it back, though.\n\n>     * is enumerating range(500) faster than 0<= i< 500 or is there another reason ?\n\nCython will write 0<= i < 500 automatically, so you can just write proper Python code and Cython will optimise it for you.\n\n>  Why did you remove the leading 'r' before the docstrings ? I was under the impression they were requried for the docstring to display correctly...\n\nOnly if they contain a backslash.",
    "created_at": "2009-12-01T18:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60403",
    "user": "@malb"
}
```

> Why do you replace == and != by is and is not ?

False and None are unique objects thus it is sufficient to compare by checking identities. Feel free to change it back, though.

>     * is enumerating range(500) faster than 0<= i< 500 or is there another reason ?

Cython will write 0<= i < 500 automatically, so you can just write proper Python code and Cython will optimise it for you.

>  Why did you remove the leading 'r' before the docstrings ? I was under the impression they were requried for the docstring to display correctly...

Only if they contain a backslash.



---

archive/issue_comments_060404.json:
```json
{
    "body": "Then.... Positive review ! And thank you for your answers and your help ! :-)\n\nNathann",
    "created_at": "2009-12-01T18:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60404",
    "user": "@nathanncohen"
}
```

Then.... Positive review ! And thank you for your answers and your help ! :-)

Nathann



---

archive/issue_comments_060405.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-12-01T18:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60405",
    "user": "@nathanncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_060406.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-01T18:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60406",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060407.json:
```json
{
    "body": "Depends on #7270 !!!!!!!!!!!!!!!",
    "created_at": "2009-12-01T18:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60407",
    "user": "@nathanncohen"
}
```

Depends on #7270 !!!!!!!!!!!!!!!



---

archive/issue_comments_060408.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-02T07:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60408",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_060409.json:
```json
{
    "body": "Merged in the with the optional packages.",
    "created_at": "2009-12-02T07:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60409",
    "user": "@mwhansen"
}
```

Merged in the with the optional packages.



---

archive/issue_comments_060410.json:
```json
{
    "body": "FYI: enumerate is now recognized and sped up by Cython (in version 0.12, which will be in the next version of Sage).  See http://trac.cython.org/cython_trac/ticket/316\n\nSo hooray!",
    "created_at": "2009-12-03T14:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60410",
    "user": "@jasongrout"
}
```

FYI: enumerate is now recognized and sped up by Cython (in version 0.12, which will be in the next version of Sage).  See http://trac.cython.org/cython_trac/ticket/316

So hooray!



---

archive/issue_comments_060411.json:
```json
{
    "body": "Thank you    !! :-)\n\nIf you are interested by (shorter) reviews, I am splitting the big Flow patch into small ones... The flow is already available, the matching will be available soon too, and the others ( less important ) will follow.",
    "created_at": "2009-12-03T14:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7268#issuecomment-60411",
    "user": "@nathanncohen"
}
```

Thank you    !! :-)

If you are interested by (shorter) reviews, I am splitting the big Flow patch into small ones... The flow is already available, the matching will be available soon too, and the others ( less important ) will follow.
