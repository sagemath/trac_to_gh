# Issue 3582: clisp 2.46 cannot deal with parllel make

archive/issues_003582.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @williamstein\n\nSeting MAKE to \"make -j4\" blows up with\n\n```\ntest -d boot || (mkdir boot && cd boot && for f in lisp.a libnoreadline.a gllib/uniwidth/width.o gllib/uniname/uniname.o gllib/localcharset.o   modules.h modules.o lisp.run lispinit.mem; do ln -s ../$f .; done && (grep -v '^FILES=' ../makevars; fl=''; for f in lisp.a libnoreadline.a gllib/uniwidth/width.o gllib/uniname/uniname.o gllib/localcharset.o  ; do fl=$fl' '`basename $f`; done; echo 'FILES='\"'\"$fl\"'\") > makevars) || (rm -rf boot ; exit 1)\nrm -rf base\nCLISP_LINKKIT=. MAKE=make -j4 ./clisp-link add-module-sets boot base i18n syscalls regexp || (rm -rf base ; exit 1)\n/bin/sh: -j4: command not found\nmake[2]: *** [base] Error 1\nmake[2]: Leaving directory `/scratch/mabshoff/release-cycle/sage-3.0.4.rc0/spkg/build/clisp-2.46/src/src'\nError building clisp\n\nreal    4m22.614s\nuser    3m33.769s\nsys     0m54.775s\n```\n\nThe fix is obvious :)\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3582\n\n",
    "created_at": "2008-07-07T12:40:28Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "clisp 2.46 cannot deal with parllel make",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3582",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  @williamstein

Seting MAKE to "make -j4" blows up with

```
test -d boot || (mkdir boot && cd boot && for f in lisp.a libnoreadline.a gllib/uniwidth/width.o gllib/uniname/uniname.o gllib/localcharset.o   modules.h modules.o lisp.run lispinit.mem; do ln -s ../$f .; done && (grep -v '^FILES=' ../makevars; fl=''; for f in lisp.a libnoreadline.a gllib/uniwidth/width.o gllib/uniname/uniname.o gllib/localcharset.o  ; do fl=$fl' '`basename $f`; done; echo 'FILES='"'"$fl"'") > makevars) || (rm -rf boot ; exit 1)
rm -rf base
CLISP_LINKKIT=. MAKE=make -j4 ./clisp-link add-module-sets boot base i18n syscalls regexp || (rm -rf base ; exit 1)
/bin/sh: -j4: command not found
make[2]: *** [base] Error 1
make[2]: Leaving directory `/scratch/mabshoff/release-cycle/sage-3.0.4.rc0/spkg/build/clisp-2.46/src/src'
Error building clisp

real    4m22.614s
user    3m33.769s
sys     0m54.775s
```

The fix is obvious :)

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3582





---

archive/issue_comments_025292.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-07T12:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3582#issuecomment-25292",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025293.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/clisp-2.46.p0.spkg\n\nsets MAKE to make and exports it. No other changes were made. Builds on sage.math with MAKE equal to \"make -j4\"\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T22:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3582#issuecomment-25293",
    "user": "mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/clisp-2.46.p0.spkg

sets MAKE to make and exports it. No other changes were made. Builds on sage.math with MAKE equal to "make -j4"

Cheers,

Michael



---

archive/issue_comments_025294.json:
```json
{
    "body": "I'm giving this a positive review.",
    "created_at": "2008-07-07T22:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3582#issuecomment-25294",
    "user": "@williamstein"
}
```

I'm giving this a positive review.



---

archive/issue_comments_025295.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T22:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3582#issuecomment-25295",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_025296.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc0",
    "created_at": "2008-07-07T23:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3582#issuecomment-25296",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.rc0
