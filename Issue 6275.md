# Issue 6275: atlas-3.8.3.p2 dumps core on Solaris 10 with gcc 4.4.0

archive/issues_006275.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: solaris atlas\n\nRunning on t2.math.washington.edu (a Sun T5240 running Solaris 10 update 4), the build of ATLAS fails when building sage-4.0.1.alpha0. (A sqlite bug was fixed first to allow Sage to start building ATLAS). \n\nI did post this to sage-devel under the title \"atlas-3.8.3.p2 failing on Solaris 10 with gcc-4.4.0\" William Stein copied this to  Clint Whaley -- the main ATLAS developer.\n\n\n\nHere's the last bit of the error. A full copy of all the output is attached file \n\n\n\n\n\nmake[6]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/src/testing'\nmake[6]: `zlib.grd' is up to date.\nmake[6]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/src/testing'\nmake clib.grd\nmake[6]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/src/testing'\nmake[6]: `clib.grd' is up to date.\nmake[6]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/src/testing'\nmake[5]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/src/testing'\nmake INSTALL_LOG/L1CacheSize\nmake[5]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'\ncp /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo/res/L1CacheSize INSTALL_LOG/.\nmake[5]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'\nmake INSTALL_LOG/sMULADD pre=s\nmake[5]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'\ncp /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo/res/sMULADD INSTALL_LOG/.\nmake[5]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'\nmake INSTALL_LOG/dMULADD pre=d\nmake[5]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'\ncp /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo/res/dMULADD INSTALL_LOG/.\nmake[5]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'\nmake[4]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'\nmake[4]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'\ncd /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm ; make res/dMMRES pre=d nb=88\nmake[5]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm'\nmake xmmsearch\nmake[6]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm'\nmake[6]: `xmmsearch' is up to date.\nmake[6]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm'\n./xmmsearch -p d\nPrecision='d', FORCE=0, LAT=-1, nreg=-1, MaxL1=128\nNB setting not supplied; calculating:\nmake[6]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm'\nrm -f res/L1CacheSize\ncd /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo ; make res/L1CacheSize\nmake[7]: Entering directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo'\nmake[7]: `res/L1CacheSize' is up to date.\nmake[7]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo'\nln -s /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/sysinfo/res/L1CacheSize res/L1CacheSize\nmake[6]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm'\n\n      Read in L1 Cache size as = 8KB.\ntmp=4, tL1size=1024\n\n      Read in L1 Cache size as = 8KB.\nL1Size=1024, pre=d, Smallnb=0\nAssertion failed: nb, file /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/../src//tune/blas/gemm/mmsearch.c, line 1106\nmmnreg = 47\n\nNB's to try: 28   20   24   16   32\n\nmake[5]: *** [res/dMMRES] Abort (core dumped)\nmake[5]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm'\nmake[4]: *** [/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/tune/blas/gemm/res/dMMRES] Error 2\nmake[4]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/bin'\nAssertion failed: fp, file /home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build/../src//bin/atlas_install.c, line 376\n\n\nIN STAGE 1 INSTALL:  SYSTEM PROBE/AUX COMPILE\n\n\n   Level 1 cache size calculated as 8KB\n   dFPU: Separate multiply and add instructions with 1 cycle pipeline.\n         Apparent number of registers : 3\n         Register-register performance=330.93MFLOPS\n   sFPU: Separate multiply and add instructions with 2 cycle pipeline.\n         Apparent number of registers : 5\n         Register-register performance=642.85MFLOPS\n\n\nIN STAGE 2 INSTALL:  TYPE-DEPENDENT TUNING\n\n\nSTAGE 2-1: TUNING PREC='d' (precision 1 of 4)\n\n\n   STAGE 2-1-1 : BUILDING BLOCK MATMUL TUNE\nmake -f Makefile INSTALL_LOG/dMMRES pre=d 2>&1 | ./xatlas_tee INSTALL_LOG/dMMSEARCH.LOG\nAbort - core dumped\nmake[3]: *** [build] Error 134\nmake[3]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build'\nmake[2]: *** [build] Error 2\nmake[2]: Leaving directory `/home/kirkby/sage-4.0.1.alpha0/spkg/build/atlas-3.8.3.p2/ATLAS-build'\nFailed to build ATLAS.\nFailed to build ATLAS.\n\nreal    46m55.681s\nuser    37m30.636s\nsys     2m54.685s\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6275\n\n",
    "created_at": "2009-06-13T15:11:39Z",
    "labels": [
        "porting: Solaris",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "atlas-3.8.3.p2 dumps core on Solaris 10 with gcc 4.4.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6275",
    "user": "drkirkby"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/6275





---

archive/issue_comments_050122.json:
```json
{
    "body": "IGNORE THIS - THE ATTACHMENT DID NOT GET ATTACHED - SEE THE NEXT TICKET (6276)",
    "created_at": "2009-06-13T15:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6275#issuecomment-50122",
    "user": "drkirkby"
}
```

IGNORE THIS - THE ATTACHMENT DID NOT GET ATTACHED - SEE THE NEXT TICKET (6276)



---

archive/issue_comments_050123.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-06-13T21:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6275#issuecomment-50123",
    "user": "@craigcitro"
}
```

Resolution: duplicate



---

archive/issue_comments_050124.json:
```json
{
    "body": "Closing this as a duplicate of #6276.",
    "created_at": "2009-06-13T21:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6275#issuecomment-50124",
    "user": "@craigcitro"
}
```

Closing this as a duplicate of #6276.
