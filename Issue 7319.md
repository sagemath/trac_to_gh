# Issue 7319: gdmodule requires libiconv on cygwin

archive/issues_007319.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein\n\nOn Cywgin, the gdmodule spkg requires libiconv.  I think we have two choices for handling this:\n\n1. Making sure that libiconv is always installed in the system Cygwin environment.  We can probably have control over this if we include the Cygwin install with Sage.\n\n2. Add a libiconv spkg that is only installed if we are in Cygwin.  Note that this would probably amount to including it in all source tarballs.\n\nOnce libiconv is present, we need to patch Setup.py in gdmodule to add libiconv to the list of required libraries.\n\nI'll put up an spkg for libiconv and gdmodule here shortly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7319\n\n",
    "created_at": "2009-10-27T05:13:46Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "gdmodule requires libiconv on cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7319",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd

CC:  @williamstein

On Cywgin, the gdmodule spkg requires libiconv.  I think we have two choices for handling this:

1. Making sure that libiconv is always installed in the system Cygwin environment.  We can probably have control over this if we include the Cygwin install with Sage.

2. Add a libiconv spkg that is only installed if we are in Cygwin.  Note that this would probably amount to including it in all source tarballs.

Once libiconv is present, we need to patch Setup.py in gdmodule to add libiconv to the list of required libraries.

I'll put up an spkg for libiconv and gdmodule here shortly.

Issue created by migration from https://trac.sagemath.org/ticket/7319





---

archive/issue_comments_061036.json:
```json
{
    "body": "The spkg can be found a http://sage.math.washington.edu/home/mhansen/gdmodule-0.56.p7.spkg",
    "created_at": "2009-10-27T14:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61036",
    "user": "https://github.com/mwhansen"
}
```

The spkg can be found a http://sage.math.washington.edu/home/mhansen/gdmodule-0.56.p7.spkg



---

archive/issue_comments_061037.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-27T14:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61037",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061038.json:
```json
{
    "body": "The latest version of R will need iconv on Solaris - currently an option to configure, something like --no-iconv is added on R. But iconv is mandatory on the latest version with Solaris. Given iconv is not large, and does not take long to build, I believe that is should be added. I would also suggest it is installed on all platforms - not just Cygwin and Solaris. It would give one more item which is fixed, and so less need to worry if someone's problem might be their version of iconv is  too old or broken in some way. \n\n\nDave",
    "created_at": "2010-01-31T05:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61038",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The latest version of R will need iconv on Solaris - currently an option to configure, something like --no-iconv is added on R. But iconv is mandatory on the latest version with Solaris. Given iconv is not large, and does not take long to build, I believe that is should be added. I would also suggest it is installed on all platforms - not just Cygwin and Solaris. It would give one more item which is fixed, and so less need to worry if someone's problem might be their version of iconv is  too old or broken in some way. 


Dave



---

archive/issue_comments_061039.json:
```json
{
    "body": "Note, SPKG.txt has:\n\n### gdmodule-0.56.p5 (Mike Hansen, October 27th, 2009)\n* Make gdmodule work on Cygwin.\n\n### gdmodule-0.56.p5 (Michael Abshoff)\n* add .hgignore, SPKG.txt\n* clean up patches directory\n* build gdmodule against libpng12 instead of libpng (#5289)\n\nwith no entry for a p6 or p7. So this needs a bit of work, but even then, I'm unable to test on Cygwin, so you would need another reviewer too.",
    "created_at": "2010-01-31T05:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61039",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Note, SPKG.txt has:

### gdmodule-0.56.p5 (Mike Hansen, October 27th, 2009)
* Make gdmodule work on Cygwin.

### gdmodule-0.56.p5 (Michael Abshoff)
* add .hgignore, SPKG.txt
* clean up patches directory
* build gdmodule against libpng12 instead of libpng (#5289)

with no entry for a p6 or p7. So this needs a bit of work, but even then, I'm unable to test on Cygwin, so you would need another reviewer too.



---

archive/issue_comments_061040.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-31T05:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61040",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061041.json:
```json
{
    "body": "As I stated above, R also needs iconv on Solaris now - the R developers have now disabled the option to not use iconv. I've created #8191 to create an iconv package. This seems the most logical way. I can't see any possible workaround with R. \n\nDave",
    "created_at": "2010-02-05T10:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61041",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

As I stated above, R also needs iconv on Solaris now - the R developers have now disabled the option to not use iconv. I've created #8191 to create an iconv package. This seems the most logical way. I can't see any possible workaround with R. 

Dave



---

archive/issue_comments_061042.json:
```json
{
    "body": "#8191 now has an iconv package, awaiting review, so there should be no need for Mike to create an iconv package.",
    "created_at": "2010-02-15T14:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61042",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

#8191 now has an iconv package, awaiting review, so there should be no need for Mike to create an iconv package.



---

archive/issue_comments_061043.json:
```json
{
    "body": "#8191 now has positive review, so iconv should soon be in Sage.",
    "created_at": "2010-03-01T01:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61043",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

#8191 now has positive review, so iconv should soon be in Sage.



---

archive/issue_comments_061044.json:
```json
{
    "body": "Can this ticket be closed, given there is now an iconv package as a standard .spkg file in Sage? \n\ndave",
    "created_at": "2010-03-19T22:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61044",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Can this ticket be closed, given there is now an iconv package as a standard .spkg file in Sage? 

dave



---

archive/issue_comments_061045.json:
```json
{
    "body": "I'm not sure since the spkg here has other changes to it.  I'll double check.",
    "created_at": "2010-03-19T23:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61045",
    "user": "https://github.com/mwhansen"
}
```

I'm not sure since the spkg here has other changes to it.  I'll double check.



---

archive/issue_comments_061046.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-06T18:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61046",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061047.json:
```json
{
    "body": "There is an spkg at http://sage.math.washington.edu/home/mhansen/cygwin_port/gdmodule-0.56.p7.spkg that should be used.  This still needs a review.",
    "created_at": "2010-04-06T18:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61047",
    "user": "https://github.com/mwhansen"
}
```

There is an spkg at http://sage.math.washington.edu/home/mhansen/cygwin_port/gdmodule-0.56.p7.spkg that should be used.  This still needs a review.



---

archive/issue_comments_061048.json:
```json
{
    "body": "Has this been tested on at least one Linux, Solaris and OS X system? There are quite a few non-trivial changes here, and I am aware iconv and gd have caused problems recently, so I think we need to be especially careful this is very well tested. \n\nDave",
    "created_at": "2010-04-07T13:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61048",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Has this been tested on at least one Linux, Solaris and OS X system? There are quite a few non-trivial changes here, and I am aware iconv and gd have caused problems recently, so I think we need to be especially careful this is very well tested. 

Dave



---

archive/issue_comments_061049.json:
```json
{
    "body": "I've tested it on Cygwin and Linux.  The only change is Cygwin-specific and does not happen on any other platform.  The rest of the last commit was just checking in files to the repo that should have been but were not.",
    "created_at": "2010-04-07T17:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61049",
    "user": "https://github.com/mwhansen"
}
```

I've tested it on Cygwin and Linux.  The only change is Cygwin-specific and does not happen on any other platform.  The rest of the last commit was just checking in files to the repo that should have been but were not.



---

archive/issue_comments_061050.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-27T00:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61050",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_017337.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-04-29T05:04:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7319#event-17337"
}
```



---

archive/issue_comments_061051.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:04:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61051",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_061052.json:
```json
{
    "body": "I'm having trouble with this on Cygwin now:\n\n```\n\nE_LIBFONTCONFIG -I/home/wstein/sage-4.4.3.alpha1/local/include -I/usr/include -I/usr/include/X11 -I/home/wstein/sage-4.4.3.al\n -c _gdmodule.c -o build/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o\n_gdmodule.c:152: warning: function declaration isn\u2019t a prototype\n_gdmodule.c:169: warning: function declaration isn\u2019t a prototype\n_gdmodule.c: In function \u2018image_string\u2019:\n_gdmodule.c:993: warning: pointer targets in passing argument 5 of \u2018gdImageString\u2019 differ in signedness\n_gdmodule.c: In function \u2018image_string16\u2019:\n_gdmodule.c:1008: warning: passing argument 5 of \u2018gdImageString16\u2019 from incompatible pointer type\n_gdmodule.c: In function \u2018image_stringup\u2019:\n_gdmodule.c:1022: warning: pointer targets in passing argument 5 of \u2018gdImageStringUp\u2019 differ in signedness\n_gdmodule.c: In function \u2018image_stringup16\u2019:\n_gdmodule.c:1037: warning: passing argument 5 of \u2018gdImageStringUp16\u2019 from incompatible pointer type\ngcc -shared -Wl,--enable-auto-image-base build/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o -L/home/wstein/sage-4.4.3.alpha1/local/\n1 -L/home/wstein/sage-4.4.3.alpha1/local/lib/python2.6/config -lgd -lpng12 -lz -lfreetype -liconv -lfontconfig -lpython2.6 -o\n-2.6/_gd.dll\nbuild/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o: In function `write_file':\n/home/wstein/sage-4.4.3.alpha1/spkg/build/gdmodule-0.56.p7/src/_gdmodule.c:248: undefined reference to `_gdImagePngPtr'\n/home/wstein/sage-4.4.3.alpha1/spkg/build/gdmodule-0.56.p7/src/_gdmodule.c:250: undefined reference to `_gdImagePng'\nbuild/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o:_gdmodule.c:(.rdata+0x7e4): undefined reference to `_gdImageCreateFromPng'\nbuild/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o:_gdmodule.c:(.rdata+0x824): undefined reference to `_gdImageCreateFromPngCtx'\ncollect2: ld returned 1 exit status\nerror: command 'gcc' failed with exit status 1\nFailure to build gdmodule\n\nreal    0m3.434s\nuser    0m0.760s\nsys     0m1.991s\nsage: An error occurred while installing gdmodule-0.56.p7\n\n```\n",
    "created_at": "2010-06-02T02:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7319#issuecomment-61052",
    "user": "https://github.com/williamstein"
}
```

I'm having trouble with this on Cygwin now:

```

E_LIBFONTCONFIG -I/home/wstein/sage-4.4.3.alpha1/local/include -I/usr/include -I/usr/include/X11 -I/home/wstein/sage-4.4.3.al
 -c _gdmodule.c -o build/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o
_gdmodule.c:152: warning: function declaration isn’t a prototype
_gdmodule.c:169: warning: function declaration isn’t a prototype
_gdmodule.c: In function ‘image_string’:
_gdmodule.c:993: warning: pointer targets in passing argument 5 of ‘gdImageString’ differ in signedness
_gdmodule.c: In function ‘image_string16’:
_gdmodule.c:1008: warning: passing argument 5 of ‘gdImageString16’ from incompatible pointer type
_gdmodule.c: In function ‘image_stringup’:
_gdmodule.c:1022: warning: pointer targets in passing argument 5 of ‘gdImageStringUp’ differ in signedness
_gdmodule.c: In function ‘image_stringup16’:
_gdmodule.c:1037: warning: passing argument 5 of ‘gdImageStringUp16’ from incompatible pointer type
gcc -shared -Wl,--enable-auto-image-base build/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o -L/home/wstein/sage-4.4.3.alpha1/local/
1 -L/home/wstein/sage-4.4.3.alpha1/local/lib/python2.6/config -lgd -lpng12 -lz -lfreetype -liconv -lfontconfig -lpython2.6 -o
-2.6/_gd.dll
build/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o: In function `write_file':
/home/wstein/sage-4.4.3.alpha1/spkg/build/gdmodule-0.56.p7/src/_gdmodule.c:248: undefined reference to `_gdImagePngPtr'
/home/wstein/sage-4.4.3.alpha1/spkg/build/gdmodule-0.56.p7/src/_gdmodule.c:250: undefined reference to `_gdImagePng'
build/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o:_gdmodule.c:(.rdata+0x7e4): undefined reference to `_gdImageCreateFromPng'
build/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o:_gdmodule.c:(.rdata+0x824): undefined reference to `_gdImageCreateFromPngCtx'
collect2: ld returned 1 exit status
error: command 'gcc' failed with exit status 1
Failure to build gdmodule

real    0m3.434s
user    0m0.760s
sys     0m1.991s
sage: An error occurred while installing gdmodule-0.56.p7

```

