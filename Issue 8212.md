# Issue 8212: arithmetic on GF(2^n) might be improved

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-02-08 07:06:33

Assignee: AlexGhitza

The default polynomials chosen by Sage to perform arithmetic over
GF(2**n) have sometimes Hamming weight 7 or more, which is not optimal.
Consider for example:

```
sage: T.<a> = GF(2^211)
sage: T.modulus()
x^211 + x^9 + x^6 + x^5 + x^3 + x + 1

def bar(n):
   f = a
   for i in range(n):
      f = f^2
   return f

sage: %timeit bar(10000)
5 loops, best of 3: 88.5 ms per loop
```

With the following pentanomial, we get a nice speedup:

```
sage: R.<x> = PolynomialRing(GF(2))
sage: T.<a> = GF(2^211,name='a',modulus=x^211 + x^11 + x^10 + x^8 + 1)

sage: %timeit bar(10000)
5 loops, best of 3: 57.3 ms per loop
```



---

Comment by ylchapuy created at 2010-02-08 11:31:11

The polynomials used are Conway's polynomials I guess, probably to stick with Magma's behaviour:
http://magma.maths.usyd.edu.au/magma/htmlhelp/text287.htm#1625 .


---

Comment by zimmerma created at 2010-02-08 12:49:44

> The polynomials used are Conway's polynomials[...]

thanks for the explanation. Would it make sense to have an option GF(p<sup>n</sup>,minimalWeight=true)
to produce a polynomial of minimal weight?

Paul


---

Comment by ylchapuy created at 2010-02-08 15:11:38

Here is a proposal. It does the job only for fields GF(2^n) implemented with NTL.

Yann


---

Comment by ylchapuy created at 2010-02-08 15:11:38

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-02-08 16:17:10

> Here is a proposal.

great! A few remarks before a complete review: (i) it would be best to write Conway instead of
conway (maybe except for the option name, if small letters are mandatory); (ii) I get an error
for 2<sup>n</sup> for 2 <= n <= 15:

```
sage:    T.<a> = GF(2^2, modulus='conway')
...
TypeError: Cannot understand modulus
```



---

Comment by zimmerma created at 2010-02-08 16:17:10

Changing assignee from AlexGhitza to zimmerma.


---

Comment by zimmerma created at 2010-02-08 16:28:41

sage -t * did pass (more precisely it did not exhibit more failures with respect to #7773), which
shows that the case p<sup>n</sup> for n <= 15 should be exercised in the tests, especially with the new
modulus=... options.


---

Attachment

Replying to [comment:4 zimmerma]:
> great! A few remarks before a complete review: (i) it would be best to write Conway instead of
> conway (maybe except for the option name, if small letters are mandatory); 

Agreed. I modified the docstring, but didn't touch the conway_polynomial functions (and therefore the RuntimeError).

(ii) I get an error
> for 2<sup>n</sup> for 2 <= n <= 15:

This is expected, that's why I specified implemented with NTL.
For smaller fields, Sage uses Givaro.
The options available for creating fields with Givaro, NTL and Pari are different. Another ticket should probably be opened to add some consistency.

Yann


---

Comment by zimmerma created at 2010-02-09 07:12:31

> Another ticket should probably be opened to add some consistency.

I'm not sure we can let this patch in, which might break some code doing
`T.<a> = GF(q, modulus='conway')`. If the limit for smaller fields is
documented somewhere, I suggest you disable the new options in that case,
and document it in GF?.


---

Comment by ylchapuy created at 2010-02-09 15:43:12

Replying to [comment:7 zimmerma]:
> > Another ticket should probably be opened to add some consistency.
> 
> I'm not sure we can let this patch in, which might break some code doing
> `T.<a> = GF(q, modulus='conway')`. If the limit for smaller fields is
> documented somewhere, I suggest you disable the new options in that case,
> and document it in GF?.

This won't break anything because the option modulus='conway' is new as well.

The limit for the different implementations is documented at the begining of the file finite_field.py
(see http://www.sagemath.org/doc/reference/sage/rings/finite_field.html )

Finally, I opened another ticket (#8220) you might review after this one:

   * it cleans the code and the documentation for finite field creation;
   * modulus = 'conway' and modulus = 'random' are available for all implementations;
   * modulus = 'minimal_weight' is available for all binary fields;
   * it adds modulus = 'first_lexicographic' for all binary fields.


---

Comment by zimmerma created at 2010-02-10 11:14:49

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-02-10 11:14:49

ok, I give a positive review for that ticket, and will review #8220 afterwards. Great work!

Paul

PS: a related question is the following over GF(2): when no irreducible trinomial exists for a 
given degree n, instead of using a pentanomial, one can use an "almost irreducible" trinomial,
i.e., a trinomial x<sup>n+d</sup>+x<sup>s</sup>+1 which has an irreducible factor of degree n. For example for
n=211, x<sup>214</sup>+x<sup>103</sup>+1 works. I tried this with QuotientRing, but it is much slower:

```
R.<x> = PolynomialRing(GF(2),x)
T.<x> = QuotientRing(R, x^214 + x^103 + 1)

def bar(n):
   f = x
   for i in range(n):
      f = f^2
   return f
sage: %timeit bar(10000)
10 loops, best of 3: 191 ms per loop
```



---

Comment by mpatel created at 2010-02-11 14:51:20

Resolution: fixed


---

Comment by mpatel created at 2010-02-11 14:51:20

Please remember to update the relevant ticket fields --- the release
managers use an automated script to generate lists of merged tickets.
