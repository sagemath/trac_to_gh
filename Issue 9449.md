# Issue 9449: The summary printed after running doctests is inaccurate.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-07-07 19:57:20

Assignee: mvngu

CC:  simonking jhpalmieri mpatel leif

The following shows a summary of a doctest failures. They were actually observed on a Solaris machine, but that is unlikely to be relevant. After building Sage


```
$ make ptestlong
```


was executed. 

 * 5 of the 6 doctest failures in the summary have 0 tests failing.
 * BSD.py is the only one of the 6 doctest failures which has a non-zero number of failures. 


```

The following tests failed:

    sage -t     -long devel/sage/doc/fr/tutorial/programming.rst # 0 doctests failed
    sage -t     -long devel/sage/sage/schemes/plane_curves/constructor.py # 0 doctests failed
    sage -t     -long devel/sage/sage/schemes/elliptic_curves/BSD.py # 1 doctests failed
    sage -t     -long devel/sage/sage/parallel/decorate.py # 0 doctests failed
    sage -t     -long devel/sage/sage/libs/galrep/wrapper.pyx # 0 doctests failed
----------------------------------------------------------------------
Total time for all tests: 3990.8 seconds 
```


In the case of one of the tests, it would appear from the log that it actually passed 


```
sage -t     -long devel/sage/sage/parallel/decorate.py
     [44.0 s] 
```


This is pretty damn serious, as it means we can not rely on the doctest results. 

 == Hardware and software used ==
  * sage-4.5.alpha4
  * A Sun T5240
  * 2 x 8 core, 64-thread UltraSPARC T2+ 1167 MHz
  * 32 GB RAM
  * Solaris 10 update 7 (05/09)
  * t2.math.washtington.edu
  * gcc 4.4.1 configured to use both the Sun linker and assembler.
  * MD5 checksum of matplotlib-1.0.0.spkg was cb9f3cb0ec3da550d2d67ea7e8b6094f
  * 32-bit build (This is the default). The environment variable `SAGE64` was *not* used.


---

Comment by drkirkby created at 2010-07-07 19:59:01

Results from long doctests on t2.math.washington.edu (Solaris 10, UltraSPARC CPUs)


---

Attachment

Could you try with patches #8641, #9243, #9316 to the doctest framework? They clean up and fix parts of the error handling.

If they don't fix it yet, I can give you a patch which adds some extra debugging info to track this down.


---

Comment by drkirkby created at 2010-07-07 20:05:21

I've attached a log. 

Also corrected something which was cut and pasted from another ticket


---

Comment by drkirkby created at 2010-07-07 20:14:34

Replying to [comment:1 wjp]:
> Could you try with patches #8641, #9243, #9316 to the doctest framework? They clean up and fix parts of the error handling.

Yes. The only problem I have is that these test failures are not always reproducible. Tests which failed when I run 

`$ make ptestlong` 

actually passed later. There's a report from John H Palmieri on sage-release of `devel/sage/sage/misc/trace.py` failing for him three times on this machine, then working. This makes any sort of testing difficult, and means it will be hard for me to know if s #8641, #9243, #9316 really solve the problem or not. But I will try them and report back later. 
 
> If they don't fix it yet, I can give you a patch which adds some extra debugging info to track this down.

OK, thank you. 

I know there was a recent patch to the doctesting to remove spurious errors about files not found - #9316. I don't know if these could be related or not. 

I've got other strange results from doctests too, but I'll put that on another ticket. 

Dave


---

Comment by drkirkby created at 2010-07-07 20:46:39

I was unable to apply the last patch cleanly - the first two were ok. 


```
kirkby`@`t2:[/tmp/kirkby/sage-4.5.alpha4/local/bin] $ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8641/trac_8641-doctest_exit_codes.3.patch
adding trac_8641-doctest_exit_codes.3.patch to series file
kirkby`@`t2:[/tmp/kirkby/sage-4.5.alpha4/local/bin] $ hg qpush
applying trac_8641-doctest_exit_codes.3.patch
now at: trac_8641-doctest_exit_codes.3.patch
kirkby`@`t2:[/tmp/kirkby/sage-4.5.alpha4/local/bin] $ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9243/trac_9243.patch
adding trac_9243.patch to series file
kirkby`@`t2:[/tmp/kirkby/sage-4.5.alpha4/local/bin] $ hg qpush
applying trac_9243.patch
now at: trac_9243.patch
kirkby`@`t2:[/tmp/kirkby/sage-4.5.alpha4/local/bin] $ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9316/scripts9316_timeout_rebased.patch
adding scripts9316_timeout_rebased.patch to series file
kirkby`@`t2:[/tmp/kirkby/sage-4.5.alpha4/local/bin] $ hg qpush
applying scripts9316_timeout_rebased.patch
patching file sage-doctest
Hunk #1 FAILED at 18
1 out of 2 hunks FAILED -- saving rejects to file sage-doctest.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh scripts9316_timeout_rebased.patch
kirkby`@`t2:[/tmp/kirkby/sage-4.5.alpha4/local/bin] $ hg status
kirkby`@`t2:[/tmp/kirkby/sage-4.5.alpha4/local/bin] $ hg log | more
changeset:   1541:6510dc91cc05
tag:         scripts9316_timeout_rebased.patch
tag:         qtip
tag:         tip
user:        Willem Jan Palenstijn <wpalenst`@`math.leidenuniv.nl>
date:        Tue Jul 06 22:58:13 2010 +0200
summary:     #9316: Add exit code 64 for time out to doctests

changeset:   1540:6e69aa36dd4d
tag:         trac_9243.patch
user:        Dan Drake <drake`@`kaist.edu>
date:        Wed Jun 16 13:48:32 2010 +0900
summary:     trac 9243: sage-doctest should use powers of 2 for return codes

changeset:   1539:08d8519d03dc
tag:         trac_8641-doctest_exit_codes.3.patch
tag:         qbase
user:        Mitesh Patel <qed777`@`gmail.com>
date:        Wed Jun 16 00:06:03 2010 -0700
summary:     trac 8641: return nonzero code if tests fail.  Dan Drake, John Palmieri
```



---

Comment by wjp created at 2010-07-07 20:49:44

You're missing the second patch at #9243.


---

Comment by drkirkby created at 2010-07-07 21:19:50

Replying to [comment:5 wjp]:
> You're missing the second patch at #9243.

Thank you. I've applied them all now and started the doctests, but I feel tired tonight and are going to sleep now.  So I doubt I'll post the results for a few hours yet. 
 

Dave


---

Comment by drkirkby created at 2010-07-08 08:08:55

Here's the results after applying #8641, #9243, #9316. As you can see, there are still tests which fail with 0 doctest failures (These results are again on the Sun T5240 t2.math.washington.edu, which is the same as before). 


```

sage -t  -long devel/sage/sage/modular/ssmod/ssmod.py
         [3001.1 s]
sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
         [3137.3 s]
 
----------------------------------------------------------------------

The following tests failed:

        sage -t  -long devel/sage/doc/en/constructions/number_fields.rst # 0 doctests failed
        sage -t  -long devel/sage/sage/categories/examples/hopf_algebras_with_basis.py # 0 doctests failed
        sage -t  -long devel/sage/sage/libs/galrep/wrapper.pyx # 0 doctests failed
        sage -t  -long devel/sage/sage/parallel/decorate.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 4264.8 seconds
```




Here's the first one, which fails, but with 0 recorded failures. 


```
sage -t  -long devel/sage/doc/en/constructions/number_fields.rst
python: can't open file '/rootpool2/local/kirkby/.sage//tmp/number_fields.py': [Errno 2] No such file or directory

         [1.9 s]
```


Here's the second recorded failure 


```
sage -t  -long devel/sage/sage/categories/examples/hopf_algebras_with_basis.py
python: can't open file '/rootpool2/local/kirkby/.sage//tmp/hopf_algebras_with_basis.py': [Errno 2] No such file or directory

         [1.7 s]
```


The third failure is where Sage crashed:


```
sage -t  -long devel/sage/sage/libs/galrep/wrapper.pyx


------------------------------------------------------------
Unhandled SIGBUS: A bus error occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------


         [21.5 s]
```


This is recorded as 0 failures, despite the fact Sage crashed. 

The only test that is recorded as a failure, with a non-zero number of failures, is the last test


```
sage -t  -long devel/sage/sage/parallel/decorate.py
**********************************************************************
File "/tmp/kirkby/sage-4.5.alpha4/devel/sage-testing/sage/parallel/decorate.py", line 152:
    sage: v = list(f([1,2,4])); v.sort(); v
Exception raised:
    Traceback (most recent call last):
      File "/tmp/kirkby/sage-4.5.alpha4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/tmp/kirkby/sage-4.5.alpha4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/tmp/kirkby/sage-4.5.alpha4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[9]>", line 1, in <module>
        v = list(f([Integer(1),Integer(2),Integer(4)])); v.sort(); v###line 152:
    sage: v = list(f([1,2,4])); v.sort(); v
      File "/tmp/kirkby/sage-4.5.alpha4/local/lib/python/site-packages/sage/parallel/multiprocessing_sage.py", line 64, in parallel_iter
        p = Pool(processes)
      File "/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/multiprocessing/__init__.py", line 227, in Pool
        return Pool(processes, initializer, initargs)
      File "/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/multiprocessing/pool.py", line 104, in __init__
        w.start()
      File "/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/multiprocessing/process.py", line 104, in start
        self._popen = Popen(self)
      File "/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/multiprocessing/forking.py", line 94, in __init__
        self.pid = os.fork()
    OSError: [Errno 12] Not enough space
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_4
***Test Failed*** 1 failures.
For whitespace errors, see the file /rootpool2/local/kirkby/.sage//tmp/.doctest_decorate.py
         [51.3 s]
```


Dave


---

Comment by drkirkby created at 2010-07-08 11:14:02

Changing priority from critical to blocker.


---

Comment by drkirkby created at 2010-07-08 11:14:02

I've marked this as a blocker, as I can't see how we can justify making a release if the summary of the doc tests can't be trusted to be correct. If we can't trust the tests, what can we trust?


---

Comment by drkirkby created at 2010-07-08 14:41:48

The log file 'ptestlong.log' after trac items #8641, #9243- and #9316 had been applied. This is the same build of Sage as before


---

Attachment


---

Comment by wjp created at 2010-07-08 15:59:36

The "# failures" that sage reports is calculated very simply by counting the number of instances of "Expected:" "Expected nothing" and "Exception raised:".

Sage correctly detected that things went wrong, as you can tell from the fact that the files causing errors are listed in the summary at the end.

As far as I can tell, the only thing that's not quite right is the reporting of what exactly went wrong. There's likely a better way of reporting these specific crashes and missing file errors you're getting, but I don't see any reason to believe something is as seriously wrong with the error reporting as you seem to be implying on this ticket and on the mailing list.

(Reverting priority to major.)


The file not found errors (Are you out of disk space?) should probably be caught before the doctesting process is launched in the first place. I'll have to think about the SIGBUS case some more.


---

Comment by wjp created at 2010-07-08 15:59:51

Changing priority from blocker to major.


---

Comment by wjp created at 2010-07-08 16:08:12

To reproduce the singal reporting issue:


```
./sage -tp 1 bus.sage
```


with bus.sage containing


```
"""
    sage: import os
    sage: os.kill(os.getpid(), 7)
"""
```



---

Comment by drkirkby created at 2010-07-08 17:18:02

It's not convenient for me to test these now, but take a look at the doctest `sage -t  -long devel/sage/sage/parallel/decorate.py`  on line 4732 of

http://trac.sagemath.org/sage_trac/attachment/ticket/9449/ptestlong.log

As far as I can see, there is absolutely no error message there, so nothing to indicate that this failed, but rather that it passed in 44.0s. But at the end it is listed as failing. 

I did 64 tests in parallel. It's possible the file system may have got too full. I will retest with fewer parallel tasks. 

Dave


---

Comment by leif created at 2010-07-08 18:45:13

I can only tell there are indeed flaws and inconsistencies in the doctest framework (I started examining it a few days ago, made some notes, but haven't finished yet).

E.g. `sage-doctest` exit code 1 can either mean "file not found", a command line syntax error or even a keyboard interrupt.
I don't understand why `sage-test` and `sage-ptest` are separated, though they contain common code that might get (or yet is) out of sync.
Different scripts use different temporary directories...
Some `make` targets for testing do `./sage -b`, others do not...

Just to name a few; I'll continue to investigate the bunch of involved scripts further, but don't really know how soon.

-Leif


---

Comment by wjp created at 2010-07-08 19:04:24

Yes, it definitely needs more cleaning up. There are already a number of patches floating around doing part of this, though. (See the aforementioned #8641, #9243, #9316 that should at least take care of the exit code 1, and also #9224, #9225 for some future plans. There may also be more.)


---

Comment by leif created at 2010-07-08 20:06:43

I don't know if _this_ one is the origin, but it's simply *horrible*:

```python
def test_file(F):
    """
    This is the function that actually tests a file
    """
    outfile = tempfile.NamedTemporaryFile()
    base, ext = os.path.splitext(F)

    cmd = 'doctest ' + opts
    if SAGE_SITE in os.path.realpath(F) and not '-force_lib' in cmd:
        cmd += ' -force_lib'

    filestr = os.path.split(F)[1]
    for i in range(0,numiteration):
        os.chdir(os.path.dirname(F))
        command = os.path.join(SAGE_ROOT, 'local', 'bin', 'sage-%s' % cmd)
        s = 'bash -c "%s %s > %s" ' % (command, filestr, outfile.name)
        try:
            t = time.time()
            ret = os.system(s)
            finished_time = time.time() - t
            if ret>=256:
                ret=ret/256
            ret = -ret
        except:
            ol = outfile.read()
            return (-5, 0, ol)
        ol = outfile.read()
        if ret != 0:
            break
    return (F, ret, finished_time, ol)
```

(Excerpt from `sage-ptest`, note not just the returned tuples...)

Beat me if I've missed something here...


---

Comment by drkirkby created at 2010-07-19 10:34:36

Replying to [comment:17 leif]:
> I don't know if _this_ one is the origin, but it's simply *horrible*:
> {{{
> #!python
> def test_file(F):
>     """
>     This is the function that actually tests a file
>     """
>     outfile = tempfile.NamedTemporaryFile()
>     base, ext = os.path.splitext(F)
> 
>     cmd = 'doctest ' + opts
>     if SAGE_SITE in os.path.realpath(F) and not '-force_lib' in cmd:
>         cmd += ' -force_lib'
> 
>     filestr = os.path.split(F)[1]
>     for i in range(0,numiteration):
>         os.chdir(os.path.dirname(F))
>         command = os.path.join(SAGE_ROOT, 'local', 'bin', 'sage-%s' % cmd)
>         s = 'bash -c "%s %s > %s" ' % (command, filestr, outfile.name)
>         try:
>             t = time.time()
>             ret = os.system(s)
>             finished_time = time.time() - t
>             if ret>=256:
>                 ret=ret/256
>             ret = -ret
>         except:
>             ol = outfile.read()
>             return (-5, 0, ol)
>         ol = outfile.read()
>         if ret != 0:
>             break
>     return (F, ret, finished_time, ol)
> }}}
> (Excerpt from `sage-ptest`, note not just the returned tuples...)
> 
> Beat me if I've missed something here...
> 
I barely know Python, so there is nothing I can do about this. But if you have a better solution, it would be worth trying it. I feel a bit uneasy about Sage, when we can't trust the mechanism for testing it. 

It's odd why failures on some test is pretty repeatable when running `make ptestlong` but run individually, they pass. I'm pretty sure that is not a memory issue, as I've noticed that on my Sun Blade 2000 SPARC where I'm the only user. That machine has 8 GB RAM and only two processors (its not multi-cored or multi-threaded), so I don't run more than 3 tests in parallel.


---

Comment by mpatel created at 2010-09-11 00:44:20

Replying to [comment:7 drkirkby]:
> The only test that is recorded as a failure, with a non-zero number of failures, is the last test

I've opened #9895 for the recurring "Not enough space" error on Solaris raised by `os.fork` in `sage/parallel/decorate.py`.


---

Comment by jdemeyer created at 2013-02-22 21:37:04

Since #12415 completely rewrites the doctest framework with much better code, I'm assuming this problem is fixed.


---

Comment by jdemeyer created at 2013-02-22 21:37:04

Resolution: duplicate
