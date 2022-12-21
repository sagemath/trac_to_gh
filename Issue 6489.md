# Issue 6489: [with patch, work in progress ...] Allow Sage to call R (statistics)

Issue created by migration from Trac.

Original creator: sjanke

Original creation time: 2009-07-08 20:27:49

Assignee: mhampton

Keywords: statistics, R,

Here we have the start of a "bridge" between Sage and R.

The R c language api is used to call R functions from Python.

This code mostly handles converting between Sage (Python) and R types.

The way it works is Python calls the callTypedArgs function defined in this module, passing in the name of the R function to call, a string specifying types of the parameters the function expects and what the function returns, then a list of Python Objects (such Sage integers, or vectors or matrices) for the parameters. R_bridge then creates the equivalent simple expressions in R for the passed Python objects, calls the given function in R, and then converts back from the returned R simple expression to a Python Object.

The way to expose R's functionality nicely in Sage using this is then to create a Sage file (like statistics.py) that uses R_bridge to call R functions. This file would wrap up the ugly parameter and return type specifier string.


---

Attachment


---

Attachment


---

Attachment


---

Comment by sjanke created at 2009-07-08 20:36:00

Changing priority from major to minor.


---

Comment by mhansen created at 2013-07-23 15:01:05

Resolution: invalid


---

Comment by mhansen created at 2013-07-23 15:01:05

I think duplicating the work in rpy (which is quite effective) isn't a good plan.
