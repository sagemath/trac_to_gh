# Issue 556: ntl re-wrapping in sage-2.8.3 broke sage on itanium linux

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-01 18:51:32

Assignee: somebody


```
> On ia64-Linux, sage-2.8.3 builds, but when I do
> 
> %./sage
> 
> I get
> 
> % ./sage
> ----------------------------------------------------------------------
> | SAGE Version 2.8.3, Release Date: 2007-08-31                       |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> 
> ---------------------------------------------------------------------------
> <type 'exceptions.RuntimeError'>          Traceback (most recent call last)
> 
> /home/kate/sage/sage-2.8.3-ia64-Linux/local/bin/<ipython console> in <module>()
> 
> /home/kate/sage/sage-2.8.3-ia64-Linux/local/lib/python2.5/site-packages/sage/all_cmdline.py
> in <module>()
>      12 try:
>      13
> ---> 14     from sage.all import *
>      15     from sage.calculus.predefined import x
>      16     preparser(on=True)
> 
> /home/kate/sage/sage-2.8.3-ia64-Linux/local/lib/python2.5/site-packages/sage/all.py
> in <module>()
>      55 from sage.misc.sh import sh
>      56
> ---> 57 from sage.libs.all       import *
>      58
>      59 get_sigs()
> 
> /home/kate/sage/sage-2.8.3-ia64-Linux/local/lib/python2.5/site-packages/sage/libs/all.py
> in <module>()
>       2
> ----> 3 import sage.libs.ntl.all  as ntl
>       4
>       5 #import sage.libs.cf.cf as cf
>       6
> 
> /home/kate/sage/sage-2.8.3-ia64-Linux/local/lib/python2.5/site-packages/sage/libs/ntl/all.py
> in <module>()
>      24 #*****************************************************************************
>      25
> ---> 26 from sage.libs.ntl.ntl import (make_new_ZZ as ZZ,
>      27                  ntl_ZZ as ZZ_class,
>      28                                randomBnd as ZZ_random,
> 
> /home/kate/sage/sage-2.8.3-ia64-Linux/local/bin/ntl.pyx in ntl()
> 
> /home/kate/sage/sage-2.8.3-ia64-Linux/local/bin/ntl.pyx in ntl.ntl_setSeed()
> 
> <type 'exceptions.RuntimeError'>:

A lot of work has gone into improving the SAGE/ntl interface lately
by Joel Mohler and others.  Unfortunately it's exactly the sort of thing
that could break things on non-tested systems. Many thanks for 
reporting this -- i'll open a trac ticket right now. 

William
```



---

Comment by was created at 2007-09-13 14:11:52

Resolution: fixed
