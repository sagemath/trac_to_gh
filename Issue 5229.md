# Issue 5229: [with patch, needs review] Jmol axes in the wrong place

Issue created by migration from https://trac.sagemath.org/ticket/5229

Original creator: jason

Original creation time: 2009-02-10 21:18:01

Assignee: was

As is, it appears that 3d plots are wrong, according to the jmol axes, because the jmol axes apparently don't default to being centered at the origin.  This patch makes the jmol axes centered at the origin.  To show the jmol axes, you still need to right-click on the jmol plot, select Style, then Axes.


---

Attachment


```
[1:28pm] ncalexan: jason|log: either it's not working or I don't get it.
[1:28pm] ncalexan: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2))
[1:28pm] ncalexan: gives me a smooth cup-like surface.
[1:28pm] ncalexan: But the value at x=0, y=0 (which is z=0) does not coincide with the jmol axes.
```



---

Comment by ncalexan created at 2009-02-10 22:05:08

After further IRC discussion, the proposed fix does not work in all situations.


---

Comment by mabshoff created at 2009-02-11 02:21:45

We don't give negative reviews any more, so change it to "needs work".

Cheers,

Michael


---

Comment by jason created at 2010-01-17 08:37:21

See #3862


---

Comment by olazo created at 2010-05-29 21:40:48

Also, and perhaps that merits a new ticket, the orientation of the axis is not what one would expect.

Normally 3d plots are shown with the positive x axis to the viewer's left, the positive y axis to the right, and the positive z upwards. Currently it is: negative y axis to the left, positive x to the right, and positive z upwards.
