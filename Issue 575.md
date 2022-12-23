# Issue 575: make building SAGE on cygwin stop fast and clean

Issue created by migration from https://trac.sagemath.org/ticket/575

Original creator: was

Original creation time: 2007-09-03 13:53:44

Assignee: was


```
Building SAGE with Cygwin is absolutely definitely not supported,
and will not work.  The only way to run SAGE on Windows, is via
VMware (or Virtual PC or some other virtualization). 

I'll make a ticket for making it so that the SAGE build scrip very very
clearly indicates that it won't work on Cygwin right at the beginning,
to avoid such confusion in the future. 

NOTE: SAGE used to support Cygwin several months ago (around March
2007), so you may have seen some old documentation about this.
```


This will be easy to fix by modifying spkg/base/prereq-0* to check for the Cygwin UNAME.




---

Comment by mabshoff created at 2007-10-21 19:06:55

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-10-21 19:06:55

Changing status from new to assigned.


---

Comment by was created at 2007-11-03 22:55:31

I fixed this by changing prereq-0.3-install, and actually did a bunch of other
minor cleanup to the base directory, including creating an .hg repo there.


---

Comment by was created at 2007-11-03 22:55:31

Resolution: fixed


---

Comment by was created at 2007-11-03 22:56:03

Here is the interesting part of the script:


```

if [ "$SAGE_PORT" = "" ]; then
   if [ `uname | sed -e 's/WIN.\+/WIN/'` = "CYGWIN" ]; then
      echo "Building or using SAGE with Cygwin is absolutely definitely"
      echo "not supported, and will definitely not work.  The only way"
      echo "to run SAGE on Windows, is via VMware (or Virtual PC or "
      echo "some other virtualization system such as andLinux)."
      echo "NOTE: SAGE used to support Cygwin several months ago (around March"
      echo "2007), so you may have seen some old documentation about this."
   fi
fi

```

