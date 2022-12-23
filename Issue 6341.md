# Issue 6341: implement Mestre's algorithm for constructing genus 2 hyperelliptic curves

Issue created by migration from https://trac.sagemath.org/ticket/6341

Original creator: ncalexan

Original creation time: 2009-06-16 19:48:36

Assignee: was

CC:  ncalexan mstreng jpflori lassina fstromberg

Keywords: mestre algorithm genus 2 hyperelliptic curves




---

Attachment


---

Attachment

Here's a work in progress version.  The extcode patch

 * updates Denis Simon's pari qfsolve program;
 * and incorporates Paul van Wamelen's pari genus 2 package.

The main devel patch integrates everything, or at least starts to.


---

Attachment


---

Attachment

The files "-without..." are the same as ncalexan's files, but with the Conic class removed and put in a separate patch at ticket 727. They still need the Conic class, but it may be better to view this as a separate enhancement.


---

Comment by mstreng created at 2011-06-06 08:56:17

This will be revived as part of a student project in August 2011.


---

Comment by mstreng created at 2011-12-17 14:39:18

Changing keywords from "mestre algorithm genus 2 hyperelliptic curves" to "mestre algorithm genus 2 hyperelliptic curves sd35".


---

Comment by mstreng created at 2011-12-17 14:39:18

Code was written by Florian Bouyer in September 2011, it works very nicely. Now it is a coding sprint at [Sage Days 35](http://wiki.sagemath.org/SageFlintDays/) to put this in.


---

Attachment

An implementation of Mestre Algorithm


---

Comment by florian created at 2011-12-19 13:12:07

Changing status from needs_work to needs_review.


---

Comment by mstreng created at 2011-12-19 21:15:38

apply trac_6341_mestre_algorithm.patch

(this helps [patchbot](http://wiki.sagemath.org/buildbot))


---

Comment by mstreng created at 2011-12-20 11:46:40

See also #12199, which will later fill in some special cases.


---

Comment by florian created at 2011-12-20 13:31:02

See also #12200, which will later fill in some special case


---

Comment by florian created at 2011-12-20 16:05:58

minor changes to first patch


---

Attachment

I corrected some typos and wasted white spaces pointed out by Marco


---

Comment by mstreng created at 2011-12-22 15:03:57

Changing status from needs_review to needs_work.


---

Comment by mstreng created at 2011-12-22 15:03:57

I'm reviewing and writing a reviewer's patch. Looks very good, but some small changes are needed that are easier to do than to explain.


---

Attachment


---

Comment by mstreng created at 2011-12-27 10:23:56

I wrapped lines and clarified / corrected documentation and corrected some formulas. I also removed functions that were not needed.

To do:

 - continue with wrapping lines and checking documentation for spelling or formatting problems
 - add the missing examples and possibly some more with non-trivial reduction properties
 - remove functions marked with "to_remove"
 - make sure stoll-cremona reduction is correctly implemented when homogenized to higher degree than the degree of the polynomial
 - add a sanity check at the end of HyperellipticCurve_from_invariants, checking if the curve has the correct invariants before outputting it (RuntimeError otherwise)

apply 6341_combined.patch


---

Comment by mstreng created at 2011-12-27 10:25:08

Changing priority from minor to major.


---

Comment by mstreng created at 2012-02-03 11:20:26

With a view towards the future (number fields), it may be a good idea to move the code from lines 679 -- 732 to a separate function with input a polynomial, a valuation and a uniformizer. If the uniformizer generates the prime ideal, this gives a local reduction that does not screw up the other primes. If this is not possible (e.g. a non-principal prime of a number field) you can still get a local reduction and combine the local reductions later.


---

Attachment

version under construction, apply on top of previous patch, supposed to work for number fields, requires #11455


---

Attachment

on top of previous


---

Attachment


---

Attachment


---

Attachment

only Mestre's algorithm


---

Comment by mstreng created at 2013-06-17 13:17:36

I separated off the (huge) reduction code from this simple functionality. Hopefully that helps in finishing this ticket.


---

Comment by chapoton created at 2013-07-09 09:37:50

instructions for the patchbot :

apply 6341-mestre-only.patch


---

Comment by chapoton created at 2013-07-09 09:56:19

here is patch, just cleaning things up. There are some doctests failing..

apply 6341-mestre-only.patch trac_6341-mestre-only_cleanup.patch


---

Attachment


---

Comment by mstreng created at 2013-07-22 13:29:33

Changing keywords from "mestre algorithm genus 2 hyperelliptic curves sd35" to "mestre algorithm genus 2 hyperelliptic curves sd35 sd51".


---

Attachment


---

Comment by florian created at 2013-07-23 13:12:25

Changing status from needs_work to needs_review.


---

Comment by mstreng created at 2013-07-24 11:29:59

Changing status from needs_review to needs_work.


---

Comment by mstreng created at 2013-07-24 12:53:52

Changing status from needs_work to needs_review.


---

Comment by mstreng created at 2013-07-24 20:05:21

apply after the other three


---

Attachment


---

Comment by mstreng created at 2013-07-24 20:21:02

Changing status from needs_review to needs_work.


---

Attachment

(testing now)


---

Comment by mstreng created at 2013-07-25 06:46:18

for patchbot:
apply 6341-mestre-only.patch and trac_6341-mestre-only_cleanup.patch and 6341-mestre-corrections.3.patch


---

Comment by mstreng created at 2013-07-25 10:09:14

Changing status from needs_work to needs_review.


---

Comment by mstreng created at 2013-07-25 11:41:37

apply 6341-mestre-only.patch and trac_6341-mestre-only_cleanup.patch and 6341-more-corrections.3.patch


---

Comment by mstreng created at 2013-08-27 11:56:05

I combined the patches into one, for easier review. Apply only 6341.patch


---

Comment by mstreng created at 2013-08-28 19:34:41

ascii version of what was uploaded earlier this week


---

Attachment

apply only 6341.patch


---

Comment by aly.deines created at 2013-09-24 13:46:18

This is working for me.  I've verified several more non-CM examples in Magma.


---

Comment by aly.deines created at 2013-09-24 13:46:18

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-10-02 06:34:34

Resolution: fixed
