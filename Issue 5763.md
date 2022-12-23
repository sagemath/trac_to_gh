# Issue 5763: [with patch, needs review] pynac -- add _polynomial_ conversion constructor

Issue created by migration from https://trac.sagemath.org/ticket/5763

Original creator: ncalexan

Original creation time: 2009-04-11 21:40:01

CC:  burcin mhansen was

Keywords: pynac symbolics _polynomial_ constructor

The attached patch adds conversion to polynomial rings.  Two doctests fail at this time; they rely on being able to convert to CDF and ComplexField(100).  I didn't want them to get forgotten so I left them in.


---

Attachment

Thanks Nick!

The patch looks great, I am looking at the doctests right now. 

Note that #5753 fixes the coercion of constants to pynac, so you can use `is_a_constant` in the .is_constant() function.

I will see what I can do about the doctest failures, and hopefully post a patch fixing them soon.


---

Comment by ncalexan created at 2009-04-12 19:44:36

In fact, you can make the doctest works by changing the if is_constant check to coerce the pyobject in.  It's a one line fix that I haven't posted here, it works well for me in practice.


---

Comment by burcin created at 2009-05-24 16:49:21

This patch seems to have been forgotten during the "pynac push." I recall that it was briefly mentioned on IRC once.

I suggest closing this issue as wontfix now. Trac doesn't allow me close tickets any more.


---

Comment by was created at 2009-05-28 06:57:06

This isn't critical for 4.0.


---

Comment by mvngu created at 2009-06-08 03:47:58

The docstring should adhere to ReST formatting. Some examples follow this rule, but most don't. I'm merely enforcing proper ReST formatting, not actually reviewing the whole patch.


---

Comment by boothby created at 2009-07-15 22:06:25

This should have been marked as a negative review.


---

Comment by mhansen created at 2013-07-22 15:07:11

Resolution: invalid


---

Comment by mhansen created at 2013-07-22 15:07:11

I think we can close this as invalid as all of the doctests in the patch currenly pass.
