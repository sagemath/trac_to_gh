# Issue 9221: update matplotlib to svn and clean out the patches

archive/issues_009221.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  drkirkby @kcrisman\n\nMatplotlib SVN 8415 has some bugfixes and enhancements that are really nice for us.  For example, the configuration variables allow us to eliminate most of our patches to the spkg, and a new path.snap config parameter solves #7808.\n\nThe spkg is up at http://sage.math.washington.edu/home/jason/matplotlib-0.99.3-svn8415.spkg, and builds on the spkg in #9202.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9221\n\n",
    "created_at": "2010-06-11T21:35:44Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "update matplotlib to svn and clean out the patches",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9221",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  drkirkby @kcrisman

Matplotlib SVN 8415 has some bugfixes and enhancements that are really nice for us.  For example, the configuration variables allow us to eliminate most of our patches to the spkg, and a new path.snap config parameter solves #7808.

The spkg is up at http://sage.math.washington.edu/home/jason/matplotlib-0.99.3-svn8415.spkg, and builds on the spkg in #9202.

Issue created by migration from https://trac.sagemath.org/ticket/9221





---

archive/issue_comments_086276.json:
```json
{
    "body": "The SVN spkg does not compile on Solaris.  See the issues with header files reported at the end of #9202.",
    "created_at": "2010-06-11T21:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86276",
    "user": "https://github.com/jasongrout"
}
```

The SVN spkg does not compile on Solaris.  See the issues with header files reported at the end of #9202.



---

archive/issue_comments_086277.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-11T21:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86277",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_086278.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-06-11T21:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86278",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_086279.json:
```json
{
    "body": "David, can you check to see if this spkg compiles on Solaris, or if we need to still address the issues at the end of #9202?",
    "created_at": "2010-07-07T05:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86279",
    "user": "https://github.com/jasongrout"
}
```

David, can you check to see if this spkg compiles on Solaris, or if we need to still address the issues at the end of #9202?



---

archive/issue_comments_086280.json:
```json
{
    "body": "See what's new at: http://matplotlib.sourceforge.net/users/whats_new.html",
    "created_at": "2010-07-07T05:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86280",
    "user": "https://github.com/jasongrout"
}
```

See what's new at: http://matplotlib.sourceforge.net/users/whats_new.html



---

archive/issue_comments_086281.json:
```json
{
    "body": "This was in the log, so I think this should compile on Solaris now:\n\n\n```\n2010-07-02 Modified CXX/WrapPython.h to fix \"swab bug\" on solaris so\n           mpl can compile on Solaris with CXX6 in the trunk.  Closes\n           tracker bug 3022815 - JDH\n```\n",
    "created_at": "2010-07-07T05:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86281",
    "user": "https://github.com/jasongrout"
}
```

This was in the log, so I think this should compile on Solaris now:


```
2010-07-02 Modified CXX/WrapPython.h to fix "swab bug" on solaris so
           mpl can compile on Solaris with CXX6 in the trunk.  Closes
           tracker bug 3022815 - JDH
```




---

archive/issue_comments_086282.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-07-07T08:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86282",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_086283.json:
```json
{
    "body": "Replying to [comment:6 jason]:\n> This was in the log, so I think this should compile on Solaris now:\n> \n> {{{\n> 2010-07-02 Modified CXX/WrapPython.h to fix \"swab bug\" on solaris so\n>            mpl can compile on Solaris with CXX6 in the trunk.  Closes\n>            tracker bug 3022815 - JDH\n> }}}\n\nNo such luck. I've tried on both Solaris 10 on SPARC, and OpenSolaris on x64. It looks like a mix of compilation modes is causing them to get two different definitions for *swab*. \n\nThe bug tracker suggests this was a very recent fix, so may not have made it into 1.0. If if did make it into 1.0, then it failed to solve the problem. \n\n## Solaris 10 update with Sun UltraSPARC T2+ processors\n\n* Sun T5240\n* 2 x 8 core, 64-thread UltraSPARC T2+ 1167 MHz\n* 32 GB RAM\n* Solaris 10 update 7 (05/09)\n* t2.math.washtington.edu\n* gcc 4.4.1 configured to use both the Sun linker and assembler. \n* A build of sage-4.5.alpha4 was used to test matplotlib-1.0.0.spkg\n* MD5 checksum of matplotlib-1.0.0.spkg was cb9f3cb0ec3da550d2d67ea7e8b6094f \n* 32-bit build (This is the default). The environment variable `SAGE64` was **not** used. \n\n\n```\ngcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -Isrc -Iagg24/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include/freetype2 -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/include/python2.6 -c agg24/src/agg_vcgen_dash.cpp -o build/temp.solaris-2.10-sun4v-2.6/agg24/src/agg_vcgen_dash.o\ncc1plus: warning: command line option \"-Wstrict-prototypes\" is valid for Ada/C/ObjC but not for C++\ngcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -Isrc -Iagg24/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include/freetype2 -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/include/python2.6 -c agg24/src/agg_image_filters.cpp -o build/temp.solaris-2.10-sun4v-2.6/agg24/src/agg_image_filters.o\ncc1plus: warning: command line option \"-Wstrict-prototypes\" is valid for Ada/C/ObjC but not for C++\ngcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -Isrc -Iagg24/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include/freetype2 -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/include/python2.6 -c src/backend_agg.cpp -o build/temp.solaris-2.10-sun4v-2.6/src/backend_agg.o\ncc1plus: warning: command line option \"-Wstrict-prototypes\" is valid for Ada/C/ObjC but not for C++\nIn file included from /tmp/kirkby/sage-4.5.alpha4/local/include/python2.6/Python.h:8,\n                 from ./CXX/WrapPython.h:61,\n                 from ./CXX/Extensions.hxx:37,\n                 from src/ft2font.h:4,\n                 from src/backend_agg.cpp:10:\n/tmp/kirkby/sage-4.5.alpha4/local/include/python2.6/pyconfig.h:1013:1: warning: \"_FILE_OFFSET_BITS\" redefined\nIn file included from /usr/include/sys/types.h:18,\n                 from /tmp/kirkby/sage-4.5.alpha4/local/include/zconf.h:364,\n                 from /tmp/kirkby/sage-4.5.alpha4/local/include/zlib.h:34,\n                 from /tmp/kirkby/sage-4.5.alpha4/local/include/png.h:470,\n                 from src/backend_agg.cpp:3:\n/usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/sys/feature_tests.h:197:1: warning: this is the location of the previous definition\nIn file included from /tmp/kirkby/sage-4.5.alpha4/local/include/python2.6/Python.h:42,\n                 from ./CXX/WrapPython.h:61,\n                 from ./CXX/Extensions.hxx:37,\n                 from src/ft2font.h:4,\n                 from src/backend_agg.cpp:10:\n/usr/include/stdlib.h:144: error: declaration of C function \u2018void swab(const char*, char*, ssize_t)\u2019 conflicts with\n/usr/include/unistd.h:496: error: previous declaration \u2018void swab(const void*, void*, ssize_t)\u2019 here\nerror: command 'gcc' failed with exit status 1\nError building matplotlib package.\n\nreal    3m35.224s\nuser    3m20.924s\nsys     0m9.504s\nsage: An error occurred while installing matplotlib-1.0.0\n```\n\n\n## OpenSolaris 2009.06 on x64 hardware\n\n* Sun Ultra 27 \n* 1 x 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads.\n* 12 GB RAM\n* OpenSolaris 2009.06 snv_134 X86\n* gcc 4.4.4 configured to use the Sun linker and GNU assembler. \n* A build of sage-4.5.alpha4 was used to test matplotlib-1.0.0.spkg\n* 64-bit build. OpenSolaris defaults to 32-bit, but the environment variable `SAGE64=yes` was used.\n* MD5 checksum of matplotlib-1.0.0.spkg was cb9f3cb0ec3da550d2d67ea7e8b6094f\n\n```\ngcc -DNDEBUG -g -O3 -m64 -Wall -Wstrict-prototypes -O2 -g -m64 -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/export/home/drkirkby/sage-4.5.alpha4/local/include -I. -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -Isrc -Iagg24/include -I. -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/export/home/drkirkby/sage-4.5.alpha4/local/include -I. -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include/freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/include/freetype2 -I./freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include/freetype2 -Isrc/freetype2 -Iagg24/include/freetype2 -I./freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include/freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/include/freetype2 -I./freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/include/python2.6 -c src/backend_agg.cpp -o build/temp.solaris-2.11-i86pc-2.6/src/backend_agg.o\ncc1plus: warning: command line option \"-Wstrict-prototypes\" is valid for Ada/C/ObjC but not for C++\nIn file included from /export/home/drkirkby/sage-4.5.alpha4/local/include/python2.6/Python.h:42,\n                 from ./CXX/WrapPython.h:61,\n                 from ./CXX/Extensions.hxx:37,\n                 from src/ft2font.h:4,\n                 from src/backend_agg.cpp:10:\n/usr/include/stdlib.h:159: error: declaration of C function 'void swab(const char*, char*, ssize_t)' conflicts with\n/usr/include/unistd.h:513: error: previous declaration 'void swab(const void*, void*, ssize_t)' here\nsrc/backend_agg.cpp: In member function 'Py::Object RendererAgg::draw_markers(const Py::Tuple&)':\nsrc/backend_agg.cpp:727: warning: dereferencing type-punned pointer will break strict-aliasing rules\nsrc/backend_agg.cpp:727: warning: dereferencing type-punned pointer will break strict-aliasing rules\nsrc/backend_agg.cpp:763: warning: dereferencing type-punned pointer will break strict-aliasing rules\nsrc/backend_agg.cpp:763: warning: dereferencing type-punned pointer will break strict-aliasing rules\nerror: command 'gcc' failed with exit status 1\nError building matplotlib package.\n\nreal\t0m19.778s\nuser\t0m17.826s\nsys\t0m1.441s\nsage: An error occurred while installing matplotlib-1.0.0\n```\n",
    "created_at": "2010-07-07T08:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86283",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:6 jason]:
> This was in the log, so I think this should compile on Solaris now:
> 
> {{{
> 2010-07-02 Modified CXX/WrapPython.h to fix "swab bug" on solaris so
>            mpl can compile on Solaris with CXX6 in the trunk.  Closes
>            tracker bug 3022815 - JDH
> }}}

No such luck. I've tried on both Solaris 10 on SPARC, and OpenSolaris on x64. It looks like a mix of compilation modes is causing them to get two different definitions for *swab*. 

The bug tracker suggests this was a very recent fix, so may not have made it into 1.0. If if did make it into 1.0, then it failed to solve the problem. 

## Solaris 10 update with Sun UltraSPARC T2+ processors

* Sun T5240
* 2 x 8 core, 64-thread UltraSPARC T2+ 1167 MHz
* 32 GB RAM
* Solaris 10 update 7 (05/09)
* t2.math.washtington.edu
* gcc 4.4.1 configured to use both the Sun linker and assembler. 
* A build of sage-4.5.alpha4 was used to test matplotlib-1.0.0.spkg
* MD5 checksum of matplotlib-1.0.0.spkg was cb9f3cb0ec3da550d2d67ea7e8b6094f 
* 32-bit build (This is the default). The environment variable `SAGE64` was **not** used. 


```
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -Isrc -Iagg24/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include/freetype2 -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/include/python2.6 -c agg24/src/agg_vcgen_dash.cpp -o build/temp.solaris-2.10-sun4v-2.6/agg24/src/agg_vcgen_dash.o
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -Isrc -Iagg24/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include/freetype2 -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/include/python2.6 -c agg24/src/agg_image_filters.cpp -o build/temp.solaris-2.10-sun4v-2.6/agg24/src/agg_image_filters.o
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -Isrc -Iagg24/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include/freetype2 -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/include/python2.6 -c src/backend_agg.cpp -o build/temp.solaris-2.10-sun4v-2.6/src/backend_agg.o
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
In file included from /tmp/kirkby/sage-4.5.alpha4/local/include/python2.6/Python.h:8,
                 from ./CXX/WrapPython.h:61,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/backend_agg.cpp:10:
/tmp/kirkby/sage-4.5.alpha4/local/include/python2.6/pyconfig.h:1013:1: warning: "_FILE_OFFSET_BITS" redefined
In file included from /usr/include/sys/types.h:18,
                 from /tmp/kirkby/sage-4.5.alpha4/local/include/zconf.h:364,
                 from /tmp/kirkby/sage-4.5.alpha4/local/include/zlib.h:34,
                 from /tmp/kirkby/sage-4.5.alpha4/local/include/png.h:470,
                 from src/backend_agg.cpp:3:
/usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/sys/feature_tests.h:197:1: warning: this is the location of the previous definition
In file included from /tmp/kirkby/sage-4.5.alpha4/local/include/python2.6/Python.h:42,
                 from ./CXX/WrapPython.h:61,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/backend_agg.cpp:10:
/usr/include/stdlib.h:144: error: declaration of C function ‘void swab(const char*, char*, ssize_t)’ conflicts with
/usr/include/unistd.h:496: error: previous declaration ‘void swab(const void*, void*, ssize_t)’ here
error: command 'gcc' failed with exit status 1
Error building matplotlib package.

real    3m35.224s
user    3m20.924s
sys     0m9.504s
sage: An error occurred while installing matplotlib-1.0.0
```


## OpenSolaris 2009.06 on x64 hardware

* Sun Ultra 27 
* 1 x 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads.
* 12 GB RAM
* OpenSolaris 2009.06 snv_134 X86
* gcc 4.4.4 configured to use the Sun linker and GNU assembler. 
* A build of sage-4.5.alpha4 was used to test matplotlib-1.0.0.spkg
* 64-bit build. OpenSolaris defaults to 32-bit, but the environment variable `SAGE64=yes` was used.
* MD5 checksum of matplotlib-1.0.0.spkg was cb9f3cb0ec3da550d2d67ea7e8b6094f

```
gcc -DNDEBUG -g -O3 -m64 -Wall -Wstrict-prototypes -O2 -g -m64 -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/export/home/drkirkby/sage-4.5.alpha4/local/include -I. -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -Isrc -Iagg24/include -I. -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/export/home/drkirkby/sage-4.5.alpha4/local/include -I. -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include/freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/include/freetype2 -I./freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include/freetype2 -Isrc/freetype2 -Iagg24/include/freetype2 -I./freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include/freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/include/freetype2 -I./freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/include/python2.6 -c src/backend_agg.cpp -o build/temp.solaris-2.11-i86pc-2.6/src/backend_agg.o
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
In file included from /export/home/drkirkby/sage-4.5.alpha4/local/include/python2.6/Python.h:42,
                 from ./CXX/WrapPython.h:61,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/backend_agg.cpp:10:
/usr/include/stdlib.h:159: error: declaration of C function 'void swab(const char*, char*, ssize_t)' conflicts with
/usr/include/unistd.h:513: error: previous declaration 'void swab(const void*, void*, ssize_t)' here
src/backend_agg.cpp: In member function 'Py::Object RendererAgg::draw_markers(const Py::Tuple&)':
src/backend_agg.cpp:727: warning: dereferencing type-punned pointer will break strict-aliasing rules
src/backend_agg.cpp:727: warning: dereferencing type-punned pointer will break strict-aliasing rules
src/backend_agg.cpp:763: warning: dereferencing type-punned pointer will break strict-aliasing rules
src/backend_agg.cpp:763: warning: dereferencing type-punned pointer will break strict-aliasing rules
error: command 'gcc' failed with exit status 1
Error building matplotlib package.

real	0m19.778s
user	0m17.826s
sys	0m1.441s
sage: An error occurred while installing matplotlib-1.0.0
```




---

archive/issue_comments_086284.json:
```json
{
    "body": "Well, the log I posted was from the changelog for 1.0.0, so it certainly look like the fix had made it in.  I'll try looking at this soon.\n\nAlso, the spkg I posted above needs:\n\n* an updated SPKG.txt file\n* long doctests run\n\nbefore it is officially ready for review.",
    "created_at": "2010-07-07T14:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86284",
    "user": "https://github.com/jasongrout"
}
```

Well, the log I posted was from the changelog for 1.0.0, so it certainly look like the fix had made it in.  I'll try looking at this soon.

Also, the spkg I posted above needs:

* an updated SPKG.txt file
* long doctests run

before it is officially ready for review.



---

archive/issue_comments_086285.json:
```json
{
    "body": "David,\n\nI verified that the md5 you reported is for the right spkg and contains the fix.  If you have time, could you download the vanilla matplotlib source and try compiling that, just to make sure it isn't a problem with the Sage environment?  The 1.0.0 source is here:\n\nhttps://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.0/  (I can't test this URL; it isn't loading for me...)\n\nThe installation instructions are here:\n\nhttp://matplotlib.sourceforge.net/users/installing.html\n\nand basically are:\n\n\n```\ncd matplotlib\npython setup.py build\npython setup.py install\n```\n\n\nI've also posted a report to https://sourceforge.net/mailarchive/forum.php?thread_name=4C349BDE.4020604%40creativetrax.com&forum_name=matplotlib-devel",
    "created_at": "2010-07-07T15:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86285",
    "user": "https://github.com/jasongrout"
}
```

David,

I verified that the md5 you reported is for the right spkg and contains the fix.  If you have time, could you download the vanilla matplotlib source and try compiling that, just to make sure it isn't a problem with the Sage environment?  The 1.0.0 source is here:

https://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.0/  (I can't test this URL; it isn't loading for me...)

The installation instructions are here:

http://matplotlib.sourceforge.net/users/installing.html

and basically are:


```
cd matplotlib
python setup.py build
python setup.py install
```


I've also posted a report to https://sourceforge.net/mailarchive/forum.php?thread_name=4C349BDE.4020604%40creativetrax.com&forum_name=matplotlib-devel



---

archive/issue_comments_086286.json:
```json
{
    "body": "The patch at #9211 (correcting behavior where vertices in graphs are clipped) depends on this spkg.",
    "created_at": "2010-07-18T06:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86286",
    "user": "https://github.com/jasongrout"
}
```

The patch at #9211 (correcting behavior where vertices in graphs are clipped) depends on this spkg.



---

archive/issue_comments_086287.json:
```json
{
    "body": "The patch needs to be applied so that axes labels come out okay.  Compare the results of\n\nplot(x, (x,-3,3), axes_labels=['x','y'])\n\nbefore and after to check this.",
    "created_at": "2010-08-13T17:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86287",
    "user": "https://github.com/jasongrout"
}
```

The patch needs to be applied so that axes labels come out okay.  Compare the results of

plot(x, (x,-3,3), axes_labels=['x','y'])

before and after to check this.



---

archive/issue_comments_086288.json:
```json
{
    "body": "David,\n\nCould you test compiling the vanilla matplotlib 1.0 source on solaris to see if the issue is in the vanilla upstream package?\n\nJust download from http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.0/matplotlib-1.0.0.tar.gz/download\n\nThen untar and do:\n\n\n```\ncd matplotlib\npython setup.py build\npython setup.py install\n```\n\n\n(or use `sage -python` if you want to install into a Sage version of python).",
    "created_at": "2010-08-14T05:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86288",
    "user": "https://github.com/jasongrout"
}
```

David,

Could you test compiling the vanilla matplotlib 1.0 source on solaris to see if the issue is in the vanilla upstream package?

Just download from http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.0/matplotlib-1.0.0.tar.gz/download

Then untar and do:


```
cd matplotlib
python setup.py build
python setup.py install
```


(or use `sage -python` if you want to install into a Sage version of python).



---

archive/issue_comments_086289.json:
```json
{
    "body": "For reference, here is the mailing list post where John Hunter discusses the fix that he hoped fixed the bug:  http://www.mail-archive.com/matplotlib-users`@`lists.sourceforge.net/msg17531.html",
    "created_at": "2010-08-14T05:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86289",
    "user": "https://github.com/jasongrout"
}
```

For reference, here is the mailing list post where John Hunter discusses the fix that he hoped fixed the bug:  http://www.mail-archive.com/matplotlib-users`@`lists.sourceforge.net/msg17531.html



---

archive/issue_comments_086290.json:
```json
{
    "body": "It's not so easy to test the upstream source code directly, as there are dependencies which are not provided on Solaris. On 't2.math' I get:\n\n\n```\nkirkby@t2:32 ~/matplotlib-1.0.0$ python setup.py build\nbasedirlist is: ['/usr/local']\n============================================================================\nBUILDING MATPLOTLIB\n            matplotlib: 1.0.0\n                python: 2.4.4 (#1, Jan 10 2007, 01:25:01) [C]\n              platform: sunos5\n\nREQUIRED DEPENDENCIES\n                 numpy: no\n                        * You must install numpy 1.1 or later to build\n                        * matplotlib.\n```\n\n\nBut Numpy has a whole list of dependencies of its own, so I don't want to spend a long time setting that lot up. \n\nBut I just retried your .spkg on 't2' using a working copy of the latest `sage-4.5.3.alpha0` and find exactly the same problem. \n\nI also tried on my OpenSolaris machine inside a slightly modified version of `sage-4.5.3.alpha0`. Again, I get the same problem as before. \n\nTo me this looks like an upstream bug, and not anything introduced in Sage. \n\nI just checked the source code, and see the code is actually in matplotlib-1.0.0. \n\n\n```\n// Prevent multiple conflicting definitions of swab from stdlib.h and unistd.h\n#if defined(__sun) || defined(sun)\n#if defined(_XPG4)\n#undef _XPG4\n#endif\n#if defined(_XPG3)\n#undef _XPG3\n#endif\n#endif\n```\n\n\nIt seems a bit of a hack to me. If `_XPG4` or `_XPG3` are defined, there were defined for good reason, and I doubt simply undefining them is the right way to tackle this. I could imagine this could cause a whole lot more problems than it solves. \n\nAccording to http://en.wikipedia.org/wiki/X/Open the [Single UNIX Specification](http://en.wikipedia.org/wiki/Single_UNIX_Specification) was based on the XPG4 standard, so I would not be surprised that undefining `_XPG4` will cause problems as the behavior of hundreds of header files will be changed.",
    "created_at": "2010-08-14T07:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86290",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It's not so easy to test the upstream source code directly, as there are dependencies which are not provided on Solaris. On 't2.math' I get:


```
kirkby@t2:32 ~/matplotlib-1.0.0$ python setup.py build
basedirlist is: ['/usr/local']
============================================================================
BUILDING MATPLOTLIB
            matplotlib: 1.0.0
                python: 2.4.4 (#1, Jan 10 2007, 01:25:01) [C]
              platform: sunos5

REQUIRED DEPENDENCIES
                 numpy: no
                        * You must install numpy 1.1 or later to build
                        * matplotlib.
```


But Numpy has a whole list of dependencies of its own, so I don't want to spend a long time setting that lot up. 

But I just retried your .spkg on 't2' using a working copy of the latest `sage-4.5.3.alpha0` and find exactly the same problem. 

I also tried on my OpenSolaris machine inside a slightly modified version of `sage-4.5.3.alpha0`. Again, I get the same problem as before. 

To me this looks like an upstream bug, and not anything introduced in Sage. 

I just checked the source code, and see the code is actually in matplotlib-1.0.0. 


```
// Prevent multiple conflicting definitions of swab from stdlib.h and unistd.h
#if defined(__sun) || defined(sun)
#if defined(_XPG4)
#undef _XPG4
#endif
#if defined(_XPG3)
#undef _XPG3
#endif
#endif
```


It seems a bit of a hack to me. If `_XPG4` or `_XPG3` are defined, there were defined for good reason, and I doubt simply undefining them is the right way to tackle this. I could imagine this could cause a whole lot more problems than it solves. 

According to http://en.wikipedia.org/wiki/X/Open the [Single UNIX Specification](http://en.wikipedia.org/wiki/Single_UNIX_Specification) was based on the XPG4 standard, so I would not be surprised that undefining `_XPG4` will cause problems as the behavior of hundreds of header files will be changed.



---

archive/issue_comments_086291.json:
```json
{
    "body": "BTW, it perfectly possible on Solaris to have both `stdlib.h` and `unistd.h` included in the one source file - here's a \"hello world\" that does just that. \n\n\n```\ndrkirkby@hawk:~$ cat test.c\n#include <stdio.h>\n#include <unistd.h>\n#include <stdlib.h>\n\nint main() {\n   printf(\"Hello world\\n\");\n   exit(0);\n}\n\ndrkirkby@hawk:~$ gcc -Wall test.c\ndrkirkby@hawk:~$ ./a.out\nHello world\n```\n",
    "created_at": "2010-08-14T08:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86291",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

BTW, it perfectly possible on Solaris to have both `stdlib.h` and `unistd.h` included in the one source file - here's a "hello world" that does just that. 


```
drkirkby@hawk:~$ cat test.c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main() {
   printf("Hello world\n");
   exit(0);
}

drkirkby@hawk:~$ gcc -Wall test.c
drkirkby@hawk:~$ ./a.out
Hello world
```




---

archive/issue_comments_086292.json:
```json
{
    "body": "Attachment [trac-9221-matplotlib-update.patch](tarball://root/attachments/some-uuid/ticket9221/trac-9221-matplotlib-update.patch) by @jasongrout created at 2010-08-14 16:00:05\n\nWith the patch, all doctests in plot/*.py pass with matplotlib 1.0.",
    "created_at": "2010-08-14T16:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86292",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9221-matplotlib-update.patch](tarball://root/attachments/some-uuid/ticket9221/trac-9221-matplotlib-update.patch) by @jasongrout created at 2010-08-14 16:00:05

With the patch, all doctests in plot/*.py pass with matplotlib 1.0.



---

archive/issue_comments_086293.json:
```json
{
    "body": "Replying to [comment:16 drkirkby]:\n> BTW, it perfectly possible on Solaris to have both `stdlib.h` and `unistd.h` included in the one source file - here's a \"hello world\" that does just that. \n> \n> {{{\n> drkirkby`@`hawk:~$ cat test.c\n> #include <stdio.h>\n> #include <unistd.h>\n> #include <stdlib.h>\n> \n> int main() {\n>    printf(\"Hello world\\n\");\n>    exit(0);\n> }\n> \n> drkirkby`@`hawk:~$ gcc -Wall test.c\n> drkirkby`@`hawk:~$ ./a.out\n> Hello world\n> }}}\n\n\nInteresting.  In this case, it seems like they want to include Python.h.\n\nBy default, which of _XPG4 or _XPG3 is defined in your compiler?  From the code in stdlib.h, it looks like setting _XPG4, but undefining _XPG3, should work.",
    "created_at": "2010-08-14T16:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86293",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:16 drkirkby]:
> BTW, it perfectly possible on Solaris to have both `stdlib.h` and `unistd.h` included in the one source file - here's a "hello world" that does just that. 
> 
> {{{
> drkirkby`@`hawk:~$ cat test.c
> #include <stdio.h>
> #include <unistd.h>
> #include <stdlib.h>
> 
> int main() {
>    printf("Hello world\n");
>    exit(0);
> }
> 
> drkirkby`@`hawk:~$ gcc -Wall test.c
> drkirkby`@`hawk:~$ ./a.out
> Hello world
> }}}


Interesting.  In this case, it seems like they want to include Python.h.

By default, which of _XPG4 or _XPG3 is defined in your compiler?  From the code in stdlib.h, it looks like setting _XPG4, but undefining _XPG3, should work.



---

archive/issue_comments_086294.json:
```json
{
    "body": "Replying to [comment:18 jason]:\n> Replying to [comment:16 drkirkby]:\n> > BTW, it perfectly possible on Solaris to have both `stdlib.h` and `unistd.h` included in the one source file - here's a \"hello world\" that does just that. \n> > \n> > {{{\n> > drkirkby`@`hawk:~$ cat test.c\n> > #include <stdio.h>\n> > #include <unistd.h>\n> > #include <stdlib.h>\n> > \n> > int main() {\n> >    printf(\"Hello world\\n\");\n> >    exit(0);\n> > }\n> > \n> > drkirkby`@`hawk:~$ gcc -Wall test.c\n> > drkirkby`@`hawk:~$ ./a.out\n> > Hello world\n> > }}}\n> \n> \n> Interesting.  In this case, it seems like they want to include Python.h.\n\nI've no idea. \n\n> By default, which of _XPG4 or _XPG3 is defined in your compiler?  \n\nNeither of them. \n\nOne can see what gets defined with any combination of C and header files by pre-processing a file, and using the -dM options. To get the defaults, just use an empty file or /dev/null. This is a very useful trick some times. \n\n\n```\ndrkirkby@laptop:~$ gcc -dM -E - </dev/null  \n#define __DBL_MIN_EXP__ (-1021)\n#define __FLT_MIN__ 1.17549435e-38F\n#define __CHAR_BIT__ 8\n#define __WCHAR_MAX__ 2147483647\n#define __DBL_DENORM_MIN__ 4.9406564584124654e-324\n#define __FLT_EVAL_METHOD__ 2\n\netc etc\n```\n\n\nFor the case of a test file where both unistd.h and stdlib.h are defined, we see both `_XOPEN_XPG3` and `_XOPEN_XPG4` get defined, but not `_XPG3` or `_XPG4`. \n\n\n```\ndrkirkby@laptop:~$ gcc -dM -E  test.c | grep XPG\n#define _XOPEN_XPG3 \n#define _XOPEN_XPG4 \n```\n\n\n> From the code in stdlib.h, it looks like setting _XPG4, but undefining _XPG3, should work.\n\nI don't think one should go defining `_XPG3` and `_XPG4`  directly, but if one does do that, then one can induce the error depending on what you define and what header files you include. I leave it for you to prove that to yourself. (Try it on 't2.math') \n\nI can suggest a few resources that might shed some light on it. \n\n* http://www.opengroup.org/forums/\n* gcc-help mailing list. (The mainly Linux crowd are bound to blame Sun, but worth asking anyway.)\n* comp.unix.solaris newsgroup http://groups.google.com/group/comp.unix.solaris\n* comp.lang.c newsgroup http://groups.google.co.uk/group/comp.lang.c \n\nThere's probably a few more. Sorry I don't know the answer, but I doubt it needs on to go around defining `_XPG4` or similar. \n\n\nDave",
    "created_at": "2010-08-14T17:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86294",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:18 jason]:
> Replying to [comment:16 drkirkby]:
> > BTW, it perfectly possible on Solaris to have both `stdlib.h` and `unistd.h` included in the one source file - here's a "hello world" that does just that. 
> > 
> > {{{
> > drkirkby`@`hawk:~$ cat test.c
> > #include <stdio.h>
> > #include <unistd.h>
> > #include <stdlib.h>
> > 
> > int main() {
> >    printf("Hello world\n");
> >    exit(0);
> > }
> > 
> > drkirkby`@`hawk:~$ gcc -Wall test.c
> > drkirkby`@`hawk:~$ ./a.out
> > Hello world
> > }}}
> 
> 
> Interesting.  In this case, it seems like they want to include Python.h.

I've no idea. 

> By default, which of _XPG4 or _XPG3 is defined in your compiler?  

Neither of them. 

One can see what gets defined with any combination of C and header files by pre-processing a file, and using the -dM options. To get the defaults, just use an empty file or /dev/null. This is a very useful trick some times. 


```
drkirkby@laptop:~$ gcc -dM -E - </dev/null  
#define __DBL_MIN_EXP__ (-1021)
#define __FLT_MIN__ 1.17549435e-38F
#define __CHAR_BIT__ 8
#define __WCHAR_MAX__ 2147483647
#define __DBL_DENORM_MIN__ 4.9406564584124654e-324
#define __FLT_EVAL_METHOD__ 2

etc etc
```


For the case of a test file where both unistd.h and stdlib.h are defined, we see both `_XOPEN_XPG3` and `_XOPEN_XPG4` get defined, but not `_XPG3` or `_XPG4`. 


```
drkirkby@laptop:~$ gcc -dM -E  test.c | grep XPG
#define _XOPEN_XPG3 
#define _XOPEN_XPG4 
```


> From the code in stdlib.h, it looks like setting _XPG4, but undefining _XPG3, should work.

I don't think one should go defining `_XPG3` and `_XPG4`  directly, but if one does do that, then one can induce the error depending on what you define and what header files you include. I leave it for you to prove that to yourself. (Try it on 't2.math') 

I can suggest a few resources that might shed some light on it. 

* http://www.opengroup.org/forums/
* gcc-help mailing list. (The mainly Linux crowd are bound to blame Sun, but worth asking anyway.)
* comp.unix.solaris newsgroup http://groups.google.com/group/comp.unix.solaris
* comp.lang.c newsgroup http://groups.google.co.uk/group/comp.lang.c 

There's probably a few more. Sorry I don't know the answer, but I doubt it needs on to go around defining `_XPG4` or similar. 


Dave



---

archive/issue_comments_086295.json:
```json
{
    "body": "I'm attaching the standards(1) man page from an OpenSolaris machine. This gives some information on this matter. I've also asked on the newsgroup [solaris.unix.solaris](http://groups.google.com/group/comp.unix.solaris/browse_thread/thread/2f10c2308c0b533d?hl=en#) about this issue.",
    "created_at": "2010-08-24T19:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86295",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm attaching the standards(1) man page from an OpenSolaris machine. This gives some information on this matter. I've also asked on the newsgroup [solaris.unix.solaris](http://groups.google.com/group/comp.unix.solaris/browse_thread/thread/2f10c2308c0b533d?hl=en#) about this issue.



---

archive/issue_comments_086296.json:
```json
{
    "body": "Oops, the standards's man page is in section 5, not 1.",
    "created_at": "2010-08-24T19:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86296",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Oops, the standards's man page is in section 5, not 1.



---

archive/issue_comments_086297.json:
```json
{
    "body": "Can I get an account on a Solaris box and instructions for reproducing this problem?  This is getting hard to debug without access to the hardware.",
    "created_at": "2010-09-07T02:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86297",
    "user": "https://github.com/jasongrout"
}
```

Can I get an account on a Solaris box and instructions for reproducing this problem?  This is getting hard to debug without access to the hardware.



---

archive/issue_comments_086298.json:
```json
{
    "body": "Replying to [comment:22 jason]:\n> Can I get an account on a Solaris box and instructions for reproducing this problem?  This is getting hard to debug without access to the hardware.\n\nAsk William - he can give you an account on t2.math, which is a Solaris 10 SPARC system. \n\nDave",
    "created_at": "2010-09-08T16:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86298",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:22 jason]:
> Can I get an account on a Solaris box and instructions for reproducing this problem?  This is getting hard to debug without access to the hardware.

Ask William - he can give you an account on t2.math, which is a Solaris 10 SPARC system. 

Dave



---

archive/issue_comments_086299.json:
```json
{
    "body": "I'm trying it out on t2 right now.  I logged into t2, extracted {{{/usr/local/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS.tar.gz}} to /scratch/grout, and then tried (as a control) to install the current matplotlib spkg:\n\n\n```\n./sage -f spkg/standard/matplotlib-0.99.3.spkg\n```\n\n\ngave errors like these:\n\n\n```\n\nbuilding 'matplotlib.ft2font' extension\ncreating build/temp.solaris-2.10-sun4v-2.6\ncreating build/temp.solaris-2.10-sun4v-2.6/src\ncreating build/temp.solaris-2.10-sun4v-2.6/CXX\ngcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -I/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/python2.6/site-packages/numpy/core/include -I/export/home/drkirkby/sage-4.5.1/local/include/freetype2 -I/export/home/drkirkby/sage-4.5.1/local/include -I/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/include/ -I/usr/local/include -I. -I/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/include/python2.6 -c src/ft2font.cpp -o build/temp.solaris-2.10-sun4v-2.6/src/ft2font.o\ncc1plus: warning: command line option \"-Wstrict-prototypes\" is valid for Ada/C/ObjC but not for C++\nIn file included from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/ext/hash_map:59,\n                 from ./CXX/Extensions.hxx:68,\n                 from src/ft2font.h:4,\n                 from src/ft2font.cpp:1:\n/usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/backward/backward_warning.h:28:2: warning: #warning This file includes at least one deprecated or antiquated header which may be removed without further notice at a future date. Please use a non-deprecated interface with equivalent functionality instead. For a listing of replacement headers and interfaces, consult the file backward_warning.h. To disable this warning use -Wno-deprecated.\nIn file included from src/ft2font.h:13,\n                 from src/ft2font.cpp:1:\n/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/include/ft2build.h:56:38: error: freetype/config/ftheader.h: No such file or directory\nIn file included from src/ft2font.cpp:1:\nsrc/ft2font.h:14:10: error: #include expects \"FILENAME\" or <FILENAME>\nsrc/ft2font.h:15:10: error: #include expects \"FILENAME\" or <FILENAME>\nsrc/ft2font.h:16:10: error: #include expects \"FILENAME\" or <FILENAME>\nsrc/ft2font.h:17:10: error: #include expects \"FILENAME\" or <FILENAME>\nsrc/ft2font.h:18:10: error: #include expects \"FILENAME\" or <FILENAME>\nIn file included from src/ft2font.cpp:1:\nsrc/ft2font.h:31: error: \u2018FT_Bitmap\u2019 has not been declared\nsrc/ft2font.h:31: error: \u2018FT_Int\u2019 has not been declared\nsrc/ft2font.h:31: error: \u2018FT_Int\u2019 has not been declared\nsrc/ft2font.h:77: error: ISO C++ forbids declaration of \u2018FT_Face\u2019 with no type\nsrc/ft2font.h:77: error: expected \u2018,\u2019 or \u2018...\u2019 before \u2018&\u2019 token\nsrc/ft2font.h:83: error: ISO C++ forbids declaration of \u2018FT_Face\u2019 with no type\nsrc/ft2font.h:83: error: expected \u2018,\u2019 or \u2018...\u2019 before \u2018&\u2019 token\nsrc/ft2font.h:122: error: \u2018FT_Face\u2019 does not name a type\nsrc/ft2font.h:123: error: \u2018FT_Matrix\u2019 does not name a type\nsrc/ft2font.h:124: error: \u2018FT_Vector\u2019 does not name a type\nsrc/ft2font.h:125: error: \u2018FT_Error\u2019 does not name a type\nsrc/ft2font.h:126: error: \u2018FT_Glyph\u2019 was not declared in this scope\nsrc/ft2font.h:126: error: template argument 1 is invalid\nsrc/ft2font.h:126: error: template argument 2 is invalid\nsrc/ft2font.h:127: error: \u2018FT_Vector\u2019 was not declared in this scope\nsrc/ft2font.h:127: error: template argument 1 is invalid\nsrc/ft2font.h:127: error: template argument 2 is invalid\nsrc/ft2font.h:133: error: \u2018FT_BBox\u2019 does not name a type\nsrc/ft2font.cpp:45: error: \u2018FT_Library\u2019 does not name a type\nsrc/ft2font.cpp:96: error: variable or field \u2018draw_bitmap\u2019 declared void\nsrc/ft2font.cpp:96: error: \u2018FT_Bitmap\u2019 was not declared in this scope\nsrc/ft2font.cpp:96: error: \u2018bitmap\u2019 was not declared in this scope\nsrc/ft2font.cpp:97: error: \u2018FT_Int\u2019 was not declared in this scope\nsrc/ft2font.cpp:98: error: \u2018FT_Int\u2019 was not declared in this scope\n/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/python2.6/site-packages/numpy/core/include/numpy/__multiarray_api.h:968: warning: \u2018int _import_array()\u2019 defined but not used\nerror: command 'gcc' failed with exit status 1\nError building matplotlib package.\n\n```\n\n\nDo you know how I can get up to at least installing the current matplotlib spkg on t2?  When I tried my updated 1.0 spkg, I also got these errors.",
    "created_at": "2010-09-09T18:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86299",
    "user": "https://github.com/jasongrout"
}
```

I'm trying it out on t2 right now.  I logged into t2, extracted {{{/usr/local/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS.tar.gz}} to /scratch/grout, and then tried (as a control) to install the current matplotlib spkg:


```
./sage -f spkg/standard/matplotlib-0.99.3.spkg
```


gave errors like these:


```

building 'matplotlib.ft2font' extension
creating build/temp.solaris-2.10-sun4v-2.6
creating build/temp.solaris-2.10-sun4v-2.6/src
creating build/temp.solaris-2.10-sun4v-2.6/CXX
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -I/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/python2.6/site-packages/numpy/core/include -I/export/home/drkirkby/sage-4.5.1/local/include/freetype2 -I/export/home/drkirkby/sage-4.5.1/local/include -I/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/include/ -I/usr/local/include -I. -I/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/include/python2.6 -c src/ft2font.cpp -o build/temp.solaris-2.10-sun4v-2.6/src/ft2font.o
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
In file included from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/ext/hash_map:59,
                 from ./CXX/Extensions.hxx:68,
                 from src/ft2font.h:4,
                 from src/ft2font.cpp:1:
/usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/backward/backward_warning.h:28:2: warning: #warning This file includes at least one deprecated or antiquated header which may be removed without further notice at a future date. Please use a non-deprecated interface with equivalent functionality instead. For a listing of replacement headers and interfaces, consult the file backward_warning.h. To disable this warning use -Wno-deprecated.
In file included from src/ft2font.h:13,
                 from src/ft2font.cpp:1:
/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/include/ft2build.h:56:38: error: freetype/config/ftheader.h: No such file or directory
In file included from src/ft2font.cpp:1:
src/ft2font.h:14:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:15:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:16:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:17:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:18:10: error: #include expects "FILENAME" or <FILENAME>
In file included from src/ft2font.cpp:1:
src/ft2font.h:31: error: ‘FT_Bitmap’ has not been declared
src/ft2font.h:31: error: ‘FT_Int’ has not been declared
src/ft2font.h:31: error: ‘FT_Int’ has not been declared
src/ft2font.h:77: error: ISO C++ forbids declaration of ‘FT_Face’ with no type
src/ft2font.h:77: error: expected ‘,’ or ‘...’ before ‘&’ token
src/ft2font.h:83: error: ISO C++ forbids declaration of ‘FT_Face’ with no type
src/ft2font.h:83: error: expected ‘,’ or ‘...’ before ‘&’ token
src/ft2font.h:122: error: ‘FT_Face’ does not name a type
src/ft2font.h:123: error: ‘FT_Matrix’ does not name a type
src/ft2font.h:124: error: ‘FT_Vector’ does not name a type
src/ft2font.h:125: error: ‘FT_Error’ does not name a type
src/ft2font.h:126: error: ‘FT_Glyph’ was not declared in this scope
src/ft2font.h:126: error: template argument 1 is invalid
src/ft2font.h:126: error: template argument 2 is invalid
src/ft2font.h:127: error: ‘FT_Vector’ was not declared in this scope
src/ft2font.h:127: error: template argument 1 is invalid
src/ft2font.h:127: error: template argument 2 is invalid
src/ft2font.h:133: error: ‘FT_BBox’ does not name a type
src/ft2font.cpp:45: error: ‘FT_Library’ does not name a type
src/ft2font.cpp:96: error: variable or field ‘draw_bitmap’ declared void
src/ft2font.cpp:96: error: ‘FT_Bitmap’ was not declared in this scope
src/ft2font.cpp:96: error: ‘bitmap’ was not declared in this scope
src/ft2font.cpp:97: error: ‘FT_Int’ was not declared in this scope
src/ft2font.cpp:98: error: ‘FT_Int’ was not declared in this scope
/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/python2.6/site-packages/numpy/core/include/numpy/__multiarray_api.h:968: warning: ‘int _import_array()’ defined but not used
error: command 'gcc' failed with exit status 1
Error building matplotlib package.

```


Do you know how I can get up to at least installing the current matplotlib spkg on t2?  When I tried my updated 1.0 spkg, I also got these errors.



---

archive/issue_comments_086300.json:
```json
{
    "body": "FYI, I did do the recommended `. /usr/local/gcc-4.4.1-sun-linker/gcc441sun` first.",
    "created_at": "2010-09-09T18:24:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86300",
    "user": "https://github.com/jasongrout"
}
```

FYI, I did do the recommended `. /usr/local/gcc-4.4.1-sun-linker/gcc441sun` first.



---

archive/issue_comments_086301.json:
```json
{
    "body": "It appears that the problem is in sage-location.  Note that the local/lib/pkgconfig/freetype2.pc file is\n\n```\nprefix=/export/home/drkirkby/sage-4.5.1/local\nexec_prefix=${prefix}\nlibdir=${exec_prefix}/lib\nincludedir=${prefix}/include\n\nName: FreeType 2\nDescription: A free, high-quality, and portable font engine.\nVersion: 9.16.3\nRequires:\nLibs: -L${libdir} -lfreetype -lz \nCflags: -I${includedir}/freetype2 -I${includedir}\n```\n\n\nwhich means it points to totally the wrong place once Sage is moved.  This should be fixed over on #9210.",
    "created_at": "2010-09-09T19:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86301",
    "user": "https://github.com/jasongrout"
}
```

It appears that the problem is in sage-location.  Note that the local/lib/pkgconfig/freetype2.pc file is

```
prefix=/export/home/drkirkby/sage-4.5.1/local
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include

Name: FreeType 2
Description: A free, high-quality, and portable font engine.
Version: 9.16.3
Requires:
Libs: -L${libdir} -lfreetype -lz 
Cflags: -I${includedir}/freetype2 -I${includedir}
```


which means it points to totally the wrong place once Sage is moved.  This should be fixed over on #9210.



---

archive/issue_comments_086302.json:
```json
{
    "body": "Jason,\n\nI have no idea why this did not work for you. That binary was not built on 't2' but on another machine, with the expectation it would work on any SPARC. However, I am aware moving Sage does not always work. \n\nI can only suggest you build the latest Sage from source. Just remember to set something like\n\n\n```\nexport SAGE_PARALLEL_SPKG_BUILD=yes\nexport MAKE=\"make -j8\"\n```\n\n\notherwise it will take ages to build. \n\nDave",
    "created_at": "2010-09-09T19:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86302",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Jason,

I have no idea why this did not work for you. That binary was not built on 't2' but on another machine, with the expectation it would work on any SPARC. However, I am aware moving Sage does not always work. 

I can only suggest you build the latest Sage from source. Just remember to set something like


```
export SAGE_PARALLEL_SPKG_BUILD=yes
export MAKE="make -j8"
```


otherwise it will take ages to build. 

Dave



---

archive/issue_comments_086303.json:
```json
{
    "body": "BTW, there's a binary at \n\n\n```\n/scratch/sage-4.5.3.rc0-binary.tar\n```\n\n\nyou could try extracting that. \n\nBut again, it has been moved, though in that case the binary was built on t2.math. \n\nDave",
    "created_at": "2010-09-09T19:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86303",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

BTW, there's a binary at 


```
/scratch/sage-4.5.3.rc0-binary.tar
```


you could try extracting that. 

But again, it has been moved, though in that case the binary was built on t2.math. 

Dave



---

archive/issue_comments_086304.json:
```json
{
    "body": "Replying to [comment:27 drkirkby]:\n> Jason,\n> \n> I have no idea why this did not work for you. That binary was not built on 't2' but on another machine, with the expectation it would work on any SPARC. However, I am aware moving Sage does not always work. \n> \n> I can only suggest you build the latest Sage from source. Just remember to set something like\n> \n> {{{\n> export SAGE_PARALLEL_SPKG_BUILD=yes\n> export MAKE=\"make -j8\"\n> }}}\n> \n> otherwise it will take ages to build. \n> \n\nThanks; I'll do that.  I'm 99% sure my problem is caused by a Sage directory move.",
    "created_at": "2010-09-09T20:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86304",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:27 drkirkby]:
> Jason,
> 
> I have no idea why this did not work for you. That binary was not built on 't2' but on another machine, with the expectation it would work on any SPARC. However, I am aware moving Sage does not always work. 
> 
> I can only suggest you build the latest Sage from source. Just remember to set something like
> 
> {{{
> export SAGE_PARALLEL_SPKG_BUILD=yes
> export MAKE="make -j8"
> }}}
> 
> otherwise it will take ages to build. 
> 

Thanks; I'll do that.  I'm 99% sure my problem is caused by a Sage directory move.



---

archive/issue_comments_086305.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-16T18:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86305",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086306.json:
```json
{
    "body": "Okay, I've updated the spkg so that it works on t2 (and passes all matplotlib tests):\n\nhttp://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg\n\nCan people try it?  Basically, I just deleted in CXX/WrapPython.h any fudging with the defines, based on drkirkby's idea above that it ought not have to do that.  The new WrapPython.h is:\n\n\n```\n#ifndef __PyCXX_wrap_python_hxx__\n#define __PyCXX_wrap_python_hxx__\n\n// On some platforms we have to include time.h to get select defined\n#if !defined(__WIN32__) && !defined(WIN32) && !defined(_WIN32) && !defined(_WIN64)\n#include <sys/time.h>\n#endif\n\n// pull in python definitions\n#include <Python.h>\n\n#endif\n```\n\n\nHere it passes the matplotlib test suite:\n\n\n```\nIn [1]: import matplotlib\nIn [2]: matplotlib.__version__\nOut[2]: '1.0.0'\n\nIn [3]: matplotlib.test()\n/scratch/grout/sage-4.5.3/local/lib/python2.6/site-packages/matplotlib/axes.py:2369: UserWarning: Attempting to set identical left==right results\nin singular transformations; automatically expanding.\nleft=730139.0, right=730139.0\n  + 'left=%s, right=%s') % (left, right))\n----------------------------------------------------------------------\nRan 138 tests in 755.419s\n\nOK (KNOWNFAIL=42)\nOut[3]: True\n```\n",
    "created_at": "2010-09-16T18:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86306",
    "user": "https://github.com/jasongrout"
}
```

Okay, I've updated the spkg so that it works on t2 (and passes all matplotlib tests):

http://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg

Can people try it?  Basically, I just deleted in CXX/WrapPython.h any fudging with the defines, based on drkirkby's idea above that it ought not have to do that.  The new WrapPython.h is:


```
#ifndef __PyCXX_wrap_python_hxx__
#define __PyCXX_wrap_python_hxx__

// On some platforms we have to include time.h to get select defined
#if !defined(__WIN32__) && !defined(WIN32) && !defined(_WIN32) && !defined(_WIN64)
#include <sys/time.h>
#endif

// pull in python definitions
#include <Python.h>

#endif
```


Here it passes the matplotlib test suite:


```
In [1]: import matplotlib
In [2]: matplotlib.__version__
Out[2]: '1.0.0'

In [3]: matplotlib.test()
/scratch/grout/sage-4.5.3/local/lib/python2.6/site-packages/matplotlib/axes.py:2369: UserWarning: Attempting to set identical left==right results
in singular transformations; automatically expanding.
left=730139.0, right=730139.0
  + 'left=%s, right=%s') % (left, right))
----------------------------------------------------------------------
Ran 138 tests in 755.419s

OK (KNOWNFAIL=42)
Out[3]: True
```




---

archive/issue_comments_086307.json:
```json
{
    "body": "Replying to [comment:30 jason]:\n> Okay, I've updated the spkg so that it works on t2 (and passes all matplotlib tests):\n> \n> http://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg\n> \n> Can people try it? \n\nI should be able to try this on OS X 10.4 PPC today or tomorrow.",
    "created_at": "2010-09-16T18:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86307",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:30 jason]:
> Okay, I've updated the spkg so that it works on t2 (and passes all matplotlib tests):
> 
> http://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg
> 
> Can people try it? 

I should be able to try this on OS X 10.4 PPC today or tomorrow.



---

archive/issue_comments_086308.json:
```json
{
    "body": "Okay, I've composed a long message to matplotlib-devel about this issue:\n\nhttp://sourceforge.net/mailarchive/message.php?msg_name=4C9262A9.5040901%40creativetrax.com",
    "created_at": "2010-09-16T18:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86308",
    "user": "https://github.com/jasongrout"
}
```

Okay, I've composed a long message to matplotlib-devel about this issue:

http://sourceforge.net/mailarchive/message.php?msg_name=4C9262A9.5040901%40creativetrax.com



---

archive/issue_comments_086309.json:
```json
{
    "body": "Replying to [comment:31 kcrisman]:\n> Replying to [comment:30 jason]:\n> > Okay, I've updated the spkg so that it works on t2 (and passes all matplotlib tests):\n> > \n> > http://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg\n> > \n> > Can people try it? \n> \n> I should be able to try this on OS X 10.4 PPC today or tomorrow.\n\nSeems to be working a-ok here, no issues.\n\nBy the way, to drkirkby, looks like matplotlib also uses `nose` to run their tests, like scipy and numpy.  I get no indication that `SAGE_CHECK=yes` does anything - or would - because of that.  \n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: import mat \nmath        matplotlib  \nsage: import matplotlib\nsage: matplotlib.test()\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n| Sage Version 4.6.prealpha4, Release Date: 2010-09-07               |\n| Type notebook() for the GUI, and license() for information.        |\n/Users/student/<ipython console> in <module>()\n\n/Users/student/Desktop/sage-4.6.prealpha4/local/lib/python2.6/site-packages/matplotlib/__init__.pyc in test(verbosity)\n    922 def test(verbosity=0):\n    923     \"\"\"run the matplotlib test suite\"\"\"\n--> 924     import nose\n    925     import nose.plugins.builtin\n    926     from testing.noseclasses import KnownFailure\n\nImportError: No module named nose\n```\n\nIf we want to test these automatically, we need nose; just adding the lines to `spkg-check` or `spkg-install` won't help.  Obviously this is a different ticket, but I wanted to point it out.  And I'd support adding this to Sage if it improved things overall.",
    "created_at": "2010-09-16T20:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86309",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:31 kcrisman]:
> Replying to [comment:30 jason]:
> > Okay, I've updated the spkg so that it works on t2 (and passes all matplotlib tests):
> > 
> > http://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg
> > 
> > Can people try it? 
> 
> I should be able to try this on OS X 10.4 PPC today or tomorrow.

Seems to be working a-ok here, no issues.

By the way, to drkirkby, looks like matplotlib also uses `nose` to run their tests, like scipy and numpy.  I get no indication that `SAGE_CHECK=yes` does anything - or would - because of that.  

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: import mat 
math        matplotlib  
sage: import matplotlib
sage: matplotlib.test()
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
| Sage Version 4.6.prealpha4, Release Date: 2010-09-07               |
| Type notebook() for the GUI, and license() for information.        |
/Users/student/<ipython console> in <module>()

/Users/student/Desktop/sage-4.6.prealpha4/local/lib/python2.6/site-packages/matplotlib/__init__.pyc in test(verbosity)
    922 def test(verbosity=0):
    923     """run the matplotlib test suite"""
--> 924     import nose
    925     import nose.plugins.builtin
    926     from testing.noseclasses import KnownFailure

ImportError: No module named nose
```

If we want to test these automatically, we need nose; just adding the lines to `spkg-check` or `spkg-install` won't help.  Obviously this is a different ticket, but I wanted to point it out.  And I'd support adding this to Sage if it improved things overall.



---

archive/issue_comments_086310.json:
```json
{
    "body": "Sorry; I should have CCd you on this: #9221",
    "created_at": "2010-09-16T20:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86310",
    "user": "https://github.com/jasongrout"
}
```

Sorry; I should have CCd you on this: #9221



---

archive/issue_comments_086311.json:
```json
{
    "body": "> Sorry; I should have CCd you on this: #9221\n???  That's this ticket, which I'm obviously already cc:ed on.  Did you mean something else related to nose?",
    "created_at": "2010-09-16T21:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86311",
    "user": "https://github.com/kcrisman"
}
```

> Sorry; I should have CCd you on this: #9221
???  That's this ticket, which I'm obviously already cc:ed on.  Did you mean something else related to nose?



---

archive/issue_comments_086312.json:
```json
{
    "body": "Yes: #9921.  Notice that it's convenient that related tickets have numbers so similar :).",
    "created_at": "2010-09-16T21:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86312",
    "user": "https://github.com/jasongrout"
}
```

Yes: #9921.  Notice that it's convenient that related tickets have numbers so similar :).



---

archive/issue_comments_086313.json:
```json
{
    "body": "Replying to [comment:33 kcrisman]:\n> Replying to [comment:31 kcrisman]:\n> > Replying to [comment:30 jason]:\n> > > Okay, I've updated the spkg so that it works on t2 (and passes all matplotlib tests):\n> > > \n> > > http://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg\n> > > \n> > > Can people try it? \n> > \n> > I should be able to try this on OS X 10.4 PPC today or tomorrow.\n> \n> Seems to be working a-ok here, no issues.\n> \n> By the way, to drkirkby, looks like matplotlib also uses `nose` to run their tests, like scipy and numpy.  I get no indication that `SAGE_CHECK=yes` does anything - or would - because of that.  \n\nSee \n\n#9921\n\nwhere only today I suggested we make 'nose' a **standard** package. \n\n> If we want to test these automatically, we need nose; just adding the lines to `spkg-check` or `spkg-install` won't help.  Obviously this is a different ticket, but I wanted to point it out.  And I'd support adding this to Sage if it improved things overall.\n\nAs far as I can see, adding nose as a stranded package would be very low risk, as nothing would depend on it except during testing. So it can't hardly screw Sage up, as long as nose builds reliably itself. Even if it was totally non-functional, it would not hurt sage. \n\nWhat we need is a list of packages that use nose, then request it is added as standard on the basis we can't test otherwise. It might be able to escape the 'experimental' stage. \n\nDave",
    "created_at": "2010-09-16T22:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86313",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:33 kcrisman]:
> Replying to [comment:31 kcrisman]:
> > Replying to [comment:30 jason]:
> > > Okay, I've updated the spkg so that it works on t2 (and passes all matplotlib tests):
> > > 
> > > http://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg
> > > 
> > > Can people try it? 
> > 
> > I should be able to try this on OS X 10.4 PPC today or tomorrow.
> 
> Seems to be working a-ok here, no issues.
> 
> By the way, to drkirkby, looks like matplotlib also uses `nose` to run their tests, like scipy and numpy.  I get no indication that `SAGE_CHECK=yes` does anything - or would - because of that.  

See 

#9921

where only today I suggested we make 'nose' a **standard** package. 

> If we want to test these automatically, we need nose; just adding the lines to `spkg-check` or `spkg-install` won't help.  Obviously this is a different ticket, but I wanted to point it out.  And I'd support adding this to Sage if it improved things overall.

As far as I can see, adding nose as a stranded package would be very low risk, as nothing would depend on it except during testing. So it can't hardly screw Sage up, as long as nose builds reliably itself. Even if it was totally non-functional, it would not hurt sage. 

What we need is a list of packages that use nose, then request it is added as standard on the basis we can't test otherwise. It might be able to escape the 'experimental' stage. 

Dave



---

archive/issue_comments_086314.json:
```json
{
    "body": "Eric Firing just committed a fix to matplotlib SVN which takes care of these compiling issues on Solaris.  Thanks for David for the tipoff on how to solve these issues (i.e., delete the kludgy defines).\n\nSee http://matplotlib.svn.sourceforge.net/viewvc/matplotlib?view=revision&revision=8707 for the commit log upstream.",
    "created_at": "2010-09-17T03:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86314",
    "user": "https://github.com/jasongrout"
}
```

Eric Firing just committed a fix to matplotlib SVN which takes care of these compiling issues on Solaris.  Thanks for David for the tipoff on how to solve these issues (i.e., delete the kludgy defines).

See http://matplotlib.svn.sourceforge.net/viewvc/matplotlib?view=revision&revision=8707 for the commit log upstream.



---

archive/issue_comments_086315.json:
```json
{
    "body": "(so in the next release, we can delete the patch I added to the spkg fixing the Solaris compiling issue).",
    "created_at": "2010-09-17T03:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86315",
    "user": "https://github.com/jasongrout"
}
```

(so in the next release, we can delete the patch I added to the spkg fixing the Solaris compiling issue).



---

archive/issue_comments_086316.json:
```json
{
    "body": "Ping about a review---can anyone review this?  The new spkg works on solaris (t2).  The new version of matplotlib adds some very nice features and allows us to clean up the spkg quite a bit.",
    "created_at": "2010-09-21T18:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86316",
    "user": "https://github.com/jasongrout"
}
```

Ping about a review---can anyone review this?  The new spkg works on solaris (t2).  The new version of matplotlib adds some very nice features and allows us to clean up the spkg quite a bit.



---

archive/issue_comments_086317.json:
```json
{
    "body": "Another friendly ping to people to look at this ticket and review it...",
    "created_at": "2010-09-28T15:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86317",
    "user": "https://github.com/jasongrout"
}
```

Another friendly ping to people to look at this ticket and review it...



---

archive/issue_comments_086318.json:
```json
{
    "body": "> Another friendly ping to people to look at this ticket and review it...\nI'd love to, but there is too much technical shell stuff mentioned in the comments so I don't want to be responsible for breaking something somewhere.",
    "created_at": "2010-09-28T15:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86318",
    "user": "https://github.com/kcrisman"
}
```

> Another friendly ping to people to look at this ticket and review it...
I'd love to, but there is too much technical shell stuff mentioned in the comments so I don't want to be responsible for breaking something somewhere.



---

archive/issue_comments_086319.json:
```json
{
    "body": "As I see it, the only outstanding problem was that it didn't compile on Solaris.  We fixed that (I compiled it on t2), but it doesn't seem appropriate for me to set the ticket to positive review.  I was hoping for someone to give it one last try on their standard platform.\n\nDavid, can you confirm that this spkg now works on Solaris?  If not, kcrisman, can you just check that it works on your platform still?",
    "created_at": "2010-09-28T15:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86319",
    "user": "https://github.com/jasongrout"
}
```

As I see it, the only outstanding problem was that it didn't compile on Solaris.  We fixed that (I compiled it on t2), but it doesn't seem appropriate for me to set the ticket to positive review.  I was hoping for someone to give it one last try on their standard platform.

David, can you confirm that this spkg now works on Solaris?  If not, kcrisman, can you just check that it works on your platform still?



---

archive/issue_comments_086320.json:
```json
{
    "body": "Replying to [comment:43 jason]:\n> As I see it, the only outstanding problem was that it didn't compile on Solaris.  We fixed that (I compiled it on t2), but it doesn't seem appropriate for me to set the ticket to positive review.  I was hoping for someone to give it one last try on their standard platform.\n> \n> David, can you confirm that this spkg now works on Solaris?  If not, kcrisman, can you just check that it works on your platform still?\nJason, that was the version I tried!\n\nSeems to be working fine on OS X 10.6 right now, tested the live documentation and the output at various spots.  Currently running doctests.",
    "created_at": "2010-09-28T16:23:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86320",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:43 jason]:
> As I see it, the only outstanding problem was that it didn't compile on Solaris.  We fixed that (I compiled it on t2), but it doesn't seem appropriate for me to set the ticket to positive review.  I was hoping for someone to give it one last try on their standard platform.
> 
> David, can you confirm that this spkg now works on Solaris?  If not, kcrisman, can you just check that it works on your platform still?
Jason, that was the version I tried!

Seems to be working fine on OS X 10.6 right now, tested the live documentation and the output at various spots.  Currently running doctests.



---

archive/issue_comments_086321.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-28T18:20:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86321",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086322.json:
```json
{
    "body": "Okay, all is well.  I love some of those plot doc graphics!  One definitely also needs the patch for the axis labels to look right - interesting change in API, though of course it was a switch from 0.x to 1.y!\n\nAs long as you are confident enough that t2 working is good (and indeed, drkirkby didn't say boo although he commented after that) then I'll set to positive review.",
    "created_at": "2010-09-28T18:20:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86322",
    "user": "https://github.com/kcrisman"
}
```

Okay, all is well.  I love some of those plot doc graphics!  One definitely also needs the patch for the axis labels to look right - interesting change in API, though of course it was a switch from 0.x to 1.y!

As long as you are confident enough that t2 working is good (and indeed, drkirkby didn't say boo although he commented after that) then I'll set to positive review.



---

archive/issue_comments_086323.json:
```json
{
    "body": "ptestlong in 4.6.alpha1 passes with the following tickets applied in order: #9221 (and new spkg), #9740, #9746, #4342.",
    "created_at": "2010-09-28T19:07:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86323",
    "user": "https://github.com/jasongrout"
}
```

ptestlong in 4.6.alpha1 passes with the following tickets applied in order: #9221 (and new spkg), #9740, #9746, #4342.



---

archive/issue_comments_086324.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T08:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86324",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009377.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-29T08:48:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9221#event-9377"
}
```



---

archive/issue_comments_086325.json:
```json
{
    "body": "Has anyone tested the new package with a full build of Sage from scratch?  I'm getting very many doctest errors that appears to stem from missing .ttf files.  I'll investigate further.",
    "created_at": "2010-09-29T23:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86325",
    "user": "https://github.com/qed777"
}
```

Has anyone tested the new package with a full build of Sage from scratch?  I'm getting very many doctest errors that appears to stem from missing .ttf files.  I'll investigate further.



---

archive/issue_comments_086326.json:
```json
{
    "body": "I haven't tested that configuration.  Can you post some of these errors here?",
    "created_at": "2010-09-30T01:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86326",
    "user": "https://github.com/jasongrout"
}
```

I haven't tested that configuration.  Can you post some of these errors here?



---

archive/issue_comments_086327.json:
```json
{
    "body": "I made a source distribution from 4.6.alpha1 + #9221 and built it in a directory named `sage-4.6.alpha2-9221`.  The long doctests pass.  I moved the directory to a different place.\n\nI made a source distribution from the latest trial 4.6.alpha2 + #9221 and built it in a directory named `sage-4.6.alpha2pre2`, i.e., it's different from the previous build directory.  Many tests fail with\n\n```\nRuntimeError: Could not open facefile /mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha2-9221/local/lib/python/site-packages/matplotlib/mpl-data/fonts/ttf/Vera.ttf; Cannot_Open_Resource\n```\n\nThe full log is [here](http://sage.math.washington.edu/home/mpatel/trac/9221/ptestlong-4.6.alpha2pre2.log).  I think the problem is that\n\n```sh\n$ grep 9221 $HOME/.matplotlib/fontList.cache | grep Vera.ttf\nS'/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha2-9221/local/lib/python/site-packages/matplotlib/mpl-data/fonts/ttf/Vera.ttf'\naS'/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha2-9221/local/lib/python/site-packages/matplotlib/mpl-data/fonts/ttf/Vera.ttf'\n$ grep 9221 $HOME/.matplotlib/fontList.cache | wc\n    128     128   16666\n```\n",
    "created_at": "2010-09-30T02:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86327",
    "user": "https://github.com/qed777"
}
```

I made a source distribution from 4.6.alpha1 + #9221 and built it in a directory named `sage-4.6.alpha2-9221`.  The long doctests pass.  I moved the directory to a different place.

I made a source distribution from the latest trial 4.6.alpha2 + #9221 and built it in a directory named `sage-4.6.alpha2pre2`, i.e., it's different from the previous build directory.  Many tests fail with

```
RuntimeError: Could not open facefile /mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha2-9221/local/lib/python/site-packages/matplotlib/mpl-data/fonts/ttf/Vera.ttf; Cannot_Open_Resource
```

The full log is [here](http://sage.math.washington.edu/home/mpatel/trac/9221/ptestlong-4.6.alpha2pre2.log).  I think the problem is that

```sh
$ grep 9221 $HOME/.matplotlib/fontList.cache | grep Vera.ttf
S'/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha2-9221/local/lib/python/site-packages/matplotlib/mpl-data/fonts/ttf/Vera.ttf'
aS'/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha2-9221/local/lib/python/site-packages/matplotlib/mpl-data/fonts/ttf/Vera.ttf'
$ grep 9221 $HOME/.matplotlib/fontList.cache | wc
    128     128   16666
```




---

archive/issue_comments_086328.json:
```json
{
    "body": "After moving `$HOME/.matplotlib` to a different place, I've rerun the tests in `sage-4.6.alpha2pre2`.  I see many failures with\n\n```\nAttributeError: 'module' object has no attribute 'cbook'\n```\n\nSee [this log](http://sage.math.washington.edu/home/mpatel/trac/9221/ptestlong-4.6.alpha2pre2-take2.log).  (I stopped the tests early.)\n\nI've started the tests again and now they appear to be passing.",
    "created_at": "2010-09-30T03:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86328",
    "user": "https://github.com/qed777"
}
```

After moving `$HOME/.matplotlib` to a different place, I've rerun the tests in `sage-4.6.alpha2pre2`.  I see many failures with

```
AttributeError: 'module' object has no attribute 'cbook'
```

See [this log](http://sage.math.washington.edu/home/mpatel/trac/9221/ptestlong-4.6.alpha2pre2-take2.log).  (I stopped the tests early.)

I've started the tests again and now they appear to be passing.



---

archive/issue_comments_086329.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-09-30T03:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86329",
    "user": "https://github.com/qed777"
}
```

Changing status from closed to needs_work.



---

archive/issue_events_009378.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-30T03:18:15Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9221#event-9378"
}
```



---

archive/issue_comments_086330.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-09-30T03:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86330",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_086331.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-09-30T03:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86331",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_086332.json:
```json
{
    "body": "I'm removing this from 4.6.alpha2, but there's still time for it in alpha3.",
    "created_at": "2010-09-30T03:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86332",
    "user": "https://github.com/qed777"
}
```

I'm removing this from 4.6.alpha2, but there's still time for it in alpha3.



---

archive/issue_comments_086333.json:
```json
{
    "body": "If you still have the directories around, keep the .matplotlib directory, but delete the fontList.cache file (it's a cache that should be automagically regenerated).",
    "created_at": "2010-09-30T04:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86333",
    "user": "https://github.com/jasongrout"
}
```

If you still have the directories around, keep the .matplotlib directory, but delete the fontList.cache file (it's a cache that should be automagically regenerated).



---

archive/issue_comments_086334.json:
```json
{
    "body": "Relevant docs: http://matplotlib.sourceforge.net/faq/troubleshooting_faq.html#matplotlib-directory-location\n\nMaybe Sage should set the MPLCONFIGDIR to point to something inside the Sage tree.",
    "created_at": "2010-09-30T04:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86334",
    "user": "https://github.com/jasongrout"
}
```

Relevant docs: http://matplotlib.sourceforge.net/faq/troubleshooting_faq.html#matplotlib-directory-location

Maybe Sage should set the MPLCONFIGDIR to point to something inside the Sage tree.



---

archive/issue_comments_086335.json:
```json
{
    "body": "In fact, setting MPLCONFIGDIR is #6235.",
    "created_at": "2010-09-30T04:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86335",
    "user": "https://github.com/jasongrout"
}
```

In fact, setting MPLCONFIGDIR is #6235.



---

archive/issue_comments_086336.json:
```json
{
    "body": "When I move things around to try to duplicate the issue, the cache file is automatically updated after plotting something using fonts.  So I'll try to recreate your problem with a fresh source+9221 build.",
    "created_at": "2010-09-30T05:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86336",
    "user": "https://github.com/jasongrout"
}
```

When I move things around to try to duplicate the issue, the cache file is automatically updated after plotting something using fonts.  So I'll try to recreate your problem with a fresh source+9221 build.



---

archive/issue_comments_086337.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-09-30T05:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86337",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_086338.json:
```json
{
    "body": "Replying to [comment:50 mpatel]:\n> I made a source distribution from 4.6.alpha1 + #9221 and built it in a directory named `sage-4.6.alpha2-9221`.  The long doctests pass.  I moved the directory to a different place.\n> \n> I made a source distribution from the latest trial 4.6.alpha2 + #9221 and built it in a directory named `sage-4.6.alpha2pre2`, i.e., it's different from the previous build directory.  Many tests fail with\n\n\nI assume this is on sage.math?  Can you make the latest trial 4.6.alpha2 tarball available somewhere so I can try to reproduce what you did?",
    "created_at": "2010-09-30T05:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86338",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:50 mpatel]:
> I made a source distribution from 4.6.alpha1 + #9221 and built it in a directory named `sage-4.6.alpha2-9221`.  The long doctests pass.  I moved the directory to a different place.
> 
> I made a source distribution from the latest trial 4.6.alpha2 + #9221 and built it in a directory named `sage-4.6.alpha2pre2`, i.e., it's different from the previous build directory.  Many tests fail with


I assume this is on sage.math?  Can you make the latest trial 4.6.alpha2 tarball available somewhere so I can try to reproduce what you did?



---

archive/issue_comments_086339.json:
```json
{
    "body": "I built on sage.math.  The latest trial 4.6.alpha2, which is likely final, as the builds appear to be going well, is in http://sage.math.washington.edu/home/release/sage-4.6.alpha2/ .",
    "created_at": "2010-09-30T10:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86339",
    "user": "https://github.com/qed777"
}
```

I built on sage.math.  The latest trial 4.6.alpha2, which is likely final, as the builds appear to be going well, is in http://sage.math.washington.edu/home/release/sage-4.6.alpha2/ .



---

archive/issue_comments_086340.json:
```json
{
    "body": "I'm going to try to reproduce this first on sage.math.\u00a0 Do I just replace the matplotlib-0.99.3 spkg with my spkg in the source tarball, then build?\u00a0 Is there something more I need to do?",
    "created_at": "2010-10-01T02:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86340",
    "user": "https://github.com/jasongrout"
}
```

I'm going to try to reproduce this first on sage.math.  Do I just replace the matplotlib-0.99.3 spkg with my spkg in the source tarball, then build?  Is there something more I need to do?



---

archive/issue_comments_086341.json:
```json
{
    "body": "Replying to [comment:60 jason]:\n> I'm going to try to reproduce this first on sage.math.\u00a0 Do I just replace the matplotlib-0.99.3 spkg with my spkg in the source tarball, then build?\u00a0 Is there something more I need to do?\n\nThat should work.  The colormap tests fixed by the patch will fail, but if the errors I saw show up --- i.e., they're not part of the \"fog of merge\" --- they'll be easy to distinguish.",
    "created_at": "2010-10-01T06:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86341",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:60 jason]:
> I'm going to try to reproduce this first on sage.math.  Do I just replace the matplotlib-0.99.3 spkg with my spkg in the source tarball, then build?  Is there something more I need to do?

That should work.  The colormap tests fixed by the patch will fail, but if the errors I saw show up --- i.e., they're not part of the "fog of merge" --- they'll be easy to distinguish.



---

archive/issue_comments_086342.json:
```json
{
    "body": "I've reproduced the problem and emailed the matplotlib mailing list.\u00a0 I'll also try tracking this down a bit this afternoon.",
    "created_at": "2010-10-01T15:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86342",
    "user": "https://github.com/jasongrout"
}
```

I've reproduced the problem and emailed the matplotlib mailing list.  I'll also try tracking this down a bit this afternoon.



---

archive/issue_comments_086343.json:
```json
{
    "body": "The reply on matplotlib-users is that this is already fixed in SVN.\u00a0 I'll get the commit, apply the patch, and update the spkg.",
    "created_at": "2010-10-01T15:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86343",
    "user": "https://github.com/jasongrout"
}
```

The reply on matplotlib-users is that this is already fixed in SVN.  I'll get the commit, apply the patch, and update the spkg.



---

archive/issue_comments_086344.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-10-01T18:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86344",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_086345.json:
```json
{
    "body": "Okay, I've updated the spkg (at the original address in the description) with the patch from matplotlib SVN that should take care of the problem.\u00a0 I'm building this momentarily.\n\nI'm putting this as needs review so that one or two others can double-check this.\u00a0 kcrisman?",
    "created_at": "2010-10-01T18:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86345",
    "user": "https://github.com/jasongrout"
}
```

Okay, I've updated the spkg (at the original address in the description) with the patch from matplotlib SVN that should take care of the problem.  I'm building this momentarily.

I'm putting this as needs review so that one or two others can double-check this.  kcrisman?



---

archive/issue_comments_086346.json:
```json
{
    "body": "> I'm putting this as needs review so that one or two others can double-check this.\u00a0 kcrisman?\nI'll do my best, but might not be able to test it on something you don't have access to already (you have OS X 10.6, and access to sage.math) until after the weekend.",
    "created_at": "2010-10-01T19:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86346",
    "user": "https://github.com/kcrisman"
}
```

> I'm putting this as needs review so that one or two others can double-check this.  kcrisman?
I'll do my best, but might not be able to test it on something you don't have access to already (you have OS X 10.6, and access to sage.math) until after the weekend.



---

archive/issue_comments_086347.json:
```json
{
    "body": "I can at least confirm that this mpl package installs fine with `./sage -i` on a relatively new (but not brand new) build of 4.6.alpha1.  I hope that is helpful; I don't have time to run any tests on this machine now.",
    "created_at": "2010-10-01T19:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86347",
    "user": "https://github.com/kcrisman"
}
```

I can at least confirm that this mpl package installs fine with `./sage -i` on a relatively new (but not brand new) build of 4.6.alpha1.  I hope that is helpful; I don't have time to run any tests on this machine now.



---

archive/issue_comments_086348.json:
```json
{
    "body": "mpatel: I just built a fresh copy of 4.6.alpha2 on sage.math with the new spkg (linked above) and ran ptestlong.\u00a0 I got the two colormap failures that are solved in the patch on this ticket, as well as two other failures that seem totally unrelated to this spkg.\n\nSo I think we are good to go.\u00a0 I feel weird setting this back to positive review, but can you try merging it again and \"reviewing\" the change to make sure it fixes the error you were seeing?",
    "created_at": "2010-10-02T02:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86348",
    "user": "https://github.com/jasongrout"
}
```

mpatel: I just built a fresh copy of 4.6.alpha2 on sage.math with the new spkg (linked above) and ran ptestlong.  I got the two colormap failures that are solved in the patch on this ticket, as well as two other failures that seem totally unrelated to this spkg.

So I think we are good to go.  I feel weird setting this back to positive review, but can you try merging it again and "reviewing" the change to make sure it fixes the error you were seeing?



---

archive/issue_comments_086349.json:
```json
{
    "body": "I haven't looked at the code at all, but it builds and passes tests for me on an Intel Mac OS X 10.6 box, skynet machine taurus (linux: x86_64-Linux-nehalem-fc), and skynet machine fulvia (Solaris on x86: x86_64-SunOS-core2). I also deleted my .matplotlib directory and reran the tests on taurus, and they passed again.  I haven't been following this ticket; is this good enough to restore the positive review?",
    "created_at": "2010-10-02T15:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86349",
    "user": "https://github.com/jhpalmieri"
}
```

I haven't looked at the code at all, but it builds and passes tests for me on an Intel Mac OS X 10.6 box, skynet machine taurus (linux: x86_64-Linux-nehalem-fc), and skynet machine fulvia (Solaris on x86: x86_64-SunOS-core2). I also deleted my .matplotlib directory and reran the tests on taurus, and they passed again.  I haven't been following this ticket; is this good enough to restore the positive review?



---

archive/issue_comments_086350.json:
```json
{
    "body": "I think so.",
    "created_at": "2010-10-02T16:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86350",
    "user": "https://github.com/jasongrout"
}
```

I think so.



---

archive/issue_comments_086351.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-02T16:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86351",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086352.json:
```json
{
    "body": "There are uncommitted changes\n\n```sh\nmatplotlib-1.0.0$ hg stat\n? patches/WrapPython.h\n? patches/WrapPython.h.diff\n```\n\nBy the way, is this the patch that fixes the font cache problem?",
    "created_at": "2010-10-02T23:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86352",
    "user": "https://github.com/qed777"
}
```

There are uncommitted changes

```sh
matplotlib-1.0.0$ hg stat
? patches/WrapPython.h
? patches/WrapPython.h.diff
```

By the way, is this the patch that fixes the font cache problem?



---

archive/issue_comments_086353.json:
```json
{
    "body": "No, that's the previous version of the spkg.  Apparently somehow the new version was not copied to my home directory on sage.math.\n\nThe new version is md5 28179fff25e33fc623f1de96a039eecc\n\nI've just double-checked, and it is now the version in my home directory:\n\nhttp://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg\n\nSorry for the mess-up!  I'm setting it back to needs_review, since apparently people reviewed the old spkg.  mpatel---I think you building on sage.math would be sufficient to review this.",
    "created_at": "2010-10-03T02:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86353",
    "user": "https://github.com/jasongrout"
}
```

No, that's the previous version of the spkg.  Apparently somehow the new version was not copied to my home directory on sage.math.

The new version is md5 28179fff25e33fc623f1de96a039eecc

I've just double-checked, and it is now the version in my home directory:

http://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg

Sorry for the mess-up!  I'm setting it back to needs_review, since apparently people reviewed the old spkg.  mpatel---I think you building on sage.math would be sufficient to review this.



---

archive/issue_comments_086354.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-10-03T02:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86354",
    "user": "https://github.com/jasongrout"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_086355.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-03T02:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86355",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086356.json:
```json
{
    "body": "BTW, WrapPython.h fixes the Solaris problem, and the font_manager.py patch fixes the font cache problem.",
    "created_at": "2010-10-03T02:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86356",
    "user": "https://github.com/jasongrout"
}
```

BTW, WrapPython.h fixes the Solaris problem, and the font_manager.py patch fixes the font cache problem.



---

archive/issue_comments_086357.json:
```json
{
    "body": "I wonder if maybe this happened because of the system maintenance on the home directory???  I don't know.  I might have also made a mistake when I thought I copied the new spkg over.",
    "created_at": "2010-10-03T02:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86357",
    "user": "https://github.com/jasongrout"
}
```

I wonder if maybe this happened because of the system maintenance on the home directory???  I don't know.  I might have also made a mistake when I thought I copied the new spkg over.



---

archive/issue_comments_086358.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-03T06:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86358",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009379.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-03T06:35:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9221#event-9379"
}
```



---

archive/issue_comments_086359.json:
```json
{
    "body": "Thanks, Jason!  The `fontList.cache` is now quietly regenerated and the tests pass on sage.math.",
    "created_at": "2010-10-03T06:40:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86359",
    "user": "https://github.com/qed777"
}
```

Thanks, Jason!  The `fontList.cache` is now quietly regenerated and the tests pass on sage.math.



---

archive/issue_comments_086360.json:
```json
{
    "body": "Replying to [comment:74 jason]:\n> BTW, WrapPython.h fixes the Solaris problem, and the font_manager.py patch fixes the font cache problem.\n\nAren't these worth an spkg patch level? This also avoids confusion with previous versions.",
    "created_at": "2010-10-20T14:57:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86360",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:74 jason]:
> BTW, WrapPython.h fixes the Solaris problem, and the font_manager.py patch fixes the font cache problem.

Aren't these worth an spkg patch level? This also avoids confusion with previous versions.



---

archive/issue_comments_086361.json:
```json
{
    "body": "Replying to [comment:79 leif]:\n> Replying to [comment:74 jason]:\n> > BTW, WrapPython.h fixes the Solaris problem, and the font_manager.py patch fixes the font cache problem.\n> \n> Aren't these worth an spkg patch level? This also avoids confusion with previous versions.\n>  \n\nI viewed this as part of the 1.0.0 spkg (these patches were necessary for the 1.0.0 spkg to be accepted and used).",
    "created_at": "2010-10-20T15:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86361",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:79 leif]:
> Replying to [comment:74 jason]:
> > BTW, WrapPython.h fixes the Solaris problem, and the font_manager.py patch fixes the font cache problem.
> 
> Aren't these worth an spkg patch level? This also avoids confusion with previous versions.
>  

I viewed this as part of the 1.0.0 spkg (these patches were necessary for the 1.0.0 spkg to be accepted and used).



---

archive/issue_comments_086362.json:
```json
{
    "body": "Replying to [comment:80 jason]:\n> Replying to [comment:79 leif]:\n> > Replying to [comment:74 jason]:\n> > > BTW, WrapPython.h fixes the Solaris problem, and the font_manager.py patch fixes the font cache problem.\n> > \n> > Aren't these worth an spkg patch level? This also avoids confusion with previous versions.\n> >  \n> \n> I viewed this as part of the 1.0.0 spkg (these patches were necessary for the 1.0.0 spkg to be accepted and used).\n\n:-) IMHO every spkg that's not almost vanilla upstream should carry a patch level, since the (Sage) package version (without the patch level) is not a Sage but the upstream version, but this appears to be an endless discussion...",
    "created_at": "2010-10-20T15:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86362",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:80 jason]:
> Replying to [comment:79 leif]:
> > Replying to [comment:74 jason]:
> > > BTW, WrapPython.h fixes the Solaris problem, and the font_manager.py patch fixes the font cache problem.
> > 
> > Aren't these worth an spkg patch level? This also avoids confusion with previous versions.
> >  
> 
> I viewed this as part of the 1.0.0 spkg (these patches were necessary for the 1.0.0 spkg to be accepted and used).

:-) IMHO every spkg that's not almost vanilla upstream should carry a patch level, since the (Sage) package version (without the patch level) is not a Sage but the upstream version, but this appears to be an endless discussion...



---

archive/issue_comments_086363.json:
```json
{
    "body": "I'm not the release manager, but **IMHO** either this ticket **needs work**, or #6235 / #9210? should be blockers for Sage 4.6, since\n\n* installing Sage 4.6.alpha3 / matplotlib 1.0.0 breaks other Sage installations (cf. doctest errors in `sage/plot/plot.py` below, which even occur after rebuilding e.g. Sage 4.5.3 from scratch),\n* the current spkg / alpha3 **again** breaks upgrading (cf. #9896) if the original Sage installation has been moved (copied / renamed), which apparently is common user practice.\n\n\nUnless one e.g. deletes `$HOME/.matplotlib/`, the following happens with **other** Sage installations (and perhaps other software):\n\n```\nsage -t -long \"devel/sage/sage/plot/plot.py\"                \n**********************************************************************\nFile \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/devel/sage/sage/plot/plot.py\", line 210:\n    sage: P    # show the result\nException raised:\n    Traceback (most recent call last):\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[55]>\", line 1, in <module>\n        P    # show the result###line 210:\n    sage: P    # show the result\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/misc/displayhook.py\", line 174, in displayhook\n        print_obj(sys.stdout, obj)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/misc/displayhook.py\", line 142, in print_obj\n        print >>out_stream, `obj`\n      File \"sage_object.pyx\", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1370)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/plot/plot.py\", line 915, in _repr_\n        self.show()\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/plot/plot.py\", line 1437, in show\n        self.save(DOCTEST_MODE_FILE, **options)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/plot/plot.py\", line 1973, in save\n        figure.savefig(filename,dpi=dpi,bbox_inches='tight',**options)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/figure.py\", line 1032, in savefig\n        self.canvas.print_figure(*args, **kwargs)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/backend_bases.py\", line 1455, in print_figure\n        **kwargs)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/backends/backend_agg.py\", line 358, in print_png\n        FigureCanvasAgg.draw(self)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/backends/backend_agg.py\", line 314, in draw\n        self.figure.draw(self.renderer)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/artist.py\", line 46, in draw_wrapper\n        draw(artist, renderer, *args, **kwargs)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/figure.py\", line 773, in draw\n        for a in self.axes: a.draw(renderer)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/artist.py\", line 46, in draw_wrapper\n        draw(artist, renderer, *args, **kwargs)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/axes.py\", line 1735, in draw\n        a.draw(renderer)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/text.py\", line 518, in draw\n        bbox, info = self._get_layout(renderer)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/text.py\", line 280, in _get_layout\n        clean_line, self._fontproperties, ismath=ismath)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/backends/backend_agg.py\", line 156, in get_text_width_height_descent\n        self.mathtext_parser.parse(s, self.dpi, prop)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/mathtext.py\", line 2797, in parse\n        font_output = fontset_class(prop, backend)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/mathtext.py\", line 658, in __init__\n        self._stix_fallback = StixFonts(*args, **kwargs)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/mathtext.py\", line 900, in __init__\n        fullpath = findfont(name)\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/font_manager.py\", line 1306, in findfont\n        if not os.path.exists(font):\n      File \"/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python2.6/genericpath.py\", line 18, in exists\n        st = os.stat(path)\n    TypeError: coercing to Unicode: need string or buffer, dict found\n**********************************************************************\n...\n[same exception in other examples]\n...\n**********************************************************************\n5 items had failures:\n   1 of  71 in __main__.example_0\n   1 of   7 in __main__.example_13\n   1 of   8 in __main__.example_14\n   1 of  45 in __main__.example_30\n   1 of  89 in __main__.example_43\n***Test Failed*** 5 failures.\nFor whitespace errors, see the file /home/leif/.sage//tmp/.doctest_plot.py\n```\n\n\n\nWhen trying to upgrade to 4.6.alpha3 in a *renamed* directory, installing matplotlib 1.0.0 fails with\n\n```\n...\nrunning build_ext\nbuilding 'matplotlib.ft2font' extension\ncreating build/temp.linux-x86_64-2.6\ncreating build/temp.linux-x86_64-2.6/src\ncreating build/temp.linux-x86_64-2.6/CXX\ngcc -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -march=native -O3 -fno-strict-aliasing -fomit-frame-pointer -DHONORS_CFLAGS -march=native -O3 -DHONORS_CPPFLAGS -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/lib/python2.6/site-packages/numpy/core/include -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/include/freetype2 -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/include -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include -I. -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6 -c src/ft2font.cpp -o build/temp.linux-x86_64-2.6/src/ft2font.o\ncc1plus: warning: command line option \"-Wstrict-prototypes\" is valid for Ada/C/ObjC but not for C++\nIn file included from /home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6/Python.h:8,\n                 from ./CXX/WrapPython.h:47,\n                 from ./CXX/Extensions.hxx:37,\n                 from src/ft2font.h:4,\n                 from src/ft2font.cpp:1:\n/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6/pyconfig.h:1028:1: warning: \"_POSIX_C_SOURCE\" redefined\nIn file included from /usr/include/sys/time.h:23,\n                 from ./CXX/WrapPython.h:43,\n                 from ./CXX/Extensions.hxx:37,\n                 from src/ft2font.h:4,\n                 from src/ft2font.cpp:1:\n/usr/include/features.h:158:1: warning: this is the location of the previous definition\nIn file included from /home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6/Python.h:8,\n                 from ./CXX/WrapPython.h:47,\n                 from ./CXX/Extensions.hxx:37,\n                 from src/ft2font.h:4,\n                 from src/ft2font.cpp:1:\n/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6/pyconfig.h:1037:1: warning: \"_XOPEN_SOURCE\" redefined\nIn file included from /usr/include/sys/time.h:23,\n                 from ./CXX/WrapPython.h:43,\n                 from ./CXX/Extensions.hxx:37,\n                 from src/ft2font.h:4,\n                 from src/ft2font.cpp:1:\n/usr/include/features.h:160:1: warning: this is the location of the previous definition\nIn file included from src/ft2font.h:14,\n                 from src/ft2font.cpp:1:\n/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/ft2build.h:56:38: error: freetype/config/ftheader.h: No such file or directory\nIn file included from src/ft2font.cpp:1:\nsrc/ft2font.h:15:10: error: #include expects \"FILENAME\" or <FILENAME>\nsrc/ft2font.h:16:10: error: #include expects \"FILENAME\" or <FILENAME>\nsrc/ft2font.h:17:10: error: #include expects \"FILENAME\" or <FILENAME>\nsrc/ft2font.h:18:10: error: #include expects \"FILENAME\" or <FILENAME>\nsrc/ft2font.h:19:10: error: #include expects \"FILENAME\" or <FILENAME>\nIn file included from src/ft2font.cpp:1:\nsrc/ft2font.h:33: error: 'FT_Bitmap' has not been declared\nsrc/ft2font.h:33: error: 'FT_Int' has not been declared\nsrc/ft2font.h:33: error: 'FT_Int' has not been declared\nsrc/ft2font.h:89: error: ISO C++ forbids declaration of 'FT_Face' with no type\nsrc/ft2font.h:89: error: expected ',' or '...' before '&' token\nsrc/ft2font.h:95: error: ISO C++ forbids declaration of 'FT_Face' with no type\nsrc/ft2font.h:95: error: expected ',' or '...' before '&' token\nsrc/ft2font.h:137: error: 'FT_Face' does not name a type\nsrc/ft2font.h:138: error: 'FT_Matrix' does not name a type\nsrc/ft2font.h:139: error: 'FT_Vector' does not name a type\nsrc/ft2font.h:140: error: 'FT_Error' does not name a type\nsrc/ft2font.h:141: error: 'FT_Glyph' was not declared in this scope\nsrc/ft2font.h:141: error: template argument 1 is invalid\nsrc/ft2font.h:141: error: template argument 2 is invalid\nsrc/ft2font.h:142: error: 'FT_Vector' was not declared in this scope\nsrc/ft2font.h:142: error: template argument 1 is invalid\nsrc/ft2font.h:142: error: template argument 2 is invalid\nsrc/ft2font.h:148: error: 'FT_BBox' does not name a type\nsrc/ft2font.cpp:45: error: 'FT_Library' does not name a type\nsrc/ft2font.cpp:108: error: variable or field 'draw_bitmap' declared void\nsrc/ft2font.cpp:108: error: 'FT_Bitmap' was not declared in this scope\nsrc/ft2font.cpp:108: error: 'bitmap' was not declared in this scope\nsrc/ft2font.cpp:109: error: 'FT_Int' was not declared in this scope\nsrc/ft2font.cpp:110: error: 'FT_Int' was not declared in this scope\n/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/lib/python2.6/site-packages/numpy/core/include/numpy/__multiarray_api.h:968: warning: 'int _import_array()' defined but not used\nerror: command 'gcc' failed with exit status 1\nError building matplotlib package.\n```\n",
    "created_at": "2010-10-20T18:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86363",
    "user": "https://github.com/nexttime"
}
```

I'm not the release manager, but **IMHO** either this ticket **needs work**, or #6235 / #9210? should be blockers for Sage 4.6, since

* installing Sage 4.6.alpha3 / matplotlib 1.0.0 breaks other Sage installations (cf. doctest errors in `sage/plot/plot.py` below, which even occur after rebuilding e.g. Sage 4.5.3 from scratch),
* the current spkg / alpha3 **again** breaks upgrading (cf. #9896) if the original Sage installation has been moved (copied / renamed), which apparently is common user practice.


Unless one e.g. deletes `$HOME/.matplotlib/`, the following happens with **other** Sage installations (and perhaps other software):

```
sage -t -long "devel/sage/sage/plot/plot.py"                
**********************************************************************
File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/devel/sage/sage/plot/plot.py", line 210:
    sage: P    # show the result
Exception raised:
    Traceback (most recent call last):
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[55]>", line 1, in <module>
        P    # show the result###line 210:
    sage: P    # show the result
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/misc/displayhook.py", line 174, in displayhook
        print_obj(sys.stdout, obj)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/misc/displayhook.py", line 142, in print_obj
        print >>out_stream, `obj`
      File "sage_object.pyx", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1370)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/plot/plot.py", line 915, in _repr_
        self.show()
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/plot/plot.py", line 1437, in show
        self.save(DOCTEST_MODE_FILE, **options)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/plot/plot.py", line 1973, in save
        figure.savefig(filename,dpi=dpi,bbox_inches='tight',**options)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/figure.py", line 1032, in savefig
        self.canvas.print_figure(*args, **kwargs)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/backend_bases.py", line 1455, in print_figure
        **kwargs)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 358, in print_png
        FigureCanvasAgg.draw(self)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 314, in draw
        self.figure.draw(self.renderer)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/artist.py", line 46, in draw_wrapper
        draw(artist, renderer, *args, **kwargs)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/figure.py", line 773, in draw
        for a in self.axes: a.draw(renderer)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/artist.py", line 46, in draw_wrapper
        draw(artist, renderer, *args, **kwargs)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/axes.py", line 1735, in draw
        a.draw(renderer)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/text.py", line 518, in draw
        bbox, info = self._get_layout(renderer)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/text.py", line 280, in _get_layout
        clean_line, self._fontproperties, ismath=ismath)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 156, in get_text_width_height_descent
        self.mathtext_parser.parse(s, self.dpi, prop)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/mathtext.py", line 2797, in parse
        font_output = fontset_class(prop, backend)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/mathtext.py", line 658, in __init__
        self._stix_fallback = StixFonts(*args, **kwargs)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/mathtext.py", line 900, in __init__
        fullpath = findfont(name)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/font_manager.py", line 1306, in findfont
        if not os.path.exists(font):
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python2.6/genericpath.py", line 18, in exists
        st = os.stat(path)
    TypeError: coercing to Unicode: need string or buffer, dict found
**********************************************************************
...
[same exception in other examples]
...
**********************************************************************
5 items had failures:
   1 of  71 in __main__.example_0
   1 of   7 in __main__.example_13
   1 of   8 in __main__.example_14
   1 of  45 in __main__.example_30
   1 of  89 in __main__.example_43
***Test Failed*** 5 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_plot.py
```



When trying to upgrade to 4.6.alpha3 in a *renamed* directory, installing matplotlib 1.0.0 fails with

```
...
running build_ext
building 'matplotlib.ft2font' extension
creating build/temp.linux-x86_64-2.6
creating build/temp.linux-x86_64-2.6/src
creating build/temp.linux-x86_64-2.6/CXX
gcc -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -march=native -O3 -fno-strict-aliasing -fomit-frame-pointer -DHONORS_CFLAGS -march=native -O3 -DHONORS_CPPFLAGS -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/lib/python2.6/site-packages/numpy/core/include -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/include/freetype2 -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/include -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include -I. -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6 -c src/ft2font.cpp -o build/temp.linux-x86_64-2.6/src/ft2font.o
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
In file included from /home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6/Python.h:8,
                 from ./CXX/WrapPython.h:47,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/ft2font.cpp:1:
/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6/pyconfig.h:1028:1: warning: "_POSIX_C_SOURCE" redefined
In file included from /usr/include/sys/time.h:23,
                 from ./CXX/WrapPython.h:43,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/ft2font.cpp:1:
/usr/include/features.h:158:1: warning: this is the location of the previous definition
In file included from /home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6/Python.h:8,
                 from ./CXX/WrapPython.h:47,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/ft2font.cpp:1:
/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6/pyconfig.h:1037:1: warning: "_XOPEN_SOURCE" redefined
In file included from /usr/include/sys/time.h:23,
                 from ./CXX/WrapPython.h:43,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/ft2font.cpp:1:
/usr/include/features.h:160:1: warning: this is the location of the previous definition
In file included from src/ft2font.h:14,
                 from src/ft2font.cpp:1:
/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/ft2build.h:56:38: error: freetype/config/ftheader.h: No such file or directory
In file included from src/ft2font.cpp:1:
src/ft2font.h:15:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:16:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:17:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:18:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:19:10: error: #include expects "FILENAME" or <FILENAME>
In file included from src/ft2font.cpp:1:
src/ft2font.h:33: error: 'FT_Bitmap' has not been declared
src/ft2font.h:33: error: 'FT_Int' has not been declared
src/ft2font.h:33: error: 'FT_Int' has not been declared
src/ft2font.h:89: error: ISO C++ forbids declaration of 'FT_Face' with no type
src/ft2font.h:89: error: expected ',' or '...' before '&' token
src/ft2font.h:95: error: ISO C++ forbids declaration of 'FT_Face' with no type
src/ft2font.h:95: error: expected ',' or '...' before '&' token
src/ft2font.h:137: error: 'FT_Face' does not name a type
src/ft2font.h:138: error: 'FT_Matrix' does not name a type
src/ft2font.h:139: error: 'FT_Vector' does not name a type
src/ft2font.h:140: error: 'FT_Error' does not name a type
src/ft2font.h:141: error: 'FT_Glyph' was not declared in this scope
src/ft2font.h:141: error: template argument 1 is invalid
src/ft2font.h:141: error: template argument 2 is invalid
src/ft2font.h:142: error: 'FT_Vector' was not declared in this scope
src/ft2font.h:142: error: template argument 1 is invalid
src/ft2font.h:142: error: template argument 2 is invalid
src/ft2font.h:148: error: 'FT_BBox' does not name a type
src/ft2font.cpp:45: error: 'FT_Library' does not name a type
src/ft2font.cpp:108: error: variable or field 'draw_bitmap' declared void
src/ft2font.cpp:108: error: 'FT_Bitmap' was not declared in this scope
src/ft2font.cpp:108: error: 'bitmap' was not declared in this scope
src/ft2font.cpp:109: error: 'FT_Int' was not declared in this scope
src/ft2font.cpp:110: error: 'FT_Int' was not declared in this scope
/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/lib/python2.6/site-packages/numpy/core/include/numpy/__multiarray_api.h:968: warning: 'int _import_array()' defined but not used
error: command 'gcc' failed with exit status 1
Error building matplotlib package.
```




---

archive/issue_comments_086364.json:
```json
{
    "body": "Replying to [comment:82 leif]:\n> I'm not the release manager, but **IMHO** either this ticket **needs work**, or #6235 / #9210? should be blockers for Sage 4.6, since\n> \n>  * installing Sage 4.6.alpha3 / matplotlib 1.0.0 breaks other Sage installations (cf. doctest errors in `sage/plot/plot.py` below, which even occur after rebuilding e.g. Sage 4.5.3 from scratch),\n\nAre you sure that you have the most recent (i.e., the merged) 1.0.0 spkg from this ticket?  Can you try sage -f just in case (you see that there have been updates to the 1.0.0 spkg on this ticket as time went on)\n\nOr wait.  Are you saying that the font cache file created by the new(est) spkg here is causing problems with older versions of matplotlib?",
    "created_at": "2010-10-20T21:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86364",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:82 leif]:
> I'm not the release manager, but **IMHO** either this ticket **needs work**, or #6235 / #9210? should be blockers for Sage 4.6, since
> 
>  * installing Sage 4.6.alpha3 / matplotlib 1.0.0 breaks other Sage installations (cf. doctest errors in `sage/plot/plot.py` below, which even occur after rebuilding e.g. Sage 4.5.3 from scratch),

Are you sure that you have the most recent (i.e., the merged) 1.0.0 spkg from this ticket?  Can you try sage -f just in case (you see that there have been updates to the 1.0.0 spkg on this ticket as time went on)

Or wait.  Are you saying that the font cache file created by the new(est) spkg here is causing problems with older versions of matplotlib?



---

archive/issue_comments_086365.json:
```json
{
    "body": "Replying to [comment:83 jason]:\n> Replying to [comment:82 leif]:\n> > I'm not the release manager, but **IMHO** either this ticket **needs work**, or #6235 / #9210? should be blockers for Sage 4.6, since\n> > \n> >  * installing Sage 4.6.alpha3 / matplotlib 1.0.0 breaks other Sage installations (cf. doctest errors in `sage/plot/plot.py` below, which even occur after rebuilding e.g. Sage 4.5.3 from scratch),\n> \n> Are you sure that you have the most recent (i.e., the merged) 1.0.0 spkg from this ticket?  Can you try sage -f just in case (you see that there have been updates to the 1.0.0 spkg on this ticket as time went on)\n\nI only have the current 1.0.0 one, but that doesn't solve the problems older MPL installations have. ;-)\n \n> Or wait.  Are you saying that the font cache file created by the new(est) spkg here is causing problems with older versions of matplotlib?\n\nExactly that. It seems they've changed the format s.t. older MPL versions expecting an older format (without doing any consistency / type / error checking) pass a dictionary to `os.path.exists()`.",
    "created_at": "2010-10-20T21:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86365",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:83 jason]:
> Replying to [comment:82 leif]:
> > I'm not the release manager, but **IMHO** either this ticket **needs work**, or #6235 / #9210? should be blockers for Sage 4.6, since
> > 
> >  * installing Sage 4.6.alpha3 / matplotlib 1.0.0 breaks other Sage installations (cf. doctest errors in `sage/plot/plot.py` below, which even occur after rebuilding e.g. Sage 4.5.3 from scratch),
> 
> Are you sure that you have the most recent (i.e., the merged) 1.0.0 spkg from this ticket?  Can you try sage -f just in case (you see that there have been updates to the 1.0.0 spkg on this ticket as time went on)

I only have the current 1.0.0 one, but that doesn't solve the problems older MPL installations have. ;-)
 
> Or wait.  Are you saying that the font cache file created by the new(est) spkg here is causing problems with older versions of matplotlib?

Exactly that. It seems they've changed the format s.t. older MPL versions expecting an older format (without doing any consistency / type / error checking) pass a dictionary to `os.path.exists()`.



---

archive/issue_comments_086366.json:
```json
{
    "body": "Leif, do the current patches at #6235 and #9210 fix the problems you've found?",
    "created_at": "2010-10-20T23:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86366",
    "user": "https://github.com/qed777"
}
```

Leif, do the current patches at #6235 and #9210 fix the problems you've found?



---

archive/issue_comments_086367.json:
```json
{
    "body": "Replying to [comment:85 mpatel]:\n> Leif, do the current patches at #6235 and #9210 fix the problems you've found?\n\nI'm pretty sure #6235 fixes (at least Sage's) MPL 1.0.0 breaking older installations.\n\nModifying `$SAGE_ROOT/local/lib/pkgconfig/freetype2.pc` on Sage relocations perhaps fixes later build errors (including upgrades) of dependent packages like MPL; I haven't looked at nor tested the patch though. (Forcing reinstallation of freetype after moving Sage fixes it; but that's of course just a work-around, cf. #9896.)\n\nAt least for freetype, it should be possible to simply set `prefix` to `$SAGE_LOCAL` (unexpanded) rather than a hard-coded absolute path. (Done once, e.g. in its `spkg-install`.)",
    "created_at": "2010-10-21T01:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86367",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:85 mpatel]:
> Leif, do the current patches at #6235 and #9210 fix the problems you've found?

I'm pretty sure #6235 fixes (at least Sage's) MPL 1.0.0 breaking older installations.

Modifying `$SAGE_ROOT/local/lib/pkgconfig/freetype2.pc` on Sage relocations perhaps fixes later build errors (including upgrades) of dependent packages like MPL; I haven't looked at nor tested the patch though. (Forcing reinstallation of freetype after moving Sage fixes it; but that's of course just a work-around, cf. #9896.)

At least for freetype, it should be possible to simply set `prefix` to `$SAGE_LOCAL` (unexpanded) rather than a hard-coded absolute path. (Done once, e.g. in its `spkg-install`.)



---

archive/issue_comments_086368.json:
```json
{
    "body": "Replying to [comment:86 leif]:\n> At least for freetype, it should be possible to simply set `prefix` to `$SAGE_LOCAL` (unexpanded) rather than a hard-coded absolute path. (Done once, e.g. in its `spkg-install`.)\n\n\n```\nprefix=${SAGE_LOCAL}\nexec_prefix=${prefix}\nlibdir=${exec_prefix}/lib\nincludedir=${prefix}/include\n\nName: FreeType 2\nDescription: A free, high-quality, and portable font engine.\nVersion: 9.16.3\nRequires:\nLibs: -L${libdir} -lfreetype\nCflags: -I${includedir}/freetype2 -I${includedir}\n```\n\nworks for me. (The curly braces are mandatory.)",
    "created_at": "2010-10-21T01:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86368",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:86 leif]:
> At least for freetype, it should be possible to simply set `prefix` to `$SAGE_LOCAL` (unexpanded) rather than a hard-coded absolute path. (Done once, e.g. in its `spkg-install`.)


```
prefix=${SAGE_LOCAL}
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include

Name: FreeType 2
Description: A free, high-quality, and portable font engine.
Version: 9.16.3
Requires:
Libs: -L${libdir} -lfreetype
Cflags: -I${includedir}/freetype2 -I${includedir}
```

works for me. (The curly braces are mandatory.)



---

archive/issue_comments_086369.json:
```json
{
    "body": "Replying to [comment:85 mpatel]:\n> Leif, do the current patches at #6235 and #9210 fix the problems you've found?\n\nObviously #9210 doesn't help with upgrades from older versions, i.e. upgrading **to** 4.6. So for 4.6, it's perhaps better to fix the freetype spkg (though even preparing a fake new spkg would suffice for the moment).\n\nAgain hard-coding `SAGE_ROOT` into the `.pc` files is IMHO superfluous btw.",
    "created_at": "2010-10-21T04:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86369",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:85 mpatel]:
> Leif, do the current patches at #6235 and #9210 fix the problems you've found?

Obviously #9210 doesn't help with upgrades from older versions, i.e. upgrading **to** 4.6. So for 4.6, it's perhaps better to fix the freetype spkg (though even preparing a fake new spkg would suffice for the moment).

Again hard-coding `SAGE_ROOT` into the `.pc` files is IMHO superfluous btw.



---

archive/issue_comments_086370.json:
```json
{
    "body": "Replying to [comment:88 leif]:\n> Replying to [comment:85 mpatel]:\n> > Leif, do the current patches at #6235 and #9210 fix the problems you've found?\n> \n> Obviously #9210 doesn't help with upgrades from older versions, i.e. upgrading **to** 4.6. So for 4.6, it's perhaps better to fix the freetype spkg (though even preparing a fake new spkg would suffice for the moment).\n\nFor 4.6, I suggest we just bump up the patch level for freetype.  Could you do this and add a link to the new spkg here?",
    "created_at": "2010-10-21T07:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86370",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:88 leif]:
> Replying to [comment:85 mpatel]:
> > Leif, do the current patches at #6235 and #9210 fix the problems you've found?
> 
> Obviously #9210 doesn't help with upgrades from older versions, i.e. upgrading **to** 4.6. So for 4.6, it's perhaps better to fix the freetype spkg (though even preparing a fake new spkg would suffice for the moment).

For 4.6, I suggest we just bump up the patch level for freetype.  Could you do this and add a link to the new spkg here?



---

archive/issue_comments_086371.json:
```json
{
    "body": "Replying to [comment:89 mpatel]:\n> Replying to [comment:88 leif]:\n> > Replying to [comment:85 mpatel]:\n> > > Leif, do the current patches at #6235 and #9210 fix the problems you've found?\n> > \n> > Obviously #9210 doesn't help with upgrades from older versions, i.e. upgrading **to** 4.6. So for 4.6, it's perhaps better to fix the freetype spkg (though even preparing a fake new spkg would suffice for the moment).\n> \n> For 4.6, I suggest we just bump up the patch level for freetype.  Could you do this and add a link to the new spkg here?\n\nI've put an \"updated\" spkg at\n\n http://sage.math.washington.edu/home/mpatel/trac/9221/freetype-2.3.5.p3.spkg",
    "created_at": "2010-10-21T09:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86371",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:89 mpatel]:
> Replying to [comment:88 leif]:
> > Replying to [comment:85 mpatel]:
> > > Leif, do the current patches at #6235 and #9210 fix the problems you've found?
> > 
> > Obviously #9210 doesn't help with upgrades from older versions, i.e. upgrading **to** 4.6. So for 4.6, it's perhaps better to fix the freetype spkg (though even preparing a fake new spkg would suffice for the moment).
> 
> For 4.6, I suggest we just bump up the patch level for freetype.  Could you do this and add a link to the new spkg here?

I've put an "updated" spkg at

 http://sage.math.washington.edu/home/mpatel/trac/9221/freetype-2.3.5.p3.spkg



---

archive/issue_comments_086372.json:
```json
{
    "body": "Replying to [comment:86 leif]:\n\n> At least for freetype, it should be possible to simply set `prefix` to `$SAGE_LOCAL` (unexpanded) rather than a hard-coded absolute path. (Done once, e.g. in its `spkg-install`.)\n\nThat's fantastic!  It sounds like we should investigate doing that for the other packages as well (like libpng, etc.)  There are some places in the pkgconfig files where the path is used in places other than the prefix, so doing this trick may not solve everything, but probably would solve a lot of the issues with pkgconfig files.",
    "created_at": "2010-10-21T12:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86372",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:86 leif]:

> At least for freetype, it should be possible to simply set `prefix` to `$SAGE_LOCAL` (unexpanded) rather than a hard-coded absolute path. (Done once, e.g. in its `spkg-install`.)

That's fantastic!  It sounds like we should investigate doing that for the other packages as well (like libpng, etc.)  There are some places in the pkgconfig files where the path is used in places other than the prefix, so doing this trick may not solve everything, but probably would solve a lot of the issues with pkgconfig files.



---

archive/issue_comments_086373.json:
```json
{
    "body": "Replying to [comment:91 jason]:\n> Replying to [comment:86 leif]:\n> \n> > At least for freetype, it should be possible to simply set `prefix` to `$SAGE_LOCAL` (unexpanded) rather than a hard-coded absolute path. (Done once, e.g. in its `spkg-install`.)\n> \n> That's fantastic!  It sounds like we should investigate doing that for the other packages as well (like libpng, etc.)  There are some places in the pkgconfig files where the path is used in places other than the prefix, so doing this trick may not solve everything, but probably would solve a lot of the issues with pkgconfig files.\n\nI've made this idea #10202.  Leif, do you think we can do this at compile time, or do we have to fix up the pkgconfig file after the spkg is installed?  I'm guessing the latter.",
    "created_at": "2010-11-02T14:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9221#issuecomment-86373",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:91 jason]:
> Replying to [comment:86 leif]:
> 
> > At least for freetype, it should be possible to simply set `prefix` to `$SAGE_LOCAL` (unexpanded) rather than a hard-coded absolute path. (Done once, e.g. in its `spkg-install`.)
> 
> That's fantastic!  It sounds like we should investigate doing that for the other packages as well (like libpng, etc.)  There are some places in the pkgconfig files where the path is used in places other than the prefix, so doing this trick may not solve everything, but probably would solve a lot of the issues with pkgconfig files.

I've made this idea #10202.  Leif, do you think we can do this at compile time, or do we have to fix up the pkgconfig file after the spkg is installed?  I'm guessing the latter.
