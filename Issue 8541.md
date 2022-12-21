# Issue 8541: modular forms / linear algebra issue -- subspace not invariant

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-03-15 05:20:37

Assignee: craigcitro


```
sage: CuspForms(DirichletGroup(5).0,5).0
sage: f[15]
Boom!
}}} 

This was reported by Paul Nelson, a grad student at Caltech.


---

Comment by davidloeffler created at 2010-04-08 18:24:41

Changing assignee from craigcitro to jason, was.


---

Comment by davidloeffler created at 2010-04-08 18:24:41

The problem is in the multimodular algorithm that's used for computing matrix multiplication over cyclotomic fields:


```
sage: K.<zeta4> = CyclotomicField(4)
sage: m = matrix(K, 1, 1, [186])
sage: n = matrix(K, 1, 2, [1, -6/125*zeta4 - 117/125])
sage: m * n
[                 -23087/125 -1116/125*zeta4 - 21762/125]
```


According to the output of verbose, it works modulo a single prime (split in K), in this case 46337; and the result is indeed correct modulo this prime. But that's not enough, clearly. I'm very suspicious about the method `sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense.height()`. It returns the maximum absolute value of any entry (in any complex embedding), so n has height 1. Shouldn't it return the maximum absolute value of the numerator or denominator of any element, as with the corresponding method for dense rational matrices? (What does this even mean when K doesn't have class number 1?)


---

Comment by davidloeffler created at 2010-04-08 18:24:41

Changing component from modular forms to linear algebra.


---

Comment by davidloeffler created at 2010-04-08 18:57:14

Hold it, my suspicion was wrong: the height method only gets called after clearing denominators, and the problem is still there if we use the integral matrix `n = matrix(K, [125, -6*zeta4 - 117])`. So maybe the problem is here:

```
        # conservative but correct estimate
        bound = A.height() * B.height() * self._ncols
```

Perhaps this estimate is wrong in this degenerate case?


---

Comment by davidloeffler created at 2010-04-09 11:25:45

Changing priority from major to critical.


---

Comment by davidloeffler created at 2010-04-09 21:18:08

Changing priority from critical to blocker.


---

Comment by burcin created at 2010-04-11 12:46:51

This seems to be a duplicate of #8666, which already has a positive review.


---

Comment by davidloeffler created at 2010-04-11 20:22:49

Changing priority from blocker to minor.


---

Comment by davidloeffler created at 2010-04-11 20:22:49

Arguably, the correct statement is that #8666 is a duplicate of this :-).

Just to be safe, it might be worth adding a doctest to the modular forms code to show that the computation that triggered the problem in the original bug report does now work -- I will write a mini-patch tomorrow morning. When that is reviewed and merged then we can close this ticket, but in any case the ticket "priority" flag can safely be reduced.


---

Comment by davidloeffler created at 2010-04-12 13:56:47

apply after #8666


---

Attachment

As promised, here's a doctest.


---

Comment by davidloeffler created at 2010-04-12 13:57:32

Changing status from new to needs_review.


---

Comment by was created at 2010-04-14 23:51:37

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 18:42:12

Merged "trac_8541.patch" in 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-16 18:42:12

Resolution: fixed
