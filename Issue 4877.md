# Issue 4877: [with spkg; needs review] update optional spkg to newest version of pyopenssl and get spkg into proper format

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-24 20:37:22

Assignee: mabshoff

The new spkg is here:  
    http://sage.math.washington.edu/home/was/patches/pyopenssl-0.8.spkg


---

Comment by mabshoff created at 2008-12-26 17:13:27

William,

the spkg at

 http://sage.math.washington.edu/home/mabshoff/spkgs/pyopenssl-0.8.p0.spkg

fixes various issues: Among them is a check for the openssl headers in $SAGE_LOCAL/include, which might or might not be too restrictive, i.e. since it doesn't allow the user to use the system openssl.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-26 17:14:03

This can also be resolved post 3.2.3 since it is unrelated to any code in the core of Sage.

Cheers,

Michael


---

Comment by was created at 2008-12-30 06:35:17

1. Could you change the error from having "openssl.spkg" to "openssl SPKG" or "openssl spkg".  I don't like "openssl.spkg" since it suggests that it is a filename, but there is no such file.   

I tested the spkg on OS X and it works well there. 

2. The repo needs to be checked in:

bsd:pyopenssl-0.8.p0 was$ hg status
M SPKG.txt
M spkg-install

3. I have to admit being slightly torn.  If one had openssl system-wide, then those headers would work fine for installing pyopenssl.  So I'm not sure we should force people to use openssl.spkg...  Or at least, it would be nice if there were some option, kind of like our SAGE_PORT=yes flag that would let users try to install an spkg damn the torpedoes, full speed ahead.   So the error could be:

"You do not have the optional openssl spkg installed, so building pyopenssl may fail.  You should either install the pyopenssl spkg, or set the environment variable SAGE_NODEPCHECKS."

Thoughts?

William


---

Comment by jdemeyer created at 2015-04-09 10:05:57

Obsolete


---

Comment by jdemeyer created at 2015-04-09 10:05:57

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2015-04-09 12:12:12

Resolution: fixed
