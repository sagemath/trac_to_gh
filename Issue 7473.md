# Issue 7473: Sphinx hangs when making a clone

Issue created by migration from https://trac.sagemath.org/ticket/7473

Original creator: mpatel

Original creation time: 2009-11-16 10:20:23

Assignee: mvngu

CC:  jhpalmieri nthiery ncohen

This is a follow-up to #6187.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/433ec95cba086551/f4286b67d64a19dd?#f4286b67d64a19dd), [sage-release](http://groups.google.com/group/sage-release/msg/76c956312e4de13d), [#sage-devel log](http://sage.math.washington.edu/home/mpatel/projects/irclogs/logs/sage-devel-2009-10-26.log.html#t21:56).


---

Comment by mpatel created at 2009-11-18 21:37:28

What if we run `hg clone`, then `cp -pr` just the files Sphinx checks?


---

Comment by mpatel created at 2009-11-18 22:47:55

What if we capture `stderr` and `stdin`, too, in

```python
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
```

?  Or do the opposite?  For example, `builder.py` issues `subprocess.call(build_command, shell=True)`, which is shorthand for `subprocess.Popen(build_command, shell=True).wait()`.   But this may not be relevant.

I'll try to take a closer look soon.


---

Comment by mpatel created at 2009-11-19 23:21:04

I've noticed that switching among _existing branches_ via `sage -b`, even if I've changed no files, can touch or byte-compile files in `SAGE_LOCAL/lib/python/site-packages/sage`.  Sphinx notices the changed dependencies and rebuilds the manual.


---

Comment by mpatel created at 2009-11-20 00:02:19

It strange that

```sh
cd SAGE_ROOT/devel
ls -lsFi `find -name environment.pickle`|grep ref
```

shows the clones to have different Sphinx pickles --- their inodes (the first column on sage.math) are distinct.  Compare with

```sh
ls -lsFi `find -name steenrod_algebra.html`
ls -lsFi `find -name steenrod_algebra.py`|grep -v build
```

But aren't the pickles hard linked?


---

Comment by mpatel created at 2009-11-20 00:16:18

I think this happens because `sphinx.environment.BuildEnvironment.topickle` first dumps the environment to a temporary file, then moves it `environment.pickle`.


---

Attachment

Make pickle saving preserve the hard link.  Apply to sage repo.


---

Comment by mpatel created at 2009-11-20 14:21:04

Don't capture Sphinx clone output.  This _may_ prevent the hang.  Apply to scripts repo.


---

Attachment

I _think_ the [attachment:trac_7473-scripts_clone.patch attached patch] for the scripts repository prevents the hang when cloning.  The [attachment:trac_7473-sage_builder.patch sage repository patch] should ensure that we usually keep just one copy of the reference manual's `environment.pickle`.

But I'm still not sure about how to avoid rebuilding nearly all of the manual when cloning or after trivially switching branches.  The latter may be a separate problem.


---

Attachment

Use `cp -pr` to preserve .rst file times.  This may work.  Apply only this patch to scripts repo.


---

Comment by mpatel created at 2009-11-22 19:09:13

Version 2 of the scripts repo (i.e., `sage-clone`) patch uses `cp -pr` instead of [shutil.copytree](http://docs.python.org/library/shutil.html#shutil.copytree) to copy the auto-generated .rst files.  Could someone please test this and the sage repo patch?  It appears to prevent the hang and unnecessary rebuilds of the reference manual on sage.math.

According to its documentation, `shutil.copytree` is very similar to `cp -pr`.  But their results aren't identical, it seems.

I don't know if `cp -pr` is cross-platform.


---

Comment by mpatel created at 2009-11-22 19:09:13

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2009-11-22 20:48:29

#7407 provides the following link, saying that it describes the only options to "cp" which should be used:

[http://www.opengroup.org/onlinepubs/009695399/utilities/cp.html](http://www.opengroup.org/onlinepubs/009695399/utilities/cp.html)

Reading this, I wonder if we should use "cp -pR" instead of "cp -pr".

I made a new clone, applied the patch, built the documentation, and then made another clone.  The new cloning process took 2-3 minutes on my iMac running OS X 10.6, and when done the documentation did not need to be rebuilt again.  On sage.math, the same thing happened, with the cloning process taking about the same amount of time.  In both cases, updating the modification times was quick.  Also in both cases, using "cp -pR" worked just as well as "cp -pr".

Shall we take the cited web page as enough evidence that this is cross-platform?  And should we change "r" to "R"?


---

Attachment

Use cp -pR for auto-generated .rst files.  Apply only this patch to the scripts repo.


---

Comment by mpatel created at 2009-11-23 21:47:25

Version 3 uses `cp -pR` instead of `cp -pr`.  Does the Windows build environment support `cp -pR`?


---

Comment by mpatel created at 2009-11-23 21:55:06

nthiery, ncohen:  If you have a chance, could you let us know if the patches above work?  In particular,

 * Apply [attachment:trac_7473-sage_builder.patch] to the sage repository.
 * Apply [attachment:trac_7473-scripts_clone_v3.patch] to the scripts repository.

If this is yet another false positive, I apologize.


---

Comment by jhpalmieri created at 2009-11-23 23:46:47

I'm happy with it (Mac OS X 10.6 and sage.math).

On what other platforms does it need to be tested?


---

Comment by ncohen created at 2009-11-24 07:32:40

I tried it on my Fedora ( built from sources ) and it applies fine and does its job ( I'm not stuck anymore when cloning ) !

( Even though I can not control your script as I have no idea of how Sage works at this level... ) :-)

Thank you for your patch !!!

Nathann


---

Comment by nthiery created at 2009-11-24 12:51:54

Replying to [comment:11 mpatel]:
> nthiery, ncohen:  If you have a chance, could you let us know if the patches above work?  In particular,
> 
>  * Apply [attachment:trac_7473-sage_builder.patch] to the sage repository.
>  * Apply [attachment:trac_7473-scripts_clone_v3.patch] to the scripts repository.
> 
> If this is yet another false positive, I apologize.

I tried sage -combinat install (which calls clone), and it worked smoothly (ubuntu 9.4, sage 4.2.1, macbook pro)!

Thanks!


---

Comment by jhpalmieri created at 2009-11-26 06:43:59

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2009-11-26 06:43:59

On the grounds that this is an improvement on some systems and I hope isn't any worse on any systems, I'm giving this a positive review.  I really would like this to be merged, because cloning is so painful right now.


---

Comment by mhansen created at 2009-11-29 05:41:47

Resolution: fixed


---

Comment by mpatel created at 2009-12-04 07:59:19

It seems that the [attachment:trac_7473-sage_builder.patch sage repo patch] didn't make it into 4.3.alpha1.  This patch will prevent some unnecessary doc rebuilds when changing branches.


---

Comment by mhansen created at 2009-12-04 08:06:31

Oops, I must only seen the last patch.  I'll add it first thing to the next release.


---

Comment by mhansen created at 2009-12-04 08:06:31

Resolution changed from fixed to 


---

Comment by mhansen created at 2009-12-04 08:06:31

Changing status from closed to new.


---

Comment by mhansen created at 2009-12-04 08:06:45

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-12-04 08:06:53

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2009-12-04 08:28:31

Thanks!


---

Comment by mhansen created at 2009-12-06 08:24:12

Merged trac_7473-sage_builder.patch in 4.3.rc0.


---

Comment by mhansen created at 2009-12-06 08:24:12

Resolution: fixed
