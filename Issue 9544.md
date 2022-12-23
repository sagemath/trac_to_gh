# Issue 9544: Fix flintqs on FreeBSD

Issue created by migration from https://trac.sagemath.org/ticket/9544

Original creator: pjeremy

Original creation time: 2010-07-18 20:01:27

Assignee: pjeremy

TonelliShanks.h references int32_t but does not directly include <stdint.h> (where it is defined).  On FreeBSD using gcc45 (but not the base gcc), this causes compilation to fail.

The attached patch makes TonelliShanks.h idempotent on FreeBSD (it probably should be on all architectures but making the patch FreeBSD-specific simplifies testing).


---

Comment by kcrisman created at 2012-01-31 02:00:15

Apparently at least once [Stephen Montgomery-Smith](http://groups.google.com/group/sage-devel/browse_thread/thread/2feec7c5511c4ae5/857a00a9aa271f17) compiled Sage on a "port" successfully on FreeBSD without this.


---

Comment by stephen created at 2012-04-08 14:51:05

Stephen Montgomery-Smith reports that this patch is absolutely necessary for building under FreeBSD.


---

Comment by leif created at 2012-04-19 21:29:18

Just for the record:  There'll be a new FLINTQS spkg at #12855 soon...


---

Comment by kcrisman created at 2012-06-20 19:10:48

The current spkg-install change being used in the port is


```diff
--- flintqs-20070817.p6/spkg-install-orig	2012-04-08 00:46:21.000000000 +0000
+++ flintqs-20070817.p6/spkg-install	2012-04-08 00:55:33.000000000 +0000
@@ -7,6 +7,7 @@
 fi
 
 cp patches/lanczos.h  src/
+patch -p0 < patches/TonelliShanks.h.patch
 
 cd src
```


but we'll have to check the exit status on that.  Or just add this into #12855 or something.


---

Comment by jdemeyer created at 2012-06-21 10:25:06

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2012-06-21 10:25:39

Rebased to #12855.


---

Attachment

Diff for the flintqs spkg. For reference / review only.


---

Comment by kcrisman created at 2012-06-21 12:58:40

This looks good, but since it's applied universally and not just on FreeBSD I am hesitant to give it positive review.  Jeroen, did you try this out on some of the buildbots?

Also, is there even an "upstream"?  This is a five-year-old program, and some searching indicates that maybe a newer version is included in flint itself?  Anyway, I figure that the age makes reporting upstream inappropriate.


---

Comment by jdemeyer created at 2012-06-21 13:02:19

Replying to [comment:9 kcrisman]:
> Jeroen, did you try this out on some of the buildbots?
No, but I don't expect problems. What harm could an additional header file do?


---

Comment by kcrisman created at 2012-06-21 13:09:15

> > Jeroen, did you try this out on some of the buildbots?
> No, but I don't expect problems. What harm could an additional header file do?
I don't know, that's why I asked!  Extra imports in Python sometimes cause all kinds of circularity issues or slowdowns, and I don't know enough about C to say either way.

But since you just repackaged this, I think it's appropriate for you to be a reviewer as well.  And I checked that the package is well-formed and installs on OS X.

I also notice that you included stdint after stdlib, while Stephen does the opposite in his patch [here](http://www.freebsd.org/cgi/cvsweb.cgi/ports/math/sage/files/spkg-patch-flintqs-20070817.p6_-_patches_TonelliShanks.h.patch?rev=1.1;content-type=text%2Fplain).  I assume this also doesn't matter?  Sorry for the very stupid questions.
----
See also #11792?


---

Comment by jdemeyer created at 2012-06-21 13:14:14

Replying to [comment:11 kcrisman]:
> > > Jeroen, did you try this out on some of the buildbots?
> > No, but I don't expect problems. What harm could an additional header file do?
> I don't know, that's why I asked!  Extra imports in Python sometimes cause all kinds of circularity issues or slowdowns, and I don't know enough about C to say either way.
In theory this could cause problems, but presumably the C headers are well-designed such that these problems don't occur.

> I also notice that you included stdint after stdlib, while Stephen does the opposite in his patch
It also shouldn't matter. The way I did it looked more natural, but there's really no reason.


---

Comment by kcrisman created at 2012-06-21 13:37:11

> It also shouldn't matter. The way I did it looked more natural, but there's really no reason.
Ok. 

I'm even having trouble finding where this is used.  `sage -grep` with various upper/lowercase of flintqs does nothing, it's not in `module_list.py`, in `spkg/standard/deps` it only has dependencies...  and I'm going to need CPU firepower in a few minutes, can't do a full doctest right now.  Weird.


---

Comment by jdemeyer created at 2012-06-21 19:04:57

Replying to [comment:13 kcrisman]:
> I'm even having trouble finding where this is used.  `sage -grep` with various upper/lowercase of flintqs does nothing, it's not in `module_list.py`, in `spkg/standard/deps` it only has dependencies...  and I'm going to need CPU firepower in a few minutes, can't do a full doctest right now.  Weird.

The interface is `sage/interfaces/qsieve.py`.


---

Comment by kcrisman created at 2012-06-21 19:17:13

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-06-21 19:17:13

> > I'm even having trouble finding where this is used.  `sage -grep` with various upper/lowercase of flintqs does nothing, it's not in `module_list.py`, in `spkg/standard/deps` it only has dependencies...  and I'm going to need CPU firepower in a few minutes, can't do a full doctest right now.  Weird.
> 
> The interface is `sage/interfaces/qsieve.py`.

Great, thanks.  That passes long tests, so since there really isn't any reason anything should be bad, we are good to go.  (Yes, I did `sage -b`.)

Since p7 is also 5.1, tentatively putting it there, but feel free to do whatever is convenient.


---

Comment by jdemeyer created at 2012-06-21 19:33:10

Replying to [comment:15 kcrisman]:
> Since p7 is also 5.1, tentatively putting it there, but feel free to do whatever is convenient.
.p7 still needs review...


---

Comment by jdemeyer created at 2012-06-28 09:36:36

Resolution: fixed
