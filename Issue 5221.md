# Issue 5221: default cmap for contour plot makes last contour line invisible when fill=False

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-02-09 16:12:04

Assignee: was

Examine the output of 


```
var('x,y')
contour_plot(x-y^2,(x,-5,5),(y,-3,3),contours=[-4,0,1], fill=False)
```



The last contour line (level curve at z=1) is invisible because the default cmap makes it white.  Compare that to a different color map:


```
var('x,y')
contour_plot(x-y^2,(x,-5,5),(y,-3,3),contours=[-4,0,1],cmap='winter',fill=False)
```


We should make the default cmap something less confusing when fill=False.



---

Comment by kcrisman created at 2009-08-27 03:08:35

As it turns out, no cmap with any better visibility is any better - many of them have white as one of the options.  So this patch creates a custom cmap which is almost the same as 'gray' for the situation where fill is False, a cmap is not specified, but there are a specific number of contours (or exact contours) specified.

Note this patch depends on the patch at #5145.


---

Comment by jason created at 2009-09-10 15:24:51

Thanks for the patch!

I think this patch needs to be rebased after #5448.  The `@`options decorator for contour_plot is changed in that patch.


---

Comment by kcrisman created at 2009-09-10 15:47:01

Based on 4.1.1 and #5448 and #5145


---

Attachment

Try this.


---

Comment by jason created at 2009-09-22 21:23:44

Very nice!


---

Comment by jason created at 2009-09-22 21:26:48

(generally, you should do: "if 'cmap' in options", rather than "options.has_key('cmap')".


---

Comment by mvngu created at 2009-09-23 00:21:55

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:41:14

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
