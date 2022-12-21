# Issue 7015: [with patch; needs review] cygwin port -- ratpoints -- don't build executable since we don't need it (and fails on cygwin)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-25 22:15:09

Assignee: mabshoff

the ratpoints spkg builds an executable we just throw away.  On Cygwin it fails though changing the link order from

```
	    -lgmp -lm -lratpoints
	to
	    -lm -lratpoints -lgmp
```

would fix the problem. 


---

Comment by was created at 2009-09-25 22:17:19

Here is the spkg:

  http://sage.math.washington.edu/home/wstein/patches/ratpoints-2.1.2.p3.spkg


---

Comment by certik created at 2009-09-25 22:24:44

The only change in the spkg package is:


```
-make
+make libratpoints.a
```


since this is all that is needed, it's +1 from me.


---

Comment by mvngu created at 2009-09-28 07:26:29

Here's an updated spkg

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/ratpoints-2.1.2.p4.spkg

Changes from William's version include:

 * Remove the junk files `spkg-install~` and `SPKG.txt~`.
 * Make `spkg-install` executable using "`chmod +x spkg-install`".
 * Use about 75 characters for each line in the file `SPKG.txt`. Any longer than that and it would be difficult to read on a standard terminal width, i.e. 80 characters wide.


---

Comment by mhansen created at 2009-10-16 08:53:26

Looks good to me.  I included the changes that Minh made to William's spkg and left the version at p3.


---

Comment by mhansen created at 2009-10-16 08:53:26

Resolution: fixed
