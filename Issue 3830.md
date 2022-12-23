# Issue 3830: plot(sin(1/x), (x,-1,3), foo=10) yields an error message about line, but should yield one about plot.

Issue created by migration from https://trac.sagemath.org/ticket/3830

Original creator: was

Original creation time: 2008-08-13 03:02:53

Assignee: was


```
plot(sin(1/x), (x,-1,3), foo=10)
///
          	

verbose 0 (1537: plot.py, options) WARNING: Ignoring option
'plot_division'=0
verbose 0 (1537: plot.py, options) 
The allowed options for Line defined by 94005 points are:
    alpha          How transparent the line is.                         

    hue            The color given as a hue.                            

    linestyle      The style of the line, which is one of '--' (dashed),
'-.' (dash dot), '-' (solid), 'steps', ':' (dotted).
    marker         '0' (tickleft), '1' (tickright), '2' (tickup), '3'
(tickdown), '' (nothing), ' ' (nothing), '+' (plus), ',' (pixel), '.'
(point), '1' (tri_down), '3' (tri_left), '2' (tri_up), '4' (tri_right),
'<' (triangle_left), '>' (triangle_right), 'None' (nothing), 'D'
(diamond), 'H' (hexagon2), '_' (hline), '^' (triangle_up), 'd'
(thin_diamond), 'h' (hexagon1), 'o' (circle), 'p' (pentagon), 's'
(square), 'v' (triangle_down), 'x' (x), '|' (vline)
    markeredgecolorthe markerfacecolor can be any color arg             

    markeredgewidththe size of the markter edge in points               

    markersize     the size of the marker in points                     

    rgbcolor       The color as an rgb tuple.                           

    thickness      How thick the line is.                               


Traceback (click to the left for traceback)
...
AttributeError: Unknown property foo
```


The error that comes from line could just be very lightly wrapped in an error from plot that says plot error using the line command.  This could thus be almost trivially fixed.


---

Comment by ddrake created at 2009-01-23 00:52:27

This looks nice, but the error message is a bit confusing: you have

```
raise RuntimeError("Error in line: option '%s' not valid."%opt) 
```

and when I see that error message, it looks like it's trying to tell me there's an error on some line of code, and not in the function that produces lines. Perhaps change it to "Error in Line(): option..."?


---

Attachment


---

Comment by rlm created at 2009-01-23 02:37:10

OK, updated.


---

Comment by ddrake created at 2009-01-23 04:12:59

Looks nice. Positive review.


---

Comment by mabshoff created at 2009-01-23 10:26:17

Merged in Sage 3.3.alpha1

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 10:26:17

Resolution: fixed
