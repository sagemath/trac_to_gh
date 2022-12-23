# Issue 9299: Test failures of Python (2.6.4.p9) on OpenSolaris x64 (64-bit)

Issue created by migration from https://trac.sagemath.org/ticket/9299

Original creator: drkirkby

Original creation time: 2010-06-21 18:28:34

Assignee: drkirkby

CC:  jsp leif mkoeppe

Although Sage 4.4.4.alpha1 does not build on OpenSolaris x64, the standard Python package does. 

## Build environment
 * Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 
 * 12 GB RAM
 * OpenSolaris 2009.06 snv_134 X86
 * gcc 4.4.4 configured to use the Sun linker and GNU assembler. 
 * Sage 4.4.4.alpha1 
 * #9041 to allow Python to build _socket.
 * #9295 to add an spkg-check file to the Sage Python package. 

## The background
Although Sage 4.4.4.alpha1 (or any Sage version for that matter) does not build fully on OpenSolaris, the Python module does build fully. However, unless #9041 is applied, _socket will not build which prevents several parts of Sage from building. 

Furthermore, unless #9295 is applied, exporting SAGE_CHECK to "yes" will not result in any tests of the Python package. 

## Summary of test results
Here are the summary of the test results. Although there are the same number of failures as observed on Solaris 10 SPARC (32-bit), the failures are not always the same - there are some unique to OpenSolaris and some unique to Solaris 10. 

```
320 tests OK.
5 tests failed:
    test_distutils test_float test_multiprocessing test_posix
    test_zlib
40 tests skipped:
    test_aepack test_al test_applesingle test_bsddb test_bsddb185
    test_bsddb3 test_cd test_cl test_codecmaps_cn test_codecmaps_hk
    test_codecmaps_jp test_codecmaps_kr test_codecmaps_tw test_curses
    test_dl test_epoll test_gdbm test_gl test_imageop test_imgfile
    test_kqueue test_linuxaudiodev test_macos test_macostools
    test_normalization test_ossaudiodev test_pep277 test_py3kwarn
    test_scriptpackages test_smtpnet test_socketserver test_startfile
    test_sunaudiodev test_tcl test_timeout test_urllib2net
    test_urllibnet test_winreg test_winsound test_zipfile64
3 skips unexpected on sunos5:
    test_tcl test_sunaudiodev test_dl
make: *** [test] Error 1
An error occured whilst testing Python
*************************************
Error testing package ** python-2.6.4.p9 **
*************************************
sage: An error occurred while testing python-2.6.4.p9
```

## Individual test failures
On failure seems a little strange below, where it reports "not enough space". The machine has 990 GB of free space! 


```
test test_distutils failed -- errors occurred; run in verbose mode for details

test test_float failed -- Traceback (most recent call last):
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_float.py", line 765, in test_roundtrip
    self.identical(-x, roundtrip(-x))
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_float.py", line 375, in identical
    self.fail('%r not identical to %r' % (x, y))
AssertionError: -0.0 not identical to 0.0

test test_multiprocessing failed -- Traceback (most recent call last):
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_multiprocessing.py", line 1666, in test_import
    __import__(name)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/multiprocessing/reduction.py", line 29, in <module>
    raise ImportError('pickling of connections not supported')
ImportError: pickling of connections not supported

test test_posix failed -- Traceback (most recent call last):
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 267, in test_getcwd_long_pathnames
    _create_and_do_getcwd(dirname)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 262, in _create_and_do_getcwd
    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py", line 260, in _create_and_do_getcwd
    os.getcwd()
OSError: [Errno 12] Not enough space

test test_zlib failed -- Traceback (most recent call last):
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_zlib.py", line 84, in test_baddecompressobj
    self.assertRaises(ValueError, zlib.decompressobj, 0)
AssertionError: ValueError not raised
```



---

Comment by leif created at 2010-07-16 16:32:15

Changing keywords from "" to "testsuite, Python modules, Failed, SAGE_CHECK".


---

Comment by leif created at 2010-07-16 16:32:15

Python testsuite failures are not specific to OpenSolaris (I've seen them on Ubuntu 9.04, too).


---

Comment by drkirkby created at 2010-07-16 16:58:14

Replying to [comment:2 leif]:
> Python testsuite failures are not specific to OpenSolaris (I've seen them on Ubuntu 9.04, too).
Yes, but the tests which actually fail vary from system to system, with the exception of `test_distutils` which fails for every report I've seen. 


Dave


---

Comment by chapoton created at 2020-06-27 08:48:54

obsolete ?


---

Comment by chapoton created at 2020-06-27 08:48:54

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-06-27 17:35:15

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-06-27 18:16:20

Resolution: invalid
