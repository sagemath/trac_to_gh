# Issue 928: add delayed profiling mode for callgrind

Issue created by migration from https://trac.sagemath.org/ticket/928

Original creator: mabshoff

Original creation time: 2007-10-19 16:49:03

Assignee: mabshoff

Keywords: valgrind, callgrind

If you pass

```
 --instr-atstart=no
```

to callgrind profiling is disabled until you tell callgrind via 

```
callgrind-control
```

to turn on profiling. After you have finished profiling your code you can use callgrind-contorl again to turn profiling off again. This can be very useful because if you only want to profile certain bits and also saves potentially a whole lot of time if it takes a long time to get to the part of the computation you want to profile.

Carl Witty suggested this in #sage-devel yesterday.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-19 16:55:54

Changing status from new to assigned.


---

Comment by jdemeyer created at 2014-11-13 14:03:04

Changing component from packages: standard to packages: optional.
