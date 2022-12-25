# Issue 7066: sympow ignores CC and uses gcc even when CC is set to Sun's compiler

archive/issues_007066.json:
```json
{
    "body": "Assignee: tbd\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used (#7021) \n\nDespite CC being set to Sun's compiler, sympow ignores this. \n\n```\nsympow-1.018.1.p6/src/Configure\nsympow-1.018.1.p6/.hgignore\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nRM = rm\nGREP = grep\nGP = gp\nSED = sed\nSH = sh\nUNAME = uname\nusing gcc\nCC = gcc\nYou do not appear to have an x86 based system --- not using fpu.c\nCP = cp\nMKDIR = mkdir\nTOUCH = touch\nTAR = tar\nMakefile has been re-made. Use make if you wish to build SYMPOW\n\n**ATTENTION** If you wish build SYMPOW, please ensure beforehand\nthat the various licenses of your C compiler, linker, assembler, etc.\nallow you to create a derived work based on SYMPOW and your C libraries\nmake[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/sympow-1.018.1.p6/src'\ngcc -O3   -c -o analrank.o analrank.c\ngcc -O3   -c -o analytic.o analytic.c\ngcc -O3   -c -o compute.o compute.c\ngcc -O3   -c -o compute2.o compute2.c\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7066\n\n",
    "created_at": "2009-09-29T12:42:13Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sympow ignores CC and uses gcc even when CC is set to Sun's compiler",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7066",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha2
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used (#7021) 

Despite CC being set to Sun's compiler, sympow ignores this. 

```
sympow-1.018.1.p6/src/Configure
sympow-1.018.1.p6/.hgignore
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
RM = rm
GREP = grep
GP = gp
SED = sed
SH = sh
UNAME = uname
using gcc
CC = gcc
You do not appear to have an x86 based system --- not using fpu.c
CP = cp
MKDIR = mkdir
TOUCH = touch
TAR = tar
Makefile has been re-made. Use make if you wish to build SYMPOW

**ATTENTION** If you wish build SYMPOW, please ensure beforehand
that the various licenses of your C compiler, linker, assembler, etc.
allow you to create a derived work based on SYMPOW and your C libraries
make[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/sympow-1.018.1.p6/src'
gcc -O3   -c -o analrank.o analrank.c
gcc -O3   -c -o analytic.o analytic.c
gcc -O3   -c -o compute.o compute.c
gcc -O3   -c -o compute2.o compute2.c
```

Issue created by migration from https://trac.sagemath.org/ticket/7066





---

archive/issue_comments_058333.json:
```json
{
    "body": "Changing component from algebra to solaris.",
    "created_at": "2009-11-09T14:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7066#issuecomment-58333",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from algebra to solaris.



---

archive/issue_comments_058334.json:
```json
{
    "body": "It looks like Jeroen took care of this in the last sympow bump, #11920.",
    "created_at": "2012-02-10T06:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7066#issuecomment-58334",
    "user": "https://github.com/orlitzky"
}
```

It looks like Jeroen took care of this in the last sympow bump, #11920.



---

archive/issue_events_016675.json:
```json
{
    "actor": "https://github.com/orlitzky",
    "created_at": "2012-02-10T06:06:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7066",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7066#event-16675"
}
```



---

archive/issue_comments_058335.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-02-10T06:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7066#issuecomment-58335",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058336.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-18T01:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7066#issuecomment-58336",
    "user": "https://github.com/ohanar"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058337.json:
```json
{
    "body": "Changing keywords from \"\" to \"rd2\".",
    "created_at": "2012-03-18T01:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7066#issuecomment-58337",
    "user": "https://github.com/ohanar"
}
```

Changing keywords from "" to "rd2".



---

archive/issue_comments_058338.json:
```json
{
    "body": "yup, that appears to be the case",
    "created_at": "2012-03-18T01:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7066#issuecomment-58338",
    "user": "https://github.com/ohanar"
}
```

yup, that appears to be the case



---

archive/issue_events_016676.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-03-21T11:36:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7066",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7066#event-16676"
}
```



---

archive/issue_comments_058339.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-03-21T11:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7066#issuecomment-58339",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
