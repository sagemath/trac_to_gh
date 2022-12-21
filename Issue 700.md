# Issue 700: fix significant bug in how cvxopt package is built on Linux

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-20 02:07:48

Assignee: was


```
I have a cvxopt package in my spkgs directory that does not raise an error
when doing

sage: from cvxopt.base import *

The problem is that on linux libf95.a must be linked in, but its located
in the local/lib/gcc-lib/i686-pc-linux-gnu/4.0.3
and I had to add that directory to the path to link it in (of course the
path is different on 64 bit).

On OSX everything works fine for some reason.

```



Note -- in addition to using the package above, there must be a doctest
added to the core SAGE library that does
   sage: from cvxopt.base import *
just to make sure the fix works on our architectures.

Likewise, 
    from scipy.optimize import *
should be a doctest.


---

Comment by was created at 2007-09-21 02:08:00

Resolution: fixed


---

Comment by was created at 2007-09-21 02:21:54

Resolution changed from fixed to 


---

Comment by was created at 2007-09-21 02:21:54

Changing status from closed to reopened.


---

Comment by was created at 2007-09-21 02:23:27

The way spkg-install is designed, this doesn't work on systems that weren't built using g95.  What if somebody builds using gfortran system-wide?
Then the spkg-install will die.

Also, even with g95 on my Ubuntu 64-bit test system umfpack still fails to get the right symbol after
installing this package:


```
sage: import cvxopt.umfpack
---------------------------------------------------------------------------
<type 'exceptions.ImportError'>           Traceback (most recent call last)

/home/was/s/devel/sage-ranges/sage/numerical/<ipython console> in <module>()

<type 'exceptions.ImportError'>: /home/was/s/local/lib/python2.5/site-packages/cvxopt/umfpack.so: undefined symbol: _g95_filename

```



---

Comment by was created at 2007-09-21 22:33:35


```
from josh:
Hmm. I don't understand why this doesn't work on your 64 bit system, as it
works fine on sage.math. Was this using the binary g95 that sage installs?

As for the gfortran issue. In that case we need to link in libgfortran,
however then we have to detect which one was used. Are there instructions
on how to build with gfortran so there is something we can check to be
sure which was used.

                                                       Josh
```



---

Comment by mabshoff created at 2007-10-19 18:40:56

This ticket is related to #709 and #636. Once #709 goes in the other two tickets should be resolved.

Cheers,

Michael


---

Comment by was created at 2007-10-20 20:21:04

Resolution: fixed
