# Issue 3599: Longer slider and labels on sliders

Issue created by migration from https://trac.sagemath.org/ticket/3599

Original creator: itolkov

Original creation time: 2008-07-08 00:28:26

Assignee: itolkov

Slider update:

 * Sliders are now version 3, which is similar to current version 1, but longer

 * Label to the right of slider containing the current slider value (string representation), which is updated dynamically

 * User can hide label with "display_value=False".


---

Attachment


---

Comment by itolkov created at 2008-07-18 00:05:11

Changing priority from minor to major.


---

Comment by jason created at 2008-07-21 22:01:48

Where does the png file go?


---

Comment by jason created at 2008-07-21 22:11:21

Answering my question, it goes in:

$SAGE_ROOT/data/extcode/notebook/javascript/jqueryui/themes/flora/i/slider-bg-3.png

This patch seems to do what it claims and looks like reasonable code, looks nice, and doctests pass in sage/server/notebook/*.py

+1


---

Comment by was created at 2008-07-29 18:38:17

the image of the slider


---

Attachment

I replaced the png by a proper patch.


---

Comment by was created at 2008-07-29 18:41:50

I give this another positive review, by the way.  Very good.


---

Comment by mabshoff created at 2008-07-31 01:19:34

Merged trac3599_sage_1.patch and trac3599_extcode_1.patch in Sage 3.1.alpha0. trac3599_extcode_2.patch is empty. You need to add a git style patch or reattach the png.

Cheers,

Michael


---

Attachment

Here's the png again.


---

Comment by mabshoff created at 2008-07-31 21:51:06

Resolution: fixed


---

Comment by mabshoff created at 2008-07-31 21:51:06

Merged slider-bg-3.png in Sage 3.1.alpha0. Thanks Igor for the png. In the future please export a git style patch in case binaries are involved.

Cheers,

Michael
