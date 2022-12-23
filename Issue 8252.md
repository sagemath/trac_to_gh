# Issue 8252: names parameter in optimized_representation is tweaked,

Issue created by migration from https://trac.sagemath.org/ticket/8252

Original creator: syazdani

Original creation time: 2010-02-12 22:17:51

Assignee: davidloeffler

Keywords: number fields

Here is a bit of annoyance:

```
sage: K.<a>=NumberField(x^2+1)
sage: L.<b>=K.extension(x^2+5)
sage: Labs.<tau> = L.absolute_field()
sage: Lnice = Labs.optimized_representation(names='t')
sage: Lnice[0]
Number Field in t3 with defining polynomial x^4 + 3*x^2 + 1
```


While the more reasonable output should be 

```
Number Field in t with defining polynomial x^4 + 3*x^2 + 1
```


I've looked at the code, and the problem is that the helper function that finds the optimized number field calculates all sorts of other fields, and needs to make sure the names don't conflict with each other, so the output makes sense in that front. However, the output is still unexpected for the user. 

There is an obvious hack that can solve this problem (edit Lnice._names before returning from optimized_representation), but I'm not sure if that's the best approach (side effects scare me).


---

Comment by AlexGhitza created at 2014-04-18 05:29:45

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2014-04-18 05:29:45

New commits:


---

Comment by rws created at 2014-05-20 13:03:15


```
sage -t --long src/sage/schemes/elliptic_curves/heegner.py  # 2 doctests failed
```



---

Comment by rws created at 2014-05-20 13:03:15

Changing status from needs_review to needs_work.
