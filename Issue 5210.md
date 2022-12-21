# Issue 5210: gmp-mpir-0.9.rc3: make check failure on various OSX boxen

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-08 20:17:37

Assignee: mabshoff


```
PASS: t-assign 
PASS: t-binary 
PASS: t-cast 
PASS: t-constr 
PASS: t-headers 
PASS: t-istream 
istream mpf_t operator>> wrong 
  point , 
  str   "1," 
  got   123 
  want  1 
  localeconv point "," 
/bin/sh: line 1: 13352 Abort trap              ${dir}$tst 
FAIL: t-locale 
PASS: t-misc 
PASS: t-ops 
PASS: t-ostream 
PASS: t-prec 
PASS: t-rand 
PASS: t-ternary 
PASS: t-unary 
============================================================= 
1 of 14 tests failed 
Please report to http://groups.google.co.uk/group/mpir-devel/ 
============================================================= 
make[6]: *** [check-TESTS] Error 1 
make[5]: *** [check-am] Error 2 
make[4]: *** [check-recursive] Error 1 
make[3]: *** [check-recursive] Error 1 
make[2]: *** [check] Error 2 
```



---

Comment by mabshoff created at 2009-02-09 11:17:55

The cause of the bug has been isolated in the discussion at

   http://groups.google.com/group/mpir-devel/t/aff995c6c3beb58d

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-11 02:41:38

The spkg at

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc0/gmp-mpir-0.9.rc4.spkg

fixes the problem. Tested on all of SkyNet, various OSX boxen where it blew up before and sage.math. Unlike the previous spkg the test suite was run in all cases unlike the previous one where by sheer coincidence I tested an spkg where the test suite wasn't run on all affected OSX boxen. Talk about a freak accident :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-11 02:41:44

Changing status from new to assigned.


---

Comment by ncalexan created at 2009-02-11 05:01:28

Success for me.


```
~/Devel/sage-3.2.3 $ uname -a
Darwin pv139196.reshsg.uci.edu 9.5.0 Darwin Kernel Version 9.5.0: Wed Sep  3 11:29:43 PDT 2008; root:xnu-1228.7.58~1/RELEASE_I386 i386 i386
```


Log at [http://sage.math.washington.edu/home/ncalexan/gmp-mpir-0.9.rc4.log](http://sage.math.washington.edu/home/ncalexan/gmp-mpir-0.9.rc4.log).


---

Comment by mabshoff created at 2009-02-11 05:09:48

Resolution: fixed


---

Comment by mabshoff created at 2009-02-11 05:09:48

Merged in Sage 3.3.rc0. Thanks Nick.

Cheers,

Michael
