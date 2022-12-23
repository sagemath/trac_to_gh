# Issue 6937: Fixed cached_function to handle defaults better.

Issue created by migration from https://trac.sagemath.org/ticket/6937

Original creator: boothby

Original creation time: 2009-09-15 20:06:23

Assignee: boothby

CC:  craigcitro

We expect the following example to take about 10 seconds:


```
sage: @cached_function
sage: def foo(x = 5):
...       print "computing foo(%s)"%x
...       sleep(10)
...       return 0
sage: w = walltime()
sage: foo()
computing foo(5)
sage: foo(5)
computing foo(5)
sage: foo(x=5)
computing foo(5)
sage: print "that took %s seconds!"%walltime(w)
that took 29.9967029095 seconds!
```


... but that obviously isn't the case.  fix it!


---

Comment by rlm created at 2009-09-19 20:05:09

Here's a problem:


```
sage: class Foo:
    def bar(self, a, b, c=0, d=None):
        return a
sage: A = Foo()
sage: A.bar(1,2,3,4)
1
sage: from sage.misc.function_mangling import ArgumentFixer
sage: AA = ArgumentFixer(A.bar)
sage: AA.fix_to_named(1,2,3,4)
((), (('self', 1), ('a', 2), ('b', 3), ('c', 4), ('d', None)))

```


Here, self isn't 1. a should be 1.


---

Comment by rlm created at 2009-09-19 20:18:15

Sorry, my gripe should be that "classmethod" is undocumented.


---

Attachment


---

Comment by rlm created at 2009-09-20 05:14:53

Bing!


---

Comment by mvngu created at 2009-09-22 20:02:14

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:31:03

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.
