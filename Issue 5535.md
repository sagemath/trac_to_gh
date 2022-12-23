# Issue 5535: is_primitive is computes integer prime factorization on every call

Issue created by migration from https://trac.sagemath.org/ticket/5535

Original creator: rhinton

Original creation time: 2009-03-16 21:04:31

Assignee: tbd

CC:  malb cremona

The current (generic) code for is_primitive in rings/polynomial/polynomial_element.pyx is

```
        if not self.is_irreducible():
            return False
        p = self.parent().characteristic()
        n = p ** self.degree() - 1
        y = self.parent().quo(self).gen()
        for d in n.prime_divisors():
            if ( y ** (n//d) ) == 1:
                return False
        return True
```

Note that the integer n and its prime divisors are calculated as part of the algorithm.  This calculation can be lengthy for large n, and can dominate the running time of the algorithm.

The proposed patch adds optional arguments to is_primitive to provide the results of these calculations -- useful for is_primitive tests for multiple polynomials of the same degree.


---

Comment by malb created at 2009-03-16 21:40:26

I think the `(default: None)` is supposed to be at the end of the overall description. If you know better I am happy to be convinced otherwise though. 

It might be a good idea to ask somebody else how they feel about this patch because we introduce a neat way to shoot oneself in the foot.

btw. when you add a patch you should add `[with patch, needs review]` to the title of the ticket.


---

Comment by cwitty created at 2009-03-16 23:42:26

I'm fine with the shoot-yourself-in-the-foot part of the patch... it seems sufficiently well documented.


---

Comment by cwitty created at 2009-03-17 00:41:25

BTW, I do agree with John Cremona's comment that for polynomials over a ring, "primitive" means something totally different, and something should be done to try to keep people from thinking that this tests for that kind of primitive (preferably more than just documentation).


---

Comment by malb created at 2009-03-17 12:16:19

Ryan, do you want to add some docs while you're on it to address John's complaint?


---

Comment by rhinton created at 2009-03-18 17:24:32

I added some verbiage to the is_primitive docstring to indicate that it's only useful for finite fields, and referenced the new trac #5561 for resolving its proper placement.  Is this sufficient for a positive review?


---

Comment by cremona created at 2009-03-18 20:37:37

This looks ok to me, though I think you could delete the second paragraph of the docstring (it's a bit too detailed).

For the code itself one could also use the (generic) order_from_multiple() function like this:

```
return order_from_multiple(y,n,n_prime_divs,operation='*')==n
```

since the order_from_multiple() function (which I wrote) already takes the list of prime divisors of n as a parameter, computing it if it is not given.  I just tried that on a poly of degree 257 over GF(2) and it worked fine (I was impressed at Sage's ability to factor the 78-digit number `2^257-1`!).  It does do a little more work though as it finds the exact order.

There seems to be quite a large literature on finding primitive polynomials which may include better tests of primitivity.  I'll take a look at some of those when I'm back at work.


---

Comment by cremona created at 2009-03-19 10:38:46

One more comment:  NTL has efficient routines for modular exponentiation modulo polynomials over GF(p) which could be used to find the order of X modulo f(X) and hence test primitivity of f:  see http://www.shoup.net/ntl/doc/ZZ_pX.txt.  This would entirely independent of the improvement implemented in this patch, of course.


---

Comment by cremona created at 2009-03-21 19:00:10

I'll give this a positive review if two things are changed: (1) replace n = p ** self.degree() - 1 by n = q ** self.degree() - 1 where q = self.base_ring().order(), which is the same as at present for polynomials defined over prime fields, but now gives a correct answer for polynomials defined over non-prime finite fields; (2) put in tests for k=self.base_ring() that k.is_field() and k.is_finite(), perhaps raising a NotImplementedError, since otherwise the result is rather random:

```
sage: x=polygen(ZZ)
sage: f=x^2+1
sage: f.is_primitive()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/john/.sage/temp/ubuntu/24798/_home_john__sage_init_sage_0.py in <module>()

/home/john/sage-3.4/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.is_primitive (sage/rings/polynomial/polynomial_element.c:19782)()

AttributeError: 'int' object has no attribute 'prime_divisors'
```



---

Attachment


---

Comment by rhinton created at 2009-03-23 15:07:02

Thanks for the excellent suggestions.  I replaced most of the existing code with `order_with_multiple`.  A quick timing test (primitive degree 128 polynomial over GF(2)) showed a slight improvement with the change (603 ms per loop instead of 740 ms per loop).  I also switched from characteristic to base ring order and put a sanity check to make sure `self` is a polynomial over a field.

Let me know if I can fix anything else.  When this patch receives a positive review, I plan to implement cremona's suggestion for #5561 by replacing the sanity check with the proper ring-theoretic primitivity check (since he came up with a 3-line solution to the problem :-).


---

Attachment


---

Comment by cremona created at 2009-03-23 17:04:35

Positive review!  I have made some cosmetic changes, only to the docstring and NotImplemented message, and added some more relevant tests.

The second patch replaces the first, and (also) applies to 3.4.


---

Comment by mabshoff created at 2009-03-23 20:18:03

Merged trac_5535_is_primitive_avoid_duplicate_factorizations.2.patch in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-23 20:18:03

Resolution: fixed


---

Comment by mvngu created at 2009-03-24 01:34:43

Replying to [comment:9 rhinton]:
> Thanks for the excellent suggestions.  I replaced most of the existing code with `order_with_multiple`.  A quick timing test (primitive degree 128 polynomial over GF(2)) showed a slight improvement with the change (603 ms per loop instead of 740 ms per loop).


Is it possible for you to give some system/architecture information of the machine you used to obtain the above timing statistics? It would also be good to include the actual code that produces those timing improvements. What I'm looking for are a "before" and an "after" sections to clearly show the timing improvements in your patch.


---

Comment by rhinton created at 2009-03-24 02:56:19

For future reference, I am running a Pentium 4, 2.4 GHz with 2 GB of RAM.  Here is some sample code I used to measure the performance difference on my system.

```
  R.<x> = PolynomialRing(GF(2), 'x')

  # degree 128
  nn = 128
  max_order = 2^nn - 1
  pdivs = max_order.prime_divisors()

  # find a primitive poly
  print "Finding a primitive polynomial of degree "+str(nn)+" for timing test."
  poly = R.random_element(nn)
  while not (poly.degree()==nn and poly.is_primitive(max_order, pdivs)):
    poly = R.random_element(nn)

  timeit('max_order.prime_divisors()')
  # 25 loops, best of 3: 20.9 ms per loop
  timeit('poly.is_primitive(max_order, pdivs)')
  # 5 loops, best of 3: 1 s per loop
  timeit('poly.is_primitive()')
  # 5 loops, best of 3: 1.03 s per loop

  # degree 256
  nn = 256
  max_order = 2^nn - 1
  pdivs = max_order.prime_divisors()

  # find a primitive poly
  print "Finding a primitive polynomial of degree "+str(nn)+" for timing test."
  poly = R.random_element(nn)
  while not (poly.degree()==nn and poly.is_primitive(max_order, pdivs)):
    poly = R.random_element(nn)

  timeit('max_order.prime_divisors()')  # this takes a long time
  # 5 loops, best of 3: 9.3 s per loop
  timeit('poly.is_primitive(max_order, pdivs)')
  # 5 loops, best of 3: 2.67 s per loop
  timeit('poly.is_primitive()')  # this takes a longer time
  # 5 loops, best of 3: 11.5 s per loop
```

The actual speedup, of course, depends on how many times you're calling is_primitive for the same degree (if you have to call prime_divisors() for each degree) and the actual degrees.  Typically speedups will be greater for higher degrees.
