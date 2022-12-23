# Issue 9777: Addition of LaTeX and better support of SI prefixes on units module

Issue created by migration from https://trac.sagemath.org/ticket/9778

Original creator: cousteau

Original creation time: 2010-08-21 20:42:35

Assignee: burcin

CC:  was eviatarbach

Keywords: latex, SI prefixes, units

Since maybe the developers are reluctant to implement the "metrology" module I submitted in #9763, when there's already a "units" module that has the same purpose, I'm trying to port the `LaTeX` capabilities to the already existing "units" module.

TO DO: Complete the latexdict list of units and `LaTeX` representation (if a unit isn't there, its symbol will be replaced by its name)

Also, I'm implementing an easier way to use `SI` prefixes on the units module. The patch I submitted in #9759 wasn't very intuitive (you had to type "units.length.meter.kilo"), partly because I didn't know very well how did that module work. This new version allows you to simply type "units.length.kilometer" (even if it's not tab-completed) and it will do the rest.


---

Attachment

Adds `LaTeX` symbols and `SI` prefixes to the units module


---

Comment by cousteau created at 2010-08-21 20:47:05

Changing status from new to needs_work.


---

Comment by kcrisman created at 2012-05-26 07:25:01

Is the "todo" necessary, or could it be postponed to another ticket?


---

Comment by cousteau created at 2012-05-28 14:19:17

Well, `latexdict` only contains a few units (10) and prefixes (5) so that it worked as an example; it would need to be completed with the names of all SI units and prefixes, at least for the LaTeX representation part.

By the way, I made this patch 2 years ago so I remember pretty little of it.


---

Comment by kcrisman created at 2012-05-28 15:51:40

This supersedes #9759.

If someone wanted to complete this, they'd just have to make sure they implemented all the SI units etc. that Sage supports (see the 'todo' above).


---

Comment by kcrisman created at 2012-05-28 15:51:57

Changing keywords from "latex, SI prefixes, units" to "latex, SI prefixes, units, sd40.5".
