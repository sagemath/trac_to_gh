# Issue 5509: Make a parametric_plot.pyx docstring a raw string because of a \times in it.

Issue created by migration from https://trac.sagemath.org/ticket/5509

Original creator: jason

Original creation time: 2009-03-13 14:39:51

Assignee: was

The following documentation looks weird because the \t in the \times in the string gets converted to a tab.


```
sage: p.triangulate?
Type:		builtin_function_or_method
Base Class:	<type 'builtin_function_or_method'>
String Form:	<built-in method triangulate of sage.plot.plot3d.parametric_surface.ParametricSurface object at 0xbb0cdec>
Namespace:	Interactive
Docstring:
    
            Call self.eval() for all (u,v) in urange 	imes vrange
            to construct this surface. 

```



---

Attachment


---

Comment by jason created at 2009-03-13 14:44:47

This is a trivial patch, I know, but it was also to demonstrate the development process to a student.


---

Comment by mabshoff created at 2009-03-20 20:35:06

Merged in Sage 3.4.1.alpha0.

Cheeers,

Michael


---

Comment by mabshoff created at 2009-03-20 20:35:06

Resolution: fixed
