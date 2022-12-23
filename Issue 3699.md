# Issue 3699: rewrite free_module.py to use basis matrices everywhere

archive/issues_003699.json:
```json
{
    "body": "Assignee: tbd\n\nYou should only do this on top of patch #3514.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3699\n\n",
    "created_at": "2008-07-21T21:39:05Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "rewrite free_module.py to use basis matrices everywhere",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3699",
    "user": "mhansen"
}
```
Assignee: tbd

You should only do this on top of patch #3514.

Issue created by migration from https://trac.sagemath.org/ticket/3699





---

archive/issue_comments_026244.json:
```json
{
    "body": "I'm not sure exactly what you mean here, but if it would involve computing the basis_matrix for all `FreeModules` (even in the `FreeModule_ambient` case, where currently the basis_matrix is only computed lazily when requested) I think it's a bad idea unless the following can be vastly sped up:\n\n```\nsage: %time K = FreeModule(ZZ, 2000)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\nsage: %time _ = K.basis_matrix()\nCPU times: user 191.08 s, sys: 19.63 s, total: 210.71 s\nWall time: 210.69 s\n```\n",
    "created_at": "2008-08-02T14:12:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3699#issuecomment-26244",
    "user": "cwitty"
}
```

I'm not sure exactly what you mean here, but if it would involve computing the basis_matrix for all `FreeModules` (even in the `FreeModule_ambient` case, where currently the basis_matrix is only computed lazily when requested) I think it's a bad idea unless the following can be vastly sped up:

```
sage: %time K = FreeModule(ZZ, 2000)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: %time _ = K.basis_matrix()
CPU times: user 191.08 s, sys: 19.63 s, total: 210.71 s
Wall time: 210.69 s
```




---

archive/issue_comments_026245.json:
```json
{
    "body": "> I'm not sure exactly what you mean here, but if it would involve computing the \n> basis_matrix for all FreeModules (even in the FreeModule_ambient case, where\n> currently the basis_matrix is only computed lazily when requested) I think \n> it's a bad idea unless the following can be vastly sped up:\n\nIt would *only* involve computing the basis matrix for proper *submodules*, where\ncurrently exactly equivalent (namely a list of basis vectors) but vastly \nharder to work with data is computed and carried around. \n\nBy the way, regarding your example, that is just creating the 2000x2000 identity\nmatrix, which can be sped up, see:\n\n```\nsage: time a = identity_matrix(ZZ,2000)\nCPU times: user 0.27 s, sys: 0.05 s, total: 0.32 s\n```\n\n\nA cheap easy patch that vastly speeds up sage would be one that optimizes the\nbasis_matrix function for ambient free modules to just call the identity matrix\ncommand :-).",
    "created_at": "2008-08-03T17:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3699#issuecomment-26245",
    "user": "was"
}
```

> I'm not sure exactly what you mean here, but if it would involve computing the 
> basis_matrix for all FreeModules (even in the FreeModule_ambient case, where
> currently the basis_matrix is only computed lazily when requested) I think 
> it's a bad idea unless the following can be vastly sped up:

It would *only* involve computing the basis matrix for proper *submodules*, where
currently exactly equivalent (namely a list of basis vectors) but vastly 
harder to work with data is computed and carried around. 

By the way, regarding your example, that is just creating the 2000x2000 identity
matrix, which can be sped up, see:

```
sage: time a = identity_matrix(ZZ,2000)
CPU times: user 0.27 s, sys: 0.05 s, total: 0.32 s
```


A cheap easy patch that vastly speeds up sage would be one that optimizes the
basis_matrix function for ambient free modules to just call the identity matrix
command :-).



---

archive/issue_comments_026246.json:
```json
{
    "body": "Attachment\n\nPatch attached which does what I think was intended.  Based on 3.4, all tests in sage/modules should pass.",
    "created_at": "2009-03-22T18:31:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3699#issuecomment-26246",
    "user": "cremona"
}
```

Attachment

Patch attached which does what I think was intended.  Based on 3.4, all tests in sage/modules should pass.



---

archive/issue_comments_026247.json:
```json
{
    "body": "This still applies fine to 4.0 and is still in need of a review -- should be very quick!  All doctests in sage/modules pass.",
    "created_at": "2009-05-30T15:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3699#issuecomment-26247",
    "user": "cremona"
}
```

This still applies fine to 4.0 and is still in need of a review -- should be very quick!  All doctests in sage/modules pass.



---

archive/issue_comments_026248.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-06-02T08:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3699#issuecomment-26248",
    "user": "AlexGhitza"
}
```

Looks good to me.



---

archive/issue_comments_026249.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-03T18:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3699#issuecomment-26249",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_026250.json:
```json
{
    "body": "Merged in 4.0.1.rc0.",
    "created_at": "2009-06-03T18:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3699#issuecomment-26250",
    "user": "mhansen"
}
```

Merged in 4.0.1.rc0.
