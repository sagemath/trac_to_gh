# Issue 4868: optional polymake spkg quickly fails to build on sage.math

archive/issues_004868.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage: install_package('polymake-2.2.p4')\n...\n**********************************************************************\n* Unable to download cddlib-094b.p1\n* Please see http://www.sagemath.org//packages for a list of valid\n* packages or check the package name.\n**********************************************************************\nsage: Failed to download package cddlib-094b.p1 from http://www.sagemath.org/\ntar: /usr/local/sage/spkg/standard/cddlib-094b.p1.spkg: Cannot open: No such file or directory\n```\n\n\nThis is even after installing cddlib. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4868\n\n",
    "created_at": "2008-12-24T05:56:01Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "optional polymake spkg quickly fails to build on sage.math",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4868",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff


```
sage: install_package('polymake-2.2.p4')
...
**********************************************************************
* Unable to download cddlib-094b.p1
* Please see http://www.sagemath.org//packages for a list of valid
* packages or check the package name.
**********************************************************************
sage: Failed to download package cddlib-094b.p1 from http://www.sagemath.org/
tar: /usr/local/sage/spkg/standard/cddlib-094b.p1.spkg: Cannot open: No such file or directory
```


This is even after installing cddlib. 



Issue created by migration from https://trac.sagemath.org/ticket/4868





---

archive/issue_comments_036809.json:
```json
{
    "body": "I fixed a few problems in the spkg, so now it fails after only 30 minutes as follows:\n\n```\n                 from ../../../apps/polytope/src/cdd_interface.cc:19:\n../../../lib/gmp_wrapper/include/Integer.h:783: warning: overflow in implicit constant conversion\n../../../lib/gmp_wrapper/include/Integer.h:784: warning: overflow in implicit constant conversion\nld -r -o cdd_interface.o cdd_interface-tmp.o ../../external/cdd/libcddgmp.a\nld: ../../external/cdd/libcddgmp.a: No such file: No such file or directory\nmake[2]: *** [cdd_interface.o] Error 1\nmake[1]: *** [all] Error 2\nmake: *** [all] Error 2\necho \"\" | make\nError building polymake\n\nreal    0m29.741s\nuser    0m26.640s\nsys     0m3.020s\nsage: An error occurred while installing polymake-2.2.p5\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /usr/local/sage/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem, yourself *don't* just cd to\n/usr/local/sage/spkg/build/polymake-2.2.p5 and type 'make'.\nInstead type \"/usr/local/sage/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/usr/local/sage/spkg/build/polymake-2.2.p5\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\n```\n\n\nThe new spkg is here and should replace the original one. Also, I think this should be moved to experimental, in which case we could close this ticket:\n\nhttp://sage.math.washington.edu/home/was/patches/polymake-2.2.p5.spkg",
    "created_at": "2008-12-24T07:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4868#issuecomment-36809",
    "user": "https://github.com/williamstein"
}
```

I fixed a few problems in the spkg, so now it fails after only 30 minutes as follows:

```
                 from ../../../apps/polytope/src/cdd_interface.cc:19:
../../../lib/gmp_wrapper/include/Integer.h:783: warning: overflow in implicit constant conversion
../../../lib/gmp_wrapper/include/Integer.h:784: warning: overflow in implicit constant conversion
ld -r -o cdd_interface.o cdd_interface-tmp.o ../../external/cdd/libcddgmp.a
ld: ../../external/cdd/libcddgmp.a: No such file: No such file or directory
make[2]: *** [cdd_interface.o] Error 1
make[1]: *** [all] Error 2
make: *** [all] Error 2
echo "" | make
Error building polymake

real    0m29.741s
user    0m26.640s
sys     0m3.020s
sage: An error occurred while installing polymake-2.2.p5
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /usr/local/sage/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/usr/local/sage/spkg/build/polymake-2.2.p5 and type 'make'.
Instead type "/usr/local/sage/sage -sh"
in order to set all environment variables correctly, then cd to
/usr/local/sage/spkg/build/polymake-2.2.p5
(When you are done debugging, you can type "exit" to leave the
subshell.)
```


The new spkg is here and should replace the original one. Also, I think this should be moved to experimental, in which case we could close this ticket:

http://sage.math.washington.edu/home/was/patches/polymake-2.2.p5.spkg



---

archive/issue_comments_036810.json:
```json
{
    "body": "I get the same with mpi4py:\n\n```\nsage: install_package('mpi4py-0.3.1')\nPossible names of non-installed packages starting with 'mpi4py-0.3.1':\n  mpi4py-0.3.1\n  mpi4py-0.3.1\n```\n",
    "created_at": "2008-12-24T07:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4868#issuecomment-36810",
    "user": "https://github.com/williamstein"
}
```

I get the same with mpi4py:

```
sage: install_package('mpi4py-0.3.1')
Possible names of non-installed packages starting with 'mpi4py-0.3.1':
  mpi4py-0.3.1
  mpi4py-0.3.1
```




---

archive/issue_comments_036811.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-12-24T11:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4868#issuecomment-36811",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_events_005111.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-24T11:44:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4868",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4868#event-5111"
}
```



---

archive/issue_comments_036812.json:
```json
{
    "body": "This is a dupe of #3640.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-24T11:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4868#issuecomment-36812",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a dupe of #3640.

Cheers,

Michael
