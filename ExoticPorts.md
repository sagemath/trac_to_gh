I'll put some info here on what I needed to build Sage on some exotic archs.

Related: #29143 - Add to tox.ini 32-bit linux environments and other architectures supported by docker

## [SageMath](SageMath) 9.0

### Raspberry Pi 4B 2GB running Raspbian Buster

* Date: 01-01-2020

> Building with MAKE='make -j3' make succeeded after a few hick-ups. There was a running sage.
> Building the docs succeeded.
> make ptestlong Total time for all tests: 31805.4 seconds
>    cpu time: 40221.9 seconds
>   cumulative wall time: 50534.2 seconds
> A lot of random(?) time outs and segmentation faults

In a few days I will build sage on a Raspberry Pi 4B with 4 GB running on a USB-ssd

*  [https://groups.google.com/forum/#!topic/sage-devel/yngGVDsQ85k ](https://groups.google.com/forum/#!topic/sage-devel/yngGVDsQ85k)


## [SageMath](SageMath) 8.9

### Raspberry Pi 4B running Raspbian Buster

> Building with MAKE='make -j3' make succeeded partially. There was a running sage, building the docs failed.



## [SageMath](SageMath) 8.2

### Raspberry Pi running Ubuntu 16.04

[As reported on sage-devel](https://groups.google.com/d/msg/sage-devel/rR1VPpTC-lM/yWgotdg-BwAJ),

> Upgrading to gcc-6, g++-6 and gfortran-6 from the ubuntu toolchain ppa
> and adding some swap made 'make build' work. There's still some error
> with building the documentation, but that's a separate issue.

## Sage 5.13

### Raspberry Pi running Raspbian (armv6 with hard floats)

* Surprisingly ATLAS built without problems, surely because ATLAS tries to be smart only for ARMv7.
* for some libs (I'd say linbox or libmari(e)) the RAM was not large enough, I had to add some swap space.
* libmarie triggers an ICE in GCC. Lowering optimization to "-O0" solves the problem.
* tachyon fails to build but that's just because our install script does not even try.

### ARMv7 board running Ubuntu 12.04 (armv7 with hard floats)

* ATLAS has to be tweaked to build with hard floats. Follow instructions at http://math-atlas.sourceforge.net/errata.html#armhardfp. I also had to bypass throttling detection: modify 
* pil did not build because of libjpeg misdetection (the lib is installed, the headers aren't, so pil thinks it can include jpeg support but then compiling fails, kind of like #7273). I modified setup.py so that it does not even try to detect libjpeg.

### Sun Ultrasparc T1/2 running debian/sparc (64 bit kernel, 32 bit userland, 32 bit Sage build)

* Be sure to export ABI=32 so that MPIR and so on are not too smart and don't try to build 64 bit libs.
* PARI fails to build because it tries to include asm for 64 bit sparc v9 but gcc defaults to 32 bit sparc v8. Passing CFLAGS="-m32 -O3 -Wa,-xarch=v8plus -mcpu=ultrasparc  -g" solves this first issue (it seems to be an fsf gcc-4.7.3 bug, no problem with debian gcc 4.6.4). Then it tries to feed "-mimpure-text" to gcc which is not supported on linux anymore, modify config/get_dlld (this is fixed upstream in rev b2bc4faa4). 
* ecl fails after building the minimal initial version of ecl, lwowering the optimization to -O1 solves this.
* tachyon fails for the same stupid reason as on the raspberry pi.
* flint fails because we have to feed gcc with -mno-relax when packing shared obj. Fixed upstream at 38d45090d5e46e7237 and in 2.4.

### Sun Ultrasparc T2 running Solaris 10 (64 bit kernel, 32 bit userland, 32 bit Sage build)

* Singular fails to buid because my system is oddly configured and a fix for very old versions of gcc includes some headers it should not. This is fixed upstream.
* FFLAS-FFLAPACK fails to build. (The new?) ATLAS needs to be linked with "-lrt" (realtime lib), see https://github.com/sagemath/sage/issues/10508?cversion=1&cnum_hist=415#comment:407.

### Sun Ultrasparc T1/2 running debian/sparc (64 bit kernel, 32 bit userland, 64 bit Sage build)

* Be sure to export something like CC="gcc -m64" if your gcc builds 32 bit objects by default. ABI=64 should not hurt.
* PARI tries to feed "-mimpure-text" to gcc which is not supported on linux anymore, modify config/get_dlld (this is fixed upstream in rev b2bc4faa4). 
* tachyon fails for the same stupid reason as before.
* flint fails because we have to feed gcc with -mno-relax when packing shared obj. Fixed upstream at 38d45090d5e46e7237 and in 2.4.
* Singular fails, ld complaining about icompatibility between sparcv9 and sparc. -melf64_sparc should be passed to ld, through SLDFLAGS, defined in Singular/configure.in

### Sun Ultrasparc T2 running Solaris 10 (64 bit kernel, 32 bit userland, 64 bit Sage build)

* Don't forget to set SAGE64=yes.
* This is not used by gcc, to build gcc pass something like CC="gcc -m64" or CFLAGS="-m64", or GCC_CONFIGURE="--target=sparc64-sun-solaris2.10 --host=sparc64-sun-solaris2.10" to build a 64 bit compiler targetting 64 bit builds, but GCC fails to build, probably in stage 1, looking for sparc64-sun-solaris2.10-gcc.
  In fact passing --build=sparc64-sun-solaris2.10 and only this does the trick.
* gf2x fails because of https://gforge.inria.fr/tracker/index.php?func=detail&aid=16531&group_id=1874&atid=6979, see #15273.
* ATLAS fails, getting "Arithmetic Error" in dR2K.sum when UST2 arch is used, then it falls back to USIV but fails with a mixture of -m64 (because of SAGE64 I guess) and -m32 (why?!? wrong ATLAS setting?) mixture, then falls back to USIII where it succeeded. See http://sourceforge.net/p/math-atlas/support-requests/934/ .