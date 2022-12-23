# Issue 4749: improve coercion of points between elliptic curves and reduction of points mod p

Issue created by migration from https://trac.sagemath.org/ticket/4749

Original creator: was

Original creation time: 2008-12-10 01:00:06

Assignee: was

CC:  cswiercz

If I have a point P on an elliptic curve E and F is another curve, then F(P) should work if possible.  It doesn't.   For example:

```
E = EllipticCurve([1,-1,0,94,9]) 
R = E([0,3]) + 5*E([8,31])      # big denom's
E11 = E.change_ring(GF(11))
E11(R) 
 BOOM!
```

But it should clear denominators and coerce in the triple like so:

```
def reduce(R, p):
    x, y = R.xy()
    d = LCM(x.denominator(), y.denominator())
    return R.curve().change_ring(GF(p))([x*d,y*d,d])
```

}}}


---

Comment by cswiercz created at 2008-12-16 05:23:09

Changing keywords from "" to "elliptic curves".


---

Comment by cswiercz created at 2008-12-16 05:23:09

Changing status from new to assigned.


---

Attachment


---

Comment by cswiercz created at 2008-12-16 05:23:09

Changing assignee from was to cswiercz.


---

Comment by was created at 2008-12-16 16:55:13

Change "This functionality is implemented in the \code{__call__} method. " to "This functionality is used in the \code{__call__} method for elliptic curves."


---

Attachment


---

Comment by cremona created at 2008-12-19 17:08:48

I have to give this a negative review.  This code does not treat the case where the point is 0 (i.e. E(0)).  It fails to reduce E(0) since the E.xy() will crash.  In the example, E11(E(0)) works ok since the __call__ function must test the input via is_zero() so that works, but:

```
sage: S = E11._reduce_point(E(0), 11)
---------------------------------------------------------------------------
ZeroDivisionError  
```


Secondly, I don't know why this code is in ell_generic.  It only applies to elliptic curves defined over Q.  I think it belongs in ell_point.py, as a member function of class  EllipticCurvePoint_number_field.

I noticed this patch just when I was working on something almost identical, though my code works over number fields.  So I would like to replace this patch with another, not just to correct the small glitch of E(0), but to make it work over number fields.  In fact, here is a chunk of code I wrote before I saw this patch posted in here with no changes:

```
        if K is rings.QQ:
            pi = P
        else:
            pi = K.uniformizer(P)

        # Make sure the curve is integral and locally minimal at P:
        Emin = E.local_minimal_model(P)
        urst = E.isomorphism_to(Emin)
        Q = urst(self)

        # Scale the homogeneous coordinates of the point to be primitive:
        xyz = list(Q)
        e = min([c.valuation(P) for c in xyz])
        if e !=0:            
            if K is rings.QQ:
                pi = P
            else:
                pi = K.uniformizer(P)
            pie = pi**e
            xyz = [c/pie for c in xyz]
```

This was just to get homogeneous coordinates in which one of x,y,z is a unit mod P, but then you could directly construct a point on the reduction from it.  (I was also concerned with having a non-minimal model at P.) 

I expect that I will post an alternative patch here before long.


---

Attachment


---

Comment by cremona created at 2008-12-19 17:27:02

OK, I relented.  I have added a patch which addresses the specific bug.  There is still a case for something more general, but it is quite hard to see how to get the __call__ function to do the right thing.  There has to be a way of telling in some more generality whether the base field of the point is a residue field of the base field of the curve (I mean that the other way round).  So it's harder than I thought, and its 5.22pm on the last Friday before a holiday, and the patch does do something which is already useful, so let's go for it!


---

Comment by mabshoff created at 2008-12-21 12:37:24

Merged all three patches in Sage 3.2.3.alpha0


---

Comment by mabshoff created at 2008-12-21 12:37:24

Resolution: fixed
