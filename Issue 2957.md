# Issue 2957: Singular multivariate polynomials are buggy on exponent overflow

Issue created by migration from https://trac.sagemath.org/ticket/2957

Original creator: cwitty

Original creation time: 2008-04-19 15:33:21

Assignee: somebody

On 64-bit x86, exponents truncate to 32 bits:

```
sage: K.<x,y> = QQ[]
sage: ((x^12345)^54321)^12345
x^2065457633
sage: 12345*54321*12345
8278467437025
sage: (12345*54321*12345) % 2^32
2065457633
```


On 32-bit x86, exponents truncate to 16 bits, and overflow from one variable to another (!!!):

```
sage: K.<x,y> = QQ[]
sage: (x^12345)^54321
x^28393*y^10232
sage: (12345*54321) // 2^16
10232
sage: (12345*54321) % 2^16
28393
```




---

Comment by malb created at 2009-01-23 08:55:29

I'm going to upload a fix in a sec, but it comes at a cost:

## Before

```
sage: P.<x,y> = PolynomialRing(QQ)
sage: %timeit x*y
1000000 loops, best of 3: 288 ns per loop

sage: f = x + 1
sage: g = y + 1
sage: %timeit f*g
1000000 loops, best of 3: 462 ns per loop
```


## After

```
sage: P.<x,y> = PolynomialRing(QQ)
sage: %timeit x*y
1000000 loops, best of 3: 314 ns per loop

sage: f = x + 1
sage: g = y + 1
sage: %timeit f*g
1000000 loops, best of 3: 501 ns per loop
```



---

Comment by malb created at 2009-01-24 10:56:09

I just replaced the existing patch with a new one which improves performance. Burcin spotted earlier, that I forgot to assign a type to `max_exponent_size`. With that, the timing difference is in the range of the normal noise.


---

Comment by burcin created at 2009-01-24 18:39:13

We already discussed this with malb, boothby and was extensively. Here are the points here for reference:
 * the return value of the function `p_GetMaxExp` is an unsigned long, fixing this should let one remove the esum < 0 check
 * `max_exponent_size` in `multi_polynomial_libsingular.pyx` should be declared an `unsigned long`
 * adding an `unlikely` hint for `esum > max_exponent_size` might reduce the speed regression even further

Boothby also remarked that checking for total degree before the degree of each variable might help. Looking at the code again, I think we only check the total degree.


---

Comment by burcin created at 2009-01-24 23:22:54

The `_imul_` method also needs the check.


---

Comment by malb created at 2009-01-25 09:02:10

newest version


---

Attachment

Burcin agrees that this is a positive review now.


---

Comment by mabshoff created at 2009-01-28 14:11:59

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 14:11:59

Resolution: fixed
