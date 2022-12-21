# Issue 8959: interact layouts with arbitrary html

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-05-13 09:05:55

Assignee: itolkov, jason

CC:  was timdumol mhampton

The layout argument of an interact should also accept a string, maybe a string in the format of either standard python formats (i.e., "<table><tr><td>{a}</td></tr></table>"), or using the simple template classes that come with python (i.e., "<table><tr><td>$a</td></tr></table>").  Whichever convention is chosen, the string is given the dictionary of {'variable name': 'html for variable control'}, or maybe {'variable name': {'label': HTML label, 'control': 'html for control'}}, so you could do "<td>{a.label}</td><td>{a.control}</td>".


---

Comment by jason created at 2010-05-13 09:07:17

See #7379 for the initial implementation of this feature.


---

Comment by jason created at 2010-05-14 03:17:37

Okay, the attached patch lets you specify controls on each side, as well as the width of the interact.  The following code gives the interact in the screenshot attached.


```

var('x')
`@`interact(layout=dict(top=[['f'],['r','plot_points']], bottom=[['color','thickness'],['adaptive_recursion','adaptive_tolerance']], left=[['gridlines'],['fill'],['frame'],['axes']], right=[This is the Trac macro *'linestyle'* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#'linestyle'-macro)))
def plot_example(f=sin(x^2),r=range_slider(-5,5,step_size=1/4,default=(-3,3)), 
                 color=color_selector(widget='colorpicker'),
                 thickness=(3,(1..10)),
                 adaptive_recursion=(5,(0..10)), adaptive_tolerance=(0.01,(0.001,1)),
                 plot_points=(20,(1..100)),
                 linestyle=['-','--','-.',':'],
                 gridlines=False, fill=False,
                 frame=False, axes=True
                 ):
    show(plot(f, (x,r[0],r[1]), color=color, thickness=thickness, 
                 adaptive_recursion=adaptive_recursion,
                 adaptive_tolerance=adaptive_tolerance, plot_points=plot_points,
                 linestyle=linestyle, fill=fill if fill else None), 
                 gridlines=gridlines, frame=frame, axes=axes)
```



---

Attachment


---

Comment by rbeezer created at 2010-05-14 04:45:11

Jason,

Nice work - this will improve the utilization of screen real estate.

Was there a patch to include?

Rob


---

Comment by jason created at 2010-05-14 07:14:23

for SAGENB repository


---

Comment by jason created at 2010-05-14 07:15:15

Changing status from new to needs_review.


---

Attachment

This patch depends on #7379 and extends the functionality there.


---

Comment by jason created at 2010-05-16 04:46:40

apply on top of previous patches


---

Attachment

The handle-update-button patch takes care of the auto_update problem mhampton pointed out on #7379.  At least, I think it does; the feature seems to work.  I don't know how to doctest the notebook after I've done "sage -python setup.py develop" to work on notebook files.  When I try to run sage -t, there's just an error about importing jsmath.


---

Comment by mhampton created at 2010-05-16 13:57:24

You can do:

sage -t -sagenb

to test the notebook.  I'll try to check the patch out today.


---

Comment by mhampton created at 2010-05-16 14:31:35

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2010-05-16 14:31:35

Tests pass now and a variety of interacts from the wiki work fine as well.  

It would be nice if there was an easy way to pack things in various ways.  It also makes me desire an option for slider and range_slider to change their lengths, but that's for another day.


---

Comment by timdumol created at 2010-07-11 06:06:38

Resolution: fixed
