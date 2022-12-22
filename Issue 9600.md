# Issue 9600: Fix atlas/liblapack.so linkage on FreeBSD

Issue created by migration from Trac.

Original creator: pjeremy

Original creation time: 2010-07-26 10:56:43

Assignee: pjeremy

CC:  jhpalmieri stephen dimpase

liblapack.so includes undefined references to __powidf2 and __powisf2, which are defined in libgcc (no other Sage shared libraries appear to rely on libgcc helper functions). Unfortunately, for reasons I don't fully understand, linking liblapack.so against libgcc.a fails, even when building a normal executable. The symptom is a message like:

usr/local/bin/ld: _configtest: hidden symbol `__powidf2' in /usr/local/lib/gcc45/gcc/x86_64-portbld-freebsd8.1/4.5.1/libgcc.a(_powidf2.o) is referenced by DSO
/usr/local/bin/ld: final link failed: Nonrepresentable section on output

The fix is to add a dependency on libgcc_s.so when (re-)building 
liblapack.so in make_correct_shared.sh.

It's not clear whether this is a defect in atlas or not - the liblapack.so used in Sage is custom-built for Sage and so this particular fix cannot be reported.


---

Attachment

This does not seem to be FreeBSD-specific!
See http://groups.google.com/group/sage-devel/browse_thread/thread/4cfaff6722c62c9b


---

Comment by drkirkby created at 2010-08-02 16:56:07

Changing assignee from pjeremy to GeorgSWeber.


---

Comment by drkirkby created at 2010-08-02 16:56:07

This could conceivably be related to an issue observed when building R as a 32-bit SPARC binary on 32-bit SPARC. Currently the ATLAS package deletes one shared libraires and does not make several other shared libraries, so there are a lot less libraries then on Linux. That caused an issue with Linbox, with it believing the static library was 32-bit, which it was not. 

When I tried to build all the libraries on Solaris, it causes a failure to build R on 32-bit SPARC. The error message 


```
  ld.so.1: R: fatal: relocation error: file /home/palmieri/mark2/sage-4.5.2.rc0/local/lib//liblapack.so: symbol __powisf2: referenced symbol not found
```

See about comment number 10 on #9508

This is not an identical message, but given FreeBSD will use a GNU linker and this uses a Sun linker, I would not rule out there being a connection. 

I set this from FreBSD -> Build, as it appears to be at least an issue on Linux too, and just possibly related to a Solaris one. 

PS,  Does anyone know how I can provide a link to a specific commitment on another track ticket?


---

Comment by drkirkby created at 2010-08-02 16:56:07

Changing component from freebsd to build.


---

Comment by wjp created at 2010-08-02 22:12:38

Changing status from new to needs_work.


---

Comment by wjp created at 2010-08-02 22:12:38

This is very likely not the right way to fix this. I don't have the time to try this properly now, but I think using gcc as the linker to produce `liblapack.so` instead of ld directly should fix this:


```
[wjp`@`eno sage-4.5.2.rc0]$ ./sage -python
Python 2.6.4 (r264:75706, Aug  1 2010, 12:24:29) 
[GCC 4.5.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import cvxopt.base
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: /home/wjp/eno/sage-4.5.2.rc0/local/lib/liblapack.so: undefined symbol: __powidf2
>>> 
[wjp`@`eno sage-4.5.2.rc0]$ cd local/lib
[wjp`@`eno lib]$ gcc -shared -o liblapack.so -Wl,-soname,liblapack.so -Wl,--whole-archive liblapack.a -Wl,--no-whole-archive
[wjp`@`eno lib]$ cd ../..
[wjp`@`eno sage-4.5.2.rc0]$ ./sage -python                                        Python 2.6.4 (r264:75706, Aug  1 2010, 12:24:29) 
[GCC 4.5.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import cvxopt.base
>>> 
```


(The gcc line above is adapted from the line in atlas' Make.lib where ld is used to produce `liblapack.so`.)


---

Comment by wjp created at 2010-08-02 22:25:13

Sorry for the repeated comment, but it looks like the final ld line generating liblapack.so might also be in (the ironically named) `make_correct_shared.sh` in atlas.


---

Comment by drkirkby created at 2010-08-02 22:36:15

Replying to [comment:3 wjp]:
> This is very likely not the right way to fix this. I don't have the time to try this properly now, but I think using gcc as the linker to produce `liblapack.so` instead of ld directly should fix this:

sing gcc might well be a better solution. It would certainly avoid the issues seen with Solaris, where the linker options have to be changed depending on whether the Sun linker or the GNU linker are used. If one called the compiler directly, rather than the linker, this should be a non-issue, as gcc would know what options to send to the linker. 

In ATLAS, mostly static libraries are built, and then these are converted to dynamic by the linker. I don't know if gcc can then convert a static library to a dynamic library. One might need to do that with the linker. 

dave


---

Comment by wjp created at 2010-08-02 22:48:45

Replying to [comment:5 drkirkby]:
> In ATLAS, mostly static libraries are built, and then these are converted to dynamic by the linker. I don't know if gcc can then convert a static library to a dynamic library. One might need to do that with the linker. 

The command I used in that quick test above does exactly that by using gcc as a frontend to the GNU linker.


```
gcc -shared -o liblapack.so -Wl,-soname,liblapack.so -Wl,--whole-archive liblapack.a -Wl,--no-whole-archive
```


(But I'm not claiming it's the perfect way to do it; it's just a proof of concept, not a well-researched solution.)


---

Comment by drkirkby created at 2010-08-02 23:12:20

Replying to [comment:6 wjp]:
> Replying to [comment:5 drkirkby]:
> > In ATLAS, mostly static libraries are built, and then these are converted to dynamic by the linker. I don't know if gcc can then convert a static library to a dynamic library. One might need to do that with the linker. 
> 
> The command I used in that quick test above does exactly that by using gcc as a frontend to the GNU linker.
> 
> {{{
> gcc -shared -o liblapack.so -Wl,-soname,liblapack.so -Wl,--whole-archive liblapack.a -Wl,--no-whole-archive
> }}}
> 
> (But I'm not claiming it's the perfect way to do it; it's just a proof of concept, not a well-researched solution.)

But you are almost directly using the linker here, since you are passing options directly to the linker. Those options are not portable, as they are GNU-specific. Better still if gcc could handle this. 

I would actually be surprised if ATLAS does not have the ability to create the shared libraries, without one needing to mess around like this in a separate stage. That would be worth investigating - whether ATLAS can take care of all this.


---

Comment by drkirkby created at 2010-08-02 23:31:34

This idea looks better, if it works. Since static libs are just collections of object files, unpack the static library and then use gcc to create the shared library. 


```
ar -x mylib.a
gcc -shared *.o -o mylib.so
```


I got that from this link


http://www.tipcache.com/tip/Convert_a_static_library_%28.a%29_to_a_shared_object_%28.so%29_12.html


---

Comment by drkirkby created at 2010-08-03 01:32:39

I'm attaching a small script, static2shared.sh, which I wrote, which will make shared libraries from the static ones. To build 64-bit shared libraries, the object files in the static library must be 64-bit ones and SAGE64 must be set to "yes". 

It works on the libraries libatlas liblapack libf77blas & libcblas. You could trivially modify it to work with others. 

This is what I get.


```
drkirkby`@`hawk:~/sage-4.5.1/local/lib$ ./static2shared.sh

Change to the directory $SAGE_LOCAL/lib before running this script
it's only a test for now.


Building a 64-bit shared library libatlas.so from the static library libatlas.a
libatlas.so has been built on SunOS
libatlas.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
Building a 64-bit shared library liblapack.so from the static library liblapack.a
liblapack.so has been built on SunOS
liblapack.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
Building a 64-bit shared library libf77blas.so from the static library libf77blas.a
libf77blas.so has been built on SunOS
libf77blas.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
Building a 64-bit shared library libcblas.so from the static library libcblas.a
libcblas.so has been built on SunOS
libcblas.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available
```



---

Comment by drkirkby created at 2010-08-03 01:35:01

Test script to convert static to shared libs. Run from $SAGE_LOCAL/lib.


---

Attachment

mpatel also [had a suggestion](http://trac.sagemath.org/sage_trac/ticket/9356#comment:7) about creating shared libraries.  I know nothing about this; how do these approaches compare?


---

Comment by drkirkby created at 2010-08-03 02:30:20

Replying to [comment:10 jhpalmieri]:
> mpatel also [had a suggestion](http://trac.sagemath.org/sage_trac/ticket/9356#comment:7) about creating shared libraries.  I know nothing about this; how do these approaches compare?
His solution again uses a lot of options that are specific to the GNU linker. I don't however know if those flags are optimal. My guess is that Michael wrote that bit of code in Sage now, and if I'm honest I would not be sure he did it right. For pure simplicity, what I put is hard to beat. Whether it works is another matter! 

Dave


---

Comment by jhpalmieri created at 2010-08-03 03:17:12

This may be a Solaris-specific comment: on mark (skynet machine, Solaris on sparc), I first built the version of ATLAS from #9508, but R refused to build -- see [my comment there](http://trac.sagemath.org/sage_trac/ticket/9508#comment:10).  I applied the script "static2shared.sh: and got similar output to the above (`liblapack.so has been built on SunOS`, etc.), but R still doesn't build: same error as before:

```
Warning in solve.default(rgb) :
  unable to load shared library '/home/palmieri/mark/sage-4.5.2.rc0-shared-script/spkg/build/r-2.1\
0.1.p2/src/modules//lapack.so':
  ld.so.1: R: fatal: libgcc_s.so.1: open failed: No such file or directory
Error in solve.default(rgb) : lapack routines cannot be loaded
Error: unable to load R code in package 'grDevices'
Execution halted
make[4]: *** [mklazy] Error 1
```


On the other hand, if I built the version of ATLAS from #9508 and then just delete liblapack.so, everything seems to work.


---

Comment by drkirkby created at 2010-08-03 03:47:24

Replying to [comment:12 jhpalmieri]:
> This may be a Solaris-specific comment: on mark (skynet machine, Solaris on sparc), I first built the version of ATLAS from #9508, but R refused to build -- see [my comment there](http://trac.sagemath.org/sage_trac/ticket/9508#comment:10).  I applied the script "static2shared.sh: and got similar output to the above (`liblapack.so has been built on SunOS`, etc.), but R still doesn't build: same error as before:
> {{{
> Warning in solve.default(rgb) :
>   unable to load shared library '/home/palmieri/mark/sage-4.5.2.rc0-shared-script/spkg/build/r-2.1\
> 0.1.p2/src/modules//lapack.so':
>   ld.so.1: R: fatal: libgcc_s.so.1: open failed: No such file or directory
> Error in solve.default(rgb) : lapack routines cannot be loaded
> Error: unable to load R code in package 'grDevices'
> Execution halted
> make[4]: *** [mklazy] Error 1
> }}}
> 
> On the other hand, if I built the version of ATLAS from #9508 and then just delete liblapack.so, everything seems to work.

When I used the ATLAS package at #9508 on a 32-bit SPARC build, it failed with this error message, which is remarkably similar to what Peter got on FreeBSD. In particualr, `powisf2` is specifically mentioned in both Peters and my error messages. 


```
make[6]: Entering directory `/export/home/drkirkby/redstart/32/sage-4.5.1/spkg/build/r-2.10.1.p3/src/src/library/grDevices'
Warning in solve.default(rgb) :
  unable to load shared library '/export/home/drkirkby/redstart/32/sage-4.5.1/spkg/build/r-2.10.1.p3/src/modules//lapack.so':
  ld.so.1: /export/home/drkirkby/redstart/32/sage-4.5.1/spkg/build/r-2.10.1.p3/src/bin/exec/R: fatal: relocation error: file /export/h
ome/drkirkby/redstart/32/sage-4.5.1/local/lib//liblapack.so: symbol __powisf2: referenced symbol not found
Error in solve.default(rgb) : lapack routines cannot be loaded
Error: unable to load R code in package 'grDevices'
Execution halted
make[6]: *** [mklazy] Error 1
```


When I used that script, I get:


```
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing rpy2-2.0.8.spkg

real    26m14.008s
user    22m45.228s
sys     3m2.236s
Successfully installed r-2.10.1.p3
```


In other words, for me that script corrects the problem. I'd be very interested what it does for Peter, as he had the same error message as me. 

I've now got 80 packages installed, so are going to leave it running overnight, so the build will have finished when I wake up.


---

Comment by pjeremy created at 2010-08-03 09:45:51

Replying to [comment:9 drkirkby]:
> I'm attaching a small script, static2shared.sh, which I wrote, which will make shared libraries from the static ones. To build 64-bit shared libraries, the object files in the static library must be 64-bit ones and SAGE64 must be set to "yes". 
> 
> It works on the libraries libatlas liblapack libf77blas & libcblas. You could trivially modify it to work with others. 

Unfortunately, I don't believe this works.

The libraries I already had installed report:

```
server% LD_LIBRARY_PATH=/usr/local/lib/gcc45:$PWD ldd lib{atlas,lapack,f77blas,cblas}.so
libatlas.so:
        libc.so.7 => /lib/libc.so.7 (0x800647000)
        libm.so.5 => /lib/libm.so.5 (0x800877000)
liblapack.so:
        libc.so.7 => /lib/libc.so.7 (0x800647000)
        libm.so.5 => /lib/libm.so.5 (0x800877000)
        libgfortran.so.3 => /usr/local/lib/gcc45/libgfortran.so.3 (0x8014bd000)
        libgcc_s.so.1 => /usr/local/lib/gcc45/libgcc_s.so.1 (0x8017a1000)
libf77blas.so:
        libc.so.7 => /lib/libc.so.7 (0x800647000)
        libm.so.5 => /lib/libm.so.5 (0x800877000)
        libgfortran.so.3 => /usr/local/lib/gcc45/libgfortran.so.3 (0x800e1e000)
libcblas.so:
server%
```


And numpy config reports (in part):

```
C compiler: gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/tank/obj/sage/sage-4.5/local/include -fPIC

compile options: '-c'
gcc: _configtest.c
gcc _configtest.o -L/tank/obj/sage/sage-4.5/local/lib -llapack -lf77blas -lcblas -latlas -o _configtest
ATLAS version 3.8.3 built by peter on Mon 26 Jul 2010 17:37:42 EST:
   UNAME    : FreeBSD server.vk2pj.dyndns.org 8.1-PRERELEASE FreeBSD 8.1-PRERELEASE #5: Thu Jul 15 05:43:01 EST 2010     root`@`server.vk2pj.dyndns.org:/var/obj/usr/src/sys/server  amd64
   INSTFLG  : -1 0 -a 1
   ARCHDEFS : -DATL_OS_FreeBSD -DATL_ARCH_HAMMER -DATL_SSE3 -DATL_SSE2 -DATL_SSE1 -DATL_3DNow -DATL_USE64BITS -DATL_GAS_x8664
   F2CDEFS  : -DAdd_ -DF77_INTEGER=int -DStringSunStyle
   CACHEEDGE: 262144
   F77      : /tank/obj/sage/sage-4.5/local/bin/sage_fortran, version GNU Fortran (GCC) 4.5.1 20100715 (prerelease)
   F77FLAGS : -fomit-frame-pointer -mfpmath=387 -O2 -falign-loops=4 -fPIC -m64
   SMC      : gcc, version gcc (GCC) 4.5.1 20100715 (prerelease)
   SMCFLAGS : -fomit-frame-pointer -mfpmath=387 -O2 -falign-loops=4 -fPIC -m64
   SKC      : gcc, version gcc (GCC) 4.5.1 20100715 (prerelease)
   SKCFLAGS : -fomit-frame-pointer -mfpmath=387 -O2 -falign-loops=4 -fPIC -m64
success!
removing: _configtest.c _configtest.o _configtest
  FOUND:
    libraries = ['lapack', 'f77blas', 'cblas', 'atlas']
    library_dirs = ['/tank/obj/sage/sage-4.5/local/lib']
    language = f77
    define_macros = [('ATLAS_INFO', '"\\"3.8.3\\""')]
    include_dirs = ['/tank/obj/sage/sage-4.5/local/include']
```


Whereas, after rebuilding the shared libraries with your script, I get:

```
server% LD_LIBRARY_PATH=/usr/local/lib/gcc45:$PWD ldd lib{atlas,lapack,f77blas,cblas}.so
libatlas.so:
        libc.so.7 => /lib/libc.so.7 (0x800647000)
liblapack.so:
        libc.so.7 => /lib/libc.so.7 (0x800647000)
libf77blas.so:
        libc.so.7 => /lib/libc.so.7 (0x800647000)
libcblas.so:
        libc.so.7 => /lib/libc.so.7 (0x800647000)
server%
```


And building numpy reports that it can't decode atlas info:

```
C compiler: gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/tank/obj/sage/sage-4.5/local/include -fPIC
compile options: '-c'
gcc: _configtest.c
gcc _configtest.o -L/tank/obj/sage/sage-4.5/local/lib -llapack -lf77blas -lcblas -latlas -o _configtest/local/lib/liblapack.so: undefined reference to `_gfortran_concat_string'age-4.5/local/lib/liblapack.so: undefined reference to `csqrt'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `sqrt'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `_gfortran_st_write_done'age-4.5/local/lib/liblapack.so: undefined reference to `_gfortran_transfer_integer'-4.5/local/lib/liblapack.so: undefined reference to `cabs'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `csqrtf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `powf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `_gfortran_cpu_time_4'e/sage-4.5/local/lib/libf77blas.so: undefined reference to `_gfortran_stop_numeric'age-4.5/local/lib/liblapack.so: undefined reference to `_gfortran_pow_i4_i4'ge/sage-4.5/local/lib/liblapack.so: undefined reference to `_gfortran_st_write'age/sage-4.5/local/lib/liblapack.so: undefined reference to `log'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `lroundf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `_gfortran_compare_string'ge-4.5/local/lib/liblapack.so: undefined reference to `logf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `cabsf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `cosf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `lround'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `pow'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `cexp'
/tank/obj/sage/sage-4.5/local/lib/libf77blas.so: undefined reference to `_gfortran_transfer_character'5/local/lib/liblapack.so: undefined reference to `cos'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `cexpf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `log10'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `log10f'
collect2: ld returned 1 exit status
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `_gfortran_concat_string'age-4.5/local/lib/liblapack.so: undefined reference to `csqrt'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `sqrt'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `_gfortran_st_write_done'age-4.5/local/lib/liblapack.so: undefined reference to `_gfortran_transfer_integer'-4.5/local/lib/liblapack.so: undefined reference to `cabs'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `csqrtf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `powf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `log'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `lroundf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `_gfortran_compare_string'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `logf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `cabsf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `cosf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `lround'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `pow'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `cexp'
/tank/obj/sage/sage-4.5/local/lib/libf77blas.so: undefined reference to `_gfortran_transfer_character'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `cos'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `cexpf'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `log10'
/tank/obj/sage/sage-4.5/local/lib/liblapack.so: undefined reference to `log10f'
collect2: ld returned 1 exit status
failure.
removing: _configtest.c _configtest.o
Status: 255
Output: 
  FOUND:
    libraries = ['lapack', 'f77blas', 'cblas', 'atlas']
    library_dirs = ['/tank/obj/sage/sage-4.5/local/lib']
    language = f77
    define_macros = [('NO_ATLAS_INFO', 2)]
    include_dirs = ['/tank/obj/sage/sage-4.5/local/include']
```



---

Attachment

Second version of script, which links maths and fortran libraries


---

Comment by drkirkby created at 2010-08-03 09:57:20

Replying to [comment:14 pjeremy]:
> Replying to [comment:9 drkirkby]:
> > I'm attaching a small script, static2shared.sh, which I wrote, which will make shared libraries from the static ones. To build 64-bit shared libraries, the object files in the static library must be 64-bit ones and SAGE64 must be set to "yes". 
> > 
> > It works on the libraries libatlas liblapack libf77blas & libcblas. You could trivially modify it to work with others. 
> 
> Unfortunately, I don't believe this works.
> And building numpy reports that it can't decode atlas info:
> {{{
> C compiler: gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/tank/obj/sage/sage-4.5/local/include -fPIC
> compile options: '-c'
> gcc: _configtest.c
> 

Thank you for trying Peter. 

Since the failure reports

```
 gcc _configtest.o -L/tank/obj/sage/sage-4.5/local/lib -llapack -lf77blas -lcblas -latlas -o _configtest/local/lib/liblapack.so: undefined reference to `_gfortran_concat_string'age-4.5/local/lib/liblapack.so: undefined reference to `csqrt'
```


I thought it might be wise to link in the Fortran and maths libraries. I note this was done in the original code (at least for some libraries), but when I tried to build something with libraries, it worked OK without that, so I did not include them. I've attached a second version. Let me know how that works

Dave


---

Attachment

Replying to [comment:15 drkirkby]:
> I thought it might be wise to link in the Fortran and maths libraries. I note this was done in the original code (at least for some libraries), but when I tried to build something with libraries, it worked OK without that, so I did not include them. I've attached a second version. Let me know how that works

And attached is my adapted variant of make_correct_shared.sh that basically replicates the shared library dependencies from the original.  I have cleaned up the overall structure but haven't touched the OS-X or Solaris since I don't know the correct OS-X incantation and am not sure whether the Solaris section is still valid (I suspect not).


---

Comment by jhpalmieri created at 2010-08-03 16:31:44

With static2shared-ver2.sh, I still can't build R on mark.


---

Comment by dimpase created at 2010-08-05 20:37:11

Replying to [comment:6 wjp]:
> Replying to [comment:5 drkirkby]:
> > In ATLAS, mostly static libraries are built, and then these are converted to dynamic by the linker. I don't know if gcc can then convert a static library to a dynamic library. One might need to do that with the linker. 
> 
> The command I used in that quick test above does exactly that by using gcc as a frontend to the GNU linker.
> 

```
 gcc -shared -o liblapack.so -Wl,-soname,liblapack.so -Wl,--whole-archive liblapack.a -Wl,--no-whole-archive
```

> 
> (But I'm not claiming it's the perfect way to do it; it's just a proof of concept, not a well-researched solution.)

I just rebuilt sage 4.5.1 on skynet's taurus, and can reproduce this bug.
I also figured out why on that machine liblapack.so does not get built.

(it took a while to figure out why:
In the part of the log related to Atlas building, the last mentioning of liblapack.so is as follows:
ld -L/home/dima/sage/taurus/sage-4.5.1/local/lib -shared -soname liblapack.so -o liblapack.so --whole-archive liblapack.a --no-whole-archive -lc -lm -lgfortran
ld: skipping incompatible /home/dima/sage/taurus/sage-4.5.1/local/lib/libgfortran.so when searching for -lgfortran
ld: cannot find -lgfortran
So this command fails, resulting in liblapack.so not being build.

The reason is that $SAGELOCAL/lib/libgfortran.so points to a wrong file, to
/usr/local/gcc-4.5.1/x86_64-Linux-nehalem-fc/lib/libgfortran.so
instead of the proper one:
/usr/local/gcc-4.5.1/x86_64-Linux-nehalem-fc/lib64/libgfortran.so

This is just a wrong setup of SAGE_FORTRAN_LIB in /usr/local/skynet_bash_profile for this machine. (I posted on this on sage-skynet, and it is now fixed)

I fixed the link manually and  rebuilt the Atlas spkg, getting the liblapack.so)

As well, Willem Jan's gcc fix above cures the problem, seemingly.


---

Comment by dimpase created at 2010-08-05 20:38:35

Replying to [comment:18 dimpase]:
> Replying to [comment:6 wjp]:
> > Replying to [comment:5 drkirkby]:
> > > In ATLAS, mostly static libraries are built, and then these are converted to dynamic by the linker. I don't know if gcc can then convert a static library to a dynamic library. One might need to do that with the linker. 
> > 
> > The command I used in that quick test above does exactly that by using gcc as a frontend to the GNU linker.
> > 
> {{{
>  gcc -shared -o liblapack.so -Wl,-soname,liblapack.so -Wl,--whole-archive liblapack.a -Wl,--no-whole-archive
> }}}
> > 
> > (But I'm not claiming it's the perfect way to do it; it's just a proof of concept, not a well-researched solution.)
> 
> I just rebuilt sage 4.5.1 on skynet's taurus, and can reproduce this bug.

rebuilt with gcc-4.5.1, that is...


---

Comment by kcrisman created at 2013-04-26 01:41:48

Changing component from build to porting: BSD.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Outdated spkg or build system ticket, should be closed


---

Comment by dimpase created at 2020-09-27 13:00:52

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-09-27 13:06:22

Resolution: invalid
