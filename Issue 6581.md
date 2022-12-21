# Issue 6581: Groebner basis not working over symbolic ring

Issue created by migration from Trac.

Original creator: rhinton

Original creation time: 2009-07-21 17:11:12

Assignee: tbd

CC:  wstein malb

I'm not sure if this is a problem in the multivariate polynomials (which seem to raise the actual error) or somewhere in the symbolics.

sage: R2.<a,b> = SR[]
sage: I2 = [a*b+a, a*a] * R2
sage: G2 = I2.groebner_basis()
verbose 0 (2247: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation.
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
...
AttributeError: 'MPolynomialRing_polydict' object has no attribute 'monomial_divides'
sage:


---

Comment by AlexGhitza created at 2009-11-15 13:16:51

Changing component from algebra to commutative algebra.


---

Comment by john_perry created at 2012-01-26 20:30:13

The failure is because the polynomials' parent is of type `MPolynomialRing_polydict`, but `MPolynomialRing_polydict_domain` is the type with the necessary methods `monomial_divides`, `monomial_pairwise_prime`, etc.

  * Should a polynomial ring in this case always initialize as `..._domain`?
  * If not, is there an easy option to create the ideal of such a ring? (in this case, at most a documentation change is necessary)
  * If no such method currently exists, what would be the best way to let the user do this?
    a. Have the user create `R2` as above, then call a (new) function that makes it re-initialize as `..._domain`? or
    a. Have a new creation mechanism for such rings, e.g., a symbolic ring `SD` that is a domain, and thus can be initialized as `..._domain`?


---

Comment by malb created at 2012-01-26 20:38:39

I don't think GB computations over SR make sense. How do we compare with zero, e.g., this: `cos(x)^2 *X + sin(x)^2 * X - X`. How do we decide divisibility, e.g. is "cos(x)" zero?


---

Comment by john_perry created at 2012-01-26 21:21:59

I've had situations where you can still compute a Groebner basis with some indeterminate coefficients. It's annoying to have to do all the work by hand, though. I can see implementing this with a warning that it may not make sense.


---

Comment by malb created at 2012-01-26 22:34:16

If you only want symbolic variables, wouldn't this work:


```
sage: P.<a,b,c> = QQ[]
sage: K = Frac(P)
sage: P.<x,y> = PolynomialRing(K)
sage: P
Multivariate Polynomial Ring in x, y over Fraction Field of Multivariate Polynomial Ring in a, b, c over Rational Field
```


This gets mapped to a Singular ring with parameters, i.e., to this one:


```
> ring r = (0,a,b,c),(x,y,z),dp;
> r;
//   characteristic : 0
//   3 parameter    : a b c 
//   minpoly        : 0
//   number of vars : 3
//        block   1 : ordering dp
//                  : names    x y z
//        block   2 : ordering C
```


So, this works:


```
sage: singular(P)
//   characteristic : 0
//   3 parameter    : a b c 
//   minpoly        : 0
//   number of vars : 2
//        block   1 : ordering dp
//                  : names    x y
//        block   2 : ordering C
sage: I = Ideal([P.random_element(), P.random_element()])
sage: %time gb = I.groebner_basis()
```


but it's slow.


---

Comment by malb created at 2012-01-26 22:36:44

Here's a smaller example:

```
sage: P.<a> = QQ[]               
sage: K = Frac(P)
sage: P.<x,y,z> = PolynomialRing(K)
sage: I = Ideal([P.random_element(), P.random_element(), P.random_element()])
sage: I
Ideal (((a^2 - 3/4*a - 1)/(a^2 + a))*y*z + ((2/3*a^2 - 5/3*a - 1)/(-9*a^2 + 5/6*a - 9/2))*z^2 + ((3/2*a^2 - a - 5/2)/(-1/20*a - 5/57))*x + ((2/3*a^2 - a - 1)/(-1/2*a^2 + 5*a + 7/4))*y + (7/3*a^2 - 5*a - 1)/(1/3*a^2 - 1/3*a + 3), ((1/2*a^2 - a - 1/2)/(-a^2 + 7))*x*y + ((-5/6*a^2 + 3*a - 1)/(-a^2 + 2/3*a - 1/4))*x*z + ((a^2 + 3/5*a + 1)/(-6*a^2 - a + 95))*y*z + ((-3*a^2 + 21/2)/(-a^2 - 1/5*a - 1))*z^2 + ((-1/3*a - 1/2)/(-1/3*a^2 - 1/8*a - 3))*z, ((a^2 + a)/(-3/2*a^2 - 1/3*a - 1))*x*y + 1/2*a*y^2 + ((1/31*a^2 - 1/8)/(-4*a^2 + 1/5*a - 2/3))*x*z + ((a^2 - a)/(a^2 - 1/20*a - 1/2))*z^2 + (-1/15*a^2 + 1/315*a + 7/15)*y) of Multivariate Polynomial Ring in x, y, z over Fraction Field of Univariate Polynomial Ring in a over Rational Field
sage: %time gb = I.groebner_basis()
CPU times: user 0.08 s, sys: 0.02 s, total: 0.09 s
Wall time: 0.33 s
sage: gb[-1]
y*z + ((-5472*a^4 + 8208*a^3 + 21888*a^2 + 8208*a)/(73872*a^4 - 62244*a^3 - 31806*a^2 - 20862*a - 36936))*z^2 + ((-2216160*a^4 - 738720*a^3 + 5171040*a^2 + 3693600*a)/(73872*a^3 + 74196*a^2 - 171072*a - 129600))*x + ((-98496*a^4 + 49248*a^3 + 295488*a^2 + 147744*a)/(73872*a^4 - 794124*a^3 + 221616*a^2 + 932634*a + 258552))*y + (517104*a^4 - 590976*a^3 - 1329696*a^2 - 221616*a)/(73872*a^4 - 129276*a^3 + 646380*a^2 - 424764*a - 664848)
```



---

Comment by john_perry created at 2012-01-26 23:11:12

Would this work when we place some assumptions on the variables; e.g., `a<sup>2+b</sup>2==1`? That was my particular situations, and I was under the impression that doing it in the way you suggest won't work for that.


---

Comment by john_perry created at 2012-01-26 23:16:17

(Sorry, I meant assumptions on the coefficients.)


---

Comment by malb created at 2012-01-26 23:45:32

This might be naive, but can't you add `a<sup>2+b</sup>2 - 1` to your ideal?


---

Comment by john_perry created at 2012-01-27 00:22:25

Replying to [comment:9 malb]:
> This might be naive, but can't you add `a<sup>2+b</sup>2 - 1` to your ideal?

Doesn't that change the ideal? These are elements of the base ring.


---

Comment by john_perry created at 2012-01-27 01:34:53

Hey, I got it to work.

```
sage: R.<a,b> = QQ[]
sage: I = R.ideal(a^2+b^2-1)
sage: R2 = QuotientRing(R,I)
sage: K = Frac(R2)
sage: P.<x,y,z> = K[]
sage: f = (a^2+b^2)*x + 1
sage: g = x + 1
sage: f - g
0
```

Sorry -- I'm a bit slow sometimes. :-)

Okay, so we should mark this as "invalid/wontfix" or something like that? Or do we wait to see if the original reporter has a scenario in mind that really does require `SR`?


---

Comment by malb created at 2012-01-27 08:28:24

Unfortunately, your construction bombs out when we try to construct an actual ideal:


```
sage: R.<a,b> = QQ[]
sage: I = R.ideal(a^2+b^2-1)
sage: R2 = QuotientRing(R,I)
sage: K = Frac(R2)
sage: P.<x,y,z> = K[]
sage: f = (a^2+b^2)*x + 1
sage: g = x + 1
sage: f - g
0
sage: Ideal([f,g])
NotImplementedError
```



---

Comment by john_perry created at 2012-01-27 16:01:04

It works (initially) if you do this:

```
sage: J = P.ideal([f,g])
```

...but then you can't do anything with `J`. The characteristic isn't set in `R2`. Curiously, I can still work with ideals in `R2`.

Likewise,

```
sage: Z7 = QuotientRing(ZZ,7*ZZ)
sage: Z7.characteristic()
...
NotImplementedError:
```

Wow. We should probably look at that one day. `;-)`

Anyway, do you know offhand why one needs the characteristic, but not the other?


---

Comment by malb created at 2012-01-27 17:11:38

Nope, unfortunately, I don't.


---

Comment by john_perry created at 2012-01-28 05:31:47

> Anyway, do you know offhand why one needs the characteristic, but not the other?

Bingo. In lines 302--307 of `multi_polynomial_sequence.py` we encounter:

```
    if k.characteristic() != 2:
        return PolynomialSequence_generic(parts, ring, immutable=immutable, cr=cr, cr_str=cr_str)
    elif k.degree() == 1:
        return PolynomialSequence_gf2(parts, ring, immutable=immutable, cr=cr, cr_str=cr_str)
    elif k.degree() > 1:
        return PolynomialSequence_gf2e(parts, ring, immutable=immutable, cr=cr, cr_str=cr_str)
```

I can make this work via judicious use of a `try`/`catch`. I found some other instances where it tried to compute a Singular representation of itself (the `reduce` function in `multi_polynomial_element`, for instance). That has allowed me to compute several Gröbner bases successfully, including one similar to the ideal you couldn't get to work:

```
sage: J = R2.ideal([(a^2+b^2)*x + y, x+y])
sage: J
Ideal (x + y, x + y) of Multivariate Polynomial Ring in x, y over Fraction Field of
Quotient of Multivariate Polynomial Ring in a, b over Rational Field by the ideal
(a^2 + b^2 - 1)
sage: J.groebner_basis()
verbose 0 (2854: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to
very slow toy implementation.
[x + y]
```

I think the patch is worth adding. However, I'm still not sure this is what the original requester wanted. Should I open a new ticket?


---

Comment by john_perry created at 2012-02-02 01:37:55

Changing status from new to needs_review.


---

Comment by john_perry created at 2012-02-02 01:37:55

I decided to upload the patch here. I didn't think a doctest was appropriate, but I can add one if desired.


---

Comment by john_perry created at 2012-02-02 01:49:08

Whoops -- the patch introduces doctest failures. I'll look into them.


---

Comment by john_perry created at 2012-02-02 01:49:08

Changing status from needs_review to needs_work.


---

Comment by john_perry created at 2012-02-02 02:03:45

Okay, that was pretty dumb. Fixed now. Added a doctest while I was at it.


---

Comment by john_perry created at 2012-02-02 02:03:45

Changing status from needs_work to needs_review.


---

Comment by malb created at 2012-02-02 10:16:26

Changing status from needs_review to positive_review.


---

Comment by malb created at 2012-02-02 10:16:26

Looks good.


---

Comment by jdemeyer created at 2012-02-05 11:25:29

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-02-05 11:25:29

You should replace the line number in

```
verbose 0 (2854: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation
```

by "..." because the line number will change all the time.


---

Comment by john_perry created at 2012-02-07 17:20:56

Changing status from needs_work to needs_review.


---

Comment by john_perry created at 2012-02-07 17:20:56

Sorry, I should have thought of that myself.

I remembered this time to check the box to replace the file of the same name, so I've changed the directions (& link) on which patch to apply.


---

Comment by jdemeyer created at 2012-02-07 21:53:21

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-02-11 00:29:13

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-02-11 00:29:13

Please write a proper commit message for your patch, use `hg qrefresh -e` for this.


---

Attachment


---

Comment by john_perry created at 2012-02-11 15:24:27

Changing status from needs_work to needs_review.


---

Comment by john_perry created at 2012-02-11 15:24:27

I should have thought of that, too. Sorry again...


---

Comment by jdemeyer created at 2012-02-11 23:58:25

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-02-14 14:19:32

Resolution: fixed
