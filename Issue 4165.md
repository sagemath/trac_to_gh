# Issue 4165: Doctest for lisp.py blows chunks on (some) Mac OS X systems

archive/issues_004165.json:
```json
{
    "body": "Assignee: mabshoff\n\nI have seen this on two Mac OS X systems, with 3.1.2 (but not 3.1.1):\n- Core Duo (10.5.5)\n- Dual Quad Xeon (10.5.4)\n\nThis is an \"Expected/Got\" problem.  The output from the test is \n\n\n```\nsage -t  devel/sage/sage/interfaces/lisp.py \n**************************************************\nFile \"/SandBox/Justin/sb/sage-3.1.2/tmp/lisp.py\", line 290:\n     sage: lisp.version()\nExpected:\n     GNU CLISP ... (...) (built ...) (memory ...)\n     ...\nGot:\n     GNU CLISP 2.46 (2008-07-02) (built on Hasse-2.local [10.0.1.200])\n     Software: GNU C 4.0.1 (Apple Inc. build 5465)\n     gcc -O0 -g -I/SandBox/Justin/sb/sage-3.1.2/local/include/ -L/\nSandBox/Justin/sb/sage-3.1.2/local/lib/ -W -Wswitch -Wcomment -\nWpointer-arith -Wimplicit -Wreturn-type -Wmissing-declarations -Wno-\nsign-compare -O0 -fexpensive-optimizations -falign-functions=4 -\nDUNIX_BINARY_DISTRIB -DUNICODE -DNO_SIGSEGV -I. -x none -lintl -Wl,-\nframework -Wl,CoreFoundation -lreadline -lncurses  -liconv\n     SAFETY=0 HEAPCODES STANDARD_HEAPCODES SPVW_BLOCKS SPVW_MIXED  \nTRIVIALMAP_MEMORY\n     libiconv 1.11\n     libreadline 5.2\n     Features:\n     (REGEXP SYSCALLS I18N LOOP COMPILER CLOS MOP CLISP ANSI-CL COMMON-\nLISP LISP=CL\n      INTERPRETER SOCKETS GENERIC-STREAMS LOGICAL-PATHNAMES SCREEN  \nGETTEXT UNICODE\n      BASE-CHAR=CHARACTER UNIX MACOS)\n     C Modules: (clisp i18n syscalls regexp)\n     Installation directory: /SandBox/Justin/sb/sage-3.1.2/local/lib/\nclisp-2.46/\n     User language: ENGLISH\n     Machine: I386 (I386) Hasse-2.local [127.0.0.1]\n     <BLANKLINE>\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4165\n\n",
    "created_at": "2008-09-22T02:03:51Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Doctest for lisp.py blows chunks on (some) Mac OS X systems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4165",
    "user": "justin"
}
```
Assignee: mabshoff

I have seen this on two Mac OS X systems, with 3.1.2 (but not 3.1.1):
- Core Duo (10.5.5)
- Dual Quad Xeon (10.5.4)

This is an "Expected/Got" problem.  The output from the test is 


```
sage -t  devel/sage/sage/interfaces/lisp.py 
**************************************************
File "/SandBox/Justin/sb/sage-3.1.2/tmp/lisp.py", line 290:
     sage: lisp.version()
Expected:
     GNU CLISP ... (...) (built ...) (memory ...)
     ...
Got:
     GNU CLISP 2.46 (2008-07-02) (built on Hasse-2.local [10.0.1.200])
     Software: GNU C 4.0.1 (Apple Inc. build 5465)
     gcc -O0 -g -I/SandBox/Justin/sb/sage-3.1.2/local/include/ -L/
SandBox/Justin/sb/sage-3.1.2/local/lib/ -W -Wswitch -Wcomment -
Wpointer-arith -Wimplicit -Wreturn-type -Wmissing-declarations -Wno-
sign-compare -O0 -fexpensive-optimizations -falign-functions=4 -
DUNIX_BINARY_DISTRIB -DUNICODE -DNO_SIGSEGV -I. -x none -lintl -Wl,-
framework -Wl,CoreFoundation -lreadline -lncurses  -liconv
     SAFETY=0 HEAPCODES STANDARD_HEAPCODES SPVW_BLOCKS SPVW_MIXED  
TRIVIALMAP_MEMORY
     libiconv 1.11
     libreadline 5.2
     Features:
     (REGEXP SYSCALLS I18N LOOP COMPILER CLOS MOP CLISP ANSI-CL COMMON-
LISP LISP=CL
      INTERPRETER SOCKETS GENERIC-STREAMS LOGICAL-PATHNAMES SCREEN  
GETTEXT UNICODE
      BASE-CHAR=CHARACTER UNIX MACOS)
     C Modules: (clisp i18n syscalls regexp)
     Installation directory: /SandBox/Justin/sb/sage-3.1.2/local/lib/
clisp-2.46/
     User language: ENGLISH
     Machine: I386 (I386) Hasse-2.local [127.0.0.1]
     <BLANKLINE>
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4165





---

archive/issue_comments_030242.json:
```json
{
    "body": "Attachment\n\nJustin,\n\ncan you test this patch?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-22T03:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4165#issuecomment-30242",
    "user": "mabshoff"
}
```

Attachment

Justin,

can you test this patch?

Cheers,

Michael



---

archive/issue_comments_030243.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-22T03:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4165#issuecomment-30243",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030244.json:
```json
{
    "body": "I tried this out in 3.1.2; haven't leapt into the 3.1.3 morass yet.  Works like it oughtta!",
    "created_at": "2008-09-22T04:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4165#issuecomment-30244",
    "user": "justin"
}
```

I tried this out in 3.1.2; haven't leapt into the 3.1.3 morass yet.  Works like it oughtta!



---

archive/issue_comments_030245.json:
```json
{
    "body": "I assume his is a positive review then? lisp.py has not changed in 3.1.3.alpha0, so this ought to work.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-22T04:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4165#issuecomment-30245",
    "user": "mabshoff"
}
```

I assume his is a positive review then? lisp.py has not changed in 3.1.3.alpha0, so this ought to work.

Cheers,

Michael



---

archive/issue_comments_030246.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-23T00:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4165#issuecomment-30246",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030247.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha1",
    "created_at": "2008-09-23T00:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4165#issuecomment-30247",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha1
