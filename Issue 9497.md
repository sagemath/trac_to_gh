# Issue 9497: Fix the Singular spkg so it can take advantage of building in parallel

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-07-14 13:53:39

Assignee: GeorgSWeber

Right now the Singular spkg contains the lines:

```
# since parallel make breaks the singular build
MAKE="make"
export MAKE
```


Since Singular takes a long time to build, e.g., > 8 minutes on sage.math, and 16 minutes on my laptop, it would be nice to be able to build it in parallel.

Why precisely does parallel build not work?  Maybe it is only one component of the singular build that has trouble?  Track this down, make the parts that can work to work, and the parts that can't should be explained.


---

Comment by malb created at 2010-07-15 17:13:27

cf. http://trac.sagemath.org/sage_trac/ticket/8059#comment:65


---

Comment by malb created at 2011-01-14 18:29:47

I believe this is fixed. I just ran the following on geom.math using the modified spkg-install attached to this ticket:


```sh
for i in `seq 1 16`; do 
  export MAKE="make -j$i"; 
  time ./spkg-install &> /home/malb/scratch/singular-build-log-$i; 
  tail -n 3 /home/malb/scratch/singular-build-log-$i;
done
```


The output

```
real    10m40.257s
user    9m30.120s
sys     1m17.510s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    6m59.972s
user    10m49.180s
sys     1m33.340s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    5m9.335s
user    10m38.340s
sys     1m17.190s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    4m18.527s
user    10m42.200s
sys     1m23.110s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    4m12.274s
user    10m54.550s
sys     1m26.130s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    3m40.495s
user    11m4.800s
sys     1m27.700s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    3m22.933s
user    10m15.020s
sys     1m16.510s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    3m21.500s
user    10m36.230s
sys     1m17.520s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    3m31.700s
user    11m22.920s
sys     1m18.760s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    3m10.116s
user    10m20.960s
sys     1m18.830s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    3m26.779s
user    11m42.740s
sys     1m24.450s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    3m7.259s
user    11m7.970s
sys     1m23.890s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    3m3.277s
user    10m40.610s
sys     1m19.030s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    3m3.885s
user    10m46.770s
sys     1m18.490s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    3m9.547s
user    10m43.620s
sys     1m17.870s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1

real    4m9.297s
user    11m37.370s
sys     1m16.790s
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libfac.a
ranlib /scratch/malb/sage-4.6.1.rc1/local/lib/libsingfac_g.a
Singular-3-1-1
```



---

Comment by malb created at 2011-01-14 18:29:47

Changing keywords from "" to "singular".


---

Attachment


---

Comment by malb created at 2011-01-14 18:35:00

Changing status from new to needs_review.


---

Comment by malb created at 2011-01-14 18:35:00

I cut an SPKG:

    http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-1-4.p4.spkg


---

Comment by jhpalmieri created at 2011-03-26 23:12:55

patch for p5


---

Attachment

patch for p6


---

Attachment

The spkg here needed to be rebased against the current one (which is also called "...p4.spkg").  I've rebased it, and then I made a further change: I changed "$RM" in the spkg-install file to "rm" -- this has been done in the spkg-install files for all of the other spkgs, and also see the discussion at #3537.  I've posted the patch files for the two new spkgs, for review purposes.  The two new spkgs are here:

 - [http://sage.math.washington.edu/home/palmieri/SPKG/singular-3-1-1-4.p5.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/singular-3-1-1-4.p5.spkg) -- enable parallel build
 - [http://sage.math.washington.edu/home/palmieri/SPKG/singular-3-1-1-4.p6.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/singular-3-1-1-4.p6.spkg) -- p5 and also change $RM to rm

By the way, I built p5 by applying malb's patch to the current p4.  I tested that successfully on a Mac, on sage.math, on Dave Kirkby's machine hawk (OpenSolaris), and on t2.math.washington.edu (Solaris).  I couldn't access the skynet machines, so I couldn't test on them, but this is a pretty good range of hardware.  The build was at least somewhat faster on all of them, and tests passed with the new version.  So this is almost good enough for a positive review of p5, except that I built it and I'd like another pair of eyes to look at it.  Then the changes in p6 require a review anyway.


---

Comment by drkirkby created at 2011-03-27 04:25:46

John,

I thought the parallel builds of Singular 3-1-1-4 were fixed on #9946 - where I tested a parallel build of Singular  3-1-1-4 for 500 times, with no failures. I'm a bit puzzled why parallel builds need to be enabled in this package, when they should have been done on #9946

The problem with builds that break in parallel is that they are very hard to test properly. Just because something builds a few times, does not mean it will build 100% of the time. Failures tend to be random in nature. Martin Albrecht has tested this 16 times, which I don't think is enough really. It took me more than 16 builds of Sage to find that `boehm_gc-7.1.p6` has a race condition. 

http://www.mail-archive.com/sage-devel`@`googlegroups.com/msg42997.html

BTW, 

if you use my machine hawk, and change your path to use the compilers: 


```
/usr/local/gcc-4.5.0-delayed/bin/gcc
/usr/local/gcc-4.5.0-delayed/bin/g++
/usr/local/gcc-4.5.0-delayed/bin/gfortran
```


then set an environment variable 


```
MAX_COMPILER_DELAY_IN_MICRO_SECONDS
```


to something like 100000, then it will pause a random amount of time (in the range 0 to 100 ms) before invoking the compiler. These random delays will tend to help induce race problems, as it changes the order in which files are built. The file


```
/usr/local/gcc-4.5.0-delayed/bin/gcc
```


is just a shell script, which calls something to pause for a random time before actually compiling the C file. 

{{{#!/bin/sh 
/usr/local/bin/randomsleep
/usr/local/gcc-4.5.0/bin/gcc "$`@`"
drkirkby`@`hawk:~$ 
```


In fact, I use `/usr/local/gcc-4.5.0-delayed/bin/gcc` all the time, though I rarely have `MAX_COMPILER_DELAY_IN_MICRO_SECONDS` set. 

Perhaps you can clarify what has changed here since #9946 - I'm too tired to look now. It will have to wait until I have had some sleep. 

The changes from p5 to p6 look fine, but I've not investigated what has changed between #9946 and the p5 you have created. 

Dave


---

Comment by jhpalmieri created at 2011-03-27 04:42:29

Hi Dave,

On both hawk and sage.math, I built the spkg at least 40 times with no problems at all, using a [script written by mpatel](http://trac.sagemath.org/sage_trac/ticket/8059#comment:112).  I think I'll try with your delayed compilers.

As far as what's changed, there are many instances of "make" in the spkg-install script, which the patch changes to "$MAKE".  There are a few instances which weren't changed, presumably because Martin found problems with building those parts in parallel.  In the tests I tried, the time gains were moderate, not amazing, compiling in roughly 2/3 the time when done in parallel.  But it's still an improvement.


---

Comment by jhpalmieri created at 2011-03-27 05:01:13

Okay, I've started a test on hawk.  It's using the delayed compilers, building in parallel with 12 threads, doing 100 builds.  This is in the directory /export/home/palmieri/testing/sage-4.7.alpha2/. It's using the script new.sh, which writes a log file in that directory for each build: singular-3-1-1-4-j12.log-N, where N goes from 1 to (I hope) 100.  I'm going to sleep soon, but this should be done in 7 or 8 hours.


---

Comment by jhpalmieri created at 2011-03-27 14:54:17

Dave: the test seems to have succeeded: each of the 100 builds reported building successfully.  I suppose to really test it, I should run full doctests after each build, but I didn't do that.


---

Comment by drkirkby created at 2011-03-27 21:33:52

Replying to [comment:8 jhpalmieri]:
> Dave: the test seems to have succeeded: each of the 100 builds reported building successfully.  I suppose to really test it, I should run full doctests after each build, but I didn't do that.

I think `singular-3-1-1-4.p6` is OK, but I'll wait about 12 hours before giving a positive review. That will give my tests more chance to run. I've done some longer random delays than you, which will have more chance of finding a bug, but due to the build times, it is not possible to build so many of these. 

I think the doctest idea, whilst nice, would take too long. It would probably not be 
necessary to run all the doctests, though sorting out what ones are necessary would be difficult. 

What would be useful, (and practical) is to compare the sizes of the libraries created each time. They appear to be identical. Unfortunately the md5 checksums of the files do change each time - I guess there is date/time information in them, which is not identical on each build. But I think if a package builds multiple times and the files built were always of the same length, we could be reasonably sure they are OK. I've just implemented such a change to `new.sh`, though this is only in use on the code which has random delays of up to 5 seconds. 

I think long random delays is the most likely way to find race conditions, but of course the builds take a lot longer. But there's no problem in building in many directories at the same time. If one builds Singular in N different directories with Sage in them, with a maximum delay of T seconds (mean T/2) in each directory, the mean delay is going to be T/(2*N) seconds. The fact the delays are present should mean building lots of copies of Singular at the same time does not overload the CPU. Memory might be an issue though - this machine only has 12 GB. Technically that's the maximum supported RAM in this Sun workstation, though in fact it is possible to get 3<sup>rd</sup> party 4 GB DIMMS to fit, so putting 24 GB in the machine is technically possible, though quite costly for a home computer. 

Anyway, I'll look at the test results in 12 hours or so, and unless I find any failures, I'll be giving the `singular-3-1-1-4.p6` package a positive review. 

Dave


---

Comment by jhpalmieri created at 2011-03-27 21:45:35

As far as doctesting goes, it's probably not sufficient, but testing sage/sage/libs/singular/ is a quick check to make sure things are working.


---

Comment by drkirkby created at 2011-03-28 00:26:23

Replying to [comment:10 jhpalmieri]:
> As far as doctesting goes, it's probably not sufficient, but testing sage/sage/libs/singular/ is a quick check to make sure things are working.
True. It would be nice if there was some way of knowing what tests made use of Singular or any other part of Sage. 

I've not checked this, but I've just started a build with this script.

$ make && ./new.sh

where `new.sh` is:

{{{#!/bin/bash

set -o pipefail

export MAX_COMPILER_DELAY_IN_MICRO_SECONDS=5000000
export PATH=/usr/local/gcc-4.5.0-delayed/bin/:$PATH
export CC=/usr/local/gcc-4.5.0-delayed/bin/gcc
export CXX=/usr/local/gcc-4.5.0-delayed/bin/g++

JOBS=12
RUNS=500
for I in `seq $RUNS`;
do
    LOG="singular-3-1-1-4-j$JOBS.log.$I"
    if [ ! -f "$LOG" ]; then
        env MAKE="make -j$JOBS" ./sage -f singular-3-1-1-4.p6.spkg 2>&1 | tee "$LOG"
        CODE=$?
        ./sage -b  >> "$LOG"
        ./sage -t devel/sage/sage/libs/singular/ >> "$LOG"
        echo $0 run $I of $RUNS: code= $CODE
    fi
done
```


That might well be totally broken - no idea, and are going to bed now, so I'm not going to check it. 

Dave


---

Comment by drkirkby created at 2011-03-28 00:38:33

For the record, this is what I have done so far:
 * 164 tests with a maximum delay of 20 ms. These are taking about 5 minutes to build Singular. 
 * 40 tests with a maximum delay of 500 ms. These are taking about 22 minutes to build. 
 * 10 tests with a maximum random delay of 5 seconds when invoking the compiler. These take about 21 minutes to build. 
 * 9 tests with a maximum delay of 5 seconds. These are taking about 22 minutes to build. 

All times are only *very* approximate, and are on heavily loaded machine. (Load average is about 18, on a quad core hyperthreaded 3.33 GHz Xeon.)


---

Comment by drkirkby created at 2011-03-28 00:40:34

Oops, I repeated the 5 seconds test data twice. So there are 10 builds now, averaging 21-22 minutes.


---

Comment by drkirkby created at 2011-03-28 10:07:08

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2011-03-28 10:07:08

OK, I'm giving this positive review now, after the following were all successful.

 * 266 tests with a maximum delay before invoking the compilers of 200 ms. *No doctests were performed*, but all builds were OK.
 * 55 tests with a maximum delay before invoking the compilers of 500 ms. *No doctests were performed*, but all builds were OK.
 * 35 tests with a maximum delay before invoking the compilers of 5 seconds. *No doctests were performed*, but all builds were OK.
 * 21 tests with a maximum delay before invoking the compilers of 5 seconds. *This time the doctest `sage/sage/libs/singular/` was run after each build.*  
 

On my machine, the doctests are taking between 17  and 47 seconds (depening on machine load), which is a lot less than the time to build Singular (5 minutes or more). So with hindsight it would have been worth running the tests on each build. But I've run the doctests on 21 builds, and with a total 377 successful builds, I'm reasonably confident this is building in parallel OK. 

Of course Sod's Law says someone will get a failure, but I can't fault it myself. 

Note, the mean delays in invoking the compiler are half the maximum. The source of random numbers for determining the delays is `/dev/urandom`


---

Comment by jdemeyer created at 2011-04-11 19:15:54

Resolution: fixed
