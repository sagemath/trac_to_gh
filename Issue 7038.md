# Issue 7038: ratpoints 2.1.2.p2 ignores CC and uses gcc whatever

archive/issues_007038.json:
```json
{
    "body": "Assignee: tbd\n\nI gather ratpoints is causing problems with it wanting a very recent version of gcc, where here is another issue. Even if the variable CC is set to the Sun compiler, ratpoints ignores that and simply uses gcc anyway. \n\nThe build of ratpoints was attempted using \n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 \n\nSo it seems there are two at least two issues to resolve in ratpoints. \n\n\n```\nratpoints-2.1.2.p2/src/testdata.h\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nmake[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/ratpoints-2.1.2.p2/src'\ngcc sift.c -c -o sift.o -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -funroll-loops\ngcc gen_init_sieve_h.c -o gen_init_sieve_h  -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -L/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib -lgmp -lm\n./gen_init_sieve_h > init_sieve.h\ngcc init.c -c -o init.o -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -funroll-loops -O3\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7038\n\n",
    "created_at": "2009-09-27T15:52:54Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "ratpoints 2.1.2.p2 ignores CC and uses gcc whatever",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7038",
    "user": "drkirkby"
}
```
Assignee: tbd

I gather ratpoints is causing problems with it wanting a very recent version of gcc, where here is another issue. Even if the variable CC is set to the Sun compiler, ratpoints ignores that and simply uses gcc anyway. 

The build of ratpoints was attempted using 

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha2
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 

So it seems there are two at least two issues to resolve in ratpoints. 


```
ratpoints-2.1.2.p2/src/testdata.h
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
make[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/ratpoints-2.1.2.p2/src'
gcc sift.c -c -o sift.o -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -funroll-loops
gcc gen_init_sieve_h.c -o gen_init_sieve_h  -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -L/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib -lgmp -lm
./gen_init_sieve_h > init_sieve.h
gcc init.c -c -o init.o -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -funroll-loops -O3
```


Issue created by migration from https://trac.sagemath.org/ticket/7038





---

archive/issue_comments_058268.json:
```json
{
    "body": "Changing component from build to packages.",
    "created_at": "2012-03-22T13:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7038#issuecomment-58268",
    "user": "@nexttime"
}
```

Changing component from build to packages.



---

archive/issue_comments_058269.json:
```json
{
    "body": "This issue is now fixed by #12682 (which provides a ratpoints-2.1.3.p3 spkg).",
    "created_at": "2012-03-22T13:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7038#issuecomment-58269",
    "user": "@nexttime"
}
```

This issue is now fixed by #12682 (which provides a ratpoints-2.1.3.p3 spkg).



---

archive/issue_comments_058270.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-03-22T13:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7038#issuecomment-58270",
    "user": "@nexttime"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058271.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-22T13:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7038#issuecomment-58271",
    "user": "@nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058272.json:
```json
{
    "body": "Dear release manager, I leave it up to you to close this now. :-)",
    "created_at": "2012-03-22T13:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7038#issuecomment-58272",
    "user": "@nexttime"
}
```

Dear release manager, I leave it up to you to close this now. :-)



---

archive/issue_comments_058273.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-04-04T13:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7038#issuecomment-58273",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
