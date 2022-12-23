# Issue 9023: ghmm is buiding 32-bit on OpenSolaris x64 even when SAGE64 is set to "yes"

Issue created by migration from https://trac.sagemath.org/ticket/9023

Original creator: drkirkby

Original creation time: 2010-05-23 20:59:54

Assignee: drkirkby

CC:  jsp

The spkg-install has the usual dumb code for building 64-bit on OS X. 


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
   echo "64 bit MacIntel"
   CFLAGS="-O2 -g -fPIC -m64 "; export CFLAGS
   LDFLAGS="-m64"; export LDFLAGS
fi
```


This should be easy to fix, by removing the OS X requirement. 




---

Attachment

Mercurial patch to build GHMM 64-bit on any operating system.


---

Comment by drkirkby created at 2010-05-23 21:38:43

A revised package can be found at 

http://boxen.math.washington.edu/home/kirkby/patches/ghmm-20080813.p1.spkg

Dave


---

Comment by drkirkby created at 2010-05-23 21:38:43

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-05-24 18:24:14

For other OpenSolaris issues, see #9026


---

Comment by drkirkby created at 2010-05-31 00:42:32

I'm not happy with this - are reverting to needs work. It appears to be linking to a 32-bit library. 

Dave


---

Comment by drkirkby created at 2010-05-31 00:42:32

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-06-14 17:41:33

I've decided to revert this back to 'needs review' and change the title slightly. The reason is that the patch, whilst not sufficient for a 64-bit build, does go some way to improving the situation, as objects are now created 64-bit. There's still a problem linking with the wrong library, which needs to be resolved. However, the attached patch may allow us to hack a fix, but putting the 64-bit libraries in the directory where the 32-bit ones should be. As such, this change is worth having, even though it is not a complete cure. 

Dave


---

Comment by drkirkby created at 2010-06-14 17:41:33

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-06-22 17:56:19

ghmm is now gone.


---

Comment by was created at 2010-06-22 17:56:19

Resolution: wontfix
