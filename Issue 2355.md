# Issue 2355: Write a clearer submatrix implementation

archive/issues_002355.json:
```json
{
    "body": "Assignee: dfdeshom\n\n The current implementation of the submatrix command could be easier to use given that matrix_from_rows_and_columns is nicely suited for this task; ie, this should just work\n\n```\nA.submatrix([1..2],[0..1])\n```\n\n\nif A is (at least) a 3x2 matrix\n \n\nIssue created by migration from https://trac.sagemath.org/ticket/2355\n\n",
    "created_at": "2008-02-29T20:30:57Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "Write a clearer submatrix implementation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2355",
    "user": "dfdeshom"
}
```
Assignee: dfdeshom

 The current implementation of the submatrix command could be easier to use given that matrix_from_rows_and_columns is nicely suited for this task; ie, this should just work

```
A.submatrix([1..2],[0..1])
```


if A is (at least) a 3x2 matrix
 

Issue created by migration from https://trac.sagemath.org/ticket/2355





---

archive/issue_comments_015835.json:
```json
{
    "body": "I vote for at least seriously considering using the same notation as numpy for submatrices, whatever that is, by extending __getitem__...",
    "created_at": "2008-02-29T20:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15835",
    "user": "was"
}
```

I vote for at least seriously considering using the same notation as numpy for submatrices, whatever that is, by extending __getitem__...



---

archive/issue_comments_015836.json:
```json
{
    "body": "Replying to [comment:1 was]:\n> I vote for at least seriously considering using the same notation as numpy for submatrices, whatever that is, by extending __getitem__...\n\nAgreed. Looking at the relevant section of the code, it looks like it should not be too hard",
    "created_at": "2008-03-01T08:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15836",
    "user": "dfdeshom"
}
```

Replying to [comment:1 was]:
> I vote for at least seriously considering using the same notation as numpy for submatrices, whatever that is, by extending __getitem__...

Agreed. Looking at the relevant section of the code, it looks like it should not be too hard



---

archive/issue_comments_015837.json:
```json
{
    "body": "Here's a patch that makes the following possible:\n\n```\n            sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)\n            sage: M\n            [ 1 -2 -1 -1  9]\n            [ 1  8  6  2  2]\n            [ 1  1 -1  1  4]\n            [-1  2 -2 -1  4]\n\n            Get The 2 x 2 submatrix of M, starting at row index and column\n            index 1\n            sage: M[1:3,1:3]\n            [ 8  6]\n            [ 1 -1]\n\n            Get the 2 x 3 submatrix of M starting at row index and column\n            index 1:\n            sage: M[1:3,[1..3]]\n            [ 8  6  2]\n            [ 1 -1  1]\n\n            Get the second column of M:\n            sage: M[1:,0]\n            [ 1]\n            [ 1]\n            [-1]\n\n            sage: M[range(2),:]\n            [ 1 -2 -1 -1  9]\n            [ 1  8  6  2  2]\n            sage: M[range(2),4]\n            [9]\n            [2]\n            sage: M[range(3),range(5)]\n            [ 1 -2 -1 -1  9]\n            [ 1  8  6  2  2]\n            [ 1  1 -1  1  4]\n\n            sage: M[3,range(5)]\n            [-1  2 -2 -1  4]\n            sage: M[3,:]\n            [-1  2 -2 -1  4]\n            sage: M[3,4]\n            4\n\n```\n",
    "created_at": "2008-03-02T17:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15837",
    "user": "dfdeshom"
}
```

Here's a patch that makes the following possible:

```
            sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
            sage: M
            [ 1 -2 -1 -1  9]
            [ 1  8  6  2  2]
            [ 1  1 -1  1  4]
            [-1  2 -2 -1  4]

            Get The 2 x 2 submatrix of M, starting at row index and column
            index 1
            sage: M[1:3,1:3]
            [ 8  6]
            [ 1 -1]

            Get the 2 x 3 submatrix of M starting at row index and column
            index 1:
            sage: M[1:3,[1..3]]
            [ 8  6  2]
            [ 1 -1  1]

            Get the second column of M:
            sage: M[1:,0]
            [ 1]
            [ 1]
            [-1]

            sage: M[range(2),:]
            [ 1 -2 -1 -1  9]
            [ 1  8  6  2  2]
            sage: M[range(2),4]
            [9]
            [2]
            sage: M[range(3),range(5)]
            [ 1 -2 -1 -1  9]
            [ 1  8  6  2  2]
            [ 1  1 -1  1  4]

            sage: M[3,range(5)]
            [-1  2 -2 -1  4]
            sage: M[3,:]
            [-1  2 -2 -1  4]
            sage: M[3,4]
            4

```




---

archive/issue_comments_015838.json:
```json
{
    "body": "I have to register the obvious concern.  You've replaced what I wrote:\n\n```\n554\t \t            if PyTuple_Size(key) != 2: \n555\t \t                raise IndexError, \"index must be an integer or pair of integers\" \n556\t \t            i = <object> PyTuple_GET_ITEM(key, 0) \n557\t \t            j = <object> PyTuple_GET_ITEM(key, 1) \n```\n\n\n\nby \n\n\n```\n \t587\t            s1 = key[0] \n \t588\t            s2 = key[1] \n \t589\t \n \t590\t            if isinstance(s1,sage.rings.integer.Integer) and \\ \n \t591\t                   isinstance(s2,sage.rings.integer.Integer): \n \t592\t                self.check_bounds(s1, s2) \n \t593\t                return self.get_unsafe(s1, s2) \n```\n\n\nIf A is a matrix doing A[i,j] is a sort of \"critical speed operation\",\nso I'm concerned about speed.    Thoughts? Benchmarks?",
    "created_at": "2008-03-02T17:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15838",
    "user": "was"
}
```

I have to register the obvious concern.  You've replaced what I wrote:

```
554	 	            if PyTuple_Size(key) != 2: 
555	 	                raise IndexError, "index must be an integer or pair of integers" 
556	 	            i = <object> PyTuple_GET_ITEM(key, 0) 
557	 	            j = <object> PyTuple_GET_ITEM(key, 1) 
```



by 


```
 	587	            s1 = key[0] 
 	588	            s2 = key[1] 
 	589	 
 	590	            if isinstance(s1,sage.rings.integer.Integer) and \ 
 	591	                   isinstance(s2,sage.rings.integer.Integer): 
 	592	                self.check_bounds(s1, s2) 
 	593	                return self.get_unsafe(s1, s2) 
```


If A is a matrix doing A[i,j] is a sort of "critical speed operation",
so I'm concerned about speed.    Thoughts? Benchmarks?



---

archive/issue_comments_015839.json:
```json
{
    "body": "Replying to [comment:4 was]:\n\nThe new method is slower, but not by much (surprisingly for me):\n\n```\n# sage-main\nsage: %timeit M[3,4]\n10000 loops, best of 3: 69.5 \u00b5s per loop\n\n#sage-getitem\nsage: %timeit M[3,4]\n10000 loops, best of 3: 71.2 \u00b5s per loop\n\n#sage-main\nsage: %timeit M[3:]\n10000 loops, best of 3: 68.3 \u00b5s per loop\n\n#sage-getitem\nsage: %timeit M[3:]\n10000 loops, best of 3: 69.5 \u00b5s per loop\n```\n\n\n\n```\n#sage-getitem only\nsage: %timeit M[:4,range(4)]\n10000 loops, best of 3: 87.8 \u00b5s per loop\n\nsage: %timeit M[3:,:4]\n10000 loops, best of 3: 78.8 \u00b5s per loop\n\nsage: %timeit M[3:,0]\n10000 loops, best of 3: 74.1 \u00b5s per loop\n\n```\n\n\nmatrix_from_rows_and_columns could also be made a little faster. I plan to post another ticket/patch for it.",
    "created_at": "2008-03-02T18:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15839",
    "user": "dfdeshom"
}
```

Replying to [comment:4 was]:

The new method is slower, but not by much (surprisingly for me):

```
# sage-main
sage: %timeit M[3,4]
10000 loops, best of 3: 69.5 µs per loop

#sage-getitem
sage: %timeit M[3,4]
10000 loops, best of 3: 71.2 µs per loop

#sage-main
sage: %timeit M[3:]
10000 loops, best of 3: 68.3 µs per loop

#sage-getitem
sage: %timeit M[3:]
10000 loops, best of 3: 69.5 µs per loop
```



```
#sage-getitem only
sage: %timeit M[:4,range(4)]
10000 loops, best of 3: 87.8 µs per loop

sage: %timeit M[3:,:4]
10000 loops, best of 3: 78.8 µs per loop

sage: %timeit M[3:,0]
10000 loops, best of 3: 74.1 µs per loop

```


matrix_from_rows_and_columns could also be made a little faster. I plan to post another ticket/patch for it.



---

archive/issue_comments_015840.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-02T18:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15840",
    "user": "dfdeshom"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015841.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-03-11T16:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15841",
    "user": "dfdeshom"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_015842.json:
```json
{
    "body": "Can't give this patch a positive review. After I applied it to a brand new sage-2.10.3\na lot of code seems to be broken.\n\nI do not quite understand what is going on.\n\nJaap",
    "created_at": "2008-03-13T18:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15842",
    "user": "jsp"
}
```

Can't give this patch a positive review. After I applied it to a brand new sage-2.10.3
a lot of code seems to be broken.

I do not quite understand what is going on.

Jaap



---

archive/issue_comments_015843.json:
```json
{
    "body": "My changes seem to have broken `matrix.__reduce___`. I'll look into it.",
    "created_at": "2008-03-13T19:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15843",
    "user": "dfdeshom"
}
```

My changes seem to have broken `matrix.__reduce___`. I'll look into it.



---

archive/issue_comments_015844.json:
```json
{
    "body": "Found the bug. All doctests for matrix0,1,2 pass now.",
    "created_at": "2008-03-13T20:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15844",
    "user": "dfdeshom"
}
```

Found the bug. All doctests for matrix0,1,2 pass now.



---

archive/issue_comments_015845.json:
```json
{
    "body": "Applyin this bundle I still got an error:\n\n\n```\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  devel/sage-main/sage/matrix/matrix_integer_dense.pyx\nTotal time for all tests: 113.4 seconds\n\n```\n\n\n\n\n```\nsage -t  devel/sage-main/sage/matrix/matrix_integer_dense.pyx**********************************************************************\nFile \"matrix_integer_dense.pyx\", line 2961:\n    sage: a._add_row_and_maintain_echelon_form(vector(ZZ,[1,2,3]),[0,1,2])\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jaap/work/sage-2.10.3/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_52[1]>\", line 1, in <module>\n        a._add_row_and_maintain_echelon_form(vector(ZZ,[Integer(1),Integer(2),Integer(3)]),[Integer(0),Integer(1),Integer(2)])###line 2961:\n    sage: a._add_row_and_maintain_echelon_form(vector(ZZ,[1,2,3]),[0,1,2])\n      File \"matrix_integer_dense.pyx\", line 3013, in sage.matrix.matrix_integer_dense.Matrix_integer_dense._add_row_and_maintain_echelon_form\n        if b % a == 0:\n      File \"matrix0.pyx\", line 1927, in sage.matrix.matrix0.Matrix.__mod__\n        v[i] = v[i] % p\n      File \"integer.pyx\", line 1335, in sage.rings.integer.Integer.__mod__\n      File \"integer.pyx\", line 3747, in sage.rings.integer.integer\n      File \"integer.pyx\", line 356, in sage.rings.integer.Integer.__init__\n    TypeError: unable to coerce element to an integer\n**********************************************************************\nFile \"matrix_integer_dense.pyx\", line 2970:\n    sage: a._add_row_and_maintain_echelon_form(vector(ZZ,[1,2,3]),[0,1])\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jaap/work/sage-2.10.3/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_52[4]>\", line 1, in <module>\n        a._add_row_and_maintain_echelon_form(vector(ZZ,[Integer(1),Integer(2),Integer(3)]),[Integer(0),Integer(1)])###line 2970:\n    sage: a._add_row_and_maintain_echelon_form(vector(ZZ,[1,2,3]),[0,1])\n      File \"matrix_integer_dense.pyx\", line 3013, in sage.matrix.matrix_integer_dense.Matrix_integer_dense._add_row_and_maintain_echelon_form\n        if b % a == 0:\n      File \"matrix0.pyx\", line 1927, in sage.matrix.matrix0.Matrix.__mod__\n        v[i] = v[i] % p\n      File \"integer.pyx\", line 1335, in sage.rings.integer.Integer.__mod__\n      File \"integer.pyx\", line 3747, in sage.rings.integer.integer\n      File \"integer.pyx\", line 356, in sage.rings.integer.Integer.__init__\n    TypeError: unable to coerce element to an integer\n**********************************************************************\n1 items had failures:\n   2 of   5 in __main__.example_52\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file .doctest_matrix_integer_dense.pyx\n         [3.2 s]\n\n```\n",
    "created_at": "2008-03-13T21:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15845",
    "user": "jsp"
}
```

Applyin this bundle I still got an error:


```
----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-main/sage/matrix/matrix_integer_dense.pyx
Total time for all tests: 113.4 seconds

```




```
sage -t  devel/sage-main/sage/matrix/matrix_integer_dense.pyx**********************************************************************
File "matrix_integer_dense.pyx", line 2961:
    sage: a._add_row_and_maintain_echelon_form(vector(ZZ,[1,2,3]),[0,1,2])
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/work/sage-2.10.3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[1]>", line 1, in <module>
        a._add_row_and_maintain_echelon_form(vector(ZZ,[Integer(1),Integer(2),Integer(3)]),[Integer(0),Integer(1),Integer(2)])###line 2961:
    sage: a._add_row_and_maintain_echelon_form(vector(ZZ,[1,2,3]),[0,1,2])
      File "matrix_integer_dense.pyx", line 3013, in sage.matrix.matrix_integer_dense.Matrix_integer_dense._add_row_and_maintain_echelon_form
        if b % a == 0:
      File "matrix0.pyx", line 1927, in sage.matrix.matrix0.Matrix.__mod__
        v[i] = v[i] % p
      File "integer.pyx", line 1335, in sage.rings.integer.Integer.__mod__
      File "integer.pyx", line 3747, in sage.rings.integer.integer
      File "integer.pyx", line 356, in sage.rings.integer.Integer.__init__
    TypeError: unable to coerce element to an integer
**********************************************************************
File "matrix_integer_dense.pyx", line 2970:
    sage: a._add_row_and_maintain_echelon_form(vector(ZZ,[1,2,3]),[0,1])
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/work/sage-2.10.3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[4]>", line 1, in <module>
        a._add_row_and_maintain_echelon_form(vector(ZZ,[Integer(1),Integer(2),Integer(3)]),[Integer(0),Integer(1)])###line 2970:
    sage: a._add_row_and_maintain_echelon_form(vector(ZZ,[1,2,3]),[0,1])
      File "matrix_integer_dense.pyx", line 3013, in sage.matrix.matrix_integer_dense.Matrix_integer_dense._add_row_and_maintain_echelon_form
        if b % a == 0:
      File "matrix0.pyx", line 1927, in sage.matrix.matrix0.Matrix.__mod__
        v[i] = v[i] % p
      File "integer.pyx", line 1335, in sage.rings.integer.Integer.__mod__
      File "integer.pyx", line 3747, in sage.rings.integer.integer
      File "integer.pyx", line 356, in sage.rings.integer.Integer.__init__
    TypeError: unable to coerce element to an integer
**********************************************************************
1 items had failures:
   2 of   5 in __main__.example_52
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_matrix_integer_dense.pyx
         [3.2 s]

```




---

archive/issue_comments_015846.json:
```json
{
    "body": "Thanks I've updated the bundle to take care of these doctest failures. Give it one more try if you can.",
    "created_at": "2008-03-13T21:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15846",
    "user": "dfdeshom"
}
```

Thanks I've updated the bundle to take care of these doctest failures. Give it one more try if you can.



---

archive/issue_comments_015847.json:
```json
{
    "body": "What should I apply to review this?  The patch, the bundle, or both?",
    "created_at": "2008-03-13T22:12:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15847",
    "user": "jason"
}
```

What should I apply to review this?  The patch, the bundle, or both?



---

archive/issue_comments_015848.json:
```json
{
    "body": "Just the bundle",
    "created_at": "2008-03-13T22:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15848",
    "user": "dfdeshom"
}
```

Just the bundle



---

archive/issue_comments_015849.json:
```json
{
    "body": "Here we are again:\n\n\n```\nsage -t  devel/sage-main/sage/matrix/matrix0.pyx            **********************************************************************\nFile \"matrix0.pyx\", line 553:\n    sage: M[1:,0]\nExpected:\n    [ 1]\n    [ 1]\n    [-1]\nGot:\n    1\n**********************************************************************\nFile \"matrix0.pyx\", line 566:\n    sage: M[range(2),4]\nExpected:\n    [9]\n    [2]\nGot:\n    9\n**********************************************************************\n1 items had failures:\n   2 of  23 in __main__.example_21\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file .doctest_matrix0.pyx\n         [2.3 s]\nsage -t  devel/sage-main/sage/matrix/matrix1.pyx            \n         [3.9 s]\nsage -t  devel/sage-main/sage/matrix/action.pyx             \n         [1.8 s]\nsage -t  devel/sage-main/sage/matrix/matrix_generic_sparse.pyx\n         [1.6 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  devel/sage-main/sage/matrix/matrix0.pyx\nTotal time for all tests: 121.8 seconds\n\n```\n",
    "created_at": "2008-03-14T12:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15849",
    "user": "jsp"
}
```

Here we are again:


```
sage -t  devel/sage-main/sage/matrix/matrix0.pyx            **********************************************************************
File "matrix0.pyx", line 553:
    sage: M[1:,0]
Expected:
    [ 1]
    [ 1]
    [-1]
Got:
    1
**********************************************************************
File "matrix0.pyx", line 566:
    sage: M[range(2),4]
Expected:
    [9]
    [2]
Got:
    9
**********************************************************************
1 items had failures:
   2 of  23 in __main__.example_21
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_matrix0.pyx
         [2.3 s]
sage -t  devel/sage-main/sage/matrix/matrix1.pyx            
         [3.9 s]
sage -t  devel/sage-main/sage/matrix/action.pyx             
         [1.8 s]
sage -t  devel/sage-main/sage/matrix/matrix_generic_sparse.pyx
         [1.6 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-main/sage/matrix/matrix0.pyx
Total time for all tests: 121.8 seconds

```




---

archive/issue_comments_015850.json:
```json
{
    "body": "Attachment [2355.hg](tarball://root/attachments/some-uuid/ticket2355/2355.hg) by dfdeshom created at 2008-03-14 13:20:11",
    "created_at": "2008-03-14T13:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15850",
    "user": "dfdeshom"
}
```

Attachment [2355.hg](tarball://root/attachments/some-uuid/ticket2355/2355.hg) by dfdeshom created at 2008-03-14 13:20:11



---

archive/issue_comments_015851.json:
```json
{
    "body": "A little embarrassing, isn't it? The bundle 2355.hg has been updated and should pass all doctests in sage/matrix",
    "created_at": "2008-03-14T13:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15851",
    "user": "dfdeshom"
}
```

A little embarrassing, isn't it? The bundle 2355.hg has been updated and should pass all doctests in sage/matrix



---

archive/issue_comments_015852.json:
```json
{
    "body": "Replying to [comment:18 dfdeshom]:\n> A little embarrassing, isn't it? The bundle 2355.hg has been updated and should pass all doctests in sage/matrix \n\nThis patch once again broke a lot of code!\n\nI tried it on a brand new sage-2.10.4.rc0\n\nJust a snapshot:\n\n```\n      File \"/home/jaap/work/sage-2.10.3/local/lib/python2.5/site-packages/sage/algebras/free_algebra.py\", line 229, in _repr_\n        self.__ngens, self.gens(), self.base_ring())\n      File \"sage_object.pyx\", line 92, in sage.structure.sage_object.SageObject.__repr__\n      File \"/home/jaap/work/sage-2.10.3/local/lib/python2.5/site-packages/sage/algebras/free_algebra_element.py\", line 74, in _repr_\n        x = repr_lincomb(mons, cffs).replace(\"*1 \",\" \")\n      File \"/home/jaap/work/sage-2.10.3/local/lib/python2.5/site-packages/sage/misc/misc.py\", line 508, in repr_lincomb\n        b = str(symbols[i])\n      File \"sage_object.pyx\", line 92, in sage.structure.sage_object.SageObject.__repr__\n      File \"/home/jaap/work/sage-2.10.3/local/lib/python2.5/site-packages/sage/monoids/free_monoid_element.py\", line 103, in _repr_\n        x = self.parent().variable_names()\n      File \"parent_gens.pyx\", line 375, in sage.structure.parent_gens.ParentWithGens.variable_names\n    RuntimeError: maximum recursion depth exceeded in cmp\n**********************************************************************\n\n```\n\n\nTesting seems to hang on\n\n\n```\nsage -t  devel/sage-main/sage/matrix/matrix_symbolic_dense.pyx\n[1]+  Stopped                 ./sage -t devel/sage-main/sage/matrix/\n[jaap@paix sage-2.10.4.rc0]$ \n\n```\n",
    "created_at": "2008-03-16T17:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15852",
    "user": "jsp"
}
```

Replying to [comment:18 dfdeshom]:
> A little embarrassing, isn't it? The bundle 2355.hg has been updated and should pass all doctests in sage/matrix 

This patch once again broke a lot of code!

I tried it on a brand new sage-2.10.4.rc0

Just a snapshot:

```
      File "/home/jaap/work/sage-2.10.3/local/lib/python2.5/site-packages/sage/algebras/free_algebra.py", line 229, in _repr_
        self.__ngens, self.gens(), self.base_ring())
      File "sage_object.pyx", line 92, in sage.structure.sage_object.SageObject.__repr__
      File "/home/jaap/work/sage-2.10.3/local/lib/python2.5/site-packages/sage/algebras/free_algebra_element.py", line 74, in _repr_
        x = repr_lincomb(mons, cffs).replace("*1 "," ")
      File "/home/jaap/work/sage-2.10.3/local/lib/python2.5/site-packages/sage/misc/misc.py", line 508, in repr_lincomb
        b = str(symbols[i])
      File "sage_object.pyx", line 92, in sage.structure.sage_object.SageObject.__repr__
      File "/home/jaap/work/sage-2.10.3/local/lib/python2.5/site-packages/sage/monoids/free_monoid_element.py", line 103, in _repr_
        x = self.parent().variable_names()
      File "parent_gens.pyx", line 375, in sage.structure.parent_gens.ParentWithGens.variable_names
    RuntimeError: maximum recursion depth exceeded in cmp
**********************************************************************

```


Testing seems to hang on


```
sage -t  devel/sage-main/sage/matrix/matrix_symbolic_dense.pyx
[1]+  Stopped                 ./sage -t devel/sage-main/sage/matrix/
[jaap@paix sage-2.10.4.rc0]$ 

```




---

archive/issue_comments_015853.json:
```json
{
    "body": "Replying to [comment:18 dfdeshom]:\n> The bundle 2355.hg has been updated and should pass all doctests in sage/matrix \n\nDidier,\n\nplease post only Mercurial patches. `hg export tip > foo.patch` works perfectly well. Bundles for single commits are a serious annoyance.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T17:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15853",
    "user": "mabshoff"
}
```

Replying to [comment:18 dfdeshom]:
> The bundle 2355.hg has been updated and should pass all doctests in sage/matrix 

Didier,

please post only Mercurial patches. `hg export tip > foo.patch` works perfectly well. Bundles for single commits are a serious annoyance.

Cheers,

Michael



---

archive/issue_comments_015854.json:
```json
{
    "body": "Replying to [comment:19 jsp]:\n> I tried it on a brand new sage-2.10.4.rc0\n\nAll tests pass on 2.10.3 here. 2.10.4rc0 obviously broke something so I'll wait until 2.10.4 is officially released to see what broke what.",
    "created_at": "2008-03-17T03:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15854",
    "user": "dfdeshom"
}
```

Replying to [comment:19 jsp]:
> I tried it on a brand new sage-2.10.4.rc0

All tests pass on 2.10.3 here. 2.10.4rc0 obviously broke something so I'll wait until 2.10.4 is officially released to see what broke what.



---

archive/issue_comments_015855.json:
```json
{
    "body": "Jaap, 2.4.10 with this patch passes all tests I care about (I ran sage -testall and only the matplotlib tests fail). This is on sage.math. I've reposted the patch file, it is named 2355.patch. Please try it out and if you still have failures, let me know which files/tests break what, your platform, etc.",
    "created_at": "2008-03-18T05:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15855",
    "user": "dfdeshom"
}
```

Jaap, 2.4.10 with this patch passes all tests I care about (I ran sage -testall and only the matplotlib tests fail). This is on sage.math. I've reposted the patch file, it is named 2355.patch. Please try it out and if you still have failures, let me know which files/tests break what, your platform, etc.



---

archive/issue_comments_015856.json:
```json
{
    "body": "The patch works for me now!\n\nCheers,\n\nJaap",
    "created_at": "2008-03-20T15:27:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15856",
    "user": "jsp"
}
```

The patch works for me now!

Cheers,

Jaap



---

archive/issue_comments_015857.json:
```json
{
    "body": "Hi, \n\nwhile the patch passes doctests for me with 2.10.4 [modulo some known problems] I am still reluctant to apply this until the performance concern that was raised has been addressed.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-20T23:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15857",
    "user": "mabshoff"
}
```

Hi, 

while the patch passes doctests for me with 2.10.4 [modulo some known problems] I am still reluctant to apply this until the performance concern that was raised has been addressed.

Cheers,

Michael



---

archive/issue_comments_015858.json:
```json
{
    "body": "Attachment [2355.patch](tarball://root/attachments/some-uuid/ticket2355/2355.patch) by dfdeshom created at 2008-03-22 01:21:30\n\nReplying to [comment:24 mabshoff]:\n> Hi, \n> \n> while the patch passes doctests for me with 2.10.4 [modulo some known problems] I am still reluctant to apply this until the performance concern that was raised has been addressed.\n> \n> Cheers,\n> \n> Michael\n\nI've lost some speed while working on this. I've optimized the code a bit. Overall, my version is still slower because I'm doing more type-checking and handling more functionality (I think that's the reason):\n\n\n```\n# M is the same as above\n\n# element-by-element: slower by about 0.1 micro-seconds ~ 1.2x slower\n\n#2355\nsage: %timeit M[2,3]\n1000000 loops, best of 3: 395 ns per loop\n\n#main\nsage: %timeit M[2,3]\n1000000 loops, best of 3: 304 ns per loop\n\n# single slices: slower by < 1 micro-seconds ~ 1.01x slower\n\n#2355\nsage: %timeit M[:4]\n10000 loops, best of 3: 48 \u00c2\u00b5s per loop\n\n#main\nsage: %timeit M[:4]\n10000 loops, best of 3: 48.5 \u00c2\u00b5s per loop\n\n# Getting a whole row: faster by < 1 micro-seconds \n#2355 \nsage: %timeit M[3]\n10000 loops, best of 3: 72.2 \u00b5s per loop\n\n#main\nsage: %timeit M[3]\n10000 loops, best of 3: 72.9 \u00b5s per loop\n```\n \n\nI'm not posting speed comparisons using the other cases (ie, `M[:3,2:]`) since sage doesn't handle them right now.\n\nIf people think this speed loss is unacceptable, I could try to fold the extra functionality into the `submatrix` method instead which would leave `__getitem__` idem. \n\n\n2355.patch is updated. Warning: I've added a new file: `ext/python_slice.pxi` to have fast access to slice objects so the patch is a bit heavy and rebuilds everything ( nearly everything depends on python.pxi). Passes all tests in `matrix/`.",
    "created_at": "2008-03-22T01:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15858",
    "user": "dfdeshom"
}
```

Attachment [2355.patch](tarball://root/attachments/some-uuid/ticket2355/2355.patch) by dfdeshom created at 2008-03-22 01:21:30

Replying to [comment:24 mabshoff]:
> Hi, 
> 
> while the patch passes doctests for me with 2.10.4 [modulo some known problems] I am still reluctant to apply this until the performance concern that was raised has been addressed.
> 
> Cheers,
> 
> Michael

I've lost some speed while working on this. I've optimized the code a bit. Overall, my version is still slower because I'm doing more type-checking and handling more functionality (I think that's the reason):


```
# M is the same as above

# element-by-element: slower by about 0.1 micro-seconds ~ 1.2x slower

#2355
sage: %timeit M[2,3]
1000000 loops, best of 3: 395 ns per loop

#main
sage: %timeit M[2,3]
1000000 loops, best of 3: 304 ns per loop

# single slices: slower by < 1 micro-seconds ~ 1.01x slower

#2355
sage: %timeit M[:4]
10000 loops, best of 3: 48 Âµs per loop

#main
sage: %timeit M[:4]
10000 loops, best of 3: 48.5 Âµs per loop

# Getting a whole row: faster by < 1 micro-seconds 
#2355 
sage: %timeit M[3]
10000 loops, best of 3: 72.2 µs per loop

#main
sage: %timeit M[3]
10000 loops, best of 3: 72.9 µs per loop
```
 

I'm not posting speed comparisons using the other cases (ie, `M[:3,2:]`) since sage doesn't handle them right now.

If people think this speed loss is unacceptable, I could try to fold the extra functionality into the `submatrix` method instead which would leave `__getitem__` idem. 


2355.patch is updated. Warning: I've added a new file: `ext/python_slice.pxi` to have fast access to slice objects so the patch is a bit heavy and rebuilds everything ( nearly everything depends on python.pxi). Passes all tests in `matrix/`.



---

archive/issue_comments_015859.json:
```json
{
    "body": "\n```\n# M is the same as above\n\n# element-by-element: \n\n#2355\nsage: %timeit M[2,3]\n1000000 loops, best of 3: 111 ns per loop\n\n#main\nsage: %timeit M[2,3]\n1000000 loops, best of 3: 111 ns per loop\n\n# single slices: \n\n#2355\nsage: %timeit M[:4]\n10000 loops, best of 3: 28.4 \u00c2\u00b5s per loop\n\n#main\nsage: %timeit M[:4]\n10000 loops, best of 3: 29.6 \u00c2\u00b5s per loop\n\n# Getting a whole row: \n#2355 \nsage: %timeit M[3]\n10000 loops, best of 3: 42.3 \u00c2\u00b5s per loop\n\n#main\nsage: %timeit M[3]\n10000 loops, best of 3: 43.7 \u00c2\u00b5s per loop\n```\n\nI note these were the best times.  In my tests for (1) the new source averaged faster then main.",
    "created_at": "2008-03-25T23:34:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15859",
    "user": "gfurnish"
}
```


```
# M is the same as above

# element-by-element: 

#2355
sage: %timeit M[2,3]
1000000 loops, best of 3: 111 ns per loop

#main
sage: %timeit M[2,3]
1000000 loops, best of 3: 111 ns per loop

# single slices: 

#2355
sage: %timeit M[:4]
10000 loops, best of 3: 28.4 Âµs per loop

#main
sage: %timeit M[:4]
10000 loops, best of 3: 29.6 Âµs per loop

# Getting a whole row: 
#2355 
sage: %timeit M[3]
10000 loops, best of 3: 42.3 Âµs per loop

#main
sage: %timeit M[3]
10000 loops, best of 3: 43.7 Âµs per loop
```

I note these were the best times.  In my tests for (1) the new source averaged faster then main.



---

archive/issue_comments_015860.json:
```json
{
    "body": "Attachment [trac_2355_fast.patch](tarball://root/attachments/some-uuid/ticket2355/trac_2355_fast.patch) by gfurnish created at 2008-03-25 23:35:13\n\nApply on top of 2355.patch",
    "created_at": "2008-03-25T23:35:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15860",
    "user": "gfurnish"
}
```

Attachment [trac_2355_fast.patch](tarball://root/attachments/some-uuid/ticket2355/trac_2355_fast.patch) by gfurnish created at 2008-03-25 23:35:13

Apply on top of 2355.patch



---

archive/issue_comments_015861.json:
```json
{
    "body": "I ran this on sage math, and while 1 was on average faster (although best time was slower), both 2 and 3 were slower.  I'm chalking this up to differences between the Core 2 and Opteron architecture.  __getitem__ is not a cdef function, so I don't see why we should be worrying over a 1\u00c2\u00b5s slowdown on some older systems.  Also, 1 is the common case, so I don't see a good reason to worry about the slower cases of 2 and 3.  Note this test was done with \"-O2\" and the new build system.",
    "created_at": "2008-03-26T09:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15861",
    "user": "gfurnish"
}
```

I ran this on sage math, and while 1 was on average faster (although best time was slower), both 2 and 3 were slower.  I'm chalking this up to differences between the Core 2 and Opteron architecture.  __getitem__ is not a cdef function, so I don't see why we should be worrying over a 1Âµs slowdown on some older systems.  Also, 1 is the common case, so I don't see a good reason to worry about the slower cases of 2 and 3.  Note this test was done with "-O2" and the new build system.



---

archive/issue_comments_015862.json:
```json
{
    "body": "Looks good to me. My concerns regarding performance have been addressed. It merges cleanly against my 2.11.alpha2 tree. If this doctests ok I will merge.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T15:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15862",
    "user": "mabshoff"
}
```

Looks good to me. My concerns regarding performance have been addressed. It merges cleanly against my 2.11.alpha2 tree. If this doctests ok I will merge.

Cheers,

Michael



---

archive/issue_comments_015863.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-28T16:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15863",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_comments_015864.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-28T16:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2355#issuecomment-15864",
    "user": "mabshoff"
}
```

Resolution: fixed
