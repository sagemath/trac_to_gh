# Issue 2449: interact -- interactive functions in the notebook

archive/issues_002449.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  timothyclemans\n\nThis was #1322.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2449\n\n",
    "created_at": "2008-03-09T23:45:58Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "interact -- interactive functions in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2449",
    "user": "was"
}
```
Assignee: boothby

CC:  timothyclemans

This was #1322.

Issue created by migration from https://trac.sagemath.org/ticket/2449





---

archive/issue_comments_016547.json:
```json
{
    "body": "Changing assignee from boothby to was.",
    "created_at": "2008-03-09T23:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16547",
    "user": "was"
}
```

Changing assignee from boothby to was.



---

archive/issue_comments_016548.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-09T23:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16548",
    "user": "was"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016549.json:
```json
{
    "body": "The two bundles below should apply cleanly against 2.10.3.rc3 and give everything\nneeded try use the new interact functionality, which is now done modulo bugfixes:\n\n* http://sage.math.washington.edu/home/was/patches/interact-extcode.hg\n\n* http://sage.math.washington.edu/home/was/patches/interact-sage.hg\n\nYou can apply both as follows:\n\n```\nsage: hg_sage.apply('http://sage.math.washington.edu/home/was/patches/interact-sage.hg'); hg_sage.merge(); hg_sage.update()\n\nsage: hg_extcode.apply('http://sage.math.washington.edu/home/was/patches/interact-extcode.hg'); hg_extcode.merge(); hg_extcode.update()\n\n```\n",
    "created_at": "2008-03-10T01:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16549",
    "user": "was"
}
```

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

archive/issue_comments_016550.json:
```json
{
    "body": "To try out this code, just start up the sage notebook, create a worksheet, and type interact?",
    "created_at": "2008-03-10T06:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16550",
    "user": "was"
}
```

To try out this code, just start up the sage notebook, create a worksheet, and type interact?



---

archive/issue_comments_016551.json:
```json
{
    "body": "Here's an example that makes use of several of the different available widgets:\n\n```\n@interact\ndef _(title=[\"A Plot Demo\", \"Something silly\", \"something tricky\"], a=input_box(sin(x*sin(x*sin(x))), 'function'),\n      clr=Color('red'), thickness=[1..30], zoom=(1,0.95,..,0.1), plot_points=(200..2000)):\n     html('<h1 align=center>%s</h1>'%title)\n     print plot_points\n     show(plot(a, -zoom*pi,zoom*pi, color=clr, thickness=thickness, plot_points=plot_points))\n```\n",
    "created_at": "2008-03-10T06:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16551",
    "user": "was"
}
```

Here's an example that makes use of several of the different available widgets:

```
@interact
def _(title=["A Plot Demo", "Something silly", "something tricky"], a=input_box(sin(x*sin(x*sin(x))), 'function'),
      clr=Color('red'), thickness=[1..30], zoom=(1,0.95,..,0.1), plot_points=(200..2000)):
     html('<h1 align=center>%s</h1>'%title)
     print plot_points
     show(plot(a, -zoom*pi,zoom*pi, color=clr, thickness=thickness, plot_points=plot_points))
```




---

archive/issue_comments_016552.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-03-10T06:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16552",
    "user": "gfurnish"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_016553.json:
```json
{
    "body": "Blows my mind. \n\nOne suggestion is to have some builtin styles for an interact box. \nMaybe:\n`@`interact(style='blue') or `@`interact(style='white') ...\n\nAlso I noticed that there is an empty white area above a plot in an interact box.",
    "created_at": "2008-03-10T06:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16553",
    "user": "TimothyClemans"
}
```

Blows my mind. 

One suggestion is to have some builtin styles for an interact box. 
Maybe:
`@`interact(style='blue') or `@`interact(style='white') ...

Also I noticed that there is an empty white area above a plot in an interact box.



---

archive/issue_comments_016554.json:
```json
{
    "body": "Also I think type=blah should be added to all of the standard controls not just input_box.",
    "created_at": "2008-03-10T06:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16554",
    "user": "TimothyClemans"
}
```

Also I think type=blah should be added to all of the standard controls not just input_box.



---

archive/issue_comments_016555.json:
```json
{
    "body": "Here is my attempt at being able to show what you are coloring in a plot:\n\n\n```\n@interact\ndef _(item=['Polygon', 'Points'],c=Color('red')):\n    pts = [(0.65438363916925979, 0.85150056342598845), (0.70937855184366272,\n0.029131148388535144), (0.85031921177678882, 0.85521222531849894),\n(0.43668577545798215, 0.08598920033699009), (0.65641161685705918,\n0.26493224917213731), (0.66939907297513568, 0.32187884928032584)]\n    a = (0,0.5,0)\n    b = (0,1,0.5)\n    if item == 'Polygon':\n        b = c\n    else:\n        a = c\n    G = points(pts,pointsize=60,rgbcolor=a) + polygon(pts, rgbcolor=b)\n    show(G, figsize=5, xmin=0, ymin=0)\n```\n\n\n(1) It would be nice if the box wasn't refreshed when I hit a button.\n(2) When I pick say a color for the polygon I want the polygon to be that color throughout until changed again by me using the polygon button and color picker.",
    "created_at": "2008-03-10T07:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16555",
    "user": "TimothyClemans"
}
```

Here is my attempt at being able to show what you are coloring in a plot:


```
@interact
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

archive/issue_comments_016556.json:
```json
{
    "body": "wow, looks very nice. just from looking at the screenshot: what about adding the current value and min/max next to the sliders? would be helpful to see the value of a slider directly.\n\nex:\n\n[min] |-------V--| [max] cur. value",
    "created_at": "2008-03-10T10:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16556",
    "user": "schilly"
}
```

wow, looks very nice. just from looking at the screenshot: what about adding the current value and min/max next to the sliders? would be helpful to see the value of a slider directly.

ex:

[min] |-------V--| [max] cur. value



---

archive/issue_comments_016557.json:
```json
{
    "body": "Hi, Thanks for all the comments above.\n\n> One suggestion is to have some builtin styles for an interact box.\n>  Maybe: `@`interact(style='blue') or `@`interact(style='white') ...\n\nThis is specifically listed as a post 1.0 enhancement in interact.py and\nI will not modify the current patch to do that.  More likely, I will leave\nthat to somebody else to do after this is released.\n\n> Also I think type=blah should be added to all of the standard \n> controls not just input_box.\n\nThat doesn't make sense because input_box is the only control where\nthe code creating the control hasn't already determined the type\nby their input.  E.g., for buttons, sliders, etc., one is giving\nthe types by the input that creates the widget.\n\n> (1) It would be nice if the box wasn't refreshed when I hit a button. \n\nWhat box?  I don't understand this at all.\n\n> (2) When I pick say a color for the polygon I want the polygon \n> to be that color throughout until changed again by me using \n> the polygon button and color picker.\n\nIsn't that exactly what happens?",
    "created_at": "2008-03-10T15:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16557",
    "user": "was"
}
```

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

archive/issue_comments_016558.json:
```json
{
    "body": "> wow, looks very nice. just from looking at the screenshot:\n> what about adding the current value and min/max next to the \n> sliders? would be helpful to see the value of a slider directly.\n\nThat should be a widget style option, which should be made \nby somebody else *after* the initial release of interact.  \nIt shouldn't be on by default because it would clutter the interface.",
    "created_at": "2008-03-10T15:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16558",
    "user": "was"
}
```

> wow, looks very nice. just from looking at the screenshot:
> what about adding the current value and min/max next to the 
> sliders? would be helpful to see the value of a slider directly.

That should be a widget style option, which should be made 
by somebody else *after* the initial release of interact.  
It shouldn't be on by default because it would clutter the interface.



---

archive/issue_comments_016559.json:
```json
{
    "body": "Attachment\n\nOnly apply this *after* #2451, or some of the doctest examples might be very slow.",
    "created_at": "2008-03-10T16:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16559",
    "user": "was"
}
```

Attachment

Only apply this *after* #2451, or some of the doctest examples might be very slow.



---

archive/issue_comments_016560.json:
```json
{
    "body": "The commentary for example one in the documentation says that a slider will be the control for the y variable, but I get a dropdown menu.\n\nI find the difference in font color and background between the interact box as a whole and the output area inside it annoying.\n\nI would like there to be a str type option for the other controls, so I don't see quote marks in say button names.",
    "created_at": "2008-03-10T19:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16560",
    "user": "TimothyClemans"
}
```

The commentary for example one in the documentation says that a slider will be the control for the y variable, but I get a dropdown menu.

I find the difference in font color and background between the interact box as a whole and the output area inside it annoying.

I would like there to be a str type option for the other controls, so I don't see quote marks in say button names.



---

archive/issue_comments_016561.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-11T02:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2449#issuecomment-16561",
    "user": "was"
}
```

Resolution: fixed
