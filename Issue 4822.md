# Issue 4822: Tweak to the error message for EllipticCurve

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2008-12-17 23:47:58

Assignee: was

I was using SAGE with the small version of the CremonaDatabase, and tried the following, which does not work because the conductor is too high:

```
EllipticCurve("10001a1")
```


I think it would be useful if the error message not only said "this curve is not in the database" (which is indeed true) but also checked to see if one was using the small database of curves, and if so told the user how to access the larger version
using the incantation

```
!sage -i database_cremona_ellcurve-2005.11.03
```

or otherwise.


---

Comment by rlm created at 2009-01-23 02:55:07

Changing type from defect to enhancement.


---

Comment by davidloeffler created at 2009-07-20 19:49:16

Changing component from number theory to elliptic curves.


---

Comment by davidloeffler created at 2009-07-20 19:49:16

Changing assignee from was to davidloeffler.


---

Attachment

Applies to 4.1.1


---

Comment by cremona created at 2009-08-15 15:13:34

Apply after previous


---

Attachment

The patch deals with this in a more intelligent way.  I did not add doctests since it's hard to do that when the output message depends on whether or not the extra database is installed.  But I did test it before and after installing the optional database.  The message suggests installing the optional database iff the desired conductor is  betweem 10000 and 13000 and the optional db is not already installed;  I did not actually include the command-line to install it though.

The second patch fixes a doctest which otherwise fails when run after installing the optional database (but is otherwise independent of this ticket, except that I wrote it so was my fault anyway!)


---

Comment by wuthrich created at 2009-08-17 15:37:00

The patch is ok (so far only tested without the optional package). I will test it with it later today.

Maybe while we are at it I could suggest that the same change is done to `cremona_label()`.
This is without the optional package:


```
sage: E= EllipticCurve([3,10])
sage: E.cremona_label()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/chrigu/.sage/temp/linux_ljo8/12909/_home_chrigu__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in cremona_label(self, space)
   3305                 X = self.database_curve()
   3306             except RuntimeError:
-> 3307                 raise RuntimeError, "Cremona label not known for %s."%self
   3308             self.__cremona_label = X.__cremona_label
   3309             return self.cremona_label(space)

RuntimeError: Cremona label not known for Elliptic Curve defined by y^2 = x^3 + 3*x + 10 over Rational Field.
sage: E.conductor()
44928
```


Chris.

ps : 'I don't know if there is an official 'under review'.


---

Comment by wuthrich created at 2009-08-17 16:38:41

This patch also works with the optional package. I give this ticket a positive review and I agree that the command-line to install the optional package should better not be included. It is very clear what to do as it is now.

 The second [independent] patch obtains also a positive review with this.

 I propose to address the issue that I raised on `cremona_label()` in a new ticket.

 Chris.


---

Comment by mvngu created at 2009-08-25 03:54:05

Merged both patches.


---

Comment by mvngu created at 2009-08-25 03:54:05

Resolution: fixed
