# Issue 834: performance issue -- echelon strassen mod p -- Sage is better than linbox on my computer., so why use linbox by default

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-06 04:52:42

Assignee: was

I'm not sure if this ticket should stay.  IT's suspicious...


See this example, where changing from Linbox's echelon to use Sage's Strassen with a wise choice of cuttoff improves performance by a factor of 3:


```
sage: time c=a._echelon_strassen(1000)   # uses linbox
CPU times: user 1.47 s, sys: 0.02 s, total: 1.50 s
Wall time: 1.49
sage: a = random_matrix(GF(17),1000)
sage: time b = a.echelon_form()
CPU times: user 1.48 s, sys: 0.01 s, total: 1.48 s
Wall time: 1.48
sage: time c = a._echelon_strassen(8)
CPU times: user 1.15 s, sys: 0.00 s, total: 1.15 s
Wall time: 1.15
sage: time c = a._echelon_strassen(32)
CPU times: user 0.90 s, sys: 0.00 s, total: 0.90 s
Wall time: 0.91
sage: time c = a._echelon_strassen(128)
CPU times: user 0.82 s, sys: 0.00 s, total: 0.82 s
Wall time: 0.82
sage: time c = a._echelon_strassen(256)
CPU times: user 0.76 s, sys: 0.00 s, total: 0.76 s
Wall time: 0.76
sage: time c = a._echelon_strassen(512)
CPU times: user 0.67 s, sys: 0.00 s, total: 0.67 s
Wall time: 0.67

Linbox isn't so good:

sage: a = random_matrix(GF(17),1000)
sage: time b = a.echelon_form(algorithm='linbox')
CPU times: user 1.49 s, sys: 0.02 s, total: 1.51 s
Wall time: 1.53
sage: time b = a.echelon_form(algorithm='linbox')
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
sage: a = random_matrix(GF(17),1000)
sage: time b = a.echelon_form(algorithm='linbox')
CPU times: user 1.53 s, sys: 0.07 s, total: 1.60 s
Wall time: 2.01
```


On my machine, Magma takes 0.39 seconds to do that strassen, so 0.67 is a reasonable time. 
But 1.57 is not.

sage: magma.eval('A:=Random(MatrixAlgebra(GF(17),1000)); time E := EchelonForm(A);')
'Time: 0.390'



---

Comment by mabshoff created at 2007-10-06 10:34:46

The interesting question is whether your Sage install uses ATLAS or netlib org's F77 BLAS in LinBox's case.

Cheers,

Michael


---

Comment by malb created at 2008-02-26 23:55:49

Is this still a valid ticket?


---

Comment by was created at 2008-02-27 12:30:08

I think this is no longer valid since we use ATLAS by default now.

Some timings:


ON OS X:

```
sage: a = random_matrix(GF(17),1000)
sage: time b=a.echelon_form(algorithm='gauss')
CPU times: user 2.33 s, sys: 0.01 s, total: 2.34 s
Wall time: 2.34
sage: a._clear_cache()
sage: time b=a.echelon_form(algorithm='linbox')
CPU times: user 0.72 s, sys: 0.06 s, total: 0.78 s
Wall time: 0.74
sage: a._clear_cache()
sage: time c=a._echelon_strassen(1000) 
CPU times: user 0.87 s, sys: 0.07 s, total: 0.93 s
Wall time: 0.89
```


when repeated timings are about the same as above.

On Linux:

```
sage: a = random_matrix(GF(17),1000)
sage: time a._clear_cache(); a.echelon_form(algorithm='linbox')
CPU times: user 1.24 s, sys: 0.06 s, total: 1.30 s
Wall time: 1.30
sage: time a._clear_cache(); a._echelon_strassen(1000)
CPU times: user 1.25 s, sys: 0.07 s, total: 1.32 s
Wall time: 1.32
sage: time a._clear_cache(); a._echelon_strassen(128)
CPU times: user 1.56 s, sys: 0.10 s, total: 1.66 s
Wall time: 1.66
sage: time a._clear_cache(); a._echelon_strassen(512)
CPU times: user 1.30 s, sys: 0.10 s, total: 1.40 s
Wall time: 1.40
```


Conclusion: Linbox always wins, at least by a tiny amount.
Anyway, with Clement around full time, Linbox is only going
to improve rapidly, IMHO.


---

Comment by was created at 2008-02-27 12:30:08

Resolution: fixed
