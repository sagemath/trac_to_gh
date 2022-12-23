# Issue 9903: ATLAS fails to build on OpenSolaris if SAGE_FAT_BINARY=yes

Issue created by migration from https://trac.sagemath.org/ticket/9904

Original creator: drkirkby

Original creation time: 2010-09-13 20:47:24

Assignee: drkirkby

CC:  jhpalmieri jsp

The subject pretty much says it all. This consistently fails for me. Two fairly critical looking messages below are:


```
/var/tmp//ccJwayyJ.s: Assembler messages:
/var/tmp//ccJwayyJ.s:35: Error: suffix or operands invalid for `mov'
```


I suspect the rest of the problems stem from that. This was on a a Sun Ultra 27 running OpenSolaris 06/2009, but I would suspect the same would happen on a Solaris 10 x86 system such as fulvia. 



```
gcc -DL2SIZE=4194304 -I/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/include -I/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/../src//include -I/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/../src//include/contrib -DAdd_ -DF77_INTEGER=int -DStringSunStyle -DATL_OS_SunOS -DATL_ARCH_HAMMER -DATL_CPUMHZ=3325 -DSUN_HR -DATL_SSE2 -DATL_SSE1 -DATL_GAS_x8632  -DATL_UCLEANM -DATL_UCLEANN -DATL_UCLEANK -fomit-frame-pointer -mfpmath=387 -O2 -falign-loops=4 -fPIC -m32 -c ATL_cupNBmm_b0.c
gcc -fPIC -m32 -DL2SIZE=4194304 -I/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/include -I/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/../src//include -I/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/../src//include/contrib -DAdd_ -DF77_INTEGER=int -DStringSunStyle -DATL_OS_SunOS -DATL_ARCH_HAMMER -DATL_CPUMHZ=3325 -DSUN_HR -DATL_SSE2 -DATL_SSE1 -DATL_GAS_x8632  -DATL_UCLEANM -DATL_UCLEANN -DATL_UCLEANK -DATL_BETA=0 -c -x assembler-with-cpp ATL_cupNBmm0_1_0_b0.c
/var/tmp//ccJwayyJ.s: Assembler messages:
/var/tmp//ccJwayyJ.s:35: Error: suffix or operands invalid for `mov'
make[7]: *** [ATL_cupNBmm0_1_0_b0.o] Error 1
make[7]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/src/blas/gemm/KERNEL'
make[6]: *** [ccleanuplib] Error 2
make[6]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/src/blas/gemm'
make[5]: *** [clib] Error 2
make[5]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/src/blas/gemm'
make[4]: *** [cmmlib] Error 2
make[4]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/tune/blas/gemm'
make[3]: *** [cinstall] Error 2
make[3]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/tune/blas/gemm'
make[2]: *** [MMinstall] Error 2
make[2]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/bin'
make[2]: Entering directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/bin'
cd /opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/tune/blas/gemm ; make res/atlas_csNKB.h
make[3]: Entering directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/tune/blas/gemm'
make csRunFindCE
make[4]: Entering directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/tune/blas/gemm'
cd /opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/src/blas/gemm ; make clib
make[5]: Entering directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/src/blas/gemm'
make auxillib ccleanuplib cusergemm
make[6]: Entering directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/src/blas/gemm'
cd /opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/src/auxil ; make lib
make[7]: Entering directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/src/auxil'
make[7]: Nothing to be done for `lib'.
make[7]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/src/auxil'
cd KERNEL ; make -f cMakefile clib
make[7]: Entering directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/src/blas/gemm/KERNEL'
gcc -fPIC -m32 -DL2SIZE=4194304 -I/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/include -I/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/../src//include -I/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/../src//include/contrib -DAdd_ -DF77_INTEGER=int -DStringSunStyle -DATL_OS_SunOS -DATL_ARCH_HAMMER -DATL_CPUMHZ=3325 -DSUN_HR -DATL_SSE2 -DATL_SSE1 -DATL_GAS_x8632  -DATL_UCLEANM -DATL_UCLEANN -DATL_UCLEANK -DATL_BETA=0 -c -x assembler-with-cpp ATL_cupNBmm0_1_0_b0.c
/var/tmp//cc1xa4zJ.s: Assembler messages:
/var/tmp//cc1xa4zJ.s:35: Error: suffix or operands invalid for `mov'
make[7]: *** [ATL_cupNBmm0_1_0_b0.o] Error 1
make[7]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/src/blas/gemm/KERNEL'
make[6]: *** [ccleanuplib] Error 2
make[6]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/src/blas/gemm'
make[5]: *** [clib] Error 2
make[5]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/src/blas/gemm'
make[4]: *** [cmmlib] Error 2
make[4]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/tune/blas/gemm'
make[3]: *** [res/atlas_csNKB.h] Error 2
make[3]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/tune/blas/gemm'
make[2]: *** [/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/tune/blas/gemm/res/atlas_csNKB.h] Error 2
make[2]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/bin'
ERROR 664 DURING CACHE EDGE DETECTION!!.
make[2]: Entering directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/bin'
cd /opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build ; make error_report
make[3]: Entering directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build'
make -f Make.top error_report
make[4]: Entering directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build'
uname -a 2>&1 >> bin/INSTALL_LOG/ERROR.LOG
gcc -v 2>&1  >> bin/INSTALL_LOG/ERROR.LOG
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/libexec/gcc/i386-pc-solaris2.10/4.5.0/lto-wrapper
Target: i386-pc-solaris2.10
Configured with: ../gcc-4.5.0/configure --prefix=/usr/local/gcc-4.5.0 --build=i386-pc-solaris2.10 --enable-languages=c,c++,fortran --with-gmp=/usr/local/gcc-4.5.0 --with-mpfr=/usr/local/gcc-4.5.0 --disable-nls --enable-checking=release --enable-werror=no --enable-multilib -with-system-zlib --enable-bootstrap --with-gnu-as --with-as=/usr/local/binutils-2.20/bin/as --without-gnu-ld --with-ld=/usr/ccs/bin/ld
Thread model: posix
gcc version 4.5.0 (GCC) 
gcc -V 2>&1  >> bin/INSTALL_LOG/ERROR.LOG
gcc: '-V' option must have argument
make[4]: [error_report] Error 1 (ignored)
gcc --version 2>&1  >> bin/INSTALL_LOG/ERROR.LOG
tar cf error_HAMMER32SSE2.tar Make.inc bin/INSTALL_LOG/*
gzip --best error_HAMMER32SSE2.tar
mv error_HAMMER32SSE2.tar.gz error_HAMMER32SSE2.tgz
make[4]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build'
make[3]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build'
make[2]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build/bin'
Error report error_<ARCH>.tgz has been created in your top-level ATLAS
directory.  Be sure to include this file in any help request.
cat: ../../CONFIG/error.txt: cannot open [No such file or directory]
cat: ../../CONFIG/error.txt: cannot open [No such file or directory]
      Performance: 5035.85 (151.45 percent of of detected clock rate)
make -f Makefile INSTALL_LOG/cNCNB pre=c 2>&1 | ./xatlas_tee INSTALL_LOG/cMMSEARCH.LOGmake -f Makefile INSTALL_LOG/cbestNN_24x24x24 pre=c nb=24 2>&1 | ./xatlas_tee INSTALL_LOG/cMMSEARCH.LOG      NCgemmNN : muladd=1, lat=5, pf=513, nb=24, mu=4, nu=1 ku=24,
                 ForceFetch=0, ifetch=3 nfetch=2
                 Performance = 5141.82 (102.10 of copy matmul, 154.64 of clock)
make -f Makefile INSTALL_LOG/cbestNT_24x24x24 pre=c nb=24 2>&1 | ./xatlas_tee INSTALL_LOG/cMMSEARCH.LOG      NCgemmNT : muladd=1, lat=6, pf=513, nb=24, mu=4, nu=1 ku=24,
                 ForceFetch=0, ifetch=3 nfetch=2
                 Performance = 4988.79 (99.07 of copy matmul, 150.04 of clock)
make -f Makefile INSTALL_LOG/cbestTN_24x24x24 pre=c nb=24 2>&1 | ./xatlas_tee INSTALL_LOG/cMMSEARCH.LOG      NCgemmTN : muladd=1, lat=2, pf=513, nb=24, mu=4, nu=1 ku=24,
                 ForceFetch=0, ifetch=3 nfetch=2
                 Performance = 4979.41 (98.88 of copy matmul, 149.76 of clock)
make -f Makefile INSTALL_LOG/cbestTT_24x24x24 pre=c nb=24 2>&1 | ./xatlas_tee INSTALL_LOG/cMMSEARCH.LOG      NCgemmTT : muladd=1, lat=8, pf=513, nb=24, mu=4, nu=1 ku=24,
                 ForceFetch=0, ifetch=3 nfetch=2
                 Performance = 4835.23 (96.02 of copy matmul, 145.42 of clock)
make -f Makefile MMinstall pre=c 2>&1 | ./xatlas_tee INSTALL_LOG/cMMSEARCH.LOG


   STAGE 2-4-2: CacheEdge DETECTION
make -f Makefile INSTALL_LOG/atlas_csNKB.h pre=c 2>&1 | ./xatlas_tee INSTALL_LOG/cMMCACHEEDGE.LOG
make[1]: *** [build] Error 255
make[1]: Leaving directory `/opt/sagemath/OpenSolaris/sage-4.5.3/spkg/build/atlas-3.8.3.p14/ATLAS-build'
make: *** [build] Error 2
Failed to build ATLAS.
```



---

Comment by jdemeyer created at 2012-08-23 18:46:48

Works for me with sage-5.3.rc0...


---

Comment by jdemeyer created at 2012-08-23 18:46:48

Resolution: worksforme
