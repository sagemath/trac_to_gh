# Issue 8753: get pynac to build with gcc-4.5.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-23 22:50:04

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


---

Comment by was created at 2010-04-26 17:52:48

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

Comment by was created at 2010-04-26 17:52:55

Changing status from new to needs_review.


---

Comment by was created at 2010-04-26 20:12:34

Changing priority from major to blocker.


---

Comment by mhansen created at 2010-04-27 06:54:23

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-04-27 06:54:23

Looks good to me.  There is a new spkg at 

http://sage.math.washington.edu/home/mhansen/pynac-0.1.12.spkg

which incorporates this fix.  I've posted this to #8644.


---

Comment by was created at 2010-04-28 19:26:08

Resolution: fixed
