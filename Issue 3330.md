# Issue 3330: multivariate polynomial GCD should work over more base rings

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-05-29 17:37:52

Assignee: malb

CC:  gaetan.bisson@loria.fr

Consider this example:

```
  R.<a,b> = NumberField(x^2-3,'g').extension(x^2-7,'h')[]
  h = R.base_ring().gen()    
  S.<y> = R.fraction_field()[]
  xgcd(y^2, a*h*y+b) 
```

(reported by Gaëtan Bisson here: http://groups.google.com/group/sage-support/browse_thread/thread/5338608bd7508b00/cd1d6555592e472f#cd1d6555592e472f)

This fails because Sage attempts to find the GCD of multivariate polynomials over a relative number field using Singular, and Singular does not support relative number fields.  This should be implemented in Sage (probably by converting the relative number field into an absolute field, performing the computation, and converting back).

See also #3329, which is about the exact same test case, but requests only a better error message.


---

Comment by malb created at 2009-01-23 07:23:04

It does something now:


```
sage: R.<a,b> = NumberField(x^2-3,'g').extension(x^2-7,'h')[]
sage: h = R.base_ring().gen()
sage: S.<y> = R.fraction_field()[]
sage: xgcd(y^2, a*h*y+b)
(49*a^4*b^2/(343*a^6), 1, ((-1)/(h*a))*y + 49*a^4*b/(343*a^6))
```



---

Comment by AlexGhitza created at 2009-03-16 09:38:10

And now:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<a,b> = NumberField(x^2-3,'g').extension(x^2-7,'h')[]
sage: h = R.base_ring().gen()    
sage: S.<y> = R.fraction_field()[]
sage: xgcd(y^2, a*h*y+b)
(b^2/(7*a^2), 1, ((-1)/(h*a))*y + b/(7*a^2))
```

| Sage Version 3.4, Release Date: 2009-03-11                         |
| Type notebook() for the GUI, and license() for information.        |
This actually looks correct to me.  I'm cc-ing the original poster so he can comment on it.


---

Comment by bisson created at 2009-04-01 08:10:55

Replying to [comment:2 AlexGhitza]:
> This actually looks correct to me.  I'm cc-ing the original poster so he can comment on it.

Thanks for letting me know this issue has been fixed, and many thanks to the people who fixed it.

Something a little bit weird happens if I try to verify Sage's output:

```
sage: R.<a,b> = NumberField(x^2-3,'g').extension(x^2-7,'h')[]
sage: h = R.base_ring().gen()
sage: S.<y> = R.fraction_field()[]
sage: xgcd(y^2, a*h*y+b)
(b^2/(7*a^2), 1, ((-1)/(h*a))*y + b/(7*a^2))

sage: y^2+(((-1)/(h*a))*y + b/(7*a^2))*(a*h*y+b)
h*a*b^2/(7*h*a^3)
```

As you see, the output is not simplified as b<sup>2</sup>/(7a<sup>2</sup>); is there a reason for that?

I am not opening a new ticket because I would like to have your opinion on whether it really is a bug or not before possibly doing so.


---

Comment by tmonteil created at 2018-10-28 13:47:29

It seems indeed to work perfectly well now, so let us add a doctest to prevent its comeback.

By the way, replying to [comment:3 bisson]:
> {{{
> sage: y^2+(((-1)/(h*a))*y + b/(7*a^2))*(a*h*y+b)
> h*a*b<sup>2/(7*h*a</sup>3)
> }}}
> As you see, the output is not simplified as b<sup>2</sup>/(7a<sup>2</sup>); is there a reason for that?

Note that we now have:


```
sage: y^2+(((-1)/(h*a))*y + b/(7*a^2))*(a*h*y+b)
b^2/(7*a^2)
```


as expected.
----
New commits:


---

Comment by tmonteil created at 2018-10-28 13:47:29

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2018-10-29 18:05:59

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2018-10-30 22:37:38

Resolution: fixed
