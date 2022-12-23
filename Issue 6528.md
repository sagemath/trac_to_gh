# Issue 6528: PolyBoRi ignores CXX and passes Sun flags to GNU C compiler.

Issue created by migration from https://trac.sagemath.org/ticket/6528

Original creator: drkirkby

Original creation time: 2009-07-14 01:08:18

Assignee: tbd

I noticed a couple of issues with polybori-0.5rc.p8 on Solaris.

Note how on the first line, polybori uses the GNU C compiler gcc to 
compile a C file, but passes an unreconised option '-KPIC'. (That option would be acceptable to the Sun compiler).

Then on the very next line, it calls the Sun C++ compiler 'CC' to 
compile a .cc file! It sure gets in a mess!


```

gcc -o Cudd/epd/so_epd.o -c -std=c99 -O3 -Wno-long-long -Wreturn-type -g 
-fPIC -KPIC -DNDEBUG -DPACKED -DHAVE_M4RI -DHAVE_IEEE_754 -DBSD 
-I/rootpool2/local/kirkby/sage-4.1.rc1/spkg/build/polybori-0.5rc.p8/src/boost_1_34_1.cropped 
-I/rootpool2/local/kirkby/sage-4.1.rc1/local/include/python2.6 
-Ipolybori/include -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr 
-ICudd/st -ICudd/epd Cudd/epd/epd.c
gcc: unrecognized option '-KPIC'
/opt/SUNWspro/bin/CC -o polybori/src/so_BoolePolyRing.o -c -O3 
-Wno-long-long -Wreturn-type -g -fPIC -ftemplate-depth-100 -g -fPIC 
-KPIC -O3 -Wno-long-long -Wreturn-type -g -fPIC -KPIC -DNDEBUG -DPACKED 
-DHAVE_M4RI -DHAVE_IEEE_754 -DBSD 
-I/rootpool2/local/kirkby/sage-4.1.rc1/spkg/build/polybori-0.5rc.p8/src/boost_1_34_1.cropped 
-I/rootpool2/local/kirkby/sage-4.1.rc1/local/include/python2.6 
-Ipolybori/include -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr 
-ICudd/st -ICudd/epd polybori/src/BoolePolyRing.cc

```


When I type



```
$ ./sage -sh
$ env

```


I see:



```
SAGE_ROOT=/rootpool2/local/kirkby/sage-4.1.rc1
PYTHONHOME=/rootpool2/local/kirkby/sage-4.1.rc1/local
SAGE_PACKAGES=/rootpool2/local/kirkby/sage-4.1.rc1/spkg
CP=cp
LN=ln
CXX=g++
```



So given CXX is defined as g++, 

It has been pointed out to me that this ticket, with the title "Some packages don't respect the CC environment variable" 	

http://sagetrac.org/sage_trac/ticket/2999

noticed similar issues with a number of packages ignoring CC and CXX and had patch for polybori, but it was never integrated. Integration is very simple. 

Another issue with PolyBoRi is that it assumes the GNU linker - see my fix at 

http://sagetrac.org/sage_trac/ticket/6437

But there is a ticket related to updating PolyBoRi to the latest upstream version too. 

http://sagetrac.org/sage_trac/ticket/6177

so I'll wait until I know what happening before applying patches against an old version of polybori which might be a waste of my time.


---

Comment by drkirkby created at 2009-07-22 13:52:43

I understand it's best to start a new 'p9' release, so here it is. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori-0.5rc.p9-Second-try/polybori-0.5rc.p9.spkg
directory with information is
http://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori-0.5rc.p9-Second-try

This has been tested on both 't2' and my Sun Blade 2000. 

dave


---

Comment by mvngu created at 2009-07-23 23:43:34

I have checked in all changes in your name. The updated SPKG is up at

http://sage.math.washington.edu/home/mvngu/patch/polybori-0.5rc.p9.spkg


---

Comment by mvngu created at 2009-07-24 00:29:45

Resolution: fixed


---

Comment by mvngu created at 2009-07-24 00:29:45

The SPKG at

http://sage.math.washington.edu/home/mvngu/patch/polybori-0.5rc.p9.spkg

builds successfully on t2. (It also compiles OK on Linux.)
