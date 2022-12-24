# Issue 4307: bad error message in SupersingularModule constructor

archive/issues_004307.json:
```json
{
    "body": "Assignee: @craigcitro\n\n\n```\nsage: SupersingularModule(15)\nTraceback (most recent call last):\n...\nValueError: order of finite field must be a prime power\n```\n\n\nThe error message should say something like:\n\n```\nNotImplementedError: supersingular module of non-prime level not yet implemented\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4307\n\n",
    "created_at": "2008-10-16T09:21:45Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "bad error message in SupersingularModule constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4307",
    "user": "@williamstein"
}
```
Assignee: @craigcitro


```
sage: SupersingularModule(15)
Traceback (most recent call last):
...
ValueError: order of finite field must be a prime power
```


The error message should say something like:

```
NotImplementedError: supersingular module of non-prime level not yet implemented
```


Issue created by migration from https://trac.sagemath.org/ticket/4307





---

archive/issue_comments_031525.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-10-16T09:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4307#issuecomment-31525",
    "user": "@williamstein"
}
```

Changing priority from major to minor.



---

archive/issue_comments_031526.json:
```json
{
    "body": "Having looked at the code in ssmod.py, it seems to me that any nontrivial functionality is only implemented for level 1 at the moment.  Two things that I tried: dimension() and hecke_matrix().\n\nThe attached patch raises ValueErrors if the characteristic is not prime or if the level is not coprime to the characteristic, and a NotImplementedError if the level is > 1.\n\nExtending the functionality in ssmod.py to general levels is right up my alley, so I'll look into doing it in the near future.  The code could also use more documentation and tests.",
    "created_at": "2008-10-18T04:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4307#issuecomment-31526",
    "user": "@aghitza"
}
```

Having looked at the code in ssmod.py, it seems to me that any nontrivial functionality is only implemented for level 1 at the moment.  Two things that I tried: dimension() and hecke_matrix().

The attached patch raises ValueErrors if the characteristic is not prime or if the level is not coprime to the characteristic, and a NotImplementedError if the level is > 1.

Extending the functionality in ssmod.py to general levels is right up my alley, so I'll look into doing it in the near future.  The code could also use more documentation and tests.



---

archive/issue_comments_031527.json:
```json
{
    "body": "Alex,\n\nplease add doctests that show the new behavior to the not yet existing class SupersingularModule(hecke.HeckeModule_free_module) docstring.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-20T16:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4307#issuecomment-31527",
    "user": "mabshoff"
}
```

Alex,

please add doctests that show the new behavior to the not yet existing class SupersingularModule(hecke.HeckeModule_free_module) docstring.

Cheers,

Michael



---

archive/issue_comments_031528.json:
```json
{
    "body": "Attachment [trac4307-ssmod_init.patch](tarball://root/attachments/some-uuid/ticket4307/trac4307-ssmod_init.patch) by @aghitza created at 2008-10-20 22:01:28\n\nYes.  Done, and replaced the patch.",
    "created_at": "2008-10-20T22:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4307#issuecomment-31528",
    "user": "@aghitza"
}
```

Attachment [trac4307-ssmod_init.patch](tarball://root/attachments/some-uuid/ticket4307/trac4307-ssmod_init.patch) by @aghitza created at 2008-10-20 22:01:28

Yes.  Done, and replaced the patch.



---

archive/issue_comments_031529.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-10-22T04:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4307#issuecomment-31529",
    "user": "@craigcitro"
}
```

Looks good.



---

archive/issue_comments_031530.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-26T01:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4307#issuecomment-31530",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha1



---

archive/issue_comments_031531.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T01:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4307#issuecomment-31531",
    "user": "mabshoff"
}
```

Resolution: fixed
