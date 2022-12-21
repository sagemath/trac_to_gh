# Issue 3506: I can't build m4ri on the vmware image unless I replace the ctypedef int bit by just an int in the two places it is used.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-06-25 01:38:51

Assignee: was

CC:  malb

The problem:

```
building 'sage.matrix.matrix_mod2_dense' extension
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/usr/local/sage/local//include -I/usr/local/sage/local//include/csage -I/usr/local/sage/devel//sage/sage/ext -I/usr/local/sage/local/include/python2.5 -c sage/matrix/matrix_mod2_dense.c -o build/temp.linux-i686-2.5/sage/matrix/matrix_mod2_dense.o -w -w
sage/matrix/matrix_mod2_dense.c: In function ‘__pyx_pf_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense___init__’:
sage/matrix/matrix_mod2_dense.c:1733: error: ‘bit’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c:1733: error: (Each undeclared identifier is reported only once
sage/matrix/matrix_mod2_dense.c:1733: error: for each function it appears in.)
sage/matrix/matrix_mod2_dense.c:1733: error: expected ‘;’ before ‘__pyx_8’
sage/matrix/matrix_mod2_dense.c:1930: error: ‘__pyx_8’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c: In function ‘__pyx_f_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense_set_unsafe’:
sage/matrix/matrix_mod2_dense.c:2047: error: ‘bit’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c:2047: error: expected ‘;’ before ‘__pyx_3’
sage/matrix/matrix_mod2_dense.c:2061: error: ‘__pyx_3’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c: In function ‘__pyx_f_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense_get_unsafe’:
sage/matrix/matrix_mod2_dense.c:2086: error: ‘bit’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c:2086: error: expected ‘;’ before ‘__pyx_1’
sage/matrix/matrix_mod2_dense.c:2095: error: ‘__pyx_1’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c: In function ‘__pyx_pf_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense__list’:
sage/matrix/matrix_mod2_dense.c:3462: error: ‘bit’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c:3462: error: expected ‘;’ before ‘__pyx_4’
sage/matrix/matrix_mod2_dense.c:3504: error: ‘__pyx_4’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c: In function ‘__pyx_pf_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense__pivots’:
sage/matrix/matrix_mod2_dense.c:4077: error: ‘bit’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c:4077: error: expected ‘;’ before ‘__pyx_4’
sage/matrix/matrix_mod2_dense.c:4164: error: ‘__pyx_4’ undeclared (first use in this function)
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```


Fix attached.   This may have to do with a C namespace clash for some compilers.  On
the vmware sage image we have:

```
root`@`sage:/usr/local/sage# gcc -v
Using built-in specs.
Target: i486-linux-gnu
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --program-suffix=-4.1 --enable-__cxa_atexit --enable-clocale=gnu --enable-libstdcxx-debug --enable-mpfr --enable-checking=release i486-linux-gnu
Thread model: posix
gcc version 4.1.2 20060928 (prerelease) (Ubuntu 4.1.1-13ubuntu5)
```



---

Attachment


---

Comment by mabshoff created at 2008-06-25 02:00:16

While I love a descriptive Summary for trac tickets this is taking it slightly too far :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-25 02:01:37

Fixed Summary slightly and added malb to the CC field since he seems to be the canonical person to review this.

Cheers,

Michael


---

Comment by malb created at 2008-06-25 11:05:18

This was the correct fix until the upgrade of the M4RI package. I claim that this update (libm4ri-20080521.p0) renders this fix unnecessary since the bit got renamed to BIT. Btw.: The analysis is correct it was a C nameclash. I'd say: wontfix but I won't just close the ticket. Which Sage is that btw.?


---

Comment by mabshoff created at 2008-07-02 20:38:43

Resolution: invalid


---

Comment by mabshoff created at 2008-07-02 20:38:43


```
[1:35pm] malb: I vote for closing #3506
[1:35pm] malb: wjp so you reviewed the first two patches and added a third?
[1:36pm] mabshoff: malb: that is what wstein|afk said about 3506, so I am closing it.
```

