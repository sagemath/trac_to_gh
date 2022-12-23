# Issue 6216: make a sage.misc.profile module that makes hotshot and grof2dot and line_profiler easily used

Issue created by migration from https://trac.sagemath.org/ticket/6216

Original creator: ncalexan

Original creation time: 2009-06-05 00:20:36

Assignee: tbd

CC:  craigcitro mhansen

Keywords: misc profile hotshot gprof2dot timing


```
[5:12pm] ncalexan: It's a script that takes profile output and writes a .dot file of the callgraph.
[5:12pm] ncalexan: It's incredibly useful for understanding where your time is going.
[5:13pm] ddrake: sounds nice.
[5:13pm] ncalexan: It is.  So I'd like to include it 
[5:13pm] mhansen: ncalexan: Have you used Robert Kern's line profiler?
[5:13pm] ncalexan: mhansen: no.
[5:13pm] ncalexan: link
[5:14pm] mhansen: http://packages.python.org/line_profiler/
[5:14pm] cwitty left the chat room. (Read error: 113 (No route to host))
[5:17pm] ncalexan: They look complimentary.
[5:18pm] mhansen: Yes.  But, I often find the line_profiler more useful.  I just thought I'd mention it since people were talking about profiling.
[5:18pm] ncalexan: We need to make this stuff easier to use from the prompt.
[5:18pm] mhansen: Definitely
[5:18pm] ncalexan: Maybe a sage.misc.profile module is in order.
[5:19pm] ncalexan: I will make a ticket.
[5:19pm] mhansen: It'd be cool if we could integrate it with craigcitro's time capsule
```



---

Comment by mmezzarobba created at 2015-04-14 08:31:27

#17689 makes `line_profiler` easy to access
