# Issue 8961: zope.testbrowser is included in sagenb but is no longer required

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2010-05-14 11:27:14

Assignee: jason, was

CC:  mpatel leif

`zope.testbrowser` is no longer needed by sagenb but is still listed as a requirement.


---

Comment by timdumol created at 2010-07-06 13:21:45

Removes zope.testbrowser as a dependency.


---

Comment by timdumol created at 2010-07-06 13:23:04

Changing priority from minor to major.


---

Comment by timdumol created at 2010-07-06 13:23:04

Changing status from new to needs_review.


---

Attachment

Now only Twisted (and its zope.interface, which is included in the Twisted spkg) is required by SageNB.


---

Comment by timdumol created at 2010-07-06 16:36:48

Removes an extra line.


---

Attachment

The package is at http://sage.math.washington.edu/home/timdumol/sagenb-0.8.1.spkg, and is the tentative package for #9430.


---

Comment by timdumol created at 2010-07-11 06:06:27

Resolution: fixed
