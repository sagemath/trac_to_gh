# Issue 2190: implement a ZZ-module saturation algorithm: this is the key thing needed to compute kernels over ZZ, etc.

archive/issues_002190.json:
```json
{
    "body": "Assignee: @williamstein\n\nSaturation of a matrix, i.e., this command in Magma:\n\n```\n    (<Mtrx> X) -> Mtrx\n    \n    The basis of the saturation w.r.t. Q of the space spanned by the rows of X.\n```\nis really important to a huge amount of my modular forms research.\nIn Magma this command exists and is quite fast, because I specifically\nneeded it for my work and Allan spent a lot of time on making it quite\ngood.  In Sage, it's built on top of PARI's `matkerint` command (one\ncan -reduce computing saturation to computing the\nkernel over ZZ of the transpose matrix).   As a result, Sage is almost\ncompletely and totally useless at doing any saturations when the size\nis at all interesting for research.  For example, a very tiny example\nbelow is nearly a hundred times slower in Sage than in Magma!\n\n```\nsage: a = random_matrix(ZZ, 40, 42)\nsage: w = a.row_space()\nsage: time s =w.saturation()\nCPU times: user 0.79 s, sys: 0.07 s, total: 0.86 s\nWall time: 0.89\nsage: b = magma(a)\nsage: magma.eval('time c := Saturation(%s);'%b.name())\n'Time: 0.010'\nsage: 0.89 / 0.01\n89.0000000000000\n```\n\nHere are some more examples:\n\n```\nsage: a = random_matrix(ZZ, 150,150)\nsage: w = a.row_space()\nsage: time s = w.saturation()\nCPU times: user 1.36 s, sys: 0.21 s, total: 1.57 s\nWall time: 1.64\nsage: m = magma(a)\nsage: magma.eval('time c := Saturation(%s);'%m.name())\n'Time: 0.290'\n```\n\nand a very typical one for my research would look like this:\n\n```\nsage: a = random_matrix(ZZ, 100,300)\nsage: w = a.row_space()\nsage: time s = w.saturation()\n[[[waited many many minutes --- no answer]]]\nsage: a = random_matrix(ZZ, 100,300)\nsage: m = magma(a)\nsage: magma.eval('time c := Saturation(%s);'%m.name())\n'Time: 0.810'\n```\n\nI just want to pause to emphasize that:\n1. there is no open source code in the world as far as I know that\ncan do saturations quickly; only Magma does them right now, and\n2. doing these reasonably quickly is utterly essential to my modular computational forms research.  \n3. The current situation is that what should be an easy everyday calculation for me -- e.g., saturating a 100x300 -- takes probably *hours* in Sage, but less than one second in Magma!\n\n\nFortunately, there is a fast algorithm for saturation that depends mainly on kernels over GF(p) and HNF, and we now have very fast HNF because of #174. \n\nHere's some code in Magma that does p-satuation.  This combined with other tricks should lead to a saturation algorithm.  Porting this to Sage is definitely step 1.\n\n```\nfunction pAdicSaturation(B,p) \n    if Type(B[1]) eq SeqEnum then\n        V := RSpace(Rationals(),#B[1]);\n\tB := [ V | v : v in B];\n    end if;\n    V := Universe(B);\n    n := Degree(V);\n    for i in [1..#B] do\n\tB[i] *:= LCM([ Denominator(c) : c in Eltseq(B[i]) ]);\n    end for;\n    ZZ := Integers();\n    FF := FiniteField(p);\n    B := RMatrixSpace(ZZ,#B,n)!Matrix(B);\n    m := Rank(B);\n    B := Submatrix(HermiteForm(B),1,1,m,n);\n    N := RMatrixSpace(FF,m,n)!B;\n    while Rank(N) lt m do \n\tK := Kernel(N);\n\tvprintf pAdicSaturation : \n\t    \"Rank(N) + Rank(K) = %o + %o = %o\\n\", Rank(N), Rank(K), m;\n\tC := RMatrixSpace(ZZ,#Basis(K),n)!\n\tMatrix([ (1/p)*V!&+[ ZZ!u[i]*B[i] : i in [1..m] ] : u in Basis(K) ]);\n\tvtime pAdicSaturation, 2 : \n\t    B := Submatrix(HermiteForm(VerticalJoin(B,C)),1,1,m,n);\n\tN := RMatrixSpace(FF,m,n)!B;\n    end while;\n    vprintf pAdicSaturation : \"Rank(N) = %o \\n\", Rank(N), m;\n    return [ B[i] : i in [1..m] ];\nend function;\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2190\n\n",
    "created_at": "2008-02-17T07:01:21Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "implement a ZZ-module saturation algorithm: this is the key thing needed to compute kernels over ZZ, etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2190",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Saturation of a matrix, i.e., this command in Magma:

```
    (<Mtrx> X) -> Mtrx
    
    The basis of the saturation w.r.t. Q of the space spanned by the rows of X.
```
is really important to a huge amount of my modular forms research.
In Magma this command exists and is quite fast, because I specifically
needed it for my work and Allan spent a lot of time on making it quite
good.  In Sage, it's built on top of PARI's `matkerint` command (one
can -reduce computing saturation to computing the
kernel over ZZ of the transpose matrix).   As a result, Sage is almost
completely and totally useless at doing any saturations when the size
is at all interesting for research.  For example, a very tiny example
below is nearly a hundred times slower in Sage than in Magma!

```
sage: a = random_matrix(ZZ, 40, 42)
sage: w = a.row_space()
sage: time s =w.saturation()
CPU times: user 0.79 s, sys: 0.07 s, total: 0.86 s
Wall time: 0.89
sage: b = magma(a)
sage: magma.eval('time c := Saturation(%s);'%b.name())
'Time: 0.010'
sage: 0.89 / 0.01
89.0000000000000
```

Here are some more examples:

```
sage: a = random_matrix(ZZ, 150,150)
sage: w = a.row_space()
sage: time s = w.saturation()
CPU times: user 1.36 s, sys: 0.21 s, total: 1.57 s
Wall time: 1.64
sage: m = magma(a)
sage: magma.eval('time c := Saturation(%s);'%m.name())
'Time: 0.290'
```

and a very typical one for my research would look like this:

```
sage: a = random_matrix(ZZ, 100,300)
sage: w = a.row_space()
sage: time s = w.saturation()
[[[waited many many minutes --- no answer]]]
sage: a = random_matrix(ZZ, 100,300)
sage: m = magma(a)
sage: magma.eval('time c := Saturation(%s);'%m.name())
'Time: 0.810'
```

I just want to pause to emphasize that:
1. there is no open source code in the world as far as I know that
can do saturations quickly; only Magma does them right now, and
2. doing these reasonably quickly is utterly essential to my modular computational forms research.  
3. The current situation is that what should be an easy everyday calculation for me -- e.g., saturating a 100x300 -- takes probably *hours* in Sage, but less than one second in Magma!


Fortunately, there is a fast algorithm for saturation that depends mainly on kernels over GF(p) and HNF, and we now have very fast HNF because of #174. 

Here's some code in Magma that does p-satuation.  This combined with other tricks should lead to a saturation algorithm.  Porting this to Sage is definitely step 1.

```
function pAdicSaturation(B,p) 
    if Type(B[1]) eq SeqEnum then
        V := RSpace(Rationals(),#B[1]);
	B := [ V | v : v in B];
    end if;
    V := Universe(B);
    n := Degree(V);
    for i in [1..#B] do
	B[i] *:= LCM([ Denominator(c) : c in Eltseq(B[i]) ]);
    end for;
    ZZ := Integers();
    FF := FiniteField(p);
    B := RMatrixSpace(ZZ,#B,n)!Matrix(B);
    m := Rank(B);
    B := Submatrix(HermiteForm(B),1,1,m,n);
    N := RMatrixSpace(FF,m,n)!B;
    while Rank(N) lt m do 
	K := Kernel(N);
	vprintf pAdicSaturation : 
	    "Rank(N) + Rank(K) = %o + %o = %o\n", Rank(N), Rank(K), m;
	C := RMatrixSpace(ZZ,#Basis(K),n)!
	Matrix([ (1/p)*V!&+[ ZZ!u[i]*B[i] : i in [1..m] ] : u in Basis(K) ]);
	vtime pAdicSaturation, 2 : 
	    B := Submatrix(HermiteForm(VerticalJoin(B,C)),1,1,m,n);
	N := RMatrixSpace(FF,m,n)!B;
    end while;
    vprintf pAdicSaturation : "Rank(N) = %o \n", Rank(N), m;
    return [ B[i] : i in [1..m] ];
end function;
```

Issue created by migration from https://trac.sagemath.org/ticket/2190





---

archive/issue_comments_014344.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-02-17T07:01:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2190",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2190#issuecomment-14344",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_014345.json:
```json
{
    "body": "The patch is here: \n\n  http://sage.math.washington.edu/home/was/tmp/saturation.hg\n\nThis includes the hnf stuff from #174, since this code depends on it.\nIt also includes numerous bug fixes and documentation enhancements to\nthe new determinant code.  \n\nVERY IMPORTANT: Sage-2.10.2 should not be released without this,\nunless all the new HNF code is also removed, since this fixes so\nmany subtle issues with that code that I discovered when building\nthis code on top of it.",
    "created_at": "2008-02-18T23:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2190",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2190#issuecomment-14345",
    "user": "https://github.com/williamstein"
}
```

The patch is here: 

  http://sage.math.washington.edu/home/was/tmp/saturation.hg

This includes the hnf stuff from #174, since this code depends on it.
It also includes numerous bug fixes and documentation enhancements to
the new determinant code.  

VERY IMPORTANT: Sage-2.10.2 should not be released without this,
unless all the new HNF code is also removed, since this fixes so
many subtle issues with that code that I discovered when building
this code on top of it.



---

archive/issue_events_005235.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-02-18T23:15:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2190",
    "milestone": "sage-2.10.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2190#event-5235"
}
```



---

archive/issue_comments_014346.json:
```json
{
    "body": "Here are some obligatory benchmarks for new saturation code.   The speed\nis still slower than Magma in many cases, but vastly faster (e.g., over 3000\ntimes faster on a reasonable problem) than Sage used to be:\n\n```\n\nsage: a = random_matrix(ZZ,40,42)\nsage: time b = a.saturation()\nCPU times: user 0.19 s, sys: 0.04 s, total: 0.23 s\nWall time: 0.23\nsage: a = random_matrix(ZZ,150)\nsage: time b = a.saturation()\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01\nsage: a = random_matrix(ZZ,100, 300)\nsage: time b = a.saturation()\nCPU times: user 5.16 s, sys: 0.24 s, total: 5.40 s   # this used to take 5 hours!\nWall time: 5.40\n```\n\nNote: to speed up sage more the main thing will be to just optimized the \"add_row\" procedure, which should be easy.",
    "created_at": "2008-02-18T23:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2190",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2190#issuecomment-14346",
    "user": "https://github.com/williamstein"
}
```

Here are some obligatory benchmarks for new saturation code.   The speed
is still slower than Magma in many cases, but vastly faster (e.g., over 3000
times faster on a reasonable problem) than Sage used to be:

```

sage: a = random_matrix(ZZ,40,42)
sage: time b = a.saturation()
CPU times: user 0.19 s, sys: 0.04 s, total: 0.23 s
Wall time: 0.23
sage: a = random_matrix(ZZ,150)
sage: time b = a.saturation()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01
sage: a = random_matrix(ZZ,100, 300)
sage: time b = a.saturation()
CPU times: user 5.16 s, sys: 0.24 s, total: 5.40 s   # this used to take 5 hours!
Wall time: 5.40
```

Note: to speed up sage more the main thing will be to just optimized the "add_row" procedure, which should be easy.



---

archive/issue_comments_014347.json:
```json
{
    "body": "Merged saturation.hg from 02/18/2008 03:15:21.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-19T09:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2190",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2190#issuecomment-14347",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged saturation.hg from 02/18/2008 03:15:21.

Cheers,

Michael



---

archive/issue_comments_014348.json:
```json
{
    "body": "The bundle has been extensively tested and I have verified via valgrind that it doesn't leak memory. While nobody external ever did a formal review I am giving this a positive review due to the excessive amount of testing. Feel free to do a formal review, but please open another ticket in case you come up with any issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T03:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2190",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2190#issuecomment-14348",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The bundle has been extensively tested and I have verified via valgrind that it doesn't leak memory. While nobody external ever did a formal review I am giving this a positive review due to the excessive amount of testing. Feel free to do a formal review, but please open another ticket in case you come up with any issues.

Cheers,

Michael



---

archive/issue_comments_014349.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-21T03:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2190",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2190#issuecomment-14349",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014350.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-21T03:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2190",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2190#issuecomment-14350",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1



---

archive/issue_events_005236.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-21T03:11:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2190",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2190#event-5236"
}
```
