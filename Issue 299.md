# Issue 299: make check and its analogues

Issue created by migration from https://trac.sagemath.org/ticket/299

Original creator: was

Original creation time: 2007-02-27 14:49:57

Assignee: was

Project:
Go through every spkg in the SAGE standard distribution and add a file

   spkg-check

that runs whatever the standard test program is for that package, assuming
spkg-install has already run successfully.  For example, for many programs
(e.g., gmp), this will just be:

  make check

or maybe "make test".

The program spkg-check should exit with a 0 code if and only if all tests pass.

Then when building SAGE, if one did something like

   export CHECK=1
   make

then all spkg-check's would get run along the way.  The build would take much longer,
but would be much more confidence inspiring. 




---

Comment by mabshoff created at 2007-08-23 11:31:13

The following come from #153 (which I have just closed as a duplicate)

It would also be nice to use the "-t" flag to run spkg-check when building packages:

```
  sage -i -t packagename.spkg
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-26 13:22:42

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-01-26 13:22:42

We now have `SAGE_CHECK` which in case of `SAGE_CHECK==yes` triggers the automated running of `{spkg-check`

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-26 14:40:51

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-30 07:08:43

As far as I know all spkgs now have spkg-checks if applicable. If any spkgs turns out to miss one we need to open a specific ticket for that spkg. Closed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-30 07:08:43

Resolution: fixed
