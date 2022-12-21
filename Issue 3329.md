# Issue 3329: attempting to convert relative number field elements to Singular should fail quickly

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-05-29 17:32:53

Assignee: was

Consider this example:

```
  R.<a,b> = NumberField(x^2-3,'g').extension(x^2-7,'h')[]
  h = R.base_ring().gen()    
  S.<y> = R.fraction_field()[]
  xgcd(y^2, a*h*y+b) 
```

(reported by Gaëtan Bisson here: http://groups.google.com/group/sage-support/browse_thread/thread/5338608bd7508b00/cd1d6555592e472f#cd1d6555592e472f)

This fails because it tries to use Singular to take the gcd of multivariate polynomials over a relative number field, and Singular does not support relative number fields.  However, the error message is quite poor; it would be better if it failed with a better error message.


---

Comment by cwitty created at 2008-05-29 17:39:13

See also #3330, which is about the exact same test case, but requests a working implementation of GCD (rather than just a better error message).


---

Comment by malb created at 2008-08-18 14:00:28

This fails before Singular:

```
TypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in y over Fraction Field of Multivariate Polynomial Ring in a, b over Number Field in h with defining polynomial x^2 - 7 over its base field' and 'Multivariate Polynomial Ring in a, b over Number Field in h with defining polynomial x^2 - 7 over its base field'
```



---

Comment by malb created at 2009-01-23 07:21:08

This seems to work now because we avoid Singular


```
sage: R.<a,b> = NumberField(x^2-3,'g').extension(x^2-7,'h')[]
sage: h = R.base_ring().gen()
sage: S.<y> = R.fraction_field()[]
sage: xgcd(y^2, a*h*y+b)
(49*a^4*b^2/(343*a^6), 1, ((-1)/(h*a))*y + 49*a^4*b/(343*a^6))
```


Carl, any thoughts on this?


---

Comment by malb created at 2009-01-25 19:02:57

Changing assignee from was to malb.


---

Comment by malb created at 2009-01-25 19:02:57

Changing status from new to assigned.


---

Comment by was created at 2010-01-18 13:08:29

Since Carl's not involved any more, and this now works fine (in sage-4.3.1.rc0 too), I'm closing this as fixed:


```
bash$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage:   R.<a,b> = NumberField(x^2-3,'g').extension(x^2-7,'h')[]
sage:   h = R.base_ring().gen()
sage:   S.<y> = R.fraction_field()[]
sage:   xgcd(y^2, a*h*y+b)
(7*a^2*b^2/(7*a^2*b^2), 7*a^2/b^2, (((-7)*a^2)/(h*a*b^2))*y + 7*a^2*b/(7*a^2*b^2))
```



---

Comment by was created at 2010-01-18 13:08:29

Resolution: fixed
