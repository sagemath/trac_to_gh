# Issue 1533: Finish converting java3d to an spkg

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-12-16 07:19:52

Assignee: was

The java3d code (with the associated, rather large) Sun jar files is now duplicated in extcode and a java3d spkg. The new code from #1473 needs to be merged into the spkg, which installs files in $SAGE_LOCAL/java and the notebook/command line should use the files from there (not extcode). 


---

Comment by robertwb created at 2007-12-16 07:22:42

Changing status from new to assigned.


---

Comment by robertwb created at 2007-12-16 07:22:42

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2007-12-16 07:22:42

New spkg up at http://sage.math.washington.edu/home/robertwb/spkgs/


---

Attachment


---

Comment by rlm created at 2007-12-22 18:58:49

spkg and patch merged in 2.9.1 rc0


---

Comment by rlm created at 2007-12-22 18:58:49

Resolution: fixed
