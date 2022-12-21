# Issue 9895: upgrading from 4.5.3 to 4.6.alpha0 fails on OS X 10.6

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-09-11 06:04:41

Assignee: GeorgSWeber

CC:  cremona drkirkby jdemeyer leif justin mhansen

On two separate machines running OS X 10.6, upgrading from 4.5.3 to 4.6.alpha0 seemed to work -- no errors were reported -- but Sage fails to start:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
  ***   bug in PARI/GP (Segmentation Fault), please report
  ***   bug in PARI/GP (Segmentation Fault), please report
```

(Building from scratch works fine.)


---

Comment by mpatel created at 2010-09-11 23:54:40

Can we somehow trace the PARI calls that lead to this?


---

Comment by mpatel created at 2010-09-12 00:02:57

Replying to [comment:2 mpatel]:
> Can we somehow trace the PARI calls that lead to this?

Running `sage -gdb` could help, but on bsd.math, I get

```
[...]
We need authorization from an admin user to run the debugger.
This will only happen once per login session.
Admin username (mpatel): 
```



---

Comment by jhpalmieri created at 2010-09-12 00:36:04

My problem is I don't know how to use gdb.  After running "sage -gdb", I see a ton of message like 

```
Reading symbols for shared libraries . done
```

and warnings like

```
warning: Could not find object file "/Applications/sage_builds/sage-4.5.3/spkg/build/gsl-1.14/src/.libs/libgsl.lax/libgslcdf.a/weibull.o" - no debug information available for "weibull.c".
```

Then

```
Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_INVALID_ADDRESS at address: 0x0000000000000000
0x000000010285aadc in err_leave ()
(gdb) 
```

Now what should I type to provide meaningful information?


---

Comment by mpatel created at 2010-09-12 00:54:36

What happens if you type `bt` (for a backtrace)?  I'm not very familiar with GDB, but perhaps [comment:ticket:9583:5 this] or David can help?


---

Comment by leif created at 2010-09-12 00:55:14

`bt` (backtrace)?

Btw, the segfault happens somewhere in `pari_init()`, because Sage afterwards disables PARI's signal handlers.


---

Comment by leif created at 2010-09-12 01:04:11

Perhaps also first rebuild PARI with `CFLAGS=-fno-omit-frame-pointer`, and less optimization (`-O1` or `-O0`).


---

Comment by jhpalmieri created at 2010-09-12 01:35:17

Well, I tried to rebuild PARI by setting CFLAGS="-fno-omit-frame-pointer -O0" and then "sage -f pari...".  (I also tried running PARI's ./Configure with the "-g" debugging option, but it failed with

```
ld: symbol(s) not found for inferred architecture x86_64
```

so I gave up on that.)  When I ran "bt", I got this:

```

(gdb) bt
#0  0x000000010285aadc in err_leave ()
#1  0x0000000102a72b5d in __pyx_pf_4sage_4libs_4pari_3gen_12PariInstance___init__ (__pyx_v_self=0x10211a4f0, __pyx_args=<value temporarily unavailable, due to optimizations>, __pyx_kwds=0x101f573b0) at sage/libs/pari/gen.c:36951
#2  0x000000010006d8c5 in type_call ()
#3  0x000000010000bcd2 in PyObject_Call ()
#4  0x0000000102a424fc in initgen () at sage/libs/pari/gen.c:46847
#5  0x00000001000d2e11 in _PyImport_LoadDynamicModule ()
#6  0x00000001000d10bf in import_submodule ()
#7  0x00000001000d15da in load_next ()
#8  0x00000001000d1932 in PyImport_ImportModuleLevel ()
#9  0x00000001000aeef3 in builtin___import__ ()
#10 0x000000010000bcd2 in PyObject_Call ()
#11 0x000000010000f825 in PyObject_CallFunction ()
#12 0x00000001000d209b in PyImport_Import ()
#13 0x000000010238cfeb in __Pyx_ImportModule [inlined] () at /Applications/sage_builds/sage-4.6.alpha0-upgrade/devel/sage-main/sage/rings/complex_double.c:15716
#14 0x000000010238cfeb in __Pyx_ImportType (module_name=0x1023a8eb2 "sage.libs.pari.gen", class_name=0x1023a825b "gen", size=56, strict=1) at sage/rings/complex_double.c:15660
#15 0x00000001023a3463 in initcomplex_double () at sage/rings/complex_double.c:14241
#16 0x00000001000d2e11 in _PyImport_LoadDynamicModule ()
#17 0x00000001000d10bf in import_submodule ()
#18 0x00000001000d15da in load_next ()
#19 0x00000001000d1932 in PyImport_ImportModuleLevel ()
#20 0x00000001000aeef3 in builtin___import__ ()
#21 0x000000010000bcd2 in PyObject_Call ()
#22 0x00000001000b0147 in PyEval_CallObjectWithKeywords ()
#23 0x00000001000b440e in PyEval_EvalFrameEx ()
#24 0x00000001000b9010 in PyEval_EvalCodeEx ()
#25 0x00000001000b90f6 in PyEval_EvalCode ()
#26 0x00000001000cdfb0 in PyImport_ExecCodeModuleEx ()
#27 0x00000001000cf212 in load_source_module ()
#28 0x00000001000d10bf in import_submodule ()
#29 0x00000001000d15da in load_next ()
#30 0x00000001000d1932 in PyImport_ImportModuleLevel ()
#31 0x00000001000aeef3 in builtin___import__ ()
#32 0x000000010000bcd2 in PyObject_Call ()
#33 0x00000001000b0147 in PyEval_CallObjectWithKeywords ()
#34 0x00000001000b440e in PyEval_EvalFrameEx ()
#35 0x00000001000b9010 in PyEval_EvalCodeEx ()
#36 0x00000001000b90f6 in PyEval_EvalCode ()
#37 0x00000001000cdfb0 in PyImport_ExecCodeModuleEx ()
#38 0x00000001000cf212 in load_source_module ()
#39 0x00000001000d10bf in import_submodule ()
#40 0x00000001000d15da in load_next ()
#41 0x00000001000d18ec in PyImport_ImportModuleLevel ()
#42 0x00000001000aeef3 in builtin___import__ ()
#43 0x000000010000bcd2 in PyObject_Call ()
#44 0x00000001000b0147 in PyEval_CallObjectWithKeywords ()
#45 0x00000001000b440e in PyEval_EvalFrameEx ()
#46 0x00000001000b9010 in PyEval_EvalCodeEx ()
#47 0x00000001000b90f6 in PyEval_EvalCode ()
#48 0x00000001000cdfb0 in PyImport_ExecCodeModuleEx ()
#49 0x00000001000cf212 in load_source_module ()
#50 0x00000001000d10bf in import_submodule ()
#51 0x00000001000d15da in load_next ()
#52 0x00000001000d1932 in PyImport_ImportModuleLevel ()
#53 0x00000001000aeef3 in builtin___import__ ()
#54 0x000000010000bcd2 in PyObject_Call ()
#55 0x00000001000b0147 in PyEval_CallObjectWithKeywords ()
#56 0x00000001000b440e in PyEval_EvalFrameEx ()
#57 0x00000001000b9010 in PyEval_EvalCodeEx ()
#58 0x00000001000b90f6 in PyEval_EvalCode ()
#59 0x00000001000cdfb0 in PyImport_ExecCodeModuleEx ()
#60 0x00000001000cf212 in load_source_module ()
#61 0x00000001000d10bf in import_submodule ()
#62 0x00000001000d15da in load_next ()
#63 0x00000001000d1932 in PyImport_ImportModuleLevel ()
#64 0x00000001000aeef3 in builtin___import__ ()
#65 0x000000010000bcd2 in PyObject_Call ()
#66 0x00000001000b0147 in PyEval_CallObjectWithKeywords ()
#67 0x00000001000b440e in PyEval_EvalFrameEx ()
#68 0x00000001000b9010 in PyEval_EvalCodeEx ()
#69 0x00000001000b90f6 in PyEval_EvalCode ()
#70 0x00000001000cdfb0 in PyImport_ExecCodeModuleEx ()
#71 0x00000001000cf212 in load_source_module ()
#72 0x00000001000d10bf in import_submodule ()
#73 0x00000001000d15da in load_next ()
#74 0x00000001000d1932 in PyImport_ImportModuleLevel ()
#75 0x00000001000aeef3 in builtin___import__ ()
#76 0x000000010000bcd2 in PyObject_Call ()
#77 0x00000001000b0147 in PyEval_CallObjectWithKeywords ()
#78 0x00000001000b440e in PyEval_EvalFrameEx ()
#79 0x00000001000b9010 in PyEval_EvalCodeEx ()
#80 0x00000001000b90f6 in PyEval_EvalCode ()
#81 0x00000001000cdfb0 in PyImport_ExecCodeModuleEx ()
#82 0x00000001000cf212 in load_source_module ()
#83 0x00000001000d10bf in import_submodule ()
#84 0x00000001000d15da in load_next ()
#85 0x00000001000d18ec in PyImport_ImportModuleLevel ()
#86 0x00000001000aeef3 in builtin___import__ ()
#87 0x00000001000b82b8 in PyEval_EvalFrameEx ()
#88 0x00000001000b745a in PyEval_EvalFrameEx ()
#89 0x00000001000b9010 in PyEval_EvalCodeEx ()
#90 0x00000001000b6ffd in PyEval_EvalFrameEx ()
#91 0x00000001000b9010 in PyEval_EvalCodeEx ()
#92 0x000000010003b0ad in function_call ()
#93 0x000000010000bcd2 in PyObject_Call ()
#94 0x000000010001dd0d in instancemethod_call ()
#95 0x000000010000bcd2 in PyObject_Call ()
#96 0x00000001000b0147 in PyEval_CallObjectWithKeywords ()
#97 0x0000000100020d0e in PyInstance_New ()
#98 0x000000010000bcd2 in PyObject_Call ()
#99 0x00000001000b457e in PyEval_EvalFrameEx ()
#100 0x00000001000b9010 in PyEval_EvalCodeEx ()
#101 0x00000001000b6ffd in PyEval_EvalFrameEx ()
#102 0x00000001000b9010 in PyEval_EvalCodeEx ()
#103 0x00000001000b90f6 in PyEval_EvalCode ()
#104 0x00000001000dde0e in PyRun_FileExFlags ()
#105 0x00000001000de0c9 in PyRun_SimpleFileExFlags ()
#106 0x00000001000eb5eb in Py_Main ()
#107 0x0000000100000f14 in start ()
```



---

Comment by leif created at 2010-09-12 02:05:10

John, can you provide a link to the full PARI spkg install log?

I also wonder if somehow PARI uses parts of its old installation (in `$SAGE_LOCAL/{lib,include/pari}/`) during the build (which one would not necessarily see in the log though). It would be safer to delete all these files prior to upgrading...

Does the stand-alone interpreter work?


---

Comment by jhpalmieri created at 2010-09-12 02:23:17

I found the problem, I think, thanks to one of your questions on [sage-release](http://groups.google.com/group/sage-release/browse_frm/thread/57d92da34ef89e69): in local/lib, I have

```
  -rwxr-xr-x    1 palmieri  admin   5249848 Sep 11 18:39 libpari-gmp-2.4.dylib
  -rwxr-xr-x    1 palmieri  admin   3487624 Sep  8 21:53 libpari-gmp.dylib
  -rw-r--r--    1 palmieri  admin  21398976 Sep 11 18:39 libpari.a
  -rwxr-xr-x    1 palmieri  admin   5249848 Sep 11 18:39 libpari.dylib
```

Note the time-stamp on the file libpari-gmp.dylib: this is from the old PARI installation.  If I get rid of this file and then link libpari-gmp-2.4.dylib to libpari-gmp.dylib, then Sage starts with no trouble.  If I just delete the file, then Sage complains

```
ImportError: dlopen(/Applications/sage_builds/sage-4.6.alpha0-upgrade/local/lib/python2.6/site-packages/sage/rings/complex_double.so, 2): Library not loaded: libpari-gmp.dylib
```

I also get the complaint after running "sage -ba".  I don't see anything in the PARI install log about libpari-gmp.dylib, just libpari-gmp-2.4.dylib, so I'm a little confused about whether this link should be here.  Two things I might try next: running tests with the link, or deleting the old dylib file and then running "sage -upgrade ..." to see if that helps.


---

Comment by jhpalmieri created at 2010-09-12 02:26:02

The time stamps on pariport.h, paritype.h, and paripriv.h are all old, too.


---

Comment by leif created at 2010-09-12 04:00:59

Some part in John's build must have been linked against `libpari.*` when this still was a copy of / symbolic link to the old `libpari-gmp.*`, s.t. the old soname got recorded, and all PARI symbols were resolved from there before `libpari-gmp-2.4.*` was considered.

`libcsage.*` is IMHO a good candidate... Did this really get updated in `local/lib`, i.e. got `devel/sage/c_lib/libcsage.*` rebuilt?


---

Comment by jhpalmieri created at 2010-09-12 04:43:31

> Two things I might try next: running tests with the link, or deleting the old dylib file and then running "sage -upgrade ..." to see if that helps.

I did these on two different machines.  With the link, all tests passed.  Deleting the old dylib file (and the old include files, just for kicks) and then upgrading caused problems: `ImportError` as above.

> libcsage.* is IMHO a good candidate... Did this really get updated in local/lib, i.e. got devel/sage/c_lib/libcsage.* rebuilt?

Yes, it did.  After taking a clean 4.5.3 install and upgrading, here are the recent files in local/lib:

```
  lrwxr-xr-x    1 palmieri  admin        37 Sep 11 21:32 libcsage.dylib -> ../../devel/sage/c_lib/libcsage.dylib
  -rwxr-xr-x    1 palmieri  admin     77488 Sep 11 21:32 libLfunction.so
  -rwxr-xr-x    1 palmieri  admin   5249848 Sep 11 21:31 libpari-gmp-2.4.dylib
  -rw-r--r--    1 palmieri  admin  21398976 Sep 11 21:31 libpari.a
  -rwxr-xr-x    1 palmieri  admin   5249848 Sep 11 21:31 libpari.dylib
```

Here is the file to which libcsage.dylib links:

```
  -rwxr-xr-x   1 palmieri  admin    83864 Sep 11 21:32 libcsage.dylib
```

The rest of the libraries in local/lib are old enough that they must have come from 4.5.3.


---

Comment by leif created at 2010-09-13 11:23:18

Justin reported successful upgrade from 4.5.3 on MacOS X 10.*5.8* on sage-release, though some doctests fail.


---

Comment by leif created at 2010-09-13 12:27:16

Replying to [comment:14 leif]:
> Justin reported successful upgrade from 4.5.3 on MacOS X 10.*5.8* on sage-release, though some doctests fail.

(... due to `eclib` not getting rebuilt.)


---

Comment by leif created at 2010-09-14 18:09:33

Necessary steps to properly upgrade (from Sage 4.5.3) to Sage 4.6.alpha0:
 * Build Sage 4.5.3 from scratch ;-)
 * Run `./sage -upgrade http://sage.math.washington.edu/home/release/sage-4.6.alpha0/sage-4.6.alpha0/` 

 (Unfortunately, modifying `spkg/standard/deps` before doing so doesn't help since this file gets overwritten during upgrade.)
 * Run `./sage -f eclib-20100711` (just to record the *new* PARI shared library name in its various shared libraries).
 * Touch the Sage library files that have to be rebuilt for the same reason:
   {{{#!sh
touch devel/sage/sage/libs/cremona/homspace.pyx 
touch devel/sage/sage/libs/cremona/newforms.pyx 
touch devel/sage/sage/libs/mwrank/mwrank.pyx 
}}}
   (Three command invocations just to make it readable without horizontal scrolling.)
 * Run `./sage -b` to rebuild them (i.e., their respective Python modules / shared libraries).

Deleting the old PARI shared library files (`local/lib/libpari-gmp.*`) is not necessary, but will trigger Sage import errors if you omit one of the above steps... (unless you have a system-wide PARI library installed which matches the old version, i.e. 2.3.*)


---

Comment by jhpalmieri created at 2010-09-14 20:02:35

> Necessary steps to properly upgrade (from Sage 4.5.3) to Sage 4.6.alpha0:

This didn't work for me; I get the same segmentation fault message.  (I think that when I tried "sage -ba" before, that would have rebuilt the files from all the pyx files, so I guess it's not a surprise that this failed.)


---

Comment by leif created at 2010-09-14 20:05:06

I consider the "`touch` issue" a bug in `module_list.py`, since PARI is not directly used by those extension modules (but listed in their `libraries`, and therefore gets recorded in the list of needed libraries).

Explicitly linking against PARI would then only be necessary if we built some _statically_ linked executable. Or is this also required on some systems like Cygwin? If so, we should make use of `uname_specific()` there, too.


---

Comment by leif created at 2010-09-14 20:05:06

Changing status from new to needs_info.


---

Comment by leif created at 2010-09-14 20:15:46

Replying to [comment:17 jhpalmieri]:
> > Necessary steps to properly upgrade (from Sage 4.5.3) to Sage 4.6.alpha0:
> 
> This didn't work for me; I get the same segmentation fault message.  (I think that when I tried "sage -ba" before, that would have rebuilt the files from all the pyx files, so I guess it's not a surprise that this failed.)

Must be some bad environment... ;-)

Does `gp` work (after upgrading)?


---

Comment by jhpalmieri created at 2010-09-14 20:24:59

> Does gp work (after upgrading)?

`./sage -gp` starts up and can execute simple calculations.  No segfault.


---

Comment by leif created at 2010-09-14 20:32:46

And what import errors do you now get after deleting the old PARI's dylibs (`libpari-gmp.*`)?


---

Comment by leif created at 2010-09-14 20:48:28

For me (Ubuntu 10.04 x86_64), upgrading with the above steps passes `ptestlong` with the original `module_list.py`, and also after deleting `"pari"` from the library lists of the mentioned extension modules, then again touching the `.pyx` files and running `./sage -b`.


---

Comment by jhpalmieri created at 2010-09-14 21:09:36

After going through the above steps, if I also delete the old libpari-gmp, then I get

```
ImportError: dlopen(/Applications/sage_builds/sage-4.6.alpha0-upgrade/local/lib/python2.6/site-packages/sage/rings/complex_double.so, 2): Library not loaded: libpari-gmp.dylib
  Referenced from: /Applications/sage_builds/sage-4.6.alpha0-upgrade/local/lib/python2.6/site-packages/sage/rings/complex_double.so
  Reason: image not found
```

If I touch complex_double.pyx and "sage -b", there is no change.  Touching all of the py, pyx, and pxd files in the libs/pari directory also triggers a rebuild of complex_double.pyx, and also doesn't help.


---

Comment by leif created at 2010-09-14 21:36:58

And the files in `.../local/lib/python2.6/site-packages/...` got properly updated?!?

Can you attach a log of the `./sage -b` run?

The only (other) thing I could imagine is some old PARI library in the linker/loader search path _during linking_, but not at run-time (i.e. dynamic loader search path). (Really) Environment issue?


---

Comment by jhpalmieri created at 2010-09-14 22:34:36

Replying to [comment:24 leif]:
> And the files in `.../local/lib/python2.6/site-packages/...` got properly updated?!?

According to the time stamps, yes.

> Can you attach a log of the `./sage -b` run?

Which one?  Here's what happens if I follow your instructions, delete libpari-gmp.dylib, and touch complex_double.pyx:

```
$ ./sage -b

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Building modified file sage/rings/complex_double.pyx.
Execute 1 commands (using 1 threads)
python `which cython` --embed-positions --directive cdivision=True -I/Applications/sage_builds/sage-4.6.alpha0-upgrade/devel/sage-main -o sage/rings/complex_double.c sage/rings/complex_double.pyx
sage/rings/complex_double.pyx --> /Applications/sage_builds/sage-4.6.alpha0-upgrade/local//lib/python/site-packages//sage/rings/complex_double.pyx
Time to execute 1 commands: 4.32504701614 seconds
Finished compiling Cython code (time = 4.87559199333 seconds)
running install
running build
running build_py
running build_ext
building 'sage.rings.complex_double' extension
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Applications/sage_builds/sage-4.6.alpha0-upgrade/local//include -I/Applications/sage_builds/sage-4.6.alpha0-upgrade/local//include/csage -I/Applications/sage_builds/sage-4.6.alpha0-upgrade/devel//sage/sage/ext -I/Applications/sage_builds/sage-4.6.alpha0-upgrade/local/include/python2.6 -c sage/rings/complex_double.c -o build/temp.macosx-10.6-i386-2.6/sage/rings/complex_double.o -std=c99 -D_XPG6 -w
gcc -L/Applications/sage_builds/sage-4.5.3/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.6-i386-2.6/sage/rings/complex_double.o -L/Applications/sage_builds/sage-4.6.alpha0-upgrade/local//lib -lcsage -lgsl -lcblas -latlas -lpari -lgmp -lm -lstdc++ -lntl -o build/lib.macosx-10.6-i386-2.6/sage/rings/complex_double.so
Total time spent compiling C/C++ extensions:  7.72538805008 seconds.
running install_lib
copying build/lib.macosx-10.6-i386-2.6/sage/rings/complex_double.so -> /Applications/sage_builds/sage-4.6.alpha0-upgrade/local/lib/python2.6/site-packages/sage/rings
running install_egg_info
Removing /Applications/sage_builds/sage-4.6.alpha0-upgrade/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /Applications/sage_builds/sage-4.6.alpha0-upgrade/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info

real	0m13.963s
user	0m12.678s
sys	0m1.095s
```


> The only (other) thing I could imagine is some old PARI library in the linker/loader search path _during linking_, but not at run-time (i.e. dynamic loader search path). (Really) Environment issue?

Well, I see it on two different machines. I don't have LD_LIBRARY_PATH or DYLD_LIBRARY_PATH set, and when I run "./sage -sh", I don't see anything odd in those variables.  I've posted what I get from "export" ordinarily and also after running "./sage -sh" at [http://sage.math.washington.edu/home/palmieri/misc/env.txt](http://sage.math.washington.edu/home/palmieri/misc/env.txt).  I'm going to try this all on bsd.math, which involves building sage 4.5.3 first, so it will take a while.  I've hardly used that machine, so my environment there is pretty vanilla.


---

Comment by leif created at 2010-09-14 22:50:26


```
gcc -L/Applications/sage_builds/sage-4.5.3/local/lib -bundle -undefined
 dynamic_lookup build/temp.macosx-10.6-i386-2.6/sage/rings/complex_double.o
 -L/Applications/sage_builds/sage-4.6.alpha0-upgrade/local//lib -lcsage
 -lgsl -lcblas -latlas -lpari -lgmp -lm -lstdc++ -lntl -o
 build/lib.macosx-10.6-i386-2.6/sage/rings/complex_double.so
```


That's what I was thinking of. Looks as if the linker also (first!) searches the old lib dir.

You renamed the directory of the upgrade / copied the Sage tree to a new directory...

Could you temporarily rename the 4.5.3 directory and rerun `./sage -b` (after again touching Cython files)?

(I assume `/Applications/sage_builds/sage-4.5.3` still exists.)


---

Comment by jhpalmieri created at 2010-09-14 23:07:26

Replying to [comment:26 leif]:
> You renamed the directory of the upgrade / copied the Sage tree to a new directory...

Yes, I copied it.  I always do this so if the upgrade screws up, I still have a working copy of Sage.
 
> Could you temporarily rename the 4.5.3 directory and rerun `./sage -b` (after again touching Cython files)?

Okay, I did that.  Here's part of the log from "./sage -b".  Note the warning, since I renamed the directory:

```
gcc -L/Applications/sage_builds/sage-4.5.3/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.6-i386-2.6/sage/rings/complex_double.o -L/Applications/sage_builds/sage-4.6.alpha0-upgrade/local//lib -lcsage -lgsl -lcblas -latlas -lpari -lgmp -lm -lstdc++ -lntl -o build/lib.macosx-10.6-i386-2.6/sage/rings/complex_double.so
ld: warning: directory '/Applications/sage_builds/sage-4.5.3/local/lib' following -L not found
Total time spent compiling C/C++ extensions:  9.04102396965 seconds.
running install_lib
copying build/lib.macosx-10.6-i386-2.6/sage/rings/complex_double.so -> /Applications/sage_builds/sage-4.6.alpha0-upgrade/local/lib/python2.6/site-packages/sage/rings
running install_egg_info
Removing /Applications/sage_builds/sage-4.6.alpha0-upgrade/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /Applications/sage_builds/sage-4.6.alpha0-upgrade/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
```

I still get the import error, unfortunately.


---

Comment by leif created at 2010-09-14 23:13:29

Replying to [comment:27 jhpalmieri]:
> I still get the import error, unfortunately.

Hopefully now from a different import?


---

Comment by jhpalmieri created at 2010-09-14 23:15:56

Ah, if I touch libs/pari/gen.pxd and then do "./sage -b", it starts without an error.  That seems to clear up all of the dependencies.


---

Comment by jhpalmieri created at 2010-09-14 23:27:48

So I think I need to delete the old libpari-gmp library, move the old Sage directory, touch 

 - devel/sage/sage/libs/cremona/homspace.pyx 
 - devel/sage/sage/libs/cremona/newforms.pyx 
 - devel/sage/sage/libs/mwrank/mwrank.pyx 
 - devel/sage/sage/libs/pari/gen.pxd

and then run "./sage -b".  Simple.


---

Comment by leif created at 2010-09-14 23:29:35

I still hate trac...

Hmmm, the preprocessor supports `-I-`, unfortunately the linker not `-L-`, so we have to modify the dumb Python default compiler settings to get rid of obsolete directories...


---

Comment by leif created at 2010-09-14 23:31:50

Replying to [comment:30 jhpalmieri]:
> So I think I need to delete the old libpari-gmp library, move the old Sage directory, touch 
>  ...
>  - devel/sage/sage/libs/pari/gen.pxd

The latter shouldn't be necessary.

 
> Simple.

;-) How many users will agree on that?


---

Comment by leif created at 2010-09-14 23:41:22

Also looks like a Python on Darwin bug; I have the opposite order of linker search directories.


---

Comment by jhpalmieri created at 2010-09-14 23:59:54

> The latter shouldn't be necessary.

I guess you're right.

Wouldn't it be easier for upgrading to see if libpari-gmp.dylib exists, and if so, delete it and then link libpari-gmp-2.4.dylib to it?

By the way, on a linux box I see libpari-gmp.so.2 and libpari-gmp.so.2.3.5 lying around from the old install.  They don't seem to cause any trouble, but should they be removed also?


---

Comment by leif created at 2010-09-15 00:19:02

Replying to [comment:34 jhpalmieri]:
> Wouldn't it be easier for upgrading to see if libpari-gmp.dylib exists, and if so, delete it and then link libpari-gmp-2.4.dylib to it?

I was thinking of fixing this in general, not a specific work-around limited to updating to _this_ release.

> By the way, on a linux box I see libpari-gmp.so.2 and libpari-gmp.so.2.3.5 lying around from the old install.  They don't seem to cause any trouble, but should they be removed also?

As I said, on Linux we seem to have the correct order of library search dirs, so if all necessary files actually get rebuilt, the old libs shouldn't cause problems. In fact, you can use both versions "at the same time" (on Linux), i.e. some Sage modules using the old, and some the new version. The Darwin loader doesn't support this, at least with how the modules are currently built on Darwin.

For the directory renaming issue (perhaps typical for upgrades, but not limited to):

```python
distutils.sysconfig.get_config_vars()["LDFLAGS"]="" # remove potentially obsolete "-L$SAGE_LOCAL/lib"
```

(To be added to `devel/sage/setup.py`; doesn't hurt on normal installations where it is redundant anyway.)


---

Comment by leif created at 2010-09-15 00:25:11

Replying to [comment:35 leif]:
>

```python
distutils.sysconfig.get_config_vars()["LDFLAGS"]="" # remove potentially obsolete "-L$SAGE_LOCAL/lib"
```


_In theory..._ We have to re-customize the compiler.


---

Comment by jhpalmieri created at 2010-09-15 01:08:49

I'm not sure where the 4.5.3 is coming from.  If I do `./sage -ipython`:

```
In [1]: import distutils.sysconfig

In [2]: s=''.join([str(x) for x in distutils.sysconfig.get_config_vars().values()])

In [3]: s.find('4.5')
Out[3]: -1
```

So the string '4.5' is not in any value of any variable listed by `get_config_vars`.  (By inspection it wasn't in LDFLAGS.)  I'm assuming that running `./sage -ipython` sets all of the variables the same way as during the `./sage -b` process, but I suppose this could be wrong.

So where does 4.5.3 come from?  Is there some file which stores it which needs to be rebuilt?  I notice that devel/sage/module_list.pyc is old and seems to refer to the absolute path, but rebuilding it didn't help.  Any other ideas?


---

Comment by jhpalmieri created at 2010-09-15 01:14:59

I'm sorry, that's wrong, I was running it on the wrong machine.  4.5.3 appears in lots of places:

```
 'BINDIR': '/Applications/sage_builds/sage-4.5.3/local/bin',
 'BINLIBDEST': '/Applications/sage_builds/sage-4.5.3/local/lib/python2.6',
 'BLDSHARED': 'gcc -L/Applications/sage_builds/sage-4.5.3/local/lib -bundle -undefined dynamic_lookup',
 'CONFIG_ARGS': "'--enable-shared' '--prefix=/Applications/sage_builds/sage-4.5.3/local' '--enable-unicode=ucs4' '--disable-toolbox-glue' 'CC=gcc' 'LDFLAGS=-L/Applications/sage_builds/sage-4.5.3/local/lib ' 'CPPFLAGS=-I/Applications/sage_builds/sage-4.5.3/local/include '",
 'CONFINCLUDEDIR': '/Applications/sage_builds/sage-4.5.3/local/include',
 'CONFINCLUDEPY': '/Applications/sage_builds/sage-4.5.3/local/include/python2.6',
 'CPPFLAGS': '-I. -IInclude -I./Include -I/Applications/sage_builds/sage-4.5.3/local/include',
 'DESTDIRS': '/Applications/sage_builds/sage-4.5.3/local /Applications/sage_builds/sage-4.5.3/local/lib /Applications/sage_builds/sage-4.5.3/local/lib/python2.6 /Applications/sage_builds/sage-4.5.3/local/lib/python2.6/lib-dynload',
 'DESTLIB': '/Applications/sage_builds/sage-4.5.3/local/lib/python2.6',
 'DESTSHARED': '/Applications/sage_builds/sage-4.5.3/local/lib/python2.6/lib-dynload'
 'INCLDIRSTOMAKE': '/Applications/sage_builds/sage-4.5.3/local/include /Applications/sage_builds/sage-4.5.3/local/include /Applications/sage_builds/sage-4.5.3/local/include/python2.6 /Applications/sage_builds/sage-4.5.3/local/include/python2.6',
 'INCLUDEDIR': '/Applications/sage_builds/sage-4.5.3/local/include',
 'INCLUDEPY': '/Applications/sage_builds/sage-4.5.3/local/include/python2.6',
 'LDFLAGS': '-L/Applications/sage_builds/sage-4.5.3/local/lib',
 'LDSHARED': 'gcc -L/Applications/sage_builds/sage-4.5.3/local/lib -bundle -undefined dynamic_lookup',
 'LIBDEST': '/Applications/sage_builds/sage-4.5.3/local/lib/python2.6'
 'LIBDIR': '/Applications/sage_builds/sage-4.5.3/local/lib'
 'LIBP': '/Applications/sage_builds/sage-4.5.3/local/lib/python2.6'
 'LIBPL': '/Applications/sage_builds/sage-4.5.3/local/lib/python2.6/config'
 'MACHDESTLIB': '/Applications/sage_builds/sage-4.5.3/local/lib/python2.6'
 'MANDIR': '/Applications/sage_builds/sage-4.5.3/local/share/man'
 'PY_CFLAGS': '-fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I. -IInclude -I./Include -I/Applications/sage_builds/sage-4.5.3/local/include  -DPy_BUILD_CORE'
 'SCRIPTDIR': '/Applications/sage_builds/sage-4.5.3/local/lib'
```



---

Comment by leif created at 2010-09-15 01:55:13

I can get rid of the second dir by adding the following line in `devel/sage/setup.py`:

```python
        self.compiler.set_library_dirs([]) # may have contained obsolete ones

        self.compiler.link_shared_object(
        ...
```


But your `LDSHARED` looks bad; mine is just

```
'gcc -march=native -O3 -fno-strict-aliasing -fomit-frame-pointer -DHONORS_CFLAGS -pthread -shared'
```

or simply (the relevant part)

```
'gcc -pthread -shared'
```



---

Comment by leif created at 2010-09-15 02:27:03

You can also replace or modify the linker command (for shared libraries) in `setup.py` by e.g.

```python
        self.compiler.linker_so=["gcc","-shared","-pthread"] # Linux

        self.compiler.link_shared_object(
        ...
```

In your case, perhaps just delete the second list element (`"-L/..."`).

Similar things have perhaps to be done for other commands and args / parameters.


---

Comment by jhpalmieri created at 2010-09-15 03:57:47

Maybe doing the equivalent of `export LDSHARED='gcc -bundle -undefined dynamic_lookup'` will do it.  Actually running that in the shell, then touching a bunch of pyx files and typing "./sage -b", produces a version of sage which starts up without an import error.  It seems to use the correct command when building the Sage library files, and in distutils.sysconfig.customize_compiler, it says

```
        if 'LDSHARED' in os.environ:
            ldshared = os.environ['LDSHARED']
```

I wish we knew why this is getting set wrong...


---

Comment by leif created at 2010-09-16 11:07:45

Replying to [comment:18 leif]:
> I consider the "`touch` issue" a bug in `module_list.py`, since PARI is not directly used by those extension modules (but listed in their `libraries`, and therefore gets recorded in the list of needed libraries).

I've opened #9914 to fix this; minimal patch up there, needs review.

(Note that these extension modules also did not get rebuilt because they *don't* [directly] depend on PARI, despite that fact linked against it. Unless one links with `--as-needed`, which isn't very portable, the - _potentially later obsolete_ - PARI library unnecessarily gets recorded as a prerequisite for those extension modules.)


---

Comment by kcrisman created at 2010-09-22 02:09:14

I have another possible data point.  I upgraded to 4.6.alpha1 (not alpha0) from 4.5.3 on OS X 10.6, and all seems well, except for failing doctests in `schemes/elliptic_curves/ell_rational_field.py` and `libs/mwrank/interface.py`.  Both errors are in mwrank.

I have an updated Pynac (which would be time-consuming to revert) on this installation, which I suppose could have something to do with this.  But this seems fairly unlikely to me, so I thought I'd ask if anyone had tried the new upgrade possibility and seen something similar.


---

Comment by kcrisman created at 2010-09-22 02:28:32

I should point out that the errors look like the ones here, segmentation fault in Pari and all that.  It's not the computer I'm on right now, so I won't laboriously type it all out.

For what it's worth, I get

```

sage -t  "devel/sage/sage/libs/mwrank/interface.py"         
The doctested process was killed by signal 4
         [199.7 s]
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
The doctested process was killed by signal 4
         [337.5 s]
 
```

on OS X 10.4 with this same upgrade pattern, and without the new Pynac.  Also curious.


---

Comment by leif created at 2010-09-22 03:25:38

Replying to [comment:44 kcrisman]:
> I should point out that the errors look like the ones here, segmentation fault in Pari and all that.  It's not the computer I'm on right now, so I won't laboriously type it all out.
> 
> For what it's worth, I get

```

sage -t  "devel/sage/sage/libs/mwrank/interface.py"         
The doctested process was killed by signal 4
         [199.7 s]
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
The doctested process was killed by signal 4
         [337.5 s]
 
```

> on OS X 10.4 with this same upgrade pattern, and without the new Pynac.  Also curious.

Hmmm, not that surprising, except that signal 4 is "illegal instruction", not a segmentation fault (but perhaps Apple uses different numbers on Darwin 8).

Did you
 * rebuild ECLIB (with `./sage -f ...`) (depends on PARI)
 * rename or copy the 4.5.3 directory? 

As mentioned above, three extension modules do *not* get rebuilt though they link against PARI (and depend on ECLIB).

In case you copied the directory to keep the 4.5.3 installation, the linker on Darwin will *first* search `$SAGE_LOCAL/lib` of the *old* Sage installation, and therefore link against the wrong PARI library. You can export `LDSHARED` to prevent this (see above).

I'm not sure if the setting differs on MacOS X 10.4, so you could do:

```
sage: import distutils.sysconfig
sage: distutils.sysconfig.get_config_var("LDSHARED")
' (current setting) '
```

and set `LDSHARED` to what you see except the first `-L...` (and export it).

Then force rebuilding ECLIB, touch the three Cython files listed above and do `./sage -b`.


I - hate - trac ... 8| (once again just logged me off when replying s.t. my whole comment went to /dev/null)


---

Comment by kcrisman created at 2010-09-22 12:54:27

> Did you
>  * rebuild ECLIB (with `./sage -f ...`) (depends on PARI)
>  * rename or copy the 4.5.3 directory? 
Nope - like I said, it was a data point.
> Then force rebuilding ECLIB, touch the three Cython files listed above and do `./sage -b`.
I'll try this.


---

Comment by kcrisman created at 2010-09-22 14:34:11

> > Then force rebuilding ECLIB, touch the three Cython files listed above and do `./sage -b`.
> I'll try this.

Yup, this fixed it.  I hope you figure out how to fix this before 4.6 is released!  A lot of our clientele is likely to have precisely this platform.


---

Comment by leif created at 2010-09-22 15:32:06

Karl-Dieter, could you add another data point, the output of

```
distutils.sysconfig.get_config_var("LDSHARED")
```

on your MacOS X 10.*4* box? (Just to make sure it doesn't differ much from the settings on 10.5 and 10.6.)

Btw, "illegal instruction" errors (signal 4) are also reasonable when the wrong PARI library is used, since memory might get corrupted and function pointers may point to some arbitrary location.

This upgrade problem isn't that hard to fix (since we now know the two rather unrelated causes), but I think I'll open a follow-up ticket for the necessary patches.


---

Comment by leif created at 2010-09-22 17:52:42

Replying to [comment:11 jhpalmieri]:
> The time stamps on pariport.h, paritype.h, and paripriv.h are all old, too.

Just for the record: `paripriv.h` is a patched Sage version which is copied with `-p` on Darwin, but that's in general ok (though we don't preserve the file attributes, including the modification time, on others systems).


---

Comment by drkirkby created at 2010-09-22 21:38:19

Replying to [comment:49 leif]:
> Replying to [comment:11 jhpalmieri]:
> > The time stamps on pariport.h, paritype.h, and paripriv.h are all old, too.
> 
> Just for the record: `paripriv.h` is a patched Sage version which is copied with `-p` on Darwin, but that's in general ok (though we don't preserve the file attributes, including the modification time, on others systems).

The file `paripriv.h` is also patched on Solaris. 

Note William told me the file should be private to Pari (hence the "priv" in the name), so he is not surprised it needs patching for OS X and Solaris. 

I don't actually understand what this file does, but I rather get the feeling it is a hack of some sort.


---

Comment by leif created at 2010-09-22 23:35:38

Replying to [comment:50 drkirkby]:
> The file `paripriv.h` is also patched on Solaris.

The patched version only avoids a single name clash on MacOS X and Solaris.  

> I don't actually understand what this file does, but I rather get the feeling it is a hack of some sort. 

It defines more lower-level structures and functions of PARI that we use in `sage/libs/pari/gen.pyx`, the Python/Cython PARI _library_ interface.


---

Comment by kcrisman created at 2010-09-23 00:13:24

Replying to [comment:48 leif]:
> Karl-Dieter, could you add another data point, the output of
> {{{
> distutils.sysconfig.get_config_var("LDSHARED")
> }}}
> on your MacOS X 10.*4* box? (Just to make sure it doesn't differ much from the settings on 10.5 and 10.6.)
> 

```
sage: import distutils
sage: distutils.sysconfig.get_config_var("LDSHARED")
'gcc -L/Users/crisman/Desktop/sage-4.5.3/local/lib -bundle -undefined dynamic_lookup'
```

Incidentally, I already changed the name of that folder to sage-4.6.alpha1, so that by itself is a little unsettling...


---

Comment by kcrisman created at 2010-09-23 00:59:19

Replying to [comment:45 leif]:
> Replying to [comment:44 kcrisman]:
> > I should point out that the errors look like the ones here, segmentation fault in Pari and all that.  It's not the computer I'm on right now, so I won't laboriously type it all out.
> > 
> > For what it's worth, I get
> {{{
> 
> sage -t  "devel/sage/sage/libs/mwrank/interface.py"         
> The doctested process was killed by signal 4
>          [199.7 s]
> sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
> The doctested process was killed by signal 4
>          [337.5 s]
>  
> }}}

Ok, did everything right and 

```
sage -t  "devel/sage/sage/libs/mwrank/interface.py"         
         [50.8 s]
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
         [279.7 s]
 
----------------------------------------------------------------------
All tests passed!
```

Thanks!


---

Comment by leif created at 2010-09-23 04:18:02

Sage library patch. Fixes the relevant extension module dependencies. Based on Sage 4.6.alpha1.


---

Attachment

Scripts repo patch (to sage-upgrade). Based on Sage 4.6.alpha1.


---

Comment by leif created at 2010-09-23 06:50:38

New `spkg/standard/deps`. Based on Sage 4.6.alpha1. (Not under revision control.)


---

Attachment

Diff of new `spkg/standard/deps` against that of Sage 4.6.alpha1.


---

Comment by leif created at 2010-09-23 07:51:34

Changing keywords from "" to "upgrade update dependencies PARI NewPARI".


---

Comment by leif created at 2010-09-23 07:51:34

Changing status from needs_info to needs_review.


---

Comment by leif created at 2010-09-23 07:51:34

I've attached a few patches / files and their diffs that make upgrading from Sage < 4.6 (i.e. to the new PARI) work.

I think this is a general improvement (not limited to PARI upgrade), though for e.g. the GMP/MPIR 2.1.2 upgrade (see #8664), more dependencies (or some other mechanism) have to be added to `module_list.py` to properly rebuild the Sage _library_ (i.e. *all* _extension modules_ that depend on MPIR). Sage _packages_ depending on an upgraded spkg will now get rebuilt without the need to download unmodified "new" versions (with just the patch level bumped in order to get them rebuilt).

I'm setting this to "needs review", though I've not yet uploaded a patch to get around the specific _Darwin_ linker problem (but I'll provide one later).

When doing an "in-place" upgrade (i.e. keeping the old directory name), the current patches should also fully work on MacOS X. A work-around to the linker problem (i.e. when the Sage to be upgraded is located in a new directory) is manually setting (and exporting) `LDSHARED` to the output of `distutils.sysconfig.get_config_var("LDSHARED")` with the second "word" (`-L...`) either dropped or replaced by `-L` immediately followed by `$SAGE_ROOT/local/lib` (with `$SAGE_ROOT` the actual directory name, not the environment variable; see also comments above for more details).

Unfortunately we'll have to set up a Sage package server (or a special directory on e.g. `www.sagemath.org`) to "fully" test this, i.e. by _really_ running `sage -upgrade`.

On the other hand, the changes are quite small such that they should easily be reviewed. The behavior can be tested by e.g. running `make` with `SAGE_UPGRADING` set to "yes", faking some spkg was new (to see that all dependent spkgs really get rebuilt) etc. .

One can also test it by doing a real upgrade from some *vanilla* version to 4.6.alpha1, *after that* applying the patch to `module_list.py` and copying over the new `spkg/install` and `spkg/standard/deps`, then exporting `SAGE_UPGRADE=yes` and running `make`. Then everything should be properly [re]built.


---

Comment by jdemeyer created at 2010-09-23 07:57:07

Replying to [comment:54 leif]:
> Unfortunately we'll have to set up a Sage package server (or a special directory on e.g. `www.sagemath.org`) to "fully" test this, i.e. by _really_ running `sage -upgrade`.

I could probably do this.


---

Comment by jdemeyer created at 2010-09-23 10:57:25

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-09-23 10:57:25

Your `spkg/install` file gives trouble:

```
cd spkg && ./install all 2>&1 | tee -a ../install.log
./install: line 90: syntax error near unexpected token `||'
./install: line 90: `    || ([ -f "$SAGE_LOCAL/bin/sage-upgrade" ] &&'
```



---

Comment by jdemeyer created at 2010-09-23 10:58:30

This is on a Gentoo Linux x86_64 system, with

```
GNU bash, version 3.2.39(1)-release (x86_64-pc-linux-gnu)
Copyright (C) 2007 Free Software Foundation, Inc.
```



---

Comment by jdemeyer created at 2010-09-23 11:01:17

I looks like lines 90 and 91 need a `\` at the end of the line.


---

Comment by leif created at 2010-09-23 13:20:31

New `spkg/install`. Based on Sage 4.6.alpha1. (Not under revision control.)


---

Attachment

Diff of new `spkg/install` against that of Sage 4.6.alpha1.


---

Attachment

Replying to [comment:54 leif]:
> One can also test it by doing a real upgrade from some *vanilla* version to 4.6.alpha1, *after that* applying the patch to `module_list.py` and copying over the new `spkg/install` and `spkg/standard/deps`, then exporting `SAGE_UPGRADE=yes` and running `make`. Then everything should be properly [re]built.

s/`SAGE_UPGRADE`/`SAGE_UPGRADING`/


---

Comment by leif created at 2010-09-23 13:24:21

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-09-23 13:25:37

Replying to [comment:56 jdemeyer]:
> Your `spkg/install` file gives trouble

Updated.


---

Comment by jdemeyer created at 2010-09-24 07:36:13

I created a Sage distribution for testing this.

Please test:

```
sage -upgrade http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/
```



---

Comment by leif created at 2010-09-24 13:59:01

Replying to [comment:61 jdemeyer]:
> I created a Sage distribution for testing this.
> 
> Please test:

```
sage -upgrade http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/
```


Thanks!

Upgrade path: http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/

On MacOS X, one should at the moment either do an "in-place" upgrade (without renaming the directory / copying the original installation) or follow the instructions given above (regarding `LDSHARED`).


---

Comment by leif created at 2010-09-24 14:11:18

Replying to [comment:62 leif]:
> On MacOS X, one should at the moment either do an "in-place" upgrade (without renaming the directory / copying the original installation) or follow the instructions given above (regarding `LDSHARED`).

If one tests upgrading in a new directory (renamed or copied) on MacOS X, it should be suffient to do

```sh
export LDSHARED="gcc -bundle -undefined dynamic_lookup"
```

*before* running `./sage -upgrade ...` (with the upgrade path provided by Jeroen).


---

Comment by jhpalmieri created at 2010-09-24 16:12:49

As is often the case with upgrading, I'm puzzled by the logic here.  How can any patches help an upgrade from 4.5.3 (for example) to 4.6?

 - Upgrading won't affect files like `spkg/standard/deps` or `spkg/install` as long as those files aren't tracked anywhere -- see #9433.
 - Upgrading will change scripts like `sage-upgrade`, but of course it has to be running the old versions during the upgrade process.

I can understand that patches to these files might help in future versions, but is there any way to deal with 4.5.3 to 4.6?

(Meanwhile, I'm building a vanilla 4.5.3 to test the new upgrade path.)


---

Comment by leif created at 2010-09-24 16:32:27

Replying to [comment:65 jhpalmieri]:
> As is often the case with upgrading, I'm puzzled by the logic here.  How can any patches help an upgrade from 4.5.3 (for example) to 4.6?
> 
>  - Upgrading won't affect files like `spkg/standard/deps` or `spkg/install` as long as those files aren't tracked anywhere -- see #9433.

`sage-upgrade.py` also copies these two files (cf. the `pipestatus` issue with upgrading to 4.5[.1]).
 
>  - Upgrading will change scripts like `sage-upgrade`, but of course it has to be running the old versions during the upgrade process.

The new `spkg/install` is aware of that, i.e. deals with an old `sage-upgrade`, too. (See comments in the patch to the former.)
 
> I can understand that patches to these files might help in future versions, but is there any way to deal with 4.5.3 to 4.6?

The patches are intended to especially deal with this (and should ease future upgrades as well).
 
> (Meanwhile, I'm building a vanilla 4.5.3 to test the new upgrade path.)

Fine. I've copied a 4.5.3 installation (_of course_<sup>TM</sup> first running out of disk space) on Ubuntu 9.04 x86 and am currently running the upgrade.

Note that when teeing the output it appears to hang, since the user is prompted, but the output isn't flushed. (One has to type "y" and hit return to start upgrading.) I'll open a ticket for that.


---

Comment by leif created at 2010-09-24 16:38:58

Ooops, it's not `sage-upgrade.py`, its name is `sage-update` (a Python script though).


---

Comment by leif created at 2010-09-24 16:48:24

Ouch!

Jeroen, you forgot to put the new `spkg/install` into the upgrade path.

(http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/spkg/install is still the old one, which doesn't work.)


---

Comment by leif created at 2010-09-24 18:36:15

Replying to [comment:58 jdemeyer]:
> I looks like lines 90 and 91 need a `\` at the end of the line.

I shouldn't have moved the `||` to the next line (which I later found more readable). ;-)

The `\` currently on line 90 (following `&&`) is superfluous, at least for POSIX-conformant shells.


---

Comment by jdemeyer created at 2010-09-24 21:04:11

Replying to [comment:68 leif]:
> Ouch!
> 
> Jeroen, you forgot to put the new `spkg/install` into the upgrade path.
> 
> (http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/spkg/install is still the old one, which doesn't work.)

Should be fixed (let's hope I didn't mess up anything else).


---

Comment by leif created at 2010-09-25 02:16:20

Hmmm, this is really odd:

Since the `sage_scripts` spkg has been updated, and is part of `$(BASE)`, and *all* standard packages depend on `$(BASE)`, *all* packages were rebuilt during upgrade.

(This is "correct", but except for the number of packages that have to be downloaded, this isn't better than rebuilding the new Sage version from source. Unfortunately, for this release. I wonder if we can improve `spkg/standard/deps`, or avoid updating `sage_scripts` [to often] in the future.)


---

Comment by leif created at 2010-09-25 02:24:51

Which packages do _really_ depend on `sage_scripts`?

(I currently have no idea, except perhaps those depending on Python? Fortran?)


---

Comment by jhpalmieri created at 2010-09-25 03:43:26

First, after doing

```
$ export LDSHARED="gcc -bundle -undefined dynamic_lookup"
$ ./sage -upgrade ...
```

Sage starts without segfaulting.  However, it wasn't totally successful because eclib didn't get rebuilt (nor did most of the packages).  Every log file gets touched, typically with a message like `sage: eclib-20100711 is already installed`, but that's it.  It looks to me as though the upgrade path still doesn't have the right version of "install", either in SAGE_ROOT/spkg or in the scripts spkg (which I don't think matters for upgrading).

Second, of course every package depends on sage_scripts because the script sage-spkg (for example) must be present.  But for upgrading, I don't know which ones really might depend on changes made to it.


---

Comment by leif created at 2010-09-25 03:58:15

Replying to [comment:73 jhpalmieri]:
> [...] it wasn't totally successful because eclib didn't get rebuilt (nor did most of the packages).  Every log file gets touched, typically with a message like `sage: eclib-20100711 is already installed`, but that's it.  It looks to me as though the upgrade path still doesn't have the right version of "install", either in SAGE_ROOT/spkg or in the scripts spkg (which I don't think matters for upgrading).

Hmmm, did you upgrade to early? Or a cache issue? Worked for me (see above, the machine was completely "clean", i.e. lacking any new version of `spkg/install`, and that got properly updated by `sage-update`.

 
> Second, of course every package depends on sage_scripts because the script sage-spkg (for example) must be present.

But a copy of that is already present (in `spkg/base/`), so it doesn't have to be extracted from an spkg, and is just copied over to `local/bin` (and later overwritten by the one from `sage_scripts`).

> But for upgrading, I don't know which ones really might depend on changes made to it.

I rather thought of dependencies on other scripts. I intentionally did _not_ change `sage-spkg`. ;-)


---

Comment by leif created at 2010-09-25 04:03:48

The copying is done in `spkg/base/dir-0.1-install`:

```sh
...
   mymkdir "../local/bin"
   mymkdir "../local/include"
   mymkdir "../tmp/"
   mymkdir "$BUILD"
   mymkdir "installed/"

   cp base/sage-* ../local/bin/
...
```



---

Comment by leif created at 2010-09-25 04:07:57

... and the base packages are of course _not_ installed with `sage-spkg`:

```make
########################################
# Building the base system
########################################
$(INST)/$(DIR):
	$(INSTALL) "base/$(DIR)-install 2>&1" "tee -a $(SAGE_LOGS)/$(DIR).log"
```



---

Comment by leif created at 2010-09-25 04:16:40

Replying to [comment:74 leif]:
> I rather thought of dependencies on other scripts. I intentionally did _not_ change `sage-spkg`. ;-)

An example is the (Python-related) `sage-make_relative`, but this could be run *once* at the end. (Or [also] integrated into `sage-spkg`, as suggested by Dave elsewhere.)


---

Comment by jhpalmieri created at 2010-09-25 05:00:00

> Hmmm, did you upgrade to early?

The file [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/spkg/install](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/spkg/install) is still the old one.  Or maybe with the activity on sage.math (with William working on /home, etc.), it got changed back to the old one?


---

Comment by leif created at 2010-09-25 05:41:25

Replying to [comment:78 jhpalmieri]:
> > Hmmm, did you upgrade to early?
> 
> The file [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/spkg/install](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/spkg/install) is still the old one.  Or maybe with the activity on sage.math (with William working on /home, etc.), it got changed back to the old one?

That's a total mess. It's not _still_, it's *again* the old one!

Hopefully trac isn't affected by such...

I only wonder if `spkg/install` gets somehow again overwritten during the upgrade process, since *after* the upgrade, I again have the old version, though I verified the new one was downloaded in the first place (and otherwise I wouldn't have run into the _rebuild all_ issue; `sage-spkg` was definitely called with `-f`).

Perhaps it (i.e. the old version) got later again downloaded when doing the _Double-checking..._.

And perhaps William should follow Dave and enable the ZIL (on an SSD).


---

Comment by leif created at 2010-09-25 06:09:20

From `sage-sage`:

```sh
if [ "$1" = '-upgrade' -o "$1" = "--upgrade" ]; then
    # People often move the Sage install right before doing the upgrade, so it's
    # important to fix any path hardcoding issues first, or certain library
    # links will fail.
    "$SAGE_ROOT/local/bin/"sage-location

    # Do it twice since when installing sage-scripts and a running
    # script changes, it gets confused and exits with an error.
    # Running again (with the script replaced) then fixes the problem.
    # Run from a temporary copy of sage-sage
    shift
    sage-upgrade "$`@`"
    if [ $? = 2 ]; then   # this exit codes means the user elected not to do the upgrade at all.
        exit $?
    fi
    echo "Double checking that all packages have been installed."
    sage-upgrade "$`@`"
    exit $?
fi
```

But `sage-update` won't download `spkg/install` twice if _"No new spkgs"_ are available, which should be the case after a successful (first) upgrade.

So it must get overwritten from somewhere else...


---

Comment by leif created at 2010-09-25 06:32:27

Replying to [comment:80 leif]:
> So it must get overwritten from somewhere else...

Yep, it's overwritten in `sage_scripts-*`'s `spkg-install`, and Jeroen (also) forgot to put the new one into the `sage_scripts` spkg, s.t. *after* the upgrade, the old one is back.

(`deps` and `sage-upgrade` are ok.)


---

Comment by leif created at 2010-09-25 06:54:48

I've successfully built and tested 4.6.alpha1 (from scratch) with a _modified_ `deps` file where only the Sage library spkg depends on the Sage scripts, with 32 jobs on an already 50% loaded system.

So as I expected, adding the scripts to `$(BASE)` is obsolete.

I'll upload a `...deps.v2` later, which then avoids rebuilding _all_ packages on every upgrade.


---

Comment by jdemeyer created at 2010-09-25 08:48:10

Apologies for the mess, I'm having a look what's going on...


---

Comment by jdemeyer created at 2010-09-25 08:55:20

Could it be that `spkg/install` is overwritten by `make`?  I've patched `spkg/install` and then built Sage.


---

Comment by jdemeyer created at 2010-09-25 09:02:13

Yes, `make` overwrites `spkg/install` some time in the very beginning of the installation.  Anybody knows where this `spkg/install` comes from?


---

Comment by jdemeyer created at 2010-09-25 09:10:22

Replying to [comment:81 leif]:
> Replying to [comment:80 leif]:
> > So it must get overwritten from somewhere else...
> 
> Yep, it's overwritten in `sage_scripts-*`'s `spkg-install`, and Jeroen (also) forgot to put the new one into the `sage_scripts` spkg, s.t. *after* the upgrade, the old one is back.

Yes, this is exactly what happened.


---

Comment by mpatel created at 2010-09-25 09:26:28

Replying to [comment:82 leif]:
> I've successfully built and tested 4.6.alpha1 (from scratch) with a _modified_ `deps` file where only the Sage library spkg depends on the Sage scripts, with 32 jobs on an already 50% loaded system.
> 
> So as I expected, adding the scripts to `$(BASE)` is obsolete.

I added the scripts to `$(BASE)` during the reorganization of `deps` at #8306, because of the problem mentioned in [comment:ticket:8306:29 this comment].  This may well have been overkill.

> I'll upload a `...deps.v2` later, which then avoids rebuilding _all_ packages on every upgrade.


---

Comment by jhpalmieri created at 2010-09-25 14:36:38

This morning, the upgrade procedure isn't working.  I'm getting this in the _termcap_ install log (?!), after the new sage_scripts has been installed successfully:

```
ar rc libtermcap.a termcap.o tparam.o version.o
ranlib libtermcap.a
/Applications/sage_builds/sage-4.6.alpha1-upgrade/local/bin/install -c -m 644 libtermcap.a /Applications/sage_builds/sage-4.6.alpha1-upgrade/local/lib/libtermcap.a
Creating pipestatus.
cp: base/sage-*: No such file or directory
cp: base/testcc.sh: No such file or directory
cp: base/testcxx.sh: No such file or directory
/Applications/sage_builds/sage-4.6.alpha1-upgrade/local/bin/install: line 105: standard/newest_version: No such file or directory
/Applications/sage_builds/sage-4.6.alpha1-upgrade/local/bin/install: line 108: standard/newest_version: No such file or directory
/Applications/sage_builds/sage-4.6.alpha1-upgrade/local/bin/install: line 111: standard/newest_version: No such file or directory
/Applications/sage_builds/sage-4.6.alpha1-upgrade/local/bin/install: line 120: standard/newest_version: No such file or directory
/Applications/sage_builds/sage-4.6.alpha1-upgrade/local/bin/install: line 123: standard/newest_version: No such file or directory
/Applications/sage_builds/sage-4.6.alpha1-upgrade/local/bin/install: line 126: standard/newest_version: No such file or directory
/Applications/sage_builds/sage-4.6.alpha1-upgrade/local/bin/install: line 129: standard/newest_version: No such file or directory
/Applications/sage_builds/sage-4.6.alpha1-upgrade/local/bin/install: line 132: standard/newest_version: No such file or directory
/Applications/sage_builds/sage-4.6.alpha1-upgrade/local/bin/install: line 135: standard/newest_version: No such file or directory
/Applications/sage_builds/sage-4.6.alpha1-upgrade/local/bin/install: line 138: standard/newest_version: No such file or directory
/Applications/sage_builds/sage-4.6.alpha1-upgrade/local/bin/install: line 141: standard/newest_version: No such file or directory
/Applications/sage_builds/sage-4.6.alpha1-upgrade/local/bin/install: line 144: standard/newest_version: No such file or directory
Error determining package name using spkg/standard/newest_version script.
make[1]: *** [install] Error 1
```

Looks like a directory is not set correctly, because for example "install" is being run from local/bin/ rather than from spkg/.


---

Comment by leif created at 2010-09-25 14:46:58

LOL, we should in any case rename our `install` which comes from `sage_scripts` and is first copied to `$SAGE_LOCAL/bin` (which is in the path!).

So it happened that the scripts spkg got installed during `libtermcap`s installation / `configure`, and that found *our* `install` as a BSD-compatible install.

I'm happy removing `sage_scripts` from `$(BASE)` also solves this! :)


---

Comment by leif created at 2010-09-25 14:50:16

(Or `libtermcap` simply ran the first `install` [currently] in the path, which happened to be ours.)

I don't think testing with the upgrade (test) path currently makes sense, not to mention the filesystem trouble.


---

Comment by jdemeyer created at 2010-09-25 15:14:35

In any case, I think I fixed the issues with `spkg/install` in my upgrade path
[http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/)


---

Comment by drkirkby created at 2010-09-25 15:28:07

I've long since thought that we need a way of stopping people upgrade from incomatible versions. One stratergy might be to only allow upgrades of the same major version, then ensure that incomatible changes are not permitted in the same version. 

I've personally given up tryig to use the upgrade option. 

Dave


---

Comment by leif created at 2010-09-25 15:53:02

Replying to [comment:89 leif]:
> I'm happy removing `sage_scripts` from `$(BASE)` also solves this! :)

That's not really true, but we definitely need a new `sage_scripts` spkg.

I'll provide one later, together with a modified `deps`.

`@`Dave: Nice attitude; I don't think many users will agree with you. If we can make upgrading work, we should IMHO do it.


---

Comment by leif created at 2010-09-25 17:17:35

Replying to [comment:91 jdemeyer]:
> In any case, I think I fixed the issues with `spkg/install` in my upgrade path
> [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/)

Well, `spkg/install` and `spkg/standard/deps` are current again, but you've checked the (also current) `install` in (s.t. it's now in the Sage scripts repo, and also ends up in `$SAGE_ROOT/local/bin` where the scripts repo of the installation lives):

```sh
leif`@`quadriga:~/tmp/sage_scripts-4.6.upgradetest_alpha1$ hg log -v install     
changeset:   1582:876225f0dec8
tag:         4.6.upgradetest_alpha1
user:        Jeroen Demeyer <jdemeyer`@`cage.ugent.be>
date:        Sat Sep 25 11:32:06 2010 +0200
files:       install
description:
#9896: new spkg/install


leif`@`quadriga:~/tmp/sage_scripts-4.6.upgradetest_alpha1$ 
```

(The file should be in `.hgignore`.)

I don't think the instance in the `sage_scripts` spkg should be copied over `spkg/install` during that spkg's installation; if at all (see below), we should do that *after* the running instance of `spkg/install` has terminated, i.e. from the scripts that start it (`sage-upgrade` and the top-level Makefile, perhaps some other scripts).

But in principle we don't have to copy it at all; we should just make sure that both are the same. If that's _not_ the case, something went very wrong. This is true for both upgrades _and_ builds from scratch.


---

Comment by leif created at 2010-09-25 18:00:47

Replying to [comment:87 mpatel]:
> Replying to [comment:82 leif]:
> > So as I expected, adding the scripts to `$(BASE)` is obsolete.
> 
> I added the scripts to `$(BASE)` during the reorganization of `deps` at #8306, because of the problem mentioned in [comment:ticket:8306:29 this comment].  This may well have been overkill.

LOL (again), "good catch". That just happened because some !"#$%& decided to put the Rpy package *into* R's spkg and recursively call `sage-spkg` from R's `spkg-install`. Perhaps #9906 should be a blocker... ;-)

`sage-spkg` is copied over to `$SAGE_LOCAL/bin` early, in `dir-0.1-install` (and `$SAGE_ROOT/sage` is also present), but not `$SAGE_LOCAL/bin/sage-sage`:

```sh
...
echo "Now install rpy"

cd "$CUR"

RPY_VER=rpy2-2.0.8

sage -f "$RPY_VER".spkg
if [ ! -f "$SAGE_ROOT"/spkg/installed/"$RPY_VER" ]; then
    echo "Error installing rpy."
    exit 1
fi
...
```

(From R's `spkg-install`. If we as a first step call `sage-spkg` there directly, the error from #8306 won't happen.)


---

Comment by jhpalmieri created at 2010-09-25 19:13:53

The programs "sage-download_package", "sage-latest-online-package", "sage-build-debian" could conceivably be called by sage-spkg during installation, but they shouldn't for any standard packages.  The script "sage-check-64" is called by sage-env, so perhaps it should be added to spkg/base?

The sagetex package should depend on the scripts package, since its spkg-check file runs Sage, and so relies on the presence of the script sage-sage.


---

Comment by leif created at 2010-09-25 19:47:13

Replying to [comment:96 jhpalmieri]:
> The programs "sage-download_package", "sage-latest-online-package", "sage-build-debian" could conceivably be called by sage-spkg during installation, but they shouldn't for any standard packages.

Hopefully. ;-)

> The script "sage-check-64" is called by sage-env, so perhaps it should be added to spkg/base?

If we keep it at all (we already had that discussion), it should be and certainly should have earlier been included in `base/`.

> The sagetex package should depend on the scripts package, since its spkg-check file runs Sage, and so relies on the presence of the script sage-sage.

I intended to make the Sage library depend on the Sage scripts; `sagetex` of course (also) depends on the former.


---

Comment by leif created at 2010-09-25 19:59:23

Analogous to `SAGE_UPGRADING`, we should perhaps set `SAGE_BUILDING` (or `SAGE_IN_BUILD`) to "yes" to prevent undesired behavior like downloading in scripts.


---

Comment by leif created at 2010-09-25 23:10:11

Replying to [comment:95 leif]:
> If we as a first step call `sage-spkg` there directly, the error from #8306 won't happen.

A new R spkg (r-2.10.1.p4) that doesn't depend on the Sage scripts spkg can be found at #10016 (needs review).


---

Comment by jdemeyer created at 2010-09-26 10:54:29

Replying to [comment:94 leif]:
> Well, `spkg/install` and `spkg/standard/deps` are current again, but you've checked the (also current) `install` in (s.t. it's now in the Sage scripts repo, and also ends up in `$SAGE_ROOT/local/bin` where the scripts repo of the installation lives):

But why is it copied to `$SAGE_ROOT/local/bin`? Surely, putting the file under revision control should not have that as consequence?


---

Comment by leif created at 2010-09-26 13:52:45

Replying to [comment:100 jdemeyer]:
> Replying to [comment:94 leif]:
> > Well, `spkg/install` and `spkg/standard/deps` are current again, but you've checked the (also current) `install` in (s.t. it's now in the Sage scripts repo, and also ends up in `$SAGE_ROOT/local/bin` where the scripts repo of the installation lives):
> 
> But why is it copied to `$SAGE_ROOT/local/bin`? Surely, putting the file under revision control should not have that as consequence?

`sage_scripts-*.spkg` _contains_ the `local/bin/.hg` repository (at the _top_ level), and *only* that. If during installation of the spkg a repository already exists in `$SAGE_LOCAL/bin`, it gets synchronized from that, so any file checked into the spkg's repo will be "copied" to `$SAGE_LOCAL/bin`. Other files in the spkg's top-level directory (i.e., in `.hgignore`) won't.

It would perhaps be less confusing if that spkg had the same structure as almost all others, i.e. the files _to be installed_ in `src/` (including the `local/bin` repo), and the files that _manage the installation_ in the top-level directory, `sage_scripts-*/`, along with their *own*, separate, Mercurial repository.


---

Comment by jdemeyer created at 2010-09-27 10:27:38

Replying to [comment:101 leif]:
> Replying to [comment:100 jdemeyer]:
> > Replying to [comment:94 leif]:
> > > Well, `spkg/install` and `spkg/standard/deps` are current again, but you've checked the (also current) `install` in (s.t. it's now in the Sage scripts repo, and also ends up in `$SAGE_ROOT/local/bin` where the scripts repo of the installation lives):
> > 
> > But why is it copied to `$SAGE_ROOT/local/bin`? Surely, putting the file under revision control should not have that as consequence?
> 
> `sage_scripts-*.spkg` _contains_ the `local/bin/.hg` repository (at the _top_ level), and *only* that. If during installation of the spkg a repository already exists in `$SAGE_LOCAL/bin`, it gets synchronized from that, so any file checked into the spkg's repo will be "copied" to `$SAGE_LOCAL/bin`. Other files in the spkg's top-level directory (i.e., in `.hgignore`) won't.

So, this means that `install` should be put in `.hgignore`, right?

> It would perhaps be less confusing if that spkg had the same structure as almost all others, i.e. the files _to be installed_ in `src/` (including the `local/bin` repo), and the files that _manage the installation_ in the top-level directory, `sage_scripts-*/`, along with their *own*, separate, Mercurial repository.

Any volunteers to do this? :-)


---

Comment by leif created at 2010-09-27 10:45:12

Replying to [comment:102 jdemeyer]:
> So, this means that `install` should be put in `.hgignore`, right?

Yep. (Or one could `hg rename` it to something else, s.t. it doesn't get confused with a BSD `install`.) 

> > It would perhaps be less confusing if that spkg had the same structure as almost all others, i.e. the files _to be installed_ in `src/` (including the `local/bin` repo), and the files that _manage the installation_ in the top-level directory, `sage_scripts-*/`, along with their *own*, separate, Mercurial repository.
> 
> Any volunteers to do this? :-)

You? But that should be done *after* this ticket and especially #9433, which adds a new root repository (and deals with files like `install` currently _not_ under revision control), have been merged.


---

Comment by leif created at 2010-09-27 11:06:56

Replying to [comment:103 leif]:
> Replying to [comment:102 jdemeyer]:
> > So, this means that `install` should be put in `.hgignore`, right?
> 
> Yep. (Or one could `hg rename` it to something else, s.t. it doesn't get confused with a BSD `install`.) 

P.S.: In case you rename it, if its name starts with `sage-`, it will also be copied during an _install/build from scratch_ (but then also wouldn't be confused with some system tool).


---

Attachment

Improved new `spkg/standard/deps`. Based on Sage 4.6.alpha1. (Not under revision control.)


---

Attachment

Diff of improved new `spkg/standard/deps` against that of Sage 4.6.alpha1.


---

Attachment

Improved new `spkg/install`. Based on Sage 4.6.alpha1. (Not under revision control.)


---

Attachment

Diff of improved new `spkg/install` against that of Sage 4.6.alpha1.


---

Comment by jdemeyer created at 2010-09-28 12:42:32

Updated upgrade path: [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha1/)


---

Comment by jdemeyer created at 2010-09-29 08:01:27

Upgraded succesfully from 4.5.3 on a Mac OS X 10.4 PPC system.


---

Comment by leif created at 2010-09-29 14:17:43

Replying to [comment:107 jdemeyer]:
> Upgraded succesfully from 4.5.3 on a Mac OS X 10.4 PPC system.

I did so on Ubuntu 9.04 x86 (in-place), and on Ubuntu 10.04 x86_64 (in a renamed directory), too.

`ptestlong` passed all tests, but Sphinx raises an exception related to `linear_programming` on both systems:

```
...
sphinx-build -b html -d /home/leif/Sage/sage-4.5.3-for-v2b-upgraded/devel/sage/doc/output/doctrees/en/constructions    /home/leif/Sage/sage-4.5.3-for-v2b-upgraded/devel/sage/doc/en/constructions /home/leif/Sage/sage-4.5.3-for-v2b-upgraded/devel/sage/doc/output/html/en/constructions
Running Sphinx v0.6.3
loading pickled environment... done
building [html]: targets for 18 source files that are out of date
updating environment: [config changed] 17 added, 0 changed, 1 removed
reading sources... [  5%] algebraic_geometry
reading sources... [ 11%] calculus
reading sources... [ 17%] contributions
reading sources... [ 23%] elliptic_curves
reading sources... [ 29%] graph_theory
reading sources... [ 35%] groups
reading sources... [ 41%] index
reading sources... [ 47%] interface_issues
reading sources... [ 52%] linear_algebra
reading sources... [ 58%] linear_codes
reading sources... [ 64%] modular_forms
reading sources... [ 70%] number_fields
reading sources... [ 76%] number_theory
reading sources... [ 82%] plotting
reading sources... [ 88%] polynomials
reading sources... [ 94%] rep_theory
reading sources... [100%] rings

looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [  5%] algebraic_geometry
writing output... [ 11%] calculus
writing output... [ 16%] contributions
writing output... [ 22%] elliptic_curves
writing output... [ 27%] graph_theory
writing output... [ 33%] groups
writing output... [ 38%] index
writing output... [ 44%] interface_issues
writing output... [ 50%] linear_algebra
writing output... [ 55%] linear_codes
writing output... [ 61%] linear_programming

Exception occurred:
  File "/home/leif/Sage/sage-4.5.3-for-v2b-upgraded/local/lib/python2.6/site-packages/Sphinx-0.6.3-py2.6.egg/sphinx/environment.py", line 934, in get_toc_for
    toc = self.tocs[docname].deepcopy()
KeyError: 'linear_programming'
The full traceback has been saved in /tmp/sphinx-err-BbYhGC.log, if you want to report the issue to the author.
Please also report this if it was a user error, so that a better error message can be provided next time.
Send reports to sphinx-dev`@`googlegroups.com. Thanks!
Build finished.  The built documents can be found in /home/leif/Sage/sage-4.5.3-for-v2b-upgraded/devel/sage/doc/output/html/en/constructions
...
```

After removing the doctrees and rebuilding the documentation, this doesn't happen; `linear_programming` had been moved from _Constructions_ to the _Thematic Tutorials_. (Note that Sage completely ignores any Sphinx errors, but that's just another bug.)


---

Comment by leif created at 2010-09-29 14:47:03

Btw, if somebody reviewed #10016 (and that got merged into Sage 4.6), we could drop the dependency of R on `sage_scripts`, which would further decrease the number of packages that have to be rebuilt during an upgrade.

(The `sage_scripts` spkg currently "changes" in *any* new Sage version, which is sub-optimal anyway.)


---

Comment by jdemeyer created at 2010-10-04 19:24:32

New upgrade path based on sage-4.6.alpha2:
[http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha2/](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha2/)


---

Comment by jhpalmieri created at 2010-10-11 22:58:39

I'm confused again.  On my mac, it seems like 

```sh
$ export LDSHARED="gcc -bundle -undefined dynamic_lookup"
```

solves the problem: I did this and then upgraded from 4.5.3 to 4.6.alpha*3*, and did not have the reported problem and all tests pass in sage/libs/pari.  So do we need the various patches?  They may be good ideas, but are they necessary for this ticket?  (I have only seen a problem on OS X, so I can't easily test what works and what doesn't on other systems.)

Also, do we need to advertise the need to set LDSHARED like this?  Or can we set it automatically during the upgrade process?


---

Comment by mpatel created at 2010-10-17 01:45:46

Replying to [comment:109 leif]:
> Btw, if somebody reviewed #10016 (and that got merged into Sage 4.6), we could drop the dependency of R on `sage_scripts`, which would further decrease the number of packages that have to be rebuilt during an upgrade.

With #10016 merged into 4.6.alpha2, should we update `deps`?


---

Comment by leif created at 2010-10-17 01:58:07

Replying to [comment:112 mpatel]:
> Replying to [comment:109 leif]:
> > Btw, if somebody reviewed #10016 (and that got merged into Sage 4.6), we could drop the dependency of R on `sage_scripts`, which would further decrease the number of packages that have to be rebuilt during an upgrade.
> 
> With #10016 merged into 4.6.alpha2, should we update `deps`?

Yes, we can... ;-)

(The modifications are already all in, but currently commented out, including the additions / changes we need once RPy becomes a stand-alone spkg. I can perhaps upload v3 versions tomorrow, or otherwise feel free to do it.)


---

Comment by leif created at 2010-10-17 02:39:29

Replying to [comment:111 jhpalmieri]:
> I'm confused again.  On my mac, it seems like 

```sh
$ export LDSHARED="gcc -bundle -undefined dynamic_lookup"
```

> solves the problem: I did this and then upgraded from 4.5.3 to 4.6.alpha*3*, and did not have the reported problem and all tests pass in sage/libs/pari.

`ptestlong`? Some extension modules should still refer to the _old_ PARI shared library, which can cause trouble. Did you do anything else except `export LDSHARED=...` and `./sage -upgrade /path/to/alpha3`?

> So do we need the various patches?

Currently just four IIRC... ;-)

> They may be good ideas, but are they necessary for this ticket?  (I have only seen a problem on OS X, so I can't easily test what works and what doesn't on other systems.)

While setting `LDSHARED` is not necessary on systems other than MacOS X (at least as far as I know / on the supported platforms), the patches make upgrading more "reliable". (I personally had to play a little to make upgrading fail on my Linux boxes I must admit, but without the patches it definitely _can_ fail. Also, we'd run into similar problems when it comes to upgrading e.g. MPIR; to make _that_ work, we'll in addition have to add some more dependencies to `module_list.py`.)
 
> Also, do we need to advertise the need to set LDSHARED like this?  Or can we set it automatically during the upgrade process?

I intended to do so, there are just (too) many ways how one could do this. ;-) (Basically e.g. adding a few Darwin-specific lines to `devel/sage/setup.py`, which is part of the `sage-x.y.z.spkg`, which "of course" gets updated upon _every_ upgrade, regardless if there are any changes to the Sage library at all - besides `version.py` which is or will become redundant anyway.)


---

Comment by jdemeyer created at 2010-10-18 07:10:59

Replying to [comment:113 leif]:
> (The modifications are already all in, but currently commented out, including the additions / changes we need once RPy becomes a stand-alone spkg. I can perhaps upload v3 versions tomorrow, or otherwise feel free to do it.)

Setting status to "needs_work" because of this comment.


---

Comment by jdemeyer created at 2010-10-18 07:10:59

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-10-18 13:13:30

Improved new `spkg/standard/deps`. Based on Sage 4.6.alpha*3*, removes `sage_scripts` from R's deps. (Not under revision control.)


---

Attachment

Diff of improved new `spkg/standard/deps` against that of Sage 4.6.alpha*3*.


---

Comment by leif created at 2010-10-18 13:49:13

Since #10016 has been merged into Sage 4.6.alpha2, I've attached a new version (v3) of `spkg/standard/deps`, which just removes the dependency of R on `sage_scripts`.

Here's a diff between v2b and v3:

```diff
--- trac_9896-SAGE_ROOT__spkg__standard__deps.v2b	2010-09-27 18:50:32.000000000 +0200
+++ trac_9896-SAGE_ROOT__spkg__standard__deps.v3	2010-10-18 14:57:44.000000000 +0200
`@``@` -21,9 +21,7 `@``@`
 # Rather than making *all* standard packages depend on SAGE_SCRIPTS (which
 # triggers the rebuild of *every* package on an upgrade), add SAGE_SCRIPTS
 # to the dependencies of only those packages that rely on them.
-# These are:
-# - R until #10016 is merged (replacing "sage -f ..." by a call to sage-spkg),
-#     or until #9906 is merged (which moves the RPy spkg out of R's)
+# These are (as of Sage 4.6.alpha3):
 # - The Sage library, $(SAGE)
 # - sagetex, but this in turn depends on $(SAGE)
 
`@``@` -368,15 +366,10 `@``@`
 $(INST)/$(MAXIMA): $(BASE) $(INST)/$(ECL)
 	$(INSTALL) "$(SAGE_SPKG) $(MAXIMA) 2>&1" "tee -a $(SAGE_LOGS)/$(MAXIMA).log"
 
-# Until #10016 (or #9906) gets merged, R depends on SAGE_SCRIPTS, because it
-# installs the contained RPy spkg with "sage -f", which also requires sage-sage:
-$(INST)/$(R): $(BASE) $(INST)/$(SAGE_SCRIPTS) \
-	      $(INST)/$(PYTHON) $(INST)/$(ATLAS) $(INST)/$(ICONV) $(INST)/$(FORTRAN)
+# Note that even with a separate RPy spkg (#9906), Sage's R will still depend on
+# Python (but does no longer on SAGE_SCRIPTS, #10016):
+$(INST)/$(R): $(BASE) $(INST)/$(PYTHON) $(INST)/$(ATLAS) $(INST)/$(ICONV) $(INST)/$(FORTRAN)
 	$(INSTALL) "$(SAGE_SPKG) $(R) 2>&1" "tee -a $(SAGE_LOGS)/$(R).log"
-# Note that even with a separate RPy spkg (#9906), Sage's R still depends on
-# Python (but no longer on SAGE_SCRIPTS, see above):
-# $(INST)/$(R): $(BASE) $(INST)/$(PYTHON) $(INST)/$(ATLAS) $(INST)/$(ICONV) $(INST)/$(FORTRAN)
-# 	$(INSTALL) "$(SAGE_SPKG) $(R) 2>&1" "tee -a $(SAGE_LOGS)/$(R).log"
 
 # Needed when #9906 gets merged (moving RPy out of R's spkg):
 # $(INST)/$(RPY): $(BASE) $(INST)/$(PYTHON) $(INST)/$(R)
```


(Note that neither `spkg/install` nor `spkg/standard/deps` have changed between Sage 4.6.alpha1 and 4.6.alpha3, so there's no new v3 of the former, and the diffs apply to alpha1...alpha3. Also, although `devel/sage/module_list.py` has changed, the current patch here still applies to Sage 4.6.alpha3 without rejects.)


---

Comment by jdemeyer created at 2010-10-18 16:02:31

Add "install" to .hgignore, patch for sage-scripts


---

Attachment


---

Attachment

Sage library patch. Fixes Darwin linker issue (in `setup.py`). Based on Sage 4.6.alpha3.


---

Comment by leif created at 2010-10-19 10:21:45

I've attached a patch that avoids manually setting `LDSHARED` on MacOS X.

Of course the upgrade path has yet to be updated for testing this, but the patch can be reviewed.


---

Comment by leif created at 2010-10-19 10:21:45

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-10-19 10:40:48

Replying to [comment:120 leif]:
> Of course the upgrade path has yet to be updated for testing this, but the patch can be reviewed.

One can also (partially) test the new patch by (optionally renaming the Sage directory of an installation to be upgraded, then) running `./sage -upgrade ...` with the _current_ upgrade path, and *after that* applying [the new patch](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9896/trac_9896-fix_hardcoded_libdirs_in_extmod_linker_cmd-sagelib.patch) to the Sage library, then running `./sage -ba` and `make ptestlong` or alike. (Running just `./sage -b` would though show that the obsolete hard-coded directory gets replaced, of course only if `SAGE_ROOT` had been changed. Another way is to put fake directories into `LDSHARED`, e.g. by setting it to `"gcc -bundle -L/foo/bar/ -undefined dynamic_lookup -Lbaz"` on MacOS X, or e.g. `"gcc -L/foo/bar -pthread -Lbaz/ -shared"` on Linux.)


---

Comment by jdemeyer created at 2010-10-19 12:49:45

I am preparing a new upgrade path with the patches.


---

Comment by leif created at 2010-10-19 12:59:51

Replying to [comment:122 jdemeyer]:
> I am preparing a new upgrade path with the patches.

Thanks again. Do you keep the alpha2 upgrade path? Incidentally, I was just going to test _that_ on another machine...


---

Comment by jdemeyer created at 2010-10-19 13:01:16

Replying to [comment:123 leif]:
> Do you keep the alpha2 upgrade path?
Sure.


---

Comment by jdemeyer created at 2010-10-19 20:50:45

New upgrade path: [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha3/](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.upgradetest_alpha3/)

Leif: the stuff about LDSHARED in the description might be outdated, can you fix it?


---

Comment by leif created at 2010-10-19 21:18:30

Replying to [comment:125 jdemeyer]:
> Leif: the stuff about LDSHARED in the description might be outdated, can you fix it?

Done. Thanks.


---

Comment by leif created at 2010-10-19 22:12:12

Just for the record: I again did a fresh build of Sage 4.5.3, renamed the directory and then upgraded to Sage 4.6.alpha*2* with the (previous) test upgrade path (on Ubuntu 10.04 x86_64).

The upgrade failed in the first place, I then "successfully" ran `make` (all new packages are present) and now I get lots of doctest errors (`ptestlong`).

More to come (still running); currently testing the new alpha*3* test upgrade path on another machine.


---

Comment by leif created at 2010-10-19 22:21:17

Replying to [comment:127 leif]:
> Just for the record: I again did a fresh build of Sage 4.5.3, renamed the directory and then upgraded to Sage 4.6.alpha*2* with the (previous) test upgrade path (on Ubuntu 10.04 x86_64).

Meaning: Did anybody test the alpha2 upgrade path? (I don't see reports here.)

> The upgrade failed in the first place, I then "successfully" ran `make` (all new packages are present) and now I get lots of doctest errors (`ptestlong`).
> 
> More to come (still running)


```
The following tests failed:

	sage -t  -long devel/sage/sage/plot/misc.py # 4 doctests failed
	sage -t  -long devel/sage/sage/plot/plot.py # 12 doctests failed
```

At least some end like this:

```
      File "/home/leif/Sage/sage-4.5.3-4.6.alpha2/local/lib/python/site-packages/matplotlib/mathtext.py", line 658, in __init__
        self._stix_fallback = StixFonts(*args, **kwargs)
      File "/home/leif/Sage/sage-4.5.3-4.6.alpha2/local/lib/python/site-packages/matplotlib/mathtext.py", line 900, in __init__
        fullpath = findfont(name)
      File "/home/leif/Sage/sage-4.5.3-4.6.alpha2/local/lib/python/site-packages/matplotlib/font_manager.py", line 1306, in findfont
        if not os.path.exists(font):
      File "/home/leif/Sage/sage-4.5.3-4.6.alpha2/local/lib/python2.6/genericpath.py", line 18, in exists
        st = os.stat(path)
    TypeError: coercing to Unicode: need string or buffer, dict found
```



---

Comment by leif created at 2010-10-20 21:25:43

Updated instructions for testing w.r.t. upgrades not performed in-place.


---

Comment by leif created at 2010-10-21 03:24:24

I've now successfully upgraded to Sage 4.6.alpha3 (from fresh builds of Sage 4.5.3) and (with the exception of the 32-bit system) `ptestlong` passed without errors on:

 * Ubuntu 9.04 x86 (in-place; after upgrading I now also get #10041, which doesn't occur when building from scratch)

 * Ubuntu 9.04 x86_64 (Sage installation moved before upgrading, with the work-around given in the description, i.e. also forcing a rebuild of freetype)

 * Ubuntu 10.04 x86_64 (in-place)

I also "repaired" a failed upgrade from a moved Sage installation on the latter system by forcing reinstallation of freetype and running `make` afterwards; `ptestlong` then also passed without errors.

----

Currently, the installation of matplotlib 1.0.0 (included in alpha3, #9221) breaks older versions of matplotlib in *other* Sage installations; this is now fixed by #6235.

Deleting or renaming `$HOME/.matplotlib/` (probably each time) before running an older (or after running the new) version of Sage also avoids that problem (cf. traceback above, _"TypeError: coercing to Unicode: need string or buffer, dict found"_).


---

Comment by mpatel created at 2010-10-21 09:46:23

Following Jeroen's [suggestion on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/2253505ea7ae98ae), I'm planning to merge this ticket into 4.6.rc0.


---

Comment by jdemeyer created at 2010-10-21 15:08:24

Upgraded succesfully on a PPC Mac OS X 10.4 from sage-4.5.3 to sage-4.6.alpha3 and `ptestlong` passes.  This upgrade was done in place.


---

Comment by jhpalmieri created at 2010-10-21 15:43:57

Upgraded a copied directory on OS X 10.6 successfully.  Also an in-place upgrade on OpenSolaris, just to try a different platform and also to test that setting SAGE_ATLAS_LIB before the initial build wouldn't interfere with anything.


---

Comment by mpatel created at 2010-10-21 21:50:02

Replying to [comment:133 mpatel]:
> Following Jeroen's [suggestion on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/2253505ea7ae98ae), I'm planning to merge this ticket into 4.6.rc0.

I'll merge all of the patches and files in the description's current "How to merge this ticket" section.


---

Comment by leif created at 2010-10-22 10:23:08

Replying to [comment:137 mpatel]:
> Replying to [comment:133 mpatel]:
> > Following Jeroen's [suggestion on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/2253505ea7ae98ae), I'm planning to merge this ticket into 4.6.rc0.
> 
> I'll merge all of the patches and files in the description's current "How to merge this ticket" section.

Thanks!

Upgrading from Sage 4.4.4 in a renamed directory (with the official rc0 upgrade path) fully worked for me on Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3; parallel build with 16 jobs).

Quite surprisingly, even `ptestlong` passed without any doctest errors. ;-) (Cf. sage-release.)

Despite that, I guess there are still missing dependencies in `module_list.py` that will come into play when e.g. updating MPIR (#8664). (I primarily addressed upgrading to the new PARI on this ticket; more changes should IMHO be made on other / the respective spkg tickets.)


---

Comment by leif created at 2010-10-22 10:39:08

Replying to [comment:138 leif]:
> Despite that, I guess there are still missing dependencies in `module_list.py` that will come into play when e.g. updating MPIR (#8664). (I primarily addressed upgrading to the new PARI on this ticket; more changes should IMHO be made on other / the respective spkg tickets.)

NumPy and SciPy (#9808) are other candidates.


---

Comment by leif created at 2010-10-22 20:31:09

Changing assignee from GeorgSWeber to leif.


---

Comment by leif created at 2010-10-22 20:35:26

Also successfully upgraded a _copied_ Sage 4.5.3 installation to 4.6.rc0 on Ubuntu 9.04 x86; `ptestlong` passed without errors (cf. sage-release).


---

Comment by jhpalmieri created at 2010-10-22 21:56:43

As far as reviewing goes, I'm happy with all of the patches except for two.

 - [/trac_9896-fix_hardcoded_libdirs_in_extmod_linker_cmd-sagelib.patch](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9896/trac_9896-fix_hardcoded_libdirs_in_extmod_linker_cmd-sagelib.patch).  This seems fine, but the messages like "Library dir found in dynamic linker command..." don't actually appear in any log (unless you pipe the whole thing through tee, perhaps, but I haven't tried this yet).  (I'm assuming that, since I upgraded from 4.5.3 on OS X, the situation dealt with in the loop would occur, and I searched through all of the logs without finding this string.)  I was hoping that they would appear in the sage-4.6.rc0 log, but no.  Is there anything to be done about this?

 - [trac_9896-fix_extension_module_deps-sagelib.patch](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9896/trac_9896-fix_extension_module_deps-sagelib.patch).  I just don't know enough about the Sage build process and the dependencies to be able to review this well, and I don't have the time to learn about it right now.  I'm hoping that someone else can do this.


---

Comment by leif created at 2010-10-22 22:22:04

Replying to [comment:142 jhpalmieri]:
> As far as reviewing goes, I'm happy with all of the patches except for two.
> 
>  - [/trac_9896-fix_hardcoded_libdirs_in_extmod_linker_cmd-sagelib.patch](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9896/trac_9896-fix_hardcoded_libdirs_in_extmod_linker_cmd-sagelib.patch).  This seems fine, but the messages like "Library dir found in dynamic linker command..." don't actually appear in any log (unless you pipe the whole thing through tee, perhaps, but I haven't tried this yet).  (I'm assuming that, since I upgraded from 4.5.3 on OS X, the situation dealt with in the loop would occur, and I searched through all of the logs without finding this string.)  I was hoping that they would appear in the sage-4.6.rc0 log, but no.  Is there anything to be done about this?


```python
                if ldso_cmd[i][:2] == "-L":
                    libdir = os.path.normpath(ldso_cmd[i][2:])
                    self.debug_print(
                      "Library dir found in dynamic linker command: " +
                      "\"%s\"" % libdir)
                    if libdir != sage_libdir:
                        self.compiler.warn(
                          "Replacing library search directory in linker " +
                          "command:\n  \"%s\" -> \"%s\"\n" % (libdir,
                                                              sage_libdir))
                        ldso_cmd[i] = "-L"+sage_libdir
                    
```


No, that's intentional. `self.debug_print()` only produces output if `DISTUTILS_DEBUG` is set.

In contrast, `self.compiler.warn()` always prints a message, so you should find _"warning: Replacing library search directory ..."_ in the logs of the installations you had moved:

```sh
$ grep "^warning: " install.log
```

or

```sh
$ grep "^warning: Replacing" spkg/logs/sage-*
```

should show these.


---

Comment by jhpalmieri created at 2010-10-22 22:30:16

Oh, sorry, that's what I meant by "messages like ...".  I don't see "Replacing library" in any log file, either.  (I copied my sage-4.5.3 directory to sage-4.6.rc0-upgrade and ran "./sage -upgrade".)


---

Comment by leif created at 2010-10-22 22:37:58

Hmmm, what does

```sh
$ ./sage -b 2>&1 | grep -A2 "^warning"
```

give (in a moved Sage installation)?

You could also do

```sh
$ env DISTUTILS_DEBUG=yes ./sage -b
```

but that produces _a lot_ of output.


---

Comment by drkirkby created at 2010-10-22 22:41:47

`grep -A2` is a GNUism - it will not work with Sun's grep. It would be better to stick to only the options mandated by the POSIX specification on the OpenGroup web site. But I can say for sure that would break on Solaris. 

Dave


---

Comment by leif created at 2010-10-22 23:08:59

I don't think John has Sun's `grep` installed on MacOS X... ;-)

----

On topic again:

There are two reasons you (John) can't find such messages:

 * `./sage -upgrade` doesn't log to `install.log` (I used `script` to log what happened, also because of #10011.)

 * There's a less obvious indirect dependency of Python on iconv (via GNUTLS, libgpg_error), so the Python spkg got rebuilt, too, which of course also updated the library search path of distutils.


---

Comment by jhpalmieri created at 2010-10-22 23:50:41

Replying to [comment:147 leif]:
> I don't think John has Sun's `grep` installed on MacOS X... ;-)

I was just about to install it, but I guess I'll wait a bit now.  

>  * There's a less obvious indirect dependency of Python on iconv (via GNUTLS, libgpg_error), so the Python spkg got rebuilt, too, which of course also updated the library search path of distutils.

The python spkg did get rebuilt.  I'm trying again, first touching spkg/installed/iconv-1.13.1.p3.


---

Comment by leif created at 2010-10-22 23:53:30

Replying to [comment:148 jhpalmieri]:
> Replying to [comment:147 leif]:
> > I don't think John has Sun's `grep` installed on MacOS X... ;-)
> 
> I was just about to install it, but I guess I'll wait a bit now.  
> 
> >  * There's a less obvious indirect dependency of Python on iconv (via GNUTLS, libgpg_error), so the Python spkg got rebuilt, too, which of course also updated the library search path of distutils.
> 
> The python spkg did get rebuilt.  I'm trying again, first touching spkg/installed/iconv-1.13.1.p3.

Note that I've updated the description on that (you have to run `make build` afterwards to make that work).


---

Comment by leif created at 2010-10-23 00:20:07

Replying to [comment:149 leif]:
> Replying to [comment:148 jhpalmieri]:
> > Replying to [comment:147 leif]:
> > > I don't think John has Sun's `grep` installed on MacOS X... ;-)
> > 
> > I was just about to install it, but I guess I'll wait a bit now.  
> > 
> > >  * There's a less obvious indirect dependency of Python on iconv (via GNUTLS, libgpg_error), so the Python spkg got rebuilt, too, which of course also updated the library search path of distutils.
> > 
> > The python spkg did get rebuilt.  I'm trying again, first touching spkg/installed/iconv-1.13.1.p3.
> 
> Note that I've updated the description on that (you have to run `make build` afterwards to make that work).

Ooops, weird. That doesn't seem to be necessary... (And just touching the new iconv worked for me, i.e. e.g. Python did _not_ get rebuilt.)


---

Comment by leif created at 2010-10-23 00:34:49

Replying to [comment:150 leif]:
> Ooops, weird. That doesn't seem to be necessary... (And just touching the new iconv worked for me, i.e. e.g. Python did _not_ get rebuilt.)

Funny, that's because `newest_version` doesn't inspect `spkg/installed/*`, but e.g. `spkg/standard/*.spkg` (and therefore `make` concludes all is up-to-date).

So it works the way I originally described.


---

Comment by drkirkby created at 2010-10-23 00:54:33

Replying to [comment:148 jhpalmieri]:
> Replying to [comment:147 leif]:
> > I don't think John has Sun's `grep` installed on MacOS X... ;-)
> 
> I was just about to install it, but I guess I'll wait a bit now.  

Given the title title had the "(not limited to OS X)" I assumed this needed a solution to work on any platform. But I've not been following this ticket closely, so I'll shut up. 

If John does manage to install Sun's grep on his OS X machine, let me know how. I might even buy a Mac then! 

Dave


---

Comment by jhpalmieri created at 2010-10-23 01:13:01

Okay, after touching iconv, I see the warning in the sage spkg log. (And this was on a machine where I didn't run "make build" before upgrading, as Leif says.)

> Given the title title had the "(not limited to OS X)" I assumed this needed a solution to work on any platform. But I've not been following this ticket closely, so I'll shut up.

At that point, Leif was just suggesting something for me to try on one machine, a mac, to troubleshoot something, not as an actual solution to any problem. So it was a safe suggestion.

Anyway, I guess now I'm happy with all but one of the patches (trac_9896-fix_extension_module_deps-sagelib.patch), and someone else will have to help with that.


---

Comment by jhpalmieri created at 2010-10-23 01:14:12

Oh, on another OS X machine I did "touch .../iconv..." and then "make build" and then "sage -upgrade ...", and then during the upgrade, the linbox spkg failed to install.


---

Comment by leif created at 2010-10-23 01:34:47

Replying to [comment:154 jhpalmieri]:
> Oh, on another OS X machine I did "touch .../iconv..." and then "make build" and then "sage -upgrade ...", and then during the upgrade, the linbox spkg failed to install.

Details? Perhaps just once again a race condition?

(The `make build` should be a nop, i.e. have no influence, unless the installation hadn't been up-to-date before.)


---

Comment by jhpalmieri created at 2010-10-23 03:22:53

The linbox log has messages like this:

```
/bin/sh ../../libtool --tag=CXX   --mode=link g++  -g -fPIC -I"/Applications/sage_builds/sage-4.6.rc0-X/local/include" -I"/Applications/sage_builds/sage-4.6.rc0-X/local/include/linbox"  -L"/Applications/sage_builds/sage-4.6.rc0-X/local/lib" -I/Applications/sage_builds/sage-4.6.rc0-X/spkg/build/linbox-1.1.6.p3/src -I/Applications/sage_builds/sage-4.6.rc0-X/spkg/build/linbox-1.1.6.p3/src/linbox  -I/Applications/sage_builds/sage-4.6.rc0-X/local/include  -I/Applications/sage_builds/sage-4.6.rc0-X/local/include -D__LINBOX_HAVE_CBLAS   -o libutil.la  timer.lo error.lo commentator.lo debug.lo  /usr/lib/libcblas.dylib -L/Applications/sage_builds/sage-4.6.rc0-X/local/lib -lgmpxx -lgmp -L/Applications/sage_builds/sage-4.6.rc0-X/local/lib -lgivaro
libtool: link: warning: library `/Applications/sage_builds/sage-4.6.rc0-X/local/lib/libgmpxx.la' was moved.
grep: /Applications/sage_builds/sage-4.5.3/local/lib/libgmp.la: No such file or directory
sed: /Applications/sage_builds/sage-4.5.3/local/lib/libgmp.la: No such file or directory
libtool: link: `/Applications/sage_builds/sage-4.5.3/local/lib/libgmp.la' is not a valid libtool archive
make[4]: *** [libutil.la] Error 1
make[3]: *** [install-recursive] Error 1
make[2]: *** [install-recursive] Error 1
make[1]: *** [install-recursive] Error 1
Error installing linbox
```



---

Comment by jhpalmieri created at 2010-10-23 04:53:22

Update: on one OS X 10.6 machine, after touching spkg/installed/iconv-1.13.1.p3, it doesn't matter whether I run "make build" or not before upgrading: I get the above error with linbox either way.  On another OS X 10.6 machine, I didn't run "make build" and it seemed to complete successfully; I haven't tried with "make build".  I'll run doctests to see if it's really successful.

I don't know what's different about the two machines.  Maybe the 4.5.3 build got corrupted on the first one somehow?  I can try rebuilding 4.5.3 and doing it again...


---

Comment by leif created at 2010-10-23 12:43:35

Replying to [comment:156 jhpalmieri]:
> The linbox log has messages like this:

```
/bin/sh ../../libtool --tag=CXX   --mode=link g++  -g -fPIC -I"/Applications/sage_builds/sage-4.6.rc0-X/local/include" -I"/Applications/sage_builds/sage-4.6.rc0-X/local/include/linbox"  -L"/Applications/sage_builds/sage-4.6.rc0-X/local/lib" -I/Applications/sage_builds/sage-4.6.rc0-X/spkg/build/linbox-1.1.6.p3/src -I/Applications/sage_builds/sage-4.6.rc0-X/spkg/build/linbox-1.1.6.p3/src/linbox  -I/Applications/sage_builds/sage-4.6.rc0-X/local/include  -I/Applications/sage_builds/sage-4.6.rc0-X/local/include -D__LINBOX_HAVE_CBLAS   -o libutil.la  timer.lo error.lo commentator.lo debug.lo  /usr/lib/libcblas.dylib -L/Applications/sage_builds/sage-4.6.rc0-X/local/lib -lgmpxx -lgmp -L/Applications/sage_builds/sage-4.6.rc0-X/local/lib -lgivaro
libtool: link: warning: library `/Applications/sage_builds/sage-4.6.rc0-X/local/lib/libgmpxx.la' was moved.
grep: /Applications/sage_builds/sage-4.5.3/local/lib/libgmp.la: No such file or directory
sed: /Applications/sage_builds/sage-4.5.3/local/lib/libgmp.la: No such file or directory
libtool: link: `/Applications/sage_builds/sage-4.5.3/local/lib/libgmp.la' is not a valid libtool archive
make[4]: *** [libutil.la] Error 1
make[3]: *** [install-recursive] Error 1
make[2]: *** [install-recursive] Error 1
make[1]: *** [install-recursive] Error 1
Error installing linbox
```


I think this _should_ have been fixed by `local/bin/sage-location`'s

```python
def update_library_files(R):
    LIB = '%s/local/lib/'%os.path.abspath(SAGE_ROOT)
    # The .a files should be re-ranlib'd
    os.system('cd "%s"; ranlib *.a 1>/dev/null 2>/dev/null'%LIB)

    # The .la files hardcode path info.  Fix this.
    for F in os.listdir(LIB):
       if F[-3:] == ".la":
           G = open(LIB + F).read()
           i = G.find('libdir=')
           j = i+8 + G[i+8:].find("'")
           z = G[i+8:j].strip().strip("'")
           i = z.rfind('local/')
           if i != -1:
               z = z[:i]
               H = G.replace(z, os.path.abspath(SAGE_ROOT) + '/')
               open(LIB + F,'w').write(H)
```

which is (also) called from `sage -upgrade` (i.e. `sage-sage`) if the installation has (newly) moved. (I'm not sure how robust that code is, it's at least less readable.)

Did you perhaps interrupt this in the first run?


---

Comment by leif created at 2010-10-23 12:56:05

Ah, I see. The above code fixes just one instance of a hard-coded path in `libgmpxx.la`, namely `libdir=...`, but *not*:

```sh
# Libraries that this one depends upon.
dependency_libs=' /home/leif/Sage/sage-4.6.rc0pre1/local/lib/libgmp.la'
```


I just wonder why this doesn't cause trouble on the other system.


---

Comment by leif created at 2010-10-23 13:12:05

Replying to [comment:161 leif]:
> Ah, I see. The above code fixes just one instance of a hard-coded path in `libgmpxx.la`, namely `libdir=...`, but *not*:

```sh
# Libraries that this one depends upon.
dependency_libs=' /home/leif/Sage/sage-4.6.rc0pre1/local/lib/libgmp.la'
```


Not true. The above reads the old path from `libdir='...'`, but then replaces _all_ occurrences of that (i.e. the old `$SAGE_ROOT`) by the new one. So perhaps really this was interrupted on the machine where LINBOX failed to build.


---

Comment by jhpalmieri created at 2010-10-23 19:06:29

> Did you perhaps interrupt this in the first run?

It's possible.  In any case, I can't repeat it now.


---

Comment by leif created at 2010-10-23 19:41:09

Replying to [comment:163 jhpalmieri]:
> > Did you perhaps interrupt this in the first run?
> 
> It's possible.  In any case, I can't repeat it now.

It would in any case be better to trap `SIGINT` / `KeyboardInterrupt` while doing `sage-location`, or make backup copies first.

Also, it would be helpful for such situations to
 * log `$SAGE_ROOT` changes / movement (in a history file) for debugging or even to get the previous one,
 * perhaps log what changes `sage-location` made (to some file, perhaps a summary on the screen),
 * log the whole upgrade process as we do for builds / spkg installations (I'd suggest `$SAGE_ROOT/upgrade.log`, but only after #10011 and #10157 have been merged).

Do you still have the broken installation? If so, you could

```sh
$ ls -rtl local/lib/*.la # see which were changed last / when
$ cat local/lib/libgmpxx.la # to see the wrong paths
```

(libtool's `.la` files are plain text files.


---

Comment by jhpalmieri created at 2010-10-23 19:52:53


```sh
$ ls -rtl local/lib/*.la
```

The only difference between the broken one and the working one is that the two linbox files have been updated more recently in the working one, presumably when the linbox spkg was installed.  There are plenty of .la files with the wrong path in the working version.  The output from the working version:

```
-rwxr-xr-x`@` 1 palmieri  admin   779 Feb 23  2008 local/lib/libgfortran.la*
-rwxr-xr-x  1 palmieri  admin   975 Sep 24 08:23 local/lib/libpng12.la*
-rwxr-xr-x  1 palmieri  admin   832 Sep 24 08:24 local/lib/libgc.la*
-rwxr-xr-x  1 palmieri  admin   902 Sep 24 08:24 local/lib/libcord.la*
-rwxr-xr-x  1 palmieri  admin   983 Sep 24 08:27 local/lib/libm4ri.la*
-rwxr-xr-x  1 palmieri  admin   827 Sep 24 08:28 local/lib/libmpir.la*
-rwxr-xr-x  1 palmieri  admin   897 Sep 24 08:28 local/lib/libmpirxx.la*
-rwxr-xr-x  1 palmieri  admin   890 Sep 24 08:28 local/lib/libgmpxx.la*
-rwxr-xr-x  1 palmieri  admin   821 Sep 24 08:28 local/lib/libgmp.la*
-rwxr-xr-x  1 palmieri  admin   857 Sep 24 08:30 local/lib/libsqlite3.la*
-rwxr-xr-x  1 palmieri  admin   887 Sep 24 08:31 local/lib/libgpg-error.la*
-rwxr-xr-x  1 palmieri  admin   879 Sep 24 08:37 local/lib/libecm.la*
-rwxr-xr-x  1 palmieri  admin  1066 Sep 24 08:38 local/lib/libmpfr.la*
-rwxr-xr-x  1 palmieri  admin   980 Sep 24 08:42 local/lib/libgivaro.la*
-rwxr-xr-x  1 palmieri  admin  1068 Sep 24 08:44 local/lib/libglpk.la*
-rwxr-xr-x  1 palmieri  admin   852 Sep 24 08:44 local/lib/libmpfi.la*
-rwxr-xr-x  1 palmieri  admin   982 Sep 24 08:55 local/lib/libgcrypt.la*
-rwxr-xr-x  1 palmieri  admin  1023 Sep 24 09:01 local/lib/libfplll.la*
-rwxr-xr-x  1 palmieri  admin  1053 Sep 24 09:01 local/lib/libopencdk.la*
-rwxr-xr-x  1 palmieri  admin  1084 Sep 24 09:02 local/lib/libgnutls.la*
-rwxr-xr-x  1 palmieri  admin  1272 Sep 24 09:02 local/lib/libgnutls-openssl.la*
-rwxr-xr-x  1 palmieri  admin  1321 Sep 24 09:02 local/lib/libgnutls-extra.la*
-rwxr-xr-x  1 palmieri  admin   945 Oct 23 10:46 local/lib/libcdd.la*
-rwxr-xr-x  1 palmieri  admin  1075 Oct 23 10:46 local/lib/libcddgmp.la*
-rwxr-xr-x  1 palmieri  admin   876 Oct 23 10:53 local/lib/libfreetype.la*
-rwxr-xr-x  1 palmieri  admin  1087 Oct 23 10:54 local/lib/libgd.la*
-rwxr-xr-x  1 palmieri  admin   979 Oct 23 10:59 local/lib/libgslcblas.la*
-rwxr-xr-x  1 palmieri  admin   951 Oct 23 10:59 local/lib/libgsl.la*
-rwxr-xr-x  1 palmieri  admin  1044 Oct 23 11:02 local/lib/libpynac.la*
-rwxr-xr-x  1 palmieri  admin   951 Oct 23 11:37 local/lib/libiml.la*
-rwxr-xr-x  1 palmieri  admin  1236 Oct 23 11:41 local/lib/liblinboxsage.la*
-rwxr-xr-x  1 palmieri  admin  1206 Oct 23 11:41 local/lib/liblinbox.la*
```


I think this is the difference, although I haven't tested it: I had a directory "/Applications/sage_builds/sage-4.5.3".  In the broken one, I copied this to another directory, sage-4.6.rc0, and then I moved the original directory (so that any references to it would fail).  When upgrading the working version, I left the old directory in place.


---

Comment by leif created at 2010-10-23 20:08:59

So it appears to be a bug in `sage-location`?

Can you track this further down on a follow-up ticket? Works for me on Linuces...

Perhaps copy all `.la` files to a temporary directory, move Sage (and run `./sage -c quit` to invoke `sage-location`), and then compare them.


---

Comment by jhpalmieri created at 2010-10-23 21:15:41

Okay, the problem is this: if you build Sage but never run it, then the script sage-location doesn't get run, so the file SAGE_ROOT/local/lib/sage-location.txt doesn't get created.  Then if you move or copy that directory, the file isn't there, so sage-location thinks everything is okay, so it doesn't rewrite the .la files.

(This is despite the comment in sage-location that the files in local/lib get written "during the build".  This is also not platform-specific: I just built on sage.math, and there is no file sage-location.txt until Sage gets run for the first time.  I was also wondering why I wasn't seeing the message "The Sage install tree may have moved..." at the start of the upgrade, and this explains it.)

See #10162 for a follow-up; it's a one-liner.


---

Comment by mpatel created at 2010-10-27 09:06:12

Replying to [comment:153 jhpalmieri]:
> Anyway, I guess now I'm happy with all but one of the patches (trac_9896-fix_extension_module_deps-sagelib.patch), and someone else will have to help with that.

I'll try to review this later today.


---

Comment by mpatel created at 2010-10-27 10:24:58

John Cremona, do you happen to see any problems in [attachment:trac_9896-fix_extension_module_deps-sagelib.patch]?


---

Comment by cremona created at 2010-10-27 10:47:35

Replying to [comment:169 mpatel]:
> John Cremona, do you happen to see any problems in [attachment:trac_9896-fix_extension_module_deps-sagelib.patch]?

Thanks for asking.  For the include files listed, I assume that someone has just gone through the relevant pyx files and listed which of my header files are actually used?  I am not sure whether the point here is that (a) if some files are omitted from this list then the build will fail, or (b) if some are omitted then upgrading will not know to recompile something.  If (a) then the test is just to see if Sage builds!  If (b) I hardly think it matters since either all of eclib is built or none of it, surely?

It is quite possible that everything I have just said is complete nonsense.  If so sorry.

About including the pari library:  Leif explained this to some extent on sage-devel.  I don't know (especially not what may or may not happen on cygwin) sp perhaps it is safer to leave it in?

If anyone ever has suggestions for improving the Makefiles for eclib I am always happy to receive them.  They were created during SD6 by editing old Makefiles of my own which had been evolving over years, so there may well be stuff in there which should not be.

Short answer: no.


---

Comment by mpatel created at 2010-10-27 12:03:47

I think we need to list eclib headers for these modules, so that during an upgrade, if the eclib package is rebuilt, because eclib and/or a dependent package has changed, the modules are also rebuilt.  Is this correct?

I see

```sh
$ cd sage-4.6.rc0/devel/sage/sage/libs/mwrank
$ grep "eclib/" *.c* *.h
wrap.cc:#include "eclib/htconst.h"
wrap.cc:#include "eclib/interface.h"
wrap.h:#include "eclib/curve.h"
wrap.h:#include "eclib/egr.h"    
wrap.h:#include "eclib/descent.h"
wrap.h:#include "eclib/points.h"
wrap.h:#include "eclib/isogs.h"
wrap.h:#include "eclib/marith.h" 
wrap.h:EXTERN void two_descent_saturate(struct two_descent* t, long sat_bd); // = -1 for default set in eclib/src/qcurves/saturate.h (currently 100)
```

and

```sh
$ cd sage-4.6.rc0/devel/sage/sage/libs/cremona
$ grep "eclib/" *.cpp | grep -v cdef
homspace.cpp:#include "eclib/moddata.h"
homspace.cpp:#include "eclib/symb.h"
homspace.cpp:#include "eclib/cusp.h"
homspace.cpp:#include "eclib/homspace.h"
mat.cpp:#include "eclib/moddata.h"
mat.cpp:#include "eclib/symb.h"
mat.cpp:#include "eclib/cusp.h"
mat.cpp:#include "eclib/homspace.h"
newforms.cpp:#include "eclib/interface.h"
newforms.cpp:#include "eclib/bigrat.h"
newforms.cpp:#include "eclib/rat.h"
newforms.cpp:#include "eclib/curve.h"
newforms.cpp:#include "eclib/moddata.h"
newforms.cpp:#include "eclib/symb.h"
newforms.cpp:#include "eclib/cusp.h"
newforms.cpp:#include "eclib/xsplit.h"
newforms.cpp:#include "eclib/method.h"
newforms.cpp:#include "eclib/oldforms.h"
newforms.cpp:#include "eclib/homspace.h"
newforms.cpp:#include "eclib/cperiods.h"
newforms.cpp:#include "eclib/newforms.h"
```

For `homspace` and `mat`, do we need to mention in `module_list.py` the `eclib/` headers that aren't listed above?


---

Comment by cremona created at 2010-10-27 14:16:50

I agree that these modules need to be rebuilt if eclib is rebuilt;  but I don't see why that means that we have to list header files individually.  Can't we make these modules depend on the spkg itself?


---

Comment by leif created at 2010-10-27 15:58:32

Replying to [comment:170 cremona]:
> Replying to [comment:169 mpatel]:
> > John Cremona, do you happen to see any problems in [attachment:trac_9896-fix_extension_module_deps-sagelib.patch]?
> 
> Thanks for asking.  For the include files listed, I assume that someone has just gone through the relevant pyx files and listed which of my header files are actually used?  

Exactly. I did that some weeks ago when debugging the original problem...

If any of these header files (to be precise, its modification time) changes, an extension module having it in its dependencies will get rebuilt. (The problem was this did not happen when ECLIB got rebuilt, such that these modules still used - or better: pulled-in - the old PARI library, which resulted in segfaults or import / dynamic linker errors.) 

Perhaps a little overkill (we just could rebuild all of these modules if _any_ ECLIB header file changes), but as is may save some unnecessary rebuilds. ;-)

> About including the pari library:  Leif explained this to some extent on sage-devel.  I don't know (especially not what may or may not happen on cygwin) so perhaps it is safer to leave it in?

Well, I kept it for the moment (here; #9914 would remove the PARI library).

> If anyone ever has suggestions for improving the Makefiles for eclib I am always happy to receive them.  They were created during SD6 by editing old Makefiles of my own which had been evolving over years, so there may well be stuff in there which should not be.

Ok, I have some patched ECLIB spkg somewhere around. Perhaps needs some more work though.


---

Comment by leif created at 2010-10-27 16:19:42

Replying to [comment:172 cremona]:
> I agree that these modules need to be rebuilt if eclib is rebuilt;  but I don't see why that means that we have to list header files individually.  Can't we make these modules depend on the spkg itself?

The most generic way would be to make any extension module (explicitly) depend on the libraries it is linked to. (Though this certainly would also trigger unnecessary rebuilds, but is easy to implement and safe, assuming libraries change when there headers do.)

Robert B. wanted to improve Cython s.t. we get rid of most of `module_list.py` (by using pragmas like `clib ...` etc. in the Cython files), which I think would also handle the true dependencies properly.

So I considered my change more or less temporary, and didn't address the dependencies of other modules *currently* not causing trouble. (As mentioned earlier, upgrading e.g. MPIR (#8664) will require further changes, and unless we get an improved Cython until then, I'll implement the above strategy in `setup.py`, but of course on another ticket. This one was at least originally meant to only or especially address the PARI upgrade, i.e. upgrading Sage to a version with the new PARI from one with the old.)


---

Comment by mpatel created at 2010-10-28 01:20:41

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-10-28 01:43:34

Thanks for finishing off the review.


---

Comment by jdemeyer created at 2010-10-28 07:30:25

Great!


---

Comment by leif created at 2010-10-28 07:39:12

Replying to [comment:177 jdemeyer]:
> Great!

The final review? We've only reached comment !#178... ;-)

Yes, thanks to you for setting up the test upgrade paths, and the reviewers!

(#9914 is still an open question.)


---

Comment by drkirkby created at 2010-10-28 08:25:12

Given the number of things that look to be needed to update this, it would be good if one could create a small shell script, something like

{{{#!/bin/sh
cd devel/sage
hg qimport /patch/to/raw-patch1
hg qpush
hg qimport /patch/to/raw-patch2
etc
```

so that we could check it easily. At the moment, looking at all those patches, it is rather off-putting!

Dave


---

Comment by mpatel created at 2010-10-30 09:39:17

Resolution: fixed


---

Comment by jhpalmieri created at 2010-11-03 19:47:37

A followup: on my mac, perhaps because of various symbolic links, whenever I run "sage -b", I see a message like

```
warning: Replacing library search directory in linker command:
  "/Applications/sage_builds/sage-4.6/local/lib" -> "/Applications/sage/local/lib"
```

I can run "sage -b" three times in a row, and I see this message all three times.

This may be because of symbolic links: "/Applications/sage" is a link pointing to "/Applications/sage_builds/sage-4.6/".

Perhaps in setup.py, we should use os.path.realpath?  For example, 

```diff
diff -r cdc586ffbdfd setup.py
--- a/setup.py  Mon Sep 13 00:52:40 2010 -0700
+++ b/setup.py  Wed Nov 03 12:46:51 2010 -0700
`@``@` -391,7 +391,7 `@``@`
                     self.debug_print(
                       "Library dir found in dynamic linker command: " +
                       "\"%s\"" % libdir)
-                    if libdir != sage_libdir:
+                    if os.path.realpath(libdir) != os.path.realpath(sage_libdir):
                         self.compiler.warn(
                           "Replacing library search directory in linker " +
                           "command:\n  \"%s\" -> \"%s\"\n" % (libdir,
```

If this sounds like a good idea, I can open a new ticket with this patch.


---

Comment by leif created at 2010-11-03 20:42:30

Replying to [comment:181 jhpalmieri]:
> A followup: on my mac, perhaps because of various symbolic links, whenever I run "sage -b", I see a message like

```
warning: Replacing library search directory in linker command:
  "/Applications/sage_builds/sage-4.6/local/lib" -> "/Applications/sage/local/lib"
```

> I can run "sage -b" three times in a row, and I see this message all three times.

Of course. `distutils` reads the Python Makefile each time it is invoked by the Sage library's `setup()`; we do not (yet) patch that Makefile and `pyconfig,h`.


> This may be because of symbolic links: "/Applications/sage" is a link pointing to "/Applications/sage_builds/sage-4.6/".

Yep.


> Perhaps in setup.py, we should use os.path.realpath?
> If this sounds like a good idea, I can open a new ticket with this patch.

Well, it's just a warning; feel free to open a ticket for that, and I'll probably review it. ;-)


---

Comment by jhpalmieri created at 2010-11-03 21:00:46

See #10208.  I agree that it is just a warning, but it's a warning when there is nothing actually wrong, which might be distracting...
