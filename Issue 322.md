# Issue 322: Have global code page for Notebook

Issue created by migration from https://trac.sagemath.org/ticket/322

Original creator: TimothyClemans

Original creation time: 2007-03-15 09:20:37

Assignee: boothby

Create a system for adding code to a notebook that can be executed by code in any cell in the worksheet. Before a chuck of code could become global the system would check it to make sure it does overwrite current SAGE functions, variables, and classes. Maybe the system could do that by executing the code and using the name space key in the various dictionaries to then see if a not found error is returned when name space called. It would be also be important for it to be easy to download a code package to be made global. I want this so I can make apps and use them from any cell in the notebook.


---

Comment by was created at 2007-03-21 22:46:42

This functionality is already provided in the SAGE notebook by putting #auto somewhere
in a cell.  Also, using %hideall one can even hide the global code.  

It's odd, because I've seen you use this functionality in your example sage notebook
applications, so you know about it.  Hmm.


---

Comment by was created at 2007-03-21 22:46:42

Resolution: invalid


---

Comment by TimothyClemans created at 2007-03-26 03:58:37

Changing status from closed to reopened.


---

Comment by TimothyClemans created at 2007-03-26 03:58:37

I said notebook not worksheet. I'm talking about writing a function or class in a global worksheet from I could use from anyother worksheet. #auto has nothing to do with global just writing a function in a cell makes that function global for the whole worksheet that the function is defined in.


---

Comment by TimothyClemans created at 2007-03-26 03:58:37

Resolution changed from invalid to 


---

Comment by kcrisman created at 2014-11-20 13:59:45

See https://github.com/sagemath/sagenb/issues/263 where I suggest that the easiest thing to do is have a 'global' (per user) DATA directory just like there is the per-worksheet DATA directory.


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets
