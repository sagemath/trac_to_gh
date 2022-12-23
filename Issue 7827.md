# Issue 7827: Fix atlas-3.8.3.p9 compilation on FreeBSD

Issue created by migration from https://trac.sagemath.org/ticket/7827

Original creator: pjeremy

Original creation time: 2010-01-03 04:15:58

Assignee: pjeremy

CC:  drkirby was

* FreeBSD uses an '_fbsd' suffix on the ELF format supported by ld - prevents ld: unrecognised emulation mode: elf_x86_64 error during atlas build. Reported upstream as https://sourceforge.net/tracker/index.php?func=detail&aid=2728930&group_id=23725&atid=379482

* Treat shared libraries the same as Linux - otherwise they aren't correctly detected by (eg) numpy. (sage-specific) 



---

Attachment


---

Comment by pjeremy created at 2010-01-03 04:18:09

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-12 17:48:59

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-12 17:48:59

I'm personally unable to verify this works on FreeBSD, but I can certainly see the changes will have no effect on any platform other than FreeBSD. So its a positive from me.


---

Comment by rlm created at 2010-01-14 06:50:23

pjeremy -- There are repositories in the directories themselves, and the best way to post a modification to an spkg is to check in the changes to the mercurial repo, and `sage -pkg` it up, posting a link to a whole spkg on the ticket. This ticket in particular won't work as is, because #7838 updated from `p9` to `p10`.


---

Comment by mvngu created at 2010-01-24 16:21:06

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-01-24 16:22:28

An updated spkg is available at

http://sage.math.washington.edu/home/mvngu/spkg/standard/atlas/atlas-3.8.3.p11.spkg

I committed the patch [7827.atlas.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7827/7827.atlas.patch) in pjeremy's name. The patched version of `SpewMakeInc.c` is available under `patches/`. I also patched the installation script `spkg-install-script` to copy pjeremy's patched `patches/SpewMakeInc.c` over to `src/CONFIG/src/SpewMakeInc.c`. The relevant modification is:

```
diff -r cffdd7ee34e2 spkg-install-script
--- a/spkg-install-script
+++ b/spkg-install-script
@@ -120,6 +120,10 @@
 
 CUR=`pwd`
 echo $CUR
+if [ `uname` = "FreeBSD" ]; then
+    echo Patching SpewMakeInc.c for FreeBSD-specific build
+    cp patches/SpewMakeInc.c src/CONFIG/src/SpewMakeInc.c
+fi
 # add PPC4 7447 CPU and better Itanium2 detection:
 echo Deal with PPC4 7447 model and Itanium 2
 cp patches/archinfo_linux.c src/CONFIG/src/backend/archinfo_linux.c
```

The updated spkg needs another pair of eyes (anyone's, other than mine) to comb through it. If my change to `spkg-install-script` gets the green light, then the updated spkg can be merged.


---

Comment by mvngu created at 2010-01-24 16:22:28

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-01-27 02:11:04

This looks good. Note there are also some patches to #8039 which needs work, but I suspect will make it into 4.3.2. 

Dave


---

Comment by drkirkby created at 2010-01-27 02:11:04

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-01 00:40:07

Merged [atlas-3.8.3.p11.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/atlas/atlas-3.8.3.p11.spkg) in the standard spkg repository.


---

Comment by mvngu created at 2010-02-01 00:40:07

Resolution: fixed
