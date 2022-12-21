# Issue 9508: ATLAS is not building shared libraries properly on Solaris 10 and OpenSolaris

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-07-15 14:20:22

Assignee: drkirkby

CC:  jhpalmieri jsp

The ATLAS package in Sage (atlas-3.8.3.p12 in sage 4.5.rc1) has a problem in the way shared libraries are built and installed. 
 * libatlas and libcblas never get built as shared libraries on Solaris or OpenSolaris, despite they do get built on Linux, OS X and FreeBSD.
 *  liblapack gets built, but later gets removed by the following few lines of code in the script `make_correct_shared.sh`, which was probably added in #5024. 
 {{{
# on Solaris a dynamic liblapack.so leads to import errors in numpy, so delete them for now.
if [ `uname` = "SunOS" ]; then
    echo "Deleting liblapack.so on Solaris due to bug in numpy/scipy"
    cd "$SAGE_LOCAL"/lib
    rm -rf liblapack.so*
fi
 }}}
 * On 64-bit builds of Sage, Linbox reports ATLAS is not installed - see #9101. Closer inspection of Linbox's config.log shows that linbox determines the ATLAS libraries are 32-bit, not 64-bit. Since it finds no 64-bit libraries, it considers ATLAS is not installed. 

I suspect the reasons the shared libraries are not currently built in Sage is that they were originally built incorrectly, so rather than fix the problem, they were just deleted. I'm aware  Michael Abshoff was using the GNU linker, despite this has never had a good reputation on Solaris, and even the GCC documentation advises using the Sun linker. Hence I think we should

 * Build the shared libraries properly, using the Sun linker `/usr/ccs/bin/ld`
 * Consider deleting the static libraries. I don't think they would perform any useful function if the shared libraries existed. 

This will have several advantages. 

 * Shared libraries are much smaller than static libraries. 
 * Shared libraries take up far less memory when th
 * Linbox will hopefully not report ATLAS is not installed. 

The following command will build a a 32-bit or 64-bit shared library liblapack.so, although it could easily be extended to other libraries too. 

```
  if [ "x$SAGE64" = xyes ] ; then 
      # To create a 64-bit shared library, the linker flag
      # '-64' must be added. Note this is not the same as 
      # the compiler flag '-m64'
      LINKER_BITS=-64 
   else
      LINKER_BITS=-32 
   fi

   # Build liblapack.so
   lapack_command="/usr/ccs/bin/ld $LINKER_BITS -L"$SAGE_LOCAL/lib"  -G -h liblapack.so -o liblapack.so  -zallextract  liblapack.a -zdefaultextract -
lc -lm -lgfortran"
   $lapack_command
```


This will need some testing, but at least this will all be specific to Solaris or OpenSolaris, so will not cause any problems on other platforms. 

Dave


---

Comment by drkirkby created at 2010-07-29 17:45:51

An updated package can be found here

http://boxen.math.washington.edu/home/kirkby/patches/atlas-3.8.3.p13.spkg

I need to double check this before marking for review.


---

Comment by drkirkby created at 2010-07-29 20:26:56

## Testing the updated ATLAS package on OpenSolaris x64 as a 64-bit build
 * [Sun Ultra 27](http://www.sun.com/desktop/workstation/ultra27/)
 * [Intel W3580 Xeon 3.33 GHz](http://ark.intel.com/Product.aspx?id=39723), Quad core. 8 threads.
 * 12 GB RAM
 * [128-bit ZFS](http://en.wikipedia.org/wiki/ZFS) file systems
 * OpenSolaris 2009.06 snv_134 X86
 * Sage sage-4.5.2.alpha.1
 * gcc 4.4.4 configured to use the Sun linker and GNU assembler
 * 64-bit build by exporting SAGE64 to "yes"
 * ATLAS's test suite was run, by exporting SAGE_CHECK to "yes"

The ATLAS log is too long to show, but summary information is provided. This includes: 
 * The start and end of logfile while ATLAS is building. 
 * The end of the logfile whilst ATLAS was being tested. 
 * The end of the log file whilst ATLAS was running some timing tests. 
 * Confirmation using the `file` command that the shared libraries all exist and are 64-bit

*First the build.*

```
drkirkby`@`hawk:~/sage-4.5.2.alpha1$ ./sage -f atlas-3.8.3.p13
chmod 0644 /export/home/drkirkby/sage-4.5.2.alpha1/local/lib/libptcblas.a /export/home/drkirkby/sage-4.5.2.alpha1/local/lib/libptf77blas.a
chmod: WARNING: can't access /export/home/drkirkby/sage-4.5.2.alpha1/local/lib/libptcblas.a
chmod: WARNING: can't access /export/home/drkirkby/sage-4.5.2.alpha1/local/lib/libptf77blas.a
make[1]: [install_lib] Error 2 (ignored)
make[1]: Leaving directory `/export/home/drkirkby/sage-4.5.2.alpha1/spkg/build/atlas-3.8.3.p13/ATLAS-build'
Building shared library libatlas.so from the static library libatlas.a
libatlas.so has been built on Solaris.
Building shared library liblapack.so from the static library liblapack.a
liblapack.so has been built on Solaris.
Building shared library libf77blas.so from the static library libf77blas.a
libf77blas.so has been built on Solaris.
Building shared library libcblas.so from the static library libcblas.a
libcblas.so has been built on Solaris.

real    8m39.991s
user    7m39.319s
sys     0m50.064s
Successfully installed atlas-3.8.3.p13
Running the test suite.
```

*Then the test suite is run. A failure of the test suite would have exited with an error message.*

```
make[1]: [sanity_test] Error 1 (ignored)
DONE
SCOPING FOR FAILURES IN CBLAS TESTS:
fgrep -e fault -e FAULT -e error -e ERROR -e fail -e FAIL \
                interfaces/blas/C/testing/sanity.out | \
                fgrep -v PASSED
make[1]: [sanity_test] Error 1 (ignored)
DONE
SCOPING FOR FAILURES IN F77BLAS TESTS:
fgrep -e fault -e FAULT -e error -e ERROR -e fail -e FAIL \
                interfaces/blas/F77/testing/sanity.out | \
                fgrep -v PASSED
make[1]: [sanity_test] Error 1 (ignored)
DONE
make[1]: Leaving directory `/export/home/drkirkby/sage-4.5.2.alpha1/spkg/build/atlas-3.8.3.p13/ATLAS-build'
The ATLAS self-tests successfully passed
```


*Finally, the timing tests are run. Had these failed, spkg-check would cause an error message to be generated*


```
The times labeled Reference are for ATLAS as installed by the authors.
NAMING ABBREVIATIONS:
   kSelMM : selected matmul kernel (may be hand-tuned)
   kGenMM : generated matmul kernel
   kMM_NT : worst no-copy kernel
   kMM_TN : best no-copy kernel
   BIG_MM : large GEMM timing (usually N=1600); estimate of asymptotic peak
   kMV_N  : NoTranspose matvec kernel
   kMV_T  : Transpose matvec kernel
   kGER   : GER (rank-1 update) kernel
Kernel routines are not called by the user directly, and their
performance is often somewhat different than the total
algorithm (eg, dGER perf may differ from dkGER)


Reference clock rate=2672Mhz, new rate=3325Mhz
   Refrenc : % of clock rate achieved by reference install
   Present : % of clock rate achieved by present ATLAS install

                    single precision                  double precision
            ********************************   *******************************
                  real           complex           real           complex
            ---------------  ---------------  ---------------  ---------------
Benchmark   Refrenc Present  Refrenc Present  Refrenc Present  Refrenc Present
=========   ======= =======  ======= =======  ======= =======  ======= =======
  kSelMM      636.3   693.9    584.2   643.0    340.4   367.6    338.8   366.6
  kGenMM      186.2   199.9    186.4   198.1    177.0   191.8    176.9   191.9
  kMM_NT      166.9   180.6    164.4   180.7    162.0   175.8    157.8   175.6
  kMM_TN      162.4   173.8    174.7   192.3    160.8   171.3    167.4   185.5
  BIG_MM      838.0   672.4    832.0   675.6    446.6   359.1    442.8   352.5
   kMV_N      177.7   196.5    282.9   273.2     86.4    89.9    121.9   121.2
   kMV_T      109.2   120.2    120.3   126.6     89.6   103.5    105.8   104.7
    kGER      201.9   234.1    266.6   281.3     77.3    89.7    102.2   111.3
make[1]: Leaving directory `/export/home/drkirkby/sage-4.5.2.alpha1/spkg/build/atlas-3.8.3.p13/ATLAS-build'
The ATLAS timing data was successfully collected
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.5.2.alpha1/spkg/build/atlas-3.8.3.p13
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing atlas-3.8.3.p13.spkg
```


It can also be seen that the shared libraries are 64-bit, as they should be:


```
drkirkby`@`hawk:~/sage-4.5.2.alpha1/local/lib$ file libcblas.so  libf77blas.so liblapack.so libatlas.so libf77blas.a liblapack.a libcblas.a libatlas.a
libcblas.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
libf77blas.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
liblapack.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
libatlas.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
libf77blas.a:	current ar archive, not a dynamic executable or shared object
liblapack.a:	current ar archive, not a dynamic executable or shared object
libcblas.a:	current ar archive, not a dynamic executable or shared object
libatlas.a:	current ar archive, not a dynamic executable or shared object
```


*Given that other programs like linbox link properly to the ATLAS library, we can assume with a reasonable degree of confidence the libraries are being built correctly on 64-bit OpenSolaris on the x64 platform.*


---

Comment by drkirkby created at 2010-07-29 21:50:19

## Testing the updated ATLAS package on Solaris 10 x64 as a 32-bit build

 * Dell Inc. OptiPlex 755 (Quad-Core Intel(R) Core(TM)2 Quad Q6600 `@` 2.40GHz)
 * 8 GB RAM
 * Solaris 10 x86 update 5 (5/08)
 * 32-bit build - SAGE64 was unset
 * gcc 4.5.0 configured to use the Sun linker and GNU assembler. 

Only the start and end of the build are shown. Had ATLAS failed to build, the tests would not have been run. Had the tests not all past, the timing information would not have been gathered. So this shows that ATLAS has built and passed all the tests, and timing information has been collected. 


```
32 drkirkby`@`fulvia:[~/fulvia/32/sage-4.5.1] $ ./sage -f atlas-3.8.3.p13
Force installing atlas-3.8.3.p13
Calling sage-spkg on atlas-3.8.3.p13
Warning: Attempted to overwrite SAGE_ROOT environment variable

<snip>

Reference clock rate=2394Mhz, new rate=2400Mhz
   Refrenc : % of clock rate achieved by reference install
   Present : % of clock rate achieved by present ATLAS install

                    single precision                  double precision
            ********************************   *******************************
                  real           complex           real           complex
            ---------------  ---------------  ---------------  ---------------
Benchmark   Refrenc Present  Refrenc Present  Refrenc Present  Refrenc Present
=========   ======= =======  ======= =======  ======= =======  ======= =======
  kSelMM      567.0   564.1    527.5   521.9    334.0   332.5    321.0   318.3
  kGenMM      162.8   121.3    164.5   163.1    155.5   143.9    154.4   145.6
  kMM_NT      135.8   155.0    132.7   158.0    104.6   135.8    115.7   147.5
  kMM_TN      159.6   115.1    123.4   112.1    123.3   110.7    127.1   114.1
  BIG_MM      553.1   539.6    554.4   553.0    322.1   321.8    324.2   321.4
   kMV_N       69.0    66.0    212.3   153.4     54.4    55.9     69.8    65.8
   kMV_T       87.5    83.1     91.5   113.7     49.9    36.8     74.1    71.4
    kGER       90.1    87.4    117.4   105.0     28.1    26.9     42.2    45.1
make[1]: Leaving directory `/home/drkirkby/fulvia/32/sage-4.5.1/spkg/build/atlas-3.8.3.p13/ATLAS-build'
The ATLAS timing data was successfully collected
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/home/drkirkby/fulvia/32/sage-4.5.1/spkg/build/atlas-3.8.3.p13
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing atlas-3.8.3.p13.spkg
32 drkirkby`@`fulvia:[~/fulvia/32/sage-4.5.1] $ 
```



---

Comment by drkirkby created at 2010-07-29 21:56:56

## Testing the updated ATLAS package on Solaris 10 x64 as a 64-bit build
 * Dell Inc. OptiPlex 755 (Quad-Core Intel(R) Core(TM)2 Quad Q6600 `@` 2.40GHz)
 * 8 GB RAM
 * Solaris 10 x86 update 5 (5/08)
 * 64-bit build - SAGE64 was exported to "yes"
 * gcc 4.5.0 configured to use the Sun linker and GNU assembler. 

Again, the full log is not shown, but the end is . 

```
64 drkirkby`@`fulvia:[~/fulvia/64/sage-4.5.1] $ ./sage -f atlas-3.8.3.p13

<snip> 

Reference clock rate=2394Mhz, new rate=2400Mhz
   Refrenc : % of clock rate achieved by reference install
   Present : % of clock rate achieved by present ATLAS install

                    single precision                  double precision
            ********************************   *******************************
                  real           complex           real           complex
            ---------------  ---------------  ---------------  ---------------
Benchmark   Refrenc Present  Refrenc Present  Refrenc Present  Refrenc Present
=========   ======= =======  ======= =======  ======= =======  ======= =======
  kSelMM      565.9   571.5    532.9   528.8    365.5   363.9    334.8   351.6
  kGenMM      177.6   156.5    177.6   171.2    166.1   142.4    162.6   141.5
  kMM_NT      134.0   129.5    138.9   169.0    119.1   119.7    137.6   157.5
  kMM_TN      159.3   154.5    165.6   157.5    148.2   138.5    159.0   152.4
  BIG_MM      558.5   545.5    557.8   549.3    353.8   353.3    346.7   348.1
   kMV_N      111.0   105.3    211.1   206.1     55.2    57.4     92.8    86.7
   kMV_T       85.0    88.7     93.1    68.3     45.5    47.3     76.7    64.9
    kGER      159.0   189.1    119.0   123.8     27.8    29.3     46.5    49.8
make[1]: Leaving directory `/home/drkirkby/fulvia/64/sage-4.5.1/spkg/build/atlas-3.8.3.p13/ATLAS-build'
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/home/drkirkby/fulvia/64/sage-4.5.1/spkg/build/atlas-3.8.3.p13
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing atlas-3.8.3.p13.spkg
64 drkirkby`@`fulvia:[~/fulvia/64/sage-4.5.1] 
```


We can see the libraries are indeed 32-bit:


```
as.arkirkby`@`fulvia:[~/fulvia/32/sage-4.5.1/local/lib] $ file libcblas.so libf77blas.so liblapack.so libatlas.so libf77blas.a liblapack.a libcblas.a libatl 
libcblas.so:	ELF 32-bit LSB dynamic lib 80386 Version 1, dynamically linked, not stripped, no debugging information available
libf77blas.so:	ELF 32-bit LSB dynamic lib 80386 Version 1, dynamically linked, not stripped, no debugging information available
liblapack.so:	ELF 32-bit LSB dynamic lib 80386 Version 1, dynamically linked, not stripped, no debugging information available
libatlas.so:	ELF 32-bit LSB dynamic lib 80386 Version 1, dynamically linked, not stripped, no debugging information available
libf77blas.a:	current ar archive, not a dynamic executable or shared object
liblapack.a:	current ar archive, not a dynamic executable or shared object
libcblas.a:	current ar archive, not a dynamic executable or shared object
libatlas.a:	current ar archive, not a dynamic executable or shared object
```



---

Comment by jhpalmieri created at 2010-08-02 05:04:52

Is this ready for review?

Regarding the check `"x`uname -m`" = xi86pc`, does this guarantee Solaris or OpenSolaris somehow?  I can't find a definitive description of the output of "uname -m", although I've seen a few places (including the uname man page on Solaris) suggest that you should use "uname -p" instead of "uname -m"...

Would it be better (or at least easier to read) to use `uname` instead of `uname -m`?

Anyway, this is a minor point. The changes look good and I'm building this on several machines to test it out.  I think if this gets a positive review, then we can close #9356: with this new spkg, ATLAS builds all of the appropriate libraries on Solaris, so we don't need to modify how SAGE_ATLAS_LIB works.


---

Comment by drkirkby created at 2010-08-02 08:59:04

Replying to [comment:7 jhpalmieri]:
> Is this ready for review?

No. I think I found an issue on SPARC. I want to make double sure this is OK. My 32-bit SPARC build did not work properly. 

> Regarding the check `"x`uname -m`" = xi86pc`, does this guarantee Solaris or OpenSolaris somehow?  

No, it guarantees the hardware is x86 based. That includes the 64-bit hardware. You will get the same on both OpenSolaris and Solaris. Note OpenSolaris does run on SPARC hardware too, though that is not very common. I don't have any OpenSolaris SPARC systems running myself and I'm not aware of anywhere where there is one. 

> I can't find a definitive description of the output of "uname -m", although I've seen a few places (including the uname man page on Solaris) suggest that you should use "uname -p" instead of "uname -m"...

I have never noticed that in the uname man page. My preference for -m, and not -p, is that -m is defined by POSIX standards:

http://www.opengroup.org/onlinepubs/009695399/utilities/uname.html

but there is no requirement for uname to support the -p option. That causes a problem on systems like HP-UX, where  there is no -p option. So before using uname -p, one should test that the system supports the option. I guess since this is in a Solaris specific part of the file, we could use uname -p, but I'm not over keen on using non-portable options if portable ones exist. 

I can't believe Sun could ever possibly remove the -m option, as Solaris would then not be a POSIX compliant operating system - it would drop to be a "Unix-like" operating system, as is Linux. I must admit I am puzzled why they recommend you use a non-portable option in preference to a portable one. 

> Would it be better (or at least easier to read) to use `uname` instead of `uname -m`?

No, since `spkg-install-script` does need to know the processor type. Trying to make those substitutions on a SPARC processor would make no sense. However, I can certainly clarify things a bit more with comments, similar to what I have put above. 
 
> Anyway, this is a minor point. The changes look good and I'm building this on several machines to test it out.  I think if this gets a positive review, then we can close #9356: with this new spkg, ATLAS builds all of the appropriate libraries on Solaris, so we don't need to modify how SAGE_ATLAS_LIB works.

Let me know how your build goes. My 32-bit SPARC build did not work, so I'd be interested in how you get on with 32-bit builds on SPARC. 

Dave


---

Comment by drkirkby created at 2010-08-02 08:59:13

Changing status from new to needs_info.


---

Comment by jhpalmieri created at 2010-08-02 14:34:00

> Let me know how your build goes. My 32-bit SPARC build did not work, so I'd be interested in how you get on with 32-bit builds on SPARC.

On mark2, it claims to have built successfully with SAGE_CHECK='yes'.  On the other hand, when building from scratch on mark2, while ATLAS seems to build okay, the R build fails:

```
Warning in solve.default(rgb) :
  unable to load shared library '/home/palmieri/mark2/sage-4.5.2.rc0/spkg/build/r-2.10.1.p2/src/modules//lapack.so':
  ld.so.1: R: fatal: relocation error: file /home/palmieri/mark2/sage-4.5.2.rc0/local/lib//liblapack.so: symbol __powisf2: referenced symbol not found
Error in solve.default(rgb) : lapack routines cannot be loaded
Error: unable to load R code in package 'grDevices'
Execution halted
```



---

Comment by drkirkby created at 2010-08-02 15:37:34

Replying to [comment:10 jhpalmieri]:
> > Let me know how your build goes. My 32-bit SPARC build did not work, so I'd be interested in how you get on with 32-bit builds on SPARC.
> 
> On mark2, it claims to have built successfully with SAGE_CHECK='yes'.  On the other hand, when building from scratch on mark2, while ATLAS seems to build okay, the R build fails:
> {{{
> Warning in solve.default(rgb) :
>   unable to load shared library '/home/palmieri/mark2/sage-4.5.2.rc0/spkg/build/r-2.10.1.p2/src/modules//lapack.so':
>   ld.so.1: R: fatal: relocation error: file /home/palmieri/mark2/sage-4.5.2.rc0/local/lib//liblapack.so: symbol __powisf2: referenced symbol not found
> Error in solve.default(rgb) : lapack routines cannot be loaded
> Error: unable to load R code in package 'grDevices'
> Execution halted
> }}}

Yes, I think that was the problem I got. Strange, on a 64-bit SPARC build I was able to get Sage to build completely. I'm not sure if I used that ATLAS package, or just made the libraries manually. 

Without creating the shared libraries, Linbox will not link - complains ATLAS is missing. Inspect of the linbox log file shows it thinks the ATLAS libraries are 32-bit. I need to check that, as potentially linbox is mistaken. 

It's hard to know if this is a Linbox, ATLAS or R problem. The R manual (http://cran.r-project.org/doc/manuals/R-admin.pdf) might have something on this. 

Adding an spkg-check file to Linbox might be useful, as we could test the ATLAS library with Linbox. It does have a test suite, but since there is no spkg-check file, it never gets executed. 

I created ticket some time back to fix the lack of a test suite in linbox - #9613. I'll create one for that today. It should be easy to review and might help debug this. If linbox passes tests on 64-bit with the ATLAS library, I would tend to suspect R is at fault. Conversely if tests fail, I would tend to suspect ATLAS. 

Dave


---

Comment by jhpalmieri created at 2010-08-02 17:58:09

> > Regarding the check "x`uname -m`" = xi86pc, does this guarantee Solaris or OpenSolaris somehow?

> No, it guarantees the hardware is x86 based. That includes the 64-bit hardware. 

Ignore my question about guaranteeing Solaris or OpenSolaris; I was confused.  

However, on a system like sage.math, uname -m outputs "x86_64".  The same happens with many of the other linux skynet machines. I've only seen the output "i86pc" on fulvia, an x86 machine running Solaris.  So if you have an x86 machine running Solaris, will it always print "i86pc" instead of "x86_64", for example?

Regarding the problem on mark2 and elsewhere, maybe we should continue to not build the shared libraries?  If I have the time, I'll try rebuilding on mark2 and then delete the shared library after ATLAS has been installed, to see if R builds successfully after that.  If this works, I'm not sure what it means: is it an ATLAS problem or an R problem or something else?


---

Comment by jhpalmieri created at 2010-08-03 03:19:40

As I commented on #9600, if on mark I just delete the shared library liblapack.so, then R builds successfully, as do the rest of the spkgs.  Doctesting is ongoing, but no failures yet.


---

Comment by jhpalmieri created at 2010-08-04 22:27:09

On fulvia, 32-bit build, the old version of ATLAS fails to build, but this one succeeds.  With the new one, I have the same situation as with mark: R fails to build *unless I delete liblapack.so*. Then it succeeds.  Right now the Sage library is building; I'm curious about how many doctest failures I'll see.

For the record, I built on fulvia using Sage 4.5.2.rc1 + this ATLAS spkg + the singular 3-1-1-4 spkg from #8059.  Once the Sage library builds (assuming it builds successfully), I'll apply the Sage library patch from #8059 also.


---

Comment by drkirkby created at 2010-08-04 23:10:18

Replying to [comment:14 jhpalmieri]:
> On fulvia, 32-bit build, the old version of ATLAS fails to build, but this one succeeds.  With the new one, I have the same situation as with mark: R fails to build *unless I delete liblapack.so*. Then it succeeds.  

We will at some point need to run the R test suite, as there are reports in the R manual that R fails some tests if built with gcc. It's also reported R can't be built on Solaris 64-bit without the Sun compilers. 

The Sage doctests don't really test R. But once we can get a Sage release that builds on fulvia without various hacks, it will be much easier to test. SAGE_CHECK can then be used to test R properly. 

> Right now the Sage library is building; I'm curious about how many doctest failures I'll see.

Thank you John.

It would be nice to understand the problem, but if all else fails, a bit of code that deletes `liblapack.so` on Solaris is trivial. 

I'd like to know if Linbox or ATLAS is at fault with Linbox believing the ATLAS library is 32-bit when building 64-bit. ATLAS is clearly not 32-bit, since if you extract the objects with `ar -x foobar.a` all the object files are 64-bit. But perhaps there is something one needs to code into a static library to make it easier for software to realise the objects are 64-bit. I'll ask on comp.unix.solaris about this. 

It is remotely possible that copying the 64-bit library to `$SAGE_LOCAL/lib/amd64` or `$SAGE_LOCAL/lib/sparcv9` will make Linbox look for the library. On Solaris, all 64-bit libraries should be in a `lib/amd64` or `lib/sparcv9` directory. That allows both 32-bit and 64-bit libraries to be on the same system. If you use the `file` command on the libraries in `/usr/lib`, you will see they are all 32-bit. In `/usr/lib/amd64` on x86 systems, or `/usr/lib/sparcv9` on SPARC system, you will see they are 64-bit. That might be a way of getting Linbox to behave. It might also be a way of getting R to behave, though I don't think the R problem is a 32-bit vs 64-bit issues, whereas the Linobx problem is. 


> For the record, I built on fulvia using Sage 4.5.2.rc1 + this ATLAS spkg + the singular 3-1-1-4 spkg from #8059.  Once the Sage library builds (assuming it builds successfully), I'll apply the Sage library patch from #8059 also.

Great. These systems seem to be coming together now. Most of the fixes for one variant of Solaris apply to the others too. I thought the Cygwin port would be completed before the other Solaris ports, but now I'm not so sure. I think its quite possible we could have Sage running 32-bit and 64-bit on both SPARC and x86 in the not too distant future. 
 
Dave


---

Comment by jhpalmieri created at 2010-08-04 23:16:56

> Great. These systems seem to be coming together now.

The 64-bit builds are causing trouble, but 32-bit Solaris on sparc works, while 32-bit Solaris on x86 seems very close.  As I've said on another ticket, I have no idea about OpenSolaris.


---

Comment by drkirkby created at 2010-08-04 23:39:28

Replying to [comment:16 jhpalmieri]:
> > Great. These systems seem to be coming together now.
> 
> The 64-bit builds are causing trouble, but 32-bit Solaris on sparc works, while 32-bit Solaris on x86 seems very close.  As I've said on another ticket, I have no idea about OpenSolaris.

I can give you an account on my OpenSolaris box if you want. That's not a problem. It will be a lot faster than fulvia. 

I've created a version of ATLAS that does not build liblapack.so. I've *not* overwritten the one in my _patches_ subdirectory, but put this in my home directory on boxen. Hence this can be found at 

http://boxen.math.washington.edu/home/kirkby/atlas-3.8.3.p13.spkg # does NOT build liblapack.so 

whereas the other one, which build liblapack.so is at 

http://boxen.math.washington.edu/home/kirkby/patches/atlas-3.8.3.p13.spkg # DOES build liblapack.so


---

Comment by drkirkby created at 2010-08-10 11:40:47

Since #9536 system_alias.py fixed problems with SAGE_ATLAS_LIB and was marged as atlas-3.8.3.p13.spkg, I needed to create a atlas-3.8.3.p14.spkg to avoid a name clash. 

The changes made by  #9356 have not been reversed, as it is still necessary to check for liblapack.a, and not liblapack.so, as that's the one library that if built causes problems for R. 

The new package can be found at 

http://boxen.math.washington.edu/home/kirkby/patches/atlas-3.8.3.p14.spkg

I've leaving this as "needs_info" until such time as I have more fully tested this.


---

Comment by drkirkby created at 2010-08-10 11:42:26

New patched, buased on atlas-3.8.3.p13 created on #9356. I've removed all previous patches, as they are not relevant and just add confusion.


---

Comment by drkirkby created at 2010-08-12 15:47:23

Changing status from needs_info to needs_review.


---

Attachment

I'm happy this ok now. 

Needs review.


---

Comment by jhpalmieri created at 2010-08-12 17:23:32

I'm expecting this to be okay, but I'm testing it one last time.  I'm testing on t2 (32- and 64-bit), among other machines, so this will take a while...


---

Comment by jhpalmieri created at 2010-08-14 02:38:22

Looks good to me.  Tested on t2 (32 and 64 bit), sage.math, fulvia (32-bit), mark.


---

Comment by jhpalmieri created at 2010-08-14 02:38:22

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-15 08:04:01

Resolution: fixed
