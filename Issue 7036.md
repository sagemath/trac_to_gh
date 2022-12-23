# Issue 7036: rubiks ignroes CC and uses gcc even if CC is Sun compiler

archive/issues_007036.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: GNUism gcc CC\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 \n\nCC was set to the Sun C compiler, CXX to the Sun C++ compiler and SAGE_FORTRAN to the Sun Fortran 95 compiler. \n\nrubiks-20070912.p9 totally ignores the setting of CC, and uses gcc which it finds in the path. This is unfortunately not an uncommon problem. \n\n\n```\nrubiks-20070912.p9/src/dik/globals.h\nrubiks-20070912.p9/src/dik/permcube.c\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nBuilding Rubiks cube solvers\nmake[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/rubiks-20070912.p9/src'\nfor dir in dietz/cu2 dietz/mcube dietz/solver dik reid; do \\\n        (cd ${dir} && make all)\\\ndone\nmake[3]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/rubiks-20070912.p9/src/dietz/cu2'\ng++ -O2 -c cu2.cpp\ng++ -O2 -c main.cpp\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7036\n\n",
    "created_at": "2009-09-27T15:33:55Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "rubiks ignroes CC and uses gcc even if CC is Sun compiler",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7036",
    "user": "drkirkby"
}
```
Assignee: tbd

Keywords: GNUism gcc CC

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha2
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 

CC was set to the Sun C compiler, CXX to the Sun C++ compiler and SAGE_FORTRAN to the Sun Fortran 95 compiler. 

rubiks-20070912.p9 totally ignores the setting of CC, and uses gcc which it finds in the path. This is unfortunately not an uncommon problem. 


```
rubiks-20070912.p9/src/dik/globals.h
rubiks-20070912.p9/src/dik/permcube.c
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
Building Rubiks cube solvers
make[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/rubiks-20070912.p9/src'
for dir in dietz/cu2 dietz/mcube dietz/solver dik reid; do \
        (cd ${dir} && make all)\
done
make[3]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/rubiks-20070912.p9/src/dietz/cu2'
g++ -O2 -c cu2.cpp
g++ -O2 -c main.cpp

```


Issue created by migration from https://trac.sagemath.org/ticket/7036





---

archive/issue_comments_058257.json:
```json
{
    "body": "Having looked at this package, I can see it was broken in numerous ways. \n\n* g++ was hard coded\n* An option was passed to the assembler in an attempt to suppress warnings, though this would only work with the GNU assembler\n* I don't think it could build 64-bit executables - there was nothing about SAGE64 in the spkg-install\n* CFLAGS were used when CXXFLAGS should have been used. \n\nBasically, the makefiles were a total mess. \n\nThe revised .spkg has been tested on\n* 32-bit Solaris SPARC with gcc\n* 64-bit Solaris SPARC with gcc\n* 32-bit Solaris SPARC with Sun compiler\n* 64-bit Solaris SPARC with Sun compiler\n* Sage.math - I think the default is 64-bit there. \n* 32-bit on bsd.math with gcc\n* 64-bit on bsd.math with gcc\n\nThere are now no hard-coded options, or compilers. Everything can be set from spkg-install, and is set sensibly. I've tested this with both 32 and 64-bit builds on Solaris, using both the GNU and Sun compilers. Also tested on sage.math. Also tested on bsd.math in both \n\nThe new spkg can be found here. \nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/rubiks-20070912.p10/rubiks-20070912.p10.spkg\n\nThe spkg-install is here\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/rubiks-20070912.p10/spkg-install\n\nThe revised Makefiles, patches etc are in this directory:\n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/rubiks-20070912.p10\n\nBe warned, the patches are bigger than the makefiles - the chances are so many.",
    "created_at": "2009-09-29T02:14:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7036#issuecomment-58257",
    "user": "drkirkby"
}
```

Having looked at this package, I can see it was broken in numerous ways. 

* g++ was hard coded
* An option was passed to the assembler in an attempt to suppress warnings, though this would only work with the GNU assembler
* I don't think it could build 64-bit executables - there was nothing about SAGE64 in the spkg-install
* CFLAGS were used when CXXFLAGS should have been used. 

Basically, the makefiles were a total mess. 

The revised .spkg has been tested on
* 32-bit Solaris SPARC with gcc
* 64-bit Solaris SPARC with gcc
* 32-bit Solaris SPARC with Sun compiler
* 64-bit Solaris SPARC with Sun compiler
* Sage.math - I think the default is 64-bit there. 
* 32-bit on bsd.math with gcc
* 64-bit on bsd.math with gcc

There are now no hard-coded options, or compilers. Everything can be set from spkg-install, and is set sensibly. I've tested this with both 32 and 64-bit builds on Solaris, using both the GNU and Sun compilers. Also tested on sage.math. Also tested on bsd.math in both 

The new spkg can be found here. 
http://sage.math.washington.edu/home/kirkby/Solaris-fixes/rubiks-20070912.p10/rubiks-20070912.p10.spkg

The spkg-install is here
http://sage.math.washington.edu/home/kirkby/Solaris-fixes/rubiks-20070912.p10/spkg-install

The revised Makefiles, patches etc are in this directory:

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/rubiks-20070912.p10

Be warned, the patches are bigger than the makefiles - the chances are so many.



---

archive/issue_comments_058258.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-05T02:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7036#issuecomment-58258",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_058259.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-05T02:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7036#issuecomment-58259",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058260.json:
```json
{
    "body": "Since you gave this a positive review, I've changed the title from '[with spkg; needs review] ' to '[with spkg; positive review]' \n\nNow this new radio button has been added to trac that allows one to specify a positive review, should one still add '[with spkg; needs review]' to the title, or the 'needs review' bit ignored? \n\nDave",
    "created_at": "2009-11-09T06:45:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7036#issuecomment-58260",
    "user": "drkirkby"
}
```

Since you gave this a positive review, I've changed the title from '[with spkg; needs review] ' to '[with spkg; positive review]' 

Now this new radio button has been added to trac that allows one to specify a positive review, should one still add '[with spkg; needs review]' to the title, or the 'needs review' bit ignored? 

Dave



---

archive/issue_comments_058261.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T06:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7036#issuecomment-58261",
    "user": "mhansen"
}
```

Resolution: fixed
