# Issue 1486: singular-3-0-4-1-20071202 fails compilation on Slackware 12.0

archive/issues_001486.json:
```json
{
    "body": "Assignee: @malb\n\nReported by John A. Murdie:\n\n```\nmake[4]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg/build/\nsingular-3-0-4-1-20071202/src/kernel'\nmake install in Singular\nmake[4]: Entering directory `/local/d0p6/john/sage-2.8.15/spkg/build/\nsingular-3-0-4-1-20071202/src/Singular'\n...\ng++ -fPIC -O3 -g -pipe -fno-implicit-templates -I. -I../kernel -I/\nlocal/d0p6/john/sage-2.8.15/local/include  -DNDEBUG -DOM_NDEBUG -\nDix86_Linux -DHAVE_CONFIG_H -c walk_ip.cc\ng++ -fPIC -O3 -g -pipe -fno-implicit-templates -I. -I../kernel -I/\nlocal/d0p6/john/sage-2.8.15/local/include  -DNDEBUG -DOM_NDEBUG -\nDix86_Linux -DHAVE_CONFIG_H -c cntrlc.cc\n/usr/include/asm/sigcontext.h:20: error: redefinition of 'struct\n_fpreg'\n/usr/include/bits/sigcontext.h:29: error: previous definition of\n'struct _fpreg'\n/usr/include/asm/sigcontext.h:25: error: redefinition of 'struct\n_fpxreg'\n/usr/include/bits/sigcontext.h:35: error: previous definition of\n'struct _fpxreg'\n/usr/include/asm/sigcontext.h:31: error: redefinition of 'struct\n_xmmreg'\n/usr/include/bits/sigcontext.h:42: error: previous definition of\n'struct _xmmreg'\n/usr/include/asm/sigcontext.h:35: error: redefinition of 'struct\n_fpstate'\n/usr/include/bits/sigcontext.h:51: error: previous definition of\n'struct _fpstate'\n/usr/include/asm/sigcontext.h:59: error: redefinition of 'struct\nsigcontext'\n/usr/include/bits/sigcontext.h:82: error: previous definition of\n'struct sigcontext'\nmake[4]: *** [cntrlc.o] Error 1\nmake[4]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg/build/\nsingular-3-0-4-1-20071202/src/Singular'\nmake[3]: *** [install] Error 1\nmake[3]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg/build/\nsingular-3-0-4-1-20071202/src'\nmake[2]: *** [/local/d0p6/john/sage-2.8.15/local/bin/Singular-3-0-4]\nError 2\nmake[2]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg/build/\nsingular-3-0-4-1-20071202/src'\nUnable to build Singular.\n...\nsage: An error occurred while installing singular-3-0-4-1-20071202\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /local/d0p6/john/sage-2.8.15/install.log.  Describe your computer,\noperating system, etc.\nIf you want to try to fix the problem, yourself *don't* just cd to\n/local/d0p6/john/sage-2.8.15/spkg/build/singular-3-0-4-1-20071202 and\ntype 'make'.\nInstead type \"/local/d0p6/john/sage-2.8.15/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/local/d0p6/john/sage-2.8.15/spkg/build/singular-3-0-4-1-20071202\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\nmake[1]: *** [installed/singular-3-0-4-1-20071202] Error 1\nmake[1]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg' \n```\n\n\nCheers,\n\nMichal\n\nIssue created by migration from https://trac.sagemath.org/ticket/1486\n\n",
    "created_at": "2007-12-13T17:18:12Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "singular-3-0-4-1-20071202 fails compilation on Slackware 12.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1486",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @malb

Reported by John A. Murdie:

```
make[4]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg/build/
singular-3-0-4-1-20071202/src/kernel'
make install in Singular
make[4]: Entering directory `/local/d0p6/john/sage-2.8.15/spkg/build/
singular-3-0-4-1-20071202/src/Singular'
...
g++ -fPIC -O3 -g -pipe -fno-implicit-templates -I. -I../kernel -I/
local/d0p6/john/sage-2.8.15/local/include  -DNDEBUG -DOM_NDEBUG -
Dix86_Linux -DHAVE_CONFIG_H -c walk_ip.cc
g++ -fPIC -O3 -g -pipe -fno-implicit-templates -I. -I../kernel -I/
local/d0p6/john/sage-2.8.15/local/include  -DNDEBUG -DOM_NDEBUG -
Dix86_Linux -DHAVE_CONFIG_H -c cntrlc.cc
/usr/include/asm/sigcontext.h:20: error: redefinition of 'struct
_fpreg'
/usr/include/bits/sigcontext.h:29: error: previous definition of
'struct _fpreg'
/usr/include/asm/sigcontext.h:25: error: redefinition of 'struct
_fpxreg'
/usr/include/bits/sigcontext.h:35: error: previous definition of
'struct _fpxreg'
/usr/include/asm/sigcontext.h:31: error: redefinition of 'struct
_xmmreg'
/usr/include/bits/sigcontext.h:42: error: previous definition of
'struct _xmmreg'
/usr/include/asm/sigcontext.h:35: error: redefinition of 'struct
_fpstate'
/usr/include/bits/sigcontext.h:51: error: previous definition of
'struct _fpstate'
/usr/include/asm/sigcontext.h:59: error: redefinition of 'struct
sigcontext'
/usr/include/bits/sigcontext.h:82: error: previous definition of
'struct sigcontext'
make[4]: *** [cntrlc.o] Error 1
make[4]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg/build/
singular-3-0-4-1-20071202/src/Singular'
make[3]: *** [install] Error 1
make[3]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg/build/
singular-3-0-4-1-20071202/src'
make[2]: *** [/local/d0p6/john/sage-2.8.15/local/bin/Singular-3-0-4]
Error 2
make[2]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg/build/
singular-3-0-4-1-20071202/src'
Unable to build Singular.
...
sage: An error occurred while installing singular-3-0-4-1-20071202
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /local/d0p6/john/sage-2.8.15/install.log.  Describe your computer,
operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/local/d0p6/john/sage-2.8.15/spkg/build/singular-3-0-4-1-20071202 and
type 'make'.
Instead type "/local/d0p6/john/sage-2.8.15/sage -sh"
in order to set all environment variables correctly, then cd to
/local/d0p6/john/sage-2.8.15/spkg/build/singular-3-0-4-1-20071202
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/singular-3-0-4-1-20071202] Error 1
make[1]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg' 
```


Cheers,

Michal

Issue created by migration from https://trac.sagemath.org/ticket/1486





---

archive/issue_comments_009549.json:
```json
{
    "body": "Hans Sch\u00f6neman from the Singular team suggest a fix that worked. It is part of \n\nhttp://sage.math.washington.edu/home/mabshoff/singular-3-0-4-1-20071209.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-12-14T23:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1486#issuecomment-9549",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hans Schöneman from the Singular team suggest a fix that worked. It is part of 

http://sage.math.washington.edu/home/mabshoff/singular-3-0-4-1-20071209.p0.spkg

Cheers,

Michael



---

archive/issue_comments_009550.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T01:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1486#issuecomment-9550",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009551.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T01:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1486#issuecomment-9551",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.
