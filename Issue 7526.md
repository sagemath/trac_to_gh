# Issue 7526: polynomial_template should avoid unnecessary coercions

Issue created by migration from https://trac.sagemath.org/ticket/7526

Original creator: ylchapuy

Original creation time: 2009-11-24 21:57:05

Assignee: tbd

e.g. in __mod__, we should coerce other only if needed.
This gives great speed up, e.g:

```
sage: R.<x> = GF(3)[]
sage: p=x^100 + x^81 + x^67 + x^33 + 1
sage: q=x^10 + x^8 + x^6 + x^3 + 1
sage: timeit('p%q')
625 loops, best of 3: 677 µs per loop  #Before
625 loops, best of 3: 60.3 µs per loop #After
```




---

Attachment

based on 4.3.alpha0


---

Comment by ylchapuy created at 2009-11-24 22:21:45

Changing status from new to needs_review.


---

Comment by ylchapuy created at 2009-11-24 22:21:45

I'm not totally sure of how this should be done as I don't know the details of coercions, neither the details of the polynomial templating used.

At least, my patch doesn't break any doctest for me.

It touch for methods, the ones using _coerce_.

It test for parent equality before applying coercion. I also introduce a variable

`parent = (<Polynomial_template>self)._parent`

for readability.


---

Comment by malb created at 2009-11-25 20:35:25

The patch looks good and applies & doctests cleanly for me. However, we can do a little better. 

On my machine I get the following:

*Before*

```
sage: R.<x> = GF(3)[]
sage: p=x^100 + x^81 + x^67 + x^33 + 1
sage: q=x^10 + x^8 + x^6 + x^3 + 1
sage: timeit('p%q')
625 loops, best of 3: 193 µs per loop
```


*Patch*

```
sage: R.<x> = GF(3)[]
sage: p=x^100 + x^81 + x^67 + x^33 + 1
sage: q=x^10 + x^8 + x^6 + x^3 + 1
sage: timeit('p%q')
625 loops, best of 3: 26.6 µs per loop
```


With my incremental reviewer patch I get:


```
sage: R.<x> = GF(3)[]
sage: p=x^100 + x^81 + x^67 + x^33 + 1
sage: q=x^10 + x^8 + x^6 + x^3 + 1
sage: timeit('p%q')
625 loops, best of 3: 18.2 µs per loop
```


So, this is a positive review if someone reviews my reviewer patch.


---

Comment by ylchapuy created at 2009-11-25 22:37:03

Replying to [comment:2 malb]:
> So, this is a positive review if someone reviews my reviewer patch.

I think you attached the patch for #7531.


---

Attachment

Woops, fixed.


---

Comment by ylchapuy created at 2009-11-25 23:39:10

Changing status from needs_review to positive_review.


---

Comment by ylchapuy created at 2009-11-25 23:39:10

Great thanks. Still applies fine and doctests ok.
And here is the positive review!


---

Comment by mhansen created at 2009-11-29 05:48:24

Resolution: fixed
