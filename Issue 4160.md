# Issue 4160: as of 2009-09-20 the polymake optional spkg fails to install

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-09-20 18:38:53

Assignee: mabshoff


```
server2`@`sage:~$ sage -i polynomial-2.2.p4
Installing polynomial-2.2.p4
Calling sage-spkg on polynomial-2.2.p4
You must set the SAGE_ROOT environment variable or
run this script from the SAGE_ROOT or 
SAGE_ROOT/local/bin/ directory.
polynomial-2.2.p4
Machine:
Linux sage 2.6.18-6-amd64 #1 SMP Sun Feb 10 17:50:19 UTC 2008 x86_64 GNU/Linux
Deleting directories from past builds of previous/current versions of polynomial-2.2.p4
/home/server2/sage/local/bin/sage-spkg: file polynomial-2.2.p4 does not exist
Attempting to download it.
http://www.sagemath.org//packages/optional/polynomial-2.2.p4.spkg --> polynomial-2.2.p4.spkg
[ ]
http://www.sagemath.org//packages/standard/polynomial-2.2.p4.spkg --> polynomial-2.2.p4.spkg
[ ]
http://www.sagemath.org//packages/experimental/polynomial-2.2.p4.spkg --> polynomial-2.2.p4.spkg
[ ]
http://www.sagemath.org//packages/archive/polynomial-2.2.p4.spkg --> polynomial-2.2.p4.spkg
[ ]
**********************************************************************
* Unable to download polynomial-2.2.p4
* Please see http://www.sagemath.org//packages for a list of valid
* packages or check the package name.
**********************************************************************
sage: Failed to download package polynomial-2.2.p4 from http://www.sagemath.org/

```



---

Comment by mabshoff created at 2008-09-20 20:30:12

This is a dupe of #3640. I have a fixed spkg-install that fixes this once and for all, but have not uploaded the spkg yet.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-20 20:30:12

Resolution: duplicate
