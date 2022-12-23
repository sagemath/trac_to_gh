# Issue 2177: [with patch; needs review] debianized jmol spkg

Issue created by migration from https://trac.sagemath.org/ticket/2177

Original creator: tabbott

Original creation time: 2008-02-16 04:33:51

Assignee: tabbott

For some reason the jmol directory shipped with SAGE does not contain the doc/ directory, which causes it to fail to build on Debian (or anything else, I'm pretty sure).  The current spkg-install script just copies the pre-built jmol jars, but presumably it'd be better to build our own (certainly Debian will want me to do this).

The doc/ directory is not large, so I'm not sure why it is missing, so I've obtained a copy of the doc directory from the jmol-11.5.2 upstream.  

I also move the "jmol/" directory to "src/" for compliance with our new spkg format standards.

I'll post a new SPKG later tonight.



---

Comment by was created at 2008-02-16 06:01:44

>  The current spkg-install script just copies the pre-built jmol 
> jars, but presumably it'd be better to build our own (certainly
> Debian will want me to do this).

We also *VERY MUCH* want easy-to-build-from source java code
for this package. Note that there is a jmol optional src package
here:

   http://sagemath.org/packages/optional/


---

Comment by tabbott created at 2008-02-16 06:50:32

JMol itself builds from source just fine if you install Sun Java (currently in Debian non-free) and ant.  It looks like the optional spkg has a bunch of dependencies that are shipped with the jmol spkg; so I guess that's what we're missing?  

The new spkg with Debian build support is available here:
http://sage.math.washington.edu/home/tabbott/jmol-11.5.2.p1.spkg


---

Comment by mabshoff created at 2008-02-16 17:53:06

I added a changelog entry to SPKG.txt, otherwise positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-16 17:53:25

Resolution: fixed


---

Comment by mabshoff created at 2008-02-16 17:53:25

Merged in Sage 2.10.2.alpha0


---

Comment by mabshoff created at 2008-02-16 18:17:44

Arrg, it was actually merged in Sage 2.10.2.alpha1
