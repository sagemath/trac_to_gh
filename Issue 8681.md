# Issue 8681: implement matrix actions on binary quadratic forms

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2010-04-13 13:05:18

Assignee: justin

CC:  tornaria was jonhanke ncalexan cremona

The attached patch implements methods for left and right matrix actions on binary quadratic forms.  It also extends the constructor `BinaryQF` to accept a homogeneous polynomial of degree 2 in 2 variables.


---

Comment by AlexGhitza created at 2010-04-13 13:06:41

Changing status from new to needs_review.


---

Comment by tornaria created at 2010-04-13 13:48:25

The patch looks good to me -- pending actually trying it.

I wonder if it would make sense to avoid using polynomials as much as possible, except for convenience printing and input. For instance, `matrix_action_left` could be defined using something like:

```
v,w = M.columns()
a1 = Q(*v)
c1 = Q(*w)
b1 = Q(*(v+w))-a1-c1
return BinaryQF(a1,b1,c1)
```

and `matrix_action_right` defined similarly with `rows()` instead of `columns()`.

I see that `__call__` is itself defined using polynomials instead of the other way around --- should that be changed as well?
e.g.


```
def __call__(self, *x):
  if len(x)==1:
    x = x[0]
  x, y = x
  return (self._a * x + self._b * y) * x + self._c * y**2
```


and


```
def polynomial(self):
  return self(ZZ['x,y'].gens())
```


besides, with the definition of `__call__` I propose above, one can actually evaluate a quadratic form at a vector (so, the * in the proposed matrix actions above would no longer be necessary -- it is because `Q(v)` now fails for v a vector, which is inconvenient IMO).


---

Comment by AlexGhitza created at 2010-04-13 21:54:09

Changing status from needs_review to needs_work.


---

Comment by AlexGhitza created at 2010-04-13 21:54:09

Gonzalo,

all of this sounds good, pending (to borrow your expression) actually trying it out.  I will do this when I get a chance later today.  I expect a performance gain and no down-sides.


---

Comment by AlexGhitza created at 2010-04-14 11:18:03

Changing status from needs_work to needs_review.


---

Attachment

I have implemented Gonzalo's suggestions.  It seems to work great, and indeed it's much faster; the matrix actions are almost 3 times faster with the new code, and `__call__` is an amazing 200 times faster.


---

Comment by cremona created at 2010-04-25 17:01:07

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-04-25 17:01:07

This looks very good.  After the discussion above I was expecting a much larger patch, but this is nice and simple, and works.

Applies fine to 4.4.rc0 and all tests in sage/quadratic_forms pass.

Positive review!


---

Comment by was created at 2010-04-29 05:19:31

Resolution: fixed


---

Comment by bascorp2 created at 2010-05-26 08:40:41

[city pictures](http://like-search.info/)
