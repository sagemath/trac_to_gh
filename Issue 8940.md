# Issue 8940: doctest failures in sagedoc.py

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-05-10 01:09:57

Assignee: tbd

Here's the failure on sage.math, when building Sage 4.4.2.alpha0 from source:

```
sage -t  -long devel/sage/sage/misc/sagedoc.py # 3 doctests failed
```

The failure with sagedoc.py is due ticket #8468, whose patch was merged without also merging the relevant Sphinx configuration files.


---

Comment by mvngu created at 2010-05-10 10:38:15

This is invalid due to the report at this [sage-devel](http://groups.google.com/group/sage-devel/msg/13ea54c19e7fcb20) thread.


---

Comment by mvngu created at 2010-05-10 10:38:15

Resolution: invalid
