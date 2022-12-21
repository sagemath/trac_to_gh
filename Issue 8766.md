# Issue 8766: document the _iadd_ and _imul_ special integer.pyx methods, which mutate self

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-26 13:47:27

Assignee: AlexGhitza

CC:  tscrim

I looked in integer.pyx at the two methods _iadd_ and _imul_, which both mutate self, e.g., allow for:

```
sage: a = 2010
sage: a._imul_(19)
sage: a
38190
```

I expected to find a bug exciting docstring about how these methods are unsafe, etc.   Instead, there is *NOTHING* -- not even a doctest or docstring at all.


---

Comment by was created at 2010-05-05 12:30:50


```
> This is odd. From their names one would expect them to be used in __imul__
> and __iadd__ somewhere in the hierarchy, just like _repr_ is used in
> __repr__, so that they will be used for:
>
> sage: a = 1
> sage: a*=5
>
> as documented here: http://docs.python.org/reference/datamodel.html.
> However, this is not the case. It may be a bug (or yet to be implemented
> feature).

That is not a bug -- it is done on purpose.  The reason is because integers are meant to be *immutable*, since they have a hash method.   If _imul_ were used by __imul__, then people would be mutating integers left and right by accident, and vast amounts of code would consequently have subtle bugs all over the place.   

There might have been a time (maybe a few weeks in 2006) when __imul__ did indeed call _imul_ in Sage, so the name might be a historical remnant. 

Personally, I think the best thing would be:

  (1) Rename _imul_ and _iadd_ to something like _unsafe_inplace_mul_, _unsafe_inplace_add_

  (2) Document them. 

William
```



---

Comment by was created at 2010-05-05 12:31:00

> This is odd. From their names one would expect them to be used in __imul__
> and __iadd__ somewhere in the hierarchy, just like _repr_ is used in
> __repr__, so that they will be used for:
>
> sage: a = 1
> sage: a*=5
>
> as documented here: http://docs.python.org/reference/datamodel.html.
> However, this is not the case. It may be a bug (or yet to be implemented
> feature).

That is not a bug -- it is done on purpose.  The reason is because integers are meant to be *immutable*, since they have a hash method.   If _imul_ were used by __imul__, then people would be mutating integers left and right by accident, and vast amounts of code would consequently have subtle bugs all over the place.   

There might have been a time (maybe a few weeks in 2006) when __imul__ did indeed call _imul_ in Sage, so the name might be a historical remnant. 

Personally, I think the best thing would be:

  (1) Rename _imul_ and _iadd_ to something like _unsafe_inplace_mul_, _unsafe_inplace_add_

  (2) Document them. 

William


---

Comment by mkoeppe created at 2021-09-10 06:33:56

Outdated, these methods no longer exist


---

Comment by mkoeppe created at 2021-09-10 06:33:56

Changing status from new to needs_review.


---

Comment by lorenz created at 2021-09-10 06:37:52

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-09-10 17:33:19

Resolution: invalid
