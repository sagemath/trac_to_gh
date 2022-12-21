# Issue 8879: Bad indentation in hyperelliptic curve file

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-05-05 00:01:01

Assignee: cremona

CC:  mjo

As of 4.4, there is bad indentation in sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py

```
    def is_in_weierstrass_disc(self,P):
        """
        Checks if $P$ is in a Weierstrass disc

        EXAMPLES:
            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,8)
            sage: HK = H.change_ring(K)
	    sage: P = HK(0,3)
	    sage: HK.is_in_weierstrass_disc(P)
	    False
	    sage: Q = HK(0,1,0)
	    sage: HK.is_in_weierstrass_disc(Q)
	    True
	    sage: S = HK(1,0)
            sage: HK.is_in_weierstrass_disc(S)
            True
	    sage: T = HK.lift_x(1+3*5^2); T
	    (1 + 3*5^2 + O(5^8) : 2*5 + 4*5^3 + 3*5^4 + 5^5 + 3*5^6 + O(5^7) : 1 + O(5^8))
	    sage: HK.is_in_weierstrass_disc(T)
	    True

	AUTHOR:
            - Jennifer Balakrishnan (2010-02)
        """
```

I don't know if it matters that much, but at the very least it's annoying.  It's not elliptic curves, of course, but that's the closest component I could find.


---

Comment by kcrisman created at 2010-05-05 00:04:38

There is also a tab in the following doctest which causes Mac OS X 10.4 to have problems while doctesting, I think.

```
    def residue_disc(self,P):
        """
        Gives the residue disc of $P$
        
        EXAMPLES:
	    sage: R.<x> = QQ['x']	
```

Note that tab character (not visible, but there!) in the last line.


---

Comment by kcrisman created at 2010-05-05 00:28:23

Also, the tests at lines 465 ff. take 12-15 seconds EACH on a pretty new computer.  Shouldn't these be marked # long time?  In general quite a few of the doctests take very long, and there are so many that it seems reasonable that some don't have to be run in a normal make check.

There is a further tab character in line 752:

```
            sage: T = HK(0,1,0)	
```

and line 757

```
            sage: HK.coleman_integral(w*x^3,T,S)	
```



---

Comment by mjo created at 2012-01-16 03:45:59

Changing status from new to needs_review.


---

Comment by mjo created at 2012-01-16 03:45:59

* All tabs were fixed in #8680.
 * The coleman_integral stuff was marked long time in #10712.
 * The bad indentation was fixed somewhere along the line.

I've cleaned up some trailing whitespace, so that there isn't nothing to do here.


---

Attachment

Remove trailing whitespace.


---

Comment by kcrisman created at 2012-02-03 03:29:45

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-02-03 03:29:45

Replying to [comment:3 mjo]:
>  * All tabs were fixed in #8680.
>  * The coleman_integral stuff was marked long time in #10712.
>  * The bad indentation was fixed somewhere along the line.
> 
> I've cleaned up some trailing whitespace, so that there isn't nothing to do here.
Not much to review either.  You could have just positively reviewed this as a duplicate too, you know!  But I suppose someone has to remove trailing whitespace!


---

Comment by mjo created at 2012-02-03 03:37:51

I had already cleaned up the whitespace in the process of investigating the fixed issues, so it felt wrong throw out a perfectly good patch.


---

Comment by kcrisman created at 2012-02-03 15:54:02

Agreed.  Changing the summary, though :)


---

Comment by jdemeyer created at 2012-02-06 21:22:49

Resolution: fixed
