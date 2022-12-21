# Issue 9155: G.list() can be modified

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-06-06 04:35:30

Assignee: AlexGhitza

CC:  rbeezer chapoton

cached_method should not be used with mutable return values


```
sage: G = SymmetricGroup(2)
sage: elements = G.list()
sage: elements.remove(G("()"))
sage: G.list()
[(1,2)]
sage: K = SymmetricGroup(2)
sage: K.list()
[(1,2)]
```


as reported at http://groups.google.com/group/sage-devel/browse_thread/thread/265e134a585cf2bf


---

Comment by mmezzarobba created at 2014-03-15 13:23:33

See also #10927.


---

Comment by jmantysalo created at 2016-04-22 12:26:15

This bug has been corrected. (#10927 is another thing,)


---

Comment by jmantysalo created at 2016-04-22 12:26:15

Changing status from new to needs_review.


---

Comment by jmantysalo created at 2016-04-29 08:41:12

Test added as suggested in email.
----
New commits:


---

Comment by jmantysalo created at 2016-04-29 08:41:12

Changing type from defect to enhancement.


---

Comment by jmantysalo created at 2016-04-29 08:41:12

Changing priority from major to trivial.


---

Comment by jmantysalo created at 2016-04-29 08:41:12

Changing component from algebra to group theory.


---

Comment by chapoton created at 2016-04-29 08:44:08

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2016-04-29 08:44:08

ok, let it be, thanks


---

Comment by vbraun created at 2016-05-01 16:30:16

Resolution: fixed
