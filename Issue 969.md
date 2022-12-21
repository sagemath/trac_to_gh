# Issue 969: cvxopt miscompiled on OSX ppc

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-22 15:16:01

Assignee: was


```
On 10/22/07, Hamptonio <hamptonio`@`gmail.com> wrote:
> I had the following failure from "make test",  from devel/sage-main/
> sage/numerical/test.py.  I'm guessing its from the convoluted history
> of my fortran installs on that machine (a powerpc apple powerbook):

You're right.  We added some doctests in test.py to specifically
test that all the convex optimization code really got built.
Evidently it didn't for you.  If you aren't doing convex optimization
(via cvxopt) this won't affect you. 

By the way, I am able to replicate exactly this problem on my powerpc mac test machine.

> sage -t  devel/sage-main/sage/numerical/test.py
> **********************************************************************
> File "test.py", line 4:
>     : from cvxopt.base import *
> Exception raised:
>     Traceback (most recent call last):
>       File "/Users/mh/sage-2.8.4.1/local/lib/python2.5/doctest.py",
> line 1212, in __run
>         compileflags, 1) in test.globs
>       File "<doctest __main__.example_0[0]>", line 1, in <module>
>         from cvxopt.base import *###line 4:
>     : from cvxopt.base import *
>     ImportError: dlopen(/Users/mh/sage-2.8.4.1/local/lib/python/site-
> packages/cvxopt/base.so, 2): Symbol not found: __g95_ioparm
>       Referenced from: /Users/mh/sage-2.8.4.1/local/lib/python/site-
> packages/cvxopt/base.so
>       Expected in: dynamic lookup
> 
> **********************************************************************
> File "test.py", line 5:
>     : from cvxopt import umfpack
> Exception raised:
>     Traceback (most recent call last):
>       File "/Users/mh/sage-2.8.4.1/local/lib/python2.5/doctest.py",
> line 1212, in __run
>         compileflags, 1) in test.globs
>       File "<doctest __main__.example_0[1]>", line 1, in <module>
>         from cvxopt import umfpack###line 5:
>     : from cvxopt import umfpack
>     ImportError: dlopen(/Users/mh/sage-2.8.4.1/local/lib/python/site-
> packages/cvxopt/umfpack.so, 2): Symbol not found: __g95_st_write_done
>       Referenced from: /Users/mh/sage-2.8.4.1/local/lib/python/site-
> packages/cvxopt/umfpack.so
>       Expected in: dynamic lookup
> 
> **********************************************************************
> 1 items had failures:
>    2 of   8 in __main__.example_0
> ***Test Failed*** 2 failures.
> 
> On Oct 21, 3:03 pm, "John Cremona" <john.crem...`@`gmail.com> wrote:
> > Successfully upgraded to 2.8.8.1 on linux (Kubuntu 7.04):
> >
> > sage --testall
> > (...)
> >
> > All tests passed!
> > Total time for all tests: 1978.6 seconds
> >
> > John Cremona
> 
> 
> --~--~---------~--~----~------------~-------~--~----~
> To post to this group, send email to sage-devel`@`googlegroups.com
> To unsubscribe from this group, send email to sage-devel-unsubscribe`@`googlegroups.com
> For more options, visit this group at http://groups.google.com/group/sage-devel
> URLs: http://sage.scipy.org/sage/ and http://modular.math.washington.edu/sage/
> -~----------~----~----~----~------~----~------~--~---
> 
> 


-- 
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org
```



---

Comment by was created at 2007-10-27 00:13:28

NOTE -- this is definitely *not* fixed yet.  With my clean sage-2.8.9 install
on my 32-bit debian test machine this happens upon typing 

from cvxopt import solvers



Specifically there's a bug report about this from lwd8700 at yahoo in sage-support. 

William


---

Comment by mabshoff created at 2007-10-28 12:06:31

The issue has been fixed upstream:

```
We recently became aware of the build-problems on OSX.  The fixes are
included in the next release of
CVXOPT (>0.9).

Joachim
```


Cheers,

Michael


---

Comment by was created at 2007-10-29 05:36:50

Josh Kantor has created an updated cvxopt that fixes these problems:

http://sage.math.washington.edu/home/jkantor/spkgs/cvxopt-0.8.2.p3.spkg


---

Comment by was created at 2007-10-29 05:36:50

Changing priority from major to critical.


---

Comment by mabshoff created at 2007-11-01 10:17:18

Resolution: fixed


---

Comment by mabshoff created at 2007-11-01 10:17:18

applied to 2.8.11.alpha0. I also updated the patch level to "4" and cleanup up a little in the spkg itself.

Cheers,

Michael
