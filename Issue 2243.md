# Issue 2243: contour_plot bug

Issue created by migration from https://trac.sagemath.org/ticket/2243

Original creator: mabshoff

Original creation time: 2008-02-21 01:35:05

Assignee: was

Keywords: contour, plot

Kate reported in https://groups.google.com/group/sage-support/browse_thread/thread/843c9452036e9608/d5c4e6a830a66327#d5c4e6a830a66327

```
In 2.10.1,

  sage:  R.<x,y> = PolynomialRing(QQ,2)
  sage:  contour_plot(y-1,(-10,10),
(-10,10),fill=False,contours=1,plot_points=100)

plots the line y = -9 rather than the line y=1

  sage:  contour_plot(-y+1,(-10,10),
(-10,10),fill=False,contours=1,plot_points=100)

correctly plots y = 1.

Kate
```

David Joyner could confirm the bug:

```
sage: contour_plot(y-1,(-10,10),(-10,10),fill=False,contours=2,plot_points=100)
sage: contour_plot(y-1,(-10,10),(-10,10),fill=False,contours=1,plot_points=100) 
```


Cheers,

Michael


---

Comment by anakha created at 2008-09-21 19:34:14

I think contour_plot is misused here.  'contours=1' tells contour_plot to draw one contour without specifying its value.  If you want to really draw the portion where the function equals 1 and nothing else, use 'contours=[1]'.


---

Comment by mhansen created at 2009-06-04 21:29:53

Resolution: invalid


---

Comment by mhansen created at 2009-06-04 21:29:53

I think Arnaud's comment is the correct one.  If you look at the (current) documentation for contour_plot, you'll see


```
            contours     -- integer or list of numbers (default: None):
                            If a list of numbers is given, then this specifies
                            the contour levels to use.  If an integer is given,
                            then this many contour lines are used, but the
                            exact levels are determined automatically.
                            If None is passed (or the option is not given),
                            then the number of contour lines is determined
                            automatically, and is usually about 5.
```

