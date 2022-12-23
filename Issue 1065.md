# Issue 1065: sage -sdist nukes libcsage.so

Issue created by migration from https://trac.sagemath.org/ticket/1065

Original creator: mabshoff

Original creation time: 2007-11-02 04:12:58

Assignee: was

CC:  craigcitro

Right after a *sage -sdist* the following happens. *A sage -b* rebuilds libcsage.so and everything works fine again (well, at least Sage starts :))

```
./sage -t  devel/sage-main/sage/groups/perm_gps/permgroup_element.py
sage -t  devel/sage-main/sage/groups/perm_gps/permgroup_element.pyTraceback (most recent call last):
  File ".doctest_permgroup_element.py", line 1, in <module>
    from sage.all_cmdline import *;
  File "/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/lib/python2.5/site-packages/sage/all_cmdline.py", line 14, in <module>
    from sage.all import *
  File "/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/lib/python2.5/site-packages/sage/all.py", line 45, in <module>
    from sage.rings.memory import pmem_malloc
ImportError: libcsage.so: cannot open shared object file: No such file or directory

         [0.1 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-main/sage/groups/perm_gps/permgroup_element.py
Total time for all tests: 0.1 seconds
mabshoff@sage:/tmp/Work-mabshoff/sage-2.8.11.alpha0$ ./sage -b

----------------------------------------------------------
sage: Building and installing modified SAGE library files.


Installing c_lib
gcc -o src/convert.os -c -O2 -g -fPIC -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/python2.5 -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/NTL -Iinclude src/convert.c
gcc -o src/interrupt.os -c -O2 -g -fPIC -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/python2.5 -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/NTL -Iinclude src/interrupt.c
gcc -o src/mpn_pylong.os -c -O2 -g -fPIC -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/python2.5 -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/NTL -Iinclude src/mpn_pylong.c
gcc -o src/mpz_pylong.os -c -O2 -g -fPIC -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/python2.5 -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/NTL -Iinclude src/mpz_pylong.c
gcc -o src/stdsage.os -c -O2 -g -fPIC -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/python2.5 -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/NTL -Iinclude src/stdsage.c
gcc -o src/gmp_globals.os -c -O2 -g -fPIC -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/python2.5 -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/NTL -Iinclude src/gmp_globals.c
g++ -o src/ZZ_pylong.os -c -fPIC -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/python2.5 -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/NTL -Iinclude src/ZZ_pylong.cpp
g++ -o src/ntl_wrap.os -c -fPIC -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/python2.5 -I/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/NTL -Iinclude src/ntl_wrap.cpp
In file included from /tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/python2.5/Python.h:8,
                 from include/ntl_wrap.h:28,
                 from src/ntl_wrap.cpp:5:
/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/include/python2.5/pyconfig.h:932:1: warning: "_POSIX_C_SOURCE" redefined
In file included from /usr/lib/gcc/x86_64-linux-gnu/4.1.2/../../../../include/c++/4.1.2/x86_64-linux-gnu/bits/os_defines.h:39,
                 from /usr/lib/gcc/x86_64-linux-gnu/4.1.2/../../../../include/c++/4.1.2/x86_64-linux-gnu/bits/c++config.h:35,
                 from /usr/lib/gcc/x86_64-linux-gnu/4.1.2/../../../../include/c++/4.1.2/iostream:43,
                 from src/ntl_wrap.cpp:1:
/usr/include/features.h:150:1: warning: this is the location of the previous definition
g++ -o libcsage.so -shared src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/tmp/Work-mabshoff/sage-2.8.11.alpha0/local/lib -lntl -lgmp -lpari
running install
running build
running build_py
running build_ext
running build_scripts
running install_lib
running install_scripts
changing mode of /tmp/Work-mabshoff/sage-2.8.11.alpha0/local/bin/dsage_server.py to 755
changing mode of /tmp/Work-mabshoff/sage-2.8.11.alpha0/local/bin/dsage_worker.py to 755
changing mode of /tmp/Work-mabshoff/sage-2.8.11.alpha0/local/bin/dsage_setup.py to 755
running install_egg_info
Removing /tmp/Work-mabshoff/sage-2.8.11.alpha0/local/lib/python2.5/site-packages/sage-0.0.0-py2.5.egg-info
Writing /tmp/Work-mabshoff/sage-2.8.11.alpha0/local/lib/python2.5/site-packages/sage-0.0.0-py2.5.egg-info

real    0m13.298s
user    0m8.865s
sys     0m2.356s
mabshoff@sage:/tmp/Work-mabshoff/sage-2.8.11.alpha0$ ./sage -t  devel/sage-main/sage/groups/perm_gps/permgroup_element.py
sage -t  devel/sage-main/sage/groups/perm_gps/permgroup_element.py
**********************************************************************
File "permgroup_element.py", line 323:
    sage: g([0,1,2,3,4])
Expected:
    [1, 2, 3, 0, 5, 4]
Got:
    [1, 2, 0, 4, 3]
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_7
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_permgroup_element.py
         [3.0 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-main/sage/groups/perm_gps/permgroup_element.py
Total time for all tests: 3.0 seconds
mabshoff@sage:/tmp/Work-mabshoff/sage-2.8.11.alpha0$                    
```


Cheers,

Michael


---

Comment by jdemeyer created at 2013-06-13 12:41:36

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-06-13 12:41:36

Works for me.


---

Comment by jdemeyer created at 2013-06-13 12:41:46

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-06-19 12:20:50

Resolution: worksforme
