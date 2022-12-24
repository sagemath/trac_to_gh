# Issue 1924: Optimize matrix multiply cache friendliness

archive/issues_001924.json:
```json
{
    "body": "Assignee: @williamstein\n\nToday in the sage seminar Cl\u00e9ment Pernet demonstrated that in the naive matrix multiply algorithm (used as a basecase for all others)\n\nSpecifically, for computing C = A*B,\n\n\n```\nfor i in A.nrows:\n    for j in B.ncols:\n        for k in B.nrows:\n            C[i,j] += A[i,k] * B[k,j]\n```\n\n\nis bad for the cache as one is iterating over the columns of B in the inner loop. Changing this to \n\n\n```\nfor i in A.nrows:\n    for k in B.nrows:\n        for j in B.ncols:\n            C[i,j] += A[i,k] * B[k,j]\n```\n\n\ngives the same result, but much better cache performance.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1924\n\n",
    "created_at": "2008-01-25T10:45:12Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Optimize matrix multiply cache friendliness",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1924",
    "user": "@robertwb"
}
```
Assignee: @williamstein

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

Issue created by migration from https://trac.sagemath.org/ticket/1924





---

archive/issue_comments_012202.json:
```json
{
    "body": "Attachment [1924-matrix-mul-loop-order.patch](tarball://root/attachments/some-uuid/ticket1924/1924-matrix-mul-loop-order.patch) by @robertwb created at 2008-01-25 10:46:06",
    "created_at": "2008-01-25T10:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1924#issuecomment-12202",
    "user": "@robertwb"
}
```

Attachment [1924-matrix-mul-loop-order.patch](tarball://root/attachments/some-uuid/ticket1924/1924-matrix-mul-loop-order.patch) by @robertwb created at 2008-01-25 10:46:06



---

archive/issue_comments_012203.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-25T10:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1924#issuecomment-12203",
    "user": "@robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012204.json:
```json
{
    "body": "The above patch integrates this loop-order change into the modn case, reducing the time by about a third.",
    "created_at": "2008-01-25T10:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1924#issuecomment-12204",
    "user": "@robertwb"
}
```

The above patch integrates this loop-order change into the modn case, reducing the time by about a third.



---

archive/issue_comments_012205.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2008-01-25T10:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1924#issuecomment-12205",
    "user": "@robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_012206.json:
```json
{
    "body": "There is something fishy about this patch. It touches the same file in the same area (hunk 1) and that causes rejects:\n\n```\nsage$ patch -p1 --dry-run < 1924-matrix-mul-loop-order.patch\npatching file sage/matrix/matrix_window_modn_dense.pyx\npatching file sage/matrix/matrix_window_modn_dense.pyx\nHunk #1 FAILED at 125.\nHunk #2 succeeded at 168 (offset -5 lines).\nHunk #3 succeeded at 213 (offset -5 lines).\n1 out of 3 hunks FAILED -- saving rejects to file sage/matrix/matrix_window_modn_dense.pyx.rej\n```\n\n\nThere is also an extra comma:`cdef mod_int A_row_k,`. So: negative review for now :(, but I am sure Robert will be quick to update. :)\n\nCheers,\n\nMichael",
    "created_at": "2008-01-25T11:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1924#issuecomment-12206",
    "user": "mabshoff"
}
```

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

archive/issue_comments_012207.json:
```json
{
    "body": "I just applied the patch (which works fine for me), then exported it again.  Maybe this will work for Mabshoff.",
    "created_at": "2008-01-25T13:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1924#issuecomment-12207",
    "user": "@williamstein"
}
```

I just applied the patch (which works fine for me), then exported it again.  Maybe this will work for Mabshoff.



---

archive/issue_comments_012208.json:
```json
{
    "body": "Attachment [trac-1924-fixed_I_think.patch](tarball://root/attachments/some-uuid/ticket1924/trac-1924-fixed_I_think.patch) by @williamstein created at 2008-01-25 13:24:29\n\nI just applied the patch without any funny business to 2.10:\n\n```\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/1924/1924-matrix-mul-loop-order.patch?format=raw')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/1924/1924-matrix-mul-loop-order.patch?format=raw\nLoading: [..]\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg status\ncd \"/Users/was/s/devel/sage\" && hg import   \"/Users/was/.sage/temp/teragon.local/47537/tmp_1.patch\"\napplying /Users/was/.sage/temp/teragon.local/47537/tmp_1.patch\n```\n\n\nAfter applying the patch I do *not* have a line like this:\n\n```\n def mod_int A_row_k,\n```\n\nThis is because the first part of the diff adds that line, but the\nsecond part removes it.  \n\nBy the way, on my laptop before and after applying this patch:\n\nBEFORE:\n\n```\nsage: sage: a = random_matrix(GF(101),500); b = random_matrix(GF(101),500)\nsage: sage: time c=a*b\nCPU times: user 0.38 s, sys: 0.02 s, total: 0.40 s\nWall time: 0.42\nsage: sage: a = random_matrix(GF(101),1000); b = random_matrix(GF(101),1000)\nsage: sage: time c=a*b\nCPU times: user 2.63 s, sys: 0.13 s, total: 2.76 s\nWall time: 2.78\n```\n\n\nAFTER:\n\n```\nsage: a = random_matrix(GF(101),500); b = random_matrix(GF(101),500)\nsage: time c=a*b\nCPU times: user 0.23 s, sys: 0.02 s, total: 0.25 s\nWall time: 0.25\nsage: a = random_matrix(GF(101),1000); b = random_matrix(GF(101),1000)\nsage: time c=a*b\nCPU times: user 1.60 s, sys: 0.13 s, total: 1.73 s\nWall time: 1.73\n```\n\n\nNot bad for basically swapping the order of two for loops!",
    "created_at": "2008-01-25T13:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1924#issuecomment-12208",
    "user": "@williamstein"
}
```

Attachment [trac-1924-fixed_I_think.patch](tarball://root/attachments/some-uuid/ticket1924/trac-1924-fixed_I_think.patch) by @williamstein created at 2008-01-25 13:24:29

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

archive/issue_comments_012209.json:
```json
{
    "body": "By the way, on my laptop (core 2 duo 2.6Ghz) magma kicks ass on the above benchmark:\n\n```\nsage: magma.eval('a := Random(MatrixAlgebra(GF(101),500)); b := Random(MatrixAlgebra(GF(101),500));')\n''\nsage: magma.eval('time c := a*b')\n'Time: 0.040'\nsage: magma.eval('a := Random(MatrixAlgebra(GF(101),1000)); b := Random(MatrixAlgebra(GF(101),1000));')\n''\nsage: magma.eval('time c := a*b')\n'Time: 0.200'\n```\n\n\nIt's not their timer lying, because one gets the same timing externally via wall time from Sage:\n\n```\nsage: aa = magma('Random(MatrixAlgebra(GF(101),1000))')\nsage: bb = magma('Random(MatrixAlgebra(GF(101),1000))')\nsage: time cc=aa*bb\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.20\nsage: time cc=aa*bb\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.20\nsage: time cc=aa*bb\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.20\nsage: aa = magma('Random(MatrixAlgebra(GF(101),500))')\nsage: bb = magma('Random(MatrixAlgebra(GF(101),500))')\nsage: time cc=aa*bb\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.04\nsage: time cc=aa*bb\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.03\n```\n\n\nMagma has special optimized matrices for such a small prime (101). \nFor the slightly larger p=10007 we have\n\n```\nsage: magma.eval('a := Random(MatrixAlgebra(GF(10007),1000)); b := Random(MatrixAlgebra(GF(10007),1000));')\n''\nsage: magma.eval('time c := a*b')\n'Time: 0.860'\n```\n\n\nand in Sage (now):\n\n```\nsage: a = random_matrix(GF(10007),1000); b = random_matrix(GF(10007), 1000)\nsage: time c=a*b\nCPU times: user 1.72 s, sys: 0.12 s, total: 1.85 s\nWall time: 1.85\nsage: a = random_matrix(GF(10007),1000); b = random_matrix(GF(10007), 1000)\nsage: time c=a._multiply_linbox(b)\nCPU times: user 0.88 s, sys: 0.12 s, total: 1.01 s\nWall time: 0.90\n```\n",
    "created_at": "2008-01-25T13:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1924#issuecomment-12209",
    "user": "@williamstein"
}
```

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

archive/issue_comments_012210.json:
```json
{
    "body": "Hey, I can give this a positive review, since I just thoroughly tried it out, and I'm not the author! :-)",
    "created_at": "2008-01-25T13:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1924#issuecomment-12210",
    "user": "@williamstein"
}
```

Hey, I can give this a positive review, since I just thoroughly tried it out, and I'm not the author! :-)



---

archive/issue_comments_012211.json:
```json
{
    "body": "Well, William's reexported patch applies cleanly. But since it is about 2kb smaller than the original patch somebody has to give me at least that the original patch was fishy ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-01-25T17:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1924#issuecomment-12211",
    "user": "mabshoff"
}
```

Well, William's reexported patch applies cleanly. But since it is about 2kb smaller than the original patch somebody has to give me at least that the original patch was fishy ;)

Cheers,

Michael



---

archive/issue_comments_012212.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-25T17:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1924#issuecomment-12212",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha2



---

archive/issue_comments_012213.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-25T17:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1924#issuecomment-12213",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012214.json:
```json
{
    "body": "The original patch had two diffs in it...I guess I'll try and avoid doing that from now on. Looks like William was able to respond faster than I was though.",
    "created_at": "2008-01-25T19:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1924#issuecomment-12214",
    "user": "@robertwb"
}
```

The original patch had two diffs in it...I guess I'll try and avoid doing that from now on. Looks like William was able to respond faster than I was though.
