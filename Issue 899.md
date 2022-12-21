# Issue 899: minor error in inst.tex

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2007-10-14 21:02:10

Assignee: wdj

The installation manual says


```
On a newly installed Ubuntu system, you can install the above
commands as follows:

 sudo apt-get install gcc-4.0-base
 sudo apt-get install make
 sudo apt-get install m4
 sudo apt-get install bison
 sudo apt-get install flex
 sudo apt-get install tar
 sudo apt-get install perl
 sudo apt-get install binutils
 sudo apt-get install gcc
 sudo apt-get install libstdc++6-dev
 sudo apt-get install g++
```


I think this should be corrected (changes on 2 lines) to say


```
On a newly installed Ubuntu system, you can install the above
commands as follows:

 sudo apt-get install gcc-4.2-base      # or the latest version available
 sudo apt-get install make
 sudo apt-get install m4
 sudo apt-get install bison
 sudo apt-get install flex
 sudo apt-get install tar
 sudo apt-get install perl
 sudo apt-get install binutils
 sudo apt-get install libstdc++6-dev
 sudo apt-get install g++
```


In fact, in 7.10 "sudo apt-get install gcc-4.0-base" yields
"E: Package gcc-4.0-base has no installation candidate"
and "sudo apt-get install gcc" is redundant.

The patch is at
http://sage.math.washington.edu/home/wdj/patches/inst.tex.hg


---

Comment by was created at 2007-10-20 21:53:11

inst.tex.hg is a bundle against hg_sage. You accidently did hg_sage.send('...') instead of hg_doc.send('...'). Please create a bundle against the docs.


---

Comment by wdj created at 2007-10-21 00:51:33

I posted a new patch to
http://sage.math.washington.edu/home/wdj/patches/inst.tex.hg


---

Comment by was created at 2007-10-21 01:50:03

This bundle is empty.  It doesn't contain anything that isn't already released or in the master hg_doc repo.


---

Comment by cwitty created at 2007-10-27 04:54:55

Resolution: fixed
