# Issue 4863: bug in install_package

Issue created by migration from https://trac.sagemath.org/ticket/4863

Original creator: was

Original creation time: 2008-12-24 04:52:27

Assignee: mabshoff

CC:  mhansen mvngu

It is impossible to use the `install_package` command to install pyopenssl-0.6.  See below:


```
sage: install_package('pyopenssl-0.6')
Possible names of non-installed packages starting with 'pyopenssl-0.6':
  pyopenssl-0.6
  pyopenssl-0.6
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/usr/local/sage/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.5/site-packages/sage/misc/package.pyc in install_package(package, force)
     79         for P in L:
     80             print " ", P
---> 81         raise ValueError, "There is more than one package name starting with '%s'. Please specify!"%(package)
     82     if len(L)==0:
     83         if not force:

ValueError: There is more than one package name starting with 'pyopenssl-0.6'. Please specify!
sage: 
```


I verified this error in sage-3.2.2 on Linux and OS X.


---

Comment by SimonKing created at 2008-12-28 11:31:30

Replying to [ticket:4863 was]:
> It is impossible to use the `install_package` command to install pyopenssl-0.6.  
<snip>
> I verified this error in sage-3.2.2 on Linux and OS X.

No problem for me, at least in sage-3.2.1 on Linux.

So maybe I'll try to upgrade and check again.


---

Comment by SimonKing created at 2008-12-30 22:50:36

Replying to [comment:1 SimonKing]:
> No problem for me, at least in sage-3.2.1 on Linux.
> 
> So maybe I'll try to upgrade and check again.

Meanwhile I upgraded and removed `SAGE_ROOT/spkg/installed/pyopenssl-0.6` and `SAGE_ROOT/optional/pyopenssl-0.6.spkg`. Then I tried 
`install_package('pyopenssl-0.6')` again. 

There was no problem. So, I can not reproduce the bug.


---

Comment by SimonKing created at 2009-02-06 21:48:39

Replying to [ticket:4863 was]:
> It is impossible to use the `install_package` command to install pyopenssl-0.6.  See below:
>

> ...
>

> I verified this error in sage-3.2.2 on Linux and OS X.

Still (meanwhile sage-3.2.3 on Linux) I can not reproduce the problem. Doing `install_package('pyopen')` resulted in the installation of pyopenssl, meanwhile in version 0.8.

So, I suggest to resolve the bug as invalid.


---

Comment by mabshoff created at 2009-02-06 23:02:04

3.4 is for ReST tickets only.

Cheers,

Michael


---

Comment by jason created at 2009-10-06 19:29:36

Please note the request to close this.


---

Comment by mhansen created at 2009-10-07 04:01:14

Resolution: invalid
