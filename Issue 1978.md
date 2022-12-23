# Issue 1978: update python-gnutls

Issue created by migration from https://trac.sagemath.org/ticket/1978

Original creator: yi

Original creation time: 2008-01-30 04:40:18

Assignee: mabshoff

python-gnutls needs to be updated to reflect the api changes in gnutls-2.2.1. 

An experimental spkg can be found here:

http://sage.math.washington.edu/home/yqiang/python-gnutls-1.1.4.p1.spkg


---

Comment by yi created at 2008-01-30 04:41:07

Changing assignee from mabshoff to yi.


---

Comment by yi created at 2008-01-30 06:00:37

There is at least one error with the spkg, namely that it needs to point to the newer gnutls libraries (ending in .23), AFAIK mabshoff fixed that already.


---

Comment by mabshoff created at 2008-01-30 06:50:49

Ok, the spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc3/python_gnutls-1.1.4.p2.spkg

should fix all known issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-30 07:03:30

There is also an updated gnutls.spkg that makes sure the old `*[dylib|so].13.*` are gone:

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc3/gnutls-2.2.1.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-30 08:09:17

Builds fine on OSX and start with `-notebook` as well as `-inotebook`. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-30 09:41:41

Resolution: fixed


---

Comment by mabshoff created at 2008-01-30 09:41:41

Merged in Sage 2.10.1.rc3. This ticket should be reopened if any problems pop up.
