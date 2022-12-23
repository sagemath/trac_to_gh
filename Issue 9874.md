# Issue 9874: Can't upload from a notebook link, only from a .sws file

Issue created by migration from https://trac.sagemath.org/ticket/9875

Original creator: kcrisman

Original creation time: 2010-09-08 15:12:26

Assignee: jason, was

Trying to upload using the dialogue and feeding a link to a sage notebook directory (such as `x.sagenb.org/home/username/3/` causes an error - you can only upload sws files.  I think this should be considered a bug, though, since it means you have to actually click on the file instead of just the link in `/pub/`.  

Alternately, creating a link directly to the .sws on each worksheet list (including `/pub/`) would be ok, but I think that's inferior and less elegant.


---

Comment by jason created at 2010-09-08 15:23:02

Can you be more clear in your description?  I'm really confused by your description.


---

Comment by kcrisman created at 2010-09-08 16:48:15

Better?


---

Comment by jason created at 2010-09-08 16:57:00

Much better.  I agree that putting in the URL of a published worksheet would be nice to work.


---

Comment by nthiery created at 2011-01-18 13:22:46

Is this a duplicate of #7441?

Related ticket #10652 (shameless plug)


---

Comment by jason created at 2011-01-18 13:35:16

I think you're right that it is a duplicate of #7441


---

Comment by kcrisman created at 2011-01-18 14:28:14

I've asked some questions on #7441 to verify whether this issue is also taken care of by the patches at #7441.  The description of #7441 is a dup, but the patches might not do exactly what this asks (namely, allowing *old* published worksheets to be uploaded from some server, and not needing the html ending).


---

Comment by kcrisman created at 2012-07-06 00:13:22

It's conceivable that this is resolved by [this github PR](https://github.com/sagemath/sagenb/pull/56), but not necessarily, since the file ending might not be taken care of.


---

Comment by kcrisman created at 2013-06-14 17:04:03

I believe this request did indeed take care of it!  At least, in Sage 5.6 I can confirm that just entering a link of the form

```
http://sage....edu/home/pub/73/
```

worked nicely.  Jason, can you try this?  I'd like to have dual confirmation that I'm not crazy.


---

Comment by kcrisman created at 2013-06-14 17:04:03

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-06-18 21:03:24

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2013-06-18 21:03:24

Okay, it was actually [this commit of Dan Drake's](https://github.com/sagemath/sagenb/commit/1b3b2c6793c621032e088e3093c99e87fd55ce07#sagenb/data/sage/html/upload.html).  Yay!


---

Comment by jdemeyer created at 2013-06-19 12:17:02

Resolution: worksforme
