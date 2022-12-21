# Issue 6836: The Sturm bound for modular forms gives the wrong result sometimes

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2009-08-28 14:21:35

Assignee: craigcitro

In the documentation for the Sturm bound, the following appears:

"Kevin Buzzard pointed out to me (William Stein) in Fall 2002 that the above bound is fine for Gamma1 with character, as one sees by taking a power of `f`. More precisely, if `fcong 0pmod{p}` for first `s` coefficients, then `f^r = 0 pmod{p}` for first `s r` coefficients. Since the weight of `f^r` is `r weight(f)`, it follows that if `s >=` the sturm bound for `Gamma_0` at weight(f), then `f^r` has valuation large enough to be forced to be `0` at `r *` weight(f) by Sturm bound (which is valid if we choose `r` right). Thus `f cong 0 pmod{p}`. Conclusion: For `Gamma_1` with fixed character, the Sturm bound is *exactly* the same as for           `Gamma_0`. "

However, this does not seem to be the case:


```
sage: CuspForms(DG144.1^2,3).sturm_bound()
3457
sage: CuspForms(Gamma0(144),3).sturm_bound()
73
```


I believe that this is due to the following code in the `sturm_bound` method for modular forms:


```
if M is not None:
            raise NotImplementedError
        if self.__sturm_bound is None:
            # the +1 below is because O(q^prec) has precision prec.
            self.__sturm_bound =      self.group().sturm_bound(self.weight())+1
        return self.__sturm_bound

```

where `self.group()' gives the wrong answer in the case of `Gamma_1` with fixed character, because it returns `Gamma_1` rather than `Gamma_0`.

I propose that the code above should be of the form

```
if M is not None:
            raise NotImplementedError
        if self.__sturm_bound is None:
            # the +1 below is because O(q^prec) has precision prec.
            G=self.group()
            if G=Gamma1(G.level()) and self.character() in DirichletGroup(self.level()):
                G=Gamma0(G.level())
            self.__sturm_bound = G.sturm_bound(self.weight())+1
        return self.__sturm_bound
```

before the sturm_bound variable is set, which would implement the remark of Buzzard given above.


---

Comment by AlexGhitza created at 2010-01-03 11:59:32

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-01-03 11:59:32

Changing keywords from "" to "sturm bound character".


---

Comment by AlexGhitza created at 2010-01-03 11:59:32

Implemented Lloyd's suggestion (with some changes to the code).  See the patch.


---

Comment by AlexGhitza created at 2010-01-03 11:59:32

Changing priority from minor to major.


---

Attachment


---

Comment by davidloeffler created at 2010-04-05 13:30:14

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-04-05 13:30:14

Looks fine to me, and tests pass on 4.3.5 (with all the other patches in the positive_review pile already applied).


---

Attachment


---

Comment by jhpalmieri created at 2010-04-15 05:37:04

Here's a patch to make the docs build without error.


---

Comment by jhpalmieri created at 2010-04-15 05:57:06

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 05:57:06

Merged in 4.4.alpha0:

 - trac_6836.patch
 - trac_6836-trivial-doc.patch
