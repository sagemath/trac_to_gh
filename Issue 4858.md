# Issue 4858: parenthesis badly handled in notebook sheet titles

Issue created by migration from https://trac.sagemath.org/ticket/4858

Original creator: schilly

Original creation time: 2008-12-23 13:16:47

Assignee: boothby

CC:  phil-sage@teuwen.org

[from notebook bug reporter](http://spreadsheets.google.com/ver?key=pCwvGVwSMxTzT6E2xNdo5fA&t=1230037542957000&pt=1230037522957000&diffWidget=true&s=AJVazbXknPq-Bx-rR5kIauR1GyZU7hV7yg)


```
Hi,

I had some notebook sheets with parenthesis in the title with Sage v3.1.1
But since I upgraded to 3.2.1 the parenthesis are escaped, even multiple times, every time the sheet is opened again.
To reproduce the problem:
Create new sheet "Untitled"
Rename it as "Untitled (test)"
Close it, it appears properly in the list
Open it again -> "Untitled &amp;#40;test&amp;#41;"
So the bug was introduced somewhere between 3.1.1 and 3.2.1
```



---

Comment by mabshoff created at 2008-12-23 13:31:35

Harald,

this looks like a dupe of #4851, so I would suggest we close this.

Cheers,

Michael


---

Comment by mhansen created at 2009-01-19 08:06:17

Resolution: duplicate


---

Comment by mhansen created at 2009-01-19 08:06:17

Yep, I'll mark this as a duplicate.  There is a fix at #4851.
