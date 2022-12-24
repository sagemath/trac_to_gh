# Issue 2094: Add jpeg support to gd

archive/issues_002094.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @dimpase\n\njpeg is a common format that most people keep their pictures in -- let's support it!\n\nIssue created by migration from https://trac.sagemath.org/ticket/2094\n\n",
    "created_at": "2008-02-08T01:21:07Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add jpeg support to gd",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2094",
    "user": "boothby"
}
```
Assignee: @williamstein

CC:  @dimpase

jpeg is a common format that most people keep their pictures in -- let's support it!

Issue created by migration from https://trac.sagemath.org/ticket/2094





---

archive/issue_comments_013535.json:
```json
{
    "body": "New spkg files at:\n\nhttp://sage.math.washington.edu/home/boothby/SPKG/2.10.1/",
    "created_at": "2008-02-08T01:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13535",
    "user": "boothby"
}
```

New spkg files at:

http://sage.math.washington.edu/home/boothby/SPKG/2.10.1/



---

archive/issue_comments_013536.json:
```json
{
    "body": "Attachment [install.patch](tarball://root/attachments/some-uuid/ticket2094/install.patch) by boothby created at 2008-02-08 01:36:16",
    "created_at": "2008-02-08T01:36:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13536",
    "user": "boothby"
}
```

Attachment [install.patch](tarball://root/attachments/some-uuid/ticket2094/install.patch) by boothby created at 2008-02-08 01:36:16



---

archive/issue_comments_013537.json:
```json
{
    "body": "Works on intel 64 / ubuntu -- needs testing on amd64, mac osx, 386, etc.",
    "created_at": "2008-02-08T01:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13537",
    "user": "boothby"
}
```

Works on intel 64 / ubuntu -- needs testing on amd64, mac osx, 386, etc.



---

archive/issue_comments_013538.json:
```json
{
    "body": "I'm confused on how to test this - can you provide an example of using jpeg?\n\nI think I have everything installed/patched OK, I'm just not sure how to use it.  I tried hacking the plot save command, but ran into trouble with matplotlib since it doesn't have good jpeg support.",
    "created_at": "2008-04-27T23:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13538",
    "user": "mhampton"
}
```

I'm confused on how to test this - can you provide an example of using jpeg?

I think I have everything installed/patched OK, I'm just not sure how to use it.  I tried hacking the plot save command, but ran into trouble with matplotlib since it doesn't have good jpeg support.



---

archive/issue_comments_013539.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_craigcitro\".",
    "created_at": "2008-06-15T21:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13539",
    "user": "@craigcitro"
}
```

Changing keywords from "" to "editor_craigcitro".



---

archive/issue_comments_013540.json:
```json
{
    "body": "use the following to test:\n\n\n```\nimport gd, os, cStringIO, urllib2\n\n\ndef simple():\n    im = gd.image((200, 200))\n\n    white = im.colorAllocate((255, 255, 255))\n    black = im.colorAllocate((0, 0, 0))\n    red = im.colorAllocate((255, 0, 0))\n    blue = im.colorAllocate((0, 0, 255))\n\n    im.colorTransparent(white)\n    im.interlace(1)\n\n    im.rectangle((0,0),(199,199),black)\n    im.arc((100,100),(195,175),0,360,blue)\n    im.fill((100,100),red)\n\n    f=open(\"xx.png\",\"w\")\n    im.writePng(f)\n    f.close()\n\n    f=open(\"xx.jpg\", \"w\")\n    im.writeJpeg(f,100)\n    f.close()\n\n    f=cStringIO.StringIO()\n    im.writePng(f)\n    print \"PNG size:\", len(f.getvalue())\n    f.close()\n    \n    f = urllib2.urlopen(\"http://www.gnu.org/graphics/gnu-head-sm.jpg\")\n    im = gd.image(f, \"jpg\")\n    f.close()\n    im.writePng(\"xy.png\")\n    print \"GNU Image Size:\", im.size()\n\nsimple()\n```\n",
    "created_at": "2008-06-16T20:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13540",
    "user": "boothby"
}
```

use the following to test:


```
import gd, os, cStringIO, urllib2


def simple():
    im = gd.image((200, 200))

    white = im.colorAllocate((255, 255, 255))
    black = im.colorAllocate((0, 0, 0))
    red = im.colorAllocate((255, 0, 0))
    blue = im.colorAllocate((0, 0, 255))

    im.colorTransparent(white)
    im.interlace(1)

    im.rectangle((0,0),(199,199),black)
    im.arc((100,100),(195,175),0,360,blue)
    im.fill((100,100),red)

    f=open("xx.png","w")
    im.writePng(f)
    f.close()

    f=open("xx.jpg", "w")
    im.writeJpeg(f,100)
    f.close()

    f=cStringIO.StringIO()
    im.writePng(f)
    print "PNG size:", len(f.getvalue())
    f.close()
    
    f = urllib2.urlopen("http://www.gnu.org/graphics/gnu-head-sm.jpg")
    im = gd.image(f, "jpg")
    f.close()
    im.writePng("xy.png")
    print "GNU Image Size:", im.size()

simple()
```




---

archive/issue_comments_013541.json:
```json
{
    "body": "Instructions for reviewer(s):\n\nThe deps/install patches are diffed against files in the Sage distribution which are not (for better or worse) under revision control.  To test, please install the spkgs in the order (jpeg, gd, gdmodule).  Then, run the sample code above.",
    "created_at": "2008-06-16T21:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13541",
    "user": "boothby"
}
```

Instructions for reviewer(s):

The deps/install patches are diffed against files in the Sage distribution which are not (for better or worse) under revision control.  To test, please install the spkgs in the order (jpeg, gd, gdmodule).  Then, run the sample code above.



---

archive/issue_comments_013542.json:
```json
{
    "body": "I get the following error (the spkgs seem to have installed without errors):\n\nTraceback (most recent call last):    \n  File \"/Volumes/D/sage-3.0.2/local/lib/python2.5/site-packages/gd.py\", line 10, in <module>\n    import _gd\nImportError: dlopen(/Volumes/D/sage-3.0.2/local/lib/python2.5/site-packages/_gd.so, 2): Symbol not found: _jpeg_std_error\n  Referenced from: /Volumes/D/sage-3.0.2/local/lib//libgd.2.dylib\n  Expected in: flat namespace",
    "created_at": "2008-06-16T21:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13542",
    "user": "mhampton"
}
```

I get the following error (the spkgs seem to have installed without errors):

Traceback (most recent call last):    
  File "/Volumes/D/sage-3.0.2/local/lib/python2.5/site-packages/gd.py", line 10, in <module>
    import _gd
ImportError: dlopen(/Volumes/D/sage-3.0.2/local/lib/python2.5/site-packages/_gd.so, 2): Symbol not found: _jpeg_std_error
  Referenced from: /Volumes/D/sage-3.0.2/local/lib//libgd.2.dylib
  Expected in: flat namespace



---

archive/issue_comments_013543.json:
```json
{
    "body": "Possible hints are here:\n\nhttp://trac.macports.org/browser/trunk/dports/graphics/jpeg",
    "created_at": "2008-06-17T06:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13543",
    "user": "boothby"
}
```

Possible hints are here:

http://trac.macports.org/browser/trunk/dports/graphics/jpeg



---

archive/issue_comments_013544.json:
```json
{
    "body": "Tom agrees that this patch needs work to function on a Mac. He'll get to it soon-ish.",
    "created_at": "2008-06-19T19:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13544",
    "user": "@craigcitro"
}
```

Tom agrees that this patch needs work to function on a Mac. He'll get to it soon-ish.



---

archive/issue_comments_013545.json:
```json
{
    "body": "Notice that these are (basically) the same errors we're seeing on #3324.",
    "created_at": "2008-06-20T04:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13545",
    "user": "@craigcitro"
}
```

Notice that these are (basically) the same errors we're seeing on #3324.



---

archive/issue_comments_013546.json:
```json
{
    "body": "This is a framework vs. sane library issue - I will likely have a workaround for this in the not too distant future.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T18:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13546",
    "user": "mabshoff"
}
```

This is a framework vs. sane library issue - I will likely have a workaround for this in the not too distant future.

Cheers,

Michael



---

archive/issue_comments_013547.json:
```json
{
    "body": "Since we now do no longer build anything against the Apple IOKit Framework this spkg should be re-reviewed.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-20T22:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13547",
    "user": "mabshoff"
}
```

Since we now do no longer build anything against the Apple IOKit Framework this spkg should be re-reviewed.

Cheers,

Michael



---

archive/issue_comments_013548.json:
```json
{
    "body": "I am now having problems different from before.  The jpeg spkg seems to install OK, and when installing the gd spkg I get the following encouraging message from the configuring:\n\n```\n** Configuration summary for gd 2.0.33:\n\n   Support for PNG library:          yes\n   Support for JPEG library:         yes\n   Support for Freetype 2.x library: yes\n   Support for Fontconfig library:   no\n   Support for Xpm library:          no\n   Support for pthreads:             yes\n```\n\n...but then the build fails, and there is a message:\n\n\n```\n*** Warning: linker path does not have real file for library -ljpeg.\n*** I have the capability to make that library automatically link in when\n*** you link to this library.  But I can only do this if you have a\n*** shared version of the library, which you do not appear to have\n*** because I did check the linker path looking for a file starting\n*** with libjpeg and none of the candidates passed a file format test\n*** using a file magic. Last file checked: /Volumes/D/sage-3.1.2/local/lib//libjpeg.a\n*** The inter-library dependencies that have been dropped here will be\n*** automatically added whenever a program is linked with this library\n*** or is declared to -dlopen it.\n```\n\n\n...which occurs before the actual error:\n\n```\n/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: Undefined symbols:\n_gdImageCreateFromJpeg\n_gdImageJpeg\ncollect2: ld returned 1 exit status\nmake[2]: *** [annotate] Error 1\nmake[2]: Leaving directory `/Volumes/D/sage-3.1.2/spkg/build/gd-2.0.33.p7/src'\nmake[1]: *** [all-recursive] Error 1\nmake[1]: Leaving directory `/Volumes/D/sage-3.1.2/spkg/build/gd-2.0.33.p7/src'\nmake: *** [all] Error 2\nError building gd.\n```\n\n\nIt would be very nice to have this stuff working; being able to quickly import images as matrices is something matlab and mathematica users take for granted.  Unfortunately I don't think I have the skills needed to fix this.",
    "created_at": "2008-09-21T02:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13548",
    "user": "mhampton"
}
```

I am now having problems different from before.  The jpeg spkg seems to install OK, and when installing the gd spkg I get the following encouraging message from the configuring:

```
** Configuration summary for gd 2.0.33:

   Support for PNG library:          yes
   Support for JPEG library:         yes
   Support for Freetype 2.x library: yes
   Support for Fontconfig library:   no
   Support for Xpm library:          no
   Support for pthreads:             yes
```

...but then the build fails, and there is a message:


```
*** Warning: linker path does not have real file for library -ljpeg.
*** I have the capability to make that library automatically link in when
*** you link to this library.  But I can only do this if you have a
*** shared version of the library, which you do not appear to have
*** because I did check the linker path looking for a file starting
*** with libjpeg and none of the candidates passed a file format test
*** using a file magic. Last file checked: /Volumes/D/sage-3.1.2/local/lib//libjpeg.a
*** The inter-library dependencies that have been dropped here will be
*** automatically added whenever a program is linked with this library
*** or is declared to -dlopen it.
```


...which occurs before the actual error:

```
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: Undefined symbols:
_gdImageCreateFromJpeg
_gdImageJpeg
collect2: ld returned 1 exit status
make[2]: *** [annotate] Error 1
make[2]: Leaving directory `/Volumes/D/sage-3.1.2/spkg/build/gd-2.0.33.p7/src'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/Volumes/D/sage-3.1.2/spkg/build/gd-2.0.33.p7/src'
make: *** [all] Error 2
Error building gd.
```


It would be very nice to have this stuff working; being able to quickly import images as matrices is something matlab and mathematica users take for granted.  Unfortunately I don't think I have the skills needed to fix this.



---

archive/issue_comments_013549.json:
```json
{
    "body": "One more note: since gd has evolved to 2.0.35, I tried installing that and it seemed to work but the suggested test still crashed with \n\n```\nsage: import gd, os, cStringIO, urllib2\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n\n/Volumes/D/sage-3.1.2/<ipython console> in <module>()\n\n/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/gd.py in <module>()\n      8 library.\"\"\"\n      9 \n---> 10 import _gd\n     11 from _gd import *\n     12 del image\n\nImportError: dlopen(/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/_gd.so, 2): Symbol not found: _gdImageCreateFromJpeg\n  Referenced from: /Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/_gd.so\n  Expected in: dynamic lookup\n```\n\n\nalthough I might have messed up in manually installing gd-2.0.35.",
    "created_at": "2008-09-21T03:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13549",
    "user": "mhampton"
}
```

One more note: since gd has evolved to 2.0.35, I tried installing that and it seemed to work but the suggested test still crashed with 

```
sage: import gd, os, cStringIO, urllib2
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/Volumes/D/sage-3.1.2/<ipython console> in <module>()

/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/gd.py in <module>()
      8 library."""
      9 
---> 10 import _gd
     11 from _gd import *
     12 del image

ImportError: dlopen(/Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/_gd.so, 2): Symbol not found: _gdImageCreateFromJpeg
  Referenced from: /Volumes/D/sage-3.1.2/local/lib/python2.5/site-packages/_gd.so
  Expected in: dynamic lookup
```


although I might have messed up in manually installing gd-2.0.35.



---

archive/issue_comments_013550.json:
```json
{
    "body": "I can fix this on OSX. Give me a little while. Besides adding the jpeg.spkg this also needs matching fixes to the gd.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-09-21T05:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13550",
    "user": "mabshoff"
}
```

I can fix this on OSX. Give me a little while. Besides adding the jpeg.spkg this also needs matching fixes to the gd.spkg

Cheers,

Michael



---

archive/issue_comments_013551.json:
```json
{
    "body": "OK, I have gotten this working as well, using gd-2.0.35.  I messed up previously when trying to install it.  I can make a spkg if you want, but you'd probably have to edit my attempts anyway.\n\n-M.Hampton",
    "created_at": "2008-09-22T16:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13551",
    "user": "mhampton"
}
```

OK, I have gotten this working as well, using gd-2.0.35.  I messed up previously when trying to install it.  I can make a spkg if you want, but you'd probably have to edit my attempts anyway.

-M.Hampton



---

archive/issue_comments_013552.json:
```json
{
    "body": "Replying to [comment:19 mhampton]:\n> OK, I have gotten this working as well, using gd-2.0.35.  I messed up previously when trying to install it.  I can make a spkg if you want, but you'd probably have to edit my attempts anyway.\n> \n> -M.Hampton\n\nWe are already using gd-2.0.35, so what changes do you propose to make? Either way, an jpeg.spkg would have to be voted in anyway.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-22T18:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13552",
    "user": "mabshoff"
}
```

Replying to [comment:19 mhampton]:
> OK, I have gotten this working as well, using gd-2.0.35.  I messed up previously when trying to install it.  I can make a spkg if you want, but you'd probably have to edit my attempts anyway.
> 
> -M.Hampton

We are already using gd-2.0.35, so what changes do you propose to make? Either way, an jpeg.spkg would have to be voted in anyway.

Cheers,

Michael



---

archive/issue_comments_013553.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13553",
    "user": "@mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_013554.json:
```json
{
    "body": "Outdated spkg or build system ticket, should be closed",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13554",
    "user": "@mkoeppe"
}
```

Outdated spkg or build system ticket, should be closed



---

archive/issue_comments_013555.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-09-08T18:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2094#issuecomment-13555",
    "user": "@fchapoton"
}
```

Resolution: invalid
