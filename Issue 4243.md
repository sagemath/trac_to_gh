# Issue 4243: [with spkg, needs review] pynac package version bump to 0.1.1

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-10-04 20:26:25

Assignee: mabshoff

CC:  was mhansen

Keywords: pynac, symbolics

There is a new version of pynac available. :)

This version allows setting custom python functions to perform evaluation, numeric evaluation, derivation, series expansion, etc. on symbolic functions.

The new package is available is here:

http://www.risc.jku.at/people/berocal/sage/pynac-0.1.1.spkg


---

Comment by burcin created at 2008-10-15 09:14:34

I updated the package at the address given in the description to correspond to the latest patch added to #4244.

Note that the package will break sage if the patches in #4244 are not applied, since libpynac will complain about missing symbols.


---

Comment by mabshoff created at 2008-10-18 12:26:08

Spkg looks good to me. I read Burcin's changes, but having another expert looks over this wouldn't hurt. Either way: damn the torpedoes :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-18 13:05:15

Merged in Sage 3.2.alpha0


---

Comment by mabshoff created at 2008-10-18 13:05:15

Resolution: fixed
