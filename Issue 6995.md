# Issue 6995: plotting specific contour lines should shade values above/below the extreme contour values

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-09-22 21:32:13

Assignee: was

CC:  kcrisman

Notice that this plot is mostly white, but the white space represents two different values---one is above the top contour, the other is below the bottom contour.

We ought to make it so that stuff above/below the requested contours is shaded appropriately.


```
var('x,y')
contour_plot(x-y^2,(x,-5,5),(y,-3,3),contours=[-4,0,1])
```




---

Comment by jason created at 2009-10-12 18:24:31

I wonder if #5221 fixes this.  I don't have an up-to-date alpha to test this, though.


---

Attachment


---

Comment by jason created at 2009-11-10 17:28:54

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-11-10 19:07:28

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-11-10 19:07:28

Positive review.  I wonder if this is also the 'right' way to have fixed #5221, since you mention that ticket? See [this link](http://matplotlib.sourceforge.net/api/pyplot_api.html?highlight=contourf#matplotlib.pyplot.contourf).

Note to release manager: this depends on #4898.


---

Comment by mhansen created at 2009-11-12 06:57:59

Resolution: fixed
