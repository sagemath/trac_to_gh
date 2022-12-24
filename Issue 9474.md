# Issue 9474: Revert ECL back to ecl-10.2.1 and apply patches for Solaris 10 and OpenSolaris x64

archive/issues_009474.json:
```json
{
    "body": "Assignee: drkirkby\n\nSince it is claimed ECL and Maxima are causing doctest failures on sage.math (see #9460) a decision has been made to revert ECL and Maxima. This patch will use the old version, but with a couple of patches which are already positively reviewed to allow ECL to build on Solaris 10 and OpenSolaris x64.\n\nLet's hope this solves the problem, as several people manage to build sage-4.5.alpah4 on sage.math.washington.edu with Maxima tests passing, and other tests have failed on sage.math too. \n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9474\n\n",
    "created_at": "2010-07-11T11:36:49Z",
    "labels": [
        "porting: Solaris",
        "blocker",
        "bug"
    ],
    "title": "Revert ECL back to ecl-10.2.1 and apply patches for Solaris 10 and OpenSolaris x64",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9474",
    "user": "drkirkby"
}
```
Assignee: drkirkby

Since it is claimed ECL and Maxima are causing doctest failures on sage.math (see #9460) a decision has been made to revert ECL and Maxima. This patch will use the old version, but with a couple of patches which are already positively reviewed to allow ECL to build on Solaris 10 and OpenSolaris x64.

Let's hope this solves the problem, as several people manage to build sage-4.5.alpah4 on sage.math.washington.edu with Maxima tests passing, and other tests have failed on sage.math too. 

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9474





---

archive/issue_comments_090867.json:
```json
{
    "body": "Reverts ECL back to an older version, while preseving a couple of important Solaris and OpenSolaris patches",
    "created_at": "2010-07-11T12:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90867",
    "user": "drkirkby"
}
```

Reverts ECL back to an older version, while preseving a couple of important Solaris and OpenSolaris patches



---

archive/issue_comments_090868.json:
```json
{
    "body": "Attachment [9474.patch](tarball://root/attachments/some-uuid/ticket9474/9474.patch) by leif created at 2010-07-11 12:08:21\n\nI think `SunOs` should be `SunOS` in `spkg-install`, right?",
    "created_at": "2010-07-11T12:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90868",
    "user": "leif"
}
```

Attachment [9474.patch](tarball://root/attachments/some-uuid/ticket9474/9474.patch) by leif created at 2010-07-11 12:08:21

I think `SunOs` should be `SunOS` in `spkg-install`, right?



---

archive/issue_comments_090869.json:
```json
{
    "body": "Replying to [comment:1 leif]:\n> I think `SunOs` should be `SunOS` in `spkg-install`, right?\nYes, give me a few minutes and I'll update it.",
    "created_at": "2010-07-11T12:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90869",
    "user": "drkirkby"
}
```

Replying to [comment:1 leif]:
> I think `SunOs` should be `SunOS` in `spkg-install`, right?
Yes, give me a few minutes and I'll update it.



---

archive/issue_comments_090870.json:
```json
{
    "body": "Attachment [9474.2.patch](tarball://root/attachments/some-uuid/ticket9474/9474.2.patch) by drkirkby created at 2010-07-11 12:16:04\n\nCorrection SunOs -> SunOS",
    "created_at": "2010-07-11T12:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90870",
    "user": "drkirkby"
}
```

Attachment [9474.2.patch](tarball://root/attachments/some-uuid/ticket9474/9474.2.patch) by drkirkby created at 2010-07-11 12:16:04

Correction SunOs -> SunOS



---

archive/issue_comments_090871.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-11T12:23:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90871",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090872.json:
```json
{
    "body": "There's a package for review at \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p0.spkg\n\nDave",
    "created_at": "2010-07-11T12:23:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90872",
    "user": "drkirkby"
}
```

There's a package for review at 

http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p0.spkg

Dave



---

archive/issue_comments_090873.json:
```json
{
    "body": "Looks at least reasonable, and doesn't break things on other platforms.\n\nI cannot really judge (or test) the behavior on SunOS/Solaris, though, especially regarding the test for `... 5.11 i86pc`.",
    "created_at": "2010-07-11T17:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90873",
    "user": "leif"
}
```

Looks at least reasonable, and doesn't break things on other platforms.

I cannot really judge (or test) the behavior on SunOS/Solaris, though, especially regarding the test for `... 5.11 i86pc`.



---

archive/issue_comments_090874.json:
```json
{
    "body": "Btw,\n\n```sh\nif [ \"$VAR\" = word ] ; then\n    ...\n```\n\nis sufficient, you don't need an extra character there, nor does `word` (not containing spaces) need to be quoted. ;-)\n\n-Leif",
    "created_at": "2010-07-11T18:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90874",
    "user": "leif"
}
```

Btw,

```sh
if [ "$VAR" = word ] ; then
    ...
```

is sufficient, you don't need an extra character there, nor does `word` (not containing spaces) need to be quoted. ;-)

-Leif



---

archive/issue_comments_090875.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2010-07-11T19:24:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90875",
    "user": "rlm"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_090876.json:
```json
{
    "body": "Replying to [comment:5 leif]:\n> Btw,\n> {{{\n> #!sh\n> if [ \"$VAR\" = word ] ; then\n>     ...\n> }}}\n> is sufficient, you don't need an extra character there, nor does `word` (not containing spaces) need to be quoted. ;-)\n> \n> -Leif\n\nIt's less portable without the extra character! (You might note that autoconf adds the extra character too). I just get into a habit of writing my code the most portable way, even if in this case it will be run with bash, which for all recent versions at least does not require an extra character. \n\nI'm aware that there are no quotes needed - you might not the new code which deletes the temporary files has no such quotes. \n\nDave",
    "created_at": "2010-07-12T07:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90876",
    "user": "drkirkby"
}
```

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

archive/issue_comments_090877.json:
```json
{
    "body": "Replying to [comment:4 leif]:\n> Looks at least reasonable, and doesn't break things on other platforms.\n> \n> I cannot really judge (or test) the behavior on SunOS/Solaris, though, especially regarding the test for `... 5.11 i86pc`.\n> \nI appreciate that. But all 3 options are POSIX, and as you say it does not break on any other platform. Basically that test ensures the code will only be executed on a very specific platform where I know there is an issue. \n\nHere's the output on my Sony Vaio laptop (OpenSolaris 2009.06 snv_111b)\n\n```\ndrkirkby@laptop:~$ uname -rsm\nSunOS 5.11 i86pc\n```\n\n\non disk.math.washington.edu (OpenSolaris 2008.11 snv_101b_rc2)\n\n```\n-bash-3.2$ uname -rsm\nSunOS 5.11 i86pc\n```\n\n\nand my Sun Ultra 27 (OpenSolaris 2009.06, upgraded to snv_134)\n\n```\ndrkirkby@hawk:~$ uname -rsm\nSunOS 5.11 i86pc\n```\n\n\nNote I did not use the unportable '-p' option. That does not work on HP-UX. \n\nSo can this get a positive review? \n\nDave",
    "created_at": "2010-07-12T07:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90877",
    "user": "drkirkby"
}
```

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

archive/issue_comments_090878.json:
```json
{
    "body": "Can you or someone test this on a few non-Solaris systems before the positive review?",
    "created_at": "2010-07-12T08:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90878",
    "user": "rlm"
}
```

Can you or someone test this on a few non-Solaris systems before the positive review?



---

archive/issue_comments_090879.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-07-12T08:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90879",
    "user": "rlm"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_090880.json:
```json
{
    "body": "Replying to [comment:8 drkirkby]:\n> Replying to [comment:4 leif]:\n> > I cannot really judge (or test) the behavior on SunOS/Solaris, though, especially regarding the test for `... 5.11 i86pc`.\n> > \n> I appreciate that. But all 3 options are POSIX, and as you say it does not break on any other platform.\n\nI had only the specific version number (and to some extent \"i86pc\") in mind, not the options to `uname`, i.e. I did not know if all affected systems report exactly the same.",
    "created_at": "2010-07-12T09:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90880",
    "user": "leif"
}
```

Replying to [comment:8 drkirkby]:
> Replying to [comment:4 leif]:
> > I cannot really judge (or test) the behavior on SunOS/Solaris, though, especially regarding the test for `... 5.11 i86pc`.
> > 
> I appreciate that. But all 3 options are POSIX, and as you say it does not break on any other platform.

I had only the specific version number (and to some extent "i86pc") in mind, not the options to `uname`, i.e. I did not know if all affected systems report exactly the same.



---

archive/issue_comments_090881.json:
```json
{
    "body": "Replying to [comment:11 leif]:\n\n> I had only the specific version number (and to some extent \"i86pc\") in mind, not the options to `uname`, i.e. I did not know if all affected systems report exactly the same.\n\nAll systems I know of report the same. It may be the problem exists on some other variations of Solaris (OpenSolaris on SPARC, Solaris 10 on x86, Solaris 10 on 64-bit SPARC), but I don't know that. Hence it is restricted to only the systems where I know its a problem. \n\nDave",
    "created_at": "2010-07-12T10:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90881",
    "user": "drkirkby"
}
```

Replying to [comment:11 leif]:

> I had only the specific version number (and to some extent "i86pc") in mind, not the options to `uname`, i.e. I did not know if all affected systems report exactly the same.

All systems I know of report the same. It may be the problem exists on some other variations of Solaris (OpenSolaris on SPARC, Solaris 10 on x86, Solaris 10 on 64-bit SPARC), but I don't know that. Hence it is restricted to only the systems where I know its a problem. 

Dave



---

archive/issue_comments_090882.json:
```json
{
    "body": "Replying to [comment:9 rlm]:\n> Can you or someone test this on a few non-Solaris systems before the positive review?\n\n == Testing on sage.math (a Sun running Ubuntu Linux 8.04.4 LTS. ) ==\nIt built fine and failed one doctest on sage.math:\n\n\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n\tsage -t  -long devel/sage/sage/schemes/elliptic_curves/lseries_ell.py # 3 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 1076.9 secon\n```\n\n\nThis is the same failure William got with the sage-4.5.alpha4, and is a result of a lack of memory:\n\n\n```\n**********************************************************************\nFile \"/mnt/usb1/scratch/kirkby/sage-4.5.rc0/devel/sage-main/sage/schemes/elliptic_curves/lseries_ell.py\", line 226:\n    sage: E.lseries().zeros(2)\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/kirkby/sage-4.5.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/kirkby/sage-4.5.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/kirkby/sage-4.5.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_9[3]>\", line 1, in <module>\n        E.lseries().zeros(Integer(2))###line 226:\n    sage: E.lseries().zeros(2)\n      File \"/mnt/usb1/scratch/kirkby/sage-4.5.rc0/local/lib/python/site-packages/sage/schemes/elliptic_curves/lseries_ell.py\", line 236, in zeros\n        return lcalc.zeros(n, L=self.__E)\n      File \"/mnt/usb1/scratch/kirkby/sage-4.5.rc0/local/lib/python/site-packages/sage/lfunctions/lcalc.py\", line 125, in zeros\n        X = self('-z %s %s'%(int(n), L))\n      File \"/mnt/usb1/scratch/kirkby/sage-4.5.rc0/local/lib/python/site-packages/sage/lfunctions/lcalc.py\", line 65, in __call__\n        return os.popen(cmd).read().strip()\n    OSError: [Errno 12] Cannot allocate memory\n**********************************************************************\n```\n\n\nI don't know how much memory that tests needs, but its passed for me before. Perhaps it needs more RAM than other tests. \n\nI'll test on OS X (bsd.math) too, but note the changes are Solaris specific, so Linux and OX X should see exactly the same code. \n\nDave",
    "created_at": "2010-07-12T12:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90882",
    "user": "drkirkby"
}
```

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

archive/issue_comments_090883.json:
```json
{
    "body": "I successfully installed the spkg linked here onto a build of 4.5.rc0, and am now testing the sage library.  I ignored the two patches on this ticket since they appear to be changes to an spkg.   If this is wrong (i.e. if I need to do something with the two patches before testing) please tell me.\n\nThis is on an AMD Opteron running ubuntu linux.",
    "created_at": "2010-07-12T13:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90883",
    "user": "cremona"
}
```

I successfully installed the spkg linked here onto a build of 4.5.rc0, and am now testing the sage library.  I ignored the two patches on this ticket since they appear to be changes to an spkg.   If this is wrong (i.e. if I need to do something with the two patches before testing) please tell me.

This is on an AMD Opteron running ubuntu linux.



---

archive/issue_comments_090884.json:
```json
{
    "body": "Replying to [comment:14 cremona]:\n> I successfully installed the spkg linked here onto a build of 4.5.rc0, and am now testing the sage library.  \n\nThank you. \n\n> I ignored the two patches on this ticket since they appear to be changes to an spkg.   If this is wrong (i.e. if I need to do something with the two patches before testing) please tell me.\n\nThat is not wrong. The patches are already in the .spkg, so you do not need to apply. \n \n> This is on an AMD Opteron running ubuntu linux.\n\nDave",
    "created_at": "2010-07-12T13:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90884",
    "user": "drkirkby"
}
```

Replying to [comment:14 cremona]:
> I successfully installed the spkg linked here onto a build of 4.5.rc0, and am now testing the sage library.  

Thank you. 

> I ignored the two patches on this ticket since they appear to be changes to an spkg.   If this is wrong (i.e. if I need to do something with the two patches before testing) please tell me.

That is not wrong. The patches are already in the .spkg, so you do not need to apply. 
 
> This is on an AMD Opteron running ubuntu linux.

Dave



---

archive/issue_comments_090885.json:
```json
{
    "body": "OK then, I can now report that testing the whole Sage library worked fine after installing the new spkg.",
    "created_at": "2010-07-12T13:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90885",
    "user": "cremona"
}
```

OK then, I can now report that testing the whole Sage library worked fine after installing the new spkg.



---

archive/issue_comments_090886.json:
```json
{
    "body": "The new spkg (actually this one plus the patch at #9187) installs for me on OS X 10.6 when building spkgs in parallel.  I haven't gotten to the doctesting part of things, but if there are problems, I'll report them here.",
    "created_at": "2010-07-12T21:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90886",
    "user": "jhpalmieri"
}
```

The new spkg (actually this one plus the patch at #9187) installs for me on OS X 10.6 when building spkgs in parallel.  I haven't gotten to the doctesting part of things, but if there are problems, I'll report them here.



---

archive/issue_comments_090887.json:
```json
{
    "body": "All doctests pass for me on OS X 10.6.  The new spkg also has built successfully on t2.math, and I'm running doctests now.",
    "created_at": "2010-07-13T02:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90887",
    "user": "jhpalmieri"
}
```

All doctests pass for me on OS X 10.6.  The new spkg also has built successfully on t2.math, and I'm running doctests now.



---

archive/issue_comments_090888.json:
```json
{
    "body": "Replying to [comment:18 jhpalmieri]:\n> All doctests pass for me on OS X 10.6.  The new spkg also has built successfully on t2.math, and I'm running doctests now.\n\nI looked in John's directory `/scratch/palmieri/sage-4.5.rc0` on t2.math, and see the doctests had completed with 7 failures. However, three of those end with `# File not found` which is actually just a timeout - hopefully #9316 should fix that bug. After running the tests that failed for John at the command line, with longer timeouts, I find there are two failures which will not go away. \n\n\n```\n\tsage -t -long \"devel/sage/doc/en/thematic_tutorials/group_theory.rst\"\n\tsage -t -long \"devel/sage/sage/libs/galrep/wrapper.pyx\"\n```\n\n\nThose two failures need to be resolved. I created tickets (#9489 and #9490) for these two doctest failures. \n\nThe longest test was:\n\n\n```\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"\n\t [3023.2 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 3023.2 seconds\n```\n\n\nso it looks like one needs a SAGE_TIMEOUT_LONG >= 3600 seconds (one hour) to be reasonably confident of not getting a timeout on 't2.math'. \n\nDave",
    "created_at": "2010-07-13T14:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90888",
    "user": "drkirkby"
}
```

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

archive/issue_comments_090889.json:
```json
{
    "body": "John's successful tests would appear to have been built with `ecl-10.2.1.p1.spkg` from #9187, which has these changes, **plus** the changes to allow better building in parallel. I'm basing this on the fact that John has the ecl-10.2.1.p1.spkg in his directory, but not the ecl-10.2.1.p0.spkg I created.  \n\n\n```\nkirkby@t2:[/scratch/palmieri/sage-4.5.rc0/spkg/standard] $ ls -l ecl-*\n-rw-r--r--   1 palmieri 1005     4850369 Jul 12 13:31 ecl-10.2.1.p1.spkg\n-rw-r--r--   1 palmieri 1005     4820179 Jul 11 12:12 ecl-10.2.1.spkg\n```\n\n\nMy successful tests on OS X were also using ecl-10.2.1.p1.spkg from #9187.\n\nDave",
    "created_at": "2010-07-13T16:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90889",
    "user": "drkirkby"
}
```

John's successful tests would appear to have been built with `ecl-10.2.1.p1.spkg` from #9187, which has these changes, **plus** the changes to allow better building in parallel. I'm basing this on the fact that John has the ecl-10.2.1.p1.spkg in his directory, but not the ecl-10.2.1.p0.spkg I created.  


```
kirkby@t2:[/scratch/palmieri/sage-4.5.rc0/spkg/standard] $ ls -l ecl-*
-rw-r--r--   1 palmieri 1005     4850369 Jul 12 13:31 ecl-10.2.1.p1.spkg
-rw-r--r--   1 palmieri 1005     4820179 Jul 11 12:12 ecl-10.2.1.spkg
```


My successful tests on OS X were also using ecl-10.2.1.p1.spkg from #9187.

Dave



---

archive/issue_comments_090890.json:
```json
{
    "body": "Replying to [comment:20 drkirkby]:\n> John's successful tests would appear to have been built with `ecl-10.2.1.p1.spkg` from #9187, which has these changes, **plus** the changes to allow better building in parallel. \n\nYes, that's right.  That's what I meant in [my comment above](http://trac.sagemath.org/sage_trac/ticket/9474#comment:17).\n\nI'm marking this as \"positive review\" since it builds on sage.math, OS X, and t2 without problem.\n\nBy the way, Dave, my build on t2 only took 2 hours this time (!) -- this is without ATLAS and the docs, of course.  Some of the speedup is probably because of building in /scratch instead of /home, so thanks for that pointer.",
    "created_at": "2010-07-13T17:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90890",
    "user": "jhpalmieri"
}
```

Replying to [comment:20 drkirkby]:
> John's successful tests would appear to have been built with `ecl-10.2.1.p1.spkg` from #9187, which has these changes, **plus** the changes to allow better building in parallel. 

Yes, that's right.  That's what I meant in [my comment above](http://trac.sagemath.org/sage_trac/ticket/9474#comment:17).

I'm marking this as "positive review" since it builds on sage.math, OS X, and t2 without problem.

By the way, Dave, my build on t2 only took 2 hours this time (!) -- this is without ATLAS and the docs, of course.  Some of the speedup is probably because of building in /scratch instead of /home, so thanks for that pointer.



---

archive/issue_comments_090891.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-13T17:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90891",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090892.json:
```json
{
    "body": "Merged, but as part of #9187.",
    "created_at": "2010-07-13T18:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90892",
    "user": "rlm"
}
```

Merged, but as part of #9187.



---

archive/issue_comments_090893.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-13T18:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9474#issuecomment-90893",
    "user": "rlm"
}
```

Resolution: fixed
