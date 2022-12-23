# Issue 7128: zlib-1.2.3.p4 always builds 32-bit binaries on Solaris.

archive/issues_007128.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jsp\n\nAn inspection of spkg-install for zlib shows that the -m64 flag is only added on OS X, and not on Solaris. \n\n\n```\n# The -fPIC is needed otherwise builing libpng fails later\n# (at least on a Debian 64-bit opteron).\n\nif [ `uname` = \"Darwin\" -a \"$SAGE64\" = \"yes\" ]; then\n   CFLAGS=\" -m64 $CFLAGS -fPIC -g -I\\\"$SAGE_LOCAL/include\\\"\"\n   cp ../patches/configure-OSX-64 configure\nelse\n   CFLAGS=\"$CFLAGS -fPIC -g -I\\\"$SAGE_LOCAL/include\\\"\"\nfi\n```\n\n\nThere are several things wrong with this\n* -fPIC is not a universally used flag. The correct flag to use on Solaris is -KPIC, though -fPIC will be accepted. On other compilers, such as those on AIX or HP-UX, there is no guarantee that -fPIC is the correct flag. \n* The -m64 flag to build 64-bit code is only used on OS X. It is not used on Solaris, despite the fact we are supposed to be supporting Solaris. On some compilers, **the correct flag to produce 64-bit code is not -m64**. IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7128\n\n",
    "created_at": "2009-10-05T22:49:47Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "title": "zlib-1.2.3.p4 always builds 32-bit binaries on Solaris.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7128",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  jsp

An inspection of spkg-install for zlib shows that the -m64 flag is only added on OS X, and not on Solaris. 


```
# The -fPIC is needed otherwise builing libpng fails later
# (at least on a Debian 64-bit opteron).

if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
   CFLAGS=" -m64 $CFLAGS -fPIC -g -I\"$SAGE_LOCAL/include\""
   cp ../patches/configure-OSX-64 configure
else
   CFLAGS="$CFLAGS -fPIC -g -I\"$SAGE_LOCAL/include\""
fi
```


There are several things wrong with this
* -fPIC is not a universally used flag. The correct flag to use on Solaris is -KPIC, though -fPIC will be accepted. On other compilers, such as those on AIX or HP-UX, there is no guarantee that -fPIC is the correct flag. 
* The -m64 flag to build 64-bit code is only used on OS X. It is not used on Solaris, despite the fact we are supposed to be supporting Solaris. On some compilers, **the correct flag to produce 64-bit code is not -m64**. IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

Issue created by migration from https://trac.sagemath.org/ticket/7128





---

archive/issue_comments_059122.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-05T21:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7128#issuecomment-59122",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059123.json:
```json
{
    "body": "I've sorted this out for Solaris. Currently the option added is always -m64, which is not ideal, as it will break with compilers other than GNU or Sun, but when #7818 get added, sorting this lot out will be a lot easier. \n\nOn OS X, not only is -m64 added to the flags, but an altered version of a configure script is copied too. There is no need to change the configure script on Solaris, so OS X is still handled differently. \n\n**Previous code:**\n\n```\nif [ \"x`uname`\" = \"xDarwin\" ] && [ \"x$SAGE64\" = \"xyes\" ]; then\n   CFLAGS=\" -m64 $CFLAGS -fPIC -g -I\\\"$SAGE_LOCAL/include\\\"\"\n   cp ../patches/configure-OSX-64 configure\nelse\n   CFLAGS=\"$CFLAGS $FPIC_FLAG -g -I\\\"$SAGE_LOCAL/include\\\"\"\nfi\n\n```\n\n\nRevised code: \n\n```\nif [ \"x`uname`\" = \"xDarwin\" ] && [ \"x$SAGE64\" = \"xyes\" ]; then\n   CFLAGS=\" -m64 $CFLAGS -fPIC -g -I\\\"$SAGE_LOCAL/include\\\"\"\n   cp ../patches/configure-OSX-64 configure\nelif [ \"x`uname`\" != \"xDarwin\" ] && [ \"x$SAGE64\" = \"xyes\" ]; then\n   CFLAGS=\"-m64 $CFLAGS $FPIC_FLAG -g -I\\\"$SAGE_LOCAL/include\\\"\"\nelse\n   CFLAGS=\"$CFLAGS $FPIC_FLAG -g -I\\\"$SAGE_LOCAL/include\\\"\"\nfi\n```\n",
    "created_at": "2010-01-05T21:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7128#issuecomment-59123",
    "user": "drkirkby"
}
```

I've sorted this out for Solaris. Currently the option added is always -m64, which is not ideal, as it will break with compilers other than GNU or Sun, but when #7818 get added, sorting this lot out will be a lot easier. 

On OS X, not only is -m64 added to the flags, but an altered version of a configure script is copied too. There is no need to change the configure script on Solaris, so OS X is still handled differently. 

**Previous code:**

```
if [ "x`uname`" = "xDarwin" ] && [ "x$SAGE64" = "xyes" ]; then
   CFLAGS=" -m64 $CFLAGS -fPIC -g -I\"$SAGE_LOCAL/include\""
   cp ../patches/configure-OSX-64 configure
else
   CFLAGS="$CFLAGS $FPIC_FLAG -g -I\"$SAGE_LOCAL/include\""
fi

```


Revised code: 

```
if [ "x`uname`" = "xDarwin" ] && [ "x$SAGE64" = "xyes" ]; then
   CFLAGS=" -m64 $CFLAGS -fPIC -g -I\"$SAGE_LOCAL/include\""
   cp ../patches/configure-OSX-64 configure
elif [ "x`uname`" != "xDarwin" ] && [ "x$SAGE64" = "xyes" ]; then
   CFLAGS="-m64 $CFLAGS $FPIC_FLAG -g -I\"$SAGE_LOCAL/include\""
else
   CFLAGS="$CFLAGS $FPIC_FLAG -g -I\"$SAGE_LOCAL/include\""
fi
```




---

archive/issue_comments_059124.json:
```json
{
    "body": "Sorry, I forgot to add the location of the code. \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/zlib-1.2.3.p6/\n\nThere's an spkg there. Best tested on Solaris, using a 64-bit build.",
    "created_at": "2010-01-05T21:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7128#issuecomment-59124",
    "user": "drkirkby"
}
```

Sorry, I forgot to add the location of the code. 

http://boxen.math.washington.edu/home/kirkby/portability/zlib-1.2.3.p6/

There's an spkg there. Best tested on Solaris, using a 64-bit build.



---

archive/issue_comments_059125.json:
```json
{
    "body": "Replying to [comment:3 drkirkby]:\n> Sorry, I forgot to add the location of the code. \n> \n> http://boxen.math.washington.edu/home/kirkby/portability/zlib-1.2.3.p6/\n> \n> There's an spkg there. Best tested on Solaris, using a 64-bit build. \n\nI was about to ask :)\n\nJaap",
    "created_at": "2010-01-05T21:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7128#issuecomment-59125",
    "user": "jsp"
}
```

Replying to [comment:3 drkirkby]:
> Sorry, I forgot to add the location of the code. 
> 
> http://boxen.math.washington.edu/home/kirkby/portability/zlib-1.2.3.p6/
> 
> There's an spkg there. Best tested on Solaris, using a 64-bit build. 

I was about to ask :)

Jaap



---

archive/issue_comments_059126.json:
```json
{
    "body": "Looks good, but SPKG.txt is not according the standards.\n\ne.g. missing Changelog header, new line between the entries.\n\nJaap",
    "created_at": "2010-01-05T22:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7128#issuecomment-59126",
    "user": "jsp"
}
```

Looks good, but SPKG.txt is not according the standards.

e.g. missing Changelog header, new line between the entries.

Jaap



---

archive/issue_comments_059127.json:
```json
{
    "body": "I've correct those two defects. \n\ndave",
    "created_at": "2010-01-05T22:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7128#issuecomment-59127",
    "user": "drkirkby"
}
```

I've correct those two defects. 

dave



---

archive/issue_comments_059128.json:
```json
{
    "body": "Looks good. Works ok. So positive review.",
    "created_at": "2010-01-07T16:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7128#issuecomment-59128",
    "user": "jsp"
}
```

Looks good. Works ok. So positive review.



---

archive/issue_comments_059129.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-07T16:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7128#issuecomment-59129",
    "user": "jsp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059130.json:
```json
{
    "body": "Oops! This link appears to be broken. Where is the spkg?",
    "created_at": "2010-01-13T06:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7128#issuecomment-59130",
    "user": "rlm"
}
```

Oops! This link appears to be broken. Where is the spkg?



---

archive/issue_comments_059131.json:
```json
{
    "body": "Please ignore this patch. I could have swore I updated the ticket to say so, but seem to have forgotten. I purposely removed the link. Just ignore it. I've set it to needs work.",
    "created_at": "2010-01-13T07:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7128#issuecomment-59131",
    "user": "drkirkby"
}
```

Please ignore this patch. I could have swore I updated the ticket to say so, but seem to have forgotten. I purposely removed the link. Just ignore it. I've set it to needs work.



---

archive/issue_comments_059132.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-13T07:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7128#issuecomment-59132",
    "user": "drkirkby"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_059133.json:
```json
{
    "body": "This can be closed as fixed by #9008 in sage-4.5.alpha0, when zlib was updated.",
    "created_at": "2011-04-02T13:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7128#issuecomment-59133",
    "user": "drkirkby"
}
```

This can be closed as fixed by #9008 in sage-4.5.alpha0, when zlib was updated.



---

archive/issue_comments_059134.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-04-05T15:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7128#issuecomment-59134",
    "user": "jdemeyer"
}
```

Resolution: duplicate
