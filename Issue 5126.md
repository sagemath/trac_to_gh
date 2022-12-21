# Issue 5126: error coercing stacked polynomial rings to relative number fields

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-01-29 05:07:46

Assignee: was

CC:  roed

Keywords: polynomial ring coercion relative number field

From David Roe, reviewing #1367:


```
I'm not completely convinced that the following example is the behavior we want:

sage: K.<a> = NumberField?(ZZx?.05 + 2, 'a') sage: L.<b> = K.extension(ZZx?.02 + 3*a, 'b') sage: u = QQu?.gen() sage: t = u.parent()t?.gen()

sage: L(u*5) 5*b

I guess if we're going to convert at all this makes the most sense, but I want to think about it a bit more. I'm even less convinced of the following:

sage: W.<w> = t.parent()[] sage: L(w*5) 5*b sage: L(W(t)) 5*a sage: L(W(u)) TypeError?
```



---

Comment by davidloeffler created at 2009-07-21 08:18:40

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-21 08:18:40

Changing assignee from was to davidloeffler.
