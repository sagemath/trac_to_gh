# Issue 6710: Numerous build issues on Solaris.

archive/issues_006710.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  david.kirkby@onetel.net @dimpase\n\nSage can build on both SPARC and x86, but some issues remain. Some of these problems can affect other operating systems too. I added this as a trac ticket, mainly so I can keep a record of what what bugs remain and what get fixed. \n\nI've split the issues into two sections. Issues 1-7 will prevent Sage building on Solaris in some or all cases. Workarounds, hacks and updated .spkg files will get around these but have negative side effects. \n\nIssues 8 onwards are less serious and do not prevent Sage building on Solaris in any case at all. \n\n**CRITICAL BUGS - Stop Sage building in some/all cases**\n\n1) The version of ECL in Sage will not build on Solaris SPARC. \n#6564\n\nThe latest ECL 9.8.1 fixes this. \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.1/\n\n2) An update to Maxima is needed to allow the new ECL to be installed, as the old Maxima in Sage has a bug which the new ECL detects and rejects. \n\n#6699 \n\nA new maxima SPKG can be found here. \nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.0\n\n3) There's an 'Error building 'modified sage library code' when including paripriv.h'\n\n#6579\n\nA hack of manually commenting out lines 258, 259 and 428 of \n\n$SAGE_HOME/local/include/pari/paripriv.h\n\nwill bypass  this. \n\n5) MPIR determines linker is GNU when it's Sun on some versions of Solaris x86.\n\n#6539\n\n6) MPIR tries to link in gmp on some versions of Solaris x86. \n\n#6706\n\n7) Sage will not build if the Sun compiler suite is installed. Some code finds the Sun C++ compiler in /opt/SUNWspro/bin/CC and uses that. Temporarily renaming /opt/SUNWspro to something else will fix this, but needs root access. #6595\n\n**LESS SERIOUS - which don't prevent Sage building on Solaris. **\n\n8) There is a bug in Solaris 10 on sun4v machines which means memset() is broken. A patch to MPFR has been included, and will allow it to MPFR to build, but it will impact performance. \n\nI'm told by Sun this will be addressed in the next release of Solaris \n10, though I should personally have a patch earlier. \n\n9) ATLAS will not tune properly on a Sun T5240 ('t2') but will on my own sun4u machines. \n\n#6705\n\n10) ATLAS dumps core on a Sun T5240 sun4v machine ('t2'). This does not appear to be a gcc 4.4.0 specific bug, as it works fine on my home machine. I added a patch to ATLAS \n\n#6276\n\nto fix this, but the fix will impact performance, as some tuning data will be computed incorrect, as a 'reasonable' rather than 'optimal' value for one of the tuning parameters is returns. \n\nI added a second patch, which means the fix can be bypassed on machines where it is not an issue.\n\n6558\n\n11) There's a potential issue in polybori - 0.5rc.p8 and/or 0.5rc.p9 which will cause problems if the Sun compilers were used. \n\n6582\n\n(There are other issues too with Sun compilers, but this is one I know of). \n\n12) No support for Sun compilers\n#6703\n\nAny attempt to use the Sun compiler suite will fail miserably at a very early stage, due to the configure script in prereq-0.3.tar \n\nIt would be sensible to allow the use of the Sun compilers, but issue a warning that it is very likely to fail. Once we know where the problems lie, we can report these upstream. \n\nAfter I hacked the configure script to allow the Sun compilers to be used, I noticed the GNU ones were being used by some code, despite CC, CXX and SAGE_FORTRAN all being set to the Sun compilers. This indicates several packages are ignoring settings of CC, CXX and SAGE_FORTRAN. \n\nI intend creating a new configure.ac which address this and many other issues with the configure script. \n\n13) No support for 64-bit on Solaris\n#6702\n\n14) Several doctests fail. \n#6709\n\n15) lcalc-20080205.p2 tries to suppress warnings from the assembler, but fails to do this on Solaris if gcc uses the Sun assembler, as the option passed to the assembler is invalid on with Sun's assembler. (Of course, its not sensible to bypass warnings). \n\n#6609\n\n16) ATLAS has no tuning parameters for sun4v machines\n\n#6705\n\n17) Sage will try to build on compilers known to be too old.\n\n#6707\n\nThis is related to #6701 and it not Solaris specific, though some things in 6701 are.\n\n18) Top level README.txt is wrong regarding Solaris (in fact, also all operating systems). More serious errors regarding Solaris in README.txt\n\n#6055\n\nIssue created by migration from https://trac.sagemath.org/ticket/6710\n\n",
    "created_at": "2009-08-09T10:44:26Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Numerous build issues on Solaris.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6710",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  david.kirkby@onetel.net @dimpase

Sage can build on both SPARC and x86, but some issues remain. Some of these problems can affect other operating systems too. I added this as a trac ticket, mainly so I can keep a record of what what bugs remain and what get fixed. 

I've split the issues into two sections. Issues 1-7 will prevent Sage building on Solaris in some or all cases. Workarounds, hacks and updated .spkg files will get around these but have negative side effects. 

Issues 8 onwards are less serious and do not prevent Sage building on Solaris in any case at all. 

**CRITICAL BUGS - Stop Sage building in some/all cases**

1) The version of ECL in Sage will not build on Solaris SPARC. 
#6564

The latest ECL 9.8.1 fixes this. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.1/

2) An update to Maxima is needed to allow the new ECL to be installed, as the old Maxima in Sage has a bug which the new ECL detects and rejects. 

#6699 

A new maxima SPKG can be found here. 
http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.0

3) There's an 'Error building 'modified sage library code' when including paripriv.h'

#6579

A hack of manually commenting out lines 258, 259 and 428 of 

$SAGE_HOME/local/include/pari/paripriv.h

will bypass  this. 

5) MPIR determines linker is GNU when it's Sun on some versions of Solaris x86.

#6539

6) MPIR tries to link in gmp on some versions of Solaris x86. 

#6706

7) Sage will not build if the Sun compiler suite is installed. Some code finds the Sun C++ compiler in /opt/SUNWspro/bin/CC and uses that. Temporarily renaming /opt/SUNWspro to something else will fix this, but needs root access. #6595

**LESS SERIOUS - which don't prevent Sage building on Solaris. **

8) There is a bug in Solaris 10 on sun4v machines which means memset() is broken. A patch to MPFR has been included, and will allow it to MPFR to build, but it will impact performance. 

I'm told by Sun this will be addressed in the next release of Solaris 
10, though I should personally have a patch earlier. 

9) ATLAS will not tune properly on a Sun T5240 ('t2') but will on my own sun4u machines. 

#6705

10) ATLAS dumps core on a Sun T5240 sun4v machine ('t2'). This does not appear to be a gcc 4.4.0 specific bug, as it works fine on my home machine. I added a patch to ATLAS 

#6276

to fix this, but the fix will impact performance, as some tuning data will be computed incorrect, as a 'reasonable' rather than 'optimal' value for one of the tuning parameters is returns. 

I added a second patch, which means the fix can be bypassed on machines where it is not an issue.

6558

11) There's a potential issue in polybori - 0.5rc.p8 and/or 0.5rc.p9 which will cause problems if the Sun compilers were used. 

6582

(There are other issues too with Sun compilers, but this is one I know of). 

12) No support for Sun compilers
#6703

Any attempt to use the Sun compiler suite will fail miserably at a very early stage, due to the configure script in prereq-0.3.tar 

It would be sensible to allow the use of the Sun compilers, but issue a warning that it is very likely to fail. Once we know where the problems lie, we can report these upstream. 

After I hacked the configure script to allow the Sun compilers to be used, I noticed the GNU ones were being used by some code, despite CC, CXX and SAGE_FORTRAN all being set to the Sun compilers. This indicates several packages are ignoring settings of CC, CXX and SAGE_FORTRAN. 

I intend creating a new configure.ac which address this and many other issues with the configure script. 

13) No support for 64-bit on Solaris
#6702

14) Several doctests fail. 
#6709

15) lcalc-20080205.p2 tries to suppress warnings from the assembler, but fails to do this on Solaris if gcc uses the Sun assembler, as the option passed to the assembler is invalid on with Sun's assembler. (Of course, its not sensible to bypass warnings). 

#6609

16) ATLAS has no tuning parameters for sun4v machines

#6705

17) Sage will try to build on compilers known to be too old.

#6707

This is related to #6701 and it not Solaris specific, though some things in 6701 are.

18) Top level README.txt is wrong regarding Solaris (in fact, also all operating systems). More serious errors regarding Solaris in README.txt

#6055

Issue created by migration from https://trac.sagemath.org/ticket/6710





---

archive/issue_comments_054996.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2009-08-10T19:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6710#issuecomment-54996",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_054997.json:
```json
{
    "body": "Can you try the new Maxima with this?  There isn't an spkg available yet but hopefully will be soon. See [http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7](http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7)",
    "created_at": "2009-12-21T02:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6710#issuecomment-54997",
    "user": "https://github.com/kcrisman"
}
```

Can you try the new Maxima with this?  There isn't an spkg available yet but hopefully will be soon. See [http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7](http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7)



---

archive/issue_comments_054998.json:
```json
{
    "body": "How many of the open tickets mentioned in the description are still problems?",
    "created_at": "2010-09-01T10:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6710#issuecomment-54998",
    "user": "https://github.com/qed777"
}
```

How many of the open tickets mentioned in the description are still problems?



---

archive/issue_comments_054999.json:
```json
{
    "body": "Bump - a number of these have been closed, and perhaps some others are solved.  Since Solaris is now a supported platform at least some of the time, it would be helpful to have an update.",
    "created_at": "2011-08-19T13:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6710#issuecomment-54999",
    "user": "https://github.com/kcrisman"
}
```

Bump - a number of these have been closed, and perhaps some others are solved.  Since Solaris is now a supported platform at least some of the time, it would be helpful to have an update.



---

archive/issue_comments_055000.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6710#issuecomment-55000",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_055001.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6710#issuecomment-55001",
    "user": "https://github.com/mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_events_006945.json:
```json
{
    "actor": "@fchapoton",
    "created_at": "2020-07-14T16:30:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6710",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6710#event-6945"
}
```



---

archive/issue_comments_055002.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-14T16:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6710#issuecomment-55002",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
