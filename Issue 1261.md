# Issue 1261: parallel "sage -br"

Issue created by migration from https://trac.sagemath.org/ticket/1261

Original creator: was

Original creation time: 2007-11-25 05:39:18

Assignee: was*

It would be very desirable for "sage -br" to take advantage of multi-processor and multi-core machines automatically.

The following irc session describes an idea for a way to easily implement this.
The main idea is to use the dry_run option to setup(...) in setup.py, capture
the output of the dry_run, then run those commands in parallel.


```
[9:21pm] was_: When "sage -br" runs we first (with custom code I wrote) run cython on a bunch of files -- for this the order is probably important.
[9:21pm] was_: (??)
[9:22pm] was_: Anyway, after that, distutils runs gcc or g++ on a large number of files.  I think for that the order doesn't matter much.
[9:22pm] cwitty: The order of running Cython should not be important.
[9:22pm] was_: Are you sure?
[9:22pm] mabshoff: ok
[9:22pm] was_: There is a dry_run option to the setup function in devel/sage/setup.py.
[9:22pm] cwitty: (Cython depends on source files, like .pxd; but I'm pretty sure it doesn't depend on the generated .c or .cpp files.)
[9:23pm] was_: cwitty -- I think you're right.
[9:23pm] mabshoff: each file cython compiles is a dynmaic library?
[9:23pm] was_: Definitely things are easier if you are.
[9:23pm] cwitty: mabshoff, yes.
[9:23pm] was_: cython just makes .c/.cpp/.h files as output; that's it.
[9:23pm] was_: And everything is dynamic.
[9:23pm] mabshoff: Then it shouldn't have compile time dependencies.
[9:23pm] was_: Anyway, back to my idea.
[9:23pm] mabshoff: link time at import, but that doesn't matter.
[9:23pm] was_: (There are possibly some mild dependencies since multiple files are combined to make one dynamic library in some cases.)
[9:24pm] was_: Anyway, back to my idea.
[9:24pm] was_: If you look at devel/sage/setup.py, and put dry_run=True as the last option to the huge setup(...) function,
[9:24pm] was_: then distutils will simply print out all the gcc commands it *would* run.
[9:24pm] was_: But it doesn't run thme.
[9:24pm] mabshoff: I see where you are going 
[9:25pm] was_: So my crazy idea is to run setup once as a dry_run, capture all the output, divide it up, do the gcc's in parallel, then run distutils again with dry_run=False,
[9:25pm] was_: which will be fast.
[9:25pm] mabshoff:
[9:25pm] mabshoff: Let's hope it works.
[9:25pm] was_: I have no idea if it would really work.
[9:25pm] mabshoff: Even then we could also create a makefile from cython info and run parallel make on that.
[9:26pm] was_: If we wanted, though it seems hardly necessary.
[9:26pm] mabshoff: KISS
[9:26pm] was_: yep.
[9:26pm] was_: Make is pretty KISS though, at least the way we're thinking of using it.
[9:26pm] was_: KISS was why the spkg build system uses make.
[9:27pm] mabshoff:
[9:27pm] mabshoff: I just got a timeout with -long running doctests.
[9:27pm] mabshoff: Maybe we should disable TIMEOUT with -long
[9:27pm] was_: There should be a timeout but it should be way longer.
[9:27pm] mabshoff: ok
[9:27pm] was_: E.g., David Joyner put an annoying #long doctest in once that took *days* to run.
[9:27pm] was_: Very annoying.
[9:27pm] was_: It was good that there was a timeout.
[9:28pm] was_: I asked him about it and he said it was a "record breaking" computation...
[9:28pm] mabshoff:
[9:28pm] mabshoff: I think the doctest finishes, but then python realises that the TIMEOUT was exceeded.
[9:29pm] was_: that sounds dumb.
[9:29pm] mabshoff:
[9:29pm] mabshoff: I set my timeout to 30 minutes for now on my copy.
[9:29pm] was_: I just did some tests with my parallel "sage -br" above and it looks very promising.
[9:30pm] mabshoff: Is it going in 2.8.14? *ducks*
[9:30pm] was_: no
[9:30pm] was_: I want to release 2.8.14 in an hour.
[9:30pm] mabshoff: I thought so.
[9:33pm] was_: For smaller files running cython takes longer than gcc.
[9:33pm] was_: E.g., I just tested on sage/libs/cremona/*.pyx, and it takes < 4 seconds to run GCC and nearly 12 seconds to run Cython.
[9:33pm] mabshoff: ok
[9:33pm] was_: Maybe we should write Cython in Cython (ducks)
[9:34pm] mabshoff: my thoughts exactly.
[9:34pm] mabshoff: For 10% of the code it would probably be worth it for performance reasons.
[9:34pm] mabshoff: Maybe you should suggest it to Robert.
[9:34pm] was_: But from the point of view of parallel sage -br, it just means we need to do that in parallel too...
[9:34pm] was_: I.e., both are worth doing.
[9:35pm] mabshoff: Yep,.
[9:35pm] was_: First should be the gcc code.
```



---

Comment by gfurnish created at 2008-03-03 02:17:55

Changing assignee from was* to gfurnish.


---

Comment by gfurnish created at 2008-03-03 02:17:55

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-03 08:23:52

The plan is to replace python distutils with scons for cython, etc.


---

Comment by gfurnish created at 2008-03-17 02:48:13

I built a new build system for this as scons was inadequate.  An alpha version is available that does parallel build all (so it is a full rebuild every time).  Set SAGE_BUILD_THREADS to set the number of threads, which defaults to 4.  Download at: http://sage.math.washington.edu/home/gfurnish/misc/build.tar


---

Attachment

Pbuild extcode repo


---

Comment by gfurnish created at 2008-03-23 12:05:10

PBuild for extcode requires glib to work correctly.  Obtain at #2436.


---

Attachment

This file is to be applied on top of the first patch.


---

Attachment

Apply on top of the 2nd patch


---

Comment by mabshoff created at 2008-03-23 20:52:55

A couple remarks:

 * the CPUID asm code is x86 specific
 * I don't understand what the option parsing code has to do in the build system? 
 * class enviroment ought to be class environment
 * there ought to be spaces between defs 
 * documentation in general is missing, but we agreed that it would be added past the review
 * how much code duplication is going on here with code like ptest?

I need to take a closer look to see what the code actually does.

Cheers,

Michael


---

Comment by gfurnish created at 2008-03-23 21:26:30

1) I fully realize the CPUID asm code is x86 specific, which is why its not fully implemented yet (or used anywhere)
2) The option parsing code doesn't have much to do with the build system other then I needed an option parser and this seemed like a good place to put it.  It doesn't have any dependencies, so we could easily remove it.  I envision a whole suite here though replacing sage-sage and friends, but maybe thats a bad idea?
3) Will run search and replace
4) Agreed
5) Right
6) There is a fair ammount of code duplication in ptest, which is why I plan on eventually removing ptest and building it into the build suite.


---

Comment by mabshoff created at 2008-03-23 22:02:52

re option parser: sure, but that code ought to go into local/bin and then when you build code it should call the build system, not the other way around. It is also debatable how much of sage-sage can be written in python since Python is not a dependency of Sage.

re code duplication: eventually we need to factor out common code, but that is post-merge if you ask me.

re cpuid: yeah, I figured that much. DSage actually does some CPUID, too, via python's build in functions. So maybe there can be some common ground, too.

Cheers,

Michael


---

Comment by gfurnish created at 2008-03-24 00:06:59

apply over 3rd patch


---

Attachment

Merged trac_1261_extcode.patch, trac_1261_extcode_2.patch, trac_1261_extcode_3.patch and trac_1261_extcode_4.patch in Sage 2.11.alpha1. Those patches are to the extcode repo and are still subject to review. 

Cheers,

Michael


---

Attachment

trac_1261_extcode_5.patch looks good. Merged in Sage 2.11.rc0

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-05 18:02:24

Linker trouble on OSX 10.5:

```
cython --embed-positions --incref-local-binop -I. -o sage/matrix/matrix_rational_sparse.c 
sage/matrix/matrix_rational_sparse.pyx
Undefined symbols:
  "_PyType_IsSubtype", referenced from:
      _mpz_set_pylong in mpz_pylong.o
  "_PyExc_KeyboardInterrupt", referenced from:
      _PyExc_KeyboardInterrupt$non_lazy_ptr in interrupt.o
  "_PyErr_SetString", referenced from:
      _sig_handle_sigfpe in interrupt.o
      _sig_handle_sigbus in interrupt.o
      _sig_handle_sigsegv in interrupt.o
      _sage_signal_handler in interrupt.o
      _sage_signal_handler in interrupt.o
      _sage_signal_handler in interrupt.o
      _sage_signal_handler in interrupt.o
  "_PyTuple_New", referenced from:
      _init_global_empty_tuple in stdsage.o
  "_PyInt_FromLong", referenced from:
      _mpz_get_pyintlong in mpz_pylong.o
  "_PyObject_InitVar", referenced from:
      _mpz_get_pylong in mpz_pylong.o
  "_PyExc_RuntimeError", referenced from:
      _PyExc_RuntimeError$non_lazy_ptr in interrupt.o
  "__PyErr_BadInternalCall", referenced from:
      _mpz_set_pylong in mpz_pylong.o
  "_main", referenced from:
      start in crt1.10.5.o
  "_PyObject_Malloc", referenced from:
      _mpz_get_pylong in mpz_pylong.o
  "_PyLong_Type", referenced from:
      _PyLong_Type$non_lazy_ptr in mpz_pylong.o
ld: symbol(s) not found
collect2: ld returned 1 exit status
gcc /Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/mpn_pylong.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/convert.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/stdsage.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/ntl_wrap.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/gmp_globals.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/interrupt.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/ZZ_pylong.o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/src/mpz_pylong.o 
-O2 -g -shared -fno-strict-aliasing -L/Users/mabshoff/sage-3.0.alpha1/local/lib  
-lcsage  -lntl  -lgmp  -lpari  -lstdc++  -lntl  -o 
/Users/mabshoff/sage-3.0.alpha1/devel/sage-main/c_lib/libcsage.so
cython --embed-positions --incref-local-binop -I. -o sage/libs/ntl/ntl_GF2X.c 
sage/libs/ntl/ntl_GF2X.pyx
```


The output should not be called "libcsage.so", but "libcsage.dylib" on OSX. You also seem be be missing libpython.

Cheers,

Michael


---

Comment by gfurnish created at 2008-04-06 04:58:49

darwin


---

Attachment

trac_1261_extcode_6.patch looks good to me. Merged in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-06 06:02:52

#2346 touches setup.py:

```
diff -r 767784c4ad52 -r 4f98891c4496 setup.py
--- a/setup.py  Sat Apr 05 22:40:57 2008 -0500
+++ b/setup.py  Sat Apr 05 22:55:32 2008 -0700
@@ -1391,6 +1391,7 @@ code = setup(name        = 'sage',
                      'sage.schemes.hyperelliptic_curves',

                      'sage.server',
+                     'sage.server.simple',
                      'sage.server.server1',
                      'sage.server.notebook',
                      'sage.server.notebook.compress',
```

But since this is only packages I guess pbuild is not affected.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-04-08 10:30:12

Merged trac_1261_extcode_7b.patch and trac_1261_extcode_8.patch into Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-08 10:31:13

trac_1261_local_1b.patch is no good as is. I will also not switch the default build system to pbuild without

 * some more testing
 * any documentation since people who add extensions do need to know how to do it

Cheers,

Michael


---

Attachment

Merged trac_1261_extcode_9.patch in Sage 3.0.alpha3


---

Attachment


---

Attachment


---

Comment by gfurnish created at 2008-04-10 07:02:36

Ignore the duplicate local_2 patch


---

Comment by mabshoff created at 2008-04-11 23:52:20

FYI: #2394 add a new extension to setup.py

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-20 05:44:06

Merged trac_1261_extcode_10.patch in Sage 3.0.rc0


---

Attachment


---

Comment by mabshoff created at 2008-04-27 03:50:46

Resolution: fixed


---

Comment by mabshoff created at 2008-04-27 03:50:46

Merged trac_1261_extcode_11.patch in Sage 3.0.1.alpha1


---

Comment by mabshoff created at 2008-04-27 03:52:16

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-04-27 03:52:16

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-04-27 03:52:16

oops, I didn't mean to close this ;(


---

Attachment

SAGE_PBUILD OPTION


---

Comment by mabshoff created at 2008-04-30 06:17:21

Merged trac_1261_local1.patch in Sage 3.0.1.alpha1. "sage -b" in its various versions as well as "sage -clone" keeps working with SAGE_PBUILD=no, so more testing with SAGE_PBUILD=yes is needed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-01 10:28:56

The patch set works for me. While there are still potential issues with more exotic, but not yet supported arches this is good to go. Positive review. Follow up will be more documentation, but since this ticket is already so crowded those will be new tickets.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-01 10:29:10

Resolution: fixed


---

Comment by mabshoff created at 2008-05-01 10:29:10

Merged in Sage 3.0.1.alpha1
