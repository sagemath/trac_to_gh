# Issue 2994: polybori.spkg: fix permission issue of the headers

Issue created by migration from https://trac.sagemath.org/ticket/2994

Original creator: mabshoff

Original creation time: 2008-04-22 03:02:45

Assignee: mabshoff

PolyBoRi's headers have too tight permissions:

```
cp: cannot open `sage-3.0.rc1/local/include/cudd/st.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/cudd/epd.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/cudd/cudd.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/cudd/util.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/cudd/cuddInt.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/cudd/mtr.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/cudd/cuddObj.hh' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/cudd/dddmp.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/DegRevLexAscOrder.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/PBoRiOutIter.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/BooleConstant.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CTermStack.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/OrderedManager.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/polybori.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CDegLexIter.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CDDManager.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CIdxVariable.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CCuddZDD.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/order_tags.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/LexOrder.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/COrderedIter.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/groebner/pairs.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/groebner/randomset.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/groebner/groebner.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/groebner/literal_factorization.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/groebner/nf.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/groebner/lexbuckets.h' for reading: Permission denied  
cp: cannot open `sage-3.0.rc1/local/include/polybori/groebner/dlex4data.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/groebner/dp_asc4data.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/groebner/lp4data.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/groebner/groebner_defs.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/groebner/groebner_alg.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/groebner/interpolate.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/groebner/cache_manager.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/BooleRing.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CVariableNames.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CPrintOperation.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CLiteralCodes.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CDegreeCache.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/pbori_routines.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/order_traits.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CCuddFirstIter.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/pbori_traits.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CStackSelector.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CCuddNavigator.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/pbori_order.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/pbori_routines_misc.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/BooleExponent.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CTermGenerator.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CStringLiteral.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/extrafwd.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CGenericIter.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/pbori_routines_order.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/COrderProperties.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/BoolePolynomial.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/DegLexOrder.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CDelayedTermIter.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/PBoRiGenericError.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/generic_hash.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/pbori_algo.h' for reading: Permission denied  
cp: cannot open `sage-3.0.rc1/local/include/polybori/M4RI/packedmatrix.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/M4RI/cpucycles.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/M4RI/brilliantrussian.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/M4RI/watch.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/M4RI/matrix.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/M4RI/m4ri.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/M4RI/grayflex.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/pbori_routines_hash.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/BooleEnv.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CCuddLastIter.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/BlockDegLexOrder.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/BooleVariable.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/pbori_func.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CCacheManagement.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/BooleSet.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/pbori_tags.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CErrorInfo.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/COrderBase.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/pbori_routines_cuddext.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/PBoRiError.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CCuddGetNode.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CCuddCore.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CacheManager.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CExpIter.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/BooleMonomial.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CDDOperations.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/pbori_algorithms.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CDDInterface.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/BoolePolyRing.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CIdxPath.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CBidirectTermIter.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CRestrictedIter.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/BlockDegRevLexAscOrder.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/pbori_defs.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/pbori_algo_int.h' for reading: Permission denied
cp: cannot open `sage-3.0.rc1/local/include/polybori/CCuddInterface.h' for reading: Permission denied 
```

Updated spkg coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-22 04:25:27

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-22 04:25:27

With the new spkg the permission issues are gone, i.e.

```
mabshoff@modular:~$ cp -r /home2/sage/build/sage-3.0.rc1/local/ .
mabshoff@modular:~$
```

The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/final/polybori-0.3.1.p1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-22 05:14:38

Merged in Sage 3.0.final


---

Comment by mabshoff created at 2008-04-22 05:14:38

Resolution: fixed
