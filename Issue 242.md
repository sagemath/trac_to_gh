# Issue 242: finite field arithmetic crash

archive/issues_000242.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nHere's one which must be an incorrect boundary check:\n \n----------------------------------------------------------------------\n----------------------------------------------------------------------\n \nsage: p = 2^32+15\nsage: FF = FiniteField(p)\nsage: a = FF(2)\nsage: a^0\n \n------------------------------------------------------------\nUnhandled SIGBUS: A bus error occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/242\n\n",
    "created_at": "2007-02-03T19:13:42Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "finite field arithmetic crash",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/242",
    "user": "was"
}
```
Assignee: somebody


```
Here's one which must be an incorrect boundary check:
 
----------------------------------------------------------------------
----------------------------------------------------------------------
 
sage: p = 2^32+15
sage: FF = FiniteField(p)
sage: a = FF(2)
sage: a^0
 
------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
```


Issue created by migration from https://trac.sagemath.org/ticket/242





---

archive/issue_comments_001076.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-02-07T10:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/242#issuecomment-1076",
    "user": "robertwb"
}
```

Resolution: fixed



---

archive/issue_comments_001077.json:
```json
{
    "body": "mpz_init wasn't being called on new integermod_gmp objects. Fixed, see patch at \n\nhttp://sage.math.washington.edu/home/robertwb/patches/2007-02-06-modint_fix.diff",
    "created_at": "2007-02-07T10:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/242#issuecomment-1077",
    "user": "robertwb"
}
```

mpz_init wasn't being called on new integermod_gmp objects. Fixed, see patch at 

http://sage.math.washington.edu/home/robertwb/patches/2007-02-06-modint_fix.diff
