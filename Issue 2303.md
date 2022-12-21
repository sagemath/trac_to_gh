# Issue 2303: bessel_I(1,1,"scipy") segfaults with gcc 4.2.3 on Linux x86

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-02-25 21:23:59

Assignee: mabshoff

Kate reports in https://groups.google.com/group/sage-support/browse_thread/thread/f7bc183b6f052943/70f4b300f5be3d13#70f4b300f5be3d13

```
When I build 2.10.2 from source on my
x86-Linux box (pentium4-fc6) using gcc-4.2.3,
I get a 'make check' failure at

./sage -t devel/sage-main/sage/functions/special.py

sh: line 1:  3345 Illegal instruction     /home/kate/sage/sage-2.10.2-
x86-Linux/local/bin/python .doctest_special.py >.doctest/out
2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have
crashed doctest.
         [3.6 s]
exit code: 256

The offending line seems to be

sage: bessel_I(1,1,"scipy")
/home/kate/sage/sage-2.10.2-x86-Linux/local/bin/sage-sage: line 212:
3484 Illegal instruction     sage-ipython -c "$SAGE_STARTUP_COMMAND;"
"$`@`"

Kate 
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-02-25 21:24:06

Changing status from new to assigned.


---

Comment by was created at 2008-02-25 21:36:54

If anybody can reproduce this, e.g., has a P4 computer, please post here.
The temporary solution will be to disable the scipy option for bessel_l, 
then report this upstream (with a gdb traceback?) to scipy.


---

Comment by jason created at 2008-03-08 20:35:16

Using Sage 2.10.2 on this computer (Ubuntu 7.10, 32-bit):

```
vendor_id       : GenuineIntel
cpu family      : 15
model           : 4
model name      : Intel(R) Pentium(R) 4 CPU 3.80GHz
stepping        : 1
cpu MHz         : 3790.991
cache size      : 1024 KB

$ gcc -v
Using built-in specs.
Target: i486-linux-gnu
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.1.3 --program-suffix=-4.1 --enable-__cxa_atexit --enable-clocale=gnu --enable-libstdcxx-debug --enable-mpfr --enable-checking=release i486-linux-gnu
Thread model: posix
gcc version 4.1.3 20070929 (prerelease) (Ubuntu 4.1.2-16ubuntu2)

```


the doctest passes:


```
$ sage -t sage/devel/sage-main/sage/functions/special.py 
sage -t  sage/devel/sage-main/sage/functions/special.py     
         [7.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 7.3 seconds
```


and I get:


```
sage: bessel_I(1,1,"scipy")
0.565159103992000
```



---

Comment by mabshoff created at 2008-07-08 22:58:37

We can finally replicate the problem:

```
(gdb) bt
#0  0x02e474ac in dgamln_ () from /tmp/foo/sage-3.0.4.rc0-x86-Linux-fc8/local/lib/python/site-packages/scipy/special/_cephes.so
#1  0x0028bbc9 in log () from /lib/libm.so.6
#2  0x40000000 in ?? ()
```

William says:

```
William:  here is the sage-free version to replicate the problem:
scipy.special.iv(float(1),complex(1,0))
```


Cheers,

Michael


---

Attachment


---

Comment by robertwb created at 2008-07-08 23:56:53

After discussing with William Stein, we are disabling this option. Note that if one wants to use it it is much faster to directly call scypy.special.iv.


---

Comment by was created at 2008-07-09 01:08:47

Robert's patch is unfortunately no good because there are *dozens* of different special
functions that crash from scipy. We can't release something that is this broken.  

So no solution to this yet.


---

Comment by robertwb created at 2008-07-09 01:10:30

In that case we should probably not bother applying this ticket at all.


---

Comment by mabshoff created at 2008-07-09 16:26:37

Having poked around the solution might be to disabled the "-fwrapv" build option for Python. We already do that on Itanium since it caused numerous unexplained doctest failures.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-11 17:46:03

It is not a -fwrapv issue, but I have a patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-11 18:25:33

With the new spkg the following three doctests that used to segfault all due to illegal instruction now pass:

```
[mabshoff`@`cicero sage-3.0.4-x86-Linux-fc8]$ ./sage -t  devel/sage/sage/plot/plot3d/list_plot3d.py
sage -t  devel/sage/sage/plot/plot3d/list_plot3d.py         
	 [6.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 6.3 seconds
[mabshoff`@`cicero sage-3.0.4-x86-Linux-fc8]$ ./sage -t  devel/sage/sage/finance/time_series.pyx
sage -t  devel/sage/sage/finance/time_series.pyx            
	 [15.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 15.1 seconds
[mabshoff`@`cicero sage-3.0.4-x86-Linux-fc8]$ ./sage -t devel/sage/sage/functions/special.py 
sage -t  devel/sage/sage/functions/special.py               
	 [8.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 8.2 seconds
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-07-11 18:27:21

The spkg at

http://sage.math.washington.edu/home/mabshoff/numpy-20080104-1.0.4.p5.spkg

fixes the problem.

Cheers,

Michael


---

Comment by was created at 2008-07-11 18:53:12

Resolution: fixed
