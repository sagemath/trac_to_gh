# Issue 4753: make sparse * sparse = dense mod p like 50 frickin' times faster.

archive/issues_004753.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @craigcitro\n\ntitle says it all\n\nIssue created by migration from https://trac.sagemath.org/ticket/4753\n\n",
    "created_at": "2008-12-11T02:36:08Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "make sparse * sparse = dense mod p like 50 frickin' times faster.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4753",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @craigcitro

title says it all

Issue created by migration from https://trac.sagemath.org/ticket/4753





---

archive/issue_comments_035909.json:
```json
{
    "body": "Attachment [trac_4753-part1.patch](tarball://root/attachments/some-uuid/ticket4753/trac_4753-part1.patch) by @williamstein created at 2008-12-11 02:37:16",
    "created_at": "2008-12-11T02:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35909",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4753-part1.patch](tarball://root/attachments/some-uuid/ticket4753/trac_4753-part1.patch) by @williamstein created at 2008-12-11 02:37:16



---

archive/issue_comments_035910.json:
```json
{
    "body": "One issue is that in the patch, it should actually be \n\n```\n            sage: type(c)\n            <type 'sage.matrix.matrix_modn_dense.Matrix_modn_dense'>\n```\n\nAlso, I'm curious as to where the big speedup comes from?  For example,\n\n```\nsage: %time a*a\nCPU times: user 3.13 s, sys: 0.00 s, total: 3.13 s\nWall time: 3.25 s\n100 x 100 sparse matrix over Finite Field of size 10007\nsage: %time a._matrix_times_matrix_dense(a)\nCPU times: user 0.16 s, sys: 0.00 s, total: 0.16 s\nWall time: 0.17 s\n100 x 100 dense matrix over Finite Field of size 10007\n```\n\nIs it because you have a faster, more specialized underlying data structure?  Wouldn't it make more sense to add an optimized _mul_ method to matrix_modn_sparse and then have it do a normal (naive) conversion?",
    "created_at": "2008-12-11T08:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35910",
    "user": "https://github.com/mwhansen"
}
```

One issue is that in the patch, it should actually be 

```
            sage: type(c)
            <type 'sage.matrix.matrix_modn_dense.Matrix_modn_dense'>
```

Also, I'm curious as to where the big speedup comes from?  For example,

```
sage: %time a*a
CPU times: user 3.13 s, sys: 0.00 s, total: 3.13 s
Wall time: 3.25 s
100 x 100 sparse matrix over Finite Field of size 10007
sage: %time a._matrix_times_matrix_dense(a)
CPU times: user 0.16 s, sys: 0.00 s, total: 0.16 s
Wall time: 0.17 s
100 x 100 dense matrix over Finite Field of size 10007
```

Is it because you have a faster, more specialized underlying data structure?  Wouldn't it make more sense to add an optimized _mul_ method to matrix_modn_sparse and then have it do a normal (naive) conversion?



---

archive/issue_comments_035911.json:
```json
{
    "body": "This code wasn't ready for review yet -- William posted an initial patch after quickly writing some code in his office, and I'm going to clean it up and implement a few more things and post a patch tomorrow ...",
    "created_at": "2008-12-11T09:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35911",
    "user": "https://github.com/craigcitro"
}
```

This code wasn't ready for review yet -- William posted an initial patch after quickly writing some code in his office, and I'm going to clean it up and implement a few more things and post a patch tomorrow ...



---

archive/issue_comments_035912.json:
```json
{
    "body": "Replying to [comment:5 craigcitro]:\n> This code wasn't ready for review yet -- William posted an initial patch after quickly writing some code in his office, and I'm going to clean it up and implement a few more things and post a patch tomorrow ...\n\n\nI saw the patch, changed the subject, but did ping William about whether this code was supposed to be reviewed yet and didn't get an answer, so my bad :(\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T09:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35912",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 craigcitro]:
> This code wasn't ready for review yet -- William posted an initial patch after quickly writing some code in his office, and I'm going to clean it up and implement a few more things and post a patch tomorrow ...


I saw the patch, changed the subject, but did ping William about whether this code was supposed to be reviewed yet and didn't get an answer, so my bad :(

Cheers,

Michael



---

archive/issue_comments_035913.json:
```json
{
    "body": "> Is it because you have a faster, more specialized underlying data structure? \n> Wouldn't  it make more sense to add an optimized _mul_ method to\n> matrix_modn_sparse and then have it do a normal (naive) conversion?\n\n\nDefinitely *not*.  Much of the time would likely be spent with setting and inserting entries in the sparse output, which is an insanely expensive datastructure compared to the super-fast dense data structure. \n\nThat said, obviously a fast sparse*sparse = sparse should also be implemented, which would just be an easy cut and paste from Matrix_rational_sparse.\n\n -- william",
    "created_at": "2008-12-12T00:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35913",
    "user": "https://github.com/williamstein"
}
```

> Is it because you have a faster, more specialized underlying data structure? 
> Wouldn't  it make more sense to add an optimized _mul_ method to
> matrix_modn_sparse and then have it do a normal (naive) conversion?


Definitely *not*.  Much of the time would likely be spent with setting and inserting entries in the sparse output, which is an insanely expensive datastructure compared to the super-fast dense data structure. 

That said, obviously a fast sparse*sparse = sparse should also be implemented, which would just be an easy cut and paste from Matrix_rational_sparse.

 -- william



---

archive/issue_comments_035914.json:
```json
{
    "body": "I'm adding a second patch, which does two things: \n\n* cleans up the doctests for `_matrix_times_matrix_dense`\n* provides a fast `_matrix_times_matrix_`, so that `a*b` is now fast for a sparse mod N matrix `a`.\n\nNow it's ready for review.",
    "created_at": "2009-01-10T12:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35914",
    "user": "https://github.com/craigcitro"
}
```

I'm adding a second patch, which does two things: 

* cleans up the doctests for `_matrix_times_matrix_dense`
* provides a fast `_matrix_times_matrix_`, so that `a*b` is now fast for a sparse mod N matrix `a`.

Now it's ready for review.



---

archive/issue_comments_035915.json:
```json
{
    "body": "Attachment [trac_4753-part2.patch](tarball://root/attachments/some-uuid/ticket4753/trac_4753-part2.patch) by @craigcitro created at 2009-01-10 12:04:01",
    "created_at": "2009-01-10T12:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35915",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_4753-part2.patch](tarball://root/attachments/some-uuid/ticket4753/trac_4753-part2.patch) by @craigcitro created at 2009-01-10 12:04:01



---

archive/issue_comments_035916.json:
```json
{
    "body": "As Michael pointed out, it wouldn't hurt to have some comparison code.\n\nBEFORE:\n\n```\nsage: m = random_matrix(GF(10007), 100, 100, sparse=True)\n\nsage: %time m*m\nCPU times: user 3.36 s, sys: 0.03 s, total: 3.39 s\nWall time: 3.42 s\n100 x 100 sparse matrix over Finite Field of size 10007\n```\n\nAFTER:\n\n```\nsage: m = random_matrix(GF(10007), 100, 100, sparse=True)\n\nsage: %time m*m\nCPU times: user 0.09 s, sys: 0.00 s, total: 0.09 s\nWall time: 0.09 s\n100 x 100 sparse matrix over Finite Field of size 10007\n```",
    "created_at": "2009-01-10T12:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35916",
    "user": "https://github.com/craigcitro"
}
```

As Michael pointed out, it wouldn't hurt to have some comparison code.

BEFORE:

```
sage: m = random_matrix(GF(10007), 100, 100, sparse=True)

sage: %time m*m
CPU times: user 3.36 s, sys: 0.03 s, total: 3.39 s
Wall time: 3.42 s
100 x 100 sparse matrix over Finite Field of size 10007
```

AFTER:

```
sage: m = random_matrix(GF(10007), 100, 100, sparse=True)

sage: %time m*m
CPU times: user 0.09 s, sys: 0.00 s, total: 0.09 s
Wall time: 0.09 s
100 x 100 sparse matrix over Finite Field of size 10007
```



---

archive/issue_comments_035917.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-01-10T13:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35917",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_035918.json:
```json
{
    "body": "This patch set causes one doctest failure:\n\n```\nsage -t  \"devel/sage/sage/modular/modsym/ambient.py\"        \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.2.4.alpha0/devel/sage/sage/modular/modsym/ambient.py\", line 20:\n    sage: M.T(2).matrix().fcp('x')\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[6]>\", line 1, in <module>\n        M.T(Integer(2)).matrix().fcp('x')###line 20:\n    sage: M.T(2).matrix().fcp('x')\n      File \"/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/hecke_operator.py\", line 459, in matrix\n        self.__matrix = self.parent().hecke_matrix(self.__n)\n      File \"/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/algebra.py\", line 201, in hecke_matrix\n        return self.__M.hecke_matrix(n)\n      File \"/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/module.py\", line 917, in hecke_matrix\n        T = self._compute_hecke_matrix(n)\n      File \"/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/module.py\", line 117, in _compute_hecke_matrix\n        return self._compute_hecke_matrix_prime(n)\n      File \"/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py\", line 653, in _compute_hecke_matrix_prime\n        Tp = W._matrix_times_matrix_dense(R)\n      File \"matrix_modn_sparse.pyx\", line 370, in sage.matrix.matrix_modn_sparse.Matrix_modn_sparse._matrix_times_matrix_dense (sage/matrix/matrix_modn_sparse.c:6236)\n    TypeError: Cannot convert sage.matrix.matrix_mod2_dense.Matrix_mod2_dense to sage.matrix.matrix_modn_dense.Matrix_modn_dense\n**********************************************************************\n```\n\nCheers,\n\nMichael",
    "created_at": "2009-01-10T13:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35918",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch set causes one doctest failure:

```
sage -t  "devel/sage/sage/modular/modsym/ambient.py"        
**********************************************************************
File "/scratch/mabshoff/sage-3.2.4.alpha0/devel/sage/sage/modular/modsym/ambient.py", line 20:
    sage: M.T(2).matrix().fcp('x')
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[6]>", line 1, in <module>
        M.T(Integer(2)).matrix().fcp('x')###line 20:
    sage: M.T(2).matrix().fcp('x')
      File "/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/hecke_operator.py", line 459, in matrix
        self.__matrix = self.parent().hecke_matrix(self.__n)
      File "/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/algebra.py", line 201, in hecke_matrix
        return self.__M.hecke_matrix(n)
      File "/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/module.py", line 917, in hecke_matrix
        T = self._compute_hecke_matrix(n)
      File "/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/hecke/module.py", line 117, in _compute_hecke_matrix
        return self._compute_hecke_matrix_prime(n)
      File "/scratch/mabshoff/sage-3.2.4.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py", line 653, in _compute_hecke_matrix_prime
        Tp = W._matrix_times_matrix_dense(R)
      File "matrix_modn_sparse.pyx", line 370, in sage.matrix.matrix_modn_sparse.Matrix_modn_sparse._matrix_times_matrix_dense (sage/matrix/matrix_modn_sparse.c:6236)
    TypeError: Cannot convert sage.matrix.matrix_mod2_dense.Matrix_mod2_dense to sage.matrix.matrix_modn_dense.Matrix_modn_dense
**********************************************************************
```

Cheers,

Michael



---

archive/issue_comments_035919.json:
```json
{
    "body": "Attachment [trac_4753-part3.patch](tarball://root/attachments/some-uuid/ticket4753/trac_4753-part3.patch) by @craigcitro created at 2009-01-11 08:59:14",
    "created_at": "2009-01-11T08:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35919",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_4753-part3.patch](tarball://root/attachments/some-uuid/ticket4753/trac_4753-part3.patch) by @craigcitro created at 2009-01-11 08:59:14



---

archive/issue_comments_035920.json:
```json
{
    "body": "Ok, new patch should fix that. The problem was fairly straightforward: we didn't think to test in the case of `GF(2)`, and in that case, the actual type for the result (`matrix_mod2_dense`) wasn't a subclass of `matrix_modn_dense`, so we were rightfully getting a type error.",
    "created_at": "2009-01-11T09:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35920",
    "user": "https://github.com/craigcitro"
}
```

Ok, new patch should fix that. The problem was fairly straightforward: we didn't think to test in the case of `GF(2)`, and in that case, the actual type for the result (`matrix_mod2_dense`) wasn't a subclass of `matrix_modn_dense`, so we were rightfully getting a type error.



---

archive/issue_comments_035921.json:
```json
{
    "body": "i applied all three patches to a clean sage-3.2.3 on sage.math and doctested matrix and got:\n\n```\nThe following tests failed:\n\n        sage -t  devel/sage/sage/matrix/matrix_modn_sparse.pyx # 2 doctests failed\n        sage -t  devel/sage/sage/matrix/matrix2.pyx # 3 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 111.4 seconds\n```",
    "created_at": "2009-01-11T20:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35921",
    "user": "https://github.com/williamstein"
}
```

i applied all three patches to a clean sage-3.2.3 on sage.math and doctested matrix and got:

```
The following tests failed:

        sage -t  devel/sage/sage/matrix/matrix_modn_sparse.pyx # 2 doctests failed
        sage -t  devel/sage/sage/matrix/matrix2.pyx # 3 doctests failed
----------------------------------------------------------------------
Total time for all tests: 111.4 seconds
```



---

archive/issue_comments_035922.json:
```json
{
    "body": "Ok, problem solved. The issue is that `set_unsafe` take different input types for `matrix_modn_dense` and `matrix_mod2_dense` -- I only looked at the latter, mistakenly assuming they would be the same. \n\nI wised up, and tested `sage/matrix/` and `sage/modular/modsym` before posting -- no failures.",
    "created_at": "2009-01-12T04:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35922",
    "user": "https://github.com/craigcitro"
}
```

Ok, problem solved. The issue is that `set_unsafe` take different input types for `matrix_modn_dense` and `matrix_mod2_dense` -- I only looked at the latter, mistakenly assuming they would be the same. 

I wised up, and tested `sage/matrix/` and `sage/modular/modsym` before posting -- no failures.



---

archive/issue_comments_035923.json:
```json
{
    "body": "Attachment [trac_4753-part4.patch](tarball://root/attachments/some-uuid/ticket4753/trac_4753-part4.patch) by @williamstein created at 2009-01-12 15:07:53",
    "created_at": "2009-01-12T15:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35923",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4753-part4.patch](tarball://root/attachments/some-uuid/ticket4753/trac_4753-part4.patch) by @williamstein created at 2009-01-12 15:07:53



---

archive/issue_comments_035924.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T13:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35924",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035925.json:
```json
{
    "body": "Merged all four patches in Sage 3.3.alpha0\n\nCheers,\n\nMichael",
    "created_at": "2009-01-18T13:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4753#issuecomment-35925",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all four patches in Sage 3.3.alpha0

Cheers,

Michael



---

archive/issue_events_010868.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-18T13:54:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4753",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4753#event-10868"
}
```
