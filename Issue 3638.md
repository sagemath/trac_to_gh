# Issue 3638: Vector equality coercion problems

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2008-07-11 02:08:47

Assignee: tbd

I think this bit of code should not produce an exception.  The vectors should both be coerced to belong to Z8!^3 and compared.

```
sage: Z8=IntegerModRing(8)
sage: vector(ZZ,[1,2,11])==vector(Z8,[1,2,3])
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
...
AttributeError: 'FreeModule_ambient' object has no attribute 'ambient_vector_space'
```


Note that a similar thing seems to work in other cases (because 7 is prime and Z7 is a field?).

```
sage: Z7=IntegerModRing(7)
sage: vector(ZZ,[1,2,10])==vector(Z7,[1,2,3])
True
```



This may or may not be related, but combining QQ and Z7 produces some wrong results:

```
sage: Z7=IntegerModRing(7)
sage: vector(Z7,[1,2,3])==vector(QQ,[1,2,3])
False
```

That those vectors are not equal is truly disturbing.  This should either raise an exception about not having compatible parents or should be True.  I'll let the coercion guru's argue about that. :)


---

Comment by malb created at 2009-01-25 19:00:03

Changing assignee from tbd to malb.


---

Comment by malb created at 2009-01-25 19:00:03

Changing status from new to assigned.


---

Attachment

Fixed the Z/8Z case. As for Z/7Z and Q, they are incomparable, which by convention means == returns False. (If it gave an error,we would have to re-think nonsense like `"some string" != random_matrix(ZZ, 3)` returning False).


---

Comment by robertwb created at 2010-01-17 09:43:06

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-01-19 01:32:45

Looks good to me.


---

Comment by mhansen created at 2010-01-19 01:32:45

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 05:33:33

Resolution: fixed
