# Issue 6802: define a real variable with var()

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-08-22 10:49:16

Keywords: var(), real variable

At this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/7bf451cf8202e085) thread, there is a request for `var()` to be able to define a "real" variable. Then one can do this

```
sage: a = var("a")
sage: conjugate(a)
a
```

As of Sage 4.1.1, we have this:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a = var("a")
sage: conjugate(a)
conjugate(a)
```



---

Comment by mvngu created at 2009-08-22 14:18:34

Resolution: duplicate


---

Comment by mvngu created at 2009-08-22 14:18:34

Closing this as a duplicate of #6559.
