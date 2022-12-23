# Issue 5746: rational points over subfields of the (finite) field of definition

Issue created by migration from https://trac.sagemath.org/ticket/5746

Original creator: AlexGhitza

Original creation time: 2009-04-11 05:08:48

Assignee: was

Keywords: rational points finite field

Right now, if X is a scheme over a finite field F and we ask for the list of rational points over a subfield K of F, Sage raises an error because it tries to base change X to K first.

It would be very easy to implement this as follows: take the list of all rational points over F and find the ones that are fixed by the appropriate power of the Frobenius morphism.  These are then the K-rational points.

A sample of what this would return:


```
sage: P = ProjectiveSpace(1, GF(3^2, 'b'))
sage: P.rational_points()
[(0 : 1),
 (2*b : 1),
 (b + 1 : 1),
 (b + 2 : 1),
 (2 : 1),
 (b : 1),
 (2*b + 2 : 1),
 (2*b + 1 : 1),
 (1 : 1),
 (1 : 0)]
sage: P.rational_points(GF(3))  # this doesn't work right now
[(0 : 1),
 (2 : 1),
 (1 : 1),
 (1 : 0)]
```




---

Comment by AlexGhitza created at 2009-05-05 07:40:30

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2009-05-05 07:40:30

Changing status from new to assigned.


---

Comment by bantieau created at 2009-05-21 02:58:13

Is this mathematically correct? In terms of categories of schemes, X/F has no K-points, because K is not in the category of F-schemes.


---

Comment by mderickx created at 2017-09-08 04:52:40

Changing status from new to needs_review.


---

Comment by mderickx created at 2017-09-08 04:52:40

I indeed think this should not be done since this is mathematically incorrect even in the broader category of schemes. 

By definition X has a morphism to spec F since it is an F scheme and if X would have a spec K point then we would get a morphism from spec K to spec F which is not possible since this would give is a field map from F to K.

If X does happen to be the base change of some X' from K to F and a user wants the K rational points of X', then I think it is good to force the user to construct X' explicitly. This is because it is not necessarily unique (sometimes one can twist X') nor does X' need to exist.

I am putting it up for review so it can be closed as won't fix.


---

Comment by pbruin created at 2017-09-08 05:04:31

Changing status from needs_review to positive_review.


---

Comment by pbruin created at 2017-09-08 05:04:31

Asking for points over a subfield of the field of definition is indeed not well defined and trying to implement this would probably only cause confusion.


---

Comment by mderickx created at 2017-09-25 13:05:14

Resolution: wontfix
