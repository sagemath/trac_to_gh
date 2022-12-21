# Issue 2190: implement a ZZ-module saturation algorithm: this is the key thing needed to compute kernels over ZZ, etc.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-17 07:01:21

Assignee: was

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
[This is the Trac macro *[waited many many minutes --- no answer* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[waited many many minutes --- no answer-macro)]
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



---

Comment by was created at 2008-02-17 07:01:42

Changing type from defect to enhancement.


---

Comment by was created at 2008-02-18 23:15:21

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

Comment by was created at 2008-02-18 23:18:18

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

Comment by mabshoff created at 2008-02-19 09:41:39

Merged saturation.hg from 02/18/2008 03:15:21.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 03:11:35

The bundle has been extensively tested and I have verified via valgrind that it doesn't leak memory. While nobody external ever did a formal review I am giving this a positive review due to the excessive amount of testing. Feel free to do a formal review, but please open another ticket in case you come up with any issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 03:11:59

Resolution: fixed


---

Comment by mabshoff created at 2008-02-21 03:11:59

Merged in Sage 2.10.2.alpha1
