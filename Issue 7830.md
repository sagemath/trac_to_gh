# Issue 7830: function for floating point representation of a number

Issue created by migration from https://trac.sagemath.org/ticket/7830

Original creator: jason

Original creation time: 2010-01-03 07:37:21

Assignee: AlexGhitza

Here's a function that answers the question posed in http://groups.google.com/group/sage-devel/browse_thread/thread/c8c75b483f2c47f6 -- give the sign, mantissa, and exponent of a floating point number.

I also cleaned up a few minor other things.


---

Attachment


---

Comment by jason created at 2010-01-03 07:45:54

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-01-07 07:40:31

Looks good. I don't like the name `representation()` either--maybe `parts()`?


---

Comment by jason created at 2010-01-07 16:59:37

parts() seems too vague.  Maybe ieee_754_parts(), except that we support arbitrary precision, not just the set precisions they mention.  Maybe floating_point_representation(), or sign_mantissa_exponent().

I'm willing to concede on the naming to make sure this gets in before I start my numerical analysis class in two weeks :).


---

Comment by robertwb created at 2010-01-07 19:51:55

Lets go with `sign_mantissa_exponent()`. Verbose but clear, and one doesn't even have to look at the docstring every time to remember what order the tuple comes in :)


---

Comment by jason created at 2010-01-08 12:27:51

apply on top of previous patch


---

Attachment

Okay, I added a patch which changes the name.  This is hopefully ready for a positive review now :).


---

Comment by cremona created at 2010-01-11 20:38:19

I see that you have only added this method to mpfr.  Should we not preserve as much consistency as possible between the different real types by also adding it to real_double?


---

Comment by jason created at 2010-01-11 22:04:14

Very good point.  I'll look at this.  I might just end up creating an RR number and calling this method behind the scenes


---

Attachment

apply on top of previous patches


---

Comment by jason created at 2010-01-20 08:42:22

I've added a similar function to RDF now.


---

Comment by robertwb created at 2010-01-20 09:02:53

http://en.wikipedia.org/wiki/IEEE_754-1985

The exponent for 0 should be 0. This also avoids the issue of platform dependance for that value, and `RDF(0)`'s exponent being unrealistically small. 

Also, sage/rings/real_mpfr.pyx, line 1890 should be EXAMPLES::


---

Comment by robertwb created at 2010-01-20 09:02:53

Changing status from needs_review to needs_work.


---

Attachment

apply on top of previous patches


---

Comment by jason created at 2010-01-20 09:33:16

The last patch fixes a few other documentation errors and an error in multiplicative_order too.  For free.


---

Comment by jason created at 2010-01-20 09:33:16

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2010-01-20 09:40:39

all four of the above folded into one


---

Attachment

Looks good.


---

Comment by robertwb created at 2010-01-20 09:40:55

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-22 21:11:27

Resolution: fixed


---

Comment by jason created at 2010-01-26 21:27:58

The mantissa and exponent for MPFR is not the same as the mantissa and exponent for IEEE 754.  So I'm a little doubtful about the choice to follow IEEE 754 conventions for the exponent value of 0.  (but I'm not doubtful enough to change it).  I just thought I'd point out that the values from MPFR are different than the conventions from IEEE 754 for the same floating point number.
