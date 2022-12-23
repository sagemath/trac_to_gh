# Issue 5903: Remove dist directories from Sage distribution

Issue created by migration from https://trac.sagemath.org/ticket/5903

Original creator: tabbott

Original creation time: 2009-04-26 06:03:37

Assignee: tabbott

CC:  leif

The dist/ directories currently shipped in various Sage .spkg's have resulted in confusion for people a few times.

These directories are no longer used (the Debian packaging for these things are now maintained in my own git repositories).  So, they should be deleted before anyone else gets confused.  The list of packages needing this treatment is as follows:


```
cddlib-094f
eclib-20080310.p7
extcode-3.4.1
flint-1.2.4.p1
flintqs-20070817.p4
gap-4.4.10.p11
genus2reduction-0.3.p5
gfan-0.3.p4
givaro-3.2.13rc2
iml-1.0.1.p11
jmol-11.6.16.p0
lcalc-20080205.p2
libfplll-2.1.6-20071129.p5
libm4ri-20090128
linbox-1.1.6
ntl-5.4.2.p6
palp-1.1.p1
polybori-0.5rc.p6
rubiks-20070912.p8
scipy_sandbox-20071020.p3
singular-3-0-4-4-20080711.p4
symmetrica-2.0.p2
sympow-1.018.1.p6
tachyon-0.98beta.p8
zn_poly-0.9.p0
```


Since this is a huge list, we probably want to handle this issue by just deleting the dist/ directories the next time each of these .spkg files is updated.


---

Comment by ddrake created at 2009-09-25 02:58:00

As part of #7005, I'll ask that the dist/ be removed from the Singular spkg.


---

Comment by mvngu created at 2010-01-25 13:07:48

Ticket #7109 removes "dist/" from cddlib.


---

Comment by mvngu created at 2010-01-25 13:13:14

Ticket #7820 removes "dist/" from gfan.


---

Comment by leif created at 2010-09-03 23:05:02

I've "informed" the Tachyon and the (three) Lcalc upgrade/update tickets...

Some of the packages in the list have meanwhile been upgraded or updated; I'm not sure which of them actually removed the `dist/` directory. (I think I did in the M4RI and/or PolyBoRi spkgs.)


---

Comment by leif created at 2010-09-03 23:19:42

Replying to [comment:4 leif]:
> I've "informed" the Tachyon and the (three) Lcalc upgrade/update tickets...

And that of genus2reduction (#9591).


---

Comment by mvngu created at 2010-10-18 09:14:30

Ticket #9562 removes `dist/` from libm4ri.


---

Comment by vbraun created at 2011-01-11 09:37:04

Ticket #5281 removes the dist directory from tachyon.


---

Comment by mariah created at 2011-05-19 19:16:32

Code to identify packages with dist directory


```/usr/bin/python

# search spkgs for dist directory 
#
# assumes you start in spkg/standard

import sys,os,subprocess

cur = os.getcwd()
print cur

for filename in os.listdir("."):
  if filename.endswith(".spkg"):
    val = subprocess.check_output(["file", filename])
    if val.find("bzip2") > -1:
      basename=filename.rstrip(".spkg")
      subprocess.check_output(["cp", filename,basename +".tar.bz2"])
      subprocess.check_output(["bunzip2", basename + ".tar.bz2"])
    else: # fortran.spkg (only tar'ed) 
      basename=filename.rstrip(".spkg")
      subprocess.check_output(["cp", filename,basename + ".tar"])
    subprocess.check_output(["tar", "xf", basename + ".tar"])
    if os.path.exists(cur + "/" + basename + "/dist") == True:
      print filename
```



---

Comment by was created at 2011-08-24 23:44:19

Changing keywords from "" to "sd32".


---

Comment by jdemeyer created at 2012-04-19 10:01:57

Changing component from debian-package to packages.


---

Comment by jdemeyer created at 2014-01-07 12:58:39

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-01-07 12:58:39

New commits:


---

Comment by git created at 2014-01-07 14:11:23

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by chapoton created at 2014-01-07 17:02:32

Ok, this is indeed the last one where dist still exists. Good enough for me.


---

Comment by chapoton created at 2014-01-07 17:02:32

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-09 06:41:42

fill in the reviewer field...


---

Comment by vbraun created at 2014-01-10 07:29:52

Resolution: fixed
