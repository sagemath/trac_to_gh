# Issue 1994: cython spyx files -- cinclude, clib, issues

Issue created by migration from https://trac.sagemath.org/ticket/1994

Original creator: was

Original creation time: 2008-01-31 04:34:13

Assignee: was

CC:  malb robertwb

There are some issues with cython spyx files:

   1. There is *still* nothing in the documentation anywhere in sage about cinclude, clib, etc.  Here's a hint:

```
Basically you put
# clang c
# clib  cblas
# cfile myfile.c
# cinclude super.h standard.h
```

Questions -- where can one put these?   Must the # be there?  
However this is documented, at a bare minimum typing 

```
sage: cython?
sage: load?
sage: attach?
```

should give enough information to find docs that clearly explain this cinclude, etc. directives. 

   2. Create a file a.pxi and a file b.pyx.  Put one of the # directives in the .pxi file and include the pxi file in the pyx file.  The directive is ignored.  This caused a ton of confusion today.


---

Comment by kedlaya created at 2008-02-14 22:18:17

Is there also a directive ccflags (analogous to cflags in C)? For instance, in order to compile an spkg using FLINT, one needs a line like

```
#ccflags -std=c99
```



---

Comment by mabshoff created at 2008-07-06 12:08:51

(1) should have been dealt via #3530, i.e. the documentation of the pragmas. 

(2) is potentially still valid and I am not sure whose fault it is: Sage or Cython. 

I am adding Martin and Robert to the CC field here.

Cheers,

Michael


---

Comment by malb created at 2008-07-06 12:11:23

Actually, (1) is not dealt with since it isn't necessarily easy to get to the new documentation. That should be addressed.


---

Comment by kcrisman created at 2012-05-18 03:06:27

Note that [this stackoverflow.com post](http://stackoverflow.com/questions/6363978/cython-linking-to-custom-c-code) points to this ticket.  Apparently this is still something that could be documented within Sage better?


---

Comment by jdemeyer created at 2017-06-02 09:42:07

Those directives should be deprecated anyway: #22461


---

Comment by jdemeyer created at 2017-06-02 09:42:07

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2017-06-02 09:42:12

Changing status from needs_review to positive_review.


---

Comment by embray created at 2017-07-13 07:54:31

Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).


---

Comment by embray created at 2017-07-13 07:54:31

Resolution: wontfix
