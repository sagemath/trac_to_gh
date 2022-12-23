# Issue 9518: Add an spkg-check file for Pari

Issue created by migration from https://trac.sagemath.org/ticket/9518

Original creator: drkirkby

Original creation time: 2010-07-16 17:10:13

Assignee: drkirkby

CC:  cremona was robertwb

John Cremona remarked on #9281 that Pari had a self test that could be run from `make test-all`, so an spkg-check file should be added to do this. I will take care of it. Hopefully John can review it. 


Dave


---

Comment by cremona created at 2010-07-16 17:36:08

Changing type from defect to enhancement.


---

Comment by cremona created at 2010-07-16 17:36:08

Dave, I suggest that you leave this to be done as part of the #9343 upgrade.  I have already started working on this, including reporting some issues with the testing script upstream to par-dev.

I thought you would like this plan -- and pleasantly surprised to see that after fixing bugs they add tests to the suite.


---

Comment by drkirkby created at 2010-07-16 17:43:31

Replying to [comment:1 cremona]:
> Dave, I suggest that you leave this to be done as part of the #9343 upgrade. 

No problem. 

I actually get some failures. I'll attach the spkg-check file as an attachment, since I'd already done it. It will save you the hassle. 

I actually get some failures on my OpenSolaris machine. In fact, whilst Sage builds on OpenSolaris, it crashes at startup. So perhaps I might look at Pari as a possible source of trouble. 


```
make[1]: Leaving directory `/export/home/drkirkby/sage-4.5/spkg/build/pari-2.3.5.p2/src/Osolaris-ix86'

real	0m21.787s
user	1m52.919s
sys	0m5.264s
Successfully installed pari-2.3.5.p2
Running the test suite.
Making test-all in Osolaris-ix86
make[1]: Entering directory `/export/home/drkirkby/sage-4.5/spkg/build/pari-2.3.5.p2/src/Osolaris-ix86'
File ../src/funclist not changed.
rm -f gp-sta
gcc  -o gp-sta -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer -fPIC  -g -m64    mp.o mpinl.o Flx.o Qfb.o RgX.o alglin1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bibli1.o bibli2.o buch1.o buch2.o buch3.o buch4.o galconj.o gen1.o gen2.o gen3.o ifactor1.o perm.o polarit1.o polarit2.o polarit3.o rootpol.o subcyclo.o subgroup.o trans1.o trans2.o trans3.o anal.o compat.o default.o errmsg.o es.o init.o intnum.o members.o sumiter.o aprcl.o elldata.o elliptic.o galois.o groupid.o kummer.o mpqs.o nffactor.o part.o stark.o subfield.o thue.o gp.o gp_init.o gp_rl.o highlvl.o whatnow.o plotport.o plotnull.o    -lm -L/export/home/drkirkby/sage-4.5/local/lib -lgmp
* Testing objets 	for gp-sta..TIME=0	for gp-dyn..TIME=0
* Testing analyz 	for gp-sta..TIME=13	for gp-dyn..TIME=15
* Testing number 	for gp-sta..TIME=13	for gp-dyn..TIME=14
* Testing polyser 	for gp-sta..TIME=3	for gp-dyn..TIME=7
* Testing linear 	for gp-sta..TIME=8	for gp-dyn..TIME=5
* Testing elliptic 	for gp-sta..TIME=9	for gp-dyn..TIME=9
* Testing sumiter 	for gp-sta..TIME=17	for gp-dyn..TIME=16
* Testing graph 	for gp-sta..TIME=4	for gp-dyn..TIME=4
* Testing program 	for gp-sta..TIME=5	for gp-dyn..TIME=8
* Testing trans 	for gp-sta..TIME=42	for gp-dyn..TIME=27
* Testing nfields 	for gp-sta..TIME=137	for gp-dyn..TIME=105
* Testing compat 	for gp-sta..TIME=157	for gp-dyn..TIME=163
* Testing ellglobalred 	for gp-sta..BUG [2]	for gp-dyn..BUG [2]
* Testing galois 	for gp-sta..TIME=7763	for gp-dyn..TIME=7455
* Testing intnum 	for gp-sta..TIME=7013	for gp-dyn..TIME=7214
* Testing qfbsolve 	for gp-sta..TIME=1465	for gp-dyn..TIME=1460
* Testing rfrac 	for gp-sta..TIME=6961	for gp-dyn..TIME=7754
* Testing round4 	for gp-sta..TIME=6535	for gp-dyn..TIME=6651
* Testing stark 	for gp-sta..TIME=16150	for gp-dyn..TIME=16396
+++ [BUG] Total bench for gp-sta is 46187
+++ [BUG] Total bench for gp-dyn is 47221

PROBLEMS WERE NOTED. The following files list them in diff format: 
Directory: /export/home/drkirkby/sage-4.5/spkg/build/pari-2.3.5.p2/src/Osolaris-ix86
	ellglobalred-sta.dif
	ellglobalred-dyn.dif
make[1]: *** [test-all] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.5/spkg/build/pari-2.3.5.p2/src/Osolaris-ix86'
make: *** [test-all] Error 2
Pari failed the self-tests when running 'make test-all'
*************************************
Error testing package ** pari-2.3.5.p2 **
*************************************
sage: An error occurred while testing pari-2.3.5.p2
```



---

Comment by drkirkby created at 2010-07-16 17:44:30

spkg-check for Pari


---

Attachment

I note there is an error in `spkg-install` The very first line has some unwanted characters, with what displays as "B1;2000;0c". 

I leave you to sort that out!

 


```
drkirkby@hawk:~/sage-4.5/spkg/standard/pari-2.3.5.p1$ head  spkg-install
B1;2000;0c#!/bin/sh
###########################################
## PARI
###########################################

TOP=`pwd`

# As of PARI 2.3.3, the compiler flag -fPIC is not added on Solaris, but it
# needs to be if using gcc. I assume the equivalent will be needed on 
# other compilers. 
drkirkby@hawk:~/sage-4.5/spkg/standard/pari-2.3.5.p1$ 
```



---

Comment by cremona created at 2010-07-16 19:10:30

For an explanation of the errors see my post to pari-dev at http://pari.math.u-bordeaux.fr/archives/pari-dev-1007/threads.html and Karim's reply which I have not yet absorbed.

I have been compiling pari and running its tests for about 20 years...


---

Comment by jdemeyer created at 2010-09-08 08:27:59

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-09-08 08:28:25

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-09-08 08:28:25

There is an spkg-check in #9343 and it seems to work, so positive review.


---

Comment by mpatel created at 2010-09-10 10:47:24

Resolution: duplicate
