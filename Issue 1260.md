# Issue 1260: clean up spkg-install for FLINT [flint-0.9-r1075.px]

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-25 04:47:41

Assignee: mabshoff

Toward the end of http://groups.google.com/group/sage-devel/t/7fad3e24f3777d92 Bill says:

```
The new build system for FLINT has the dylib stuff in it already. If
you do make library, it should make a dylib if you are compiling on
Darwin. (If you have other systems you want to compile a dylib instead
of a .so, just edit the file flint_env in the FLINT trunk and send me
the modifications and I'll commit them.)

The only things spkg_install should need to do is:

1) Tell it where GMP is, i.e:

export FLINT_GMP_LIB_DIR=....
export FLINT_GMP_INCLUDE_DIR=....

2) Make sure LD_LIBRARY_PATH has the GMP library path in it (currently
if LD_LIBRARY_PATH is empty FLINT sets it to FLINT_GMP_LIB_DIR,
otherwise it assumes you set it yourself)

3) source flint_env

4) make library

5) Move the library and header files to wherever you need them to be

Everything else should be done by flint_env automatically, including
all the platform specific stuff. If not, let me know and I'll fix it.

Similarly if you are building the test programs, you'd do the above
but with make test instead of make library. There is also make
examples, make tune (only makes the tuning targets at this point,
doesn't run them, and they aren't ready to be used yet), make profiles
(again just makes profiling programs, doesn't do anything with them)
and make all (does all of the above except it doesn't make a library).

Eventually SAGE will want to build FLINT by doing make tune before
make library. But this is not useful yet.

Bill. 
```

and later

```
Michael,

Is there a simple way to either:

1) Use a bash script to parse the existing $LD_LIBRARY_PATH to see if
one of the path strings it contains is equal to $FLINT_GMP_LIB_DIR

2) Add $FLINT_GMP_LIB_DIR to $LD_LIBRARY_PATH if it isn't already in
there (I see how to add it whether or not it is in there, but this
could lead to a duplicate path string)
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-11-25 04:48:51

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-12-06 20:50:59

The new spkg is at

http://sage.math.washington.edu/home/mabshoff/flint-1.0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-06 20:51:11

Merged in 2.9.alpha1.


---

Comment by mabshoff created at 2007-12-06 20:51:11

Resolution: fixed
