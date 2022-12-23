# Issue 6766: faster powers of factorizations

Issue created by migration from https://trac.sagemath.org/ticket/6766

Original creator: fwclarke

Original creation time: 2009-08-16 21:08:14

Assignee: tbd

CC:  cremona

The patch provides a much faster method for computing powers of commutative factorizations.  This implements a suggestion made by John Cremona in #5188. 
The speed-up is most marked for factorizations of ideals in number fields.
Before:

```
sage: f = NumberField(x^2 + 23, 'a').factor(47)
sage: timeit('f^10')
5 loops, best of 3: 134 ms per loop
```

After:

```
sage: f = NumberField(x^2 + 23, 'a').factor(47)
sage: timeit('f^10')
625 loops, best of 3: 571 µs per loop
```


In addition, five redundant lines have been removed from the `__init__` function of the `Factorization` class.




---

Attachment

Hi Francis. After uploading a patch for a ticket, you should change the subject to "[with patch, needs review]". That way, the ticket can be picked up by the relevant trac report as needing review.


---

Comment by cremona created at 2009-08-18 16:29:29

This looks good to me;  it applies fine to 4.1.1.  I only tested the file which was changed.


---

Comment by mvngu created at 2009-08-18 16:35:53

It would be nice if there are more code to illustrate timings before and after applying the patch. As I see it, the patch claims to optimize an operation and Francis has provided one example. Is it possible to provide some more examples of before and after timing statistics? Such examples goes very well with release tours, in which features are being showcased.


---

Comment by cremona created at 2009-08-18 20:21:33

Replying to [comment:3 mvngu]:
> It would be nice if there are more code to illustrate timings before and after applying the patch. As I see it, the patch claims to optimize an operation and Francis has provided one example. Is it possible to provide some more examples of before and after timing statistics? Such examples goes very well with release tours, in which features are being showcased.

I'm not sure this is really worth it in this case.  Before a stupid method was used (by default) while now a sensible one is.  But on the other hand there are not that many situations where one needs to raise a factoization to a power anyway, so I would not want to make a big issue of this in release notes! [This is not to diminish the credit to Francis for bothering to do the job, of course!]


---

Comment by fwclarke created at 2009-08-18 22:22:54

I agree with John's comments, but  for the record: before (4.1.1)

```
sage: f = factor(120)
sage: for i in range(10): timeit('f^(2^%s)' % i)
....: 
625 loops, best of 3: 80.1 µs per loop
625 loops, best of 3: 538 µs per loop
625 loops, best of 3: 1.03 ms per loop
125 loops, best of 3: 1.5 ms per loop
125 loops, best of 3: 1.93 ms per loop
125 loops, best of 3: 2.39 ms per loop
125 loops, best of 3: 2.81 ms per loop
125 loops, best of 3: 3.23 ms per loop
125 loops, best of 3: 3.7 ms per loop
125 loops, best of 3: 4.12 ms per loop
```

and after (4.1.1 + patch)

```
sage: f = factor(120)
sage: for i in range(10): timeit('f^(2^%s)' % i)
....: 
625 loops, best of 3: 4.49 µs per loop
625 loops, best of 3: 95.1 µs per loop
625 loops, best of 3: 95 µs per loop
625 loops, best of 3: 95 µs per loop
625 loops, best of 3: 95.1 µs per loop
625 loops, best of 3: 95 µs per loop
625 loops, best of 3: 95.2 µs per loop
625 loops, best of 3: 95.2 µs per loop
625 loops, best of 3: 95.3 µs per loop
625 loops, best of 3: 95.3 µs per loop
```

It might be possible to make this faster still.  But as John points out, it's a fairly obscure function.  I only wrote the patch because I found in the course of doing some calculations that the existing code can't cope at all with factorizations of ideals in moderately sized number fields; what takes all the time is the completely unnecessary check for idempotence in the generic power code.


---

Comment by mvngu created at 2009-08-18 22:28:02

Replying to [comment:5 fwclarke]:
> I agree with John's comments, but  for the record: before (4.1.1)

```
sage: f = factor(120)
sage: for i in range(10): timeit('f^(2^%s)' % i)
....: 
625 loops, best of 3: 80.1 µs per loop
625 loops, best of 3: 538 µs per loop
625 loops, best of 3: 1.03 ms per loop
125 loops, best of 3: 1.5 ms per loop
125 loops, best of 3: 1.93 ms per loop
125 loops, best of 3: 2.39 ms per loop
125 loops, best of 3: 2.81 ms per loop
125 loops, best of 3: 3.23 ms per loop
125 loops, best of 3: 3.7 ms per loop
125 loops, best of 3: 4.12 ms per loop
```

> and after (4.1.1 + patch)

```
sage: f = factor(120)
sage: for i in range(10): timeit('f^(2^%s)' % i)
....: 
625 loops, best of 3: 4.49 µs per loop
625 loops, best of 3: 95.1 µs per loop
625 loops, best of 3: 95 µs per loop
625 loops, best of 3: 95 µs per loop
625 loops, best of 3: 95.1 µs per loop
625 loops, best of 3: 95 µs per loop
625 loops, best of 3: 95.2 µs per loop
625 loops, best of 3: 95.2 µs per loop
625 loops, best of 3: 95.3 µs per loop
625 loops, best of 3: 95.3 µs per loop
```

These are what I was looking for. Thank you for providing more examples. And my apologies since my above request was ambiguous.


---

Comment by mvngu created at 2009-08-25 04:44:10

Resolution: fixed
