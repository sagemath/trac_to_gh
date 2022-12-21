# Issue 2449: interact -- interactive functions in the notebook

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-09 23:45:58

Assignee: boothby

CC:  timothyclemans

This was #1322.


---

Comment by was created at 2008-03-09 23:47:03

Changing assignee from boothby to was.


---

Comment by was created at 2008-03-09 23:47:03

Changing status from new to assigned.


---

Comment by was created at 2008-03-10 01:35:11

The two bundles below should apply cleanly against 2.10.3.rc3 and give everything
needed try use the new interact functionality, which is now done modulo bugfixes:

  * http://sage.math.washington.edu/home/was/patches/interact-extcode.hg

  * http://sage.math.washington.edu/home/was/patches/interact-sage.hg

You can apply both as follows:

```
sage: hg_sage.apply('http://sage.math.washington.edu/home/was/patches/interact-sage.hg'); hg_sage.merge(); hg_sage.update()

sage: hg_extcode.apply('http://sage.math.washington.edu/home/was/patches/interact-extcode.hg'); hg_extcode.merge(); hg_extcode.update()

```



---

Comment by was created at 2008-03-10 06:00:54

To try out this code, just start up the sage notebook, create a worksheet, and type interact?


---

Comment by was created at 2008-03-10 06:12:55

Here's an example that makes use of several of the different available widgets:

```
`@`interact
def _(title=["A Plot Demo", "Something silly", "something tricky"], a=input_box(sin(x*sin(x*sin(x))), 'function'),
      clr=Color('red'), thickness=[1..30], zoom=(1,0.95,..,0.1), plot_points=(200..2000)):
     html('<h1 align=center>%s</h1>'%title)
     print plot_points
     show(plot(a, -zoom*pi,zoom*pi, color=clr, thickness=thickness, plot_points=plot_points))
```



---

Comment by gfurnish created at 2008-03-10 06:19:13

Changing type from defect to enhancement.


---

Comment by TimothyClemans created at 2008-03-10 06:38:34

Blows my mind. 

One suggestion is to have some builtin styles for an interact box. 
Maybe:
`@`interact(style='blue') or `@`interact(style='white') ...

Also I noticed that there is an empty white area above a plot in an interact box.


---

Comment by TimothyClemans created at 2008-03-10 06:45:13

Also I think type=blah should be added to all of the standard controls not just input_box.


---

Comment by TimothyClemans created at 2008-03-10 07:02:43

Here is my attempt at being able to show what you are coloring in a plot:


```
`@`interact
def _(item=['Polygon', 'Points'],c=Color('red')):
    pts = [(0.65438363916925979, 0.85150056342598845), (0.70937855184366272,
0.029131148388535144), (0.85031921177678882, 0.85521222531849894),
(0.43668577545798215, 0.08598920033699009), (0.65641161685705918,
0.26493224917213731), (0.66939907297513568, 0.32187884928032584)]
    a = (0,0.5,0)
    b = (0,1,0.5)
    if item == 'Polygon':
        b = c
    else:
        a = c
    G = points(pts,pointsize=60,rgbcolor=a) + polygon(pts, rgbcolor=b)
    show(G, figsize=5, xmin=0, ymin=0)
```


(1) It would be nice if the box wasn't refreshed when I hit a button.
(2) When I pick say a color for the polygon I want the polygon to be that color throughout until changed again by me using the polygon button and color picker.


---

Comment by schilly created at 2008-03-10 10:07:38

wow, looks very nice. just from looking at the screenshot: what about adding the current value and min/max next to the sliders? would be helpful to see the value of a slider directly.

ex:

[min] |-------V--| [max] cur. value


---

Comment by was created at 2008-03-10 15:35:37

Hi, Thanks for all the comments above.

> One suggestion is to have some builtin styles for an interact box.
>  Maybe: `@`interact(style='blue') or `@`interact(style='white') ...

This is specifically listed as a post 1.0 enhancement in interact.py and
I will not modify the current patch to do that.  More likely, I will leave
that to somebody else to do after this is released.

> Also I think type=blah should be added to all of the standard 
> controls not just input_box.

That doesn't make sense because input_box is the only control where
the code creating the control hasn't already determined the type
by their input.  E.g., for buttons, sliders, etc., one is giving
the types by the input that creates the widget.

> (1) It would be nice if the box wasn't refreshed when I hit a button. 

What box?  I don't understand this at all.

> (2) When I pick say a color for the polygon I want the polygon 
> to be that color throughout until changed again by me using 
> the polygon button and color picker.

Isn't that exactly what happens?


---

Comment by was created at 2008-03-10 15:37:35

> wow, looks very nice. just from looking at the screenshot:
> what about adding the current value and min/max next to the 
> sliders? would be helpful to see the value of a slider directly.

That should be a widget style option, which should be made 
by somebody else *after* the initial release of interact.  
It shouldn't be on by default because it would clutter the interface.


---

Attachment

Only apply this *after* #2451, or some of the doctest examples might be very slow.


---

Comment by TimothyClemans created at 2008-03-10 19:19:05

The commentary for example one in the documentation says that a slider will be the control for the y variable, but I get a dropdown menu.

I find the difference in font color and background between the interact box as a whole and the output area inside it annoying.

I would like there to be a str type option for the other controls, so I don't see quote marks in say button names.


---

Comment by was created at 2008-03-11 02:11:43

Resolution: fixed
