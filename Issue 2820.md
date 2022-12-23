# Issue 2820: notebook -- turn off the jsmath warning

Issue created by migration from https://trac.sagemath.org/ticket/2820

Original creator: was

Original creation time: 2008-04-06 04:02:16

Assignee: boothby

I think the plan should be 
  1. get rid of it; 
  2. make much better jsmath instructions;
  3. put something like it back (that doesn't suck)

Also, we could support official jsmath image fonts (150MB) as an optional package.


---

Comment by jason created at 2008-04-06 04:06:16

The jsmath image fonts are already an optional package.  See #1971.


---

Comment by was created at 2008-04-08 17:03:00

The attached patch does the following:
  * turns off the jsmath warning
  * greatly improves how the input text area gets autoresized
  * fixes all cursor/tab location bugs from #2840
  * makes some small cosmetic changes to finish #2852
  * restores backspace in empty cell to delete functionality (to avoid confusion)
  * turns on javascript compression so main.js is 1/3rd the size, which means loading sage worksheets will be faster. 
  * get rid of lisp from the list-of-systems menu, since it doesn't work.


---

Attachment

This patch also fixes #2800.

Cheers,

Michael


---

Comment by boothby created at 2008-04-08 18:12:19

Works for me.


---

Comment by mabshoff created at 2008-04-08 18:13:09

Merged in Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-08 18:13:09

Resolution: fixed
