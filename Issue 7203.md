# Issue 7203: prereq-0.4 does not exit if CC is not gcc, but CXX is g++

archive/issues_007203.json:
```json
{
    "body": "Assignee: tbd\n\nOne of changes made in my recent update of prereq (#7021) from 0.3 to 0.4 was to exit when there was a mix of GNU and non-GNU compilers. \n\nWhilst this works if you have a GNU C compiler and a non-GNU C++ compiler, it does **not** work if you have a non-GNU C compiler and a GNU C++ compiler. This is a bug, and is entirely my fault. \n\nBasically the testing for mixing of compilers happens in configure.ac something like this:\n\n\n\n```\nif test x$GCC = xyes\nthen\n    # Check if C++ compiler is g++. If not, there is a problem.\n    # as mixing GNU and non-GNU compilers is likely to cause problems.\n    if test x$GXX != xyes\n    then\n       AC_MSG_WARN([You are trying to use gcc but not g++])\n       AC_MSG_ERROR([The mixing of GNU and non-GNU compilers is not permitted])\n    fi\n```\n\n\nThere is no corresponding test if x$GXX (the C++ compiler) is GNU. (Yes, GXX is correct, its not a mistake/)\n\nI will also need to fix #7156, which is a minor portability issue with prereq. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7203\n\n",
    "created_at": "2009-10-13T23:02:54Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "prereq-0.4 does not exit if CC is not gcc, but CXX is g++",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7203",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

One of changes made in my recent update of prereq (#7021) from 0.3 to 0.4 was to exit when there was a mix of GNU and non-GNU compilers. 

Whilst this works if you have a GNU C compiler and a non-GNU C++ compiler, it does **not** work if you have a non-GNU C compiler and a GNU C++ compiler. This is a bug, and is entirely my fault. 

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


Issue created by migration from https://trac.sagemath.org/ticket/7203





---

archive/issue_comments_059662.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-20T06:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7203#issuecomment-59662",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_059663.json:
```json
{
    "body": "Fixed by #7352",
    "created_at": "2009-11-20T06:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7203#issuecomment-59663",
    "user": "https://github.com/mwhansen"
}
```

Fixed by #7352



---

archive/issue_events_007424.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-11-20T06:22:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7203",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7203#event-7424"
}
```
