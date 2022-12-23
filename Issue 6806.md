# Issue 6806: typo in patch of ticket #6396: primes_of_degree_one is broken for relative extensions

Issue created by migration from https://trac.sagemath.org/ticket/6806

Original creator: mvngu

Original creation time: 2009-08-22 20:26:11

Assignee: tba

CC:  davidloeffler ncalexan

The patch trac_6396-deg1primes.patch at ticket #6396 has this docstring:

```
201             We test that #6396 is fixed. Note that the doctest is flagged as random
202             since the string representation of ideals is somewhat unpredictable.::
203
204                 sage: N.<a,b> = NumberField([x^2 + 1, x^2 - 5])
205                 sage: ids = N.primes_of_degree_one_list(10); a # random
206                 [Fractional ideal ((-1/2*b + 1/2)*a + 2),
207                  Fractional ideal (-b*a + 1/2*b + 1/2),
208                  Fractional ideal ((1/2*b + 3/2)*a - b),
209                  Fractional ideal ((-1/2*b - 3/2)*a + b - 1),
210                  Fractional ideal (-b*a - b + 1),
211                  Fractional ideal (3*a + 1/2*b - 1/2),
212                  Fractional ideal ((-3/2*b + 1/2)*a + 1/2*b - 1/2),
213                  Fractional ideal ((-1/2*b - 5/2)*a - b + 1),
214                  Fractional ideal (2*a - 3/2*b - 1/2),
215                  Fractional ideal (3*a + 1/2*b + 5/2)]
```

In particular, note line 205:

```
sage: ids = N.primes_of_degree_one_list(10); a # random
```

which the docstring flags as random. But I think the "a" on that line is a typo, because with Sage 4.1.1 this is what I get:

```
sage: N.<a,b> = NumberField([x^2 + 1, x^2 - 5])
sage: ids = N.primes_of_degree_one_list(10)
sage: ids
[Fractional ideal (2*a + 1/2*b - 1/2),
 Fractional ideal ((-1/2*b - 1/2)*a - b),
 Fractional ideal (b*a + 1/2*b + 3/2),
 Fractional ideal ((-1/2*b - 3/2)*a + b - 1),
 Fractional ideal ((-b + 1)*a + b),
 Fractional ideal (3*a + 1/2*b - 1/2),
 Fractional ideal ((1/2*b - 1/2)*a + 3/2*b - 1/2),
 Fractional ideal ((-1/2*b - 5/2)*a - b + 1),
 Fractional ideal (2*a - 3/2*b - 1/2),
 Fractional ideal (3*a + 1/2*b + 5/2)]
```

That is, I replaced the "a" with "ids".


---

Comment by mvngu created at 2009-08-22 21:54:23

based on Sage 4.1.1


---

Attachment


---

Comment by kcrisman created at 2009-09-14 21:07:36

This is clearly what's going on.  Positive review.


---

Comment by mvngu created at 2009-09-16 01:12:25

Resolution: fixed
