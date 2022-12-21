# Issue 3933: Set iteration is broken over sets created with iterators

Issue created by migration from Trac.

Original creator: anakha

Original creation time: 2008-08-22 19:12:05

Assignee: cwitty

This works:

sage: list(Set([1, 2, 3, 4, 5]))
[1, 2, 3, 4, 5]

But this doesn't:

sage: list(Set(iter([1, 2, 3, 4, 5])))
[]

Basically Set makes a Set_object() out of it and Set_object is really not prepared to deal with an iterator.  I glanced over the code and did find an obvious solution.


---

Comment by anakha created at 2008-08-22 19:13:38

The examples should read


```
sage: list(Set([1, 2, 3, 4, 5]))
[1, 2, 3, 4, 5]
```


and 


```
sage: list(Set(iter([1, 2, 3, 4, 5])))
[]
```



---

Comment by rlm created at 2009-01-23 14:00:39

amusingly:


```
sage: list(Set(iter([1, 2, 3, 4, 5])))
[]
sage: list(Set(set(iter([1, 2, 3, 4, 5]))))
[1, 2, 3, 4, 5]
```



---

Comment by rlm created at 2009-01-23 14:08:00

Also, I was worried about giving it an infinite iterator, but it seems Python is happy to shoot itself in the foot:


```
sage: set(Primes())
<wait approximately forever for nothing to happen>
```



---

Attachment


---

Comment by abergeron created at 2009-01-24 03:31:01

This works and passes tests.  So I give it a positive review.


---

Comment by mabshoff created at 2009-01-25 20:59:17

Resolution: fixed


---

Comment by mabshoff created at 2009-01-25 20:59:17

Merged in Sage 3.3.alpha3
