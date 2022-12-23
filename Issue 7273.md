# Issue 7273: PIL spkg uses libraries it must not use

Issue created by migration from https://trac.sagemath.org/ticket/7273

Original creator: GeorgSWeber

Original creation time: 2009-10-23 20:50:07

Assignee: mabshoff

From the pil-1.1.6.spkg's "setup.py":

```
# --------------------------------------------------------------------
# Library pointers.
#
# Use None to look for the libraries in well-known library locations.
# Use a string to specify a single directory, for both the library and
# the include files.  Use a tuple to specify separate directories:
# (libpath, includepath).  Examples:
#
# JPEG_ROOT = "/home/libraries/jpeg-6b"
# TIFF_ROOT = "/opt/tiff/lib", "/opt/tiff/include"
#
# If you have "lib" and "include" directories under a common parent,
# you can use the "libinclude" helper:
#
# TIFF_ROOT = libinclude("/opt/tiff")

FREETYPE_ROOT = None
JPEG_ROOT = None
TIFF_ROOT = None
ZLIB_ROOT = None
TCL_ROOT = None

# FIXME: add mechanism to explicitly *disable* the use of a library

# --------------------------------------------------------------------
```

and any of these libraries the setup thinks it finds will be set as

```
-DHAVE_LIBJPEG -DHAVE_LIBZ
```

and the like in "building '_imaging' extension".

This means that if a Sage binary is built on a computer with having some of these libraries, then this binary will *not* work (might not even start) on a computer not having at least these libraries available.

Even more fun (again taken from PIL's setup.py):

```
        elif sys.platform == "darwin":
            # attempt to make sure we pick freetype2 over other versions
            add_directory(include_dirs, "/sw/include/freetype2")
            add_directory(include_dirs, "/sw/lib/freetype2/include")
            # fink installation directories
            add_directory(library_dirs, "/sw/lib")
            add_directory(include_dirs, "/sw/include")
            # darwin ports installation directories
            add_directory(library_dirs, "/opt/local/lib")
            add_directory(include_dirs, "/opt/local/include")
```

Last, but not least, pil-1.1.6 as contained in Sage-4.2.alpha1 breaks the Sage build, at least on my computer. It somehow thinks it could find "libjpeg" and its includes, but then cannot:

```
...
running build_ext
--- using frameworks at /System/Library/Frameworks
building '_imaging' extension
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-
prototypes -DHAVE_LIBJPEG -DHAVE_LIBZ -I/System/Library/Frameworks/
Tcl.framework/Headers -I/System/Library/Frameworks/Tk.framework/
Headers -I/Users/Shared/sage/sage-4.2.alpha1/local/include/freetype2 -
IlibImaging -I/opt/local/include -I/Users/Shared/sage/sage-4.2.alpha1/
local/include -I/usr/local/include -I/usr/include -I/Users/Shared/sage/
sage-4.2.alpha1/local/include/python2.6 -c decode.c -o build/
temp.macosx-10.3-i386-2.6/decode.o
In file included from decode.c:653:
libImaging/Jpeg.h:11:21: error: jpeglib.h: No such file or directory
In file included from decode.c:653:
libImaging/Jpeg.h:17: error: field 'pub' has incomplete type
libImaging/Jpeg.h:26: error: field 'pub' has incomplete type
libImaging/Jpeg.h:49: error: field 'cinfo' has incomplete type
libImaging/Jpeg.h:62: error: field 'pub' has incomplete type
libImaging/Jpeg.h:90: error: field 'cinfo' has incomplete type
error: command 'gcc' failed with exit status 1

The full install.log is at http://sage.math.washington.edu/home/weberg/logs/sage-4.2.alpha1_install.log
```

But the problem with the binaries *will* occur on any platform, not only Darwin.

So we either have to also include a jpeg.spkg, a tiff.spkg, and so on in Sage (and make sure PIL uses these !!!), or cripple PIL to not use any of these libraries (even if they *were* present).

The former is problematic, as far as I remember e.g. the tiff license is not GPL compatible (apart from the technical aspects), but I might be mistaken. Crippling might render PIL pretty useless, however.


---

Comment by was created at 2009-10-23 21:18:02

> Crippling might render PIL pretty useless, however. 

PIL will still be able to work with PNG, which we do include.

---

That said, I'm OK with not including PIL in sage-4.2.  Whoever really wants PIL in Sage should fix the above issues for a future Sage release.


---

Comment by timdumol created at 2009-10-24 14:24:28

I have made a libjpeg (I needed it for PIL) -- it is available here: http://sage.math.washington.edu/home/timdumol/libjpeg-7.p0.spkg


---

Comment by timdumol created at 2009-10-24 14:28:25

As for the TIFF library, it seems to be BSD licensed: http://www.libtiff.org/misc.html, which is GPL compatible, as far as I know. Are there any other libraries needed for inclusion?

I'll gladly make an spkg for libtiff as well, if needed.


---

Comment by timdumol created at 2009-10-29 01:40:46

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-10-29 01:40:46

Here's a libtiff package: http://sage.math.washington.edu/home/timdumol/libtiff-3.9.1.p0.spkg. 
Updated PIL package here: http://sage.math.washington.edu/home/timdumol/pil-1.1.6.p1.spkg. The updated package has explicid dependencies on Sage's libtiff, libpng and libjpeg, and disables TCL/TK.

I'm guessing libtiff and libjpeg have to be voted in?


---

Comment by timdumol created at 2009-10-29 06:24:42

Changed PIL package as per William's suggestion at http://groups.google.com/group/sage-devel/msg/6ea0a0e0a0a2a71a. `libjpeg` and `libtiff` packages are up at #7344 and #7345 respectively. Patch to automatically rebuild PIL in binary build mode attached.


---

Comment by timdumol created at 2009-10-29 06:25:09

`sage-bdist` -- Rebuild PIL in binary build mode.


---

Attachment


---

Comment by was created at 2009-11-11 19:14:55

It has a patch with this name "trac_7273-sage-bdist.spkg".  Huh?  I have no idea what that means.  I'm totally confused by this "with patch; needs review" ticket.


---

Comment by GeorgSWeber created at 2009-11-11 19:50:20

A reviewer (and, on positive review, an integrator) is IMHO supposed to do the following:

- replace the current "pil-1.1.6.spkg" with "pil-1.1.6.p2.spkg" placed (see above) at http://sage.math.washington.edu/home/timdumol/pil-1.1.6.p2.spkg

- apply the patch with the strange name to "$SAGE_ROOT/local/bin/", i.e. the sage_scripts spkg's repository, in order to apply certain changes to the shell-script "sage-bdist" (one can view the contents of this patch from/inside trac just as usual).

And check that everything works fine, i.e. especially in the case of building a Sage binary distribution, neither jpeg nor tiff (even though they migth be present at the host computer where the bdist takes place and/or where the Sage version was built) are added as libraries that the then newly built PIL depends on.


---

Comment by was created at 2009-11-12 06:13:41

Sorry, there was some miscommunication.  I do not like the design of trac_7273-sage-bdist.spkg, in that I strongly disagree with "sage -bdist" literally rebuilding parts of that Sage install.   I would much prefer the following, which would fit well with my workflow:

  (1) introduce a SAGE_BINARY_BUILD flag

  (2) whenever I'm going to build sage binaries, I set that flag in my build script before ever starting any of the builds.  

My understanding is that in fact your pil-1.1.6.p2.spkg in fact fully accomplishes (1) and (2) above already, and that if I simply ignore the patch trac_7273-sage-bdist.spkg  then I get everything I want already? 

Also, should libtiff and libjpeg be posted to the optional spkg repo?  Is there a ticket for that?   To do that, I would want a commitment that 2 people are going to maintain them, at least for the next year (say). 

OK, I've looked at the PIL spkg and I think it looks very good. 

So I'm +1 for putting this new spkg in, and I'm -1 to trac_7273-sage-bdist.spkg.


---

Comment by was created at 2009-11-12 06:13:41

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-12 06:16:18

> I'm guessing libtiff and libjpeg have to be voted in? 

For standard yes, but for optional, the main thing is to get somebody to referee the packages and commit to maintaining them.


---

Comment by mhansen created at 2009-11-12 07:06:23

Resolution: fixed


---

Comment by mhansen created at 2009-11-12 07:06:23

I've merge just the spkg in 4.2.1.rc0.


---

Comment by timdumol created at 2009-11-12 11:53:22

Just to confirm, yes, GeorgSWeber's description was right. The tickets for libtiff and libjpeg are #7345 and #7344. I'm not sure who else can maintain them, though.


---

Comment by kcrisman created at 2010-08-02 17:59:25

See also [here](http://groups.google.com/group/sage-devel/browse_frm/thread/48f720062cc4e38b/ff817dfb819e5ce).
