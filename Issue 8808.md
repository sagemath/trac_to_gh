# Issue 8808: upgrade ecl from 10.2.1 to 10.4.1 (or whatever is newest upstream)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-28 18:26:36

Assignee: tbd

CC:  nbruin

Download the newest tarball from:

   http://sourceforge.net/projects/ecls/

This *should* also fix #7690.


---

Comment by was created at 2010-04-28 18:35:03

Changing priority from critical to major.


---

Comment by was created at 2010-04-28 18:35:03

Changing status from new to needs_review.


---

Comment by was created at 2010-04-28 18:35:03

Here's the new spkg:

   http://wstein.org/home/wstein/patches/ecl-10.4.1.spkg


---

Comment by was created at 2010-04-28 18:36:43

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-04-28 18:36:43

NOTE:

Maxima-5.20.1.p0 doesn't just build with this ECL

```
Summary:
ECL enabled. Executable name: "ecl"
default lisp: ecl
wish executable name: "wish"
Making all in src
make[1]: Entering directory `/mnt/usb1/scratch/wstein/build/san_diego/sage-4.4/spkg/build/maxima-5.20.1.p0/src/src'
test -d binary-ecl || mkdir binary-ecl
ecl -norc -eval '(progn (load "../lisp-utils/defsystem.lisp") (funcall (intern (symbol-name :operate-on-system) :mk) "maxima" :compile :verbose t) (build-maxima-lib))' -eval '(ext:quit)'
;;; Loading "/mnt/usb1/scratch/wstein/build/san_diego/sage-4.4/spkg/build/maxima-5.20.1.p0/src/src/../lisp-utils/defsystem.lisp"
;;; Loading #P"/mnt/usb1/scratch/wstein/build/san_diego/sage-4.4/local/lib/ecl/cmp.fas"
;;; Loading #P"/mnt/usb1/scratch/wstein/build/san_diego/sage-4.4/local/lib/ecl/sysfun.lsp"
An error occurred during initialization:
Attempt to redefine function REQUIRE in locked package..
make[1]: *** [binary-ecl/maxima] Error 1
make[1]: Leaving directory `/mnt/usb1/scratch/wstein/build/san_diego/sage-4.4/spkg/build/maxima-5.20.1.p0/src/src'
make: *** [all-recursive] Error 1
***********************************************************
Failed to make Maxima.
***********************************************************

real    0m3.803s
user    0m1.190s
sys     0m1.200s
sage: An error occurred while installing maxima-5.20.1.p0
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /mnt/usb1/scratch/wstein/build/san_diego/sage-4.4/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/mnt/usb1/scratch/wstein/build/san_diego/sage-4.4/spkg/build/maxima-5.20.1.p0 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/mnt/usb1/scratch/wstein/build/san_diego/sage-4.4/spkg/build/maxima-5.20.1.p0' && '/mnt/usb1/scratch/wstein/build/san_diego/sage-4.4/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
```



---

Comment by was created at 2010-04-28 18:54:11

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-04-28 19:03:00

Question: Does this ECL incorporate the patch nbruin mentions in #8645?


---

Comment by jason created at 2010-05-13 04:18:52

Replying to [comment:5 kcrisman]:
> Question: Does this ECL incorporate the patch nbruin mentions in #8645?

That patch just adds a Changelog entry.  This spkg has a different changelog entry (i.e., William updated this spkg, not Nils).  So this is a nonissue.


---

Comment by jason created at 2010-05-13 06:13:17

The spkg looks good, and the new maxima (#8731) builds with it.

This should *only* be merged simultaneously with the new maxima at #8731.


---

Comment by jason created at 2010-05-13 06:13:17

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-05-13 13:09:10

I think you should look at #8951 too.  It seems silly to have competing ECL packages, although of course they were addressing two different things.  Maybe there could be an immediate p0, or maybe that fix could be incorporated here?  It isn't a change to ECL, but just a change to how to determine if you build 64-bit on Solaris and a conditional removal of temp files, so either way of solving it seems reasonable.


---

Comment by drkirkby created at 2010-05-14 12:25:35

I've updated #8951 so it includes both the changes here (upadate of ECL) and the changes on that ticket (remove /tmp/ECL*).


---

Comment by nbruin created at 2010-05-14 16:46:43

Just note that ticket #8645 is about the same issue. The ticket there is closed because the "src" directory there is not the same as in the official ECL distribution.

However, the instructions for making an ECL spkg explicitly mention that these directories should be removed. So, either change the instructions on building an ECL spkg or remove those directories from the spkg.

The reasons why those directories should be removed are mentioned in the instructions.


---

Comment by nbruin created at 2010-05-14 16:46:43

Changing status from positive_review to needs_work.


---

Comment by jason created at 2010-05-14 17:10:29

Thanks for pointing this out.  I didn't see that.


---

Comment by mvngu created at 2010-05-14 21:30:16

Resolution: invalid
