# Issue 5346: Sage 3.3: schemes/elliptic_curves/ell_rational_field.py fails to doctest with optional database installed

Issue created by migration from https://trac.sagemath.org/ticket/5346

Original creator: mabshoff

Original creation time: 2009-02-23 07:34:07

Assignee: was

CC:  cremona

Reported by Jan Groenewald in http://groups.google.com/group/sage-devel/browse_thread/thread/d5db5c25fbce1e99

```
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/usr/local/src/sage-3.3/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py", line 2675:
    sage: E.cremona_label()
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: Cremona label not known for Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field.
Got:
    '10351a1'
**********************************************************************
```



---

Comment by mabshoff created at 2009-02-23 08:19:16

This problem is ironically introduced by having database_cremona_ellcurve-20071019.spkg installed :)

Cheers,

Michael


---

Comment by GeorgSWeber created at 2009-03-26 23:05:25

For the record:

The optional database covers conductor ranges from 10000 to 130000 AFAIK. So an obviously working patch (to be tested ...) already discussed elsewhere (I don't remember exactly who had this idea first, it wasn't me) would be to exchange the curve with conductor 10351 in the doctest, with a curve having conductor bigger than 130000.

Cheers,
gsw


---

Comment by cremona created at 2009-03-27 08:11:00

Replying to [comment:2 GeorgSWeber]:
> For the record:
> 
> The optional database covers conductor ranges from 10000 to 130000 AFAIK. So an obviously working patch (to be tested ...) already discussed elsewhere (I don't remember exactly who had this idea first, it wasn't me) would be to exchange the curve with conductor 10351 in the doctest, with a curve having conductor bigger than 130000.

I agree, and suggest

```
sage: E = EllipticCurve([1, -1, 0, -79, 289]) 
sage: E.cremona_label()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/john/.sage/temp/ubuntu/1126/_home_john__sage_init_sage_0.py in <module>()

/home/john/sage-3.4/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in cremona_label(self, space)
   3034                 X = self.database_curve()
   3035             except RuntimeError:
-> 3036                 raise RuntimeError, "Cremona label not known for %s."%self
   3037             self.__cremona_label = X.__cremona_label
   3038             return self.cremona_label(space)

RuntimeError: Cremona label not known for Elliptic Curve defined by y^2 + x*y = x^3 - x^2 - 79*x + 289 over Rational Field.
```

as that curve will one day have label 234446a1 (or b1 or c1, I forget).


> 
> Cheers,
> gsw


---

Comment by cremona created at 2009-04-23 09:19:22

Apply to 3.4.1


---

Attachment

The patch cahnges taht example to the one with condictor 234446 as I suggested.

It also make another doctest work ok with & without the database (at line 4941) by hard-wiring in some points instead of getting the gens.

I tested this on sage-3.4.1 with & without the database installed.


---

Comment by mabshoff created at 2009-04-24 08:26:50

Thanks for taking care of this John. Doctests pass, pass reads good and fixes the problem. Positve review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 08:27:50

Resolution: fixed


---

Comment by mabshoff created at 2009-04-24 08:27:50

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael
