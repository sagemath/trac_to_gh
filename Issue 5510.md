# Issue 5510: [with patch, not ready for review] update M4RI interface

archive/issues_005510.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @rhinton\n\nKeywords: m4ri, linear algebra\n\nThe attached patch(es) update Sage's interface to work with the HG version of M4RI available at: http://bitbucket.org/malb/m4ri/\n\nAlso, a dedicated (faster) `rank()` function was added for dense matrices over GF(2).\n\nIssue created by migration from https://trac.sagemath.org/ticket/5510\n\n",
    "created_at": "2009-03-13T15:38:21Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "[with patch, not ready for review] update M4RI interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5510",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @rhinton

Keywords: m4ri, linear algebra

The attached patch(es) update Sage's interface to work with the HG version of M4RI available at: http://bitbucket.org/malb/m4ri/

Also, a dedicated (faster) `rank()` function was added for dense matrices over GF(2).

Issue created by migration from https://trac.sagemath.org/ticket/5510





---

archive/issue_comments_042703.json:
```json
{
    "body": "Attachment [matrix_mod2_new_api_and_rank.patch](tarball://root/attachments/some-uuid/ticket5510/matrix_mod2_new_api_and_rank.patch) by @malb created at 2009-05-12 01:36:56\n\nPatch requires SPKG at:\n\n   http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20090512.spkg\n\nThis update is a requirement for updating PolyBoRi to 0.6.",
    "created_at": "2009-05-12T01:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5510#issuecomment-42703",
    "user": "https://github.com/malb"
}
```

Attachment [matrix_mod2_new_api_and_rank.patch](tarball://root/attachments/some-uuid/ticket5510/matrix_mod2_new_api_and_rank.patch) by @malb created at 2009-05-12 01:36:56

Patch requires SPKG at:

   http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20090512.spkg

This update is a requirement for updating PolyBoRi to 0.6.



---

archive/issue_comments_042704.json:
```json
{
    "body": "The spkg looks great.  Positive review for that.\n\nThe patch looks good to me as well.  Here are some timings:\n\nBEFORE:\n\n```\nsage: A = random_matrix(GF(2), 1000, 1000) \nsage: timeit('B=A.copy(); B.rank()')\n25 loops, best of 3: 8.42 ms per loop\nsage: timeit('B=A.copy(); B.rank()')\n25 loops, best of 3: 8.39 ms per loop\nsage: A = matrix(GF(2),10, 0) \nsage: timeit('B=A.copy(); B.rank()')\n625 loops, best of 3: 24.5 \u00b5s per loop\nsage: timeit('B=A.copy(); B.rank()')\n625 loops, best of 3: 24.3 \u00b5s per loop\n```\n\n\nAFTER\n\n```\nsage: A = random_matrix(GF(2), 1000, 1000) \nsage: timeit('B=A.copy(); B.rank()')\n125 loops, best of 3: 6.05 ms per loop\nsage: timeit('B=A.copy(); B.rank()')\n125 loops, best of 3: 6.09 ms per loop\nsage: A = matrix(GF(2),10, 0) \nsage: timeit('B=A.copy(); B.rank()')\n625 loops, best of 3: 38.7 \u00b5s per loop\nsage: timeit('B=A.copy(); B.rank()')\n625 loops, best of 3: 40.1 \u00b5s per loop\n```\n\n\nNote that the rank of a zero matrix is significantly longer (i.e., twice as long).  Malb, can you comment?\n\nIf malb addresses this performance regression sufficiently, then this is a positive review as far as I'm concerned for both the spkg and the patch.",
    "created_at": "2009-05-30T06:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5510#issuecomment-42704",
    "user": "https://github.com/jasongrout"
}
```

The spkg looks great.  Positive review for that.

The patch looks good to me as well.  Here are some timings:

BEFORE:

```
sage: A = random_matrix(GF(2), 1000, 1000) 
sage: timeit('B=A.copy(); B.rank()')
25 loops, best of 3: 8.42 ms per loop
sage: timeit('B=A.copy(); B.rank()')
25 loops, best of 3: 8.39 ms per loop
sage: A = matrix(GF(2),10, 0) 
sage: timeit('B=A.copy(); B.rank()')
625 loops, best of 3: 24.5 µs per loop
sage: timeit('B=A.copy(); B.rank()')
625 loops, best of 3: 24.3 µs per loop
```


AFTER

```
sage: A = random_matrix(GF(2), 1000, 1000) 
sage: timeit('B=A.copy(); B.rank()')
125 loops, best of 3: 6.05 ms per loop
sage: timeit('B=A.copy(); B.rank()')
125 loops, best of 3: 6.09 ms per loop
sage: A = matrix(GF(2),10, 0) 
sage: timeit('B=A.copy(); B.rank()')
625 loops, best of 3: 38.7 µs per loop
sage: timeit('B=A.copy(); B.rank()')
625 loops, best of 3: 40.1 µs per loop
```


Note that the rank of a zero matrix is significantly longer (i.e., twice as long).  Malb, can you comment?

If malb addresses this performance regression sufficiently, then this is a positive review as far as I'm concerned for both the spkg and the patch.



---

archive/issue_comments_042705.json:
```json
{
    "body": "Here is the code that used to be called:\n\n\n```\n    def rank(self):\n        x = self.fetch('rank')\n        if not x is None: return x\n        if self._nrows == 0 or self._ncols == 0:\n            return 0\n```\n\n\n\nAnd here is the code that is called now:\n\n\n```\n    def rank(self):\n        x = self.fetch('rank')\n        if not x is None:\n            return x\n        if self._nrows == 0 or self._ncols == 0:\n            return 0\n```\n\n\ni.e. they are identical and thus I have no idea to address this performance regression. Maybe the fetch is more expensive from a subclass or something? In any case, I don't think this should hold back the merge of this ticket.",
    "created_at": "2009-05-30T21:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5510#issuecomment-42705",
    "user": "https://github.com/malb"
}
```

Here is the code that used to be called:


```
    def rank(self):
        x = self.fetch('rank')
        if not x is None: return x
        if self._nrows == 0 or self._ncols == 0:
            return 0
```



And here is the code that is called now:


```
    def rank(self):
        x = self.fetch('rank')
        if not x is None:
            return x
        if self._nrows == 0 or self._ncols == 0:
            return 0
```


i.e. they are identical and thus I have no idea to address this performance regression. Maybe the fetch is more expensive from a subclass or something? In any case, I don't think this should hold back the merge of this ticket.



---

archive/issue_comments_042706.json:
```json
{
    "body": "Jason, can you comment on my reply?",
    "created_at": "2009-06-07T13:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5510#issuecomment-42706",
    "user": "https://github.com/malb"
}
```

Jason, can you comment on my reply?



---

archive/issue_comments_042707.json:
```json
{
    "body": "I thought your patch had a new rank function (at the bottom of the patch).  Isn't that what is called now?",
    "created_at": "2009-06-09T19:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5510#issuecomment-42707",
    "user": "https://github.com/jasongrout"
}
```

I thought your patch had a new rank function (at the bottom of the patch).  Isn't that what is called now?



---

archive/issue_comments_042708.json:
```json
{
    "body": "I re-ran my timings (on a different computer) in 4.0.  Here are the results:\n\nBEFORE:\n\n```\nsage: A = matrix(GF(2),100, 100,0)\nsage: timeit('A.rank(); A._clear_cache()')\n625 loops, best of 3: 47.9 \u00b5s per loop\nsage: A = matrix(GF(2),10, 10,0)\nsage: timeit('A.rank(); A._clear_cache()')\n625 loops, best of 3: 39.9 \u00b5s per loop\nsage: A = matrix(GF(2),100, 100,0)\nsage: timeit('A.rank(); A._clear_cache()')\n625 loops, best of 3: 47.7 \u00b5s per loop\nsage: A = matrix(GF(2),1000, 1000,0)\nsage: timeit('A.rank(); A._clear_cache()')\n625 loops, best of 3: 222 \u00b5s per loop\nsage: A = random_matrix(GF(2), 1000)\nsage: save(A,'m4ri.sobj')\nsage: timeit('A.rank(); A._clear_cache()')\n125 loops, best of 3: 6.85 ms per loop\nsage: A = random_matrix(GF(2), 100)\nsage: save(A,'m4ri2.sobj')\nsage: timeit('A.rank(); A._clear_cache()')\n625 loops, best of 3: 164 \u00b5s per loop\nsage: A = random_matrix(GF(2), 10000)\nsage: save(A,'m4ri3.sobj')\nsage: timeit('A.rank(); A._clear_cache()')\n5 loops, best of 3: 4.24 s per loop\n```\n\n\nAFTER\n\n```\nsage: A = matrix(GF(2),100, 100,0)\nsage: timeit('A.rank(); A._clear_cache()')\n625 loops, best of 3: 17.9 \u00b5s per loop\nsage: A = matrix(GF(2),10, 10,0)\nsage: timeit('A.rank(); A._clear_cache()')\n625 loops, best of 3: 13.4 \u00b5s per loop\nsage: A = matrix(GF(2),100, 100,0)\nsage: timeit('A.rank(); A._clear_cache()')\n625 loops, best of 3: 18.3 \u00b5s per loop\nsage: A = matrix(GF(2),1000, 1000,0)\nsage: timeit('A.rank(); A._clear_cache()')\n625 loops, best of 3: 205 \u00b5s per loop\nsage: A=load('./m4ri.sobj')\nsage: timeit('A.rank(); A._clear_cache()')\n125 loops, best of 3: 4.72 ms per loop\nsage: A=load('./m4ri2.sobj')\nsage: timeit('A.rank(); A._clear_cache()')\n625 loops, best of 3: 115 \u00b5s per loop\nsage: A=load('./m4ri3.sobj')\nsage: timeit('A.rank(); A._clear_cache()')\n5 loops, best of 3: 2.57 s per loop\n```\n\n\nThe new code is a clear winner.  I don't know what was happening before, but it seems great now.  Positive review.",
    "created_at": "2009-06-09T19:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5510#issuecomment-42708",
    "user": "https://github.com/jasongrout"
}
```

I re-ran my timings (on a different computer) in 4.0.  Here are the results:

BEFORE:

```
sage: A = matrix(GF(2),100, 100,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 47.9 µs per loop
sage: A = matrix(GF(2),10, 10,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 39.9 µs per loop
sage: A = matrix(GF(2),100, 100,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 47.7 µs per loop
sage: A = matrix(GF(2),1000, 1000,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 222 µs per loop
sage: A = random_matrix(GF(2), 1000)
sage: save(A,'m4ri.sobj')
sage: timeit('A.rank(); A._clear_cache()')
125 loops, best of 3: 6.85 ms per loop
sage: A = random_matrix(GF(2), 100)
sage: save(A,'m4ri2.sobj')
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 164 µs per loop
sage: A = random_matrix(GF(2), 10000)
sage: save(A,'m4ri3.sobj')
sage: timeit('A.rank(); A._clear_cache()')
5 loops, best of 3: 4.24 s per loop
```


AFTER

```
sage: A = matrix(GF(2),100, 100,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 17.9 µs per loop
sage: A = matrix(GF(2),10, 10,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 13.4 µs per loop
sage: A = matrix(GF(2),100, 100,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 18.3 µs per loop
sage: A = matrix(GF(2),1000, 1000,0)
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 205 µs per loop
sage: A=load('./m4ri.sobj')
sage: timeit('A.rank(); A._clear_cache()')
125 loops, best of 3: 4.72 ms per loop
sage: A=load('./m4ri2.sobj')
sage: timeit('A.rank(); A._clear_cache()')
625 loops, best of 3: 115 µs per loop
sage: A=load('./m4ri3.sobj')
sage: timeit('A.rank(); A._clear_cache()')
5 loops, best of 3: 2.57 s per loop
```


The new code is a clear winner.  I don't know what was happening before, but it seems great now.  Positive review.



---

archive/issue_comments_042709.json:
```json
{
    "body": "Ah, I think I know what was happening before.  I was creating a 10x0 matrix.  The copy was probably swamping the rank function.",
    "created_at": "2009-06-09T19:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5510#issuecomment-42709",
    "user": "https://github.com/jasongrout"
}
```

Ah, I think I know what was happening before.  I was creating a 10x0 matrix.  The copy was probably swamping the rank function.



---

archive/issue_comments_042710.json:
```json
{
    "body": "So, for the tour: calculating the rank of a random 10,000x10,000 GF(2) matrix takes approximately half the time it used to.  Nice!",
    "created_at": "2009-06-09T19:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5510#issuecomment-42710",
    "user": "https://github.com/jasongrout"
}
```

So, for the tour: calculating the rank of a random 10,000x10,000 GF(2) matrix takes approximately half the time it used to.  Nice!



---

archive/issue_comments_042711.json:
```json
{
    "body": "The dependencies are definitely not correct.  Even after 'touch sage/matrix/*' I can't compile it.\n\n\n```\nsage/rings/polynomial/polynomial_gf2x.cpp: In function \u00e2\ufffd\ufffdPyObject* __pyx_pf_4sage_5rings_10polynomial_15polynomial_gf2x_15Polynomial_GF2X_modular_compos                                                                                                                                                    sition(PyObject*, PyObject*, PyObject*)\u00e2\ufffd\ufffd:\nsage/rings/polynomial/polynomial_gf2x.cpp:10871: error: \u00e2\ufffd\ufffdstruct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_dense\u00e2\ufffd\ufffd has no member named \u00e2\ufffd\ufffd_en                                                                                                                                                ntries\u00e2\ufffd\ufffd\nsage/rings/polynomial/polynomial_gf2x.cpp:10941: error: \u00e2\ufffd\ufffdstruct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_dense\u00e2\ufffd\ufffd has no member named \u00e2\ufffd\ufffd_en                                                                                                                                                ntries\u00e2\ufffd\ufffd\nsage/rings/polynomial/polynomial_gf2x.cpp:11042: error: \u00e2\ufffd\ufffdstruct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_dense\u00e2\ufffd\ufffd has no member named \u00e2\ufffd\ufffd_en                                                                                                                                                ntries\u00e2\ufffd\ufffd\nsage/rings/polynomial/polynomial_gf2x.cpp:11227: error: \u00e2\ufffd\ufffdstruct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_dense\u00e2\ufffd\ufffd has no member named \u00e2\ufffd\ufffd_en                                                                                                                                                ntries\u00e2\ufffd\ufffd\nsage/rings/polynomial/polynomial_gf2x.cpp:11250: error: \u00e2\ufffd\ufffdstruct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_dense\u00e2\ufffd\ufffd has no member named \u00e2\ufffd\ufffd_en                                                                                                                                                ntries\u00e2\ufffd\ufffd\nsage/rings/polynomial/polynomial_gf2x.cpp:11475: error: \u00e2\ufffd\ufffdstruct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_dense\u00e2\ufffd\ufffd has no member named \u00e2\ufffd\ufffd_en                                                                                                                                                ntries\u00e2\ufffd\ufffd\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/numpy/core/include -I/scratch/ncalexan/sage-4.0.2.alpha1/local//include -I/scratch/ncalexan/sage-4.0.2.alpha1/local//include/csage -I/scratch/ncalexan/sage-4.0.2.alpha1/devel//sage/sage/ext -I/scratch/ncalexan/sage-4.0.2.alpha1/local/include/python2.5 -c sage/stats/hmm/chmm.c -o build/temp.linux-x86_64-2.5/sage/stats/hmm/chmm.o -w\ngcc -pthread -shared build/temp.linux-x86_64-2.5/sage/matrix/matrix2.o -L/scratch/ncalexan/sage-4.0.2.alpha1/local//lib -lcsage -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/matrix/matrix2.so\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/numpy/core/include -I/scratch/ncalexan/sage-4.0.2.alpha1/local//include -I/scratch/ncalexan/sage-4.0.2.alpha1/local//include/csage -I/scratch/ncalexan/sage-4.0.2.alpha1/devel//sage/sage/ext -I/scratch/ncalexan/sage-4.0.2.alpha1/local/include/python2.5 -c sage/stats/hmm/hmm.c -o build/temp.linux-x86_64-2.5/sage/stats/hmm/hmm.o -w\ngcc -pthread -shared build/temp.linux-x86_64-2.5/sage/matrix/matrix_integer_dense.o -L/scratch/ncalexan/sage-4.0.2.alpha1/local//lib -lcsage -liml -lgmp -lm -lcblas -latlas -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/matrix/matrix_integer_dense.so\nerror: command 'gcc' failed with exit status 1\nsage: There was an error installing modified sage library code.\n```\n\n\nAfter 'touch sage/polynomial/*' and a few retries, this still fails.  (I didn't try sage -ba.)  So I'm going to say needs work, to fix the dependencies.",
    "created_at": "2009-06-13T22:07:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5510#issuecomment-42711",
    "user": "https://github.com/ncalexan"
}
```

The dependencies are definitely not correct.  Even after 'touch sage/matrix/*' I can't compile it.


```
sage/rings/polynomial/polynomial_gf2x.cpp: In function â��PyObject* __pyx_pf_4sage_5rings_10polynomial_15polynomial_gf2x_15Polynomial_GF2X_modular_compos                                                                                                                                                    sition(PyObject*, PyObject*, PyObject*)â��:
sage/rings/polynomial/polynomial_gf2x.cpp:10871: error: â��struct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_denseâ�� has no member named â��_en                                                                                                                                                ntriesâ��
sage/rings/polynomial/polynomial_gf2x.cpp:10941: error: â��struct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_denseâ�� has no member named â��_en                                                                                                                                                ntriesâ��
sage/rings/polynomial/polynomial_gf2x.cpp:11042: error: â��struct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_denseâ�� has no member named â��_en                                                                                                                                                ntriesâ��
sage/rings/polynomial/polynomial_gf2x.cpp:11227: error: â��struct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_denseâ�� has no member named â��_en                                                                                                                                                ntriesâ��
sage/rings/polynomial/polynomial_gf2x.cpp:11250: error: â��struct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_denseâ�� has no member named â��_en                                                                                                                                                ntriesâ��
sage/rings/polynomial/polynomial_gf2x.cpp:11475: error: â��struct __pyx_obj_4sage_6matrix_17matrix_mod2_dense_Matrix_mod2_denseâ�� has no member named â��_en                                                                                                                                                ntriesâ��
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/numpy/core/include -I/scratch/ncalexan/sage-4.0.2.alpha1/local//include -I/scratch/ncalexan/sage-4.0.2.alpha1/local//include/csage -I/scratch/ncalexan/sage-4.0.2.alpha1/devel//sage/sage/ext -I/scratch/ncalexan/sage-4.0.2.alpha1/local/include/python2.5 -c sage/stats/hmm/chmm.c -o build/temp.linux-x86_64-2.5/sage/stats/hmm/chmm.o -w
gcc -pthread -shared build/temp.linux-x86_64-2.5/sage/matrix/matrix2.o -L/scratch/ncalexan/sage-4.0.2.alpha1/local//lib -lcsage -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/matrix/matrix2.so
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/numpy/core/include -I/scratch/ncalexan/sage-4.0.2.alpha1/local//include -I/scratch/ncalexan/sage-4.0.2.alpha1/local//include/csage -I/scratch/ncalexan/sage-4.0.2.alpha1/devel//sage/sage/ext -I/scratch/ncalexan/sage-4.0.2.alpha1/local/include/python2.5 -c sage/stats/hmm/hmm.c -o build/temp.linux-x86_64-2.5/sage/stats/hmm/hmm.o -w
gcc -pthread -shared build/temp.linux-x86_64-2.5/sage/matrix/matrix_integer_dense.o -L/scratch/ncalexan/sage-4.0.2.alpha1/local//lib -lcsage -liml -lgmp -lm -lcblas -latlas -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/matrix/matrix_integer_dense.so
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```


After 'touch sage/polynomial/*' and a few retries, this still fails.  (I didn't try sage -ba.)  So I'm going to say needs work, to fix the dependencies.



---

archive/issue_comments_042712.json:
```json
{
    "body": "You need to also install the spkg listed in the comments above.",
    "created_at": "2009-06-13T22:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5510#issuecomment-42712",
    "user": "https://github.com/jasongrout"
}
```

You need to also install the spkg listed in the comments above.



---

archive/issue_comments_042713.json:
```json
{
    "body": "With the spkg, works perfectly.  Sorry for the confusion.",
    "created_at": "2009-06-13T23:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5510#issuecomment-42713",
    "user": "https://github.com/ncalexan"
}
```

With the spkg, works perfectly.  Sorry for the confusion.



---

archive/issue_comments_042714.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T23:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5510#issuecomment-42714",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed
