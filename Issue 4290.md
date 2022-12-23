# Issue 4290: stopgap function to turn plane curves of genus one into elliptic curves

Issue created by migration from https://trac.sagemath.org/ticket/4290

Original creator: ljpk

Original creation time: 2008-10-14 22:39:08

Assignee: was

This is a function to turn plane curves of genus 1 with a known point into objects of type EllipticCurve. It relies on MAGMA (as does EllipticCurve_from_cubic) but will add a little functionality. Here is an example of how it works:


```
sage: x,y,z=MPolynomialRing(QQ,Integer(3),'xyz').gens() # optional
sage: C=Curve(x^4+x^2*y^2-z^4) 
sage: P=C(1,0,1) 
sage: E=EllipticCurve_from_plane_curve(C,P) 
sage: E 
Elliptic Curve defined by y^2  = x^3 + 4*x over Rational Field
```




---

Attachment

implementation of EllipticCurve_from_plane_curve


---

Comment by ljpk created at 2008-10-14 22:41:17

Changing assignee from was to craigcitro.


---

Comment by cremona created at 2008-11-04 17:41:15

The "patch" isn't a patch, it's just a function defined in Sage. Secondly, there is already a function that does almost the same as this in sage/schemes/elliptic_curves/constructor.py .

So what needs to be done (Lloyd!) is to (1) Explain briefly how this function differs from the existing one, and why it is better, and also (2) actually make a patch.

If Lloyd convinces me of  (1) then I'll happily do (2).


---

Comment by ljpk created at 2008-11-24 11:20:17

The current Sage function only converts cubics into elliptic curves, but MAGMA can do quite a bit more than that. My function can also cope with other genus one curves such as x<sup>4+x</sup>2*y<sup>2-z</sup>4 which is not cubic. Possibly the current function should be tweaked slightly so that it can do both cubic and non-cubic examples.


---

Comment by mabshoff created at 2009-04-06 06:01:13

Anything going on with this patch? It has been sitting around for 4 months :(.

Cheers,

Michael


---

Comment by cremona created at 2009-04-06 10:07:38

Patch based on the above, based on 3.4.1.rc0


---

Attachment

I have made a proper patch based on Lloyd's function (based on 3.4.1.rc0), which also fixes his function so that it works when the variable names are something other than 'x','y','z' (which it did not before).

You might think that this function makes the existing EllipicCurve_from_cubic redundant;  it nearly does, but that function takes a homogeneous polynomial while this one takes an actual curve.  It would probably be better to combine these when all this is rewritten in Sage.

I added the new function to all.py so that it is in the global namespace.  I am not sure what the convention is here, given that it is an optional-only function requiring magma!  Also I have nto tested my patch o na machine without magma since I don't have one handy :)


---

Comment by was created at 2009-04-12 02:56:02

The doctests should be marked:

```
   # optional - magma
```

so when one does

```
  sage -t -only_optional=magma
```

they get run.


---

Comment by cremona created at 2009-06-11 20:37:44

Replaces previous; rebased to 4.0.1


---

Attachment

The new patch replaces previous ones.  It marks the doctests as William asked;  testing then revealed bugs which have been fixed.  Also rebased to 4.0.1 and the docstrings properly ReSTified to the reference manual page looks good.


---

Comment by ncalexan created at 2009-06-15 19:34:09

Works well for me.  Pity it requires magma :(


---

Comment by rlm created at 2009-06-24 10:04:23

Resolution: fixed
