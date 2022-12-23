# Issue 9297: Test failures of Python (2.6.4.p9) on Solaris 10 SPARC (32-bit)

Issue created by migration from https://trac.sagemath.org/ticket/9297

Original creator: drkirkby

Original creation time: 2010-06-21 16:20:21

Assignee: drkirkby

CC:  jsp leif mkoeppe

## Hardware & associated software

 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and Sun assembler)
 * Sage 4.4.4.alpha1
 * #9041 to allow Python to build _socket. (Not needed on SPARC, but it was applied)
 * #9295 to permit Python test suite to build. 

## Background
Although Sage 4.4.4.alpha1 builds fully on Solaris 10 (SPARC), there are some test failures of the Python test suite, which are discovered if SAGE_CHECK is exported to "yes", and #9295 included in Sage, which allows SAGE_CHECK to work with Python. 

## Summary of test results

```
322 tests OK.
5 tests failed:
    test_distutils test_float test_hotshot test_multiprocessing
    test_sunaudiodev
38 tests skipped:
    test_aepack test_al test_applesingle test_bsddb test_bsddb185
    test_bsddb3 test_cd test_cl test_codecmaps_cn test_codecmaps_hk
    test_codecmaps_jp test_codecmaps_kr test_codecmaps_tw test_curses
    test_epoll test_gdbm test_gl test_imgfile test_kqueue
    test_linuxaudiodev test_macos test_macostools test_normalization
    test_ossaudiodev test_pep277 test_py3kwarn test_scriptpackages
    test_smtpnet test_socketserver test_ssl test_startfile test_tcl
    test_timeout test_urllib2net test_urllibnet test_winreg
    test_winsound test_zipfile64
2 skips unexpected on sunos5:
    test_tcl test_ssl
```

## Individual test failures

```
test test_distutils failed -- errors occurred; run in verbose mode for details

test test_float failed -- Traceback (most recent call last):
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_float.py", line 765, in test_roundtrip
    self.identical(-x, roundtrip(-x))
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_float.py", line 375, in identical
    self.fail('%r not identical to %r' % (x, y))
AssertionError: -0.0 not identical to 0.0

test_hotshot
test test_hotshot failed -- Traceback (most recent call last):
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_hotshot.py", line 130, in test_logreader_eof_error
    self.assertRaises((IOError, EOFError), _hotshot.logreader, ".")
AssertionError: (<type 'exceptions.IOError'>, <type 'exceptions.EOFError'>) not raised

test_multiprocessing
test test_multiprocessing failed -- Traceback (most recent call last):
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_multiprocessing.py", line 1666, in test_import
    __import__(name)
  File "/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/multiprocessing/reduction.py", line 29, in <module>
    raise ImportError('pickling of connections not supported')
ImportError: pickling of connections not supported


test test_sunaudiodev failed -- (13, 'Permission denied', '/dev/audio')
```



---

Comment by drkirkby created at 2010-06-21 18:34:34

Note, #8440 was supposed to fix a failure of _multiprocessing to build, but it may be that whilst that fix allowed it to build, it does not actually work correctly.


---

Comment by rlm created at 2010-07-16 08:05:21

Python failures have also been reported with `SAGE_CHECK=yes` on Ubuntu 9.04 x86 and x86_64.

See http://groups.google.com/group/sage-release/msg/92e83194909d4d72


---

Comment by rlm created at 2010-07-16 08:31:14

This also occurs on sage.math, so it is very easy for someone to work on...


---

Comment by drkirkby created at 2010-07-16 09:59:17

Replying to [comment:2 rlm]:
> Python failures have also been reported with `SAGE_CHECK=yes` on Ubuntu 9.04 x86 and x86_64.
> 
> See http://groups.google.com/group/sage-release/msg/92e83194909d4d72

If you see this thread

http://groups.google.co.uk/group/sage-devel/browse_thread/thread/b7856076ea5aefbd/8d381b77e4d461cb

where I asked people to test their python build, *everyone* who responded had one or more failures. `test_distutils` is a bit worrying, as everyone reported that failed for them. There was a report that the clean 2.6.5 source code passes this test, but I don't know for sure if the 2.6.4 in Sage passes this test. I think it does, in which case a patch in Sage, or the Sage build environment is screwing `test_disutils` up. 

I reported the `test_float` on Solaris upstream

http://bugs.python.org/issue9069

but that was found to be a bug in gcc >= 4.4.0, but has now been fixed in the gcc source code, so the next release should have the issue resolved. 

That still leaves a few python failures on Solaris that I've not resolved. 

I think people should create individual tickets for individual test failures, as there are many different failures on many peoples systems. But `test_disutils` is common to ever single report I see. 

Dave


---

Comment by drkirkby created at 2010-07-16 10:11:47

Replying to [comment:4 drkirkby]:
> But `test_disutils` is common to ever single report I see. 
> 
> Dave 

Oops, 

I mean `test_disutils` is common to every single report I see. 

If anyone has some time and wants to work on them, then `test_disutils` is probably the best test to start with, as it effects everyone. Or is is _affects_ everyone? I always have problems with those words!

Dave


---

Comment by leif created at 2010-07-16 16:37:47

Changing keywords from "" to "testsuite, Python modules, Failed, SAGE_CHECK".


---

Comment by leif created at 2010-07-16 17:15:49

On Ubuntu 9.04 (x86 in this case), `spkg/logs/python-*.log` shows:


```
...
running build
running build_ext
INFO: Can't locate Tcl/Tk libs and/or headers

Failed to find the necessary bits to build these modules:
_bsddb             _curses            _curses_panel
_hashlib           _ssl               _tkinter
bsddb185           dbm                gdbm
sunaudiodev
To find the necessary bits, look in setup.py in detect_modules() for the module's name.

running build_scripts
...
```

and

```
...
Successfully installed python-2.6.4.p9
Running the test suite.
Testing the Python package
...
test_distutils
test test_distutils failed -- errors occurred; run in verbose mode for details
...
test_os
/home/leif/sage-4.5.rc1-par-j6-sage-check/spkg/build/python-2.6.4.p9/src/Lib/os.py:760: DeprecationWarning: integer argument expected, got float
  bs += read(_urandomfd, n - len(bs))
...
test_sundry
/home/leif/sage-4.5.rc1-par-j6-sage-check/spkg/build/python-2.6.4.p9/src/Lib/test/test_sundry.py:66: DeprecationWarning: The posixfile module is deprecated; fcntl.lockf() provides better locking
  import posixfile
...
test_xmllib
/home/leif/sage-4.5.rc1-par-j6-sage-check/spkg/build/python-2.6.4.p9/src/Lib/test/test_xmllib.py:24: DeprecationWarning: The xmllib module is obsolete.  Use xml.sax instead.
  import xmllib
...
test_zlib
test test_zlib failed -- Traceback (most recent call last):
  File "/home/leif/sage-4.5.rc1-par-j6-sage-check/spkg/build/python-2.6.4.p9/src/Lib/test/test_zlib.py", line 84, in test_baddecompressobj
    self.assertRaises(ValueError, zlib.decompressobj, 0)
AssertionError: ValueError not raised

323 tests OK.
2 tests failed:
    test_distutils test_zlib
40 tests skipped:
    test_aepack test_al test_applesingle test_bsddb test_bsddb185
    test_bsddb3 test_cd test_cl test_codecmaps_cn test_codecmaps_hk
    test_codecmaps_jp test_codecmaps_kr test_codecmaps_tw test_curses
    test_dbm test_gdbm test_gl test_imgfile test_kqueue
    test_linuxaudiodev test_macos test_macostools test_normalization
    test_ossaudiodev test_pep277 test_py3kwarn test_scriptpackages
    test_smtpnet test_socketserver test_ssl test_startfile
    test_sunaudiodev test_tcl test_timeout test_unicode_file
    test_urllib2net test_urllibnet test_winreg test_winsound
    test_zipfile64
5 skips unexpected on linux2:
    test_tcl test_dbm test_ssl test_gdbm test_bsddb
make[2]: [test] Error 1 (ignored)
...
[above repeated]
test test_zlib failed -- Traceback (most recent call last):
  File "/home/leif/sage-4.5.rc1-par-j6-sage-check/spkg/build/python-2.6.4.p9/src/Lib/test/test_zlib.py", line 84, in test_baddecompressobj
    self.assertRaises(ValueError, zlib.decompressobj, 0)
AssertionError: ValueError not raised

323 tests OK.
2 tests failed:
    test_distutils test_zlib
40 tests skipped:
    test_aepack test_al test_applesingle test_bsddb test_bsddb185
    test_bsddb3 test_cd test_cl test_codecmaps_cn test_codecmaps_hk
    test_codecmaps_jp test_codecmaps_kr test_codecmaps_tw test_curses
    test_dbm test_gdbm test_gl test_imgfile test_kqueue
    test_linuxaudiodev test_macos test_macostools test_normalization
    test_ossaudiodev test_pep277 test_py3kwarn test_scriptpackages
    test_smtpnet test_socketserver test_ssl test_startfile
    test_sunaudiodev test_tcl test_timeout test_unicode_file
    test_urllib2net test_urllibnet test_winreg test_winsound
    test_zipfile64
5 skips unexpected on linux2:
    test_tcl test_dbm test_ssl test_gdbm test_bsddb
make[2]: *** [test] Error 1
make[2]: Leaving directory `/home/leif/sage-4.5.rc1-par-j6-sage-check/spkg/build/python-2.6.4.p9/src'
An error occurred while testing Python
*************************************
Error testing package ** python-2.6.4.p9 **
*************************************
sage: An error occurred while testing python-2.6.4.p9
...
```

The former can be found by doing

```sh
grep -A5 Failed install.log     # or spkg/logs/python-*.log
```

in (successful) builds without `SAGE_CHECK=yes`, too.


---

Comment by drkirkby created at 2010-07-16 17:26:49

It would be good if the Linux failures could be put on another ticket. Otherwise, this ticket will be just full of test results on every conceivable system. I've created tickets for 32-bit SPARC (this one) and OpenSolaris (#9299) 



Dave


---

Comment by leif created at 2010-07-16 18:05:33

Replying to [comment:8 drkirkby]:
> It would be good if the Linux failures could be put on another ticket. Otherwise, this ticket will be just full of test results on every conceivable system.

Ok, my post was a bit verbose, too. I only wanted to stress that `zlib` and `distutils` failing is not specific to SunOS/Solaris (or SPARC).

> I've created tickets for 32-bit SPARC (this one) and OpenSolaris (#9299) 

Perhaps we should create meta-tickets for

 * "Missing bits" (they differ from system to system, I don't know which of them might be relevant for Sage)

 * Python testsuite failures

The former need not be a meta-ticket, perhaps just collecting brief reports from various platforms, and informational to users who wonder if Sage's functionality can be affected. This information should be put into the Wiki and Installation Guide later.


---

Comment by chapoton created at 2020-06-27 08:48:30

obsolete ?


---

Comment by chapoton created at 2020-06-27 08:48:30

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-06-27 17:35:02

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-06-27 18:16:02

Resolution: invalid
