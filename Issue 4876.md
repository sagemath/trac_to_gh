# Issue 4876: replace the two kash3 optional spkg's by a single optional spkg that works on both Linux and OS X, and gives a graceful message on other systems

Issue created by migration from https://trac.sagemath.org/ticket/4876

Original creator: was

Original creation time: 2008-12-24 19:55:15

Assignee: mabshoff




---

Comment by was created at 2008-12-24 20:13:57

Also:
   * create an hg repo in the spkg
   * make the spkg-install script way more robust (more checks for error conditions)
   * put the SPKG.txt in the format described here: http://wiki.sagemath.org/SPKG_Audit


---

Comment by was created at 2008-12-24 20:15:11

To test this, you can do

  sage -i http://sage.math.washington.edu/home/was/patches/kash3-2008-07-31.spkg

on both a linux and OS X box.  Then do "sage -kash" to see if it works.  Then look do 

```
tar xf SAGE_ROOT/spkg/optional/kash3-2008-07-31.spkg
cd kash3-2008-07-31
# look around
```



---

Comment by was created at 2008-12-24 20:19:36

By the way, I checked and the OS X binary is "universal", in that it works on both PowerPC and Intel OS X 10.5 boxes.


---

Comment by was created at 2008-12-24 20:21:28

(This spkg won't work on itaniums correctly yet.  But it is still a massive improvement over the current kash spkg's.)


---

Comment by was created at 2008-12-24 20:42:04

NOTE: I've already posted this to the package repo, so all this needs is an official review.  I posted this, since it's clearly better than the kash spkg I made 3 years ago, which was all that was there.


---

Comment by jsp created at 2008-12-24 22:04:06

The package installed on Fedora 9 without problems.

The examples of

[http://www.math.tu-berlin.de/~kant/KASH/pdf/kash3intro.pdf](http://www.math.tu-berlin.de/~kant/KASH/pdf/kash3intro.pdf)

work.

Looks good to me (the linux binaries), I don't have a mac to test.

Jaap


---

Comment by mabshoff created at 2008-12-26 17:58:31

For the record: The spkg has already been uploaded to the optional spkg repo.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-01 05:26:10

Ok, since no one has complained let's change this to a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-01 05:27:05

Resolution: fixed


---

Comment by mabshoff created at 2009-04-01 05:27:05

Merged in the Sage 3.4.1 release cycle (at least officially :))

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-01 05:27:05

Changing component from packages to optional packages.
