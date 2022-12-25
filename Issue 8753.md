# Issue 8753: get pynac to build with gcc-4.5.

archive/issues_008753.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nRight now:\n\n```\nfunction.cpp:1886:29: warning: deprecated conversion from string constant to \u2018char*\u2019\nfunction.cpp: In member function \u2018GiNaC::ex GiNaC::function::power(const GiNaC::ex&) const\u2019:\nfunction.cpp:2186:15: error: expected type-specifier\nfunction.cpp:2186:15: error: expected \u2018)\u2019\nfunction.cpp:2187:72: error: conversion from \u2018int*\u2019 to \u2018GiNaC::ex\u2019 is ambiguous\nex.h:297:1: note: candidates are: GiNaC::ex::ex(long unsigned int) <near match>\nex.h:291:1: note:                 GiNaC::ex::ex(long int) <near match>\nex.h:285:1: note:                 GiNaC::ex::ex(unsigned int) <near match>\nex.h:273:1: note:                 GiNaC::ex::ex(int) <near match>\nmv -f .deps/color.Tpo .deps/color.Plo\n\n\n```\n\nThere is a new spkg posted on trac, but it doesn't fix this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8753\n\n",
    "created_at": "2010-04-23T22:50:04Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "get pynac to build with gcc-4.5.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8753",
    "user": "https://github.com/williamstein"
}
```
Assignee: GeorgSWeber

Right now:

```
function.cpp:1886:29: warning: deprecated conversion from string constant to ‘char*’
function.cpp: In member function ‘GiNaC::ex GiNaC::function::power(const GiNaC::ex&) const’:
function.cpp:2186:15: error: expected type-specifier
function.cpp:2186:15: error: expected ‘)’
function.cpp:2187:72: error: conversion from ‘int*’ to ‘GiNaC::ex’ is ambiguous
ex.h:297:1: note: candidates are: GiNaC::ex::ex(long unsigned int) <near match>
ex.h:291:1: note:                 GiNaC::ex::ex(long int) <near match>
ex.h:285:1: note:                 GiNaC::ex::ex(unsigned int) <near match>
ex.h:273:1: note:                 GiNaC::ex::ex(int) <near match>
mv -f .deps/color.Tpo .deps/color.Plo


```

There is a new spkg posted on trac, but it doesn't fix this.

Issue created by migration from https://trac.sagemath.org/ticket/8753





---

archive/issue_comments_079945.json:
```json
{
    "body": "The fix is to replace the one instance (around line 2000) of\n\n```\npower::power\n```\nin src/ginac/functions.cpp with\n\n```\nGiNaC::power\n```\nThis is evidently due to *better* checking of the proper namespace/scoping rules in GCC-4.5.0.\n\nI made the above change, and Ginac builds fine.  Moreover, I ran this code:\n\n```\nsage: 1/tan(x)\n```\nand\n\n```\nsage: derivative(1/tan(x)).integrate(x)\n1/tan(x)\n```\n\nAccording to the print statements I inserted into functions.cpp, the code that called power::power before is activated and is working correctly (no weird infinite recursions or anything).\n\nI'm hoping this can just be given a positive review by Burcin and the fix rolled into the spkg at #8644, with a link from #8644 to this ticket.",
    "created_at": "2010-04-26T17:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8753#issuecomment-79945",
    "user": "https://github.com/williamstein"
}
```

The fix is to replace the one instance (around line 2000) of

```
power::power
```
in src/ginac/functions.cpp with

```
GiNaC::power
```
This is evidently due to *better* checking of the proper namespace/scoping rules in GCC-4.5.0.

I made the above change, and Ginac builds fine.  Moreover, I ran this code:

```
sage: 1/tan(x)
```
and

```
sage: derivative(1/tan(x)).integrate(x)
1/tan(x)
```

According to the print statements I inserted into functions.cpp, the code that called power::power before is activated and is working correctly (no weird infinite recursions or anything).

I'm hoping this can just be given a positive review by Burcin and the fix rolled into the spkg at #8644, with a link from #8644 to this ticket.



---

archive/issue_comments_079946.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-26T17:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8753#issuecomment-79946",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079947.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-04-26T20:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8753#issuecomment-79947",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_079948.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-27T06:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8753#issuecomment-79948",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079949.json:
```json
{
    "body": "Looks good to me.  There is a new spkg at \n\nhttp://sage.math.washington.edu/home/mhansen/pynac-0.1.12.spkg\n\nwhich incorporates this fix.  I've posted this to #8644.",
    "created_at": "2010-04-27T06:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8753#issuecomment-79949",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  There is a new spkg at 

http://sage.math.washington.edu/home/mhansen/pynac-0.1.12.spkg

which incorporates this fix.  I've posted this to #8644.



---

archive/issue_comments_079950.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-28T19:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8753#issuecomment-79950",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_021268.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-04-28T19:26:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8753",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8753#event-21268"
}
```
