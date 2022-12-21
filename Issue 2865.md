# Issue 2865: PolyBori fails to build on OSX 10.4 intel

Issue created by migration from Trac.

Original creator: jkantor

Original creation time: 2008-04-09 18:10:52

Assignee: polybori

CC:  polybori

The build failed at polybori with the following error


```
g++ -o polybori/polybori -s -bundle Cudd/obj/cuddObj.os Cudd/util/cpu_stats.os Cudd/util/cpu_time.os Cudd/util/datalimit.os Cudd/util/getopt.os Cudd/util/pathsearch.os Cudd/util/pipefork.os Cudd/util/prtime.os Cudd/util/ptime.os Cudd/util/safe_mem.os Cudd/util/state.os Cudd/util/strsav.os Cudd/util/stub.os Cudd/util/texpand.os Cudd/util/tmpfile.os Cudd/cudd/cuddAddAbs.os Cudd/cudd/cuddAddApply.os Cudd/cudd/cuddAddFind.os Cudd/cudd/cuddAddInv.os Cudd/cudd/cuddAddIte.os Cudd/cudd/cuddAddNeg.os Cudd/cudd/cuddAddWalsh.os Cudd/cudd/cuddAndAbs.os Cudd/cudd/cuddAnneal.os Cudd/cudd/cuddApa.os Cudd/cudd/cuddAPI.os Cudd/cudd/cuddApprox.os Cudd/cudd/cuddBddAbs.os Cudd/cudd/cuddBddCorr.os Cudd/cudd/cuddBddIte.os Cudd/cudd/cuddBridge.os Cudd/cudd/cuddCache.os Cudd/cudd/cuddCheck.os Cudd/cudd/cuddClip.os Cudd/cudd/cuddCof.os Cudd/cudd/cuddCompose.os Cudd/cudd/cuddDecomp.os Cudd/cudd/cuddEssent.os Cudd/cudd/cuddExact.os Cudd/cudd/cuddExport.os Cudd/cudd/cuddGenCof.os Cudd/cudd/cuddGenetic.os Cudd/cudd/cuddGroup.os Cudd/cudd/cuddHarwell.os Cudd/cudd/cuddInit.os Cudd/cudd/cuddInteract.os Cudd/cudd/cuddLCache.os Cudd/cudd/cuddLevelQ.os Cudd/cudd/cuddLinear.os Cudd/cudd/cuddLiteral.os Cudd/cudd/cuddMatMult.os Cudd/cudd/cuddPriority.os Cudd/cudd/cuddRead.os Cudd/cudd/cuddRef.os Cudd/cudd/cuddReorder.os Cudd/cudd/cuddSat.os Cudd/cudd/cuddSign.os Cudd/cudd/cuddSolve.os Cudd/cudd/cuddSplit.os Cudd/cudd/cuddSubsetHB.os Cudd/cudd/cuddSubsetSP.os Cudd/cudd/cuddSymmetry.os Cudd/cudd/cuddTable.os Cudd/cudd/cuddUtil.os Cudd/cudd/cuddWindow.os Cudd/cudd/cuddZddCount.os Cudd/cudd/cuddZddFuncs.os Cudd/cudd/cuddZddGroup.os Cudd/cudd/cuddZddIsop.os Cudd/cudd/cuddZddLin.os Cudd/cudd/cuddZddMisc.os Cudd/cudd/cuddZddPort.os Cudd/cudd/cuddZddReord.os Cudd/cudd/cuddZddSetop.os Cudd/cudd/cuddZddSymm.os Cudd/cudd/cuddZddUtil.os Cudd/dddmp/dddmpBinary.os Cudd/dddmp/dddmpConvert.os Cudd/dddmp/dddmpDbg.os Cudd/dddmp/dddmpLoad.os Cudd/dddmp/dddmpLoadCnf.os Cudd/dddmp/dddmpNodeAdd.os Cudd/dddmp/dddmpNodeBdd.os Cudd/dddmp/dddmpNodeCnf.os Cudd/dddmp/dddmpStoreAdd.os Cudd/dddmp/dddmpStoreBdd.os Cudd/dddmp/dddmpStoreCnf.os Cudd/dddmp/dddmpStoreMisc.os Cudd/dddmp/dddmpUtil.os Cudd/mtr/mtrBasic.os Cudd/mtr/mtrGroup.os Cudd/st/st.os Cudd/epd/epd.os polybori/src/BoolePolyRing.os polybori/src/BooleEnv.os polybori/src/BoolePolynomial.os polybori/src/BooleVariable.os polybori/src/CErrorInfo.os polybori/src/PBoRiError.os polybori/src/CCuddFirstIter.os polybori/src/CCuddNavigator.os polybori/src/BooleMonomial.os polybori/src/BooleSet.os polybori/src/LexOrder.os polybori/src/CCuddLastIter.os polybori/src/CCuddGetNode.os polybori/src/BooleExponent.os polybori/src/DegLexOrder.os polybori/src/DegRevLexAscOrder.os polybori/src/pbori_routines.os polybori/src/BlockDegLexOrder.os polybori/src/BlockDegRevLexAscOrder.os -L/Users/kantor/sage-3.0.alpha1/local/lib -L/Users/kantor/sage-3.0.alpha1/local/lib/python2.5/config -Lpolybori -Lgroebner -LCudd -ldl -lm
/usr/bin/ld: can't use -s with -bundle (file must contain at least global symbols, for maximum stripping use -x)
collect2: ld returned 1 exit status
```




---

Comment by mabshoff created at 2008-04-10 00:36:32

The spkg at

http://sage.math.washington.edu/home/mabshoff/SPKG/polybori-0.3.1.p0.spkg

fixes the issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-10 01:22:37

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-10 01:22:37

The final spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha4/polybori-0.3.1.p0.spkg

Instead of the original quick fix spkg this one now copies over a modified SConstruct that does not use the `-s` flag when linking.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-10 01:22:37

Changing assignee from polybori to mabshoff.


---

Comment by jkantor created at 2008-04-10 01:51:30

This version seems to build fine on OSX 10.4


---

Comment by mabshoff created at 2008-04-10 01:52:06

Merged in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-10 01:52:06

Resolution: fixed


---

Comment by PolyBoRi created at 2008-04-10 04:54:15

Resolution changed from fixed to 


---

Comment by PolyBoRi created at 2008-04-10 04:54:15

Bad solution:
The provided SConstruct should work, when using the LINKFLAGS parameter.
scons LINKFLAGS= <SCONSTARGET>

Try
scons --help
for a list of parameters


---

Comment by PolyBoRi created at 2008-04-10 04:54:15

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-04-10 12:43:25

Resolution: fixed


---

Comment by mabshoff created at 2008-04-10 12:43:25

This is not a bad solution. The provided SConstruct *apppends* `-s` regardless. Setting LINKFLAGS will not fix the problem.

Cheers,

Michael


---

Comment by PolyBoRi created at 2008-04-11 08:35:28

Can you provide me the output of


scons -h LINKFLAGS=""


please?
Michael, the *real* one
