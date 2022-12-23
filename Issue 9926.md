# Issue 9926: non-squarefree Hecke operators on BrandtModule

Issue created by migration from https://trac.sagemath.org/ticket/9927

Original creator: AlexGhitza

Original creation time: 2010-09-17 01:19:51

Assignee: craigcitro

Keywords: brandt module, hecke operator

This was reported by Nicolás Sirolli on sage-nt:


`BrandtModule` has a problem when calculating the n-th Hecke operator
when n is not squarefree, and is smaller than the prime where the
algebra ramifies.

For example, I get a "not implemented" error if I run this


```
sage: B=BrandtModule(13)
sage: B.hecke_matrix(4)
```


Gonzalo Tornaría told me that the 'direct' algorithm is not
implemented when n is not squarefree; hence I found that


```
sage: B.hecke_matrix(4,algorithm='brandt')
```


instead, there is no trouble. A workaround could be (I'm not sure
whether this is the best to do) changing line 852 of brandt.py,


```
if self.level().gcd(n) != 1:
```


for


```
if self.level().gcd(n) != 1 or is_squarefree(n)==False:
```


(and adding `is_squarefree` to the "imports" block).



---

Comment by tornaria created at 2014-08-25 22:49:02

The reason why the 'direct' algorithm is broken for non-squarefree n is that the base class `AmbientHeckeModule` needs to know the character of the modular form.

Since the `BrandtModule` corresponds to modular forms with trivial character, a fix is to just implement the character() method returning a trivial character.


---

Comment by tornaria created at 2014-08-25 23:25:25

Changing status from new to needs_review.


---

Comment by nmsirolli created at 2014-12-29 14:50:13

This fix solves the problem and (unlike the one proposed by me) is reasonable. All tests run fine.

It would be nice to include, in the hecke_matrix method, an example of a n-th Hecke matrix with non-squarefree n.


---

Comment by nmsirolli created at 2014-12-29 14:50:13

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-01-02 15:51:05

Author/Reviewer name should be real names, not trac usernames.


---

Comment by vbraun created at 2015-01-02 15:51:05

Changing status from positive_review to needs_work.


---

Comment by nmsirolli created at 2015-01-02 15:52:57

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2015-01-04 12:43:19

Resolution: fixed
