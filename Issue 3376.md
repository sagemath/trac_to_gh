# Issue 3376: matrix multiplication should use Strassen's algorithm

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2008-06-06 06:54:44

Assignee: was

CC:  malb

Multiplication of large matrices over GF(2) seems to use a cubic algorithm in Sage, whereas Magma
implements Strassen's algorithm:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.2, Release Date: 2008-05-24                       |
| Type notebook() for the GUI, and license() for information.        |
sage: A=Matrix(GF(2),2048);A.randomize()
sage: B=Matrix(GF(2),2048);B.randomize()
sage: time C=A*B
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.03 s

sage: A=Matrix(GF(2),4096);A.randomize()
sage: B=Matrix(GF(2),4096);B.randomize()
sage: time C=A*B
CPU times: user 0.26 s, sys: 0.00 s, total: 0.26 s
Wall time: 0.26 s

sage: A=Matrix(GF(2),8192);A.randomize()
sage: B=Matrix(GF(2),8192);B.randomize()
sage: time C=A*B
CPU times: user 4.31 s, sys: 0.01 s, total: 4.31 s
Wall time: 4.31 s
```

And in Magma:

```
Magma V2.14-8     Fri Jun  6 2008 08:25:49 on pasta    [Seed = 1195890521]
Type ? for help.  Type <Ctrl>-D to quit.

Loading startup file "/users/cacao/zimmerma/.magmarc"

> n:=2048;
> A:=RandomMatrix(GF(2),n,n);
> B:=RandomMatrix(GF(2),n,n);
> time C:=A*B;
Time: 0.030

> n:=4096;
> A:=RandomMatrix(GF(2),n,n);
> B:=RandomMatrix(GF(2),n,n);
> time C:=A*B;
Time: 0.200

> n:=8192;
> A:=RandomMatrix(GF(2),n,n);
> B:=RandomMatrix(GF(2),n,n);
> time C:=A*B;
Time: 1.370
```



---

Comment by mabshoff created at 2008-06-06 07:01:34

Hi Paul,

check out #3204 which has been merged into 3.0.3.a1. The discussion about speeding up m4ri lasted 85 messages - see 


http://groups.google.com/group/sage-devel/browse_thread/thread/aa4edc241ca4d6bb/7b928e8c28dfd4a2

The final number according to malb were:

```
64-bit Debian/GNU Linux, 2.33Ghz Core2Duo (Macbook Pro, 2nd Gen.)
Matrix Dimension        Magma           GAP             M4RI
10,000 x 10,000         2.920           6.691           1.760
16,384 x 16,384         11.140          36.063          6.760
20,000 x 20,000         20.370          -               12.200
32,000 x 32,000         74.260          -               51.510 
```

There is likely more work planned on this at Dev1 next week. Maybe malb can comment on this a little more.

Cheers,

Michael


---

Comment by malb created at 2008-06-06 09:53:17

Actually, some clarifications:
 * Sage as is, uses a O(n<sup>3</sup>/log_2(n)) algorithm ("Method of the Four Russians", sometimes also called greasing)
 * At these sizes (up to 8192) the difference between n<sup>3</sup>/log_2(n) and n<sup>2.807</sup> isn't that important yet (at least on the Core2Duo):

```
sage: A = random_matrix(GF(2),8192)
sage: B = random_matrix(GF(2),8192); B
8192 x 8192 dense matrix over Finite Field of size 2
sage: time C = A*B
CPU times: user 0.96 s, sys: 0.01 s, total: 0.97 s
Wall time: 0.97
```


```
> n:=8192;
> A:=RandomMatrix(GF(2),n,n);
> B:=RandomMatrix(GF(2),n,n);
> time C:= A*B;
Time: 1.570
```

 * The times mentioned by Michael (and posted by me above) are (at least slightly) off since they compare a non-optimised Magma against an optimised Sage, times on the Opteron are more fair:

```
64-bit Suse Linux, 2.4Ghz Opteron 
Matrix Dimension Magma 2.13-5 M4RI-20080521
10,000 x 10,000  2.940        2.250
16,384 x 16,384  9.250        8.800
20,000 x 20,000  16.570       15.480
32,000 x 32,000  59.100       57.800
```

 * In Sage 3.0.3 you get dramatically better performance but still no Strassen-Winograd multiplication by default, since I haven't implemented L2 cache detection yet. To use Strassen-Winograd, do

```
sage: time A._multiply_strassen(B,cutoff=4096)
CPU times: user 0.96 s, sys: 0.01 s, total: 0.97 s
Wall time: 0.97
```

as you can see: It isn't really much faster than M4RM yet, since the tricky part is cache friendliness in that region and our M4RM as seen some love there (see the thread mentioned by Michael).


---

Comment by malb created at 2008-06-06 12:52:08

Changing assignee from was to malb.


---

Comment by malb created at 2008-06-06 12:52:08

Changing status from new to assigned.


---

Comment by zimmerma created at 2008-06-10 08:00:48

Thank you very much Michael and Martin. It seems indeed you had some fun
optimizing m4ri! Looking at the discussion, especially when I saw Gray code,
I wondered whether the techniques we used to multiply polynomials over GF(2)
might be useful too. See <http://hal.inria.fr/inria-00188261/en>.

My initial interest was modular composition: Brent and Kung's 1978 Algo 2.1
enables one to perform a fast modular composition using fast matrix 
multiplication. In turn, modular composition enables to improve polynomial
factorisation or irreducibility tests.

Do you know if Sage implements modular composition, i.e, f(g) mod h over
GF(p)[x]?


---

Comment by malb created at 2008-06-10 12:14:35

I forwarded your question to [sage-devel]

   http://groups.google.com/group/sage-devel/browse_thread/thread/96433650dd75b104

since I don't know the answer. Though, quite likely Sage doesn't implement it. Thanks for the link to the GF(2)[x] paper!


---

Attachment

The patch requires

   http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080601.spkg


---

Attachment


---

Comment by malb created at 2008-08-06 16:41:22

=Correction=

 * apply #3324
 * apply #3780
 * install http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080624.spkg
 * apply `m4ri_strassen_standard.patch`
 * apply `m4ri_20080620.patch`


---

Comment by mabshoff created at 2008-08-31 00:35:32

Positive review for the spkg. Note that there is some debug output to be killed:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3$ ./sage -t devel/sage/sage/matrix/matrix_mod2_dense.pyx
sage -t  devel/sage/sage/matrix/matrix_mod2_dense.pyx       k: 1
k: 1
k: 1
k: 1
k: 1
k: 1
k: 1
k: 1
k: 1
k: 1
k: 1
k: 5
k: 3
k: 2
k: 1
k: 1
k: 2
k: 3
k: 3
k: 3
k: 3
k: 3
k: 1
k: 1

         [2.9 s]
```


Cheers,

Michael


---

Comment by rlm created at 2008-08-31 00:39:03

The two patches here look good.


---

Comment by rlm created at 2008-08-31 00:42:21

The `k: 1` crap is coming from line 573, `src/src/brilliantrussian.c`.


---

Comment by mabshoff created at 2008-08-31 00:53:11

Martin,

I have deleted the line rlm pointed out against policy in the src directory. Please make sure to fix it upstream. I have also cleaned up SPKG.txt a little, so please base the next libm4ri.spkg off the one in Sage 3.1.2.alpha3 since I saw another updated libm4ri.spkg in you spkg directory on sage.math.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-31 00:53:27

Merged both patches and the spkg in Sage 3.1.2.alpha3


---

Comment by mabshoff created at 2008-08-31 00:53:27

Resolution: fixed


---

Comment by mabshoff created at 2008-08-31 03:55:03

Note that the two patches attached to this ticket are diffs. I did commit them in Martin's name.

Cheers,

Michael
