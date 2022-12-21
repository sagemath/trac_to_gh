# Issue 6275: atlas-3.8.3.p2 dumps core on Solaris 10 with gcc 4.4.0

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-06-13 15:11:39

Assignee: tbd

Keywords: solaris atlas

Running on t2.math.washington.edu (a Sun T5240 running Solaris 10 update 4), the build of ATLAS fails when building sage-4.0.1.alpha0. (A sqlite bug was fixed first to allow Sage to start building ATLAS). 

I did post this to sage-devel under the title "atlas-3.8.3.p2 failing on Solaris 10 with gcc-4.4.0" William Stein copied this to  Clint Whaley -- the main ATLAS developer.



Here's the last bit of the error. A full copy of all the output is attached file 





make[6]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/src/testing'
make[6]: `zlib.grd' is up to date.
make[6]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/src/testing'
make clib.grd
make[6]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/src/testing'
make[6]: `clib.grd' is up to date.
make[6]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/src/testing'
make[5]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/src/testing'
make INSTALL_LOG/L1CacheSize
make[5]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'
cp /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo/res/L1CacheSize INSTALL_LOG/.
make[5]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'
make INSTALL_LOG/sMULADD pre=s
make[5]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'
cp /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo/res/sMULADD INSTALL_LOG/.
make[5]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'
make INSTALL_LOG/dMULADD pre=d
make[5]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'
cp /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo/res/dMULADD INSTALL_LOG/.
make[5]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'
make[4]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'
make[4]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'
cd /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm ; make res/dMMRES pre=d nb=88
make[5]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm'
make xmmsearch
make[6]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm'
make[6]: `xmmsearch' is up to date.
make[6]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm'
./xmmsearch -p d
Precision='d', FORCE=0, LAT=-1, nreg=-1, MaxL1=128
NB setting not supplied; calculating:
make[6]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm'
rm -f res/L1CacheSize
cd /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo ; make res/L1CacheSize
make[7]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo'
make[7]: `res/L1CacheSize' is up to date.
make[7]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo'
ln -s /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo/res/L1CacheSize res/L1CacheSize
make[6]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm'

      Read in L1 Cache size as = 8KB.
tmp=4, tL1size=1024

      Read in L1 Cache size as = 8KB.
L1Size=1024, pre=d, Smallnb=0
Assertion failed: nb, file /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/../src//tune/blas/gemm/mmsearch.c, line 1106
mmnreg = 47

NB's to try: 28   20   24   16   32

make[5]: *** [res/dMMRES] Abort (core dumped)
make[5]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm'
make[4]: *** [/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm/res/dMMRES] Error 2
make[4]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'
Assertion failed: fp, file /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/../src//bin/atlas_install.c, line 376


IN STAGE 1 INSTALL:  SYSTEM PROBE/AUX COMPILE


   Level 1 cache size calculated as 8KB
   dFPU: Separate multiply and add instructions with 1 cycle pipeline.
         Apparent number of registers : 3
         Register-register performance=330.93MFLOPS
   sFPU: Separate multiply and add instructions with 2 cycle pipeline.
         Apparent number of registers : 5
         Register-register performance=642.85MFLOPS


IN STAGE 2 INSTALL:  TYPE-DEPENDENT TUNING


STAGE 2-1: TUNING PREC='d' (precision 1 of 4)


   STAGE 2-1-1 : BUILDING BLOCK MATMUL TUNE
make -f Makefile INSTALL_LOG/dMMRES pre=d 2>&1 | ./xatlas_tee INSTALL_LOG/dMMSEARCH.LOG
Abort - core dumped
make[3]: *** [build] Error 134
make[3]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build'
make[2]: *** [build] Error 2
make[2]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build'
Failed to build ATLAS.
Failed to build ATLAS.

real    46m55.681s
user    37m30.636s
sys     2m54.685s



---

Comment by drkirkby created at 2009-06-13 15:21:25

IGNORE THIS - THE ATTACHMENT DID NOT GET ATTACHED - SEE THE NEXT TICKET (6276)


---

Comment by craigcitro created at 2009-06-13 21:12:52

Resolution: duplicate


---

Comment by craigcitro created at 2009-06-13 21:12:52

Closing this as a duplicate of #6276.
