# Issue 7297: spkg's for libogg and libtheora

archive/issues_007297.json:
```json
{
    "body": "Assignee: whuss\n\nKeywords: video, animation\n\nPackages for libogg and libtheora. The libtheora spkg installs the\ncommand line tool \"png2theora\" which can be used to encode a series\nof PNG images into a Theora video.\n\nhttp://www.math.tugraz.at/~huss/spkg/libogg-1.1.4.spkg \n\nhttp://www.math.tugraz.at/~huss/spkg/libtheora-1.1.1.spkg\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7297\n\n",
    "created_at": "2009-10-25T15:47:27Z",
    "labels": [
        "component: packages: optional"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "spkg's for libogg and libtheora",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7297",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```
Assignee: whuss

Keywords: video, animation

Packages for libogg and libtheora. The libtheora spkg installs the
command line tool "png2theora" which can be used to encode a series
of PNG images into a Theora video.

http://www.math.tugraz.at/~huss/spkg/libogg-1.1.4.spkg 

http://www.math.tugraz.at/~huss/spkg/libtheora-1.1.1.spkg



Issue created by migration from https://trac.sagemath.org/ticket/7297





---

archive/issue_comments_060627.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-25T15:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7297#issuecomment-60627",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060628.json:
```json
{
    "body": "The end of my install for libtheora looks like this:\n\n```\n/bin/sh ./mkinstalldirs /Users/mh/sagestuff/sage-4.2/local/lib/pkgconfig\n /usr/bin/install -c -m 644 theora.pc /Users/mh/sagestuff/sage-4.2/local/lib/pkgconfig/theora.pc\n /usr/bin/install -c -m 644 theoradec.pc /Users/mh/sagestuff/sage-4.2/local/lib/pkgconfig/theoradec.pc\n /usr/bin/install -c -m 644 theoraenc.pc /Users/mh/sagestuff/sage-4.2/local/lib/pkgconfig/theoraenc.pc\ncp: examples/.libs/png2theora: No such file or directory\n\nreal\t0m32.161s\nuser\t0m19.908s\nsys\t0m8.520s\nsage: An error occurred while installing libtheora-1.1.1\n```\n\n\nSeems like things compiled OK though.  This is on an intel mac, 10.5.\n\n-Marshall",
    "created_at": "2009-10-26T18:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7297#issuecomment-60628",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

The end of my install for libtheora looks like this:

```
/bin/sh ./mkinstalldirs /Users/mh/sagestuff/sage-4.2/local/lib/pkgconfig
 /usr/bin/install -c -m 644 theora.pc /Users/mh/sagestuff/sage-4.2/local/lib/pkgconfig/theora.pc
 /usr/bin/install -c -m 644 theoradec.pc /Users/mh/sagestuff/sage-4.2/local/lib/pkgconfig/theoradec.pc
 /usr/bin/install -c -m 644 theoraenc.pc /Users/mh/sagestuff/sage-4.2/local/lib/pkgconfig/theoraenc.pc
cp: examples/.libs/png2theora: No such file or directory

real	0m32.161s
user	0m19.908s
sys	0m8.520s
sage: An error occurred while installing libtheora-1.1.1
```


Seems like things compiled OK though.  This is on an intel mac, 10.5.

-Marshall



---

archive/issue_comments_060629.json:
```json
{
    "body": "As far as I can tell, there is no attempt to actually build png2theora, its not a failure.  But I am not sure how to edit the makefile to force this build.",
    "created_at": "2009-10-26T18:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7297#issuecomment-60629",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

As far as I can tell, there is no attempt to actually build png2theora, its not a failure.  But I am not sure how to edit the makefile to force this build.



---

archive/issue_comments_060630.json:
```json
{
    "body": "Is there the line\n\n\n```\nBuild example code: ......... yes\n```\n\n\nat the end of configure?\n\nDid it find libpng?\n\nThe option --enable-examples for configure should force the building of the examples.",
    "created_at": "2009-10-27T08:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7297#issuecomment-60630",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Is there the line


```
Build example code: ......... yes
```


at the end of configure?

Did it find libpng?

The option --enable-examples for configure should force the building of the examples.



---

archive/issue_comments_060631.json:
```json
{
    "body": "I do see the \"Build example code: ........... yes\" string at the end of the configure output.\n\nI don't see any indication of it looking for libpng, either a failure or success.\n\nThe only things that are being built inside of spkg/build/libtheora-1.1.1/src/examples are dump_video and dump_psnr.  \n\n-Marshall",
    "created_at": "2009-10-27T17:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7297#issuecomment-60631",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I do see the "Build example code: ........... yes" string at the end of the configure output.

I don't see any indication of it looking for libpng, either a failure or success.

The only things that are being built inside of spkg/build/libtheora-1.1.1/src/examples are dump_video and dump_psnr.  

-Marshall



---

archive/issue_comments_060632.json:
```json
{
    "body": "I think the problem might be that I installed libogg, but this is not being detected by the script \"newest_version\", which looks in the standard directory for the spkg, which is not copied over.",
    "created_at": "2009-10-27T18:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7297#issuecomment-60632",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I think the problem might be that I installed libogg, but this is not being detected by the script "newest_version", which looks in the standard directory for the spkg, which is not copied over.



---

archive/issue_comments_060633.json:
```json
{
    "body": "OK, I tried copying the libogg spkg into the spkg/standard directory, but then the configure script fails with:\n\nchecking for Ogg... no\n*** Could not run Ogg test program, checking why...\n\n-I'm not sure what to try now.",
    "created_at": "2009-10-27T18:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7297#issuecomment-60633",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

OK, I tried copying the libogg spkg into the spkg/standard directory, but then the configure script fails with:

checking for Ogg... no
*** Could not run Ogg test program, checking why...

-I'm not sure what to try now.



---

archive/issue_comments_060634.json:
```json
{
    "body": "Whats the point of \n\n\n```\nunset RM\n```\n\nin the spkg-install of libogg-1.1.4 ? \n\nI'd either remove the line, or add a comment why it is needed.",
    "created_at": "2009-12-24T00:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7297#issuecomment-60634",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Whats the point of 


```
unset RM
```

in the spkg-install of libogg-1.1.4 ? 

I'd either remove the line, or add a comment why it is needed.



---

archive/issue_comments_060635.json:
```json
{
    "body": "I would add 'set -e' before the 'cp' command in the spkg-install of libtheora-1.1.1. Then, if the copy fails, the spkg-install script will exit with a code of 1. Otherwise, this will appear to have installed correctly, even if the copy fails. \n\n\n```\nset -e \ncp examples/.libs/png2theora $SAGE_LOCAL/bin\n```\n",
    "created_at": "2009-12-24T00:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7297#issuecomment-60635",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I would add 'set -e' before the 'cp' command in the spkg-install of libtheora-1.1.1. Then, if the copy fails, the spkg-install script will exit with a code of 1. Otherwise, this will appear to have installed correctly, even if the copy fails. 


```
set -e 
cp examples/.libs/png2theora $SAGE_LOCAL/bin
```




---

archive/issue_comments_060636.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-01T08:04:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7297#issuecomment-60636",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060637.json:
```json
{
    "body": "Everything looks fine to me. I also don't understand the \"unset RM\" line, but I don't think it can hurt in any way. Not an expert in the reviewing process, but I'm giving positive review.",
    "created_at": "2010-05-01T08:04:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7297#issuecomment-60637",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

Everything looks fine to me. I also don't understand the "unset RM" line, but I don't think it can hurt in any way. Not an expert in the reviewing process, but I'm giving positive review.



---

archive/issue_comments_060638.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-07T05:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7297#issuecomment-60638",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007518.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-06-07T05:06:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7297#event-7518"
}
```



---

archive/issue_comments_060639.json:
```json
{
    "body": "libtheora no longer builds; if it's not fixed, we'll have to remove it from optional packages...",
    "created_at": "2017-09-19T17:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7297#issuecomment-60639",
    "user": "https://github.com/dimpase"
}
```

libtheora no longer builds; if it's not fixed, we'll have to remove it from optional packages...
