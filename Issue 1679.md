# Issue 1679: two documentation typos

Issue created by migration from https://trac.sagemath.org/ticket/1679

Original creator: was

Original creation time: 2008-01-04 09:20:27

Assignee: tba


```
Fabio Tonti to sage-devel
	
show details 12:56 AM (20 minutes ago)
	
	
	
Reply
	
	
The page numbers are numbers in the pdf version (in parentheses the printed page numbers)
I'm actually not sure about how to reference the page numbers...

page 175 (162): ** instead of ^;
the pyx example says: "sage: y(x) = x*sin(x**2)"
using the "**" is nice for python, but isn't Sage emphasizing to use "^" instead?

page 1843 (1830): ncols()... return number of "rows" instead of "coloumns";
the description for ncols() reads "number of rows" instead of "number of coloumns"



Best wishes, Fabio
```


NOTES:
   The first sin(x**2) above this from plot.py, and I agree with changing it to sin(x^2)

   The second listed problem seems like a clear mistake. 




---

Attachment


---

Comment by mabshoff created at 2008-01-13 14:57:21

Looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-13 14:58:26

Resolution: fixed


---

Comment by mabshoff created at 2008-01-13 14:58:26

Merged in Sage 2.10.alpha3.
