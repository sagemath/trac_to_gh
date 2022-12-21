# Issue 5116: update M4RI to newest upstream release

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-01-28 11:43:10

Assignee: mabshoff

Keywords: m4ri

A new version of M4RI is available. 

Release notes: http://bitbucket.org/malb/m4ri/wiki/M4RI-20090105


---

Attachment

* builds/checks/doctests clean on sage.math (Linux 64-bit)
 * builds/checks/doctests clean on bsd (OSX 32-bit)
 * builds/checks/doctests clean on iras (Linux IA-64)

Note that the SPKG has `make check` enabled.


---

Comment by malb created at 2009-01-28 23:40:01

* builds/checks/doctests clean on vbox-linux-32-bit (Linux 32-bit)


---

Comment by mabshoff created at 2009-02-03 23:18:19

The spkg can be found at

http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20090128.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-04 00:07:24

Spkg builds fine and passes make check also on OSX 10.4/PPC. The patch is also good to go and passes doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-04 00:08:29

Resolution: fixed


---

Comment by mabshoff created at 2009-02-04 00:08:29

Merged patch and spkg into Sage 3.3.alpha4.

Cheers,

Michael
