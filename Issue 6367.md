# Issue 6367: polygon2d -- several issues: typo in docs, shouldn't have been renamed

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-20 15:25:14

Assignee: was

CC:  ksmith

The help for polygon2d? says:


```
 Type ``polygon.options`` for a dictionary of the default 
    options for polygons.  You can change this to change 
```

but it should say

```
 Type ``polygon2d.options`` for a dictionary of the default 
    options for polygons.  You can change this to change 
```


And for the record I think it is unfortunate that somebody changed the function name from polygon to polygon2d, since that it inconsistent with almost all the rest of plotting in Sage, where the 2d version of the function doesn't specifically say it is 2d (e.g., plot, line, text, etc.) Well, there is line2d, to add to the confusion.    The design of Sage graphics is *supposed* to follow the naming scheme in Matheamtica.  In Mathematica there is Polygon and Polygon3D.  That's what Sage should have.

To resolve this patch, either fix the docstring or change the name back to polygon (not polygon2d).  I prefer the latter for consistency with the rest fo the design of sage 2d graphics. 





---

Comment by kcrisman created at 2010-07-27 17:25:19

For the record, this caused some actual problems for a potential Sage user recently, so it should get fixed - and soon.  Probably we'll need to make polygon=polygon2d (for 2d input) for deprecation reasons, for now.


---

Comment by kcrisman created at 2012-05-26 21:11:13

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-05-26 21:11:13

Unfortunately this is pretty hard to change since `polygon` is expected to work for two and three D input.  This patch does take care of the problem.


---

Attachment

> Unfortunately this is pretty hard to change since `polygon` is expected to work for two and three D input.
What I mean, of course, is that it would be hard to change since users probably are using it this way a lot and the deprecation period and all simply isn't worth the effort at this point.  Anyway, needs review.


---

Comment by kcrisman created at 2012-05-27 06:50:14

Oops, totally forgot about #12214, which is a dup of this.  Given that #12214 is virtually the same ticket, this one is much older, and the patch is quite similar, I'm adding the author there to this ticket and closing that one.


---

Comment by vbraun created at 2012-11-06 04:14:36

Looks good to me!


---

Comment by vbraun created at 2012-11-06 04:14:36

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-11-11 09:48:16

Resolution: fixed
