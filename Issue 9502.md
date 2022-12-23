# Issue 9502: Basis parent bug in FreeModule

Issue created by migration from https://trac.sagemath.org/ticket/9502

Original creator: novoselt

Original creation time: 2010-07-15 02:49:51

Assignee: AlexGhitza

CC:  vbraun

There is an inconsistency in the example below for the echelonized basis of submodules with basis:

```
sage: F = FreeModule(ZZ, 3)
sage: S = F.submodule_with_basis([(1,2,3),(3,2,1)])
sage: parent(S.basis()[0])
Free module of degree 3 and rank 2 over Integer Ring
User basis matrix:
[1 2 3]
[3 2 1]
sage: parent(S.echelonized_basis()[0])
Ambient free module of rank 3 over the principal ideal domain Integer Ring
```


For automatic bases everything is OK:

```
sage: S = F.submodule([(1,2,3),(3,2,1)])
sage: parent(S.echelonized_basis()[0])
Free module of degree 3 and rank 2 over Integer Ring
Echelon basis matrix:
[1 2 3]
[0 4 8]
sage: parent(S.basis()[0])
Free module of degree 3 and rank 2 over Integer Ring
Echelon basis matrix:
[1 2 3]
[0 4 8]
```


I am working on a patch to fix this.


---

Comment by novoselt created at 2010-07-15 07:23:21

Changing status from new to needs_review.


---

Attachment


---

Comment by vbraun created at 2010-07-21 04:18:55

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2010-07-21 04:18:55

Fixes the original issue and is a general improvement! Tests OK on Sage 4.5, too.


---

Comment by ddrake created at 2010-07-22 08:52:19

Changing status from positive_review to needs_work.


---

Comment by ddrake created at 2010-07-22 08:52:19

I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get "ImportError: cannot import name SR". Any ideas? I've rebuilt the entire Sage library and the problem persists.


---

Comment by novoselt created at 2010-07-22 14:06:43

Replying to [comment:4 ddrake]:
> I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get "ImportError: cannot import name SR". Any ideas? I've rebuilt the entire Sage library and the problem persists. 

That's strange, since the patch does not mention `SR`...


---

Comment by kcrisman created at 2010-07-23 01:40:55

Replying to [comment:5 novoselt]:
> Replying to [comment:4 ddrake]:
> > I applied the patch to 4.5.2.alpha0 and when I try to start Sage, I get "ImportError: cannot import name SR". Any ideas? I've rebuilt the entire Sage library and the problem persists. 
> 
> That's strange, since the patch does not mention `SR`...
Sure it does, implicitly - the final bit is part of 

```
cdef class SymbolicRing(CommutativeRing):
```

which is changed.   And #8562 in alpha0 did change the behavior of Fields, though it's not clear to me how that change would affect SR's ability to import...


---

Attachment

Reverted change to symbolic/ring.pyx


---

Comment by novoselt created at 2010-07-24 07:43:32

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2010-07-24 07:43:32

I have reverted the change to `symbolic/ring.pyx` since it is actually not necessary for this ticket (it may be relevant for #9503). Now I don't have problems with 4.5.2.alpha0.


---

Comment by vbraun created at 2010-08-09 22:32:19

Works on 4.5.2. Positive review!

For the maintainer: Apply `trac_9502_basis_parent_bug_in_FreeModule.2.patch` only.


---

Comment by vbraun created at 2010-08-09 22:32:19

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-09-02 11:03:56

Changing component from algebra to linear algebra.


---

Comment by mpatel created at 2010-09-15 10:00:29

Resolution: fixed


---

Comment by ddrake created at 2010-11-12 01:21:31

For future reference: this ticket might have introduced a segfault; see http://groups.google.com/group/sage-devel/t/b1f3a7bec3ba655f and #10250.
