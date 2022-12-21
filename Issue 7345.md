# Issue 7345: New libtiff package

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-10-29 04:25:27

Assignee: boothby

This is used by PIL (c.f. #7273). Inclusion as an optional or even as a standard package would be helpful.

The package is here:  http://sage.math.washington.edu/home/timdumol/libtiff-3.9.1.p0.spkg


---

Comment by mpatel created at 2009-11-01 01:20:45

Should this belong to a different component?


---

Comment by timdumol created at 2009-11-01 02:16:06

Changing component from notebook to packages.


---

Comment by timdumol created at 2009-11-01 02:16:06

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-11-01 02:16:06

Woops. Yep.


---

Comment by jhpalmieri created at 2009-12-22 06:05:25

Builds fine on Mac OS X 10.6 and sage.math, and installs what look like the right libraries in the right place.  What can I do to test it?

I've marked it as "needs work" because the SPKG.txt file says "libjpeg" several places instead of "libtiff".

Is the spkg-install file modeled after other ones currently in use?  (Will drkirby complain about gnuisms, for instance, or is this derived from one of his spkg-install files?)


---

Comment by jhpalmieri created at 2009-12-22 06:05:25

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2009-12-22 06:08:35

Oh, there is also a file SPKG.txt~ which should not be there.


---

Comment by kcrisman created at 2010-08-02 18:00:14

See also [here](http://groups.google.com/group/sage-devel/browse_frm/thread/48f720062cc4e38b/ff817dfb819e5ce).


---

Comment by boothby created at 2010-08-02 18:07:28

Changing assignee from boothby to timdumol.


---

Comment by timdumol created at 2010-08-17 18:17:01

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-08-17 18:17:01

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

Comment by mariah created at 2011-05-13 13:39:50

Changing status from needs_review to needs_info.


---

Comment by mariah created at 2011-05-13 13:39:50

[http://libtiff.org](http://libtiff.org) says latest version is 3.6.1, yet this
spkg is labeled 3.9.4.  Why?


---

Comment by timdumol created at 2011-08-02 17:30:53

The web page itself is outdated. The downloads page: ftp://ftp.remotesensing.org/pub/libtiff actually states that the latest package is 3.9.5.


---

Comment by timdumol created at 2011-08-02 17:30:53

Changing status from needs_info to needs_review.


---

Comment by timdumol created at 2011-08-02 17:31:13

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2011-08-02 18:20:05

New package here: http://sage.math.washington.edu/home/timdumol/libtiff-3.9.5.spkg


---

Comment by timdumol created at 2011-08-02 18:20:05

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-08-03 00:01:10

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

Comment by jhpalmieri created at 2011-08-03 00:01:10

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2011-08-03 09:22:15

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2011-08-03 09:22:15

In the notebook, `im.show()` saves a JPEG into the worksheet directory, which is then automatically displayed by the SageNB. Thus, the error you got was actually because PIL has no access to libjpeg, and is thus not related to this package.


---

Comment by jhpalmieri created at 2011-08-03 15:43:15

I was actually working from the command line, but anyway, what about this part:

```
sage: im = im.resize((im.size[0]/2,im.size[1]/2))
sage: print im.format
None
```

According to the earlier example, this should have said "TIFF".


---

Comment by jhpalmieri created at 2011-08-03 15:43:15

Changing status from needs_review to needs_info.


---

Comment by jhpalmieri created at 2011-08-03 15:52:22

By the way, I can successfully save the resized image.  Somewhere along the line I reinstalled PIL, so I don't know if that's necessary.


---

Comment by jhpalmieri created at 2011-08-03 22:16:29

Two things: since this package installs files into `SAGE_ROOT/local/bin`, you should add those files to `.hgignore` — this will require a separate patch to the scripts repo.  Also the spkg file contains "SPKG.txt~", which shouldn't be there.


---

Comment by leif created at 2011-08-04 12:41:26

Replying to [comment:13 timdumol]:
> In the notebook, `im.show()` saves a JPEG into the worksheet directory, which is then automatically displayed by the SageNB.

May I ask why? Does it make any sense to convert a "lossless image" into a lossy format, i.e., why not convert it to e.g. PNG which any (GUI) browser should be able to display?

(I know TIFF is also a "meta format", i.e. you can encapsulate JPEGs in a TIFF file, but John's example file doesn't look like it was such.)

The only reason I can imagine is that it's easier to scale JPEG images than bitmaps, but unless we include the batteries by default, a simple `show()` of a bitmap image shouldn't require `libjpeg`.


---

Comment by was created at 2011-08-24 23:46:36

Changing keywords from "" to "sd32".


---

Comment by janssen created at 2011-11-12 23:11:29

Regarding the im.format printing as None, that's OK, since the format attribute is only defined if the image was loaded from a file.

Regarding the action of Image.show():  Leif is right, using JPEG is a bad idea.  Using TIFF is also a bad idea, for this purpose, as the PIL TIFF encoder only saves uncompressed TIFF files.  They're big and slow.  I second the idea of using PNG for Image.show().  But that really is a separate issue, and should be broken out as such.


---

Comment by janssen created at 2011-11-12 23:42:41

Hmm, I see that JPEG is hard-coded into PIL 1.1.6.  In PIL 1.1.7, im.show() uses a non-lossy format, and the user can override the viewer used by show(), so one custom-designed for Sage could be put in there if necessary.


---

Comment by jdemeyer created at 2014-11-13 14:04:00

Changing component from packages: standard to packages: optional.


---

Comment by mkoeppe created at 2021-08-26 02:41:10

outdated, should close


---

Comment by mkoeppe created at 2021-08-26 02:41:10

Changing status from needs_info to needs_review.


---

Comment by jhpalmieri created at 2021-08-26 03:50:18

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2021-09-01 06:16:58

Resolution: invalid
