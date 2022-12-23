# Issue 2891: inline_fortran -- completely rewrite to not save a global variable and *not* got hacked into various global structures all over

Issue created by migration from https://trac.sagemath.org/ticket/2891

Original creator: was

Original creation time: 2008-04-12 03:14:41

Assignee: cwitty

CC:  jdemeyer

The InlineFortran stuff in misc/inline_fortran.py is bad.  That global variable should be explicitly passed into the __eval__ and __call__ methods, and should *not* be set on creation.   I've attached what the file *should* roughly be, but I can't get it to work.

Also, it's terrible the hacking in server/support.py to get the fortran stuff in there.  This is just really wrong. 

NOTE -- this all works -- it's not a bug.  It's just not good programming.


---

Comment by was created at 2008-04-12 03:17:57

Changing type from defect to enhancement.


---

Attachment


---

Comment by kcrisman created at 2014-12-09 16:17:37

Hey Jeroen, you worked on several related tickets like #13992 and #13887 - is this ticket even needed at this point?  

~~(Also, I can't figure out how exactly `src/sage/misc/inline_fortran.py` gets used, as it doesn't seem to ever be imported, and is only mentioned a comment in the scripts...)~~ The notebook is the only place this is used in any case (maybe also SMC?).  See also #8427.


---

Comment by jdemeyer created at 2014-12-09 17:19:29

Replying to [comment:8 kcrisman]:
> Hey Jeroen, you worked on several related tickets like #13992 and #13887 - is this ticket even needed at this point?
For sure, the issue that this ticket talks about (the `globals` variable) hasn't been changed.


---

Comment by jdemeyer created at 2014-12-09 17:21:50

The problem is also that there isn't a single example using this `globals` argument, so it's hard to even know what the code _should_ do.


---

Comment by jdemeyer created at 2014-12-09 17:26:39

We could probably remove this whole `inline_fortran` thing without anybody noticing...


---

Comment by jdemeyer created at 2014-12-09 17:31:39

If you care, the `inline_fortran` stuff was added in Sage by

```
commit d46359f9384268204bd687e2a7aaded15938399d
Author: William Stein <wstein@gmail.com>
Date:   Tue Jun 26 16:37:36 2007 -0700

    (Josh Kantor and W Stein) Add support for %fortran in the notebook.

```



---

Comment by kcrisman created at 2014-12-09 18:06:41

> We could probably remove this whole `inline_fortran` thing without anybody noticing...
I thought so too, but I figured out where it is used - in sagenb for `%fortran`.  As it says in the thing you quote, in fact.


---

Comment by jdemeyer created at 2014-12-09 20:04:37

New commits:


---

Comment by jdemeyer created at 2014-12-09 20:04:37

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2014-12-09 20:13:31

Overall looks good to me, but I would have to take some time to look at the details in a few instances, especially the 

```
# Note that f2py() doesn't raise an exception if it fails.
```

bit and checking that the deprecations work.  The reorganization, importing, and removal of much of server/support.py is just fine.


---

Comment by git created at 2014-12-09 21:23:12

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-12-12 10:44:22

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kcrisman created at 2014-12-12 16:20:54

I'm not sure why you removed the doctest file, since after you remove `sage/server/misc.py` there are no doctests left in that directory :-) but surely it can't hurt.

However, this needs a slight bit of work to be compatible with https://github.com/sagemath/sagenb/pull/291 now in upstream.  Before:

```
sage: from sage.server.support import save_session
sage: save_session()
DeprecationWarning: 
Importing save_session from here is deprecated. If you need to use it, please import it directly from sagenb.misc.support
See http://trac.sagemath.org/2891 for details.

```

after:

```
sage: from sage.server.support import save_session
sage: save_session()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
AttributeError: 'module' object has no attribute 'save_session'
```

and likewise for `load_session` and `variables`, I believe.


---

Comment by kcrisman created at 2014-12-12 16:43:28

Glad the deprecation works, but I don't know why this failed - and shouldn't your exception `imp` code take care of this if it wasn't there?

```
sage: fortran('fib1.f')
/Users/.../sage/local/lib/python2.7/site-packages/sage/misc/inline_fortran.py:23: DeprecationWarning: Calling fortran() with a filename is deprecated, use fortran(open(f).read) instead
See http://trac.sagemath.org/2891 for details.
  return self.eval(*args, **kwds)
sage: import numpy
sage: a = numpy.array(range(10), dtype=float)
sage: fib(a,10)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-5-a86fea2d23a9> in <module>()
----> 1 fib(a,Integer(10))

NameError: name 'fib' is not defined
sage: 
```


But it did find the right file, if I do something else it complains a few lines later because it can't load the file, which makes sense.  If I use `globals` (wasn't that the deprecated part? maybe only elsewhere) I get

```

sage: fortran('./fib1.f',globals())
sage: fib(a,10)  # so now it exists, anyway!
sage: a = numpy.array(range(10), dtype=float)
sage: a
array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
```

I'm not saying 'needs work', but I am saying 'reviewer doesn't understand'.


---

Comment by kcrisman created at 2014-12-12 16:46:27

But if I write the file in the other test

```
sage: fortran('./hello.f',globals())
/Users/.../sage/local/lib/python2.7/site-packages/sage/misc/inline_fortran.py:23: DeprecationWarning: Calling fortran() with a filename is deprecated, use fortran(open(f).read) instead
See http://trac.sagemath.org/2891 for details.
  return self.eval(*args, **kwds)
sage: hello
<fortran object>
sage: hello()
 Hello World!
```



---

Comment by jdemeyer created at 2014-12-12 18:34:43

Replying to [comment:22 kcrisman]:
> If I use `globals`
Yes, that's what you should do.

> wasn't that the deprecated part? maybe only elsewhere
Indeed, elsewhere. The idea of this ticket is that the `globals` parameter was moved from `InlineFortran.__init__()` to `InlineFortran.__call__()`.


---

Comment by kcrisman created at 2014-12-12 19:26:57

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2014-12-12 19:26:57

Got it, I also see what I was messing up earlier.

So this is fine other than the import stuff in comment:21, though one way to deal with that is to _not_ remove those for now and deal with it when updating sagenb, e.g. #10057.


---

Comment by git created at 2014-12-13 07:37:34

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jdemeyer created at 2014-12-13 07:38:42

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2014-12-13 17:09:48

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-12-15 17:50:57

Resolution: fixed
