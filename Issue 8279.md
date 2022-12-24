# Issue 8279: cygwin: cliquer names the library incorrectly for cygwin

archive/issues_008279.json:
```json
{
    "body": "Assignee: tbd\n\nBuilding the sage library fails because the cliquer shared object library is named incorrectly on cygwin.  It should be named with .dll but is named with .so.\n\n\n```\n   [ ] fails not finding cliquer:\ngcc -shared -Wl,--enable-auto-image-base build/temp.cygwin-1.7.1-i686-2.6/sage/graphs/cliquer.o -L/home/wstein/build/sage-\\\n4.3.3.alpha0/local//lib -L/home/wstein/build/sage-4.3.3.alpha0/local/lib/python2.6/config -lcsage -lcliquer -lstdc++ -lntl\\\n -lpython2.6 -o build/lib.cygwin-1.7.1-i686-2.6/sage/graphs/cliquer.dll\n/usr/lib/gcc/i686-pc-cygwin/4.3.4/../../../../i686-pc-cygwin/bin/ld: cannot find -lcliquer\ncollect2: ld returned 1 exit status\nerror: command 'gcc' failed with exit status 1\n\n  The problem is due to a misnamed library:\n\n$ cd local/lib/\n$ ls -lh *cliq*\n-rwxr-xr-x 1 wstein None 167K 2010-02-12 22:40 libcliquer.so\n$ ln -s libcliquer.so libcliquer.dll\n\nThat works.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8279\n\n",
    "created_at": "2010-02-16T01:26:20Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "cygwin: cliquer names the library incorrectly for cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8279",
    "user": "@williamstein"
}
```
Assignee: tbd

Building the sage library fails because the cliquer shared object library is named incorrectly on cygwin.  It should be named with .dll but is named with .so.


```
   [ ] fails not finding cliquer:
gcc -shared -Wl,--enable-auto-image-base build/temp.cygwin-1.7.1-i686-2.6/sage/graphs/cliquer.o -L/home/wstein/build/sage-\
4.3.3.alpha0/local//lib -L/home/wstein/build/sage-4.3.3.alpha0/local/lib/python2.6/config -lcsage -lcliquer -lstdc++ -lntl\
 -lpython2.6 -o build/lib.cygwin-1.7.1-i686-2.6/sage/graphs/cliquer.dll
/usr/lib/gcc/i686-pc-cygwin/4.3.4/../../../../i686-pc-cygwin/bin/ld: cannot find -lcliquer
collect2: ld returned 1 exit status
error: command 'gcc' failed with exit status 1

  The problem is due to a misnamed library:

$ cd local/lib/
$ ls -lh *cliq*
-rwxr-xr-x 1 wstein None 167K 2010-02-12 22:40 libcliquer.so
$ ln -s libcliquer.so libcliquer.dll

That works.
```


Issue created by migration from https://trac.sagemath.org/ticket/8279





---

archive/issue_comments_073312.json:
```json
{
    "body": "I've put the spkg that fixes this at http://sage.math.washington.edu/home/mhansen/cygwin_port/cliquer-1.2.p5.spkg",
    "created_at": "2010-02-16T04:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8279#issuecomment-73312",
    "user": "@mwhansen"
}
```

I've put the spkg that fixes this at http://sage.math.washington.edu/home/mhansen/cygwin_port/cliquer-1.2.p5.spkg



---

archive/issue_comments_073313.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-16T04:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8279#issuecomment-73313",
    "user": "@mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073314.json:
```json
{
    "body": "This also includes David Kirkby's suggestions at #7308.",
    "created_at": "2010-02-16T05:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8279#issuecomment-73314",
    "user": "@mwhansen"
}
```

This also includes David Kirkby's suggestions at #7308.



---

archive/issue_comments_073315.json:
```json
{
    "body": "Sage 4.3.3.alpha0 rebuilt OK with this updated spkg. All doctests passed. The Cygwin build of Sage 4.3.3alpha0 also got pass the compilation process of cliquer.",
    "created_at": "2010-02-17T00:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8279#issuecomment-73315",
    "user": "mvngu"
}
```

Sage 4.3.3.alpha0 rebuilt OK with this updated spkg. All doctests passed. The Cygwin build of Sage 4.3.3alpha0 also got pass the compilation process of cliquer.



---

archive/issue_comments_073316.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-17T00:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8279#issuecomment-73316",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073317.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-17T00:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8279#issuecomment-73317",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_073318.json:
```json
{
    "body": "Could you check that libcliquer.dll is in your Cygwin build?",
    "created_at": "2010-02-17T00:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8279#issuecomment-73318",
    "user": "@mwhansen"
}
```

Could you check that libcliquer.dll is in your Cygwin build?
