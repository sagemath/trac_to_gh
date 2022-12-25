# Issue 6528: PolyBoRi ignores CXX and passes Sun flags to GNU C compiler.

archive/issues_006528.json:
```json
{
    "body": "Assignee: tbd\n\nI noticed a couple of issues with polybori-0.5rc.p8 on Solaris.\n\nNote how on the first line, polybori uses the GNU C compiler gcc to \ncompile a C file, but passes an unreconised option '-KPIC'. (That option would be acceptable to the Sun compiler).\n\nThen on the very next line, it calls the Sun C++ compiler 'CC' to \ncompile a .cc file! It sure gets in a mess!\n\n\n```\n\ngcc -o Cudd/epd/so_epd.o -c -std=c99 -O3 -Wno-long-long -Wreturn-type -g \n-fPIC -KPIC -DNDEBUG -DPACKED -DHAVE_M4RI -DHAVE_IEEE_754 -DBSD \n-I/rootpool2/local/kirkby/sage-4.1.rc1/spkg/build/polybori-0.5rc.p8/src/boost_1_34_1.cropped \n-I/rootpool2/local/kirkby/sage-4.1.rc1/local/include/python2.6 \n-Ipolybori/include -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr \n-ICudd/st -ICudd/epd Cudd/epd/epd.c\ngcc: unrecognized option '-KPIC'\n/opt/SUNWspro/bin/CC -o polybori/src/so_BoolePolyRing.o -c -O3 \n-Wno-long-long -Wreturn-type -g -fPIC -ftemplate-depth-100 -g -fPIC \n-KPIC -O3 -Wno-long-long -Wreturn-type -g -fPIC -KPIC -DNDEBUG -DPACKED \n-DHAVE_M4RI -DHAVE_IEEE_754 -DBSD \n-I/rootpool2/local/kirkby/sage-4.1.rc1/spkg/build/polybori-0.5rc.p8/src/boost_1_34_1.cropped \n-I/rootpool2/local/kirkby/sage-4.1.rc1/local/include/python2.6 \n-Ipolybori/include -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr \n-ICudd/st -ICudd/epd polybori/src/BoolePolyRing.cc\n\n```\n\n\nWhen I type\n\n\n\n```\n$ ./sage -sh\n$ env\n\n```\n\n\nI see:\n\n\n\n```\nSAGE_ROOT=/rootpool2/local/kirkby/sage-4.1.rc1\nPYTHONHOME=/rootpool2/local/kirkby/sage-4.1.rc1/local\nSAGE_PACKAGES=/rootpool2/local/kirkby/sage-4.1.rc1/spkg\nCP=cp\nLN=ln\nCXX=g++\n```\n\n\n\nSo given CXX is defined as g++, \n\nIt has been pointed out to me that this ticket, with the title \"Some packages don't respect the CC environment variable\" \t\n\nhttp://sagetrac.org/sage_trac/ticket/2999\n\nnoticed similar issues with a number of packages ignoring CC and CXX and had patch for polybori, but it was never integrated. Integration is very simple. \n\nAnother issue with PolyBoRi is that it assumes the GNU linker - see my fix at \n\nhttp://sagetrac.org/sage_trac/ticket/6437\n\nBut there is a ticket related to updating PolyBoRi to the latest upstream version too. \n\nhttp://sagetrac.org/sage_trac/ticket/6177\n\nso I'll wait until I know what happening before applying patches against an old version of polybori which might be a waste of my time.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6528\n\n",
    "created_at": "2009-07-14T01:08:18Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "PolyBoRi ignores CXX and passes Sun flags to GNU C compiler.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6528",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/6528





---

archive/issue_comments_053124.json:
```json
{
    "body": "I understand it's best to start a new 'p9' release, so here it is. \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori-0.5rc.p9-Second-try/polybori-0.5rc.p9.spkg\ndirectory with information is\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori-0.5rc.p9-Second-try\n\nThis has been tested on both 't2' and my Sun Blade 2000. \n\ndave",
    "created_at": "2009-07-22T13:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6528#issuecomment-53124",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I understand it's best to start a new 'p9' release, so here it is. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori-0.5rc.p9-Second-try/polybori-0.5rc.p9.spkg
directory with information is
http://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori-0.5rc.p9-Second-try

This has been tested on both 't2' and my Sun Blade 2000. 

dave



---

archive/issue_comments_053125.json:
```json
{
    "body": "I have checked in all changes in your name. The updated SPKG is up at\n\nhttp://sage.math.washington.edu/home/mvngu/patch/polybori-0.5rc.p9.spkg",
    "created_at": "2009-07-23T23:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6528#issuecomment-53125",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I have checked in all changes in your name. The updated SPKG is up at

http://sage.math.washington.edu/home/mvngu/patch/polybori-0.5rc.p9.spkg



---

archive/issue_events_006764.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-07-24T00:29:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6528",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6528#event-6764"
}
```



---

archive/issue_comments_053126.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-24T00:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6528#issuecomment-53126",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053127.json:
```json
{
    "body": "The SPKG at\n\nhttp://sage.math.washington.edu/home/mvngu/patch/polybori-0.5rc.p9.spkg\n\nbuilds successfully on t2. (It also compiles OK on Linux.)",
    "created_at": "2009-07-24T00:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6528#issuecomment-53127",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The SPKG at

http://sage.math.washington.edu/home/mvngu/patch/polybori-0.5rc.p9.spkg

builds successfully on t2. (It also compiles OK on Linux.)
