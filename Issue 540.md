# Issue 540: 3d: move all .jar files to an optional package;

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-31 19:10:57

Assignee: robertwb

IMPORTANT NOTE: I just realized that SAGE-2.8.3 includes some pre-compiled
java .jar files in the
     SAGE_ROOT/data/extcode/notebook/java/3d
directory.  If you're the sort of person who must compile everything from source, wait
for SAGE-2.9, when we'll do something about this problem (probably the only option
is to move these to an optional package since I do not want to require java to be installed
in order to build SAGE). 

This made the extcode .hg directory *HUGE*, so we're going to have to probably
revert to right before these were added.


---

Comment by was created at 2007-08-31 20:19:55

Moreover, it turns out that one of the java libraries isn't GPL compatible, so it definitely has to be moved out of the core of SAGE.   We'll just have to make it easy to install.


---

Comment by robertwb created at 2007-09-06 17:03:07

Resolution: fixed
