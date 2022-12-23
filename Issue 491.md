# Issue 491: gcc 4.3: fix givaro build due to ::memcpy failure

Issue created by migration from https://trac.sagemath.org/ticket/491

Original creator: mabshoff

Original creation time: 2007-08-25 23:16:18

Assignee: was

The givaro spkg released with Sage 2.8.2 doesn't compile with gcc 4.3:

```
Making all in memory
make[4]: Entering directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src/src/kernel/memory'
/bin/sh ../../../libtool --mode=compile g++ -DHAVE_CONFIG_H -I. -I. -I../../.. -I../../.. -I../../../src/kernel/system   -g -O2 -Wall -c givaromm.C
 g++ -DHAVE_CONFIG_H -I. -I. -I../../.. -I../../.. -I../../../src/kernel/system -g -O2 -Wall -c givaromm.C  -fPIC -DPIC -o .libs/givaromm.o
givaromm.C: In static member function 'static void* GivMMFreeList::reallocate(void*, size_t, size_t)':
givaromm.C:191: error: '::memcpy' has not been declared
givaromm.C: In static member function 'static void GivMMFreeList::memcpy(void*, const void*, size_t)':
givaromm.C:205: error: '::memcpy' has not been declared
givaromm.C: In static member function 'static void* GivMMRefCount::reallocate(void*, size_t, size_t)':
givaromm.C:246: error: '::memcpy' has not been declared
givaromm.C:247: error: '::memcpy' has not been declared
givaromm.C:245: warning: suggest explicit braces to avoid ambiguous 'else'
make[4]: *** [givaromm.lo] Error 1
make[4]: Leaving directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src/src/kernel/memory'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src/src/kernel'
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src/src'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src'
make: *** [all-recursive-am] Error 2
```

Including string.h in givaromm.C fixes the problem. 

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-25 23:17:06

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-08-25 23:17:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-08-26 12:50:52

Another suggestion has been made by Patrick Pelissier:

```
For checking of givaro inside the configure, as a work-around,
I suggest including cstdio explicitly before gmp.h.
```

This supposedly will not require workarounds for the gmp.h

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-06 21:02:29

Fix in the new spkg at

http://sage.math.washington.edu/home/mabshoff/givaro-3.2.6.p4.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-06 21:02:46

Resolution: fixed


---

Comment by mabshoff created at 2007-12-06 21:02:46

Merged in 2.9.alpha1.
