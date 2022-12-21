# Issue 6603: [with SPKG, need review] COIN-OR / CBC for SAGE

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-07-23 14:35:48

Assignee: jkantor

CBC is a Free ( though not GPL-compatible ) Linear Program and Mixed Integer Program Solver from the COIN-OR suite.

Even though it is not Free and will have to remain an optional package, COIN-OR has performances way above GLPK which is to be used by default in SAGE ( see http://trac.sagemath.org/sage_trac/ticket/6502 and http://groups.google.com/group/sage-devel/browse_thread/thread/9da47e06bcdfc49f )

This SPKG contains the last version of CBC and a Cython class to make it available through numerical.mip when installed.

The SPKG can be found at this address :
http://www-sop.inria.fr/members/Nathann.Cohen/cbc.spkg

I hope you will like it ! ;-)


---

Comment by wdj created at 2009-07-25 14:37:13

ON an amd64 ubuntu 9.04 machine, I got an error in installationof cbc. Here is the tail:


```

make[2]: Leaving directory `/home/wdj/sagefiles/sage-4.1.1.alpha0/spkg/build/cbc-2.3/src'
make[1]: Leaving directory `/home/wdj/sagefiles/sage-4.1.1.alpha0/spkg/build/cbc-2.3/src'
python: can't open file 'setup.py': [Errno 2] No such file or directory

real    12m35.674s
user    10m40.044s
sys     1m53.819s
sage: An error occurred while installing cbc-2.3
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/wdj/sagefiles/sage-4.1.1.alpha0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/home/wdj/sagefiles/sage-4.1.1.alpha0/spkg/build/cbc-2.3 and type 'make'.
Instead type "/home/wdj/sagefiles/sage-4.1.1.alpha0/sage -sh"
in order to set all environment variables correctly, then cd to
/home/wdj/sagefiles/sage-4.1.1.alpha0/spkg/build/cbc-2.3
(When you are done debugging, you can type "exit" to leave the
subshell.)
```


Any idea what the problem is?


---

Comment by ncohen created at 2009-07-26 00:06:29

It comes from the fact that I stupidly forgot to add a "cd .." somewhere... I just updated the spkg, it should work a bit better now ;-)


---

Comment by wdj created at 2009-07-27 01:47:00

This installs fine on an amd64 ubuntu 9.04 machine and passes sage -testall.

Unless there are further tests to run, I give this a positive review as an optional package.


---

Comment by ncohen created at 2009-07-27 05:15:17

This spkg creates a class numerical.MIPCoin, but it is an extension to numerical.MIP ( see http://trac.sagemath.org/sage_trac/ticket/6502 ), and I think the reviewing process of these two files should go in paralell ;-)

( And I also hope there will be nothing to change :-) )


---

Comment by ncohen created at 2009-07-28 12:25:56

I just updated the SPKG, which now raises exceptions when the computations are wrong for some reason, and added some bugfixes ;-)


---

Comment by ncohen created at 2009-07-28 12:25:56

Changing type from defect to enhancement.


---

Comment by wdj created at 2009-07-30 19:15:45

Regarding the problems in #6502, the last thing you said was "I suggest we wait until 4.1.1 is out." 

We are now at 4.1.1.rc0. Would you like more checking done on this ticket? On #6502? Wait for 4.1.1.final to 
retest both?


---

Comment by ncohen created at 2009-07-30 19:26:04

The only thing that can be checked on this SPKG for the moment is the installation process. Most of the tests will occur during the reviewing of #6502 .

It seems you had some problems in #6502 applying the patch I posted, and I thought it may be because I was working on an old version of SAGE. If you are available to review #6502 I would be glad to install a new one and create a new patch for this version, containing all the stuff related to the class mip. It will take some time though, as I have to compile SAGE ( there is no binary version for my distribution ). Do you know how I could download the sources Sage 4.1.1.rc0 ?

As soon as it will be compiled, you will have the new patch ! ;-)

Thank you !


---

Comment by wdj created at 2009-07-30 19:47:10

You can find it here: http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.rc0.tar


---

Comment by wdj created at 2009-08-01 16:11:15

I just gave #6502 a positive review. Does that mean this can change to positive as well?


---

Comment by ncohen created at 2009-08-01 16:18:58

I just updated the spkg to fix something important that I did not notice because I always worked on Integer programs. I also added an Exception in the case where the user tries to solve() a program without having defined its objective function, but that is all :-)


---

Comment by wdj created at 2009-08-01 23:36:32

This cbc-2.3.spkg package installs fine for 4.1.1.a1 on an amd64 ubuntu 9.04 machine and passes sage -testall, except for the known failures (abstract_method.py and lazy_attribute.py).

Nathann, can you tell me which existing Sage python or cython files (if any) your package modifies? Does it modify any files in another spkg (other than cbc, I mean)?


---

Comment by ncohen created at 2009-08-02 06:19:00

This spkg just install all the Cbc-related librarires with a regular /configure && make && make install, then installs the class sage.numerical.mipCoin with a setup.py script ( which, if I make no mistake, creates no file except in the build/directory.

In the end, I'd say this package does not touch a hair of any pre-existing file in Sage ! ;-)


---

Comment by wdj created at 2009-08-03 14:47:06

Okay, thanks.

Changing this to "positive review" as an optional package.


---

Comment by mvngu created at 2009-09-02 08:50:33

Resolution: fixed


---

Comment by mvngu created at 2009-09-02 08:50:33

Merged in optional packages repository. See this page



http://www.sagemath.org/packages/optional/



and CBC is available at



http://www.sagemath.org/packages/optional/cbc-2.3.spkg


---

Comment by mvngu created at 2009-09-02 08:50:33

Changing component from numerical to optional packages.


---

Comment by bascorp created at 2010-04-30 11:55:49

[spring pictures](http://top20search.biz/)
