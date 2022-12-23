# Issue 2674: Bug in modforms

Issue created by migration from https://trac.sagemath.org/ticket/2674

Original creator: justin

Original creation time: 2008-03-26 16:37:12

Assignee: was

Reported by Jay Pottharst <sharlaon`@`gmail.com>:

```
sage: b=CuspForms(22).basis()
sage: sum(b)
Traceback (most recent call last):
...
NameError: global name 'other' is not defined
```

This covers up a possibly larger problem:

```
sage: ssum=0
sage: for u in b:
...     ssum=(ssum+u)
...
Traceback (most recent call last):
...
TypeError: unsupported operand parent(s) for '+': 'Integer Ring' and
'Cuspidal subspace of dimension 2 of Modular Forms space of dimension
5 for Congruence Subgroup Gamma0(22) of weight 2 over Rational Field'
```


The first problem is easily fixed.




---

Comment by justin created at 2008-03-26 16:37:49

Fix for the first of the two reported problms.


---

Attachment

I disagree that the second issue is a bug:

```

Note that 

  b[0] + 0

and 

  0 + b[0]

should *not* work, since in each case that's a canonical coercion,
and there is no natural map from ZZ (the parent of 0) into CuspForms(...)
for any weight except 0.   In Sage coercions should not happen automatically
unless they are in some way natural and well defined on the whole domain
of the coercion (in this case ZZ).
```



---

Attachment

This new patch fixes the first issue reported above, as well as making the natural coercion from a subspace of modular forms into its parent work. 

Interestingly, this makes the second issue work, too.

So I'm not sure whether or not I like that this second issue works, because I agree with William's point that it should only work if there is a coercion from ZZ to a space of ModularForms. However, it's working "for free" for us, because it ultimately uses that the following works:


```
sage: M = ZZ**5
sage: M(0)
(0, 0, 0, 0, 0)
sage: M(1)
...
<type 'exceptions.TypeError'>: can't initialize vector from nonzero non-list
```


The issue is that a free module knows how to coerce 0 in, but no other integer (even when the module is rank 1 over ZZ, which I think is a good thing). So we could easily change it to make William's expectations correct by changing free modules, where the same issue arises.


---

Comment by craigcitro created at 2008-03-26 22:56:23

Changing assignee from was to craigcitro.


---

Attachment

Apply the bottom two patches in order, and this should also make coercion from `ModularForms(Gamma0(N))` to `ModularForms(Gamma0(Nd))` work. Note that it's currently *not* going to work involving `Gamma1(N)` -- this is because of a bug in `sturm_bound` (namely that it assumes it's working on `Gamma0`); I'm going to file another ticket for this, because I don't have time to fix it right now.


---

Comment by craigcitro created at 2008-03-26 22:56:23

Changing status from new to assigned.


---

Comment by robertwb created at 2008-03-26 23:12:57

Nice work. Apply only the second two patches in order (they do more than just fix this bug).


---

Comment by mabshoff created at 2008-03-26 23:18:21

Resolution: fixed


---

Comment by mabshoff created at 2008-03-26 23:18:21

Merged trac-2674.patch and trac-2674-pt2.patch in Sage 2.11.alpha2
