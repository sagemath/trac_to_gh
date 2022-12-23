# Issue 8801: implement the projective dual of a plane curve

Issue created by migration from https://trac.sagemath.org/ticket/8801

Original creator: AlexGhitza

Original creation time: 2010-04-28 14:24:54

Assignee: AlexGhitza

This was requested by Ursula Whitcher on sage-support.  She adds:


```
  I'm playing with a family of plane curves with rational coefficients in 
  the complex projective plane.  So rational or complex numbers would be 
  enough for me to test examples.  In a perfect world I'd be able to 
  specify a family using rational functions of arbitrary constants 
  (something like a x^2 + b/(a-1) y^2), and compute the projective dual in 
  terms of those constants.
```


A good place to start in implementing this could be http://www.emilvolcheck.com/dual.ps



---

Comment by davideklund created at 2012-05-26 01:45:11

The attached patch implements this for (reduced and irreducible) hypersurfaces over the rationals. I intend to generalize this.

I use Grobner bases and elimination. Resultants might be faster so I might switch to that approach.

If you plug in a variety I think the dual should be reduced. I'm not sure exactly what the scheme structure of the output is at the moment.

Something related to think about for the general case: given a subscheme X of projective space, what should the dual of X be?

I will look at the approach described in the attached paper. When the dual is a hypersurface and has smaller degree than "expected", that approach seems to be better than the one used at the moment.


---

Comment by davideklund created at 2012-05-26 02:11:09

Changing priority from major to minor.


---

Attachment

The patch implements duals of projective hypersurfaces. Patch rebased on top of Sage 5.2.


---

Comment by davideklund created at 2012-08-24 17:40:16

Patch rebased on top of Sage 5.2.


---

Comment by chapoton created at 2014-03-06 13:52:22

Here is a git branch. Maybe this could be considered as need review ?
----
New commits:


---

Comment by davideklund created at 2014-03-06 18:18:48

I guess it could be reviewed. It could be useful as it is. I had some plans to do something better but someone stole all my time... There is no particular reason to stick to hypersurfaces, it was just meant as an initial simplification.


---

Comment by davideklund created at 2014-03-06 18:20:30

Nor is there any particular reason to stick to varieties over Q.


---

Comment by git created at 2015-01-27 20:35:06

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-01-27 20:44:40

Changing status from new to needs_review.


---

Comment by chapoton created at 2015-01-27 20:44:40

turning that into `needs review` to require feedback:

what is the class of rings over which this can currently work ?


---

Comment by git created at 2015-02-27 09:45:49

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-05-28 13:36:33

Changing keywords from "" to "projective duality".


---

Comment by chapoton created at 2015-10-18 19:50:26

nobody interested by this ticket ?


---

Comment by git created at 2016-01-18 13:30:04

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vbraun created at 2016-02-23 22:46:59

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-02-24 19:35:24

Resolution: fixed
