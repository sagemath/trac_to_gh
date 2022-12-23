# Issue 335: directory not empty issue

Issue created by migration from https://trac.sagemath.org/ticket/335

Original creator: was

Original creation time: 2007-03-27 14:28:48

Assignee: was

From Kate Minola:


```
After building sage-2.4 on my pentium4-pc-linux machine,
when I do 'make test', I get

[stuff deleted]
sage -t devel/sage-main/sage/geometry/lattice_polytope.py
sage -t  devel/sage-main/sage/geometry/lattice_polytope.py  [Errno 39]
Directory not empty: '/home/kate/.sage//tmp/31372/'

        [3.2 s]
[stuff deleted]

The code in the function 'all_cached_data(polytopes)' in lattice_polytope.py
seems to be causing this.

Even though at the end, 'make test' says all the tests passed, this
looks like a problem.
```



---

Comment by mabshoff created at 2007-08-24 23:09:38

Mmmh, didn't this get fixed? Something with NFS mounts (or some other network file system via automounter)

Cheers,

Michael


---

Comment by was created at 2007-08-30 00:23:19

Resolution: fixed


---

Comment by was created at 2007-08-30 00:23:19

This has long since been fixed.
