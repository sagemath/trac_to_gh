# Issue 6161: Polynomial rings have no coercion map to themselves

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-05-30 22:13:32

Assignee: malb

Keywords: coercion polynomial

The following happens with the 'official' Sage 4.0 on sage.math and on at least one other x_86_64 machine (built from sources and in addition with the singular-3-1-0-spkg). It also occurs at least with sage 3.4.2.

```
sage: R.<x>=QQ[]
sage: R._has_coerce_map_from(R)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/SimonKing/.sage/temp/sage.math.washington.edu/2444/_home_SimonKing__sage_init_sage_0.py in <module>()

TypeError: 'dict' object is not callable
sage: R.<x,y>=QQ[]
sage: R._has_coerce_map_from(R)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/SimonKing/.sage/temp/sage.math.washington.edu/2444/_home_SimonKing__sage_init_sage_0.py in <module>()

TypeError: 'dict' object is not callable
```


So, both uni- and multivariate polynomial rings do not believe that they have a coercion to themselves. Or: Coercion of polynomial rings is seriously broken. 

I really wonder why this does not break hundreds of doc tests. I hope it is ok to make this a blocker.



---

Comment by mhansen created at 2009-05-31 19:25:02

Resolution: invalid


---

Comment by mhansen created at 2009-05-31 19:25:02

Simon,

You're using _has_coerce_map_from incorrectly.  The error you get is be cause it is actually a dictionary and not an function.  See:


```
sage: R.<x,y> = QQ[]
sage: R.coerce_map_from(R)
Identity endomorphism of Multivariate Polynomial Ring in x, y over Rational Field
sage: R.<x> = QQ[]
sage: R.coerce_map_from(R)
Identity endomorphism of Univariate Polynomial Ring in x over Rational Field
```


I'm going to close this an invalid.  A more appropriate ticket should be opened if there is a failure you're trying to fix.
