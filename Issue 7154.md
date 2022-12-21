# Issue 7154: options for point/arrow thickness are inconsistently named

Issue created by migration from Trac.

Original creator: vbraun

Original creation time: 2009-10-08 11:07:33

Assignee: was

CC:  jason kcrisman

Keywords: point arrow thickness

There should be a consistent naming scheme for the "thickness" of graphics objects. If I have a function my_plot(**kwds) that passes **kwds to all constructed graphics objects, then my_plot(thickness=5) should consistently scale the thickness. 

The current status is:


```
  sage: point([0,0], pointsize = 5)
  sage: point3d((0,0,0), thickness=5)                      
  sage: line2d([[0,0],[1,1]], thickness=5)
  sage: line3d([[0,0,0],[1,1,0]], thickness=5)
  sage: arrow([0,0],[1,1], width=5)    
  sage: arrow3d([0,0,0],[1,1,1], thickness=5)
  sage: polygon([(0,0), (1,1), (0,1)], thickness=5)      
  sage: polygon3d([(0,0,0), (1,1,0), (0,1,0)], thickness=5)
```




---

Comment by vbraun created at 2009-10-09 09:29:13

Also, the arrow3d thickness behaves differently than the thickness of point3d and line3d: If you zoom in, the arrow becomes bigger and bigger like a physical object. The line3d and point3d stay the same apparent size, about thickness pixels wide on screen. Since the arrow3d is usually used to indicate a direction it would be nice if it would scale (or, rather, not scale) just like point3d and line3d.


```
  sage: scene = \
  ....: line3d([[1,0,0],[1,3,0]],thickness=5) + \
  ....: arrow3d([2,0,0],[2,3,0],thickness=5) + \
  ....: point3d([3,2,0],thickness=5)
  sage: scene.show( aspect_ratio=[1,1,1])
```


and then zoom in/out in the Jmol viewer.


---

Comment by jason created at 2010-05-26 15:38:54

I agree with the first comment; the arguments should distinguish between "width", which is in data coordinates and changes as you zoom, and "thickness", which is in screen coordinates, and does not change as you zoom.  Figure out which is which for the cases above, and probably use the `@`rename_keyword decorator from the plotting code to change instances with deprecation.


---

Comment by jason created at 2010-05-26 15:38:54

Changing keywords from "point arrow thickness" to "point arrow thickness, beginner".


---

Comment by ryan created at 2010-08-21 14:13:51

Rename arrow 'width' option to 'thickness'


---

Attachment

looking at the arrow3d thickness now.


---

Attachment


---

Comment by ryan created at 2010-08-21 22:38:27

In response to jason's comment, I submit a patch that renames the thickness keyword of arrow3d to width.  The reason is that the width of the arrow3d are not screen coordinates.  Why? Because arrow3d is constructed of a cylinder and the thickness controls the radius of this cylinder.

If someone is looking for an alternative to arrow3d that does not scale when zoomed, you can use line3d with arrow_head=True.


---

Comment by ryan created at 2010-08-21 22:38:27

Changing status from new to needs_review.


---

Comment by jason created at 2010-08-21 23:55:15

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-08-21 23:55:15

Thanks!  Fixing things like this really add to the polish and ease-of-use of Sage, and make it much more user-friendly.

Three comments:

1. I think the rename_keyword works the other way.  See this example from the docs:


```
rename_keyword(deprecated='Sage version 4.2', deprecated_option='new_option')
```


Don't you want it to be thickness='width'?  Also, the actual keyword in the function should be changed in the function declaration (you can probably then search and replace in the function definition to replace 'thickness' with 'width'.

2. Could you add a deprecation by using the deprecation feature of rename_keyword?

3. Could you add a short doctest showing the deprecation warning and the new option?  The deprecation warning should probably be in a TESTS: section, while the new option should definitely be in the EXAMPLES section.

Thanks for working on this!


---

Comment by ryan created at 2010-08-22 02:11:38

oops. The rename_keyword in the *arrow3d_width.patch is backwards.  I'll update it as soon as I can (with the other changes as well).

Also, is there really a need for arrow3d to scale when zoomed?  I can't think of any instance where that would be genuinely useful.  Maybe arrow3d should be changed to match the behavior of line3d if that is what people are expecting.


---

Comment by ryan created at 2010-08-28 18:16:17

updated - added doctests and deprecation warning


---

Attachment

the real update :)  added doctest and deprecation warning


---

Comment by ryan created at 2010-08-28 18:19:07

sorry accidentally uploaded the wrong patch.


---

Comment by jason created at 2010-08-29 02:56:02

Wow, that is a huge patch.  It looks like a lot of whitespace changes.  Is that right?


---

Comment by ryan created at 2010-08-29 04:57:08

Replying to [comment:10 jason]:
> Wow, that is a huge patch.  It looks like a lot of whitespace changes.  Is that right?

I was also puzzled at why it was so big.  Most likely it has something to do with my python editor removing trailing spaces on save.


---

Comment by ryan created at 2010-09-11 05:23:32

Updated patch (with Sage 4.5.3)


---

Comment by ryan created at 2010-09-11 05:24:36

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by jason created at 2010-09-11 16:55:02

apply instead of previous patch


---

Comment by jason created at 2010-09-11 16:56:33

Changing status from needs_review to positive_review.


---

Attachment

Looks good.  I updated the version number in trac_7154_arrow3d_width.4.patch; apply only that patch.  

Thanks!

This is Ryan's first contribution, along with #8838 and #9199.


---

Comment by mpatel created at 2010-09-15 10:40:41

Resolution: fixed
