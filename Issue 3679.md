# Issue 3679: Range Slider Control

Issue created by migration from https://trac.sagemath.org/ticket/3679

Original creator: itolkov

Original creation time: 2008-07-19 06:27:37

Assignee: itolkov

Allows to select a range using a slider with two handles. Includes a jQuery patch.

Depends on #3599 and #3636.


---

Attachment


---

Attachment


---

Comment by jason created at 2008-07-21 22:26:37

Why did you need to patch jquery?  Would it be sufficient to upgrade to the newest jqueryui, which has slider controls with multiple sliders?  I'd rather not maintain a fork of jquery here.


---

Comment by itolkov created at 2008-07-28 20:00:34

I wouldn't need to generally, but #3735 makes it hard to do anything Javascript-related. The old version works for some reason.

Of course, the best thing for me to do here is fix #3735.


---

Comment by was created at 2008-07-29 18:58:54

REFEREE REPORT:

 * Add documentation to interact? that illustrates how to use range_slider.

 * Doing range_slider? gives help on slider instead of range_slider. 

 * I tried one example -- see http://sage.math.washington.edu/home/was/patches/3679.png and the displayed positions were different than the values of the variable when I first pressed shift enter.  Dragging the slider fixed this.

```
@interact
def _(t1=range_slider(2, 5, 1/5, (3,4), 'alpha')):
    print t1
    show(plot(sin,t1[0], t1[1]),xmin=t1[0])
```


 * In the above example, it seems like the order of the two sliders is reversed?


---

Attachment

Append to sage.patch


---

Comment by itolkov created at 2008-07-29 20:37:20

Points 1 and 2 are addressed.

3 and 4 - did you apply the extcode patch?


---

Comment by was created at 2008-07-29 23:24:40

> 3 and 4 - did you apply the extcode patch? 

No, I messed up and didn't apply it.  Now everything works perfectly and the improved docs are great!  Very positive review!


---

Comment by mabshoff created at 2008-07-31 01:23:02

Is the jQuery patch being upstreamed? Otherwise we will have problems once we upgrade to a newer release of jQuery.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-31 01:25:43

Resolution: fixed


---

Comment by mabshoff created at 2008-07-31 01:25:43

Merged all three patches in Sage 3.1.alpha0


---

Comment by jason created at 2008-08-12 21:16:42

I see that 3735 is fixed now.  Does that mean that the patches above to jquery should be reverted (as per the comment above)?
