# Issue 4977: vector(RR vector) doesn't create a new vector

Issue created by migration from https://trac.sagemath.org/ticket/4977

Original creator: jason

Original creation time: 2009-01-14 21:44:34

Assignee: was


```
Hi,

Is there a reason why, in sage 3.2.2, the following works :

sage: vector(vector((1, 6)))
(1, 6)

but the following doesn't :

sage: vector(vector((1, 6.8)))
Traceback (most recent call last):
...
TypeError: _vector_() takes exactly one argument (0 given)

???

Thank you,

Sébastien Labbé
UQAM


```




---

Comment by slabbe created at 2009-01-15 15:20:20

I want also to mention that the same problem was occuring when using the Symbolic Ring :

```
sage: vector(vector(SR, (1, sqrt(2)) ) )
```



---

Attachment


---

Comment by AlexGhitza created at 2009-01-22 00:12:37

Looks good.


---

Comment by mabshoff created at 2009-01-23 08:03:28

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 08:03:28

Merged in Sage 3.3.alpha1
