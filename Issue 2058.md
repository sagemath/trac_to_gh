# Issue 2058: [with patch, needs review] PolyBoRi evaluation

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-02-05 17:05:33

Assignee: malb

CC:  burcin

Keywords: polybori

With the attached patches `8314.patch` (by burcin) and `8315.patch` (by malb) the following now works:


```
sage: B.<x,y,z> = BooleanPolynomialRing(3)
sage: x.subs({x:y})
y
sage: x.subs({'x':y})
y
sage: x.subs(x=y)
y
```


The implementation is far from being perfect but at least the functionality is there now.


---

Attachment

Burcin's original __call__ patch


---

Comment by malb created at 2008-02-05 17:06:26

my doctests/corrections for Burcin's patch


---

Attachment

patch to be applied on top of the other two to speed up subs method


---

Attachment

yet another patch (to be applied on to of the rest) which speeds up substitution and evalutation


---

Comment by malb created at 2008-02-06 15:01:52

`8316.patch` reorders the coercion by moving integers more to the front. Burcin, if that affects performance for other operations negatively, let me know and I can move it back.


---

Comment by malb created at 2008-02-06 16:11:58

reintroduces evaluation with aribitrary values again


---

Attachment

Patch `8318.patch` addresses a concern burcin raised in a private conversation.


---

Comment by malb created at 2008-02-14 23:37:43

Burcin mentioned some issues in a private communication. Don't apply yet.


---

Attachment

this patch replaces *all* other patches and should address Burcin's off-record concerns


---

Comment by malb created at 2008-02-26 18:00:09

Burcin, could you check if both `__call__` and `subs` now behave as you would expect? I am trying to get this patch (or a corrected version) into 2.10.3. You only need the _superpatch_.


---

Comment by burcin created at 2008-02-26 19:51:03

add doctest to _eval


---

Attachment

Martin's patch looks good, it should be applied.

attachment:booleanmonomial_eval_doctest.patch makes it conform to the "all functions should have a doctest" rule. :)


---

Comment by mabshoff created at 2008-02-26 21:36:32

Merged trac_2058_superpatch.patch and booleanmonomial_eval_doctest.patch in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-26 21:36:32

Resolution: fixed
