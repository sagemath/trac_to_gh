# Issue 8338: Add Fourier transforms

Issue created by migration from Trac.

Original creator: olazo

Original creation time: 2010-02-23 19:36:16

Assignee: burcin

CC:  kcrisman

Keywords: fourier,transform

Sage has got laplace and inverse_laplace. It should be fairly easy to add fourier and inverse_fourier. An adecuate definition for each should be agreed upon though...


---

Comment by wdj created at 2010-02-23 20:05:12

Sage has Fourier series in the Piecewise class. 

For the FT, I vote to use the normalization so that FT is an isometry from L<sup>2</sup>(R) to itself.


---

Comment by olazo created at 2010-02-24 01:27:34

Changing assignee from burcin to olazo.


---

Comment by olazo created at 2010-02-24 01:28:31

Changing type from defect to enhancement.


---

Comment by olazo created at 2010-02-24 01:38:24

Replying to [comment:1 wdj]:
> Sage has Fourier series in the Piecewise class. 

I'll be checking that.

> For the FT, I vote to use the normalization so that FT is an isometry from L<sup>2</sup>(R) to itself.

I don't understand what you mean there. Could you explain, perhaps post some latex formulas to show your proposed definition.

thanks

Oscar


---

Comment by wdj created at 2010-02-24 13:18:04

Replying to [comment:4 olazo]:
> Replying to [comment:1 wdj]:
> 
> > For the FT, I vote to use the normalization so that FT is an isometry from L<sup>2</sup>(R) to itself.
> 
> I don't understand what you mean there. Could you explain, perhaps 
> post some latex formulas to show your proposed definition.


The formulas are at http://en.wikipedia.org/wiki/Fourier_transform
(which in turn refers to Rudin)

> 
> thanks
> 
> Oscar


---

Comment by burcin created at 2010-04-05 12:42:18

I don't think anybody is working on this. I'm changing the milestone to `sage-wishlist`. 

See also the [symbolics wiki page](http://wiki.sagemath.org/symbolics) for some general pointers about implementing transforms in Sage.
