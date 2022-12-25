# Issue 7273: PIL spkg uses libraries it must not use

archive/issues_007273.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrom the pil-1.1.6.spkg's \"setup.py\":\n\n```\n# --------------------------------------------------------------------\n# Library pointers.\n#\n# Use None to look for the libraries in well-known library locations.\n# Use a string to specify a single directory, for both the library and\n# the include files.  Use a tuple to specify separate directories:\n# (libpath, includepath).  Examples:\n#\n# JPEG_ROOT = \"/home/libraries/jpeg-6b\"\n# TIFF_ROOT = \"/opt/tiff/lib\", \"/opt/tiff/include\"\n#\n# If you have \"lib\" and \"include\" directories under a common parent,\n# you can use the \"libinclude\" helper:\n#\n# TIFF_ROOT = libinclude(\"/opt/tiff\")\n\nFREETYPE_ROOT = None\nJPEG_ROOT = None\nTIFF_ROOT = None\nZLIB_ROOT = None\nTCL_ROOT = None\n\n# FIXME: add mechanism to explicitly *disable* the use of a library\n\n# --------------------------------------------------------------------\n```\n\nand any of these libraries the setup thinks it finds will be set as\n\n```\n-DHAVE_LIBJPEG -DHAVE_LIBZ\n```\n\nand the like in \"building '_imaging' extension\".\n\nThis means that if a Sage binary is built on a computer with having some of these libraries, then this binary will *not* work (might not even start) on a computer not having at least these libraries available.\n\nEven more fun (again taken from PIL's setup.py):\n\n```\n        elif sys.platform == \"darwin\":\n            # attempt to make sure we pick freetype2 over other versions\n            add_directory(include_dirs, \"/sw/include/freetype2\")\n            add_directory(include_dirs, \"/sw/lib/freetype2/include\")\n            # fink installation directories\n            add_directory(library_dirs, \"/sw/lib\")\n            add_directory(include_dirs, \"/sw/include\")\n            # darwin ports installation directories\n            add_directory(library_dirs, \"/opt/local/lib\")\n            add_directory(include_dirs, \"/opt/local/include\")\n```\n\nLast, but not least, pil-1.1.6 as contained in Sage-4.2.alpha1 breaks the Sage build, at least on my computer. It somehow thinks it could find \"libjpeg\" and its includes, but then cannot:\n\n```\n...\nrunning build_ext\n--- using frameworks at /System/Library/Frameworks\nbuilding '_imaging' extension\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-\nprototypes -DHAVE_LIBJPEG -DHAVE_LIBZ -I/System/Library/Frameworks/\nTcl.framework/Headers -I/System/Library/Frameworks/Tk.framework/\nHeaders -I/Users/Shared/sage/sage-4.2.alpha1/local/include/freetype2 -\nIlibImaging -I/opt/local/include -I/Users/Shared/sage/sage-4.2.alpha1/\nlocal/include -I/usr/local/include -I/usr/include -I/Users/Shared/sage/\nsage-4.2.alpha1/local/include/python2.6 -c decode.c -o build/\ntemp.macosx-10.3-i386-2.6/decode.o\nIn file included from decode.c:653:\nlibImaging/Jpeg.h:11:21: error: jpeglib.h: No such file or directory\nIn file included from decode.c:653:\nlibImaging/Jpeg.h:17: error: field 'pub' has incomplete type\nlibImaging/Jpeg.h:26: error: field 'pub' has incomplete type\nlibImaging/Jpeg.h:49: error: field 'cinfo' has incomplete type\nlibImaging/Jpeg.h:62: error: field 'pub' has incomplete type\nlibImaging/Jpeg.h:90: error: field 'cinfo' has incomplete type\nerror: command 'gcc' failed with exit status 1\n\nThe full install.log is at http://sage.math.washington.edu/home/weberg/logs/sage-4.2.alpha1_install.log\n```\n\nBut the problem with the binaries *will* occur on any platform, not only Darwin.\n\nSo we either have to also include a jpeg.spkg, a tiff.spkg, and so on in Sage (and make sure PIL uses these !!!), or cripple PIL to not use any of these libraries (even if they *were* present).\n\nThe former is problematic, as far as I remember e.g. the tiff license is not GPL compatible (apart from the technical aspects), but I might be mistaken. Crippling might render PIL pretty useless, however.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7273\n\n",
    "created_at": "2009-10-23T20:50:07Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "PIL spkg uses libraries it must not use",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7273",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/7273





---

archive/issue_comments_060399.json:
```json
{
    "body": "> Crippling might render PIL pretty useless, however. \n\nPIL will still be able to work with PNG, which we do include.\n\n---\n\nThat said, I'm OK with not including PIL in sage-4.2.  Whoever really wants PIL in Sage should fix the above issues for a future Sage release.",
    "created_at": "2009-10-23T21:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60399",
    "user": "https://github.com/williamstein"
}
```

> Crippling might render PIL pretty useless, however. 

PIL will still be able to work with PNG, which we do include.

---

That said, I'm OK with not including PIL in sage-4.2.  Whoever really wants PIL in Sage should fix the above issues for a future Sage release.



---

archive/issue_comments_060400.json:
```json
{
    "body": "I have made a libjpeg (I needed it for PIL) -- it is available here: http://sage.math.washington.edu/home/timdumol/libjpeg-7.p0.spkg",
    "created_at": "2009-10-24T14:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60400",
    "user": "https://github.com/TimDumol"
}
```

I have made a libjpeg (I needed it for PIL) -- it is available here: http://sage.math.washington.edu/home/timdumol/libjpeg-7.p0.spkg



---

archive/issue_comments_060401.json:
```json
{
    "body": "As for the TIFF library, it seems to be BSD licensed: http://www.libtiff.org/misc.html, which is GPL compatible, as far as I know. Are there any other libraries needed for inclusion?\n\nI'll gladly make an spkg for libtiff as well, if needed.",
    "created_at": "2009-10-24T14:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60401",
    "user": "https://github.com/TimDumol"
}
```

As for the TIFF library, it seems to be BSD licensed: http://www.libtiff.org/misc.html, which is GPL compatible, as far as I know. Are there any other libraries needed for inclusion?

I'll gladly make an spkg for libtiff as well, if needed.



---

archive/issue_comments_060402.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-29T01:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60402",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060403.json:
```json
{
    "body": "Here's a libtiff package: http://sage.math.washington.edu/home/timdumol/libtiff-3.9.1.p0.spkg. \nUpdated PIL package here: http://sage.math.washington.edu/home/timdumol/pil-1.1.6.p1.spkg. The updated package has explicid dependencies on Sage's libtiff, libpng and libjpeg, and disables TCL/TK.\n\nI'm guessing libtiff and libjpeg have to be voted in?",
    "created_at": "2009-10-29T01:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60403",
    "user": "https://github.com/TimDumol"
}
```

Here's a libtiff package: http://sage.math.washington.edu/home/timdumol/libtiff-3.9.1.p0.spkg. 
Updated PIL package here: http://sage.math.washington.edu/home/timdumol/pil-1.1.6.p1.spkg. The updated package has explicid dependencies on Sage's libtiff, libpng and libjpeg, and disables TCL/TK.

I'm guessing libtiff and libjpeg have to be voted in?



---

archive/issue_comments_060404.json:
```json
{
    "body": "Changed PIL package as per William's suggestion at http://groups.google.com/group/sage-devel/msg/6ea0a0e0a0a2a71a. `libjpeg` and `libtiff` packages are up at #7344 and #7345 respectively. Patch to automatically rebuild PIL in binary build mode attached.",
    "created_at": "2009-10-29T06:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60404",
    "user": "https://github.com/TimDumol"
}
```

Changed PIL package as per William's suggestion at http://groups.google.com/group/sage-devel/msg/6ea0a0e0a0a2a71a. `libjpeg` and `libtiff` packages are up at #7344 and #7345 respectively. Patch to automatically rebuild PIL in binary build mode attached.



---

archive/issue_comments_060405.json:
```json
{
    "body": "`sage-bdist` -- Rebuild PIL in binary build mode.",
    "created_at": "2009-10-29T06:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60405",
    "user": "https://github.com/TimDumol"
}
```

`sage-bdist` -- Rebuild PIL in binary build mode.



---

archive/issue_comments_060406.json:
```json
{
    "body": "Attachment [trac_7273-sage-bdist.spkg](tarball://root/attachments/some-uuid/ticket7273/trac_7273-sage-bdist.spkg) by @TimDumol created at 2009-10-29 06:29:46",
    "created_at": "2009-10-29T06:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60406",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7273-sage-bdist.spkg](tarball://root/attachments/some-uuid/ticket7273/trac_7273-sage-bdist.spkg) by @TimDumol created at 2009-10-29 06:29:46



---

archive/issue_comments_060407.json:
```json
{
    "body": "It has a patch with this name \"trac_7273-sage-bdist.spkg\".  Huh?  I have no idea what that means.  I'm totally confused by this \"with patch; needs review\" ticket.",
    "created_at": "2009-11-11T19:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60407",
    "user": "https://github.com/williamstein"
}
```

It has a patch with this name "trac_7273-sage-bdist.spkg".  Huh?  I have no idea what that means.  I'm totally confused by this "with patch; needs review" ticket.



---

archive/issue_comments_060408.json:
```json
{
    "body": "A reviewer (and, on positive review, an integrator) is IMHO supposed to do the following:\n\n- replace the current \"pil-1.1.6.spkg\" with \"pil-1.1.6.p2.spkg\" placed (see above) at http://sage.math.washington.edu/home/timdumol/pil-1.1.6.p2.spkg\n\n- apply the patch with the strange name to \"$SAGE_ROOT/local/bin/\", i.e. the sage_scripts spkg's repository, in order to apply certain changes to the shell-script \"sage-bdist\" (one can view the contents of this patch from/inside trac just as usual).\n\nAnd check that everything works fine, i.e. especially in the case of building a Sage binary distribution, neither jpeg nor tiff (even though they migth be present at the host computer where the bdist takes place and/or where the Sage version was built) are added as libraries that the then newly built PIL depends on.",
    "created_at": "2009-11-11T19:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60408",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

A reviewer (and, on positive review, an integrator) is IMHO supposed to do the following:

- replace the current "pil-1.1.6.spkg" with "pil-1.1.6.p2.spkg" placed (see above) at http://sage.math.washington.edu/home/timdumol/pil-1.1.6.p2.spkg

- apply the patch with the strange name to "$SAGE_ROOT/local/bin/", i.e. the sage_scripts spkg's repository, in order to apply certain changes to the shell-script "sage-bdist" (one can view the contents of this patch from/inside trac just as usual).

And check that everything works fine, i.e. especially in the case of building a Sage binary distribution, neither jpeg nor tiff (even though they migth be present at the host computer where the bdist takes place and/or where the Sage version was built) are added as libraries that the then newly built PIL depends on.



---

archive/issue_comments_060409.json:
```json
{
    "body": "Sorry, there was some miscommunication.  I do not like the design of trac_7273-sage-bdist.spkg, in that I strongly disagree with \"sage -bdist\" literally rebuilding parts of that Sage install.   I would much prefer the following, which would fit well with my workflow:\n\n  (1) introduce a SAGE_BINARY_BUILD flag\n\n  (2) whenever I'm going to build sage binaries, I set that flag in my build script before ever starting any of the builds.  \n\nMy understanding is that in fact your pil-1.1.6.p2.spkg in fact fully accomplishes (1) and (2) above already, and that if I simply ignore the patch trac_7273-sage-bdist.spkg  then I get everything I want already? \n\nAlso, should libtiff and libjpeg be posted to the optional spkg repo?  Is there a ticket for that?   To do that, I would want a commitment that 2 people are going to maintain them, at least for the next year (say). \n\nOK, I've looked at the PIL spkg and I think it looks very good. \n\nSo I'm +1 for putting this new spkg in, and I'm -1 to trac_7273-sage-bdist.spkg.",
    "created_at": "2009-11-12T06:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60409",
    "user": "https://github.com/williamstein"
}
```

Sorry, there was some miscommunication.  I do not like the design of trac_7273-sage-bdist.spkg, in that I strongly disagree with "sage -bdist" literally rebuilding parts of that Sage install.   I would much prefer the following, which would fit well with my workflow:

  (1) introduce a SAGE_BINARY_BUILD flag

  (2) whenever I'm going to build sage binaries, I set that flag in my build script before ever starting any of the builds.  

My understanding is that in fact your pil-1.1.6.p2.spkg in fact fully accomplishes (1) and (2) above already, and that if I simply ignore the patch trac_7273-sage-bdist.spkg  then I get everything I want already? 

Also, should libtiff and libjpeg be posted to the optional spkg repo?  Is there a ticket for that?   To do that, I would want a commitment that 2 people are going to maintain them, at least for the next year (say). 

OK, I've looked at the PIL spkg and I think it looks very good. 

So I'm +1 for putting this new spkg in, and I'm -1 to trac_7273-sage-bdist.spkg.



---

archive/issue_comments_060410.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-12T06:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60410",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060411.json:
```json
{
    "body": "> I'm guessing libtiff and libjpeg have to be voted in? \n\nFor standard yes, but for optional, the main thing is to get somebody to referee the packages and commit to maintaining them.",
    "created_at": "2009-11-12T06:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60411",
    "user": "https://github.com/williamstein"
}
```

> I'm guessing libtiff and libjpeg have to be voted in? 

For standard yes, but for optional, the main thing is to get somebody to referee the packages and commit to maintaining them.



---

archive/issue_comments_060412.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T07:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60412",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_060413.json:
```json
{
    "body": "I've merge just the spkg in 4.2.1.rc0.",
    "created_at": "2009-11-12T07:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60413",
    "user": "https://github.com/mwhansen"
}
```

I've merge just the spkg in 4.2.1.rc0.



---

archive/issue_comments_060414.json:
```json
{
    "body": "Just to confirm, yes, GeorgSWeber's description was right. The tickets for libtiff and libjpeg are #7345 and #7344. I'm not sure who else can maintain them, though.",
    "created_at": "2009-11-12T11:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60414",
    "user": "https://github.com/TimDumol"
}
```

Just to confirm, yes, GeorgSWeber's description was right. The tickets for libtiff and libjpeg are #7345 and #7344. I'm not sure who else can maintain them, though.



---

archive/issue_comments_060415.json:
```json
{
    "body": "See also [here](http://groups.google.com/group/sage-devel/browse_frm/thread/48f720062cc4e38b/ff817dfb819e5ce).",
    "created_at": "2010-08-02T17:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7273#issuecomment-60415",
    "user": "https://github.com/kcrisman"
}
```

See also [here](http://groups.google.com/group/sage-devel/browse_frm/thread/48f720062cc4e38b/ff817dfb819e5ce).
