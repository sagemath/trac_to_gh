# Issue 7856: update matplotlib hack for OS X

Issue created by migration from https://trac.sagemath.org/ticket/7856

Original creator: was

Original creation time: 2010-01-06 15:01:56

Assignee: tbd




---

Comment by was created at 2010-01-06 15:02:59

Changing status from new to needs_review.


---

Comment by was created at 2010-01-06 15:14:46

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-01-06 15:35:02

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-01-06 15:48:42

http://wstein.org/home/wstein/patches/matplotlib-0.99.1.p3.spkg


---

Comment by jhpalmieri created at 2010-01-06 16:02:27

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-01-06 16:02:27

A few quick comments: SPGK.txt needs to be updated.  Also, is the hack appropriate for OS X running 10.5 (since it now just checks for "DARWIN", not the version number)?  I don't have access to a machine to test that.

Finally, if SAGE64 is set and we're on DARWIN, is it worth making some of the other changes in [http://blog.hyperjeff.net/?p=160](http://blog.hyperjeff.net/?p=160)?  For example, in src/make.osx, changing 

```
CFLAGS="-arch i386 -arch ppc -I${PREFIX}/include -I${PREFIX}/include/freetype2 -isysroot /Developer/SDKs/MacOSX10.4u.sdk"
LDFLAGS="-arch i386 -arch ppc -L${PREFIX}/lib -syslibroot,/Developer/SDKs/MacOSX10.4u.sdk"
```

so that "-arch ppc" gets changed to "-arch x86_64"?  (That web page also suggests adding "FFLAGS", and making a few other changes.  We can defer these until later, also.)


---

Comment by jhpalmieri created at 2010-01-06 16:02:58

Oh, also, the file patches/osx10.6hack~ should be deleted.


---

Comment by jhpalmieri created at 2010-01-06 18:07:22

As far as actual testing goes, on my OS X 10.6 machines:

 - before the patch, if I delete the files in ~/.matplotlib, then `sage: plot(sin)` causes a crash.

 - after the patch, if I delete the files in ~/.matplotlib, then `sage: plot(sin)` works fine.

 - this is completely reproducible: if I force installation of the old matplotlib spkg, then the crashes come back, and then if I force installation of the new one, the crashes go away.

So positive review, modulo the comments made above.

Do we need to test on an OS X 10.5 machine?


---

Comment by was created at 2010-01-06 23:14:25

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-01-06 23:14:25

> A few quick comments: SPGK.txt needs to be updated. Also, is the hack 
> appropriate for OS X running 10.5 (since it now just checks for "DARWIN", 
> not the version number)?

It runs patches/osx10.6hack on any OS X, but *only* actually applies the hack on 10.6.  It immediately exits patches/osx10.6hack on other than 10.6. 

I've updated the spkg, and also now tested it on 10.5 and it works fine (as before).  So, can you change it to positive review?


---

Comment by jhpalmieri created at 2010-01-06 23:22:03

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-01-08 01:24:29

Please see [http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04165.html](http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04165.html) and [http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04166.html](http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04166.html) for something which looks relevant - namely, DPY_ARRAYAUNIQUE_SYMBOL is, in fact, a typo for DPY_ARRAY_UNIQUE_SYMBOL.  I don't know if this would fix things for us, but at any rate the 'horrible hack' uses precisely this (incorrect) variable, so we should at least fix both the source and the hack to use the correct one.


---

Comment by jhpalmieri created at 2010-01-08 06:19:14

Replying to [comment:11 kcrisman]:
> Please see [http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04165.html](http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04165.html) and [http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04166.html](http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04166.html) for something which looks relevant - namely, DPY_ARRAYAUNIQUE_SYMBOL is, in fact, a typo for DPY_ARRAY_UNIQUE_SYMBOL.  I don't know if this would fix things for us, but at any rate the 'horrible hack' uses precisely this (incorrect) variable, so we should at least fix both the source and the hack to use the correct one.

I tried just the patches mentioned above, not the "horrible hack", but it didn't work: the hack was needed to avoid crashes.


---

Comment by rlm created at 2010-01-13 06:39:02

Resolution: fixed
