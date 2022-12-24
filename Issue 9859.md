# Issue 9859: Port changes in PARI 2.3.5.p4 (#9722) to current 2.4.3

archive/issues_009859.json:
```json
{
    "body": "Assignee: leif\n\nSome fixes to PARI 2.3.5.p2 from #9722 had to be ported to the current [NewPARI](http://wiki.sagemath.org/wiki/NewPARI) spkg. The new PARI 2.4.3.p5 spkg here contains some further changes (including some on Sage's side, mostly clean-up), while other issues have meanwhile been fixed upstream.\n\n----\n\n### pari-2.4.3.svn-12577.p5 (Leif Leonhardy, September 5th, 2010)\n* Added patches to:\n  - config/get_config_options:\n    * Make invalid arguments to \"--graphic\" a \"Configure\" error\n      (rather than potentially running into *compilation* errors\n      later).\n  - config/get_fltk: (see also/ported from #9722)\n    * Add libstdc++ to the libraries (to support Fedora 13 et al.).\n    * Also check the presence of the FLTK include directory to\n      prevent compilation errors on broken installations.\n  - config/get_X11: (see also/ported from #9722)\n    * Also search */lib64/* directories when doing a 64-bit build.\n    * Give more specific messages.\n* Slightly extended existing patch to src/kernel/gmp/mp.c:\n  - Allow disabling PARI's use of \"GMP internals\" by preprocessor\n    directive (i.e. by adding \"-DPARI_DONT_USE_GMP_INTERNALS\" to\n    CFLAGS). Brief explanation added.\n* spkg-install:\n  - Don't override user-specified CFLAGS (w.r.t. optimization, unless\n    SAGE_DEBUG=yes).\n  - Handle PARI_EXTRA_OPTS properly, and print informative messages\n    (regarding graphics support for plotting).\n  - Recognize SAGE_TUNE_PARI in addition to SAGE_TUNE_pari, and\n    add \"--tune\" to PARI_EXTRA_OPTS if self-tuning was requested.\n  - Clear/unset lots of (environment) variables used by PARI that might\n    unintentionally get their values from user settings.\n  - Quote *all* occurrences of SAGE_LOCAL (and some other expressions).\n  - Use $UNAME instead of `uname` everywhere, use \"elif ...\".\n  - *Always* use $MAKE (changed for \"install-data\").\n  - Begin all error messages with \"Error\".\n  - Removed useless tests of $? at end.\n  - Some clean-up (typos, formatting); some comments, some messages added.\n* spkg-check:\n  - Use $MAKE instead of \"make\".\n  - Don't override user-specified CFLAGS (w.r.t. optimization, unless\n    SAGE_DEBUG=yes).\n  - Begin error message with \"Error\".\n  - Some clean-up.\n* Slight corrections to SPKG.txt.\n* Updated patches/README.txt, some cosmetic changes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9860\n\n",
    "created_at": "2010-09-06T11:47:15Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "Port changes in PARI 2.3.5.p4 (#9722) to current 2.4.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9859",
    "user": "leif"
}
```
Assignee: leif

Some fixes to PARI 2.3.5.p2 from #9722 had to be ported to the current [NewPARI](http://wiki.sagemath.org/wiki/NewPARI) spkg. The new PARI 2.4.3.p5 spkg here contains some further changes (including some on Sage's side, mostly clean-up), while other issues have meanwhile been fixed upstream.

----

### pari-2.4.3.svn-12577.p5 (Leif Leonhardy, September 5th, 2010)
* Added patches to:
  - config/get_config_options:
    * Make invalid arguments to "--graphic" a "Configure" error
      (rather than potentially running into *compilation* errors
      later).
  - config/get_fltk: (see also/ported from #9722)
    * Add libstdc++ to the libraries (to support Fedora 13 et al.).
    * Also check the presence of the FLTK include directory to
      prevent compilation errors on broken installations.
  - config/get_X11: (see also/ported from #9722)
    * Also search */lib64/* directories when doing a 64-bit build.
    * Give more specific messages.
* Slightly extended existing patch to src/kernel/gmp/mp.c:
  - Allow disabling PARI's use of "GMP internals" by preprocessor
    directive (i.e. by adding "-DPARI_DONT_USE_GMP_INTERNALS" to
    CFLAGS). Brief explanation added.
* spkg-install:
  - Don't override user-specified CFLAGS (w.r.t. optimization, unless
    SAGE_DEBUG=yes).
  - Handle PARI_EXTRA_OPTS properly, and print informative messages
    (regarding graphics support for plotting).
  - Recognize SAGE_TUNE_PARI in addition to SAGE_TUNE_pari, and
    add "--tune" to PARI_EXTRA_OPTS if self-tuning was requested.
  - Clear/unset lots of (environment) variables used by PARI that might
    unintentionally get their values from user settings.
  - Quote *all* occurrences of SAGE_LOCAL (and some other expressions).
  - Use $UNAME instead of `uname` everywhere, use "elif ...".
  - *Always* use $MAKE (changed for "install-data").
  - Begin all error messages with "Error".
  - Removed useless tests of $? at end.
  - Some clean-up (typos, formatting); some comments, some messages added.
* spkg-check:
  - Use $MAKE instead of "make".
  - Don't override user-specified CFLAGS (w.r.t. optimization, unless
    SAGE_DEBUG=yes).
  - Begin error message with "Error".
  - Some clean-up.
* Slight corrections to SPKG.txt.
* Updated patches/README.txt, some cosmetic changes.

Issue created by migration from https://trac.sagemath.org/ticket/9860





---

archive/issue_comments_097338.json:
```json
{
    "body": "Apply to pari-2.4.3.svn-12577.p4.spkg. Note that added/changed files in `patches/files` are not included here!",
    "created_at": "2010-09-06T11:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97338",
    "user": "leif"
}
```

Apply to pari-2.4.3.svn-12577.p4.spkg. Note that added/changed files in `patches/files` are not included here!



---

archive/issue_comments_097339.json:
```json
{
    "body": "Attachment [trac_9860-pari-2.4.3.svn-12577.p4-p5.spkg.patch](tarball://root/attachments/some-uuid/ticket9860/trac_9860-pari-2.4.3.svn-12577.p4-p5.spkg.patch) by leif created at 2010-09-06 12:12:47\n\nDiff of files in `patches/files`. Apply with `patch -p1` inside spkg directory.",
    "created_at": "2010-09-06T12:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97339",
    "user": "leif"
}
```

Attachment [trac_9860-pari-2.4.3.svn-12577.p4-p5.spkg.patch](tarball://root/attachments/some-uuid/ticket9860/trac_9860-pari-2.4.3.svn-12577.p4-p5.spkg.patch) by leif created at 2010-09-06 12:12:47

Diff of files in `patches/files`. Apply with `patch -p1` inside spkg directory.



---

archive/issue_comments_097340.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-06T12:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97340",
    "user": "leif"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097341.json:
```json
{
    "body": "Attachment [trac_9860-patched_files_not_under_revision_control.p4-p5.spkg.diff](tarball://root/attachments/some-uuid/ticket9860/trac_9860-patched_files_not_under_revision_control.p4-p5.spkg.diff) by leif created at 2010-09-06 12:38:46",
    "created_at": "2010-09-06T12:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97341",
    "user": "leif"
}
```

Attachment [trac_9860-patched_files_not_under_revision_control.p4-p5.spkg.diff](tarball://root/attachments/some-uuid/ticket9860/trac_9860-patched_files_not_under_revision_control.p4-p5.spkg.diff) by leif created at 2010-09-06 12:38:46



---

archive/issue_comments_097342.json:
```json
{
    "body": "I've only tested this with a couple of variations on parameters and installed libraries / graphics packages on Ubuntu 10.04 x86_64 and Fedora 13 x86.\n\n*Should* work on other systems as well... ;-)",
    "created_at": "2010-09-06T12:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97342",
    "user": "leif"
}
```

I've only tested this with a couple of variations on parameters and installed libraries / graphics packages on Ubuntu 10.04 x86_64 and Fedora 13 x86.

*Should* work on other systems as well... ;-)



---

archive/issue_comments_097343.json:
```json
{
    "body": "What do I need to do to test this - **just** download the package - do I need to patch anything else? \n\nI've done:\n\n* Downloaded and installed  http://spkg-upload.googlecode.com/files/pari-2.4.3.svn-12577.p5.spkg\n* Nothing else changed from 4.5.3.alpha2\n* No attempt to tune code\n \n\n```\ndrkirkby@hawk:~/5/sage-4.5.3.alpha2$ ./sage -b\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\ngcc -o src/convert.pic.o -c -fPIC -I/export/home/drkirkby/5/sage-4.5.3.alpha2/local/include -I/export/home/drkirkby/5/sage-4.5.3.alpha2/local/include/python2.6 -I/export/home/drkirkby/5/sage-4.5.3.alpha2/local/include/NTL -Iinclude src/convert.c\ng++ -o libcsage.so -shared src/convert.pic.o src/interrupt.pic.o src/mpn_pylong.pic.o src/mpz_pylong.pic.o src/mpz_longlong.pic.o src/stdsage.pic.o src/gmp_globals.pic.o src/ZZ_pylong.pic.o src/ntl_wrap.pic.o -L/export/home/drkirkby/5/sage-4.5.3.alpha2/local/lib -L/export/home/drkirkby/5/sage-4.5.3.alpha2/local/lib/python/config -lntl -lgmp -lpari -lpython2.6\nUpdating Cython code....\nExecute 0 commands (using 0 threads)\nTime to execute 0 commands: 0.0976297855377 seconds\nFinished compiling Cython code (time = 3.07916307449 seconds)\nrunning install\nrunning build\nrunning build_py\nrunning build_ext\nTotal time spent compiling C/C++ extensions:  0.913223028183 seconds.\nrunning install_lib\nrunning install_egg_info\nRemoving /export/home/drkirkby/5/sage-4.5.3.alpha2/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\nWriting /export/home/drkirkby/5/sage-4.5.3.alpha2/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\n\nreal\t0m8.727s\nuser\t0m1.339s\nsys\t0m0.727s\ndrkirkby@hawk:~/5/sage-4.5.3.alpha2$ make ptestlong\ncd spkg && ./install all 2>&1 | tee -a ../install.log\nmake[1]: Entering directory `/export/home/drkirkby/5/sage-4.5.3.alpha2/spkg'\nmake[1]: Nothing to be done for `all'.\nmake[1]: Leaving directory `/export/home/drkirkby/5/sage-4.5.3.alpha2/spkg'\n\nreal\t0m0.018s\nuser\t0m0.003s\nsys\t0m0.003s\nTo install gap, gp, singular, etc., scripts\nin a standard bin directory, start sage and\ntype something like\n   sage: install_scripts('/usr/local/bin')\nat the Sage command prompt.\n\nTo build the documentation, run\n   make doc\n\nSage build/upgrade complete!\n./sage -docbuild all html  2>&1 | tee -a dochtml.log\nsphinx-build -b html -d /export/home/drkirkby/5/sage-4.5.3.alpha2/devel/sage/doc/output/doctrees/en/website    /export/home/drkirkby/5/sage-4.5.3.alpha2/devel/sage/doc/en/website /export/home/drkirkby/5/sage-4.5.3.alpha2/devel/sage/doc/output/html/en/website\n  ***   bug in PARI/GP (Segmentation Fault), please report\n^Cmake: *** [doc-html] Interrupt\n```\n\n\nIIRC, the changes from `sage-4.5.3.alpha2` to `sage-4.5.3.rc0` were just a few Solaris-specific changes which would not all all doc tests to pass, but were not need to actually get things working. \n\nThis is on an OpenSolaris (Xeon processor) machine. I've not tried on anything else. \n\nI'm rather hoping I've forgot something - in which case you have time to review #9603 !\n\nDave",
    "created_at": "2010-09-06T15:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97343",
    "user": "drkirkby"
}
```

What do I need to do to test this - **just** download the package - do I need to patch anything else? 

I've done:

* Downloaded and installed  http://spkg-upload.googlecode.com/files/pari-2.4.3.svn-12577.p5.spkg
* Nothing else changed from 4.5.3.alpha2
* No attempt to tune code
 

```
drkirkby@hawk:~/5/sage-4.5.3.alpha2$ ./sage -b

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
gcc -o src/convert.pic.o -c -fPIC -I/export/home/drkirkby/5/sage-4.5.3.alpha2/local/include -I/export/home/drkirkby/5/sage-4.5.3.alpha2/local/include/python2.6 -I/export/home/drkirkby/5/sage-4.5.3.alpha2/local/include/NTL -Iinclude src/convert.c
g++ -o libcsage.so -shared src/convert.pic.o src/interrupt.pic.o src/mpn_pylong.pic.o src/mpz_pylong.pic.o src/mpz_longlong.pic.o src/stdsage.pic.o src/gmp_globals.pic.o src/ZZ_pylong.pic.o src/ntl_wrap.pic.o -L/export/home/drkirkby/5/sage-4.5.3.alpha2/local/lib -L/export/home/drkirkby/5/sage-4.5.3.alpha2/local/lib/python/config -lntl -lgmp -lpari -lpython2.6
Updating Cython code....
Execute 0 commands (using 0 threads)
Time to execute 0 commands: 0.0976297855377 seconds
Finished compiling Cython code (time = 3.07916307449 seconds)
running install
running build
running build_py
running build_ext
Total time spent compiling C/C++ extensions:  0.913223028183 seconds.
running install_lib
running install_egg_info
Removing /export/home/drkirkby/5/sage-4.5.3.alpha2/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /export/home/drkirkby/5/sage-4.5.3.alpha2/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info

real	0m8.727s
user	0m1.339s
sys	0m0.727s
drkirkby@hawk:~/5/sage-4.5.3.alpha2$ make ptestlong
cd spkg && ./install all 2>&1 | tee -a ../install.log
make[1]: Entering directory `/export/home/drkirkby/5/sage-4.5.3.alpha2/spkg'
make[1]: Nothing to be done for `all'.
make[1]: Leaving directory `/export/home/drkirkby/5/sage-4.5.3.alpha2/spkg'

real	0m0.018s
user	0m0.003s
sys	0m0.003s
To install gap, gp, singular, etc., scripts
in a standard bin directory, start sage and
type something like
   sage: install_scripts('/usr/local/bin')
at the Sage command prompt.

To build the documentation, run
   make doc

Sage build/upgrade complete!
./sage -docbuild all html  2>&1 | tee -a dochtml.log
sphinx-build -b html -d /export/home/drkirkby/5/sage-4.5.3.alpha2/devel/sage/doc/output/doctrees/en/website    /export/home/drkirkby/5/sage-4.5.3.alpha2/devel/sage/doc/en/website /export/home/drkirkby/5/sage-4.5.3.alpha2/devel/sage/doc/output/html/en/website
  ***   bug in PARI/GP (Segmentation Fault), please report
^Cmake: *** [doc-html] Interrupt
```


IIRC, the changes from `sage-4.5.3.alpha2` to `sage-4.5.3.rc0` were just a few Solaris-specific changes which would not all all doc tests to pass, but were not need to actually get things working. 

This is on an OpenSolaris (Xeon processor) machine. I've not tried on anything else. 

I'm rather hoping I've forgot something - in which case you have time to review #9603 !

Dave



---

archive/issue_comments_097344.json:
```json
{
    "body": "Replying to [comment:3 drkirkby]:\n> What do I need to do to test this - **just** download the package - do I need to patch anything else? \nYou also need to apply the sagelib and extcode patches from #9343.  Or easier: download [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar), install that and *then* install the new pari spkg.",
    "created_at": "2010-09-06T16:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97344",
    "user": "jdemeyer"
}
```

Replying to [comment:3 drkirkby]:
> What do I need to do to test this - **just** download the package - do I need to patch anything else? 
You also need to apply the sagelib and extcode patches from #9343.  Or easier: download [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar), install that and *then* install the new pari spkg.



---

archive/issue_comments_097345.json:
```json
{
    "body": "I have made a few small changes to the pari spkg and put the result at  http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p5.spkg (I kept the p5 version number).",
    "created_at": "2010-09-06T16:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97345",
    "user": "jdemeyer"
}
```

I have made a few small changes to the pari spkg and put the result at  http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p5.spkg (I kept the p5 version number).



---

archive/issue_comments_097346.json:
```json
{
    "body": "Replying to [comment:4 jdemeyer]:\n> Replying to [comment:3 drkirkby]:\n> > What do I need to do to test this - **just** download the package - do I need to patch anything else? \n> You also need to apply the sagelib and extcode patches from #9343.  Or easier: download [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar), install that and *then* install the new pari spkg.\n\nIt would be good if you could make a new tar file with all the changes in place - i.e. make a `sage-4.6.prealpha4.tar`\n\n\n\nDave",
    "created_at": "2010-09-06T16:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97346",
    "user": "drkirkby"
}
```

Replying to [comment:4 jdemeyer]:
> Replying to [comment:3 drkirkby]:
> > What do I need to do to test this - **just** download the package - do I need to patch anything else? 
> You also need to apply the sagelib and extcode patches from #9343.  Or easier: download [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar), install that and *then* install the new pari spkg.

It would be good if you could make a new tar file with all the changes in place - i.e. make a `sage-4.6.prealpha4.tar`



Dave



---

archive/issue_comments_097347.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n> It would be good if you could make a new tar file with all the changes in place - i.e. make a `sage-4.6.prealpha4.tar`\n\nI will now make a new 4.6-prealpha4 based on 4.5.3-rc0 with the new spkgs (I will also update genus2reduction, see #9591 and lcalc, see #9845).",
    "created_at": "2010-09-06T16:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97347",
    "user": "jdemeyer"
}
```

Replying to [comment:7 drkirkby]:
> It would be good if you could make a new tar file with all the changes in place - i.e. make a `sage-4.6.prealpha4.tar`

I will now make a new 4.6-prealpha4 based on 4.5.3-rc0 with the new spkgs (I will also update genus2reduction, see #9591 and lcalc, see #9845).



---

archive/issue_comments_097348.json:
```json
{
    "body": "Attachment [pari.p5.patch](tarball://root/attachments/some-uuid/ticket9860/pari.p5.patch) by jdemeyer created at 2010-09-06 19:32:01\n\nAdditional spkg patches by me",
    "created_at": "2010-09-06T19:32:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97348",
    "user": "jdemeyer"
}
```

Attachment [pari.p5.patch](tarball://root/attachments/some-uuid/ticket9860/pari.p5.patch) by jdemeyer created at 2010-09-06 19:32:01

Additional spkg patches by me



---

archive/issue_comments_097349.json:
```json
{
    "body": "Replying to [comment:6 jdemeyer]:\n> I have made a few small changes to the pari spkg and put the result at  http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p5.spkg (I kept the p5 version number).\n\nI'm ok with your changes (\"positive review\"). Not very surprisingly Sage 4.6.prealpha4 also passed all tests. Tuning on a Core2 worked, too, at least did pass without errors. ;-)\n\nThe way we handle the patches now (without the patched *replacement files* being under revision control) is a bit dangerous though. Perhaps we should also add some script to *generate the patches* from `patches/files/*` and one to just make sure they're in sync.",
    "created_at": "2010-09-07T07:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97349",
    "user": "leif"
}
```

Replying to [comment:6 jdemeyer]:
> I have made a few small changes to the pari spkg and put the result at  http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p5.spkg (I kept the p5 version number).

I'm ok with your changes ("positive review"). Not very surprisingly Sage 4.6.prealpha4 also passed all tests. Tuning on a Core2 worked, too, at least did pass without errors. ;-)

The way we handle the patches now (without the patched *replacement files* being under revision control) is a bit dangerous though. Perhaps we should also add some script to *generate the patches* from `patches/files/*` and one to just make sure they're in sync.



---

archive/issue_comments_097350.json:
```json
{
    "body": "Leif: your patch looks good on visual inspection.  Since it fixes all known build issues, I give it positive review.",
    "created_at": "2010-09-07T10:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97350",
    "user": "jdemeyer"
}
```

Leif: your patch looks good on visual inspection.  Since it fixes all known build issues, I give it positive review.



---

archive/issue_comments_097351.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-07T10:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97351",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097352.json:
```json
{
    "body": "Otherwise looks a bit funny. Thanks though. ;-)\n\nI think we should report some of the changes upstream when our PARI has successfully reached some Sage 4.6.{alpha,rc}.",
    "created_at": "2010-09-07T10:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97352",
    "user": "leif"
}
```

Otherwise looks a bit funny. Thanks though. ;-)

I think we should report some of the changes upstream when our PARI has successfully reached some Sage 4.6.{alpha,rc}.



---

archive/issue_comments_097353.json:
```json
{
    "body": "Replying to [comment:12 leif]:\n> I think we should report some of the changes upstream when our PARI has successfully reached some Sage 4.6.{alpha,rc}.\n\nAgreed.",
    "created_at": "2010-09-07T10:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97353",
    "user": "jdemeyer"
}
```

Replying to [comment:12 leif]:
> I think we should report some of the changes upstream when our PARI has successfully reached some Sage 4.6.{alpha,rc}.

Agreed.



---

archive/issue_comments_097354.json:
```json
{
    "body": "P.S.: Attempting to build with Qt as the graphics back-end is still broken in some constellations (i.e. may lead to build errors, too), since the code apparently expects Qt <= 3 and some (Qt) tools PARI doesn't look for. I haven't yet worked on `config/get_Qt` though.",
    "created_at": "2010-09-07T10:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97354",
    "user": "leif"
}
```

P.S.: Attempting to build with Qt as the graphics back-end is still broken in some constellations (i.e. may lead to build errors, too), since the code apparently expects Qt <= 3 and some (Qt) tools PARI doesn't look for. I haven't yet worked on `config/get_Qt` though.



---

archive/issue_comments_097355.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-10T10:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9859#issuecomment-97355",
    "user": "mpatel"
}
```

Resolution: fixed
