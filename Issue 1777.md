# Issue 1777: jmol up/down metaphor confusing in the "View" right-click menu

Issue created by migration from https://trac.sagemath.org/ticket/1777

Original creator: jason

Original creation time: 2008-01-14 17:55:53

Assignee: was

I noticed a potentially confusing thing in the totally awesome 3d 
graphics we now have with jmol.

sage: arrow3d((0,0,0),(1,1,1))

draws a very nice-looking 3d arrow in a bounding cube.  When I 
right-click on the graphic and choose "View | front", it swings the 
viewpoint around so that I'm looking at the *top* of the original cube 
(so that I'm looking in the direction of the negative z-axis).  I 
realize that the standard computer graphics viewpoint has the z-axis 
coming out of the monitor, so "front" is a valid label for this position 
in that sense, but it can be confusing to students who would have said 
that what is labeled as the "front" position is actually showing the top 
of graph.  I imagine that it would be even more confusing to calc 3 
students that the labeled "top" position is looking in the negative 
y-axis direction *with the positive z pointing down*.

The positions and actual viewing directions are thus:

"front" = looking down negative z-axis, positive y-axis pointing up
"back" = looking down positive z-axis, positive y-axis pointing up

"left" = looking down positive x-axis, positive y-axis pointing up
"right" = looking down negative x-axis, positive y-axis pointing up

"top" = looking down negative y-axis, positive z-axis pointing *down*
"bottom" = looking down positive y-axis, positive z-axis pointing up

I think it would be less confusing if the View menu just listed viewing 
directions instead of assigning a "up" and "down" metaphor that can 
change depending on if you are doing math or doing computer science.

Jason


---

Comment by jason created at 2008-07-24 22:26:03

See #2873 for how to fix this.


---

Comment by jason created at 2009-02-14 10:04:20

Changing status from new to assigned.


---

Comment by jason created at 2009-02-14 10:04:20

Changing assignee from was to jason.


---

Comment by mabshoff created at 2009-02-14 14:50:11

Resolution: fixed


---

Comment by mabshoff created at 2009-02-14 14:50:11

Fixed via #2873 in Sage 3.3.rc1.

Cheers,

Michael
