# Issue 2094: Add jpeg support to gd

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2008-02-08 01:21:07

Assignee: was

CC:  dimpase

jpeg is a common format that most people keep their pictures in -- let's support it!


---

Comment by boothby created at 2008-02-08 01:22:49

New spkg files at:

http://sage.math.washington.edu/home/boothby/SPKG/2.10.1/


---

Attachment


---

Comment by boothby created at 2008-02-08 01:38:31

Works on intel 64 / ubuntu -- needs testing on amd64, mac osx, 386, etc.


---

Comment by mhampton created at 2008-04-27 23:52:41

I'm confused on how to test this - can you provide an example of using jpeg?

I think I have everything installed/patched OK, I'm just not sure how to use it.  I tried hacking the plot save command, but ran into trouble with matplotlib since it doesn't have good jpeg support.


---

Comment by craigcitro created at 2008-06-15 21:36:48

Changing keywords from "" to "editor_craigcitro".


---

Comment by boothby created at 2008-06-16 20:55:58

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

Comment by boothby created at 2008-06-16 21:42:26

Instructions for reviewer(s):

The deps/install patches are diffed against files in the Sage distribution which are not (for better or worse) under revision control.  To test, please install the spkgs in the order (jpeg, gd, gdmodule).  Then, run the sample code above.


---

Comment by mhampton created at 2008-06-16 21:47:03

I get the following error (the spkgs seem to have installed without errors):

Traceback (most recent call last):    
  File "/Volumes/D/sage-3.0.2/local/lib/python2.5/site-packages/gd.py", line 10, in <module>
    import _gd
ImportError: dlopen(/Volumes/D/sage-3.0.2/local/lib/python2.5/site-packages/_gd.so, 2): Symbol not found: _jpeg_std_error
  Referenced from: /Volumes/D/sage-3.0.2/local/lib//libgd.2.dylib
  Expected in: flat namespace


---

Comment by boothby created at 2008-06-17 06:38:08

Possible hints are here:

http://trac.macports.org/browser/trunk/dports/graphics/jpeg


---

Comment by craigcitro created at 2008-06-19 19:33:14

Tom agrees that this patch needs work to function on a Mac. He'll get to it soon-ish.


---

Comment by craigcitro created at 2008-06-20 04:20:00

Notice that these are (basically) the same errors we're seeing on #3324.


---

Comment by mabshoff created at 2008-08-30 18:49:57

This is a framework vs. sane library issue - I will likely have a workaround for this in the not too distant future.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-20 22:27:31

Since we now do no longer build anything against the Apple IOKit Framework this spkg should be re-reviewed.

Cheers,

Michael


---

Comment by mhampton created at 2008-09-21 02:57:54

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

Comment by mhampton created at 2008-09-21 03:17:28

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

Comment by mabshoff created at 2008-09-21 05:20:16

I can fix this on OSX. Give me a little while. Besides adding the jpeg.spkg this also needs matching fixes to the gd.spkg

Cheers,

Michael


---

Comment by mhampton created at 2008-09-22 16:54:12

OK, I have gotten this working as well, using gd-2.0.35.  I messed up previously when trying to install it.  I can make a spkg if you want, but you'd probably have to edit my attempts anyway.

-M.Hampton


---

Comment by mabshoff created at 2008-09-22 18:03:34

Replying to [comment:19 mhampton]:
> OK, I have gotten this working as well, using gd-2.0.35.  I messed up previously when trying to install it.  I can make a spkg if you want, but you'd probably have to edit my attempts anyway.
> 
> -M.Hampton

We are already using gd-2.0.35, so what changes do you propose to make? Either way, an jpeg.spkg would have to be voted in anyway.

Cheers,

Michael


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Outdated spkg or build system ticket, should be closed


---

Comment by chapoton created at 2020-09-08 18:07:36

Resolution: invalid
