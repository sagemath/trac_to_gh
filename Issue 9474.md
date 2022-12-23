# Issue 9474: Revert ECL back to ecl-10.2.1 and apply patches for Solaris 10 and OpenSolaris x64

Issue created by migration from https://trac.sagemath.org/ticket/9474

Original creator: drkirkby

Original creation time: 2010-07-11 11:36:49

Assignee: drkirkby

Since it is claimed ECL and Maxima are causing doctest failures on sage.math (see #9460) a decision has been made to revert ECL and Maxima. This patch will use the old version, but with a couple of patches which are already positively reviewed to allow ECL to build on Solaris 10 and OpenSolaris x64.

Let's hope this solves the problem, as several people manage to build sage-4.5.alpah4 on sage.math.washington.edu with Maxima tests passing, and other tests have failed on sage.math too. 

Dave


---

Comment by drkirkby created at 2010-07-11 12:06:55

Reverts ECL back to an older version, while preseving a couple of important Solaris and OpenSolaris patches


---

Attachment

I think `SunOs` should be `SunOS` in `spkg-install`, right?


---

Comment by drkirkby created at 2010-07-11 12:11:58

Replying to [comment:1 leif]:
> I think `SunOs` should be `SunOS` in `spkg-install`, right?
Yes, give me a few minutes and I'll update it.


---

Attachment

Correction SunOs -> SunOS


---

Comment by drkirkby created at 2010-07-11 12:23:08

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-07-11 12:23:08

There's a package for review at 

http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p0.spkg

Dave


---

Comment by leif created at 2010-07-11 17:15:09

Looks at least reasonable, and doesn't break things on other platforms.

I cannot really judge (or test) the behavior on SunOS/Solaris, though, especially regarding the test for `... 5.11 i86pc`.


---

Comment by leif created at 2010-07-11 18:14:26

Btw,

```sh
if [ "$VAR" = word ] ; then
    ...
```

is sufficient, you don't need an extra character there, nor does `word` (not containing spaces) need to be quoted. ;-)

-Leif


---

Comment by rlm created at 2010-07-11 19:24:30

Changing priority from blocker to major.


---

Comment by drkirkby created at 2010-07-12 07:09:46

Replying to [comment:5 leif]:
> Btw,
> {{{
> #!sh
> if [ "$VAR" = word ] ; then
>     ...
> }}}
> is sufficient, you don't need an extra character there, nor does `word` (not containing spaces) need to be quoted. ;-)
> 
> -Leif

It's less portable without the extra character! (You might note that autoconf adds the extra character too). I just get into a habit of writing my code the most portable way, even if in this case it will be run with bash, which for all recent versions at least does not require an extra character. 

I'm aware that there are no quotes needed - you might not the new code which deletes the temporary files has no such quotes. 

Dave


---

Comment by drkirkby created at 2010-07-12 07:30:27

Replying to [comment:4 leif]:
> Looks at least reasonable, and doesn't break things on other platforms.
> 
> I cannot really judge (or test) the behavior on SunOS/Solaris, though, especially regarding the test for `... 5.11 i86pc`.
> 
I appreciate that. But all 3 options are POSIX, and as you say it does not break on any other platform. Basically that test ensures the code will only be executed on a very specific platform where I know there is an issue. 

Here's the output on my Sony Vaio laptop (OpenSolaris 2009.06 snv_111b)

```
drkirkby@laptop:~$ uname -rsm
SunOS 5.11 i86pc
```


on disk.math.washington.edu (OpenSolaris 2008.11 snv_101b_rc2)

```
-bash-3.2$ uname -rsm
SunOS 5.11 i86pc
```


and my Sun Ultra 27 (OpenSolaris 2009.06, upgraded to snv_134)

```
drkirkby@hawk:~$ uname -rsm
SunOS 5.11 i86pc
```


Note I did not use the unportable '-p' option. That does not work on HP-UX. 

So can this get a positive review? 

Dave


---

Comment by rlm created at 2010-07-12 08:06:13

Can you or someone test this on a few non-Solaris systems before the positive review?


---

Comment by rlm created at 2010-07-12 08:45:56

Changing priority from major to blocker.


---

Comment by leif created at 2010-07-12 09:48:20

Replying to [comment:8 drkirkby]:
> Replying to [comment:4 leif]:
> > I cannot really judge (or test) the behavior on SunOS/Solaris, though, especially regarding the test for `... 5.11 i86pc`.
> > 
> I appreciate that. But all 3 options are POSIX, and as you say it does not break on any other platform.

I had only the specific version number (and to some extent "i86pc") in mind, not the options to `uname`, i.e. I did not know if all affected systems report exactly the same.


---

Comment by drkirkby created at 2010-07-12 10:00:59

Replying to [comment:11 leif]:

> I had only the specific version number (and to some extent "i86pc") in mind, not the options to `uname`, i.e. I did not know if all affected systems report exactly the same.

All systems I know of report the same. It may be the problem exists on some other variations of Solaris (OpenSolaris on SPARC, Solaris 10 on x86, Solaris 10 on 64-bit SPARC), but I don't know that. Hence it is restricted to only the systems where I know its a problem. 

Dave


---

Comment by drkirkby created at 2010-07-12 12:37:49

Replying to [comment:9 rlm]:
> Can you or someone test this on a few non-Solaris systems before the positive review?

 == Testing on sage.math (a Sun running Ubuntu Linux 8.04.4 LTS. ) ==
It built fine and failed one doctest on sage.math:


```
----------------------------------------------------------------------

The following tests failed:

	sage -t  -long devel/sage/sage/schemes/elliptic_curves/lseries_ell.py # 3 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1076.9 secon
```


This is the same failure William got with the sage-4.5.alpha4, and is a result of a lack of memory:


```
**********************************************************************
File "/mnt/usb1/scratch/kirkby/sage-4.5.rc0/devel/sage-main/sage/schemes/elliptic_curves/lseries_ell.py", line 226:
    sage: E.lseries().zeros(2)
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/kirkby/sage-4.5.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/kirkby/sage-4.5.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/kirkby/sage-4.5.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[3]>", line 1, in <module>
        E.lseries().zeros(Integer(2))###line 226:
    sage: E.lseries().zeros(2)
      File "/mnt/usb1/scratch/kirkby/sage-4.5.rc0/local/lib/python/site-packages/sage/schemes/elliptic_curves/lseries_ell.py", line 236, in zeros
        return lcalc.zeros(n, L=self.__E)
      File "/mnt/usb1/scratch/kirkby/sage-4.5.rc0/local/lib/python/site-packages/sage/lfunctions/lcalc.py", line 125, in zeros
        X = self('-z %s %s'%(int(n), L))
      File "/mnt/usb1/scratch/kirkby/sage-4.5.rc0/local/lib/python/site-packages/sage/lfunctions/lcalc.py", line 65, in __call__
        return os.popen(cmd).read().strip()
    OSError: [Errno 12] Cannot allocate memory
**********************************************************************
```


I don't know how much memory that tests needs, but its passed for me before. Perhaps it needs more RAM than other tests. 

I'll test on OS X (bsd.math) too, but note the changes are Solaris specific, so Linux and OX X should see exactly the same code. 

Dave


---

Comment by cremona created at 2010-07-12 13:36:25

I successfully installed the spkg linked here onto a build of 4.5.rc0, and am now testing the sage library.  I ignored the two patches on this ticket since they appear to be changes to an spkg.   If this is wrong (i.e. if I need to do something with the two patches before testing) please tell me.

This is on an AMD Opteron running ubuntu linux.


---

Comment by drkirkby created at 2010-07-12 13:51:15

Replying to [comment:14 cremona]:
> I successfully installed the spkg linked here onto a build of 4.5.rc0, and am now testing the sage library.  

Thank you. 

> I ignored the two patches on this ticket since they appear to be changes to an spkg.   If this is wrong (i.e. if I need to do something with the two patches before testing) please tell me.

That is not wrong. The patches are already in the .spkg, so you do not need to apply. 
 
> This is on an AMD Opteron running ubuntu linux.

Dave


---

Comment by cremona created at 2010-07-12 13:53:20

OK then, I can now report that testing the whole Sage library worked fine after installing the new spkg.


---

Comment by jhpalmieri created at 2010-07-12 21:19:18

The new spkg (actually this one plus the patch at #9187) installs for me on OS X 10.6 when building spkgs in parallel.  I haven't gotten to the doctesting part of things, but if there are problems, I'll report them here.


---

Comment by jhpalmieri created at 2010-07-13 02:26:20

All doctests pass for me on OS X 10.6.  The new spkg also has built successfully on t2.math, and I'm running doctests now.


---

Comment by drkirkby created at 2010-07-13 14:32:27

Replying to [comment:18 jhpalmieri]:
> All doctests pass for me on OS X 10.6.  The new spkg also has built successfully on t2.math, and I'm running doctests now.

I looked in John's directory `/scratch/palmieri/sage-4.5.rc0` on t2.math, and see the doctests had completed with 7 failures. However, three of those end with `# File not found` which is actually just a timeout - hopefully #9316 should fix that bug. After running the tests that failed for John at the command line, with longer timeouts, I find there are two failures which will not go away. 


```
	sage -t -long "devel/sage/doc/en/thematic_tutorials/group_theory.rst"
	sage -t -long "devel/sage/sage/libs/galrep/wrapper.pyx"
```


Those two failures need to be resolved. I created tickets (#9489 and #9490) for these two doctest failures. 

The longest test was:


```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
	 [3023.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3023.2 seconds
```


so it looks like one needs a SAGE_TIMEOUT_LONG >= 3600 seconds (one hour) to be reasonably confident of not getting a timeout on 't2.math'. 

Dave


---

Comment by drkirkby created at 2010-07-13 16:19:13

John's successful tests would appear to have been built with `ecl-10.2.1.p1.spkg` from #9187, which has these changes, *plus* the changes to allow better building in parallel. I'm basing this on the fact that John has the ecl-10.2.1.p1.spkg in his directory, but not the ecl-10.2.1.p0.spkg I created.  


```
kirkby@t2:[/scratch/palmieri/sage-4.5.rc0/spkg/standard] $ ls -l ecl-*
-rw-r--r--   1 palmieri 1005     4850369 Jul 12 13:31 ecl-10.2.1.p1.spkg
-rw-r--r--   1 palmieri 1005     4820179 Jul 11 12:12 ecl-10.2.1.spkg
```


My successful tests on OS X were also using ecl-10.2.1.p1.spkg from #9187.

Dave


---

Comment by jhpalmieri created at 2010-07-13 17:15:41

Replying to [comment:20 drkirkby]:
> John's successful tests would appear to have been built with `ecl-10.2.1.p1.spkg` from #9187, which has these changes, *plus* the changes to allow better building in parallel. 

Yes, that's right.  That's what I meant in [my comment above](http://trac.sagemath.org/sage_trac/ticket/9474#comment:17).

I'm marking this as "positive review" since it builds on sage.math, OS X, and t2 without problem.

By the way, Dave, my build on t2 only took 2 hours this time (!) -- this is without ATLAS and the docs, of course.  Some of the speedup is probably because of building in /scratch instead of /home, so thanks for that pointer.


---

Comment by jhpalmieri created at 2010-07-13 17:15:41

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-13 18:39:44

Merged, but as part of #9187.


---

Comment by rlm created at 2010-07-13 18:39:44

Resolution: fixed
