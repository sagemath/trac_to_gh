# Issue 993: Pari's gp interpreter has built-in library search path, defeating Sage mechanisms

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-25 05:01:15

Assignee: was

Pari uses "-rpath" (or its equivalent) when building gp, to hardcode a library search path.  This search path is used before the $LD_LIBRARY_PATH set by Sage.  The hardcoded search path includes $SAGE_ROOT/local/lib:/usr/lib .

Normally, this is harmless (and perhaps slightly beneficial, since it means you can run $SAGE_ROOT/local/bin/gp directly, without having the SAGE environment variables set).  However, if you move your Sage installation tree, the hardcoded search path ensures that gp will search /usr/lib before the Sage libraries.  If your /usr/lib has libgmp or libpari-gmp libraries, these will be used instead of Sage's versions, leading (in my case) to one actual doctest failure (where the value of gp(log2), as tested in constants.py, was rounded correctly, rather than the slightly incorrect rounding enshrined in the doctest).


---

Comment by cwitty created at 2007-10-25 05:15:29

Changing assignee from was to cwitty.


---

Comment by cwitty created at 2007-11-01 06:03:57

I've put up a new Pari spkg at http://sage.math.washington.edu/home/cwitty/pari-2.3.2.p4.spkg that disables the use of rpath entirely.  (It's been tested on Linux, but not OS X.)  (This spkg also fixes #830.)


---

Comment by was created at 2007-11-01 07:13:33

I tested this on osx intel and osx ppc and it works.


---

Comment by mabshoff created at 2007-11-01 10:41:21

Resolution: fixed


---

Comment by mabshoff created at 2007-11-01 10:41:21

applied to 2.8.11.alpha0
