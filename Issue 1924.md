# Issue 1924: Optimize matrix multiply cache friendliness

Issue created by migration from https://trac.sagemath.org/ticket/1924

Original creator: robertwb

Original creation time: 2008-01-25 10:45:12

Assignee: was

Today in the sage seminar Clément Pernet demonstrated that in the naive matrix multiply algorithm (used as a basecase for all others)

Specifically, for computing C = A*B,


```
for i in A.nrows:
    for j in B.ncols:
        for k in B.nrows:
            C[i,j] += A[i,k] * B[k,j]
```


is bad for the cache as one is iterating over the columns of B in the inner loop. Changing this to 


```
for i in A.nrows:
    for k in B.nrows:
        for j in B.ncols:
            C[i,j] += A[i,k] * B[k,j]
```


gives the same result, but much better cache performance.


---

Attachment


---

Comment by robertwb created at 2008-01-25 10:47:26

Changing status from new to assigned.


---

Comment by robertwb created at 2008-01-25 10:47:26

The above patch integrates this loop-order change into the modn case, reducing the time by about a third.


---

Comment by robertwb created at 2008-01-25 10:47:26

Changing assignee from was to robertwb.


---

Comment by mabshoff created at 2008-01-25 11:49:08

There is something fishy about this patch. It touches the same file in the same area (hunk 1) and that causes rejects:

```
sage$ patch -p1 --dry-run < 1924-matrix-mul-loop-order.patch
patching file sage/matrix/matrix_window_modn_dense.pyx
patching file sage/matrix/matrix_window_modn_dense.pyx
Hunk #1 FAILED at 125.
Hunk #2 succeeded at 168 (offset -5 lines).
Hunk #3 succeeded at 213 (offset -5 lines).
1 out of 3 hunks FAILED -- saving rejects to file sage/matrix/matrix_window_modn_dense.pyx.rej
```


There is also an extra comma:`cdef mod_int A_row_k,`. So: negative review for now :(, but I am sure Robert will be quick to update. :)

Cheers,

Michael


---

Comment by was created at 2008-01-25 13:23:55

I just applied the patch (which works fine for me), then exported it again.  Maybe this will work for Mabshoff.


---

Attachment

I just applied the patch without any funny business to 2.10:

```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/1924/1924-matrix-mul-loop-order.patch?format=raw')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/1924/1924-matrix-mul-loop-order.patch?format=raw
Loading: [..]
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg status
cd "/Users/was/s/devel/sage" && hg import   "/Users/was/.sage/temp/teragon.local/47537/tmp_1.patch"
applying /Users/was/.sage/temp/teragon.local/47537/tmp_1.patch
```


After applying the patch I do *not* have a line like this:

```
 def mod_int A_row_k,
```

This is because the first part of the diff adds that line, but the
second part removes it.  

By the way, on my laptop before and after applying this patch:

BEFORE:

```
sage: sage: a = random_matrix(GF(101),500); b = random_matrix(GF(101),500)
sage: sage: time c=a*b
CPU times: user 0.38 s, sys: 0.02 s, total: 0.40 s
Wall time: 0.42
sage: sage: a = random_matrix(GF(101),1000); b = random_matrix(GF(101),1000)
sage: sage: time c=a*b
CPU times: user 2.63 s, sys: 0.13 s, total: 2.76 s
Wall time: 2.78
```


AFTER:

```
sage: a = random_matrix(GF(101),500); b = random_matrix(GF(101),500)
sage: time c=a*b
CPU times: user 0.23 s, sys: 0.02 s, total: 0.25 s
Wall time: 0.25
sage: a = random_matrix(GF(101),1000); b = random_matrix(GF(101),1000)
sage: time c=a*b
CPU times: user 1.60 s, sys: 0.13 s, total: 1.73 s
Wall time: 1.73
```


Not bad for basically swapping the order of two for loops!


---

Comment by was created at 2008-01-25 13:32:21

By the way, on my laptop (core 2 duo 2.6Ghz) magma kicks ass on the above benchmark:

```
sage: magma.eval('a := Random(MatrixAlgebra(GF(101),500)); b := Random(MatrixAlgebra(GF(101),500));')
''
sage: magma.eval('time c := a*b')
'Time: 0.040'
sage: magma.eval('a := Random(MatrixAlgebra(GF(101),1000)); b := Random(MatrixAlgebra(GF(101),1000));')
''
sage: magma.eval('time c := a*b')
'Time: 0.200'
```


It's not their timer lying, because one gets the same timing externally via wall time from Sage:

```
sage: aa = magma('Random(MatrixAlgebra(GF(101),1000))')
sage: bb = magma('Random(MatrixAlgebra(GF(101),1000))')
sage: time cc=aa*bb
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.20
sage: time cc=aa*bb
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.20
sage: time cc=aa*bb
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.20
sage: aa = magma('Random(MatrixAlgebra(GF(101),500))')
sage: bb = magma('Random(MatrixAlgebra(GF(101),500))')
sage: time cc=aa*bb
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.04
sage: time cc=aa*bb
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.03
```


Magma has special optimized matrices for such a small prime (101). 
For the slightly larger p=10007 we have

```
sage: magma.eval('a := Random(MatrixAlgebra(GF(10007),1000)); b := Random(MatrixAlgebra(GF(10007),1000));')
''
sage: magma.eval('time c := a*b')
'Time: 0.860'
```


and in Sage (now):

```
sage: a = random_matrix(GF(10007),1000); b = random_matrix(GF(10007), 1000)
sage: time c=a*b
CPU times: user 1.72 s, sys: 0.12 s, total: 1.85 s
Wall time: 1.85
sage: a = random_matrix(GF(10007),1000); b = random_matrix(GF(10007), 1000)
sage: time c=a._multiply_linbox(b)
CPU times: user 0.88 s, sys: 0.12 s, total: 1.01 s
Wall time: 0.90
```



---

Comment by was created at 2008-01-25 13:33:39

Hey, I can give this a positive review, since I just thoroughly tried it out, and I'm not the author! :-)


---

Comment by mabshoff created at 2008-01-25 17:22:44

Well, William's reexported patch applies cleanly. But since it is about 2kb smaller than the original patch somebody has to give me at least that the original patch was fishy ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-25 17:23:01

Merged in Sage 2.10.1.alpha2


---

Comment by mabshoff created at 2008-01-25 17:23:01

Resolution: fixed


---

Comment by robertwb created at 2008-01-25 19:03:42

The original patch had two diffs in it...I guess I'll try and avoid doing that from now on. Looks like William was able to respond faster than I was though.
