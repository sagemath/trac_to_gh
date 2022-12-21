# Issue 1930: Sage 2.10.1.alpha2: R is broken for parallel make, rpy is broken for fresh installs

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-26 08:05:42

Assignee: mabshoff

subject says it all, a updated spkg is coming.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-26 10:44:41

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc0/r-2.6.1.p11.spkg

fixed the issue. There is a spkg-check failure, which is now #1936.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-26 10:45:16

Resolution: fixed


---

Comment by mabshoff created at 2008-01-26 10:45:16

Merged in Sage 2.10.1.rc0


---

Comment by mabshoff created at 2008-01-26 11:05:58

Another updated r.spkg (which is also merged in 2.10.1.rc0) is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc0/r-2.6.1.p12.spkg

It removes the tar.gzs in Recommended and shrinks the spkgs by 3 mb. Once we build the recommended extensions we need to add the tar.gzs back.

Cheers,

Michael
