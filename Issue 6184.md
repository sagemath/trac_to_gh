# Issue 6184: mesh=True and dots=True don't work for 3D plots

Issue created by migration from https://trac.sagemath.org/ticket/6184

Original creator: wcauchois

Original creation time: 2009-06-02 08:30:53

Assignee: tbd

Just like the title says; the options noted do not have any effect on 3D plots in Sage 4.0.rc0.

For example, the command

```
plot3d(lambda x,y: exp(x+y*I).real(), (-2, 2.4), (-3, 3), mesh=True)
```

Should display a 3D plot with mesh lines drawn in. However, the result does not have mesh lines.

(This bug was discussed at [this forum thread](http://groups.google.com/group/sage-devel/browse_thread/thread/ac3ae56aa896826f).)

I will attach a patch that fixes the issue.


---

Attachment

based on sage 4.0.rc0


---

Comment by wcauchois created at 2009-06-02 08:33:33

Does anyone know where this functionality was broken, and what the code was like before?


---

Comment by mhampton created at 2009-06-02 12:16:18

This seems to fix the problem and not cause others in the limited testing I have done.  Since it is a surgical-strike type of patch I feel good about giving it a positive review - this is basically two extra lines that correctly pass on an option.


---

Comment by mhampton created at 2009-06-02 12:16:18

Changing component from algebra to graphics.


---

Comment by mhampton created at 2009-06-02 12:16:18

Changing assignee from tbd to was.


---

Comment by mhansen created at 2009-06-03 18:24:11

Resolution: fixed


---

Comment by mhansen created at 2009-06-03 18:24:11

Merged in 4.0.1.rc0.
