# Issue 9486: ECL 10.2.1 fails to install on OS X (bsd.math) in sage-4.5.rc0

archive/issues_009486.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nFollowing a decision to roll back the version of ECL and remove a patch from maxima\n\n|                    |                |        |\n|--------------------|----------------|--------|\n|**sage-4.5.alpha4** |**sage-4.5.rc0**|*Notes*'|\n|ecl-10.4.1 | ecl-10.2.1 ||\n|maxima-5.20.1.p1 |maxima-5.20.1.p0 | Removing #8645|\nmy attempts to build on OS X have constantly failed unless I install ecl manually from sage. \n\n\n```\n$ export MAKE=\"make -j3\"\n$ export SAGE_PARALLEL_SPKG_BUILD=yes\n$ make # First try\n$ make # Second try\n$ make # Third try\n$ ./sage -f ecl-10.2.1 # Give up, use 'sage' to install ECL\n```\n\n\nI get exactly the same error if I use ecl-10.2.1.p0, which has a couple of Solaris/OpenSolaris specific patches contained on #9474. \n\nThe error message the build fails with is:\n\n\n```\ncat /Users/kirkby/sage-4.5.rc0/spkg/build/ecl-10.2.1/src/src/c/symbols_list.h | \\\n\tsed -e 's%{\\([A-Z ]*.*\".*\"\\),[^,]*,[ ]*NULL,.*}%{\\1,NULL}%g' \\\n\t    -e 's%{\\([A-Z ]*.*\".*\"\\),[^,]*,[ ]*\\([^,]*\\),.*}%{\\1,\"\\2\"}%g' \\\n\t    -e 's%{NULL.*%{NULL,NULL}};%' > /Users/kirkby/sage-4.5.rc0/spkg/build/ecl-10.2.1/src/src/c/symbols_list2.h\nif test -f ../CROSS-DPP ; then ../CROSS-DPP /Users/kirkby/sage-4.5.rc0/spkg/build/ecl-10.2.1/src/src/c/main.d tmp.c ; else ./dpp /Users/kirkby/sage-4.5.rc0/spkg/build/ecl-10.2.1/src/src/c/main.d tmp.c ; fi\n/bin/sh: ./dpp: No such file or directory\nmake[4]: *** [main.o] Error 127\nmake[3]: *** [libeclmin.a] Error 2\nmake[2]: *** [all] Error 2\nFailed to build ECL ... exiting\n\nreal\t1m59.589s\nuser\t0m17.877s\nsys\t0m31.643s\nsage: An error occurred while installing ecl-10.2.1\n```\n\n\nThis error has also been seen with ecl-9.8.4 in sage-4.1.2.alpha2. \n\nhttp://www.mail-archive.com/sage-devel`@`googlegroups.com/msg29628.html\n\nI'm attaching a log file \n\n`sage-4.5.rc0/spkg/logs/ecl-10.2.1.log`\n\nwhich shows 3 failed builds using ecl-10.2.1\n\n\nI'm also attaching a log which just shows one failed build using ecl-10.2.1.p0 from #9474. Unlike the case with ecl-10.2.1, I did not attempt the installation multiple times, or install it manually. Hence this log file is shorter.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9486\n\n",
    "created_at": "2010-07-12T20:35:59Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "ECL 10.2.1 fails to install on OS X (bsd.math) in sage-4.5.rc0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9486",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

Following a decision to roll back the version of ECL and remove a patch from maxima

|                    |                |        |
|--------------------|----------------|--------|
|**sage-4.5.alpha4** |**sage-4.5.rc0**|*Notes*'|
|ecl-10.4.1 | ecl-10.2.1 ||
|maxima-5.20.1.p1 |maxima-5.20.1.p0 | Removing #8645|
my attempts to build on OS X have constantly failed unless I install ecl manually from sage. 


```
$ export MAKE="make -j3"
$ export SAGE_PARALLEL_SPKG_BUILD=yes
$ make # First try
$ make # Second try
$ make # Third try
$ ./sage -f ecl-10.2.1 # Give up, use 'sage' to install ECL
```


I get exactly the same error if I use ecl-10.2.1.p0, which has a couple of Solaris/OpenSolaris specific patches contained on #9474. 

The error message the build fails with is:


```
cat /Users/kirkby/sage-4.5.rc0/spkg/build/ecl-10.2.1/src/src/c/symbols_list.h | \
	sed -e 's%{\([A-Z ]*.*".*"\),[^,]*,[ ]*NULL,.*}%{\1,NULL}%g' \
	    -e 's%{\([A-Z ]*.*".*"\),[^,]*,[ ]*\([^,]*\),.*}%{\1,"\2"}%g' \
	    -e 's%{NULL.*%{NULL,NULL}};%' > /Users/kirkby/sage-4.5.rc0/spkg/build/ecl-10.2.1/src/src/c/symbols_list2.h
if test -f ../CROSS-DPP ; then ../CROSS-DPP /Users/kirkby/sage-4.5.rc0/spkg/build/ecl-10.2.1/src/src/c/main.d tmp.c ; else ./dpp /Users/kirkby/sage-4.5.rc0/spkg/build/ecl-10.2.1/src/src/c/main.d tmp.c ; fi
/bin/sh: ./dpp: No such file or directory
make[4]: *** [main.o] Error 127
make[3]: *** [libeclmin.a] Error 2
make[2]: *** [all] Error 2
Failed to build ECL ... exiting

real	1m59.589s
user	0m17.877s
sys	0m31.643s
sage: An error occurred while installing ecl-10.2.1
```


This error has also been seen with ecl-9.8.4 in sage-4.1.2.alpha2. 

http://www.mail-archive.com/sage-devel`@`googlegroups.com/msg29628.html

I'm attaching a log file 

`sage-4.5.rc0/spkg/logs/ecl-10.2.1.log`

which shows 3 failed builds using ecl-10.2.1


I'm also attaching a log which just shows one failed build using ecl-10.2.1.p0 from #9474. Unlike the case with ecl-10.2.1, I did not attempt the installation multiple times, or install it manually. Hence this log file is shorter.

Issue created by migration from https://trac.sagemath.org/ticket/9486





---

archive/issue_comments_091072.json:
```json
{
    "body": "One failed build on OS X  (bsd.math). No attempt was made to install this manually, or try more than once.",
    "created_at": "2010-07-12T20:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91072",
    "user": "drkirkby"
}
```

One failed build on OS X  (bsd.math). No attempt was made to install this manually, or try more than once.



---

archive/issue_comments_091073.json:
```json
{
    "body": "Attachment [ecl-10.2.1.log](tarball://root/attachments/some-uuid/ticket9486/ecl-10.2.1.log) by drkirkby created at 2010-07-12 20:39:54\n\nLog of failed build on OS X using the ECL from sage-4.5.rc0. Three attempts were made to install via 'make' all failed. The last attempt, using 'sage' worked.",
    "created_at": "2010-07-12T20:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91073",
    "user": "drkirkby"
}
```

Attachment [ecl-10.2.1.log](tarball://root/attachments/some-uuid/ticket9486/ecl-10.2.1.log) by drkirkby created at 2010-07-12 20:39:54

Log of failed build on OS X using the ECL from sage-4.5.rc0. Three attempts were made to install via 'make' all failed. The last attempt, using 'sage' worked.



---

archive/issue_comments_091074.json:
```json
{
    "body": "I think this is a duplicate of #9187.",
    "created_at": "2010-07-12T21:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91074",
    "user": "jhpalmieri"
}
```

I think this is a duplicate of #9187.



---

archive/issue_comments_091075.json:
```json
{
    "body": "Dave, can you upload the spkg log of ecl-10.2.1.p1 on bsd.math, too?",
    "created_at": "2010-07-12T22:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91075",
    "user": "leif"
}
```

Dave, can you upload the spkg log of ecl-10.2.1.p1 on bsd.math, too?



---

archive/issue_comments_091076.json:
```json
{
    "body": "Replying to [comment:1 jhpalmieri]:\n> I think this is a duplicate of #9187.\nI suspect the issue will be resolved by #9187, though I'd rather not close it as a duplicate just now. The issue could be a different one, though the fact ecl failed to build every time before adding #9187, does make me think that #9197 will resolve it. But a lot of issues in this version of Sage seem to fail on one occasion and work on another. I'm taking nothing for granted just yet!\n\nDave",
    "created_at": "2010-07-12T22:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91076",
    "user": "drkirkby"
}
```

Replying to [comment:1 jhpalmieri]:
> I think this is a duplicate of #9187.
I suspect the issue will be resolved by #9187, though I'd rather not close it as a duplicate just now. The issue could be a different one, though the fact ecl failed to build every time before adding #9187, does make me think that #9197 will resolve it. But a lot of issues in this version of Sage seem to fail on one occasion and work on another. I'm taking nothing for granted just yet!

Dave



---

archive/issue_comments_091077.json:
```json
{
    "body": "Attachment [ecl-10.2.1.p1.log](tarball://root/attachments/some-uuid/ticket9486/ecl-10.2.1.p1.log) by drkirkby created at 2010-07-12 22:16:58\n\nLog of failed successful build on OS X (bsd.math) using the ecl-10.2.1.p1 produced by mpatel. This built ecl ok. The complete build of sage has not completed.",
    "created_at": "2010-07-12T22:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91077",
    "user": "drkirkby"
}
```

Attachment [ecl-10.2.1.p1.log](tarball://root/attachments/some-uuid/ticket9486/ecl-10.2.1.p1.log) by drkirkby created at 2010-07-12 22:16:58

Log of failed successful build on OS X (bsd.math) using the ecl-10.2.1.p1 produced by mpatel. This built ecl ok. The complete build of sage has not completed.



---

archive/issue_comments_091078.json:
```json
{
    "body": "Replying to [comment:2 leif]:\n> Dave, can you upload the spkg log of ecl-10.2.1.p1 on bsd.math, too?\n> \nYep, done it already.",
    "created_at": "2010-07-12T22:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91078",
    "user": "drkirkby"
}
```

Replying to [comment:2 leif]:
> Dave, can you upload the spkg log of ecl-10.2.1.p1 on bsd.math, too?
> 
Yep, done it already.



---

archive/issue_comments_091079.json:
```json
{
    "body": "The comment on the log file shows \n\n*Log of failed successful build on OS X (bsd.math) using the ecl-10.2.1.p1 produced by mpatel. This built ecl ok. The complete build of sage has not completed.* \n\nThe word *failed* should be removed, as this was successful at building ecl on bsd.math.\n\nDave",
    "created_at": "2010-07-12T22:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91079",
    "user": "drkirkby"
}
```

The comment on the log file shows 

*Log of failed successful build on OS X (bsd.math) using the ecl-10.2.1.p1 produced by mpatel. This built ecl ok. The complete build of sage has not completed.* 

The word *failed* should be removed, as this was successful at building ecl on bsd.math.

Dave



---

archive/issue_comments_091080.json:
```json
{
    "body": "Changing assignee from GeorgSWeber to drkirkby.",
    "created_at": "2010-07-12T22:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91080",
    "user": "drkirkby"
}
```

Changing assignee from GeorgSWeber to drkirkby.



---

archive/issue_comments_091081.json:
```json
{
    "body": "Replying to [comment:4 drkirkby]:\n> Replying to [comment:2 leif]:\n> > Dave, can you upload the spkg log of ecl-10.2.1.p1 on bsd.math, too?\n> > \n> Yep, done it already. \nThis is most probably **not** what we want:\n\n```\n...\nconfigure: Configuring included Boehm GC library:\nchecking build system type... i386-apple-darwin10.4.0\nchecking host system type... i386-apple-darwin10.4.0\nchecking target system type... i386-apple-darwin10.4.0\nchecking GC version numbers... major=7 minor=1 \n...\n```\n\n(We should remove Boehm GC from ECL's source tree anyway, besides the directories mentioned in `SPKG.txt`'s \"Special Update/Build Instructions\".)\n\nThis *might* be the cause of other strange (doctest) errors on MacOS X.",
    "created_at": "2010-07-12T23:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91081",
    "user": "leif"
}
```

Replying to [comment:4 drkirkby]:
> Replying to [comment:2 leif]:
> > Dave, can you upload the spkg log of ecl-10.2.1.p1 on bsd.math, too?
> > 
> Yep, done it already. 
This is most probably **not** what we want:

```
...
configure: Configuring included Boehm GC library:
checking build system type... i386-apple-darwin10.4.0
checking host system type... i386-apple-darwin10.4.0
checking target system type... i386-apple-darwin10.4.0
checking GC version numbers... major=7 minor=1 
...
```

(We should remove Boehm GC from ECL's source tree anyway, besides the directories mentioned in `SPKG.txt`'s "Special Update/Build Instructions".)

This *might* be the cause of other strange (doctest) errors on MacOS X.



---

archive/issue_comments_091082.json:
```json
{
    "body": "My build on OS X (bsd.math) completed with one doc test failure. This used:\n\n* http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg \n* Library patch at #7379 (only the file trac-7379-decorator-defaults.patch)\n\n$ make ptestlong\n\n\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n\tsage -t  -long devel/sage/sage/interfaces/sage0.py # 3 doctests failed\n----------------------------------------------------------------------\n```\n\n\nI've attached the ptestlong.log (renamed to bsd.math+7379+9187-ptestlong.log). After that one test failed, I run it again from the command line:\n\n\n```\n[kirkby@bsd sage-4.5.rc0]$ ./sage -t  -long devel/sage/sage/interfaces/sage0.py                 \nsage -t -long \"devel/sage/sage/interfaces/sage0.py\"         \n\t [13.7 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 13.7 seconds\n[kirkby@bsd sage-4.5.rc0]$ \n```\n\n\nIt's difficult to really trust anything, when tests results are not reproducible. \n\nLine 3527 looks a bit odd in the log of the tests. \n\nDave",
    "created_at": "2010-07-13T01:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91082",
    "user": "drkirkby"
}
```

My build on OS X (bsd.math) completed with one doc test failure. This used:

* http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg 
* Library patch at #7379 (only the file trac-7379-decorator-defaults.patch)

$ make ptestlong


```
----------------------------------------------------------------------

The following tests failed:

	sage -t  -long devel/sage/sage/interfaces/sage0.py # 3 doctests failed
----------------------------------------------------------------------
```


I've attached the ptestlong.log (renamed to bsd.math+7379+9187-ptestlong.log). After that one test failed, I run it again from the command line:


```
[kirkby@bsd sage-4.5.rc0]$ ./sage -t  -long devel/sage/sage/interfaces/sage0.py                 
sage -t -long "devel/sage/sage/interfaces/sage0.py"         
	 [13.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 13.7 seconds
[kirkby@bsd sage-4.5.rc0]$ 
```


It's difficult to really trust anything, when tests results are not reproducible. 

Line 3527 looks a bit odd in the log of the tests. 

Dave



---

archive/issue_comments_091083.json:
```json
{
    "body": "Test results on bsd.math. Note the strange characters on line 3527. The test latter passed.",
    "created_at": "2010-07-13T01:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91083",
    "user": "drkirkby"
}
```

Test results on bsd.math. Note the strange characters on line 3527. The test latter passed.



---

archive/issue_comments_091084.json:
```json
{
    "body": "Attachment [bsd.math+7379+9187-ptestlong.log](tarball://root/attachments/some-uuid/ticket9486/bsd.math+7379+9187-ptestlong.log) by drkirkby created at 2010-07-13 09:58:08\n\nHere's a list of the order in which the packages were installed in a parallel build on bsd.math. Do these look right? Note boehm_gc was built 10 minutes before ecl. `spkg/standard/deps` does list BOEHM_GC as being a depenancy of ecl. I think leif is saying we should ensure ecl uses the Boehm garbage collector supplied with Sage, rather than the one built into the ECL source code. \n\n\n```\n[kirkby@bsd sage-4.5.rc0]$ ls -lrt spkg/installed\ntotal 380\n-rw-r--r-- 1 kirkby staff   0 Jul 12 14:02 dir-0.1\n-rw-r--r-- 1 kirkby staff   0 Jul 12 14:02 prereq-0.7\n-rw-r--r-- 1 kirkby staff 314 Jul 12 14:02 sage_scripts-4.5.rc0\n-rw-r--r-- 1 kirkby staff   0 Jul 12 14:02 bzip2-1.0.5\n-rw-r--r-- 1 kirkby staff 310 Jul 12 14:02 termcap-1.3.1.p1\n-rw-r--r-- 1 kirkby staff 304 Jul 12 14:02 zlib-1.2.5\n-rw-r--r-- 1 kirkby staff 310 Jul 12 14:02 fortran-20100629\n-rw-r--r-- 1 kirkby staff 309 Jul 12 14:02 iconv-1.13.1.p2\n-rw-r--r-- 1 kirkby staff 307 Jul 12 14:02 blas-20070724\n-rw-r--r-- 1 kirkby staff 310 Jul 12 14:03 libpng-1.2.35.p2\n-rw-r--r-- 1 kirkby staff 314 Jul 12 14:03 boost-cropped-1.34.1\n-rw-r--r-- 1 kirkby staff 309 Jul 12 14:03 readline-6.0.p2\n-rw-r--r-- 1 kirkby staff 304 Jul 12 14:04 cephes-2.8\n-rw-r--r-- 1 kirkby staff 316 Jul 12 14:04 conway_polynomials-0.2\n-rw-r--r-- 1 kirkby staff 309 Jul 12 14:04 boehm_gc-7.1.p6\n-rw-r--r-- 1 kirkby staff 313 Jul 12 14:04 elliptic_curves-0.1\n-rw-r--r-- 1 kirkby staff 310 Jul 12 14:04 examples-4.5.rc0\n-rw-r--r-- 1 kirkby staff 309 Jul 12 14:04 f2c-20070816.p2\n-rw-r--r-- 1 kirkby staff 312 Jul 12 14:04 graphs-20070722.p1\n-rw-r--r-- 1 kirkby staff 311 Jul 12 14:05 freetype-2.3.5.p2\n-rw-r--r-- 1 kirkby staff 313 Jul 12 14:05 rubiks-20070912.p12\n-rw-r--r-- 1 kirkby staff 310 Jul 12 14:05 libm4ri-20100221\n-rw-r--r-- 1 kirkby staff 315 Jul 12 14:06 polytopes_db-20100210\n-rw-r--r-- 1 kirkby staff 305 Jul 12 14:06 palp-1.1.p3\n-rw-r--r-- 1 kirkby staff 311 Jul 12 14:06 sympow-1.018.1.p7\n-rw-r--r-- 1 kirkby staff 314 Jul 12 14:06 tachyon-0.98beta.p11\n-rw-r--r-- 1 kirkby staff 307 Jul 12 14:07 mpir-1.2.2.p1\n-rw-r--r-- 1 kirkby staff 312 Jul 12 14:08 lapack-20071123.p1\n-rw-r--r-- 1 kirkby staff 307 Jul 12 14:09 sqlite-3.6.22\n-rw-r--r-- 1 kirkby staff 311 Jul 12 14:09 symmetrica-2.0.p5\n-rw-r--r-- 1 kirkby staff 313 Jul 12 14:09 libgpg_error-1.6.p3\n-rw-r--r-- 1 kirkby staff 308 Jul 12 14:10 cddlib-094f.p7\n-rw-r--r-- 1 kirkby staff 307 Jul 12 14:10 pari-2.3.5.p1\n-rw-r--r-- 1 kirkby staff 306 Jul 12 14:11 ecm-6.2.1.p2\n-rw-r--r-- 1 kirkby staff 313 Jul 12 14:11 flintqs-20070817.p5\n-rw-r--r-- 1 kirkby staff 307 Jul 12 14:14 ecl-10.2.1.p1\n-rw-r--r-- 1 kirkby staff 316 Jul 12 14:14 genus2reduction-0.3.p6\n-rw-r--r-- 1 kirkby staff 304 Jul 12 14:14 mpfr-2.4.2\n-rw-r--r-- 1 kirkby staff 307 Jul 12 14:15 ntl-5.4.2.p12\n-rw-r--r-- 1 kirkby staff 306 Jul 12 14:15 gd-2.0.35.p5\n-rw-r--r-- 1 kirkby staff 303 Jul 12 14:16 glpk-4.44\n-rw-r--r-- 1 kirkby staff 319 Jul 12 14:16 mpfi-1.3.4-cvs20071125.p8\n-rw-r--r-- 1 kirkby staff 312 Jul 12 14:16 ratpoints-2.1.3.p1\n-rw-r--r-- 1 kirkby staff 313 Jul 12 14:16 givaro-3.2.13rc2.p1\n-rw-r--r-- 1 kirkby staff 309 Jul 12 14:18 gfan-0.4plus.p1\n-rw-r--r-- 1 kirkby staff 308 Jul 12 14:18 zn_poly-0.9.p4\n-rw-r--r-- 1 kirkby staff 316 Jul 12 14:18 lcalc-20100428-1.23.p0\n-rw-r--r-- 1 kirkby staff 312 Jul 12 14:19 libgcrypt-1.4.4.p3\n-rw-r--r-- 1 kirkby staff 312 Jul 12 14:23 eclib-20080310.p10\n-rw-r--r-- 1 kirkby staff 308 Jul 12 14:23 flint-1.5.0.p5\n-rw-r--r-- 1 kirkby staff 312 Jul 12 14:24 libfplll-3.0.12.p0\n-rw-r--r-- 1 kirkby staff 310 Jul 12 14:25 opencdk-0.6.6.p5\n-rw-r--r-- 1 kirkby staff 310 Jul 12 14:29 maxima-5.20.1.p0\n-rw-r--r-- 1 kirkby staff 309 Jul 12 14:29 gnutls-2.2.1.p5\n-rw-r--r-- 1 kirkby staff 313 Jul 12 14:32 singular-3.1.0.4.p7\n-rw-r--r-- 1 kirkby staff 309 Jul 12 14:33 python-2.6.4.p9\n-rw-r--r-- 1 kirkby staff 305 Jul 12 14:34 scons-1.2.0\n-rw-r--r-- 1 kirkby staff 309 Jul 12 14:34 atlas-3.8.3.p12\n-rw-r--r-- 1 kirkby staff 309 Jul 12 14:34 docutils-0.5.p0\n-rw-r--r-- 1 kirkby staff 310 Jul 12 14:34 gdmodule-0.56.p7\n-rw-r--r-- 1 kirkby staff 312 Jul 12 14:34 mercurial-1.3.1.p2\n-rw-r--r-- 1 kirkby staff 310 Jul 12 14:34 ipython-0.9.1.p0\n-rw-r--r-- 1 kirkby staff 305 Jul 12 14:34 mpmath-0.15\n-rw-r--r-- 1 kirkby staff 308 Jul 12 14:34 networkx-1.0.1\n-rw-r--r-- 1 kirkby staff 308 Jul 12 14:34 pexpect-2.0.p4\n-rw-r--r-- 1 kirkby staff 307 Jul 12 14:35 cython-0.12.1\n-rw-r--r-- 1 kirkby staff 311 Jul 12 14:35 pycrypto-2.0.1.p5\n-rw-r--r-- 1 kirkby staff 308 Jul 12 14:39 pynac-0.2.0.p3\n-rw-r--r-- 1 kirkby staff 305 Jul 12 14:41 gsl-1.10.p2\n-rw-r--r-- 1 kirkby staff 316 Jul 12 14:42 python_gnutls-1.1.4.p7\n-rw-r--r-- 1 kirkby staff 313 Jul 12 14:42 setuptools-0.6c9.p0\n-rw-r--r-- 1 kirkby staff 308 Jul 12 14:42 sympy-0.6.4.p0\n-rw-r--r-- 1 kirkby staff 306 Jul 12 14:42 pil-1.1.6.p2\n-rw-r--r-- 1 kirkby staff 308 Jul 12 14:42 cliquer-1.2.p5\n-rw-r--r-- 1 kirkby staff 308 Jul 12 14:44 numpy-1.3.0.p3\n-rw-r--r-- 1 kirkby staff 309 Jul 12 14:45 extcode-4.5.rc0\n-rw-r--r-- 1 kirkby staff 307 Jul 12 14:46 iml-1.0.1.p12\n-rw-r--r-- 1 kirkby staff 311 Jul 12 14:46 polybori-0.6.4.p1\n-rw-r--r-- 1 kirkby staff 311 Jul 12 14:49 matplotlib-0.99.3\n-rw-r--r-- 1 kirkby staff 308 Jul 12 14:50 twisted-9.0.p2\n-rw-r--r-- 1 kirkby staff 309 Jul 12 14:52 linbox-1.1.6.p3\n-rw-r--r-- 1 kirkby staff 308 Jul 12 14:52 weave-0.4.9.p0\n-rw-r--r-- 1 kirkby staff 307 Jul 12 14:54 cvxopt-0.9.p8\n-rw-r--r-- 1 kirkby staff 308 Jul 12 14:55 zodb3-3.7.0.p4\n-rw-r--r-- 1 kirkby staff 312 Jul 12 14:55 pygments-0.11.1.p0\n-rw-r--r-- 1 kirkby staff 306 Jul 12 14:55 jinja-1.2.p0\n-rw-r--r-- 1 kirkby staff 309 Jul 12 14:55 jinja2-2.1.1.p0\n-rw-r--r-- 1 kirkby staff 309 Jul 12 14:55 sphinx-0.6.3.p4\n-rw-r--r-- 1 kirkby staff 310 Jul 12 14:56 sqlalchemy-0.5.8\n-rw-r--r-- 1 kirkby staff 306 Jul 12 14:57 sagenb-0.8.1\n-rw-r--r-- 1 kirkby staff 304 Jul 12 14:57 rpy2-2.0.8\n-rw-r--r-- 1 kirkby staff 305 Jul 12 14:58 r-2.10.1.p2\n-rw-r--r-- 1 kirkby staff 306 Jul 12 15:02 scipy-0.7.p5\n-rw-r--r-- 1 kirkby staff 319 Jul 12 15:03 scipy_sandbox-20071020.p5\n-rw-r--r-- 1 kirkby staff 307 Jul 12 15:03 moin-1.9.1.p1\n-rw-r--r-- 1 kirkby staff 306 Jul 12 15:17 sage-4.5.rc0\n-rw-r--r-- 1 kirkby staff 307 Jul 12 15:18 gap-4.4.12.p4\n-rw-r--r-- 1 kirkby staff 307 Jul 12 15:18 sagetex-2.2.5\n[kirkby@bsd sage-4.5.rc0]$ \n```\n\n\nSince running the long doctests, with the one failure `devel/sage/sage/interfaces/sage0.py`, I've run the long doctests again, without rebuilding Sage - just re-running the doctests. The one failure is reproducible. That test always fails when running `make ptestlong`\n\nHowever, equally reproducible is fact this test passes at the command line if one invokes Sage directly. \n\n\n```\n[kirkby@bsd sage-4.5.rc0]$ ./sage -t  -long devel/sage/sage/interfaces/sage0.py\nsage -t -long \"devel/sage/sage/interfaces/sage0.py\"         \n\t [16.9 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 16.9 seconds\n[kirkby@bsd sage-4.5.rc0]$ ./sage -t  -long devel/sage/sage/interfaces/sage0.py\nsage -t -long \"devel/sage/sage/interfaces/sage0.py\"         \n\t [12.7 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 12.7 seconds\n[kirkby@bsd sage-4.5.rc0]$ ./sage -t  -long devel/sage/sage/interfaces/sage0.py\nsage -t -long \"devel/sage/sage/interfaces/sage0.py\"         \n\t [18.6 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 18.6 seconds\n```\n\n\nTwo other experiments that may be useful to perform would be:\n\n* Determine if this test fails if one runs `make testlong` rather than `make ptestlong`\n* Determine if rebuilding Sage produces the same result each time. \n\n\nDave",
    "created_at": "2010-07-13T09:58:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91084",
    "user": "drkirkby"
}
```

Attachment [bsd.math+7379+9187-ptestlong.log](tarball://root/attachments/some-uuid/ticket9486/bsd.math+7379+9187-ptestlong.log) by drkirkby created at 2010-07-13 09:58:08

Here's a list of the order in which the packages were installed in a parallel build on bsd.math. Do these look right? Note boehm_gc was built 10 minutes before ecl. `spkg/standard/deps` does list BOEHM_GC as being a depenancy of ecl. I think leif is saying we should ensure ecl uses the Boehm garbage collector supplied with Sage, rather than the one built into the ECL source code. 


```
[kirkby@bsd sage-4.5.rc0]$ ls -lrt spkg/installed
total 380
-rw-r--r-- 1 kirkby staff   0 Jul 12 14:02 dir-0.1
-rw-r--r-- 1 kirkby staff   0 Jul 12 14:02 prereq-0.7
-rw-r--r-- 1 kirkby staff 314 Jul 12 14:02 sage_scripts-4.5.rc0
-rw-r--r-- 1 kirkby staff   0 Jul 12 14:02 bzip2-1.0.5
-rw-r--r-- 1 kirkby staff 310 Jul 12 14:02 termcap-1.3.1.p1
-rw-r--r-- 1 kirkby staff 304 Jul 12 14:02 zlib-1.2.5
-rw-r--r-- 1 kirkby staff 310 Jul 12 14:02 fortran-20100629
-rw-r--r-- 1 kirkby staff 309 Jul 12 14:02 iconv-1.13.1.p2
-rw-r--r-- 1 kirkby staff 307 Jul 12 14:02 blas-20070724
-rw-r--r-- 1 kirkby staff 310 Jul 12 14:03 libpng-1.2.35.p2
-rw-r--r-- 1 kirkby staff 314 Jul 12 14:03 boost-cropped-1.34.1
-rw-r--r-- 1 kirkby staff 309 Jul 12 14:03 readline-6.0.p2
-rw-r--r-- 1 kirkby staff 304 Jul 12 14:04 cephes-2.8
-rw-r--r-- 1 kirkby staff 316 Jul 12 14:04 conway_polynomials-0.2
-rw-r--r-- 1 kirkby staff 309 Jul 12 14:04 boehm_gc-7.1.p6
-rw-r--r-- 1 kirkby staff 313 Jul 12 14:04 elliptic_curves-0.1
-rw-r--r-- 1 kirkby staff 310 Jul 12 14:04 examples-4.5.rc0
-rw-r--r-- 1 kirkby staff 309 Jul 12 14:04 f2c-20070816.p2
-rw-r--r-- 1 kirkby staff 312 Jul 12 14:04 graphs-20070722.p1
-rw-r--r-- 1 kirkby staff 311 Jul 12 14:05 freetype-2.3.5.p2
-rw-r--r-- 1 kirkby staff 313 Jul 12 14:05 rubiks-20070912.p12
-rw-r--r-- 1 kirkby staff 310 Jul 12 14:05 libm4ri-20100221
-rw-r--r-- 1 kirkby staff 315 Jul 12 14:06 polytopes_db-20100210
-rw-r--r-- 1 kirkby staff 305 Jul 12 14:06 palp-1.1.p3
-rw-r--r-- 1 kirkby staff 311 Jul 12 14:06 sympow-1.018.1.p7
-rw-r--r-- 1 kirkby staff 314 Jul 12 14:06 tachyon-0.98beta.p11
-rw-r--r-- 1 kirkby staff 307 Jul 12 14:07 mpir-1.2.2.p1
-rw-r--r-- 1 kirkby staff 312 Jul 12 14:08 lapack-20071123.p1
-rw-r--r-- 1 kirkby staff 307 Jul 12 14:09 sqlite-3.6.22
-rw-r--r-- 1 kirkby staff 311 Jul 12 14:09 symmetrica-2.0.p5
-rw-r--r-- 1 kirkby staff 313 Jul 12 14:09 libgpg_error-1.6.p3
-rw-r--r-- 1 kirkby staff 308 Jul 12 14:10 cddlib-094f.p7
-rw-r--r-- 1 kirkby staff 307 Jul 12 14:10 pari-2.3.5.p1
-rw-r--r-- 1 kirkby staff 306 Jul 12 14:11 ecm-6.2.1.p2
-rw-r--r-- 1 kirkby staff 313 Jul 12 14:11 flintqs-20070817.p5
-rw-r--r-- 1 kirkby staff 307 Jul 12 14:14 ecl-10.2.1.p1
-rw-r--r-- 1 kirkby staff 316 Jul 12 14:14 genus2reduction-0.3.p6
-rw-r--r-- 1 kirkby staff 304 Jul 12 14:14 mpfr-2.4.2
-rw-r--r-- 1 kirkby staff 307 Jul 12 14:15 ntl-5.4.2.p12
-rw-r--r-- 1 kirkby staff 306 Jul 12 14:15 gd-2.0.35.p5
-rw-r--r-- 1 kirkby staff 303 Jul 12 14:16 glpk-4.44
-rw-r--r-- 1 kirkby staff 319 Jul 12 14:16 mpfi-1.3.4-cvs20071125.p8
-rw-r--r-- 1 kirkby staff 312 Jul 12 14:16 ratpoints-2.1.3.p1
-rw-r--r-- 1 kirkby staff 313 Jul 12 14:16 givaro-3.2.13rc2.p1
-rw-r--r-- 1 kirkby staff 309 Jul 12 14:18 gfan-0.4plus.p1
-rw-r--r-- 1 kirkby staff 308 Jul 12 14:18 zn_poly-0.9.p4
-rw-r--r-- 1 kirkby staff 316 Jul 12 14:18 lcalc-20100428-1.23.p0
-rw-r--r-- 1 kirkby staff 312 Jul 12 14:19 libgcrypt-1.4.4.p3
-rw-r--r-- 1 kirkby staff 312 Jul 12 14:23 eclib-20080310.p10
-rw-r--r-- 1 kirkby staff 308 Jul 12 14:23 flint-1.5.0.p5
-rw-r--r-- 1 kirkby staff 312 Jul 12 14:24 libfplll-3.0.12.p0
-rw-r--r-- 1 kirkby staff 310 Jul 12 14:25 opencdk-0.6.6.p5
-rw-r--r-- 1 kirkby staff 310 Jul 12 14:29 maxima-5.20.1.p0
-rw-r--r-- 1 kirkby staff 309 Jul 12 14:29 gnutls-2.2.1.p5
-rw-r--r-- 1 kirkby staff 313 Jul 12 14:32 singular-3.1.0.4.p7
-rw-r--r-- 1 kirkby staff 309 Jul 12 14:33 python-2.6.4.p9
-rw-r--r-- 1 kirkby staff 305 Jul 12 14:34 scons-1.2.0
-rw-r--r-- 1 kirkby staff 309 Jul 12 14:34 atlas-3.8.3.p12
-rw-r--r-- 1 kirkby staff 309 Jul 12 14:34 docutils-0.5.p0
-rw-r--r-- 1 kirkby staff 310 Jul 12 14:34 gdmodule-0.56.p7
-rw-r--r-- 1 kirkby staff 312 Jul 12 14:34 mercurial-1.3.1.p2
-rw-r--r-- 1 kirkby staff 310 Jul 12 14:34 ipython-0.9.1.p0
-rw-r--r-- 1 kirkby staff 305 Jul 12 14:34 mpmath-0.15
-rw-r--r-- 1 kirkby staff 308 Jul 12 14:34 networkx-1.0.1
-rw-r--r-- 1 kirkby staff 308 Jul 12 14:34 pexpect-2.0.p4
-rw-r--r-- 1 kirkby staff 307 Jul 12 14:35 cython-0.12.1
-rw-r--r-- 1 kirkby staff 311 Jul 12 14:35 pycrypto-2.0.1.p5
-rw-r--r-- 1 kirkby staff 308 Jul 12 14:39 pynac-0.2.0.p3
-rw-r--r-- 1 kirkby staff 305 Jul 12 14:41 gsl-1.10.p2
-rw-r--r-- 1 kirkby staff 316 Jul 12 14:42 python_gnutls-1.1.4.p7
-rw-r--r-- 1 kirkby staff 313 Jul 12 14:42 setuptools-0.6c9.p0
-rw-r--r-- 1 kirkby staff 308 Jul 12 14:42 sympy-0.6.4.p0
-rw-r--r-- 1 kirkby staff 306 Jul 12 14:42 pil-1.1.6.p2
-rw-r--r-- 1 kirkby staff 308 Jul 12 14:42 cliquer-1.2.p5
-rw-r--r-- 1 kirkby staff 308 Jul 12 14:44 numpy-1.3.0.p3
-rw-r--r-- 1 kirkby staff 309 Jul 12 14:45 extcode-4.5.rc0
-rw-r--r-- 1 kirkby staff 307 Jul 12 14:46 iml-1.0.1.p12
-rw-r--r-- 1 kirkby staff 311 Jul 12 14:46 polybori-0.6.4.p1
-rw-r--r-- 1 kirkby staff 311 Jul 12 14:49 matplotlib-0.99.3
-rw-r--r-- 1 kirkby staff 308 Jul 12 14:50 twisted-9.0.p2
-rw-r--r-- 1 kirkby staff 309 Jul 12 14:52 linbox-1.1.6.p3
-rw-r--r-- 1 kirkby staff 308 Jul 12 14:52 weave-0.4.9.p0
-rw-r--r-- 1 kirkby staff 307 Jul 12 14:54 cvxopt-0.9.p8
-rw-r--r-- 1 kirkby staff 308 Jul 12 14:55 zodb3-3.7.0.p4
-rw-r--r-- 1 kirkby staff 312 Jul 12 14:55 pygments-0.11.1.p0
-rw-r--r-- 1 kirkby staff 306 Jul 12 14:55 jinja-1.2.p0
-rw-r--r-- 1 kirkby staff 309 Jul 12 14:55 jinja2-2.1.1.p0
-rw-r--r-- 1 kirkby staff 309 Jul 12 14:55 sphinx-0.6.3.p4
-rw-r--r-- 1 kirkby staff 310 Jul 12 14:56 sqlalchemy-0.5.8
-rw-r--r-- 1 kirkby staff 306 Jul 12 14:57 sagenb-0.8.1
-rw-r--r-- 1 kirkby staff 304 Jul 12 14:57 rpy2-2.0.8
-rw-r--r-- 1 kirkby staff 305 Jul 12 14:58 r-2.10.1.p2
-rw-r--r-- 1 kirkby staff 306 Jul 12 15:02 scipy-0.7.p5
-rw-r--r-- 1 kirkby staff 319 Jul 12 15:03 scipy_sandbox-20071020.p5
-rw-r--r-- 1 kirkby staff 307 Jul 12 15:03 moin-1.9.1.p1
-rw-r--r-- 1 kirkby staff 306 Jul 12 15:17 sage-4.5.rc0
-rw-r--r-- 1 kirkby staff 307 Jul 12 15:18 gap-4.4.12.p4
-rw-r--r-- 1 kirkby staff 307 Jul 12 15:18 sagetex-2.2.5
[kirkby@bsd sage-4.5.rc0]$ 
```


Since running the long doctests, with the one failure `devel/sage/sage/interfaces/sage0.py`, I've run the long doctests again, without rebuilding Sage - just re-running the doctests. The one failure is reproducible. That test always fails when running `make ptestlong`

However, equally reproducible is fact this test passes at the command line if one invokes Sage directly. 


```
[kirkby@bsd sage-4.5.rc0]$ ./sage -t  -long devel/sage/sage/interfaces/sage0.py
sage -t -long "devel/sage/sage/interfaces/sage0.py"         
	 [16.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 16.9 seconds
[kirkby@bsd sage-4.5.rc0]$ ./sage -t  -long devel/sage/sage/interfaces/sage0.py
sage -t -long "devel/sage/sage/interfaces/sage0.py"         
	 [12.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 12.7 seconds
[kirkby@bsd sage-4.5.rc0]$ ./sage -t  -long devel/sage/sage/interfaces/sage0.py
sage -t -long "devel/sage/sage/interfaces/sage0.py"         
	 [18.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 18.6 seconds
```


Two other experiments that may be useful to perform would be:

* Determine if this test fails if one runs `make testlong` rather than `make ptestlong`
* Determine if rebuilding Sage produces the same result each time. 


Dave



---

archive/issue_comments_091085.json:
```json
{
    "body": "Replying to [comment:6 leif]:\n> Replying to [comment:4 drkirkby]:\n> > Replying to [comment:2 leif]:\n> > > Dave, can you upload the spkg log of ecl-10.2.1.p1 on bsd.math, too?\n> > > \n> > Yep, done it already. \n> This is most probably **not** what we want:\n> {{{\n> ...\n> configure: Configuring included Boehm GC library:\n> checking build system type... i386-apple-darwin10.4.0\n> checking host system type... i386-apple-darwin10.4.0\n> checking target system type... i386-apple-darwin10.4.0\n> checking GC version numbers... major=7 minor=1 \n> ...\n> }}}\n> (We should remove Boehm GC from ECL's source tree anyway, besides the directories mentioned in `SPKG.txt`'s \"Special Update/Build Instructions\".)\n> \n> This *might* be the cause of other strange (doctest) errors on MacOS X.\nThere are several options on ECL's configure script for this \n\n```\n  --enable-boehm          use the Boehm-Weiser garbage collector\n                          (no|included|system|auto, default=auto)\n```\n\nbut there does not appear to be any way to specify the path to this, like\n\n\n```\n  --enable-boehm=\"$SAGE_LOCAL\"\n```\n\nWe could request that the ECL developer add this - he is very helpful. We **may** find that `--enable-boehm=system` will work, though I don't think that could be considered reliable without verification that it will do what we want. \n\nDave",
    "created_at": "2010-07-13T10:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91085",
    "user": "drkirkby"
}
```

Replying to [comment:6 leif]:
> Replying to [comment:4 drkirkby]:
> > Replying to [comment:2 leif]:
> > > Dave, can you upload the spkg log of ecl-10.2.1.p1 on bsd.math, too?
> > > 
> > Yep, done it already. 
> This is most probably **not** what we want:
> {{{
> ...
> configure: Configuring included Boehm GC library:
> checking build system type... i386-apple-darwin10.4.0
> checking host system type... i386-apple-darwin10.4.0
> checking target system type... i386-apple-darwin10.4.0
> checking GC version numbers... major=7 minor=1 
> ...
> }}}
> (We should remove Boehm GC from ECL's source tree anyway, besides the directories mentioned in `SPKG.txt`'s "Special Update/Build Instructions".)
> 
> This *might* be the cause of other strange (doctest) errors on MacOS X.
There are several options on ECL's configure script for this 

```
  --enable-boehm          use the Boehm-Weiser garbage collector
                          (no|included|system|auto, default=auto)
```

but there does not appear to be any way to specify the path to this, like


```
  --enable-boehm="$SAGE_LOCAL"
```

We could request that the ECL developer add this - he is very helpful. We **may** find that `--enable-boehm=system` will work, though I don't think that could be considered reliable without verification that it will do what we want. 

Dave



---

archive/issue_comments_091086.json:
```json
{
    "body": "Though `SPKG.txt` of Sage's Boehm GC (also 7.1) states it was vanilla, it contains a patch for MacOS X 10.6 (Snow Leopard) and a post-configure Makefile hack for Cygwin.\n\nSage's Boehm GC is configured with:\n\n```sh\n# See ticket #7336.  We want to set THREADDLLIBS to be nothing.\n# Rather than hacking the configure.ac file to do the right thing on\n# Cygwin, we just edit the Makefile after configure has been run.\nif [ $UNAME = \"CYGWIN\" ]; then\n     ./configure --prefix=$SAGE_LOCAL --enable-large-config --enable-threads=None\n     sed -i -e 's/^THREADDLLIBS = .*/THREADDLLIBS =/' Makefile\nelse\n     ./configure --prefix=$SAGE_LOCAL --enable-large-config\nfi\n```\n\n\n(I'd say its `spkg-install` needs some work, too.)\n\nI wonder if the Boehm GC shipped with ECL is only used on MacOS X 10.4, and why ECL's `configure` doesn't find Sage's GC on bsd.math (the log shows Sage's Boehm GC being installed before ECL is, as intended).",
    "created_at": "2010-07-13T14:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91086",
    "user": "leif"
}
```

Though `SPKG.txt` of Sage's Boehm GC (also 7.1) states it was vanilla, it contains a patch for MacOS X 10.6 (Snow Leopard) and a post-configure Makefile hack for Cygwin.

Sage's Boehm GC is configured with:

```sh
# See ticket #7336.  We want to set THREADDLLIBS to be nothing.
# Rather than hacking the configure.ac file to do the right thing on
# Cygwin, we just edit the Makefile after configure has been run.
if [ $UNAME = "CYGWIN" ]; then
     ./configure --prefix=$SAGE_LOCAL --enable-large-config --enable-threads=None
     sed -i -e 's/^THREADDLLIBS = .*/THREADDLLIBS =/' Makefile
else
     ./configure --prefix=$SAGE_LOCAL --enable-large-config
fi
```


(I'd say its `spkg-install` needs some work, too.)

I wonder if the Boehm GC shipped with ECL is only used on MacOS X 10.4, and why ECL's `configure` doesn't find Sage's GC on bsd.math (the log shows Sage's Boehm GC being installed before ECL is, as intended).



---

archive/issue_comments_091087.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n> My build on OS X (bsd.math) completed with one doc test failure. [...]\n> I've attached the ptestlong.log (renamed to bsd.math+7379+9187-ptestlong.log). After that one test failed, I run it again from the command line:\n\n```\n[kirkby@bsd sage-4.5.rc0]$ ./sage -t  -long devel/sage/sage/interfaces/sage0.py                 \nsage -t -long \"devel/sage/sage/interfaces/sage0.py\"         \n\t [13.7 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 13.7 seconds\n[kirkby@bsd sage-4.5.rc0]$ \n```\n\n> \n> It's difficult to really trust anything, when tests results are not reproducible. \n> \n> Line 3527 looks a bit odd in the log of the tests. \n\nThat's an ANSI escape sequence (actually `xterm`) generated by readline/ncurses and should be harmless; you'll find another instance of it right at the beginning after \"Testing that Sage starts...\":\n\n```sh\n$ head -n 3 kirkby/bsd.math+7379+9187-ptestlong.log | hd\n00000000  54 65 73 74 69 6e 67 20  74 68 61 74 20 53 61 67  |Testing that Sag|\n00000010  65 20 73 74 61 72 74 73  2e 2e 2e 0a 1b 5b 3f 31  |e starts.....[?1|\n00000020  30 33 34 68 59 65 73 2c  20 53 61 67 65 20 73 74  |034hYes, Sage st|\n00000030  61 72 74 73 2e 0a 47 6c  6f 62 61 6c 20 69 74 65  |arts..Global ite|\n00000040  72 61 74 69 6f 6e 73 3a  20 31 0a                 |rations: 1.|\n```\n",
    "created_at": "2010-07-13T16:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91087",
    "user": "leif"
}
```

Replying to [comment:7 drkirkby]:
> My build on OS X (bsd.math) completed with one doc test failure. [...]
> I've attached the ptestlong.log (renamed to bsd.math+7379+9187-ptestlong.log). After that one test failed, I run it again from the command line:

```
[kirkby@bsd sage-4.5.rc0]$ ./sage -t  -long devel/sage/sage/interfaces/sage0.py                 
sage -t -long "devel/sage/sage/interfaces/sage0.py"         
	 [13.7 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 13.7 seconds
[kirkby@bsd sage-4.5.rc0]$ 
```

> 
> It's difficult to really trust anything, when tests results are not reproducible. 
> 
> Line 3527 looks a bit odd in the log of the tests. 

That's an ANSI escape sequence (actually `xterm`) generated by readline/ncurses and should be harmless; you'll find another instance of it right at the beginning after "Testing that Sage starts...":

```sh
$ head -n 3 kirkby/bsd.math+7379+9187-ptestlong.log | hd
00000000  54 65 73 74 69 6e 67 20  74 68 61 74 20 53 61 67  |Testing that Sag|
00000010  65 20 73 74 61 72 74 73  2e 2e 2e 0a 1b 5b 3f 31  |e starts.....[?1|
00000020  30 33 34 68 59 65 73 2c  20 53 61 67 65 20 73 74  |034hYes, Sage st|
00000030  61 72 74 73 2e 0a 47 6c  6f 62 61 6c 20 69 74 65  |arts..Global ite|
00000040  72 61 74 69 6f 6e 73 3a  20 31 0a                 |rations: 1.|
```




---

archive/issue_comments_091088.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n> My build on OS X (bsd.math) completed with one doc test failure. This used:\n> \n>  * http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg \n>  * Library patch at #7379 (only the file trac-7379-decorator-defaults.patch)\n\nBased on this, I'm going to close this ticket, since #9187 is about to be merged. If you like, you can open a separate ticket about the Sage-Sage interface randomly failing doctests, but that has nothing to do with ecl.",
    "created_at": "2010-07-13T16:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91088",
    "user": "rlm"
}
```

Replying to [comment:7 drkirkby]:
> My build on OS X (bsd.math) completed with one doc test failure. This used:
> 
>  * http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg 
>  * Library patch at #7379 (only the file trac-7379-decorator-defaults.patch)

Based on this, I'm going to close this ticket, since #9187 is about to be merged. If you like, you can open a separate ticket about the Sage-Sage interface randomly failing doctests, but that has nothing to do with ecl.



---

archive/issue_comments_091089.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-07-13T16:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9486#issuecomment-91089",
    "user": "rlm"
}
```

Resolution: duplicate
