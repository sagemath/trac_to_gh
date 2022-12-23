# Issue 7203: prereq-0.4 does not exit if CC is not gcc, but CXX is g++

Issue created by migration from https://trac.sagemath.org/ticket/7203

Original creator: drkirkby

Original creation time: 2009-10-13 23:02:54

Assignee: tbd

One of changes made in my recent update of prereq (#7021) from 0.3 to 0.4 was to exit when there was a mix of GNU and non-GNU compilers. 

Whilst this works if you have a GNU C compiler and a non-GNU C++ compiler, it does *not* work if you have a non-GNU C compiler and a GNU C++ compiler. This is a bug, and is entirely my fault. 

Basically the testing for mixing of compilers happens in configure.ac something like this:



```
if test x$GCC = xyes
then
    # Check if C++ compiler is g++. If not, there is a problem.
    # as mixing GNU and non-GNU compilers is likely to cause problems.
    if test x$GXX != xyes
    then
       AC_MSG_WARN([You are trying to use gcc but not g++])
       AC_MSG_ERROR([The mixing of GNU and non-GNU compilers is not permitted])
    fi
```


There is no corresponding test if x$GXX (the C++ compiler) is GNU. (Yes, GXX is correct, its not a mistake/)

I will also need to fix #7156, which is a minor portability issue with prereq. 



---

Comment by mhansen created at 2009-11-20 06:22:20

Resolution: fixed


---

Comment by mhansen created at 2009-11-20 06:22:20

Fixed by #7352
