# Issue 7166: HP-UX issue. numpy does not understand PA-RISC CPU

Issue created by migration from https://trac.sagemath.org/ticket/7166

Original creator: drkirkby

Original creation time: 2009-10-09 23:22:42

Assignee: tbd

CC:  mkoeppe

Keywords: HP-UX

I tried to build numpy on a HP C3600 (PA-RISC chip, big endian) running HP-UX 11i. It fails with since the code does not know what CPU I have. *If one of the numpy maintainers wants access to the machine, they can have it.* 


```
customize UnixCCompiler
customize UnixCCompiler using build_ext
building 'numpy.core._sort' extension
compiling C sources
C compiler: gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC

compile options: '-Inumpy/core/include -Ibuild/src.hp-ux-B.11.11-9000-785-2.6/numpy/core/include/numpy -Inumpy/core/src -Inumpy/core/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -c'
gcc: build/src.hp-ux-B.11.11-9000-785-2.6/numpy/core/src/_sortmodule.c
In file included from numpy/core/include/numpy/npy_endian.h:22,
                 from numpy/core/include/numpy/ndarrayobject.h:26,
                 from numpy/core/include/numpy/noprefix.h:7,
                 from numpy/core/src/_sortmodule.c.src:29:
numpy/core/include/numpy/npy_cpu.h:49:6: error: #error Unknown CPU, please report this to numpy maintainers with information about your platform (OS, CPU and compiler)
In file included from numpy/core/include/numpy/ndarrayobject.h:26,
                 from numpy/core/include/numpy/noprefix.h:7,
                 from numpy/core/src/_sortmodule.c.src:29:
numpy/core/include/numpy/npy_endian.h:33:10: error: #error Unknown CPU: can not set endianness
In file included from numpy/core/include/numpy/npy_endian.h:22,
                 from numpy/core/include/numpy/ndarrayobject.h:26,
                 from numpy/core/include/numpy/noprefix.h:7,
                 from numpy/core/src/_sortmodule.c.src:29:
numpy/core/include/numpy/npy_cpu.h:49:6: error: #error Unknown CPU, please report this to numpy maintainers with information about your platform (OS, CPU and compiler)
In file included from numpy/core/include/numpy/ndarrayobject.h:26,
                 from numpy/core/include/numpy/noprefix.h:7,
                 from numpy/core/src/_sortmodule.c.src:29:
numpy/core/include/numpy/npy_endian.h:33:10: error: #error Unknown CPU: can not set endianness
error: Command "gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -Inumpy/core/include -Ibuild/src.hp-ux-B.11.11-9000-785-2.6/numpy/core/include/numpy -Inumpy/core/src -Inumpy/core/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -c build/src.hp-ux-B.11.11-9000-785-2.6/numpy/core/src/_sortmodule.c -o build/temp.hp-ux-B.11.11-9000-785-2.6/build/src.hp-ux-B.11.11-9000-785-2.6/numpy/core/src/_sortmodule.o" failed with exit status 1
Error building numpy.

real    0m40.370s
user    0m29.010s
sys     0m8.280s
sage: An error occurred while installing numpy-1.3.0.p2
```




---

Comment by drkirkby created at 2009-12-09 17:21:25

numpy-discussion`@`scipy.org on 9 December 2009 `@` 17:09 GMT


---

Comment by kcrisman created at 2011-02-16 22:32:37

Changing component from porting to AIX or HP-UX ports.


---

Comment by chapoton created at 2020-06-25 13:35:30

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-06-25 13:35:30

close as obsolete ?


---

Comment by mkoeppe created at 2020-06-25 17:11:01

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-06-25 17:21:53

Resolution: invalid
