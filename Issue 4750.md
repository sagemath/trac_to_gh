# Issue 4750: make it so sage -t foo.sage pulls in the preparsed version of all the code in foo.sage before doctesting foo.py; make it so "sage -t foo.py" has an option to pull in all code from foo.py before doctesting it.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-10 12:34:53

Assignee: mabshoff

CC:  ddrake abergeron




---

Comment by mderickx created at 2011-08-24 16:29:10

I'm not sure if this is a good idea to do by default. We also use the doctests to give examples for the endusers. Enabling this functionality by default makes it possible to write passing doctests which are not working in interactive sage sessions.


---

Comment by roed created at 2012-02-06 05:15:22

I don't understand what this ticket is suggesting.  I thought we already imported the classes and functions defined in a .sage file....


---

Comment by jdemeyer created at 2013-02-28 15:58:07

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-02-28 15:58:13

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-07 08:12:15

Resolution: worksforme
