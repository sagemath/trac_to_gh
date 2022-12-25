# Issue 7860: sage_fortran builds 32-bit exuctabes when SAGE64=yes

archive/issues_007860.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @williamstein @jaapspies\n\nI'm trying to make a 64-bit build of Sage on my Sun Ultra 27, but although I've sorted out many packages which do not honour SAGE64, the sage_fortran package is unique, and I don't have a clue how to fix it. \n\nI've also set FCFLAGS to -m64, but that is being ignored. \n\nI've marked this as critical, as it really will inhibit progress on Sage on Open Solaris if this bit insists on building 32-bit executables. Overall, it seems less hassle to build 64-bit on Open Solaris than 32-bit, due to the OpenSSL issues.\n\nDave \n\n\n```\nsage_fortran -fPIC  -c sgerqf.f -o sgerqf.o\nsage_fortran -fPIC  -c sgesc2.f -o sgesc2.o\nsage_fortran -fPIC  -c sgesdd.f -o sgesdd.o\nsage_fortran -fPIC  -c sgesv.f -o sgesv.o\nsage_fortran -fPIC  -c sgesvd.f -o sgesvd.o\n^Cmake: *** [all] Interrupt\n\ndrkirkby@hawk:~/sage-4.3.1.alpha1$ find . -name sgerfs.o\n./spkg/build/lapack-20071123.p0/src/SRC/sgerfs.o\ndrkirkby@hawk:~/sage-4.3.1.alpha1$ file ./spkg/build/lapack-20071123.p0/src/SRC/sgerfs.o\n./spkg/build/lapack-20071123.p0/src/SRC/sgerfs.o:\tELF 32-bit LSB relocatable 80386 Version 1\ndrkirkby@hawk:~/sage-4.3.1.alpha1$ echo $SAGE64\nyes\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7860\n\n",
    "created_at": "2010-01-06T22:25:37Z",
    "labels": [
        "component: porting",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage_fortran builds 32-bit exuctabes when SAGE64=yes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7860",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @williamstein @jaapspies

I'm trying to make a 64-bit build of Sage on my Sun Ultra 27, but although I've sorted out many packages which do not honour SAGE64, the sage_fortran package is unique, and I don't have a clue how to fix it. 

I've also set FCFLAGS to -m64, but that is being ignored. 

I've marked this as critical, as it really will inhibit progress on Sage on Open Solaris if this bit insists on building 32-bit executables. Overall, it seems less hassle to build 64-bit on Open Solaris than 32-bit, due to the OpenSSL issues.

Dave 


```
sage_fortran -fPIC  -c sgerqf.f -o sgerqf.o
sage_fortran -fPIC  -c sgesc2.f -o sgesc2.o
sage_fortran -fPIC  -c sgesdd.f -o sgesdd.o
sage_fortran -fPIC  -c sgesv.f -o sgesv.o
sage_fortran -fPIC  -c sgesvd.f -o sgesvd.o
^Cmake: *** [all] Interrupt

drkirkby@hawk:~/sage-4.3.1.alpha1$ find . -name sgerfs.o
./spkg/build/lapack-20071123.p0/src/SRC/sgerfs.o
drkirkby@hawk:~/sage-4.3.1.alpha1$ file ./spkg/build/lapack-20071123.p0/src/SRC/sgerfs.o
./spkg/build/lapack-20071123.p0/src/SRC/sgerfs.o:	ELF 32-bit LSB relocatable 80386 Version 1
drkirkby@hawk:~/sage-4.3.1.alpha1$ echo $SAGE64
yes
```


Issue created by migration from https://trac.sagemath.org/ticket/7860





---

archive/issue_comments_068021.json:
```json
{
    "body": "Not so strange if you have:\n\n\n\n```/bin/sh\n\n/usr/bin/gfortran -fPIC $@\n\n```\n\n\nthis is my sage_fortran\n\nJaap",
    "created_at": "2010-01-07T13:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7860#issuecomment-68021",
    "user": "https://github.com/jaapspies"
}
```

Not so strange if you have:



```/bin/sh

/usr/bin/gfortran -fPIC $@

```


this is my sage_fortran

Jaap



---

archive/issue_comments_068022.json:
```json
{
    "body": "At the very least you would have to add -m64 to that, but that does not solve the problems - still things are build 32-bit, so screw up.",
    "created_at": "2010-01-10T04:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7860#issuecomment-68022",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

At the very least you would have to add -m64 to that, but that does not solve the problems - still things are build 32-bit, so screw up.



---

archive/issue_comments_068023.json:
```json
{
    "body": "Is this still  a problem?",
    "created_at": "2012-04-30T10:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7860#issuecomment-68023",
    "user": "https://github.com/jdemeyer"
}
```

Is this still  a problem?



---

archive/issue_comments_068024.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-04-12T12:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7860#issuecomment-68024",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068025.json:
```json
{
    "body": "Close as obsolete (`sage_fortran` is no longer used).",
    "created_at": "2014-04-12T12:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7860#issuecomment-68025",
    "user": "https://github.com/jdemeyer"
}
```

Close as obsolete (`sage_fortran` is no longer used).



---

archive/issue_comments_068026.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-04-12T12:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7860#issuecomment-68026",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008075.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-04-13T14:52:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7860",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7860#event-8075"
}
```



---

archive/issue_comments_068027.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-04-13T14:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7860#issuecomment-68027",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix
