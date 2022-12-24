# Issue 9299: Test failures of Python (2.6.4.p9) on OpenSolaris x64 (64-bit)

archive/issues_009299.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies @nexttime @mkoeppe\n\nAlthough Sage 4.4.4.alpha1 does not build on OpenSolaris x64, the standard Python package does. \n\n## Build environment\n* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. \n* 12 GB RAM\n* OpenSolaris 2009.06 snv_134 X86\n* gcc 4.4.4 configured to use the Sun linker and GNU assembler. \n* Sage 4.4.4.alpha1 \n* #9041 to allow Python to build _socket.\n* #9295 to add an spkg-check file to the Sage Python package. \n\n## The background\nAlthough Sage 4.4.4.alpha1 (or any Sage version for that matter) does not build fully on OpenSolaris, the Python module does build fully. However, unless #9041 is applied, _socket will not build which prevents several parts of Sage from building. \n\nFurthermore, unless #9295 is applied, exporting SAGE_CHECK to \"yes\" will not result in any tests of the Python package. \n\n## Summary of test results\nHere are the summary of the test results. Although there are the same number of failures as observed on Solaris 10 SPARC (32-bit), the failures are not always the same - there are some unique to OpenSolaris and some unique to Solaris 10. \n\n```\n320 tests OK.\n5 tests failed:\n    test_distutils test_float test_multiprocessing test_posix\n    test_zlib\n40 tests skipped:\n    test_aepack test_al test_applesingle test_bsddb test_bsddb185\n    test_bsddb3 test_cd test_cl test_codecmaps_cn test_codecmaps_hk\n    test_codecmaps_jp test_codecmaps_kr test_codecmaps_tw test_curses\n    test_dl test_epoll test_gdbm test_gl test_imageop test_imgfile\n    test_kqueue test_linuxaudiodev test_macos test_macostools\n    test_normalization test_ossaudiodev test_pep277 test_py3kwarn\n    test_scriptpackages test_smtpnet test_socketserver test_startfile\n    test_sunaudiodev test_tcl test_timeout test_urllib2net\n    test_urllibnet test_winreg test_winsound test_zipfile64\n3 skips unexpected on sunos5:\n    test_tcl test_sunaudiodev test_dl\nmake: *** [test] Error 1\nAn error occured whilst testing Python\n*************************************\nError testing package ** python-2.6.4.p9 **\n*************************************\nsage: An error occurred while testing python-2.6.4.p9\n```\n\n## Individual test failures\nOn failure seems a little strange below, where it reports \"not enough space\". The machine has 990 GB of free space! \n\n\n```\ntest test_distutils failed -- errors occurred; run in verbose mode for details\n\ntest test_float failed -- Traceback (most recent call last):\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_float.py\", line 765, in test_roundtrip\n    self.identical(-x, roundtrip(-x))\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_float.py\", line 375, in identical\n    self.fail('%r not identical to %r' % (x, y))\nAssertionError: -0.0 not identical to 0.0\n\ntest test_multiprocessing failed -- Traceback (most recent call last):\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_multiprocessing.py\", line 1666, in test_import\n    __import__(name)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/multiprocessing/reduction.py\", line 29, in <module>\n    raise ImportError('pickling of connections not supported')\nImportError: pickling of connections not supported\n\ntest test_posix failed -- Traceback (most recent call last):\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 267, in test_getcwd_long_pathnames\n    _create_and_do_getcwd(dirname)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 262, in _create_and_do_getcwd\n    _create_and_do_getcwd(dirname, current_path_length + len(dirname) + 1)\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_posix.py\", line 260, in _create_and_do_getcwd\n    os.getcwd()\nOSError: [Errno 12] Not enough space\n\ntest test_zlib failed -- Traceback (most recent call last):\n  File \"/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src/Lib/test/test_zlib.py\", line 84, in test_baddecompressobj\n    self.assertRaises(ValueError, zlib.decompressobj, 0)\nAssertionError: ValueError not raised\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9299\n\n",
    "created_at": "2010-06-21T18:28:34Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Test failures of Python (2.6.4.p9) on OpenSolaris x64 (64-bit)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9299",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies @nexttime @mkoeppe

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


Issue created by migration from https://trac.sagemath.org/ticket/9299





---

archive/issue_comments_087598.json:
```json
{
    "body": "Changing keywords from \"\" to \"testsuite, Python modules, Failed, SAGE_CHECK\".",
    "created_at": "2010-07-16T16:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9299#issuecomment-87598",
    "user": "@nexttime"
}
```

Changing keywords from "" to "testsuite, Python modules, Failed, SAGE_CHECK".



---

archive/issue_comments_087599.json:
```json
{
    "body": "Python testsuite failures are not specific to OpenSolaris (I've seen them on Ubuntu 9.04, too).",
    "created_at": "2010-07-16T16:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9299#issuecomment-87599",
    "user": "@nexttime"
}
```

Python testsuite failures are not specific to OpenSolaris (I've seen them on Ubuntu 9.04, too).



---

archive/issue_comments_087600.json:
```json
{
    "body": "Replying to [comment:2 leif]:\n> Python testsuite failures are not specific to OpenSolaris (I've seen them on Ubuntu 9.04, too).\nYes, but the tests which actually fail vary from system to system, with the exception of `test_distutils` which fails for every report I've seen. \n\n\nDave",
    "created_at": "2010-07-16T16:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9299#issuecomment-87600",
    "user": "drkirkby"
}
```

Replying to [comment:2 leif]:
> Python testsuite failures are not specific to OpenSolaris (I've seen them on Ubuntu 9.04, too).
Yes, but the tests which actually fail vary from system to system, with the exception of `test_distutils` which fails for every report I've seen. 


Dave



---

archive/issue_comments_087601.json:
```json
{
    "body": "obsolete ?",
    "created_at": "2020-06-27T08:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9299#issuecomment-87601",
    "user": "@fchapoton"
}
```

obsolete ?



---

archive/issue_comments_087602.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-27T08:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9299#issuecomment-87602",
    "user": "@fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087603.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-06-27T17:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9299#issuecomment-87603",
    "user": "@mkoeppe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087604.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-27T18:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9299#issuecomment-87604",
    "user": "@fchapoton"
}
```

Resolution: invalid
