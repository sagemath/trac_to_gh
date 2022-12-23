# Issue 5230: implement boundary_style parameter for parametric 3d plots

Issue created by migration from https://trac.sagemath.org/ticket/5230

Original creator: was

Original creation time: 2009-02-10 22:12:41

Assignee: was

Basically make it easy to create plots like this but in 1 line:

```
u, v = var('u,v')
G = parametric_plot3d((cos(u), sin(u) + cos(v), sin(v)), (u, 0, pi), (v, 0, pi), opacity=0.9)    
C = parametric_plot3d((cos(0), sin(0) + cos(v), sin(v)), (v, 0, pi), color='black', thickness=2)    
D = parametric_plot3d((cos(pi), sin(pi) + cos(v), sin(v)), (v, 0, pi), color='black', thickness=2)
E = parametric_plot3d((cos(u), sin(u) + cos(0), sin(0)), (u, 0, pi), color='black', thickness=2)    
F = parametric_plot3d((cos(u), sin(u) + cos(pi), sin(pi)), (u, 0, pi), color='black', thickness=2)
K = G + C + D + E + F
```


Input would probably be like this (dictionary):

```
u, v = var('u,v')
parametric_plot3d((cos(u), sin(u) + cos(v), sin(v)), (u, 0, pi), (v, 0, pi),
      boundary_style={'color':'black', 'thickness':2})    
```



---

Comment by wcauchois created at 2009-02-12 00:45:07

Changing status from new to assigned.


---

Comment by wcauchois created at 2009-02-12 00:45:07

Changing assignee from was to wcauchois.


---

Attachment


---

Comment by was created at 2009-02-25 23:00:19

REFEREE REPORT:

It works perfectly. 

 * Add to "        boundary_style -- (default: None, no boundary) a dict that describes
                          how to draw boundaries of regions"
that the dict just gives the options that are passed to the line3d command.

 * Put a space after the doctest:

```
 	105	        sage: parametric_plot3d((cos(u), sin(u) + cos(v), sin(v)), (u, 0, pi), (v, 0, pi), boundary_style={"color": "black", "thickness": 2}) 
 	106	    Any options you would normally use to specify the appearance of a curve are valid 
 	107	    as entries in the boundary_style dict. 
```


I attached a patch that makes these trivial changes.  With this, positive review.

NOTE: This patch will have to be rebased for 3.4.alpha because of the ReST transition.  It applies fine to 3.3 though.


---

Attachment

This needs to be rebased, as mentioned in the comment:

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.alpha1/devel/sage$ patch -p1 < trac_5230_boundary-style.patch 
patching file sage/plot/plot3d/parametric_plot3d.py
Hunk #1 succeeded at 10 with fuzz 2 (offset 1 line).
Hunk #2 FAILED at 39.
Hunk #3 FAILED at 100.
Hunk #4 succeeded at 492 (offset 106 lines).
Hunk #5 succeeded at 537 with fuzz 2 (offset 107 lines).
Hunk #6 succeeded at 565 (offset 108 lines).
```


So I am changing the summary properly so I won't find it out that way again :)

Cheers,

Michael


---

Attachment


---

Comment by wcauchois created at 2009-04-07 17:50:10

Please apply ONLY trac5230-rebased.patch! It should apply fine to Sage 3.4 now.


---

Comment by mabshoff created at 2009-04-09 08:12:36

Resolution: fixed


---

Comment by mabshoff created at 2009-04-09 08:12:36

Merged in Sage 3.4.1.rc2.

Cheers,

Michael
