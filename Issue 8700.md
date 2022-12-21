# Issue 8700: the libpng-1.2.35.p0 in sage-4.4.alpha0 contains an extra copy of libpng-1.2.35!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-17 06:35:02

Assignee: tbd


```
wstein`@`boxen:~/build/sage-4.4.alpha0/spkg/standard/libpng-1.2.35.p0$ ls
libpng-1.2.35  spkg-install  SPKG.txt  src
wstein`@`boxen:~/build/sage-4.4.alpha0/spkg/standard/libpng-1.2.35.p0$ ls libpng-1.2.35/
spkg-install  SPKG.txt  src
```


Basically there is an accidental complete copy of the extracted spkg in the spkg!


---

Comment by was created at 2010-04-17 06:36:48

Looking in the changelog, the last person to work on the spkg left this message:

```
### libpng-1.2.35.p0 (Jaap Spies, Feb 1th, 2010)
 *
```


What was done?  It doesn't say.    The log shows this though:

```
changeset:   13:ae01944f408c
tag:         tip
user:        Jaap Spies <jaapspies`@`gmail.com>
date:        Thu Feb 04 19:32:51 2010 +0100
summary:     Corrected stupid typo I thought I had corrected earlier.

changeset:   12:329a8eb6dd2e
user:        Jaap Spies <jaapspies`@`gmail.com>
date:        Wed Feb 03 19:09:41 2010 +0100
summary:     Let SAGE64=yes work not only on OSX, but also on Open Solaris and possibly on other platform
```


Anyway, somebody was sloppy refereeing this, etc.


---

Comment by was created at 2010-04-17 06:40:20

Here's a fixed spkg:

    http://boxen.math.washington.edu/home/wstein/patches/libpng-1.2.35.p1.spkg


---

Comment by was created at 2010-04-17 06:40:20

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-04-23 04:40:47

I'm downgrading this from a blocker to critical: the current spkg makes the Sage source distribution a little bigger, but causes no bugs or test failures.


---

Comment by jhpalmieri created at 2010-04-23 04:40:47

Changing priority from blocker to critical.


---

Comment by mvngu created at 2010-06-16 01:59:49

Close as fixed:


```
[mvngu`@`sage libpng-1.2.35.p2]$ pwd
/dev/shm/mvngu/sage-4.4.4.alpha0/spkg/standard/libpng-1.2.35.p2
[mvngu`@`sage libpng-1.2.35.p2]$ ls
spkg-install  SPKG.txt  src
```



---

Comment by mvngu created at 2010-06-16 01:59:49

Resolution: fixed
