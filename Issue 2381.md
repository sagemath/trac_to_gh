# Issue 2381: plot_vector_field can't plot arbitrary vector fields

Issue created by migration from Trac.

Original creator: edrex

Original creation time: 2008-03-04 04:15:15

Assignee: was

Keywords: plot vector quiver

Is the a way to produce "quiver plots" for 2d vector fields? plot_vector_field should accept functions of two parameters, but doesn't:

Usage example:

```
sage: vf1 = plot_vector_field((lambda x:sin(x), lambda y:cos(y)), (-3,3), (-3,3))
```


With 2 arguments:

```
sage: plot_vector_field((lambda x,y:y,lambda x,y:(cos(x)-2)*sin(x)),(-pi,pi),(-pi,pi))
<type 'exceptions.TypeError'>: <lambda>() takes exactly 2 arguments (1 given)
```


See http://groups.google.com/group/sage-support/browse_thread/thread/13e52e07c7d7a7f9/ca8623384c7a1f55


---

Comment by was created at 2008-03-04 04:46:15

Changing type from defect to enhancement.


---

Comment by mhansen created at 2008-03-04 04:56:23

Having functions that take two arguments is the right thing to do.  I have a patch that I'll post here in a second.


---

Comment by mhansen created at 2008-03-04 04:56:23

Changing status from new to assigned.


---

Comment by mhansen created at 2008-03-04 04:56:23

Changing assignee from was to mhansen.


---

Comment by jason created at 2008-03-04 06:22:51

mhansen and I independently came up with the same solution in about the same time.


---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2008-03-05 06:04:31

Merged in Sage 2.10.3.rc2


---

Comment by mabshoff created at 2008-03-05 06:04:31

Resolution: fixed
