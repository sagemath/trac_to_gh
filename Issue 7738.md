# Issue 7738: remove Michael Abshoff as maintainer of any of spkg's

Issue created by migration from https://trac.sagemath.org/ticket/7738

Original creator: was

Original creation time: 2009-12-18 22:04:03

Assignee: tbd

CC:  was

Michael Abshoff is listed as maintainer of many spkg's, but he quit, so we need to delete his name from all of them:

```
optional/graphviz-2.16.1.p0.txt: * Michael Abshoff
optional/guppy-0.1.8.txt: * Michael Abshoff
optional/jsmath-image-fonts-1.4.p2.txt: * Michael Abshoff
optional/lrs-4.2b.p1.txt: * Michael Abshoff
optional/valgrind_3.3.1.txt: * Michael Abshoff
standard/boost-cropped-1.34.1.txt: * Michael Abshoff
standard/eclib-20080310.p7.txt: * Michael Abshoff
standard/ecm-6.2.1.p1.txt: * Michael Abshoff
standard/gap-4.4.10.p12.txt: * Michael Abshoff
standard/gdmodule-0.56.p6.txt: * Michael Abshoff
standard/gsl-1.10.p1.txt: * Michael Abshoff
standard/iml-1.0.1.p11.txt: * Michael Abshoff
standard/ipython-0.9.1.p0.txt: * Michael Abshoff
standard/libfplll-3.0.12.p0.txt: * Michael Abshoff
standard/libpng-1.2.35.txt: * Michael Abshoff
standard/mpfr-2.4.1.p0.txt: * Michael Abshoff 
standard/networkx-0.99.p1-fake_really-0.36.p1.txt: * Michael Abshoff
standard/ntl-5.4.2.p9.txt: * Michael Abshoff
standard/numpy-1.3.0.p2.txt:  Michael Abshoff
standard/pari-2.3.3.p5.txt: * Michael Abshoff
standard/polybori-0.6.3-20090827.txt: * Michael Abshoff
standard/pynac-0.1.9.p0.txt: * Michael Abshoff 
standard/python-2.6.2.p4.txt: * Included a fix by Michael Abshoff: patch posixmodule.c to avoid an
standard/scipy_sandbox-20071020.p4.txt: * Michael Abshoff
standard/scons-1.2.0.txt: * Michael Abshoff
standard/setuptools-0.6c9.p0.txt: * Michael Abshoff
standard/symmetrica-2.0.p4.txt: * Michael Abshoff
standard/tachyon-0.98beta.p10.txt: * Michael Abshoff
```



---

Comment by jsp created at 2010-01-10 22:14:24

Maybe cwitty falls in the same category?

Jaap


---

Comment by jason created at 2010-06-11 08:41:19

I would be very surprised if cwitty maintained any spkgs.  I remember him telling me that he refused to maintain spkgs, in fact.


---

Comment by leif created at 2010-07-11 00:22:08

I've removed _Michael Abshoff_ from the maintainer list in a new polybori-0.6.4.p2 package at #9472 (yet to be reviewed).

-Leif


---

Comment by leif created at 2010-07-28 14:53:49

Just came across http://wiki.sagemath.org/Sage_Spkg_Tracking (which is fairly out of date at some points btw); Michael Abshoff is still listed there as package maintainer of many packages, too...


---

Comment by leif created at 2010-07-28 16:41:39

I've now removed Michael Abshoff from all entries on the [SPKG tracking Wiki page](http://wiki.sagemath.org/Sage_Spkg_Tracking).


---

Comment by aapitzsch created at 2015-01-18 09:40:06

Changing status from new to needs_review.


---

Comment by chapoton created at 2015-01-18 16:16:23

missing one:

```
grep -r --include="*.txt" "* Michael Abshoff" .
./scons/SPKG.txt: * Michael Abshoff
./tachyon/SPKG.txt: * Michael Abshoff
./setuptools/SPKG.txt: * Michael Abshoff
./boost_cropped/SPKG.txt: * Michael Abshoff

```



---

Comment by aapitzsch created at 2015-01-18 19:34:38

Changing status from needs_review to needs_info.


---

Comment by aapitzsch created at 2015-01-18 19:34:38

Michael Abshoff is the only maintainer mentioned in `./boost_cropped/SPKG.txt`. Is it okay to have a spkg without maintainer or whom we could add as maintainer?


---

Comment by kcrisman created at 2015-01-21 04:06:33

The concept of maintainer is really a bit misleading anyway.  But yes, just go ahead and remove, it would be inaccurate to do otherwise.


---

Comment by chapoton created at 2015-01-21 08:48:47

Changing status from needs_info to needs_review.


---

Comment by chapoton created at 2015-01-21 08:48:47

if you agree, please set this to positive review
----
New commits:


---

Comment by jdemeyer created at 2015-01-21 09:15:43

Couldn't you just remove

```
## Maintainers

None
```

completely?


---

Comment by git created at 2015-01-21 09:19:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jdemeyer created at 2015-01-21 09:21:36

That was quick :-)


---

Comment by jdemeyer created at 2015-01-21 09:21:36

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-01-24 13:18:47

Resolution: fixed
