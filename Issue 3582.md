# Issue 3582: clisp 2.46 cannot deal with parllel make

Issue created by migration from https://trac.sagemath.org/ticket/3582

Original creator: mabshoff

Original creation time: 2008-07-07 12:40:28

Assignee: mabshoff

CC:  was

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


---

Comment by mabshoff created at 2008-07-07 12:40:42

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-07 22:24:20

The spkg at

http://sage.math.washington.edu/home/mabshoff/clisp-2.46.p0.spkg

sets MAKE to make and exports it. No other changes were made. Builds on sage.math with MAKE equal to "make -j4"

Cheers,

Michael


---

Comment by was created at 2008-07-07 22:38:59

I'm giving this a positive review.


---

Comment by was created at 2008-07-07 22:39:34

Resolution: fixed


---

Comment by mabshoff created at 2008-07-07 23:01:20

Merged in Sage 3.0.4.rc0
