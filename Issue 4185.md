# Issue 4185: [with spkg, needs review] remove GNUisms from spkg-install of the jmol.spkg

Issue created by migration from https://trac.sagemath.org/ticket/4185

Original creator: mabshoff

Original creation time: 2008-09-24 08:27:24

Assignee: mabshoff

It boils down to:

```
 # Insert localize.in after first line of startup script.
-head -n 1 jmol > "$DIR/jmol"
+head -1 jmol > "$DIR/jmol"
 cat ../patches/localize.in >> "$DIR/jmol"
-tail -n +2 jmol >> "$DIR/jmol"
+tail +2 jmol >> "$DIR/jmol"
 check
```

The new spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha1/jmol-11.6.rc8.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-24 08:27:29

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-24 09:35:57

I get this:


```
****************************************************
Copying Jmol libraries...
Copying Jmol scripts...
tail: cannot open `+2' for reading: No such file or directory
Error.

real	0m0.377s
user	0m0.020s
sys	0m0.056s
sage: An error occurred while installing jmol-11.6.rc8.p0
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /opt/sage/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/opt/sage/spkg/build/jmol-11.6.rc8.p0 and type 'make'.
Instead type "/opt/sage/sage -sh"
in order to set all environment variables correctly, then cd to
/opt/sage/spkg/build/jmol-11.6.rc8.p0
(When you are done debugging, you can type "exit" to leave the
subshell.)
```



---

Comment by mabshoff created at 2008-09-24 09:56:28

Ok, I need to think about this an fix the problem. It looks like we cannot get something that works equally well on Solaris and on-Solaris.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-24 10:09:11

Ok, I am taking it back for now and will figure out what to do here.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-19 10:06:12

The latest working spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha0/jmol-11.6.rc8.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-19 10:06:12

Changing priority from major to critical.


---

Comment by mhansen created at 2009-01-19 10:15:34

Looks good to me.


---

Comment by mabshoff created at 2009-01-19 10:30:35

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 10:30:35

Merged in Sage 3.3.alpha0
