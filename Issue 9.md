# Issue 9: Memory leak _is_relaxation()

`src/sage/matroids/basis_matroid.pyx` has `_is_relaxation()` with `bitset_init` for `bb_comp` and `b2`, but no corresponding `bitset_free`. Try this:


```
from sage.matroids.advanced import *
import gc

i = 0
while True:
    if i%1000==0: print get_memory_usage()
    i += 1
    M = BasisMatroid(matroids.named_matroids.NonFano())
    N = BasisMatroid(matroids.named_matroids.Fano())
    m = {e:e for e in M.groundset()}
    M._is_relaxation(N, m)
    N._is_relaxation(M, m)
```


Issue created by migration from https://trac.sagemath.org/ticket/26806




---

this was easy


---

Thanks. Please fill author name and put to needs_review.

If this was too easy, see `psi(0.5)` at #19363...


---

Changing status from new to needs_review.


---

Changing status from needs_review to positive_review.


---

Thanks.


---

Resolution: fixed
