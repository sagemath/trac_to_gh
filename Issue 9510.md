# Issue 9510: gfan fails to build on skynet machines eno, taurus

Issue created by migration from https://trac.sagemath.org/ticket/9510

Original creator: jhpalmieri

Original creation time: 2010-07-15 15:49:25

Assignee: tbd

Toward the end of the gfan log file, it says

```
make[2]: Leaving directory `/home/palmieri/eno/sage-4.5.alpha4/spkg/build/gfan-0.4plus.p1\
/src'
rm: cannot remove `gfan_*': No such file or directory
./gfan: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.14' not found (required by ./gfan\
)
gfan links not created correctly
```

The full log file is here:

[http://sage.math.washington.edu/home/palmieri/misc/gfan-0.4plus.p1.log](http://sage.math.washington.edu/home/palmieri/misc/gfan-0.4plus.p1.log)



---

Comment by jhpalmieri created at 2010-07-15 20:11:32

I've now built this successfully.  I'm pretty sure that the reason is because of a bad  LD_LIBRARY_PATH, as in #8769.  I was building on eno using "screen", and when I use screen on eno, it doesn't set LD_LIBRARY_PATH at all.  On taurus, LD_LIBRARY_PATH was misconfigured.  On taurus, for example, if I set it correctly, then gfan (and everything else) builds fine.  If I then set it to the previous wrong value and delete spkg/installed/gfan..., then I get the same error that I reported here.

So I'm going to close this ticket.


---

Comment by jhpalmieri created at 2010-07-15 20:11:32

Resolution: worksforme


---

Comment by jhpalmieri created at 2010-07-15 20:11:32

Changing priority from blocker to trivial.
