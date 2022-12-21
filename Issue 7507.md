# Issue 7507: can't forget some assumptions

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-11-21 12:21:56

Assignee: burcin

CC:  kcrisman robert.marik

Keywords: maxima, assume

Reported by Mike Witt on sage-support:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: n=var('n')
sage: assumptions()
[]
sage: foo=sin((-1)*n*pi)
sage: foo.simplify()
-sin(pi*n)
sage: assume(n, 'odd')
sage: assumptions()
[n is odd]
sage: foo=sin((-1)*n*pi)
sage: foo.simplify()
0
sage: forget(n, 'odd')
sage: assumptions()
[]
sage: foo=sin((-1)*n*pi)
sage: foo.simplify()
0
```

| Sage Version 4.2, Release Date: 2009-10-24                         |
| Type notebook() for the GUI, and license() for information.        |
Robert Dodier's comments:


```
I'm guessing that Sage punts to Maxima for this stuff.
For better or worse (mostly worse) there are different ways
to declare & undeclare stuff in Maxima.
For the "odd" declaration, it's declare(n, odd) and remove(n, odd).
I guess assume(n, 'odd') was translated to declare(n, odd) but
forget(n, 'odd') was not translated to remove(n, odd).
I don't know much about Sage so I could be way off here.
```


Here is the thread:

http://groups.google.com/group/sage-support/browse_thread/thread/9db67c2df781966b


---

Comment by kcrisman created at 2009-11-21 14:16:41

Okay, this is closed related to #1163 and #7315.  Should not be hard to fix, and might help in making GenericDeclarations better in any case.


---

Comment by kcrisman created at 2010-01-08 16:36:56

Replying to [comment:1 kcrisman]:
> Okay, this is closed related to #1163 and #7315.  Should not be hard to fix, and might help in making GenericDeclarations better in any case.

Sorry, I meant _closely_ related.


---

Attachment

This seems to be fixed in the meanwhile. attachment:trac_7507-forget_assumptions.patch adds a doctest.


---

Comment by burcin created at 2011-05-08 20:11:15

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-05-11 18:58:44

Yes, this was fixed as part of #1163, as it turns out.

```

    for x in preprocess_assumptions(args):
        if isinstance(x, (tuple, list)):
            forget(*x)
```

used to have

```

    for x in preprocess_assumptions(args):
        if isinstance(x, (tuple, list)):
            assume(*x)
```

before that patch.


---

Comment by kcrisman created at 2011-05-11 19:04:15

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-05-11 19:04:15

Nice catch to close this; tests pass.


---

Comment by jdemeyer created at 2011-05-25 12:51:51

Resolution: fixed
