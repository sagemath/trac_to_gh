# Issue 2709: add a prime_above() function to NumberField_generic for finding prime ideals above other ideals

Issue created by migration from https://trac.sagemath.org/ticket/2709

Original creator: ncalexan

Original creation time: 2008-03-28 21:24:02

Assignee: was

CC:  ncalexan craigcitro

Keywords: number field prime above

My research requires reducing curves over number fields modulo prime ideals, so I need to find suitable prime ideals all the time.  The attached function does exactly that, albeit naively.  I imagine this is useful to more people than me.


---

Attachment


---

Comment by ncalexan created at 2008-03-28 21:35:54

Craig's ticket request is #2711.


---

Comment by ncalexan created at 2008-03-28 22:11:01

Replying to [comment:2 ncalexan]:
> Craig's ticket request is #2711.

This was posted to the wrong ticket.


---

Attachment

After discussion on IRC, generalized to lists and made to raise an error on individual failure.  Apply both patches -- sorry for the inconvenience, I couldn't figure out how to cut one patch encompassing both changesets.


---

Comment by AlexGhitza created at 2008-03-29 02:39:30

Changing type from defect to enhancement.


---

Comment by AlexGhitza created at 2008-03-29 02:39:30

I like it *a lot*.  One small typo: in the docstring for prime_above(), section INPUT, description of the degree, have: "If one, find a prime...".  It should be "If None, find a prime..."  Of course, one would have to be fairly out of it to be confused by this for too long.

Did I mention that I like it *a lot*?


---

Comment by mabshoff created at 2008-03-29 14:36:09

Doctests pass for me on sage.math, so I will merge this in Sage 2.11.rc0 :)


---

Comment by mabshoff created at 2008-03-29 14:36:45

Merged in Sage 2.11.rc0


---

Comment by mabshoff created at 2008-03-29 14:36:45

Resolution: fixed
