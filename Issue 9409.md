# Issue 9409: Bug in elliptic curves method .count_points() over finite fields

Issue created by migration from Trac.

Original creator: adam

Original creation time: 2010-07-02 16:23:51

Assignee: cremona

Keywords: Elliptic Curves .count_points()

There is some bug in the method .count_points() which belongs to elliptic curves defined over finite fields. This might be specific to EC defined over number fields - I only get this error when I take an EC over a number field, reduce at a good prime and then count points. In fact, I get the correct answer the first time, but if I define a second EC over a possibly different number field and count points at a good reduction, then the method .count_points() fails. I suspect this has to do with the cacheing...

If you want to reproduce the behavior, try the following code:


### this just runs through the method outlined above:

def test(curve, bound):
    for i in primes(bound):
        print "Checking primes over %d:        "%i
        factors = curve.base_field().ideal(i).factor()
        for j in range(len(factors)):
            if  curve.has_good_reduction(factors[j][0]):
                if factors[j][0].divides(curve.discriminant()):
                    print "Curve has good reduction, but this isn't not a minimal model",
                    print "at %s with %d points in the reduced curve"%(factors[j][0], curve.local_minimal_model(factors[j][0]).reduction(factors[j][0]).count_points() )
                else:                 
                    print "Curve has good reduction and is a minimal model"
                    print "at %s with %d points in the reduced curve"%(factors[j][0],  curve.reduction(factors[j][0]).count_points() )
            else:
                print "Curve has bad reduction over %s"%factors[j][0]
    return


### sample 1
K.<t> = NumberField(x^2 + 1); E = EllipticCurve(K, [0, 1, 0, -2*t - 2, 2*t]); E
### sample 2
L.<u> = NumberField(x^2 - 2); F = EllipticCurve(L, [0,2,0, 2*u +4, 2*u + 3]); F

test(E, 100)

## now the error will happen
test(F, 100)


---

Comment by cremona created at 2010-07-05 16:51:10

You do not actually say what the error is -- can you paste in the relevant part of the output?

This is one of a number of tickets which claim to be about elliptic curves but are almost certainly about the caching of finite fields (as you suggest).  the trouble is that because of this, elliptic curves people (like me) look at the ticket and do nothing, while the finite fields people who need to fix code do not look at it!


---

Comment by adam created at 2010-07-05 19:08:05

Changing keywords from "Elliptic Curves .count_points()" to "Elliptic Curves .count_points() finite fields".


---

Comment by cremona created at 2010-08-14 16:49:42

This should be tested after #9315 is in as that may well fix it.


---

Attachment

Test script


---

Comment by cremona created at 2010-08-14 17:21:07

Replying to [comment:4 cremona]:
> This should be tested after #9315 is in as that may well fix it.

Unfortunately not.  After loading the attached script, running either testE() or testF() in a fresh Sage (so no cached fields) works fine, but then running the other one fails (at p=59).


---

Comment by cremona created at 2010-10-03 16:32:03

This now seems to work fine (both functions testE() and testF() in the test script now run without errors) in 4.6.alpha2 (not alpha1!).

If the reviewer agrees, this can be set to fixed and the closed.


---

Comment by cremona created at 2010-10-03 16:32:03

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-10-03 16:40:32

(Editing description because the entire ticket webpage appears stuck in a rogue `<sup>` tag!)


---

Comment by davidloeffler created at 2010-10-03 16:44:58

Looks fine to me. I'm flagging this as positive review so the release manager can close it as fixed.


---

Comment by davidloeffler created at 2010-10-03 16:44:58

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-10-04 01:28:54

Resolution: worksforme
