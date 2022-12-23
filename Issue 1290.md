# Issue 1290: [with patch] add computationg of Rencontres numbers to Sage

Issue created by migration from https://trac.sagemath.org/ticket/1290

Original creator: was

Original creation time: 2007-11-27 14:43:43

Assignee: mhansen

CC:  sage-combinat

Dan Drake posted this on sage-devel, and I reformatted it into a proper patch.

I rewrote the patch to avoid using any symbolic computation (e.g., maxima) for speed and to be correct when the input/output is very large. 


---

Attachment

See my alternative on the mailing list sage-devel: derangements = rencontres


```
def derangements(n, k):
     if n == 0 and k == 0:
         return 1
     if n == 1 and k == 0:
         return 0

     if k == 0:
         lst = [(-1)^r * binomial(n, r) * (n-r)^r * (n-r-1)^(n-r) for r in range(n)]
         return sum(lst)
     else:
         return binomial(n, k) * derangements(n-k, 0)
```


Someone should check the implications!?
Eventually translate it into Cython, etcetera.


---

Comment by mhansen created at 2007-12-02 05:02:07

Looks good to me.


---

Comment by mabshoff created at 2007-12-02 05:56:13

Resolution: fixed


---

Comment by mabshoff created at 2007-12-02 05:56:13

Merged in 2.8.15.alpha2.
