# Issue 402: %slide directive produces segfault in dvipng

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-07-11 20:25:07

Assignee: boothby

Currently, both in sage 2.6 and William's online notebook (which I guess is also sage 2.6)

```
%slide
some text here
```

fails with

```
sh: line 1: 23279 Segmentation fault      dvipng -q* -T bbox -D 256 sage6.dvi
>/dev/null 2>/dev/null
An error occured.
[...]
```



---

Comment by was created at 2007-08-18 23:34:30

Resolution: fixed
