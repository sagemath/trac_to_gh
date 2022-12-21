# Issue 648: memory leak: matrix_integer_dense leaks private gmp_randinit_mt(state)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-13 16:01:00

Assignee: mabshoff

Hello folks,

matrix_integer_dense.pyx, lines 2190-2202:

```
##########################################################
# Setup the c-library and GMP random number generators.
# seed it when module is loaded.
from random import randrange
cdef extern from "stdlib.h":
    long random()
    void srandom(unsigned int seed)
k = randrange(0,Integer(2)**(32))
srandom(k)

cdef gmp_randstate_t state
gmp_randinit_mt(state)
gmp_randseed_ui(state,k)
```


So in this particular case we actually seed the random number
generator with a random value. Now my questions:

a) Why do we need randomness here?
b) Why don't we use the global seed? 

See also http://groups.google.com/group/sage-devel/browse_thread/thread/5fe050ae9a2dc373/


---

Comment by mabshoff created at 2007-09-15 00:09:36

Okay, there is a patch for this at

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.4.2-remove-unneeded-gmp_randinit_mt.patch

With the patch Sage startup + quit leads to

```
==30873== LEAK SUMMARY:
==30873==    definitely lost: 0 bytes in 0 blocks.
==30873==      possibly lost: 277,574 bytes in 776 blocks.
==30873==    still reachable: 136,202,587 bytes in 17,438 blocks.
==30873==         suppressed: 0 bytes in 0 blocks.
```


./sage -testall passes.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-15 00:09:36

Changing status from new to assigned.


---

Comment by was created at 2007-09-15 00:21:23

Resolution: fixed
