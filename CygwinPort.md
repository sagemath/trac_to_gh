
 This page is for tracking working specifically on the 32-bit version of Cygwin.  This work is currently in stasis for a few reasons:

* The number of users with 32-bit versions of Windows is declining.  While we have encountered students with older laptops running 32-bit versions of Windows 7, and would like to be able to support them, chances are in a few years that number will be almost zero, as 32-bit Windows 8 and up is almost unheard of (though also probably not non-existent).

* Supporting Sage on 32-bit !Cygwin/Windows has greater technical challenges than the 64-bit version.  In particular, the more constrained address space for user-mode processes on 32-bit Windows (2GB by default--3GB with a special boot parameter) can be very limiting.  See in particular issue [#22186](https://trac.sagemath.org/ticket/22186).

* Current development of Cygwin is focused primarily on the 64-bit version.  While the 32-bit version of Cygwin is still supported, it is not supported _as well_ and most new development targets the 64-bit version.

For the full list of open issues specific to 32-bit Cygwin see the [cygwin32 keyword](https://trac.sagemath.org/query?status=needs_info&status=needs_review&status=needs_work&status=new&status=positive_review&keywords=~cygwin32&component=porting%3A+Cygwin&col=id&col=summary&col=component&col=status&col=type&col=priority&col=milestone&order=priority).

*All active work on Cygwin support* is on the 64-bit version which is tracked at [wiki:Cygwin64Port].

----


# Archived information for the Cygwin port

As of Sage 5.9.beta4, Sage should build "out of the box" with a Cygwin that has the same prereqs as any other Sage, with the very minor caveats below, and start.  See [#6743](https://trac.sagemath.org/ticket/6743) or below for more details. The only exception is that rebase and forking problems continue (see below and [#14031](https://trac.sagemath.org/ticket/14031)).  The _only_ special prerequisites are
 * That the gcc versions must match, if you install gcc4-core, gcc4-gfortran, and gcc4-g++ (with just gcc4-core, Sage's gcc 4.7.x gets built)
 * That we need liblapack-devel and lapack
We no longer need `SAGE_PORT=yes`, as of this release!

See  [wiki:Cygwin64Port] for the Cygwin64 port and for **current info** on the Cygwin port status.
**All further testing/progress will be posted on that page!!

 * Below are the list of prerequisites, bug fixes/upgrades needed for Cygwin to build, and doctest tickets for Cygwin
 * We try to keep these notes current, but some may be dependent on Sage version (5.2, 5.5, etc.). See bottom of this page for recent build attempts.
 * Closed tickets and some other information, like how to mark Cygwin-specific parts in C, is here as well
 * Although below it compares Windows 7 and Windows XP, it is conceivable that the Cygwin version also sometimes has something to do with the problems listed


## Cygwin Build Notes

### Prerequisites
These Cygwin packages need to be installed in order for the Sage build to complete.  Eventually, these should be added to prereq, but that would be for when Cygwin is actually supported.

Also, many of these require things like zlib and other included Sage packages, so it would probably be possible to remove a lot of those from a Sage Cygwin tarball (with effort).

 * file, liblapack, liblapack0, liblapack-devel, patch
 * also libiconv and openssl, openssl-devel
 * Windows 7 additional requirements
   * libncurses-devel (to build Singular)
   * zlib-devel (but see [#13914](https://trac.sagemath.org/ticket/13914))
 * Reminders for compilers
   * Don't forget fortran
   * Make sure you download all gcc and g++ so the versions match
 * Useful other things to install, especially on a minimal install of Cygwin
   * gcc, make, m4, and perl are needed
   * not strictly needed but very useful are wget, ssh and scp
   * similarly and nano or vim or something to edit files with
 * Make sure you uninstall the applications interfering with Cygwin, see [BLODA](http://cygwin.com/faq/faq.using.html#faq.using.bloda) (Big List Of Dodgy Apps), including:
   * antivirus programs
   * antispyware programs
   * etc etc etc


### Rebasing
At any point in the build process (or after), one can get forking problems, related to the fact that Windows can relocate a dynamic library that just called fork() to another place in memory, causing fork() failure (this is a "feature" of the current Cygwin fork() implementation on Win32). To decrease the probability of this happening, you may need to rebase all the Cygwin and Sage DLLs you have so far, i.e. allocate each its own space address to load in (otherwise they compete for the space).

 * See [these build notes of William's](https://groups.google.com/d/msg/sage-windows/ygK1kJm9p9w/XKyuJfiMlgYJ) for a fairly effective strategy to deal with this. (But ignore the parts (4) and (5)  about editing the list of Sage dlls, this is no longer necessary since [#12096](https://trac.sagemath.org/ticket/12096).)
 * In order to use this, you will need to run the 'ash' shell (or 'dash' shell) from the Windows command line.
   * This will require closing all Cygwin applications, and doing `C:\cygwin\bin\ash.exe` or something similar instead of just `ash`.
   * For ash to actually find any commands, you may need to follow the tips at [this blog post](http://thehacklist.blogspot.com/2009/04/cygwin-ls-command-not-found.html) for setting the `CYGWIN_HOME` variable and prepending the Cygwin binary directory (usually `C:\cygwin\bin`) to the `Path` variable.
   * You may also have problems with permissions (getting a message about "is not writable").  [This cyg-apt thread](http://code.google.com/p/cyg-apt/issues/detail?id=8) seems to have several solutions for this.
   * [#14031](https://trac.sagemath.org/ticket/14031) aims to make this process less painful: one would need just run a MSDOS batch file (after closing all the cygwin apps)


### Porting!
Also, don't forget to `export SAGE_PORT=yes` before starting.


## Build Tickets
 * [#6743](https://trac.sagemath.org/ticket/6743): A metaticket for exactly this, which also points here.  Can be closed when Sage builds out of the box with the prerequisites above. Be aware that exactly what tickets/spkgs are needed depends on which alpha or release you use; read carefully to make sure the spkgs coincide.

 * [#13324](https://trac.sagemath.org/ticket/13324): ECL
 * [#13137](https://trac.sagemath.org/ticket/13137): MPIR
 * [#13804](https://trac.sagemath.org/ticket/13804): fpLLL (Win 7 only)
 * [#13806](https://trac.sagemath.org/ticket/13806): complex double build (Win 7 only)
 * [#11635](https://trac.sagemath.org/ticket/11635): NTL (not strictly needed for building, but for starting)
 * [#13954](https://trac.sagemath.org/ticket/13954): GAP

### Things without tickets
 * in some cases, untarring the Sage source needs to be done with options xopf, not just xf (observed on Win7)
 * Issue with Python 2.6.4 building on Win7 reported.  This seems to no longer be a problem with 2.7.x - see this page's history for previous comments


## Getting Sage to start
 * [#11635](https://trac.sagemath.org/ticket/11635): Also copy "libntl.dll.a -> libntl.dll" (see ticket for why this was split off from the previous one) - [#12104](https://trac.sagemath.org/ticket/12104) is a dup, as it turns out


## Doctest Tickets
 * [#9165](https://trac.sagemath.org/ticket/9165) -- lcalc does not work for elliptic curves on cygwin
 * [#9167](https://trac.sagemath.org/ticket/9167) -- importing sage.libs.ecl yields a "no such process" error
 * [#9168](https://trac.sagemath.org/ticket/9168) --  ratpoints does not work correctly
 * [#9169](https://trac.sagemath.org/ticket/9169) -- a cachefunc.py doctest hangs seemingly forever
 * [#9170](https://trac.sagemath.org/ticket/9170) -- get_memory_usage isn't implemented, e.g., because there's no top
 * [#9171](https://trac.sagemath.org/ticket/9171) -- some test failures in sagedoc.py
 * [#9172](https://trac.sagemath.org/ticket/9172) -- numerical noise in sage/rings/integer.pyx
 * [#9173](https://trac.sagemath.org/ticket/9173) -- BSD.py tests behave differently on cygwin, so need to be written to reflect that
 * [#9174](https://trac.sagemath.org/ticket/9174) -- robert miller's 2-descent is completely broken on cygwin
 * [#9176](https://trac.sagemath.org/ticket/9176) -- various heegner_index errors involving interval arithmetic on cygwin


## Other Tickets
 * [#8854](https://trac.sagemath.org/ticket/8854) -- Sage segfaults on upgrade
 * [#9164](https://trac.sagemath.org/ticket/9164) -- gap.cputime error
 * [#13343](https://trac.sagemath.org/ticket/13343) -- uppercase characters in path
 * [#13350](https://trac.sagemath.org/ticket/13350) -- import rpy2
 * [#13351](https://trac.sagemath.org/ticket/13351) -- import lcalc
 * [#13354](https://trac.sagemath.org/ticket/13354) -- autotools and shared libraries


## Closed
  * See [this Trac search](http://trac.sagemath.org/sage_trac/query?status=closed&component=porting%3A+Cygwin&col=id&col=summary&col=component&col=status&col=type&col=priority&col=milestone&order=priority) for closed tickets in the Cygwin component.


## how to mark CYGWIN-specific parts in code
gcc on CYGWIN defines a variable `__CYGWIN__`. So you can use it to #if(n)def stuff.


## old Cygwin binaries
(Old) Cygwin prebuilt sage binaries for cygwin are here:  http://sage.math.washington.edu/home/wstein/binaries/cygwin/


## Recent tests


### Testing Sage 5.1.rc1 on Windows 7 64 bits with Cygwin 1.7.15
Let's put here reports of my WIP. When this is finished, I'll reformat everything in a more proper way.

 * The version of gcc is hardcoded in /bin/libtool, if you happen to use 4.5.3 rather than 4.3.4 you'll have to edit /bin/libtool
 * As noted above, you should surely rebase (your system once, and) the libraries build by Sage from time to time when fork errors occurs before restarting the compilation
 * I also got quite often cannot allocate memory errors, which could (only) be solved by restarting my computer (memleak somewhere in cygwin?)
 * [#12115](https://trac.sagemath.org/ticket/12115) : MPIR cannot be built both as a static and a shared library, lets try only shared for the time being, although that may not be the most sensible choice
 * ABI=32 must be set to build MPIR on 64 bits systems
 * Python 2.7.3 does not compile, fixes from issues 9665, 14437, 14438 in Python issue tracker are needed
 * ECL does not build with recent Cygwin version because fd_set does not get defined. See https://groups.google.com/forum/?fromgroups#!topic/sage-devel/7e-CCbRLpto
 * eclib fails with undefined references to gmp -> -lgmp should come at the end of the command line for gcc to correctly take it into account
 * eclib fails in make tests -> disable as a workaround in Makefile.in (somehow eclib/*.h are not found because AM_CPPFLAGS is not used and so the include path are not set...)
 * flint-1.5.2.p0 fails to apply the patch for longlong.h because of bad line breaks in the patch file, same problem in mpn_extras.patch
 * the libntl.a hack in flint spkg-install is not needed anymore since [#9050](https://trac.sagemath.org/ticket/9050) (which is not a really good solution, gcc should be told to generate a proper .dll.a file)
 * polybori from [#13124](https://trac.sagemath.org/ticket/13124) is needed
 * singular fails with ld not finding -lkernel and -lhtmlhelp, see http://wstein.org/home/wstein/www/home/keshav/irclogs/%23sagemath.2011-11-26.log, this can be fixed by modifying LDFLAGS in Singular/Makefile.in  to include -L../kernel even on Windows (and not -L/bin which seems useless) (this is [#12089](https://trac.sagemath.org/ticket/12089))
 * libpari.dll should be moved to libpari.dll.a to be linked with (rather than libpari.a, which anyway looks dysfunctional) so that the Sage library can be built
 * gmp should be added as a dependency to ecl.pyx in modules_list to avoid undefined references
 * matrix_modn_dense_float fails with ndefined references in givaro. Change order of dependencies in module_list.
 * in modules_list.pyx, farey_symbol.pyx should include gmpxx AND gmp; but that's not enough yet: undefined reference to convert_to_long and things defined in farey_symbol.pyx, to solve this second problem, one can add a extra_compiler_flags="-Wl,--enable-auto-import" to the farey stuff in module_list. A better way could be to let Cytohn add _declspec(dll[im|exp]port) things in farey_symbol.h
 * complex_double linking fails because of -lmc not found -> indeed, this was not built (don't know what it should be), solution: remove it from module_list
 * expression.pyx fails, seems related to http://www.mail-archive.com/debian-bugs-dist`@`lists.debian.org/msg163112.html. Somehow g++ does not realize that the infinity class used in the templates is the one from pynac. Maybe some name clash with Python/Cython/Sage things in sage.rings.infinity[.infinity .infinity]. So letting g++ know that infinity is GiNaC::infinity should do the trick (I did that by modifying the cpp file produced by Cython which was hackish but quick), explicitly writing GiNaC::infinity in ginac.h in sage.libs solves the problem
 * undefined references in stl_vectors solved by adding the correct library dependencies in modules_list
 * undefined references in wrapper_rdf because of a functions defined in interp_rdf and seemingly correctly shown by nm in both files. Changing the order of the files in the linking command, and adding -no-undefined flag, did not solve the problem yet. It seems that there are incorrect `__imp__` prefix added to the symbols of the interp_* functions when wrapper_*.o is built. Because of that, the functions are looked to be imported from some .dll rather .o file. Indeed, building an independent .dll for interp_* and then linking wrapper_* to it to produce wrapper_*.dll works. To only have one wrapper_*.dll I've added an header file for interp_*.c and included it as cdef extern from "interp_*.h" in wrapper_*.pyx rather than without the from part as before. This seems functional, but needs non-trivial modifications to gen_interpreter.py.
 * Apart from that, one of the modules built by gen_interpreter.py linked to the mc library which is not available on my system (also had that problem for some module build in module_list.py).
 * gap fails because an old ln trick which used to be needed now fails.
 * maxima was a pain to build, not sure if that's a local problem, but after the "make" stage, the "make install" stage always failed with fork errors (cannot commit memory...). So I just let the "make" stage finish, rebase my system, and go on with the process, which seems ok (I can ./sage -maxima and compute 1+1)
 * finally sage finished to build but would not start. Just copying libntl.dll.a to libntl.dll was enough (this is [#11635](https://trac.sagemath.org/ticket/11635))
 * some elliptic curve stuff worked ok, but the notebook did not start in the first session (something about an alarm set at 1 second, maybe it was just too slow) and then was ok!


### Testing sage 5.2 on cygwin 1.7.16 on Windows 7 64 bits
Let's do the same thing as before with updated and freshly installed cygwin/sage, but opening tickets this time in addition to posting the progress here.

Recall that the procedure to rebase is to:

 * kill all cygwin processes (i.e. close all cygwin terminal windows, and shut down cygwin services, if any)
 * launch dash.exe (in .../cygwin/bin) as admin (sometimes you might need to use ash.exe instead, as C:\cygwin\bin\ash.exe)
 * cd $SAGE_ROOT (i.e. to the root of the currently building Sage install, or just cd / which should be a parent of the former)
 * /bin/find . -name *.dll > sage-dlls.lst  (warning: on some systems to get this to actually find the right stuff you may need /bin/find . -name "*.dll" > sage-dlls.lst)
 * /bin/rebaseall -T sage-dlls.lst (you add -v flag to get verbose output and check that the currently building Sage dlls are rebased)

I still had problems with libtool (which I installed when I wanted to test an updated NTL spkg using the system libtool).
I think it is because I installed libtool after installing the gcc packages.
Therefore the postinstall scripts included in the gcc packages did not have the chance to modify the hardcoded path in libtool (unless there is also some such script in the libtool package itself).
Anyway, reinstalling gcc packages did not solve the problem.
Paths in sys_lib_search_path_spec where updated, but not in compiler_lib_search_dirs, predep_objects, postdep_objects, compiler_lib_search_path.
The /usr/sbin/fix... script with is run be gcc4-core package (at least) does not update these paths.
The other package do not seem to update any path by themselves.
I'll file a Cygwin bug report.

Avoid to build Sage in a path involving uppercase letters or ECL might get upset! See [#13343](https://trac.sagemath.org/ticket/13343).

Here follow the problem encountered while building Sage:

 * The python-2.7.3.p0.spkg fails as before. This is now [#13319](https://trac.sagemath.org/ticket/13319). The python-2.7.3.p1.spkg from there installs fine.
 * The mercurial-2.2.2.p0.spkg fails because of a fork errors. Rebasing solves the problem.
 * The mpir-2.4.0.p6.spkg fails as before. This is [#12115](https://trac.sagemath.org/ticket/12115). The mpir-2.4.0.p7.spkg from there installs fine.
 * Second rebase needed to be able to build matplotlib.
 * The ecl-[... ...].p1.spkg failed as above. This is now [#13324](https://trac.sagemath.org/ticket/13324). The ecl-[... ...].p2.spkg from there installs fine.
 * Install PARI spkg from [#13333](https://trac.sagemath.org/ticket/13333), to make sure that the `libpari.dll.a` import file gets installed.
 * The eclib spkg fails as above. This is now [#13325](https://trac.sagemath.org/ticket/13325). The *.p0.spkg from there installs fine after installing PARI spkg from [#13333](https://trac.sagemath.org/ticket/13333).
 * The flint-1.5.2.p0.spkg fails as above. This is now [#13330](https://trac.sagemath.org/ticket/13330). The p1 spkg from there installs fine.
 * Singular fails as above. See [#12089](https://trac.sagemath.org/ticket/12089). Updated spkg from [#13237](https://trac.sagemath.org/ticket/13237) works fine.
 * Got segfaults during the tuning phase of zn_poly-0.9.p9.spkg. Rebooting solved the problem...
 * Now building the Sage library itself:
   * Failed for ecl.pyx as above. This is now [#13334](https://trac.sagemath.org/ticket/13334).
   * Failed for matrix_modn_dense_float.pyx and matrix_mod_dense_double.pyx as above. This is now [#13335](https://trac.sagemath.org/ticket/13335).
   * Failed for farey.pyx as above. This is now [#13336](https://trac.sagemath.org/ticket/13336).
   * Failed for expression.pyx as above. This is now [#13337](https://trac.sagemath.org/ticket/13337).
   * Failed for stl_vector.pyx as above. This is now [#13338](https://trac.sagemath.org/ticket/13338).
   * Failed for wrapper_*.pyx as above. This is now [#13339](https://trac.sagemath.org/ticket/13339).
 * The gap-4.4.12.p7.spkg fails. This is now [#13341](https://trac.sagemath.org/ticket/13341). The *.p8.spkg from there installs fine.
 * The sagenb-0.9.1.spkg fails while installing pyOpenSSL-0.12.tar.gz because of  Singular's file Singular/LIB/crypto.lib which is installed in local/lib/crypto.lib. See [#13344](https://trac.sagemath.org/ticket/13344). Updated spkg from [#13237](https://trac.sagemath.org/ticket/13237) works fine.
 * No fork problems with Maxima this time! (but beware of [#13343](https://trac.sagemath.org/ticket/13343) !)
 * Build finished ok, but "Testing that Sage starts..." failed with fork errors. Rebasing solved the problem, although I got "Warning: Could not import sage.interfaces.maxima_lib No such process". This is [#9167](https://trac.sagemath.org/ticket/9167). Need NTL trick as well, this is [#11635](https://trac.sagemath.org/ticket/11635).
 * While building the reference manual, I got "from sage.libs.ecl import * ImportError: No such process". This is [#9167](https://trac.sagemath.org/ticket/9167) as well.
 * Once again, got some alarm problems when starting the notebook: "KeyboardInterrupt: computation timed out because alarm was set for 1 seconds", but trying several times let it start.
 * "./sage -gdb" fails with
   "Reading symbols from /home/jp/sage-5.2/local/bin/python...done.
   /home/jp/sage-5.2/local/bin/sage-gdb-commands:1: Error in sourced command file:
   Error creating process /home/jp/sage-5.2/local/bin/python, (error 87)."
 * Now running "make test".

It should be noted that some libraries were only build in static version although building a shared version should not be a problem, but just a matter of passing -no-undefined to libtool when it is invoked in link mode (adding --no-undefined to LDFLAGS might not work, nor adding -Wl,--no-undefined to C[XX]FLAGS flags, it is really libtool which must be convinced it is not an issue and it doesn't care about the previous env variables) so that libtool does not complain, this is now [#13354](https://trac.sagemath.org/ticket/13354) (see there for current status).

Some worrying cygcheck output:
```
(sage-sh) jp`@`THINKPAD:~/sage-5.2$ for d in `find . -name *.dll`; do t=`cygcheck $d 2>&1|grep "not find"`; if [ -n "$t" ]; then echo $d; echo $t; fi; done
./devel/sage-main/build/lib.cygwin-1.7.16-i686-2.7/sage/libs/lcalc/lcalc_Lfunction.dll
cygcheck: track_down: could not find libLfunction.so
./devel/sage-main/build/sage/libs/lcalc/lcalc_Lfunction.dll
cygcheck: track_down: could not find libLfunction.so
./local/lib/python2.7/site-packages/rpy2/rinterface/rinterface.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/class/libs/class.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/cluster/libs/cluster.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/foreign/libs/foreign.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/grDevices/libs/grDevices.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/grid/libs/grid.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/KernSmooth/libs/KernSmooth.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/lattice/libs/lattice.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/MASS/libs/MASS.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/Matrix/libs/Matrix.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/methods/libs/methods.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/mgcv/libs/mgcv.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/nlme/libs/nlme.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/nnet/libs/nnet.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/parallel/libs/parallel.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/rpart/libs/rpart.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/spatial/libs/spatial.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/splines/libs/splines.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/stats/libs/stats.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/survival/libs/survival.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/library/tools/libs/tools.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/modules/internet.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/modules/lapack.dll
cygcheck: track_down: could not find libR.dll
./local/lib/R/modules/vfonts.dll
cygcheck: track_down: could not find libR.dll
```
Follow-up tickets:
* the lcalc_Lfunction is now [#13351](https://trac.sagemath.org/ticket/13351),
* the rpy2.rinterface.rinterface is now [#13350](https://trac.sagemath.org/ticket/13350),
* the R/modules/* errors are harmless.

Doctest failures:
```

```
Follow-up tickets:
* sage.libs.mwrank.mwrank seems dysfunctional. Linking it to a shared version of eclib provided in [#13325](https://trac.sagemath.org/ticket/13325) solves the problem.



### Testing Sage 5.4.rc on Windows XP
So far, following the above instructions, all goes more or less well.  Python still reports missing some bits (_bsddb, _tkinter, bsddb185, gdbm, linuxaudiodev, his, osaudiodev, spwd, and sunaudiodev) and at the very beginning it was missing one of the sqrtl() functions, but `SAGE_PORT=yes` caused it to ignore this.  A missing library to link against (gmp) in cvxopt means that one doesn't build (this is now [#13799](https://trac.sagemath.org/ticket/13799)), but everything else does with all the above.  And Sage starts, and import ecl works with the appropriate ticket above.  A number of doctest errors, at least some of which seem to be due to forking problems, still exist.



### Testing Sage 5.5.rc0 on Windows XP
I'm going to try this with the spkgs from:
 * [#11635](https://trac.sagemath.org/ticket/11635) (NTL)
 * [#13324](https://trac.sagemath.org/ticket/13324) (ECL, but *not* including [#9167](https://trac.sagemath.org/ticket/9167) yet)
 * [#13137](https://trac.sagemath.org/ticket/13137) (MPIR)
 * Had to pretend to build cvxopt due to [#13799](https://trac.sagemath.org/ticket/13799)
 * [#13325](https://trac.sagemath.org/ticket/13325) (eclib)
 * [#13319](https://trac.sagemath.org/ticket/13319) (Python, based on [#13631](https://trac.sagemath.org/ticket/13631))
If all goes well, I'll update [#6743](https://trac.sagemath.org/ticket/6743) appropriately.



### Testing Sage 5.5.rc0 on Windows 7 (64 bits)
I'm going the same with the spkgs from:
 * [#11635](https://trac.sagemath.org/ticket/11635) (NTL)
 * [#13324](https://trac.sagemath.org/ticket/13324) (ECL, but *not* including [#9167](https://trac.sagemath.org/ticket/9167) yet)
 * [#13137](https://trac.sagemath.org/ticket/13137) (MPIR)
 * [#13755](https://trac.sagemath.org/ticket/13755) (linbox)
 * [#13325](https://trac.sagemath.org/ticket/13325) (eclib)
 * [#13319](https://trac.sagemath.org/ticket/13319) (Python, based on [#13631](https://trac.sagemath.org/ticket/13631))
 * [#12173](https://trac.sagemath.org/ticket/12173) (FLINT)


### Testing Sage 5.5.rc1 on Windows 7 (64 bits)
I'm testing to build Sage-5.5.rc1 on a minimal Cygwin install on 64 bits Windows 7 with:
 * [#11635](https://trac.sagemath.org/ticket/11635) (NTL)
 * [#13324](https://trac.sagemath.org/ticket/13324) and [#9167](https://trac.sagemath.org/ticket/9167) (ECL)
 * [#13364](https://trac.sagemath.org/ticket/13364) (Maxima)
 * [#13137](https://trac.sagemath.org/ticket/13137) (MPIR)
 * [#13755](https://trac.sagemath.org/ticket/13755) (linbox)
 * [#13325](https://trac.sagemath.org/ticket/13325) (eclib)
 * [#13319](https://trac.sagemath.org/ticket/13319) (Python)
 * [#13802](https://trac.sagemath.org/ticket/13802) (letterplace)
 * [#9543](https://trac.sagemath.org/ticket/9543) and [#13806](https://trac.sagemath.org/ticket/13806) (cephes)
 * [#13804](https://trac.sagemath.org/ticket/13804) (fplll)

About Cygwin packages:

* I had first to install make (to be able to issue make...)
* Then have to export SAGE_PORT to pass through the prereq spkg. But this disables checking for Sage minimal requirements...
* So following http://www.sagemath.org/doc/installation/source.html, I installed:
  * gcc4-core,
  * m4,
  * perl,
  * make was installed above,
  * tar came by default,
  * ranlib came with some of these,
  * it seems file was installed by default.
* The patch spkg complained I had to have patch installed, so I modified it to try to install itself (and for this I installed the Cygwin nano and emacs packages). See [#13844](https://trac.sagemath.org/ticket/13844).
* Now the iconv spkg fails because gcc cannot find /usr/lib/libiconv.la although libiconv was just installed. This is mentioned (without solution) here: http://cygwin.com/ml/cygwin/2012-08/msg00597.html . Got it: iconv is linked with -lintl which points to /lib/libintl.la which itself points to /usr/lib/libiconv.la . See also http://cygwin.com/ml/cygwin/2010-03/msg00373.html . So we have two solutions:
  * Require libiconv as a prereq (remark that libiconv2 is installed by default but does not contain the la file),
  * Patch libiconv configure to use /bin/cygintl-?.dll instead of /lib/libintl.la,
  * Wait for libintl Cyg package (by not including libintl.la) or upstream (by not hardcoding the libiconv.la path) or libtool (by not thinking using -lintl will work)to be fixed.
  * Consider the Cywgin libiconv2 package is now good enough.
  * Configure our iconv not to use libintl/gettext with --disable-nls (that seems to be the best solution for me, but then further spkg might fail and we have to go back to requiring libiconv), for that solution see [#13912](https://trac.sagemath.org/ticket/13912)).
* I'll provide an iconv spkg with the last solution, but for the moment I'm faking its installation anyway to see whether its really needed or not (apparently by R, see [#8191](https://trac.sagemath.org/ticket/8191) and [#8567](https://trac.sagemath.org/ticket/8567)).
* Problems with zlib once again when building libpng. By default only the zlib0 cygwin package is installed, which only contains the dll, not the zlib-devel one which contains headers, import file, static archive... I guess we'll have to make that one a prereq. In fact I think we should not, I think the install of OUR zlib spkg must be somehow broken. Indeed, it seems we do not install the import library, see [#13914](https://trac.sagemath.org/ticket/13914).
* About libpng, I'm a little confused by the copying and removing at the end of spkg-install, this looks very very fishy, I'll remove it for now. See [#11696](https://trac.sagemath.org/ticket/11696) as well although I may provide the SYMBOL_PREFIX fix on an independent ticket.
* gd seems to have trouble detecting libpng now and is missing symbols/functions and gdmodule fails because of that. Indeed the libpng import library is almost empty (and so broken) whence the hack of [#9146](https://trac.sagemath.org/ticket/9146). See http://old.nabble.com/Fwd%3A---libpng-Bugs-2981656---Import-library-definitions-missing-in-Windows-td28130513.html, this is fixed in libpng 1.5. The SYMBOL_PREFIX hack there seems to work (and less hackish than our previous one). But prefer solution although is to properly reenable dllexport as was done for 1.5.
* ecl fails to build with Sage's GCC 4.6.3, same error as http://sourceforge.net/mailarchive/message.php?msg_id=28468685, see http://gcc.gnu.org/bugzilla/show_bug.cgi?id=52061. It is ok with Cygwin earlier GCC or Sage's GCC 4.7.2 (although you'd better craft a stripped down spkg from the all including one in optional which ships all the GCC suite including gcj and gobjc and go and which depends on zip or jar (not installed by default)). Use stripped 4.7.2 at [#13913](https://trac.sagemath.org/ticket/13913).
* The libncurses-devel Cygwin package is indeed needed by Singular (but I don't think its Windows 7 specific). Not really sure anymore about that as I'm rebuilding singular only after a complete sage build, without libncurses-devel, on my 5.6.rc0 install and it does not complain...
* R actually wants iconv.h so I've installed Cygwin's libiconv package (ie the "devel" package not installed by default) and see if its now good enough. And it seems good enough, so either we build our own iconv or prereq iconv-devel, I mean libiconv package... And by the way it does not seem gd module still needs iconv as stated in [#7319](https://trac.sagemath.org/ticket/7319)
* The new Gap spkg request a static GMP, too bad. See [#13954](https://trac.sagemath.org/ticket/13954).


### Testing Sage 5.6.beta2 on Windows XP
 * [#11635](https://trac.sagemath.org/ticket/11635) (NTL)
 * [#13324](https://trac.sagemath.org/ticket/13324) and [#9167](https://trac.sagemath.org/ticket/9167) (ECL)
 * [#13137](https://trac.sagemath.org/ticket/13137) (MPIR)
 * [#9543](https://trac.sagemath.org/ticket/9543) (cephes)
 * [#13804](https://trac.sagemath.org/ticket/13804) (fplll)

Experience:
 * For some reason this fails at GAP with an error about GMP not being where it should be.  Rebasing did not help.  This makes no sense since the same computer did fine with the same spkg above, and it fails whether or not I set `SAGE_CHECK`.  Touching spkg file for now.  (This turned out to probably be [#13954](https://trac.sagemath.org/ticket/13954).)
 * In iml, the test suite only, I get `ld returned 1 exit status`, because it could not find `-lcblas` and `-latlas`.  So not relevant to building, but fails with `SAGE_CHECK=yes`.
 * Failure in polybori with Python forking; after rebase, still failed.  Touching spkg file for now.
 * In r, the test suite only, I got an error in the return of one of the tests which seemed innocuous (extra spaces or something).  So not relevant to building, but it failed with `SAGE_CHECK=yes`.
 * In zn_poly, the test suite only, I got an error in the return of one of the tests also seen on Mac (see [#13137](https://trac.sagemath.org/ticket/13137)).  So not relevant to building, but it failed with `SAGE_CHECK=yes`.  (This turned out to be [#13947](https://trac.sagemath.org/ticket/13947).)
 * Failure to even start building Sage library due to Python forking errors.  After rebasing, the polybori being gone caused a different error (since `$SAGE_LOCAL/share/polybori/flags.conf` were missing) but then forking errors anyway.  Other experiments indicate the polybori error was a red herring and things would have gone wrong anyway.  So at this point I can't go any further.
 * But then starting from scratch _without_ `SAGE_CHECK=yes` but the same packages worked fine, except the GAP problem which led to a built Sage!  Which still won't start, see JP's attempt below as well as [#13954](https://trac.sagemath.org/ticket/13954).
 * And using the package from [#13954](https://trac.sagemath.org/ticket/13954) resulted in a functional Sage!



### Testing Sage 5.6.rc0 on 64 bits Windows 7

With the following Cygwin packages installed:
```
$ cygcheck -c
Cygwin Package Information
Package              Version              Status
_autorebase          000192-1             OK
_update-info-dir     01100-1              OK
alternatives         1.3.30c-10           OK
base-cygwin          3.1-1                OK
base-files           4.1-1                OK
bash                 4.1.10-4             OK
binutils             2.22.51-2            OK
bzip2                1.0.6-2              OK
coreutils            8.15-1               OK
crypt                1.2-1                OK
csih                 0.9.6-1              OK
cygrunsrv            1.40-2               OK
cygutils             1.4.10-2             OK
cygwin               1.7.17-1             OK
cygwin-doc           1.7-1                OK
dash                 0.5.7-1              OK
diffutils            3.2-1                OK
dos2unix             6.0.2-1              OK
editrights           1.01-2               OK
file                 5.11-1               OK
findutils            4.5.9-2              OK
gawk                 4.0.2-1              OK
gcc4-core            4.5.3-3              OK
gettext              0.18.1.1-2           OK
grep                 2.6.3-1              OK
groff                1.21-2               OK
gzip                 1.4-1                OK
ipc-utils            1.0-1                OK
lapack               3.4.2-1              OK
less                 444-1                OK
libasn1_8            1.5.2-4              OK
libattr1             2.4.46-1             OK
libbz2_1             1.0.6-2              OK
libcharset1          1.14-2               OK
libcloog0            0.15.7-1             OK
libcom_err2          1.42.6-1             OK
libdb4.5             4.5.20.2-3           OK
libedit0             20120311-1           OK
libexpat1            2.1.0-1              OK
libffi4              4.5.3-3              OK
libgcc1              4.5.3-3              OK
libgdbm4             1.8.3-20             OK
libgfortran3         4.5.3-3              OK
libgmp3              4.3.2-1              OK
libgmpxx4            4.3.2-1              OK
libgomp1             4.5.3-3              OK
libgssapi3           1.5.2-4              OK
libheimbase1         1.5.2-4              OK
libheimntlm0         1.5.2-4              OK
libhx509_5           1.5.2-4              OK
libiconv             1.14-2               OK
libiconv2            1.14-2               OK
libintl8             0.18.1.1-2           OK
libkafs0             1.5.2-4              OK
libkrb5_26           1.5.2-4              OK
liblapack-devel      3.4.2-1              OK
liblapack0           3.4.2-1              OK
liblzma5             5.0.2_20110517-1     OK
libmpc1              0.8-1                OK
libmpfr1             2.4.1-4              OK
libmpfr4             3.0.1-1              OK
libncurses-devel     5.7-18               OK
libncurses10         5.7-18               OK
libncurses9          5.7-16               OK
libncursesw10        5.7-18               OK
libopenssl100        1.0.1c-2             OK
libpcre0             8.21-2               OK
libpopt0             1.6.4-4              OK
libppl               0.10.2-1             OK
libreadline7         6.1.2-3              OK
libroken18           1.5.2-4              OK
libsigsegv2          2.10-1               OK
libsqlite3_0         3.7.13-1             OK
libssp0              4.5.3-3              OK
libstdc++6           4.5.3-3              OK
libwind0             1.5.2-4              OK
libwrap0             7.6-21               OK
libxml2              2.9.0-1              OK
login                1.10-10              OK
m4                   1.4.16-1             OK
make                 3.82.90-1            OK
man                  1.6g-1               OK
mintty               1.1.2-1              OK
nano                 2.2.5-1              OK
openssh              6.1p1-1              OK
perl                 5.14.2-3             OK
perl_vendor          5.14.2-3             OK
rebase               4.3.0-1              OK
run                  1.1.13-1             OK
sed                  4.2.1-2              OK
tar                  1.26-1               OK
terminfo             5.7_20091114-14      OK
texinfo              4.13-4               OK
tzcode               2012j-1              OK
w32api               9999-1               OK
w32api-headers       3.0b_svn5496-1       OK
w32api-runtime       3.0b_svn5496-1       OK
which                2.20-2               OK
xz                   5.0.2_20110517-1     OK
zlib0                1.2.7-1              OK
```
+ hacks:
* the gcc-4.7.2.p0 optional spkg (from [#13913](https://trac.sagemath.org/ticket/13913), merged) as gcc 4.6.3 is known to fail to build ECL,
* the zlib spkg from [#13914](https://trac.sagemath.org/ticket/13914) to install shared libraries,
* the patch spkg from [#13844](https://trac.sagemath.org/ticket/13844),
* the mpir spkg from [#13137](https://trac.sagemath.org/ticket/13137) (which includes the fix from [#12115](https://trac.sagemath.org/ticket/12115) but the one from [#12115](https://trac.sagemath.org/ticket/12115) should be fine),
* a custom libpng spkg using the SYMBOL_PREFIX trick (and cleaning the terribly dirty spkg-install), to be posted, maybe on [#11696](https://trac.sagemath.org/ticket/11696), meanwhile you can grab it at http://boxen.math.washington.edu/home/jpflori/libpng-1.2.35.p5.spkg
* I faked the iconv spkg install and installed Cygwin libiconv (devel) instead (libiconv2 (runtime) was installed by default), but using [#13912](https://trac.sagemath.org/ticket/13912) should work as well without requiring libiconv,
* I installed Cygwin lapack* packages rather than trying to install ATLAS,
* GAP failed, this is [#13954](https://trac.sagemath.org/ticket/13954), so I faked its install, there is now a package at [#13954](https://trac.sagemath.org/ticket/13954) which should be functional,
and I was able to build Sage! only rebasing when building the sage library itself!(although Gap and so Sage does not start obviously.)

And with [#9167](https://trac.sagemath.org/ticket/9167) the doc completely builds (and I'll be able to import ecl and maxima).



### Testing Sage 5.7.beta1 on 64 bits Windows 7
* I've explicitely uninstalled file.
* there really is a problem with singular, see [#14033](https://trac.sagemath.org/ticket/14033)
* had to rebase once before the sage library
* errors building libgap related files in the sage library, surely because no shared libgap is built because of libtool -no-undefined flag mess (by the way libgap spkg-install is a real mess):
```
gcc -shared -Wl,--enable-auto-image-base -L/home/jp/sage-5.7.beta1/local/lib build/temp.cygwin-1.7.17-i686-2.7/sage/libs/gap/util.o -L/home/jp/sage-5.7.beta1/local/lib -L/home/jp/sage-5.7.beta1/local/lib/python2.7/config -lcsage -lcsage -lgmp -lgap -lm -lstdc++ -lntl -lpython2.7 -o build/lib.cygwin-1.7.17-i686-2.7/sage/libs/gap/util.dll
build/temp.cygwin-1.7.17-i686-2.7/sage/libs/gap/util.o: In function `__pyx_f_4sage_4libs_3gap_4util_memory_usage':
/home/jp/sage-5.7.beta1/devel/sage/sage/libs/gap/util.c:4232: undefined reference to `__imp__libGAP_StopBags'
/home/jp/sage-5.7.beta1/devel/sage/sage/libs/gap/util.c:4241: undefined reference to `__imp__libGAP_EndBags'
```
* after fixing the libgap issue (see [#14038](https://trac.sagemath.org/ticket/14038)), Sage builds and starts, reissued make to build the few missing spkg (sagetex, conway_polynomials), and now its building the doc.
* needs a rebase when building the doc, then finished successfully.
* now running "make ptest" (expecting some failures as I did not take care of [#13960](https://trac.sagemath.org/ticket/13960) or [#9176](https://trac.sagemath.org/ticket/9176) and surely others).


### Testing Sage 5.7.beta2 on 32 bits Windows 7
* This time file got pulled in because I installed procps to have top.
* Also installed the lapack packages, the gcc, g++ and gfortran ones, m4, make, binutils, perl.
* Used libgap from [#14038](https://trac.sagemath.org/ticket/14038), R from [#14078](https://trac.sagemath.org/ticket/14078), Singular from [#14033](https://trac.sagemath.org/ticket/14033), zlib from [#13914](https://trac.sagemath.org/ticket/13914), lcalc from [#13351](https://trac.sagemath.org/ticket/13351), palp from [#13960](https://trac.sagemath.org/ticket/13960), libpng from http://boxen.math.washington.edu/home/jpflori/libpng-1.2.35.p5.spkg, a custom gsl from https://savannah.gnu.org/bugs/index.php?37894.
* Applied patches from [#13351](https://trac.sagemath.org/ticket/13351) and [#9170](https://trac.sagemath.org/ticket/9170) to the Sage library.
* Built fine, had to rebase twice.
* Starts and exits gracefully.
* Most of "make ptest" passes. The remaining problems are:
  * timeouts because tests are too long, or because some functions use a default timeout value which is too low for this computer (but Cygwin in general as well I guess),
  * numerical noise, probably a bug in the libc reported here https://groups.google.com/forum/#!topic/sage-devel/QACdziLhniU/discussion, ticket [#10285](https://trac.sagemath.org/ticket/10285) and https://bugs.launchpad.net/ubuntu/+source/eglibc/+bug/713985
  * gfortran troubles, have to investigate.
  * cython trouble, have to investigate.


### Testing Sage 5.7.beta4 on 64 bits Windows 7
* Applied [#14038](https://trac.sagemath.org/ticket/14038), [#14033](https://trac.sagemath.org/ticket/14033), [#13351](https://trac.sagemath.org/ticket/13351), [#13960](https://trac.sagemath.org/ticket/13960), [#14118](https://trac.sagemath.org/ticket/14118) and used GCC 4.7.2 optional spkg.
* Built successfully and starts.
* Ive cleaned up my rebase database and rebased everything and it seems most of the remaining fork errors I had last time are gone.


### Testing Sage 5.9.beta2 on 32 bits Windows 7
* I launched the build yesterday night and found it back this morning having installed most of the spkg, it just failed during compilation of the Sage library because of a fork error, that was expected. So to summarize, great news!
* Cygwin has recently (early 2013) integrated Python 2.7 which happens to be the same version that Sage ships. That's a problem because on Cygwin libpython2.7.dll is installed in the "bin" directory and we don't include it in LD_LIBRARY_PATH. That would not be a problem because most of Cygwin dll system uses the PATH var where "bin" is present, but dlopen  does not use PATH, so the _ctypes module of python which uses it to load libpython sees an empty LD_LIBRARY_PATH, then looks for default dirs, which point to /usr/lib,bin, and if you have a system wide python 2.7 installed, loads the libpython2.7 from there at a different address than the initial libpython loaded by Sage's python initially. And then when you try to fork(), Cygwin whines because it's using the dlopened libpython, but the libraries loaded during fork use PATH which points to the Sage's libpython (already loaded once, but whatever), so the base address are different and BOOM (not that this base address conflict is not a problem for dlopen at first...). This is now [#14380](https://trac.sagemath.org/ticket/14380)/


### Testing Sage 5.9.beta5 on 32 bits Windows XP running under Virtualbox 4.1.18 on 64 bits Debian sid/experimental
* Still had to set SAGE_PORT because of broken [#14406](https://trac.sagemath.org/ticket/14406), should be fixed in [#14447](https://trac.sagemath.org/ticket/14447).
* All of Sage built fine without rebasing until building the doc!
* Rebased and the doc built fine.
* Testing seems ok (whether I use "./sage -tp" or "make ptest").