# Issue 7345: New libtiff package

archive/issues_007345.json:
```json
{
    "body": "Assignee: boothby\n\nThis is used by PIL (c.f. #7273). Inclusion as an optional or even as a standard package would be helpful.\n\nThe package is here:  http://sage.math.washington.edu/home/timdumol/libtiff-3.9.1.p0.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/7345\n\n",
    "created_at": "2009-10-29T04:25:27Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "New libtiff package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7345",
    "user": "https://github.com/TimDumol"
}
```
Assignee: boothby

This is used by PIL (c.f. #7273). Inclusion as an optional or even as a standard package would be helpful.

The package is here:  http://sage.math.washington.edu/home/timdumol/libtiff-3.9.1.p0.spkg

Issue created by migration from https://trac.sagemath.org/ticket/7345





---

archive/issue_comments_061416.json:
```json
{
    "body": "Should this belong to a different component?",
    "created_at": "2009-11-01T01:20:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61416",
    "user": "https://github.com/qed777"
}
```

Should this belong to a different component?



---

archive/issue_comments_061417.json:
```json
{
    "body": "Changing component from notebook to packages.",
    "created_at": "2009-11-01T02:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61417",
    "user": "https://github.com/TimDumol"
}
```

Changing component from notebook to packages.



---

archive/issue_comments_061418.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-01T02:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61418",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061419.json:
```json
{
    "body": "Woops. Yep.",
    "created_at": "2009-11-01T02:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61419",
    "user": "https://github.com/TimDumol"
}
```

Woops. Yep.



---

archive/issue_comments_061420.json:
```json
{
    "body": "Builds fine on Mac OS X 10.6 and sage.math, and installs what look like the right libraries in the right place.  What can I do to test it?\n\nI've marked it as \"needs work\" because the SPKG.txt file says \"libjpeg\" several places instead of \"libtiff\".\n\nIs the spkg-install file modeled after other ones currently in use?  (Will drkirby complain about gnuisms, for instance, or is this derived from one of his spkg-install files?)",
    "created_at": "2009-12-22T06:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61420",
    "user": "https://github.com/jhpalmieri"
}
```

Builds fine on Mac OS X 10.6 and sage.math, and installs what look like the right libraries in the right place.  What can I do to test it?

I've marked it as "needs work" because the SPKG.txt file says "libjpeg" several places instead of "libtiff".

Is the spkg-install file modeled after other ones currently in use?  (Will drkirby complain about gnuisms, for instance, or is this derived from one of his spkg-install files?)



---

archive/issue_comments_061421.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-22T06:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61421",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061422.json:
```json
{
    "body": "Oh, there is also a file SPKG.txt~ which should not be there.",
    "created_at": "2009-12-22T06:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61422",
    "user": "https://github.com/jhpalmieri"
}
```

Oh, there is also a file SPKG.txt~ which should not be there.



---

archive/issue_comments_061423.json:
```json
{
    "body": "See also [here](http://groups.google.com/group/sage-devel/browse_frm/thread/48f720062cc4e38b/ff817dfb819e5ce).",
    "created_at": "2010-08-02T18:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61423",
    "user": "https://github.com/kcrisman"
}
```

See also [here](http://groups.google.com/group/sage-devel/browse_frm/thread/48f720062cc4e38b/ff817dfb819e5ce).



---

archive/issue_comments_061424.json:
```json
{
    "body": "Changing assignee from boothby to @TimDumol.",
    "created_at": "2010-08-02T18:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61424",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing assignee from boothby to @TimDumol.



---

archive/issue_comments_061425.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-17T18:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61425",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061426.json:
```json
{
    "body": "Updated version found here: http://sage.math.washington.edu/home/timdumol/libtiff-3.9.4.spkg\n\nThis should fix the OS X 10.6 problems (c.f. #7344).\n\n\n```\nsage: import Image\nsage: im = Image.open(\"<your-tiff-file-here>\")\nsage: im = im.resize((im.size[0]/2,im.size[1]/2))\nsage: print im.format, im.size, im.mode\nTIFF (455, 495) 1\nsage: im.show()\nsage: im.save(\"wherever.tiff\")\n```\n",
    "created_at": "2010-08-17T18:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61426",
    "user": "https://github.com/TimDumol"
}
```

Updated version found here: http://sage.math.washington.edu/home/timdumol/libtiff-3.9.4.spkg

This should fix the OS X 10.6 problems (c.f. #7344).


```
sage: import Image
sage: im = Image.open("<your-tiff-file-here>")
sage: im = im.resize((im.size[0]/2,im.size[1]/2))
sage: print im.format, im.size, im.mode
TIFF (455, 495) 1
sage: im.show()
sage: im.save("wherever.tiff")
```




---

archive/issue_comments_061427.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-05-13T13:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61427",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_061428.json:
```json
{
    "body": "[http://libtiff.org](http://libtiff.org) says latest version is 3.6.1, yet this\nspkg is labeled 3.9.4.  Why?",
    "created_at": "2011-05-13T13:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61428",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

[http://libtiff.org](http://libtiff.org) says latest version is 3.6.1, yet this
spkg is labeled 3.9.4.  Why?



---

archive/issue_comments_061429.json:
```json
{
    "body": "The web page itself is outdated. The downloads page: ftp://ftp.remotesensing.org/pub/libtiff actually states that the latest package is 3.9.5.",
    "created_at": "2011-08-02T17:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61429",
    "user": "https://github.com/TimDumol"
}
```

The web page itself is outdated. The downloads page: ftp://ftp.remotesensing.org/pub/libtiff actually states that the latest package is 3.9.5.



---

archive/issue_comments_061430.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-08-02T17:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61430",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_061431.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-08-02T17:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61431",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061432.json:
```json
{
    "body": "New package here: http://sage.math.washington.edu/home/timdumol/libtiff-3.9.5.spkg",
    "created_at": "2011-08-02T18:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61432",
    "user": "https://github.com/TimDumol"
}
```

New package here: http://sage.math.washington.edu/home/timdumol/libtiff-3.9.5.spkg



---

archive/issue_comments_061433.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-08-02T18:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61433",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061434.json:
```json
{
    "body": "There are some problems on OS X:\n\n```\nsage: im = Image.open('/Users/palmieri/Desktop/P1000717.tiff')\nsage: im.show()\n---------------------------------------------------------------------------\nIOError                                   Traceback (most recent call last)\n...\nIOError: encoder jpeg not available\nsage: im = im.resize((im.size[0]/2,im.size[1]/2))\nsage: print im.format\nNone\n```\n\n\nBy the way, according to ImageMagick's \"identify\" program:\n\n```\n$ identify P1000717.tiff \nP1000717.tiff TIFF 3648x2736 3648x2736+0+0 DirectClass 8-bit 28.5613mb \n```\n\nSo I think it's the right format to be opened by this library.  Is there anything else I should check?",
    "created_at": "2011-08-03T00:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61434",
    "user": "https://github.com/jhpalmieri"
}
```

There are some problems on OS X:

```
sage: im = Image.open('/Users/palmieri/Desktop/P1000717.tiff')
sage: im.show()
---------------------------------------------------------------------------
IOError                                   Traceback (most recent call last)
...
IOError: encoder jpeg not available
sage: im = im.resize((im.size[0]/2,im.size[1]/2))
sage: print im.format
None
```


By the way, according to ImageMagick's "identify" program:

```
$ identify P1000717.tiff 
P1000717.tiff TIFF 3648x2736 3648x2736+0+0 DirectClass 8-bit 28.5613mb 
```

So I think it's the right format to be opened by this library.  Is there anything else I should check?



---

archive/issue_comments_061435.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-08-03T00:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61435",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061436.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-08-03T09:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61436",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061437.json:
```json
{
    "body": "In the notebook, `im.show()` saves a JPEG into the worksheet directory, which is then automatically displayed by the SageNB. Thus, the error you got was actually because PIL has no access to libjpeg, and is thus not related to this package.",
    "created_at": "2011-08-03T09:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61437",
    "user": "https://github.com/TimDumol"
}
```

In the notebook, `im.show()` saves a JPEG into the worksheet directory, which is then automatically displayed by the SageNB. Thus, the error you got was actually because PIL has no access to libjpeg, and is thus not related to this package.



---

archive/issue_comments_061438.json:
```json
{
    "body": "I was actually working from the command line, but anyway, what about this part:\n\n```\nsage: im = im.resize((im.size[0]/2,im.size[1]/2))\nsage: print im.format\nNone\n```\n\nAccording to the earlier example, this should have said \"TIFF\".",
    "created_at": "2011-08-03T15:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61438",
    "user": "https://github.com/jhpalmieri"
}
```

I was actually working from the command line, but anyway, what about this part:

```
sage: im = im.resize((im.size[0]/2,im.size[1]/2))
sage: print im.format
None
```

According to the earlier example, this should have said "TIFF".



---

archive/issue_comments_061439.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-08-03T15:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61439",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_061440.json:
```json
{
    "body": "By the way, I can successfully save the resized image.  Somewhere along the line I reinstalled PIL, so I don't know if that's necessary.",
    "created_at": "2011-08-03T15:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61440",
    "user": "https://github.com/jhpalmieri"
}
```

By the way, I can successfully save the resized image.  Somewhere along the line I reinstalled PIL, so I don't know if that's necessary.



---

archive/issue_comments_061441.json:
```json
{
    "body": "Two things: since this package installs files into `SAGE_ROOT/local/bin`, you should add those files to `.hgignore` \u2014 this will require a separate patch to the scripts repo.  Also the spkg file contains \"SPKG.txt~\", which shouldn't be there.",
    "created_at": "2011-08-03T22:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61441",
    "user": "https://github.com/jhpalmieri"
}
```

Two things: since this package installs files into `SAGE_ROOT/local/bin`, you should add those files to `.hgignore` — this will require a separate patch to the scripts repo.  Also the spkg file contains "SPKG.txt~", which shouldn't be there.



---

archive/issue_comments_061442.json:
```json
{
    "body": "Replying to [comment:13 timdumol]:\n> In the notebook, `im.show()` saves a JPEG into the worksheet directory, which is then automatically displayed by the SageNB.\n\nMay I ask why? Does it make any sense to convert a \"lossless image\" into a lossy format, i.e., why not convert it to e.g. PNG which any (GUI) browser should be able to display?\n\n(I know TIFF is also a \"meta format\", i.e. you can encapsulate JPEGs in a TIFF file, but John's example file doesn't look like it was such.)\n\nThe only reason I can imagine is that it's easier to scale JPEG images than bitmaps, but unless we include the batteries by default, a simple `show()` of a bitmap image shouldn't require `libjpeg`.",
    "created_at": "2011-08-04T12:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61442",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:13 timdumol]:
> In the notebook, `im.show()` saves a JPEG into the worksheet directory, which is then automatically displayed by the SageNB.

May I ask why? Does it make any sense to convert a "lossless image" into a lossy format, i.e., why not convert it to e.g. PNG which any (GUI) browser should be able to display?

(I know TIFF is also a "meta format", i.e. you can encapsulate JPEGs in a TIFF file, but John's example file doesn't look like it was such.)

The only reason I can imagine is that it's easier to scale JPEG images than bitmaps, but unless we include the batteries by default, a simple `show()` of a bitmap image shouldn't require `libjpeg`.



---

archive/issue_comments_061443.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61443",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_comments_061444.json:
```json
{
    "body": "Regarding the im.format printing as None, that's OK, since the format attribute is only defined if the image was loaded from a file.\n\nRegarding the action of Image.show():  Leif is right, using JPEG is a bad idea.  Using TIFF is also a bad idea, for this purpose, as the PIL TIFF encoder only saves uncompressed TIFF files.  They're big and slow.  I second the idea of using PNG for Image.show().  But that really is a separate issue, and should be broken out as such.",
    "created_at": "2011-11-12T23:11:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61444",
    "user": "https://trac.sagemath.org/admin/accounts/users/janssen"
}
```

Regarding the im.format printing as None, that's OK, since the format attribute is only defined if the image was loaded from a file.

Regarding the action of Image.show():  Leif is right, using JPEG is a bad idea.  Using TIFF is also a bad idea, for this purpose, as the PIL TIFF encoder only saves uncompressed TIFF files.  They're big and slow.  I second the idea of using PNG for Image.show().  But that really is a separate issue, and should be broken out as such.



---

archive/issue_comments_061445.json:
```json
{
    "body": "Hmm, I see that JPEG is hard-coded into PIL 1.1.6.  In PIL 1.1.7, im.show() uses a non-lossy format, and the user can override the viewer used by show(), so one custom-designed for Sage could be put in there if necessary.",
    "created_at": "2011-11-12T23:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61445",
    "user": "https://trac.sagemath.org/admin/accounts/users/janssen"
}
```

Hmm, I see that JPEG is hard-coded into PIL 1.1.6.  In PIL 1.1.7, im.show() uses a non-lossy format, and the user can override the viewer used by show(), so one custom-designed for Sage could be put in there if necessary.



---

archive/issue_comments_061446.json:
```json
{
    "body": "Changing component from packages: standard to packages: optional.",
    "created_at": "2014-11-13T14:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61446",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from packages: standard to packages: optional.



---

archive/issue_comments_061447.json:
```json
{
    "body": "outdated, should close",
    "created_at": "2021-08-26T02:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61447",
    "user": "https://github.com/mkoeppe"
}
```

outdated, should close



---

archive/issue_comments_061448.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2021-08-26T02:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61448",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_061449.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-08-26T03:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61449",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061450.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-09-01T06:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7345#issuecomment-61450",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
