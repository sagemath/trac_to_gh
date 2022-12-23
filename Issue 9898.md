# Issue 9898: PARI/GP (2.4.3-svn) self-test fails after self-tuning on Pentium 4 Prescott

Issue created by migration from https://trac.sagemath.org/ticket/9899

Original creator: leif

Original creation time: 2010-09-11 22:35:44

Assignee: leif

CC:  jdemeyer

Keywords: mathilbert SAGE_TUNE SAGE_CHECK

On Ubuntu 9.04 x86 (Pentium 4 Prescott, gcc 4.3.3) I get the following when (re)installing PARI 2.4.3.svn-12577.p5 with `SAGE_TUNE_PARI=yes` and `SAGE_CHECK=yes`:


```
...
==========================================================================
Building and tuning PARI (this may take a while)
...
Bye !
Building and installing PARI/GP...
Making gp in Olinux-i686
...
real	20m58.068s
user	20m28.501s
sys	0m20.849s
Successfully installed pari-2.4.3.svn-12577.p5
Running the test suite.
Making test-all in Olinux-i686
...
* Testing analyz 	for gp-sta..TIME=28	for gp-dyn..TIME=36
* Testing apply 	for gp-sta..TIME=0	for gp-dyn..TIME=8
* Testing aurifeuille 	for gp-sta..TIME=4	for gp-dyn..TIME=8
* Testing bezout 	for gp-sta..TIME=4	for gp-dyn..TIME=8
* Testing bnfisintnorm 	for gp-sta..TIME=1124	for gp-dyn..TIME=1164
* Testing bnr 	for gp-sta..TIME=36	for gp-dyn..TIME=44
* Testing charpoly 	for gp-sta..TIME=4	for gp-dyn..TIME=8
* Testing combinat 	for gp-sta..TIME=36	for gp-dyn..TIME=12
* Testing compat 	for gp-sta..TIME=448	for gp-dyn..TIME=432
* Testing contfrac 	for gp-sta..TIME=4	for gp-dyn..TIME=8
* Testing debugger 	for gp-sta..TIME=8	for gp-dyn..TIME=4
* Testing ell 	for gp-sta..TIME=18781	for gp-dyn..TIME=18869
* Testing elliptic 	for gp-sta..TIME=44	for gp-dyn..TIME=36
* Testing ellsea 	for gp-sta..TIME=27077	for gp-dyn..TIME=27025
* Testing ellweilpairing 	for gp-sta..TIME=128	for gp-dyn..TIME=108
* Testing err 	for gp-sta..TIME=4	for gp-dyn..TIME=4
* Testing exact0 	for gp-sta..TIME=4	for gp-dyn..TIME=4
* Testing extract 	for gp-sta..TIME=8	for gp-dyn..TIME=8
* Testing ff 	for gp-sta..TIME=884	for gp-dyn..TIME=820
* Testing ffisom 	for gp-sta..TIME=700	for gp-dyn..TIME=684
* Testing galois 	for gp-sta..TIME=25029	for gp-dyn..TIME=25569
* Testing galoisinit 	for gp-sta..TIME=7304	for gp-dyn..TIME=7276
* Testing graph 	for gp-sta..TIME=24	for gp-dyn..TIME=32
* Testing ideal 	for gp-sta..TIME=8	for gp-dyn..TIME=4
* Testing idealappr 	for gp-sta..TIME=4	for gp-dyn..TIME=8
* Testing idealramgroups 	for gp-sta..TIME=3576	for gp-dyn..TIME=3580
* Testing intformal 	for gp-sta..TIME=4	for gp-dyn..TIME=8
* Testing intnum 	for gp-sta..TIME=30797	for gp-dyn..TIME=31073
* Testing ispower 	for gp-sta..TIME=7604	for gp-dyn..TIME=7632
* Testing krasner 	for gp-sta..TIME=6996	for gp-dyn..TIME=7000
* Testing linear 	for gp-sta..BUG [20]	for gp-dyn..BUG [36]
* Testing list 	for gp-sta..TIME=96	for gp-dyn..TIME=60
* Testing lll 	for gp-sta..TIME=0	for gp-dyn..TIME=4
* Testing mat 	for gp-sta..TIME=4	for gp-dyn..TIME=8
* Testing matsnf 	for gp-sta..TIME=816	for gp-dyn..TIME=760
* Testing member 	for gp-sta..TIME=136	for gp-dyn..TIME=108
* Testing modpr 	for gp-sta..TIME=0	for gp-dyn..TIME=4
* Testing multivar-mul 	for gp-sta..TIME=17417	for gp-dyn..TIME=19153
* Testing nf 	for gp-sta..TIME=4128	for gp-dyn..TIME=4072
* Testing nffactor 	for gp-sta..TIME=20721	for gp-dyn..TIME=20745
* Testing nfhilbert 	for gp-sta..TIME=8	for gp-dyn..TIME=12
* Testing nfields 	for gp-sta..TIME=248	for gp-dyn..TIME=216
* Testing nfrootsof1 	for gp-sta..TIME=45166	for gp-dyn..TIME=45766
* Testing number 	for gp-sta..TIME=76	for gp-dyn..TIME=48
* Testing objets 	for gp-sta..TIME=4	for gp-dyn..TIME=4
* Testing partition 	for gp-sta..TIME=60831	for gp-dyn..TIME=62931
* Testing polchebyshev 	for gp-sta..TIME=16	for gp-dyn..TIME=20
* Testing polmod 	for gp-sta..TIME=4	for gp-dyn..TIME=8
* Testing polred 	for gp-sta..TIME=6104	for gp-dyn..TIME=6136
* Testing polyser 	for gp-sta..TIME=16	for gp-dyn..TIME=28
* Testing printf 	for gp-sta..TIME=4	for gp-dyn..TIME=16
* Testing program 	for gp-sta..TIME=44	for gp-dyn..TIME=28
* Testing qf 	for gp-sta..TIME=4	for gp-dyn..TIME=4
* Testing qfbsolve 	for gp-sta..TIME=3576	for gp-dyn..TIME=3756
* Testing quad 	for gp-sta..TIME=0	for gp-dyn..TIME=8
* Testing quadclassunit 	for gp-sta..TIME=17357	for gp-dyn..TIME=18169
* Testing quadray 	for gp-sta..TIME=1232	for gp-dyn..TIME=1256
* Testing random 	for gp-sta..TIME=12	for gp-dyn..TIME=12
* Testing resultant 	for gp-sta..TIME=22545	for gp-dyn..TIME=23341
* Testing rfrac 	for gp-sta..TIME=6680	for gp-dyn..TIME=7128
* Testing rnf 	for gp-sta..TIME=564	for gp-dyn..TIME=548
* Testing rnfkummer 	for gp-sta..TIME=87353	for gp-dyn..TIME=87361
* Testing round4 	for gp-sta..TIME=13872	for gp-dyn..TIME=13904
* Testing select 	for gp-sta..TIME=8	for gp-dyn..TIME=4
* Testing stark 	for gp-sta..TIME=47794	for gp-dyn..TIME=47862
* Testing subcyclo 	for gp-sta..TIME=4	for gp-dyn..TIME=8
* Testing subfields 	for gp-sta..TIME=24165	for gp-dyn..TIME=24129
* Testing sumiter 	for gp-sta..TIME=52	for gp-dyn..TIME=44
* Testing thue 	for gp-sta..TIME=3756	for gp-dyn..TIME=3932
* Testing trans 	for gp-sta..TIME=112	for gp-dyn..TIME=84
* Testing zetak 	for gp-sta..TIME=5560	for gp-dyn..TIME=5520
* Testing zn 	for gp-sta..TIME=8	for gp-dyn..TIME=8
+++ [BUG] Total bench for gp-sta is 521185
+++ [BUG] Total bench for gp-dyn is 528713

PROBLEMS WERE NOTED. The following files list them in diff format: 
Directory: /home/leif/Sage/sage-4.6.prealpha4/spkg/build/pari-2.4.3.svn-12577.p5/src/Olinux-i686
	linear-sta.dif
	linear-dyn.dif
make[1]: *** [test-all] Error 1
make[1]: Leaving directory `/home/leif/Sage/sage-4.6.prealpha4/spkg/build/pari-2.4.3.svn-12577.p5/src/Olinux-i686'
make: *** [test-all] Error 2
Error: PARI failed the self-tests when running 'make -j8 test-all'
*************************************
Error testing package ** pari-2.4.3.svn-12577.p5 **
*************************************
sage: An error occurred while testing pari-2.4.3.svn-12577.p5
...
```


The attached diffs generated by PARI look weird since PARI breaks the output into fixed width lines (and compares these) - even *within numbers* that would fit on a single line. 

I've reformatted both the expected and the actual output s.t. the differences are more readable; now more obviously this is just *numerical noise*:

```diff
--- pari-test-linear.should.reformatted.txt	2010-09-11 21:13:22.000000000 +0200
+++ pari-test-linear.is.reformatted.txt	2010-09-11 23:25:41.000000000 +0200
@@ -1,7 +1,7 @@
 ? (1.*mathilbert(7))^(-1)
 
 [       49.000000000000000000000000000001579425
-     -1176.0000000000000000000000000000621879
+     -1176.0000000000000000000000000000621902
       8820.0000000000000000000000000005948011
     -29400.000000000000000000000000002301748
      48510.000000000000000000000000004207809
@@ -9,7 +9,7 @@
      12012.000000000000000000000000001189528]
 
 [    -1176.0000000000000000000000000000626175
-     37632.000000000000000000000000002469695
+     37632.000000000000000000000000002469681
    -317520.00000000000000000000000002364675
    1128960.0000000000000000000000000915946
   -1940400.0000000000000000000000001675308
@@ -17,7 +17,7 @@
    -504504.00000000000000000000000004740575]
 
 [     8820.0000000000000000000000000006015186
-   -317520.00000000000000000000000002375151
+   -317520.00000000000000000000000002375139
    2857680.0000000000000000000000002275919
  -10584000.000000000000000000000000882085
   18711000.000000000000000000000001614074
@@ -25,7 +25,7 @@
    5045040.0000000000000000000000004570220]
 
 [   -29400.000000000000000000000000002335330
-   1128960.0000000000000000000000000922894
+   1128960.0000000000000000000000000922890
  -10584000.000000000000000000000000884843
   40320000.000000000000000000000003430862
  -72765000.000000000000000000000006279937
@@ -33,7 +33,7 @@
  -20180160.000000000000000000000001778972]
 
 [    48510.000000000000000000000000004278611
-  -1940400.0000000000000000000000001691936
+  -1940400.0000000000000000000000001691929
   18711000.000000000000000000000001622888
  -72765000.000000000000000000000006294553
  133402500.00000000000000000000001152452
@@ -41,7 +41,7 @@
   37837800.000000000000000000000003265792]
 
 [   -38808.000000000000000000000000003696181
-   1596672.0000000000000000000000001462360
+   1596672.0000000000000000000000001462353
  -15717240.000000000000000000000001403167
   62092800.000000000000000000000005443713
 -115259760.00000000000000000000000996866
@@ -49,7 +49,7 @@
  -33297264.000000000000000000000002825670]
 
 [    12012.000000000000000000000000001213544
-   -504504.00000000000000000000000004803250
+   -504504.00000000000000000000000004803228
    5045040.0000000000000000000000004610120
  -20180160.000000000000000000000001788903
   37837800.000000000000000000000003276393
```


At least in Sage 4.6.alpha0 the slight deviation doesn't affect `ptestlong`, i.e. all tests passed regardless of PARI's self-tuning being enabled or not.

Nevertheless it's odd PARI's test suite fails with tuning enabled, since
 * Sage will reject to install the package when `SAGE_CHECK=yes`,
 * analyzing the failures is quite tedious, and
 * disabling the self-tests is potentially dangerous.

----

On the same machine running Fedora 13 x86 (gcc 4.4.4) PARI's self-tuning hangs when tuning `REMIIMUL_LIMIT`, i.e. the output stops, but `tune` doesn't terminate. This should be reported upstream as well.


---

Attachment


---

Comment by jdemeyer created at 2013-10-03 10:23:40

This refers to an old version of PARI...


---

Comment by jdemeyer created at 2013-10-03 10:23:40

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-10-03 10:23:50

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-10-05 09:39:56

Resolution: invalid
