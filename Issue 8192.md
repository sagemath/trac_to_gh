# Issue 8192: Update PolyBoRi to newest upstream release

Issue created by migration from https://trac.sagemath.org/ticket/8192

Original creator: malb

Original creation time: 2010-02-05 10:59:50

Assignee: tbd

CC:  polybori burcin

* gat parser added
 * Disabled keyboard interrupt handling (but re-raised)
 * Fixed critical bug in normal form
 * Naming convention: `minimalElements` -> `minimal_elements`
 * has_constant_part for variable/monomial
 * `lead/lex_lead/lead_deg/lex_lead_deg` also for Variable/Monomial
 * iterator for literal factorization
 * Added treatment of customizable settings for `BOOST_LIBRARY`,`SHCFLAGS`, `SHCCFLAGS`, and `SHCXXFLAGS`
 * Improved Sun Studio compatibility
 * Fix for hpux (CUDD needs `pwd.h`)
}}}

This should be relatively straight forward then.


---

Comment by PolyBoRi created at 2010-03-12 14:20:29

Changing status from new to needs_review.


---

Comment by PolyBoRi created at 2010-03-12 14:20:29

Burcin and I prepared the Package:

http://sage.math.washington.edu/home/dreyer/spkg/polybori-0.6.4.spkg

Regards,
  Alexander Dreyer


---

Comment by PolyBoRi created at 2010-03-12 14:20:38

Changing assignee from tbd to PolyBoRi.


---

Comment by malb created at 2010-04-05 19:51:20

Looks good.


---

Comment by malb created at 2010-04-05 19:51:20

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-19 21:53:57

Do you know why the spkg is so small?

```
palmieri@sage:~$ ls -l /home/dreyer/spkg/polybori-0.6.4.spkg 
... 2040576 2010-03-12 06:13 /home/dreyer/spkg/polybori-0.6.4.spkg
palmieri@sage:~$ ls -l /home/release/sage-4.3.5/sage-4.3.5/spkg/standard/polybori-0.6.3-20091028.spkg 
... 6825939 2010-02-11 08:56 /home/release/sage-4.3.5/sage-4.3.5/spkg/standard/polybori-0.6.3-20091028.spkg
```

I'm not complaining, but I'm curious.


---

Comment by PolyBoRi created at 2010-04-20 08:33:29

Indeed, the polybori-0-6-3*spkg's contain a clone of PolyBoRi's mercurial repository as well a a mercurial repository of the Sage-related patches,  The polybori-0-6-4.spkg only has the patch repo. 

What is Sage's policy here?

Best regards,
  Alexander


---

Comment by jhpalmieri created at 2010-04-21 16:32:52

I don't think there is a policy, but it seems to be okay to delete an upstream mercurial repository like this.


---

Comment by mhansen created at 2010-04-27 07:34:37

This does not build on Cygwin due to missing libpng12 and libz.  I've posted an spkg which fixes this at

http://sage.math.washington.edu/home/mhansen/cygwin_port/polybori-0.6.4.spkg

Could someone review my changes?  Otherwise, I can make a new ticket for this.


---

Comment by malb created at 2010-04-27 17:15:22

Hi Mike,

I'm afraid your SPKG will need a new ticket since this one was merged in 4.4 already. 

Your SPKG builds fine on sage.math, however I get


```
Exiting Sage (CPU time 0m0.06s, Wall time 0m0.88s).
*** glibc detected *** python: corrupted double-linked list: 0x000000000329b9c0 ***
======= Backtrace: =========
/lib/libc.so.6[0x7fccf4577663]
/lib/libc.so.6[0x7fccf4578ea1]
/lib/libc.so.6(cfree+0x8c)[0x7fccf457cc1c]
/lib/libc.so.6(exit+0xe0)[0x7fccf453a110]
python[0x4baac3]
python(PyErr_PrintEx+0x19a)[0x4bacca]
python(PyRun_SimpleFileExFlags+0x116)[0x4bb926]
python(Py_Main+0x984)[0x416354]
/lib/libc.so.6(__libc_start_main+0xf4)[0x7fccf45231c4]
python[0x415629]
```


which is likely unrelated to your SPKG? I will build a fresh 4.4 to check.


---

Comment by mhansen created at 2010-04-27 17:18:07

Okay, I'll open a new ticket. Shouldn't this ticket have been closed when it was merged into 4.4?


---

Comment by malb created at 2010-04-27 17:21:27

Argh, I mixed it up. No it isn't merged, so no new ticket needed.


---

Comment by malb created at 2010-04-27 17:29:41

SPKG looks good, the bug reported above had nothing to do with the SPKG. Running doctests now, if they pass this should be a positive review.


---

Comment by mhansen created at 2010-04-27 17:31:45

Thanks!


---

Comment by malb created at 2010-04-27 19:17:36

Mhh, can you try your SPKG on sage.math? It seems it does produce a fair amount of segfaults.


---

Comment by mhansen created at 2010-04-27 19:19:16

Sure.


---

Comment by was created at 2010-04-28 19:30:33

Changing status from positive_review to needs_work.


---

Comment by was created at 2010-04-28 19:30:33

given the report of segfaults above, I'm changing this to needs work!


---

Comment by burcin created at 2010-04-28 19:48:02

Replying to [comment:18 was]:
> given the report of segfaults above, I'm changing this to needs work!

Or you could merge the package which got a positive review and we move the Cygwin problems to a different ticket.

http://sage.math.washington.edu/home/dreyer/spkg/polybori-0.6.4.spkg


---

Comment by mhansen created at 2010-04-28 21:57:49

Yep, I think using that one would be fine for now.  I'll look into these segfaults and make a new ticket.


---

Comment by mhansen created at 2010-04-28 21:57:49

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-04-28 21:57:59

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-29 00:25:41

Resolution: fixed


---

Comment by wjp created at 2010-04-29 12:41:02

Both the 0.6.4.spkgs here give those crashes reported above, but only once in every 10-15 runs.

Valgrind shows invalid reads/writes on exit pointing to polybori:


```
==14880== Invalid read of size 4
==14880==    at 0x30CE3642: __tcf_1 (sp_counted_base_gcc_x86.hpp:50)
==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)
==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)
==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)
==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)
==14880==    by 0x4164C4: Py_Main (main.c:142)
==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)
==14880==  Address 0x3225a538 is not stack'd, malloc'd or (recently) free'd
==14880== 
==14880== Invalid read of size 8
==14880==    at 0x30CE365C: __tcf_1 (CCuddCore.h:208)
==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)
==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)
==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)
==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)
==14880==    by 0x4164C4: Py_Main (main.c:142)
==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)
==14880==  Address 0x31a599e8 is 8 bytes inside a block of size 64 free'd
==14880==    at 0x4C2216E: operator delete(void*) (vg_replace_malloc.c:346)
==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)
==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)
==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)
==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)
==14880==    by 0x4164C4: Py_Main (main.c:142)
==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)
==14880== 
==14880== Invalid write of size 8
==14880==    at 0x30CE3667: __tcf_1 (CCuddCore.h:208)
==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)
==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)
==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)
==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)
==14880==    by 0x4164C4: Py_Main (main.c:142)
==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)
==14880==  Address 0x31a599e8 is 8 bytes inside a block of size 64 free'd
==14880==    at 0x4C2216E: operator delete(void*) (vg_replace_malloc.c:346)
==14880==    by 0x56FEB48: exit (in /lib64/libc-2.9.so)
==14880==    by 0x4B9531: handle_system_exit (pythonrun.c:1716)
==14880==    by 0x4B9738: PyErr_PrintEx (pythonrun.c:1126)
==14880==    by 0x4BA334: PyRun_SimpleFileExFlags (pythonrun.c:1035)
==14880==    by 0x4164C4: Py_Main (main.c:142)
==14880==    by 0x56E95E3: (below main) (in /lib64/libc-2.9.so)
```



---

Comment by burcin created at 2010-04-29 13:10:05

Hi Willem Jan,

The crashes are probably caused by the fact that I disabled the code that statically links polybori in the new package. IIRC, we were doing that exactly because of these double free errors. We tested the new package on different platforms, and didn't see the crashes, so we assumed the problem was fixed.

I don't have time to reproduce the problem, or test new packages at the moment. Can you try enabling the static build and try again?

From the diff of the changes (of an earlier version of the package in Alexander Dreyer's home dir), this looks like the relevant change:


```
diff --git a/patches/SConstruct b/patches/SConstruct
--- a/patches/SConstruct
+++ b/patches/SConstruct
@@ -561,7 +581,7 @@
 gb_src = [GBPath('src', source) for source in gb_src]
 if not(external_m4ri):
    gb_src += m4ri
-gb=env.StaticLibrary(GBPath('groebner'), gb_src+[libpb])
+gb=env.StaticLibrary(GBPath('groebner'), gb_src)#+[libpb])
 
 #print "gb:", gb, dir(gb)
 #sometimes l seems to be boxed by a list
```



BTW, this also looks suspect to me:


```
diff --git a/patches/SConstruct b/patches/SConstruct
--- a/patches/SConstruct
+++ b/patches/SConstruct
@@ -327,7 +350,7 @@
 Help(opts.GenerateHelpText(env))
 
 have_l2h = have_t4h = False
-external_m4ri = True
+external_m4ri = False
 
 if not env.GetOption('clean'):
     conf = Configure(env)
```


Many thanks for looking into this.


---

Comment by PolyBoRi created at 2010-04-29 13:22:57

Hi Burcin,

I think, we removed  the call of` remove_dylib`  from `spkg-install`. So reintroducing `remove_dylib` may fit it already.

Regards,

  Alexander Dreyer


---

Comment by malb created at 2010-04-29 13:26:43

> BTW, this also looks suspect to me:
> 
> {{{
> diff --git a/patches/SConstruct b/patches/SConstruct
> --- a/patches/SConstruct
> +++ b/patches/SConstruct
> `@``@` -327,7 +350,7 `@``@`
>  Help(opts.GenerateHelpText(env))
>  
>  have_l2h = have_t4h = False
> -external_m4ri = True
> +external_m4ri = False
>  
>  if not env.GetOption('clean'):
>      conf = Configure(env)
> }}}

I agree, that this wrong and should be reverted (we really want the external M4RI)


---

Comment by PolyBoRi created at 2010-04-29 13:34:23

Hi malb,

right, but this is only the inital value of an internal variable. Later in the Sconstruct file, external_m4ri will be set to True, if the library is found.

Regards,

  Alexander Dreyer


---

Comment by wjp created at 2010-04-29 14:13:40

I don't have time to extensively test right now, so I tried both reverting the patch that Burcin gave above and reintroducing remove_dylib at the same time. That fixed the problems.

So you're definitely on the right track, but I'll leave it to you to figure out what exactly needs to be changed for a new spkg :-)


---

Comment by PolyBoRi created at 2010-04-29 14:18:48

Hi Willem Jan,

I changed than remove_dynlib only at:

!http://sage.math.washington.edu/home/dreyer/spkg/polybori-0.6.4-p1.spkg

Is this enough to fix the problem?

Since I was not able to reproduce the problem: Can you test it? (How do you run it?)

Best regards,


  Alexander Dreyer


---

Comment by wjp created at 2010-04-29 15:18:34

Hi Alexander,

Yes, I don't get the errors anymore with that package. (After renaming the spkg to polybori-0.6.4.p1.spkg and the directory inside it to match the spkg filename.)

I test it by running sage through valgrind and seeing if there are any errors on exit in polybori files, since the actual crashes happen here only once every 10-15 runs or so.


Still I can't help but wonder if there's something subtle going wrong with sage's interface to polybori or in polybori itself on exit to require static linking. Maybe something like multiple libraries sharing a global memory manager and each of them trying to clean up global structures on quit or something similar...


Thanks!
-Willem Jan


---

Comment by mvngu created at 2010-04-29 19:41:59

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/ff294013a41ea05c):



Sage 4.4.1.alpha2 contains two PolyBoRi spkg's:

 * polybori-0.6.3-20091028.spkg
 * polybori-0.6.4.spkg

I think polybori-0.6.4.spkg is the newer one, so I deleted the other one from `SAGE_ROOT/spkg/standard/`. Here's a diff between the `spkg-install` of polybori-0.6.3-20091028.spkg and polybori-0.6.4.spkg:


```diff
[mvngu@sage mvngu]$ diff -Naur polybori-0.6.3-20091028/spkg-install polybori-0.6.4.p0/spkg-install 
--- polybori-0.6.3-20091028/spkg-install	2009-05-17 10:31:16.000000000 -0700
+++ polybori-0.6.4.p0/spkg-install	2010-04-29 07:10:46.000000000 -0700
@@ -6,14 +6,14 @@
    exit 1
 fi
 
-PBDIR=polybori-0.6
+PBDIR=polybori-0.6.4
 WORKDIR=${PWD}/src
 SCONS=scons
 
 # For some strange reason the installed boost in $SAGE_LOCAL causes 
 # make install failures, so copy it over. 
-mkdir src/boost_1_34_1.cropped
-cp -r $SAGE_LOCAL/include/boost src/boost_1_34_1.cropped
+#mkdir src/boost_1_34_1.cropped
+#cp -r $SAGE_LOCAL/include/boost src/boost_1_34_1.cropped
 BOOSTDIR=boost_1_34_1.cropped
 
 patch() 
@@ -26,9 +26,6 @@
 
     cp patches/SConstruct src/${PBDIR}/SConstruct
     cp patches/PyPolyBoRi.py src/${PBDIR}/pyroot/polybori
-
-    # workaround so will build on cygwin
-    cp patches/cpu_stats.c src/${PBDIR}/Cudd/util/cpu_stats.c
 }
 
 
@@ -68,7 +65,7 @@
 
 remove_dylib()
 {
-    # linking dynmic libraries causes segfaults at exit (see #2822)
+    # linking dynamic libraries causes segfaults at exit (see #2822)
     if [ `uname` = "Darwin" ]; then
         rm -f $SAGE_LOCAL/lib/libpolybori.dylib
         rm -f $SAGE_LOCAL/lib/libpboriCudd.dylib
@@ -101,9 +98,3 @@
 echo "Removing dynamic libraries..."
 remove_dylib
 echo "Done removing dynamic libraries."
-
-# force a rebuild of the PolyBoRi extension
-if [ -f $SAGE_ROOT/devel/sage/sage/rings/polynomial/pbori.pyx ]; then
-    touch $SAGE_ROOT/devel/sage/sage/rings/polynomial/pbori.pyx
-fi
-
```


I replaced polybori-0.6.4.spkg with

http://sage.math.washington.edu/home/mvngu/spkg/standard/polybori/polybori-0.6.4.p0.spkg

The latter spkg restores the command "remove_dynlib". I then built Sage 4.4.1.alpha2 from scratch on sage.math with polybori-0.6.4.p0.spkg. Doctesting resulted in the following failure:


```sh
[mvngu@sage sage-4.4.1.alpha2]$ ./sage -t -long local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/misc/misc.py
sage -t -long "local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/misc/misc.py"
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/misc/misc.py", line 109:
    sage: print "ignore this";  sage.server.misc.find_next_available_port('', 9000, verbose=False)   # random output -- depends on network
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        print "ignore this";  sage.server.misc.find_next_available_port('', Integer(9000), verbose=False)   # random output -- depends on network###line 109:
    sage: print "ignore this";  sage.server.misc.find_next_available_port('', 9000, verbose=False)   # random output -- depends on network
      File "/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/lib/python/site-packages/sage/server/misc.py", line 105, in find_next_available_port
        for port in range(start, start+max_tries+1):
      File "element.pyx", line 1271, in sage.structure.element.RingElement.__add__ (sage/structure/element.c:10830)
      File "coerce.pyx", line 765, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)
    TypeError: unsupported operand parent(s) for '+': '<type 'str'>' and 'Integer Ring'
```


I have wrapped up a sage.math binary of this patched version of Sage 4.4.1.alpha2. You can find it at

http://sage.math.washington.edu/home/mvngu/sage.math-bin/sage-4.4.1.alpha2-patched-sage.math.washington.edu-x86_64-Linux.tar.gz

I removed the directory

`SAGE_ROOT/devel/sage-main/doc/en/thematic_tutorials/`

and wrapped up a source distribution, which can be found at

http://sage.math.washington.edu/home/mvngu/sage-src/sage-4.4.1.alpha2-patched.tar


---

Comment by wjp created at 2010-04-30 12:32:59

I'm wondering if we should create a new ticket for this new polybori p0 spkg.
In any case, I tested it, and it works fine for me.


---

Comment by wjp created at 2010-04-30 12:54:11

I created ticket #8830 for the p0 spkg.
