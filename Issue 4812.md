# Issue 4812: [with patch, needs review] matrix_plot is broken for matrices with "complicated" base rings

archive/issues_004812.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nHello all,\n\nI'm trying to run the following code:\n\ns     = 7\ns2    = 2^s\nP.<x> = GF(2)[]\nM     = matrix(parent(x),s2)\nfor i in range(s2):\n  p  = (1+x)^i\n  pc = p.coeffs()\n  a  = pc.count(1)\n  for j in range(a):\n    idx        = pc.index(1)\n    M[i,idx+j] = pc.pop(idx)\nmatrixprogram = matrix_plot(M,cmap='Greys')\n\n...but with 3.2.1, it complains:\n\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/home/drake/.sage/temp/klee/11408/_tmp_foo_sage_2.py in <module>()\n    16        M[i,idx+j] = pc.pop(idx)\n    17\n---> 18 matrixprogram = matrix_plot(M,cmap='Greys')     19\n    20\n\n/opt/sage-3.2.1/local/lib/python2.5/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)\n   279                 options['__original_opts'] = kwds\n   280             options.update(kwds)\n--> 281             return func(*args, **options)\n   282\n   283\n\n/opt/sage-3.2.1/local/lib/python2.5/site-packages/sage/plot/matrix_plot.pyc in matrix_plot(mat, **options)\n   123         xrange = (0, len(mat[0]))\n   124         yrange = (0, len(mat))\n--> 125     xy_data_array = [array(r, dtype=float) for r in mat]\n   126\n   127     g = Graphics()\n\n/opt/sage-3.2.1/local/lib/python2.5/site-packages/numpy/oldnumeric/functions.pyc in array(sequence, typecode, copy, savespace, dtype)\n    77 def array(sequence, typecode=None, copy=1, savespace=0, dtype=None):\n    78     dtype = convtypecode2(typecode, dtype)\n---> 79     return mu.array(sequence, dtype, copy=copy)\n    80\n    81 def sarray(a, typecode=None, copy=False, dtype=None):\n\nValueError: setting an array element with a sequence.\n\n\nI know this used to work, because the example distributed with SageTeX\nhas it! See example.{tex,pdf} from\nhttp://tug.ctan.org/tex-archive/macros/latex/contrib/sagetex/. Is the\nabove code still considered correct, or is there now a problem with\nmatrix_plot? The matrix M above has all 1's and 0's despite its parent\nbeing GF(2)[x], so perhaps this is a coercion thing?\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4812\n\n",
    "created_at": "2008-12-16T11:51:31Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "[with patch, needs review] matrix_plot is broken for matrices with \"complicated\" base rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4812",
    "user": "@mwhansen"
}
```
Assignee: @williamstein


```
Hello all,

I'm trying to run the following code:

s     = 7
s2    = 2^s
P.<x> = GF(2)[]
M     = matrix(parent(x),s2)
for i in range(s2):
  p  = (1+x)^i
  pc = p.coeffs()
  a  = pc.count(1)
  for j in range(a):
    idx        = pc.index(1)
    M[i,idx+j] = pc.pop(idx)
matrixprogram = matrix_plot(M,cmap='Greys')

...but with 3.2.1, it complains:

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/drake/.sage/temp/klee/11408/_tmp_foo_sage_2.py in <module>()
    16        M[i,idx+j] = pc.pop(idx)
    17
---> 18 matrixprogram = matrix_plot(M,cmap='Greys')     19
    20

/opt/sage-3.2.1/local/lib/python2.5/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)
   279                 options['__original_opts'] = kwds
   280             options.update(kwds)
--> 281             return func(*args, **options)
   282
   283

/opt/sage-3.2.1/local/lib/python2.5/site-packages/sage/plot/matrix_plot.pyc in matrix_plot(mat, **options)
   123         xrange = (0, len(mat[0]))
   124         yrange = (0, len(mat))
--> 125     xy_data_array = [array(r, dtype=float) for r in mat]
   126
   127     g = Graphics()

/opt/sage-3.2.1/local/lib/python2.5/site-packages/numpy/oldnumeric/functions.pyc in array(sequence, typecode, copy, savespace, dtype)
    77 def array(sequence, typecode=None, copy=1, savespace=0, dtype=None):
    78     dtype = convtypecode2(typecode, dtype)
---> 79     return mu.array(sequence, dtype, copy=copy)
    80
    81 def sarray(a, typecode=None, copy=False, dtype=None):

ValueError: setting an array element with a sequence.


I know this used to work, because the example distributed with SageTeX
has it! See example.{tex,pdf} from
http://tug.ctan.org/tex-archive/macros/latex/contrib/sagetex/. Is the
above code still considered correct, or is there now a problem with
matrix_plot? The matrix M above has all 1's and 0's despite its parent
being GF(2)[x], so perhaps this is a coercion thing?
```


Issue created by migration from https://trac.sagemath.org/ticket/4812





---

archive/issue_comments_036479.json:
```json
{
    "body": "Code looks good, the SageTeX example file now works...positive review.",
    "created_at": "2008-12-16T13:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4812#issuecomment-36479",
    "user": "@dandrake"
}
```

Code looks good, the SageTeX example file now works...positive review.



---

archive/issue_comments_036480.json:
```json
{
    "body": "This patch needs some fixing:\n\n```\nsage -t -long \"devel/sage/sage/plot/matrix_plot.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/devel/sage/sage/plot/matrix_plot.py\", line 129:\n    sage: matrix_plot(random_matrix(P, 3, 3))\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: can not convert array entries to floating point numbers\nGot:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[15]>\", line 1, in <module>\n        matrix_plot(random_matrix(P, Integer(3), Integer(3)))###line 129:\n    sage: matrix_plot(random_matrix(P, 3, 3))\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/plot/misc.py\", line 285, in wrapper\n        return func(*args, **options)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/plot/matrix_plot.py\", line 150, in matrix_plot\n        mat = mat.change_ring(RDF).numpy()\n      File \"matrix0.pyx\", line 888, in sage.matrix.matrix0.Matrix.change_ring (sage/matrix/matrix0.c:5304)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py\", line 354, in __call__\n        return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py\", line 979, in matrix\n        return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce)\n      File \"matrix_double_dense.pyx\", line 222, in sage.matrix.matrix_double_dense.Matrix_double_dense.__init__ (sage/matrix/matrix_double_dense.c:2203)\n      File \"polynomial_element.pyx\", line 649, in sage.rings.polynomial.polynomial_element.Polynomial.__float__ (sage/rings/polynomial/polynomial_element.c:7124)\n    TypeError: cannot coerce nonconstant polynomial to float\n**********************************************************************\n1 items had failures:\n   1 of  18 in __main__.example_3\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.2.rc1/tmp/.doctest_matrix_plot.py\n         [5.1 s]\nexit code: 1024\n```\n\nDan: Please don't give positive reviews without at least doctesting all changed files ;)\n\nThe fix here seems obvious since only the traceback message has changed.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-17T14:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4812#issuecomment-36480",
    "user": "mabshoff"
}
```

This patch needs some fixing:

```
sage -t -long "devel/sage/sage/plot/matrix_plot.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/devel/sage/sage/plot/matrix_plot.py", line 129:
    sage: matrix_plot(random_matrix(P, 3, 3))
Expected:
    Traceback (most recent call last):
    ...
    ValueError: can not convert array entries to floating point numbers
Got:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[15]>", line 1, in <module>
        matrix_plot(random_matrix(P, Integer(3), Integer(3)))###line 129:
    sage: matrix_plot(random_matrix(P, 3, 3))
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/plot/misc.py", line 285, in wrapper
        return func(*args, **options)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/plot/matrix_plot.py", line 150, in matrix_plot
        mat = mat.change_ring(RDF).numpy()
      File "matrix0.pyx", line 888, in sage.matrix.matrix0.Matrix.change_ring (sage/matrix/matrix0.c:5304)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py", line 354, in __call__
        return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py", line 979, in matrix
        return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce)
      File "matrix_double_dense.pyx", line 222, in sage.matrix.matrix_double_dense.Matrix_double_dense.__init__ (sage/matrix/matrix_double_dense.c:2203)
      File "polynomial_element.pyx", line 649, in sage.rings.polynomial.polynomial_element.Polynomial.__float__ (sage/rings/polynomial/polynomial_element.c:7124)
    TypeError: cannot coerce nonconstant polynomial to float
**********************************************************************
1 items had failures:
   1 of  18 in __main__.example_3
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.2.rc1/tmp/.doctest_matrix_plot.py
         [5.1 s]
exit code: 1024
```

Dan: Please don't give positive reviews without at least doctesting all changed files ;)

The fix here seems obvious since only the traceback message has changed.

Cheers,

Michael



---

archive/issue_comments_036481.json:
```json
{
    "body": "Attachment [trac_4812.patch](tarball://root/attachments/some-uuid/ticket4812/trac_4812.patch) by @mwhansen created at 2008-12-22 16:37:06",
    "created_at": "2008-12-22T16:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4812#issuecomment-36481",
    "user": "@mwhansen"
}
```

Attachment [trac_4812.patch](tarball://root/attachments/some-uuid/ticket4812/trac_4812.patch) by @mwhansen created at 2008-12-22 16:37:06



---

archive/issue_comments_036482.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-22T16:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4812#issuecomment-36482",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036483.json:
```json
{
    "body": "I put up a new patch which fixes the issue above.",
    "created_at": "2008-12-22T16:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4812#issuecomment-36483",
    "user": "@mwhansen"
}
```

I put up a new patch which fixes the issue above.



---

archive/issue_comments_036484.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-12-22T16:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4812#issuecomment-36484",
    "user": "@mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_036485.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-22T22:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4812#issuecomment-36485",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.3.alpha0



---

archive/issue_comments_036486.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-22T22:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4812#issuecomment-36486",
    "user": "mabshoff"
}
```

Resolution: fixed
