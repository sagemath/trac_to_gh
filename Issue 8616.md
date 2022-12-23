# Issue 8616: Symbolic type checking and expression parcing module

Issue created by migration from https://trac.sagemath.org/ticket/8616

Original creator: yuri.k

Original creation time: 2010-03-27 20:26:08

Assignee: burcin

CC:  robert.marik novoselt

Keywords: symbolic, type, subexpression

Provides unified interface for standard python types and sage specific types.
Treats everything as symbolic expression which allows to check its type, take
operator and operands and extract subexpressions by given types.

http://groups.google.com/group/sage-devel/browse_thread/thread/f2ba2198dc5b79ed


---

Comment by yuri.k created at 2010-03-27 20:27:13

Changing status from new to needs_review.


---

Attachment

symbolic sage module


---

Attachment

symbolic sage module


---

Comment by robert.marik created at 2010-03-28 13:20:15

Hm I have the following error after installing the patch

```
ImportError: No module named mtype
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```

And there is no mtype.* file in sage/symmbolic in my Sage 4.3.4


---

Attachment


---

Attachment

more precise autodetect of independent variable


---

Comment by robertwb created at 2010-04-10 17:35:24

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2010-04-10 17:35:24

Thank you for working on desolve, that module is in need of a lot of help. I'm really not seeing what mtype has to do with it though (and what does "mtype" mean? wtype, stype, ... are equally obscure). Also _ for a wildcard is very non-standard notation, perhaps "*.integer" would be better. 

In any case, my main issue with this patch is that a huge list of isinstance statements is not the way to implement this--it's brittle and requires the module to know about everything in Sage. If we need an mtype (operator, ...), it should be done OO style, with tests just for a few of the builtin types (and even then it could be cleaner, using their names.


---

Comment by yuri.k created at 2010-04-10 21:27:51

Replying to [comment:10 robertwb]:
> Thank you for working on desolve, that module is in need of a lot of help. I'm really not seeing what mtype has to do with it though (and what does "mtype" mean? wtype, stype, ... are equally obscure). Also _ for a wildcard is very non-standard notation, perhaps "*.integer" would be better. 
>

_ wildcard is used in scala. * is used for multiply operator. desolve module is really bad it is beter to completly rewrite it, but sage doesn't have enough functions to start doing it. mtype is the firs step. It helps to deal with symbolical expression.

> In any case, my main issue with this patch is that a huge list of isinstance statements is not the way to implement this--it's brittle and requires the module to know about everything in Sage. If we need an mtype (operator, ...), it should be done OO style, with tests just for a few of the builtin types (and even then it could be cleaner, using their names.

I absolutely agree with you. It is much better to have class hierarchy or at least some common interface which can help to define type. And wraps or mixins should be used for Python types. But I did mtype class to concentrate attention on existing problem - sage is almost useless for complex symbolical computations (it is my opinion as well as  opinion of my colleagues) It is hard for people who are new to python. You shouldn't use mtype, but it is good to do smth about this problem in sage.

I made sketch to solve some simple de problems I write some common functions in mtype, which can be easily rewritten to extract only diff operators. So just use it if you want to.

I finished with sage for this year, now I need to do smth real. I'm sorry I can't afford to spend some more time to finish this improvements.


---

Comment by kcrisman created at 2011-06-14 17:31:44

Changing title to more accurately reflect what it's about.
