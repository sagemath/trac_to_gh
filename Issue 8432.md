# Issue 8432: make iconv a prerequisite for building gd

archive/issues_008432.json:
```json
{
    "body": "Assignee: tbd\n\nFrom [sage-release](http://groups.google.com/group/sage-release/msg/2c501eca0da2a056):\n\n```\nAs expected based on my experience with 4.3.3, I got a build error\nbuilding 4.3.4.alpha0, though this time it was a linking error with gd\nrather than cddlib. Again, this is Fedora 10 on a 64-bit system, but\non a 32-bit network, so there exist 32-bit libraries findable via NFS\n(under /usr/local). But this time I don't see any obvious evidence\nthat this is the source of the trouble.\n-----\n/bin/sh ./libtool --tag=CC --mode=link gcc  -fPIC -g -I\"/scratch/\nsage-4.3.4.alph\na0/local/include\" -I/scratch/sage-4.3.4.alpha0/local/include/\nfreetype2/  -L/scra\ntch/sage-4.3.4.alpha0/local/lib -Wl,--rpath -Wl,/scratch/\nsage-4.3.4.alpha0/local\n/lib  -L/scratch/sage-4.3.4.alpha0/local/lib  -o annotate\nannotate.o ./libgd.la\n -lfontconfig -lfreetype -lpng12 -lz -lm\ngcc -fPIC -g -I/scratch/sage-4.3.4.alpha0/local/include -I/scratch/\nsage-4.3.4.al\npha0/local/include/freetype2/ -Wl,--rpath -Wl,/scratch/\nsage-4.3.4.alpha0/local/l\nib -o .libs/annotate annotate.o  -L/scratch/sage-4.3.4.alpha0/local/\nlib ./.libs/\nlibgd.so -lfontconfig /scratch/sage-4.3.4.alpha0/local/lib/\nlibfreetype.so /scrat\nch/sage-4.3.4.alpha0/local/lib/libpng12.so -lz -lm -Wl,--rpath -Wl,/\nscratch/sage\n-4.3.4.alpha0/local/lib\n./.libs/libgd.so: undefined reference to `libiconv'\n./.libs/libgd.so: undefined reference to `libiconv_close'\n./.libs/libgd.so: undefined reference to `libiconv_open'\ncollect2: ld returned 1 exit status\n```\n\nThis is due to gd being built before iconv. mpatel suggested at [#8191](http://trac.sagemath.org/sage_trac/ticket/8191#comment:10) to make iconv a dependency for building gd. See also #8306 which implements this dependency rule.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8432\n\n",
    "created_at": "2010-03-04T03:55:31Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "make iconv a prerequisite for building gd",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8432",
    "user": "mvngu"
}
```
Assignee: tbd

From [sage-release](http://groups.google.com/group/sage-release/msg/2c501eca0da2a056):

```
As expected based on my experience with 4.3.3, I got a build error
building 4.3.4.alpha0, though this time it was a linking error with gd
rather than cddlib. Again, this is Fedora 10 on a 64-bit system, but
on a 32-bit network, so there exist 32-bit libraries findable via NFS
(under /usr/local). But this time I don't see any obvious evidence
that this is the source of the trouble.
-----
/bin/sh ./libtool --tag=CC --mode=link gcc  -fPIC -g -I"/scratch/
sage-4.3.4.alph
a0/local/include" -I/scratch/sage-4.3.4.alpha0/local/include/
freetype2/  -L/scra
tch/sage-4.3.4.alpha0/local/lib -Wl,--rpath -Wl,/scratch/
sage-4.3.4.alpha0/local
/lib  -L/scratch/sage-4.3.4.alpha0/local/lib  -o annotate
annotate.o ./libgd.la
 -lfontconfig -lfreetype -lpng12 -lz -lm
gcc -fPIC -g -I/scratch/sage-4.3.4.alpha0/local/include -I/scratch/
sage-4.3.4.al
pha0/local/include/freetype2/ -Wl,--rpath -Wl,/scratch/
sage-4.3.4.alpha0/local/l
ib -o .libs/annotate annotate.o  -L/scratch/sage-4.3.4.alpha0/local/
lib ./.libs/
libgd.so -lfontconfig /scratch/sage-4.3.4.alpha0/local/lib/
libfreetype.so /scrat
ch/sage-4.3.4.alpha0/local/lib/libpng12.so -lz -lm -Wl,--rpath -Wl,/
scratch/sage
-4.3.4.alpha0/local/lib
./.libs/libgd.so: undefined reference to `libiconv'
./.libs/libgd.so: undefined reference to `libiconv_close'
./.libs/libgd.so: undefined reference to `libiconv_open'
collect2: ld returned 1 exit status
```

This is due to gd being built before iconv. mpatel suggested at [#8191](http://trac.sagemath.org/sage_trac/ticket/8191#comment:10) to make iconv a dependency for building gd. See also #8306 which implements this dependency rule.

Issue created by migration from https://trac.sagemath.org/ticket/8432





---

archive/issue_comments_075657.json:
```json
{
    "body": "differences between deps in Sage 4.3.4.alpha0 and updated deps",
    "created_at": "2010-03-04T04:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8432#issuecomment-75657",
    "user": "mvngu"
}
```

differences between deps in Sage 4.3.4.alpha0 and updated deps



---

archive/issue_comments_075658.json:
```json
{
    "body": "Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket8432/deps.diff) by mvngu created at 2010-03-04 04:02:41\n\nupdated deps",
    "created_at": "2010-03-04T04:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8432#issuecomment-75658",
    "user": "mvngu"
}
```

Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket8432/deps.diff) by mvngu created at 2010-03-04 04:02:41

updated deps



---

archive/issue_comments_075659.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket8432/deps) by mvngu created at 2010-03-04 04:03:13",
    "created_at": "2010-03-04T04:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8432#issuecomment-75659",
    "user": "mvngu"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket8432/deps) by mvngu created at 2010-03-04 04:03:13



---

archive/issue_comments_075660.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-04T04:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8432#issuecomment-75660",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075661.json:
```json
{
    "body": "You should replace the current file `SAGE_ROOT/spkg/standard/deps` in Sage 4.3.4.alpha0 with the updated one on this ticket, i.e. [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/8432/deps).",
    "created_at": "2010-03-04T04:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8432#issuecomment-75661",
    "user": "mvngu"
}
```

You should replace the current file `SAGE_ROOT/spkg/standard/deps` in Sage 4.3.4.alpha0 with the updated one on this ticket, i.e. [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/8432/deps).



---

archive/issue_comments_075662.json:
```json
{
    "body": "I'll make a patch for that. Sorry, I overlooked the importance of this. I'm still somewhat puzzled how it ever built on Fedora if it needs an iconv - unless gd has been recently updated to need iconv too. \n\nThere is, as yet an untested file on 't2' \n\n/rootpool2/local/kirkby/sage-4.3.4.alpha0.Solaris-untested.tar\n\nwhich has\n\n* sage-4.3.4.alpha0 source\n* All the patches list at http://trac.sagemath.org/sage_trac/ticket/8409 applied\n* This item addressed. \n\nThat may or may not build on 't2', but if it does, it should have all known bug fixes that allow all doctests (including the long ones) to pass.\n\nDave",
    "created_at": "2010-03-04T05:30:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8432#issuecomment-75662",
    "user": "drkirkby"
}
```

I'll make a patch for that. Sorry, I overlooked the importance of this. I'm still somewhat puzzled how it ever built on Fedora if it needs an iconv - unless gd has been recently updated to need iconv too. 

There is, as yet an untested file on 't2' 

/rootpool2/local/kirkby/sage-4.3.4.alpha0.Solaris-untested.tar

which has

* sage-4.3.4.alpha0 source
* All the patches list at http://trac.sagemath.org/sage_trac/ticket/8409 applied
* This item addressed. 

That may or may not build on 't2', but if it does, it should have all known bug fixes that allow all doctests (including the long ones) to pass.

Dave



---

archive/issue_comments_075663.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2010-03-04T05:30:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8432#issuecomment-75663",
    "user": "drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_075664.json:
```json
{
    "body": "Sorry, I forgot to preview my previous post. I'll make it again. \n\nI'll make a patch for this bug. Sorry, I overlooked the importance of this. I'm still somewhat puzzled how gd ever built on Fedora if it needs an iconv - unless gd has been recently updated to need iconv too.\n\nThere is, as yet an untested file on 't2'\n\n/rootpool2/local/kirkby/sage-4.3.4.alpha0.Solaris-untested.tar\n\nwhich has\n\n* sage-4.3.4.alpha0 source \n* All the patches list at  http://trac.sagemath.org/sage_trac/ticket/8409 applied \n* This item addressed.\n\nThat may or may not build on 't2', but if it does, it should have all known bug fixes that allow all doctests (including the long ones) to pass.\n\nDave",
    "created_at": "2010-03-04T05:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8432#issuecomment-75664",
    "user": "drkirkby"
}
```

Sorry, I forgot to preview my previous post. I'll make it again. 

I'll make a patch for this bug. Sorry, I overlooked the importance of this. I'm still somewhat puzzled how gd ever built on Fedora if it needs an iconv - unless gd has been recently updated to need iconv too.

There is, as yet an untested file on 't2'

/rootpool2/local/kirkby/sage-4.3.4.alpha0.Solaris-untested.tar

which has

* sage-4.3.4.alpha0 source 
* All the patches list at  http://trac.sagemath.org/sage_trac/ticket/8409 applied 
* This item addressed.

That may or may not build on 't2', but if it does, it should have all known bug fixes that allow all doctests (including the long ones) to pass.

Dave



---

archive/issue_comments_075665.json:
```json
{
    "body": "I realise I can't make a patch for this, as this is not under revision control. But I can give it a positive review. Minh will have to integrate this manually.",
    "created_at": "2010-03-04T06:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8432#issuecomment-75665",
    "user": "drkirkby"
}
```

I realise I can't make a patch for this, as this is not under revision control. But I can give it a positive review. Minh will have to integrate this manually.



---

archive/issue_comments_075666.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-04T06:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8432#issuecomment-75666",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075667.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T08:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8432#issuecomment-75667",
    "user": "mhansen"
}
```

Resolution: fixed
