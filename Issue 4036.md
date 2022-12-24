# Issue 4036: [with patch, needs review] minor improvements to the Axiom interface

archive/issues_004036.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4036\n\n",
    "created_at": "2008-09-01T23:34:49Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] minor improvements to the Axiom interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4036",
    "user": "@mwhansen"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/4036





---

archive/issue_comments_029114.json:
```json
{
    "body": "Attachment [trac_4036.patch](tarball://root/attachments/some-uuid/ticket4036/trac_4036.patch) by @mwhansen created at 2008-09-01 23:35:10",
    "created_at": "2008-09-01T23:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29114",
    "user": "@mwhansen"
}
```

Attachment [trac_4036.patch](tarball://root/attachments/some-uuid/ticket4036/trac_4036.patch) by @mwhansen created at 2008-09-01 23:35:10



---

archive/issue_comments_029115.json:
```json
{
    "body": "Attachment [trac_4036-2.patch](tarball://root/attachments/some-uuid/ticket4036/trac_4036-2.patch) by @mwhansen created at 2008-09-08 02:11:35",
    "created_at": "2008-09-08T02:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29115",
    "user": "@mwhansen"
}
```

Attachment [trac_4036-2.patch](tarball://root/attachments/some-uuid/ticket4036/trac_4036-2.patch) by @mwhansen created at 2008-09-08 02:11:35



---

archive/issue_comments_029116.json:
```json
{
    "body": "Attachment [trac_4036-3.patch](tarball://root/attachments/some-uuid/ticket4036/trac_4036-3.patch) by @rlmill created at 2008-09-15 00:55:41\n\npatches apply to 3.1.2.rc1 and doctests pass in `sage/interfaces`, with the following exceptions:\n\n```\nsage -t  devel/sage/sage/interfaces/psage.py\nEnd Of File (EOF) in read_nonblocking(). Empty string style platform.\n<pexpect.spawn instance at 0x7550f80>\nversion: 2.0 ($Revision: 1.151 $)\ncommand: /Users/rlmill/sage-3.1.2.rc1/sage\nargs: ['/Users/rlmill/sage-3.1.2.rc1/sage']\npatterns:\n    sage: \nbuffer (last 100 chars): \nbefore (last 100 chars): \nafter: <class 'pexpect.EOF'>\nmatch: None\nmatch_index: None\nexitstatus: None\nflag_eof: 1\npid: 27789\nchild_fd: 5\ntimeout: 30\ndelimiter: <class 'pexpect.EOF'>\nlogfile: None\nmaxread: 100000\nsearchwindowsize: None\ndelaybeforesend: 0\n\t [14.6 s]\n```\n\nThis one passes, but...\n\nAnd this one:\n\n```\nsage -t  devel/sage/sage/interfaces/lisp.py\n**********************************************************************\nFile \"/Users/rlmill/sage-3.1.2.rc1/tmp/lisp.py\", line 282:\n    sage: lisp.version()\nExpected:\n    GNU CLISP ... (...) (built ...) (memory ...)\n    ...\nGot:\n    GNU CLISP 2.46 (2008-07-02) (built on robert-millers-macbook-pro-15.local [192.168.0.101])\n    Software: GNU C 4.0.1 (Apple Inc. build 5465) \n    gcc -O0 -g -I/Users/rlmill/sage-3.1.2.rc1/local/include/ -L/Users/rlmill/sage-3.1.2.rc1/local/lib/ -W -Wswitch -Wcomment -Wpointer-arith -Wimplicit -Wreturn-type -Wmissing-declarations -Wno-sign-compare -O0 -fexpensive-optimizations -falign-functions=4 -DUNIX_BINARY_DISTRIB -DUNICODE -DNO_GETTEXT -DNO_SIGSEGV -I. -x none -lreadline -lncurses  -liconv  -L/usr/X11/lib -R/usr/X11/lib\n    SAFETY=0 HEAPCODES STANDARD_HEAPCODES SPVW_BLOCKS SPVW_MIXED TRIVIALMAP_MEMORY\n    libiconv 1.11\n    libreadline 5.2\n    Features: \n    (REGEXP SYSCALLS I18N LOOP COMPILER CLOS MOP CLISP ANSI-CL COMMON-LISP LISP=CL\n     INTERPRETER SOCKETS GENERIC-STREAMS LOGICAL-PATHNAMES SCREEN UNICODE\n     BASE-CHAR=CHARACTER UNIX MACOS)\n    C Modules: (clisp i18n syscalls regexp)\n    Installation directory: /Users/rlmill/sage-3.1.2.rc1/local/lib/clisp-2.46/\n    User language: ENGLISH\n    Machine: I386 (I386) D-69-91-148-44.dhcp4.washington.edu [69.91.148.44]\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   1 of   3 in __main__.example_14\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/rlmill/sage-3.1.2.rc1/tmp/.doctest_lisp.py\n\n\t [3.2 s]\n```\n",
    "created_at": "2008-09-15T00:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29116",
    "user": "@rlmill"
}
```

Attachment [trac_4036-3.patch](tarball://root/attachments/some-uuid/ticket4036/trac_4036-3.patch) by @rlmill created at 2008-09-15 00:55:41

patches apply to 3.1.2.rc1 and doctests pass in `sage/interfaces`, with the following exceptions:

```
sage -t  devel/sage/sage/interfaces/psage.py
End Of File (EOF) in read_nonblocking(). Empty string style platform.
<pexpect.spawn instance at 0x7550f80>
version: 2.0 ($Revision: 1.151 $)
command: /Users/rlmill/sage-3.1.2.rc1/sage
args: ['/Users/rlmill/sage-3.1.2.rc1/sage']
patterns:
    sage: 
buffer (last 100 chars): 
before (last 100 chars): 
after: <class 'pexpect.EOF'>
match: None
match_index: None
exitstatus: None
flag_eof: 1
pid: 27789
child_fd: 5
timeout: 30
delimiter: <class 'pexpect.EOF'>
logfile: None
maxread: 100000
searchwindowsize: None
delaybeforesend: 0
	 [14.6 s]
```

This one passes, but...

And this one:

```
sage -t  devel/sage/sage/interfaces/lisp.py
**********************************************************************
File "/Users/rlmill/sage-3.1.2.rc1/tmp/lisp.py", line 282:
    sage: lisp.version()
Expected:
    GNU CLISP ... (...) (built ...) (memory ...)
    ...
Got:
    GNU CLISP 2.46 (2008-07-02) (built on robert-millers-macbook-pro-15.local [192.168.0.101])
    Software: GNU C 4.0.1 (Apple Inc. build 5465) 
    gcc -O0 -g -I/Users/rlmill/sage-3.1.2.rc1/local/include/ -L/Users/rlmill/sage-3.1.2.rc1/local/lib/ -W -Wswitch -Wcomment -Wpointer-arith -Wimplicit -Wreturn-type -Wmissing-declarations -Wno-sign-compare -O0 -fexpensive-optimizations -falign-functions=4 -DUNIX_BINARY_DISTRIB -DUNICODE -DNO_GETTEXT -DNO_SIGSEGV -I. -x none -lreadline -lncurses  -liconv  -L/usr/X11/lib -R/usr/X11/lib
    SAFETY=0 HEAPCODES STANDARD_HEAPCODES SPVW_BLOCKS SPVW_MIXED TRIVIALMAP_MEMORY
    libiconv 1.11
    libreadline 5.2
    Features: 
    (REGEXP SYSCALLS I18N LOOP COMPILER CLOS MOP CLISP ANSI-CL COMMON-LISP LISP=CL
     INTERPRETER SOCKETS GENERIC-STREAMS LOGICAL-PATHNAMES SCREEN UNICODE
     BASE-CHAR=CHARACTER UNIX MACOS)
    C Modules: (clisp i18n syscalls regexp)
    Installation directory: /Users/rlmill/sage-3.1.2.rc1/local/lib/clisp-2.46/
    User language: ENGLISH
    Machine: I386 (I386) D-69-91-148-44.dhcp4.washington.edu [69.91.148.44]
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_14
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/rlmill/sage-3.1.2.rc1/tmp/.doctest_lisp.py

	 [3.2 s]
```




---

archive/issue_comments_029117.json:
```json
{
    "body": "...both of which failed before applying too. Looks good to me!",
    "created_at": "2008-09-15T00:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29117",
    "user": "@rlmill"
}
```

...both of which failed before applying too. Looks good to me!



---

archive/issue_comments_029118.json:
```json
{
    "body": "This patch introduces the following problem:\n\n```\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/tmp/parent.py\", line 13:\n    sage: gp(2) + gap(3)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[2]>\", line 1, in <module>\n        gp(Integer(2)) + gap(Integer(3))###line 13:\n    sage: gp(2) + gap(3)\n      File \"element.pyx\", line 718, in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:5748)\n        return coercion_model.bin_op(left, right, add)\n      File \"coerce.pyx\", line 662, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6364)\n        raise TypeError, arith_error_message(x,y,op)\n    TypeError: unsupported operand parent(s) for '+': 'GP/PARI interpreter' and 'Gap'\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-09-15T03:05:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29118",
    "user": "mabshoff"
}
```

This patch introduces the following problem:

```
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/tmp/parent.py", line 13:
    sage: gp(2) + gap(3)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        gp(Integer(2)) + gap(Integer(3))###line 13:
    sage: gp(2) + gap(3)
      File "element.pyx", line 718, in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:5748)
        return coercion_model.bin_op(left, right, add)
      File "coerce.pyx", line 662, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6364)
        raise TypeError, arith_error_message(x,y,op)
    TypeError: unsupported operand parent(s) for '+': 'GP/PARI interpreter' and 'Gap'
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_029119.json:
```json
{
    "body": "And this one, too:\n\n```\nsage -t -long devel/sage/sage/matrix/matrix_symbolic_dense.pyx\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/tmp/matrix_symbolic_dense.py\", line 185:\n    sage: print \"ignore this\";  hash(maxima(m)) #random due to architecture dependence\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[5]>\", line 1, in <module>\n        print \"ignore this\";  hash(maxima(m)) #random due to architecture dependence###line 185:\n    sage: print \"ignore this\";  hash(maxima(m)) #random due to architecture dependence\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 984, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1008, in _coerce_from_special_method\n        return (x.__getattribute__(s))(self)\n      File \"matrix_symbolic_dense.pyx\", line 383, in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense._maxima_ (sage/matrix/matrix_symbolic_dense.c:3536)\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 977, in __call__\n        return self(x._sage_())\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/maxima.py\", line 1440, in _sage_\n        return symbolic_expression_from_maxima_string(repr(self))\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 8515, in symbolic_expression_from_maxima_string\n        raise TypeError, \"unable to make sense of Maxima expression '%s' in SAGE\"%s\n    TypeError: unable to make sense of Maxima expression 'matrix([sqrt(2),3],[pi,e])' in SAGE\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/tmp/matrix_symbolic_dense.py\", line 377:\n    sage: m._maxima_(maxima)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_17[4]>\", line 1, in <module>\n        m._maxima_(maxima)###line 377:\n    sage: m._maxima_(maxima)\n      File \"matrix_symbolic_dense.pyx\", line 383, in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense._maxima_ (sage/matrix/matrix_symbolic_dense.c:3536)\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 977, in __call__\n        return self(x._sage_())\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/maxima.py\", line 1440, in _sage_\n        return symbolic_expression_from_maxima_string(repr(self))\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 8515, in symbolic_expression_from_maxima_string\n        raise TypeError, \"unable to make sense of Maxima expression '%s' in SAGE\"%s\n    TypeError: unable to make sense of Maxima expression 'matrix([sqrt(2),3],[pi,e])' in SAGE\n**********************************************************************\n```\n",
    "created_at": "2008-09-15T03:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29119",
    "user": "mabshoff"
}
```

And this one, too:

```
sage -t -long devel/sage/sage/matrix/matrix_symbolic_dense.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/tmp/matrix_symbolic_dense.py", line 185:
    sage: print "ignore this";  hash(maxima(m)) #random due to architecture dependence
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[5]>", line 1, in <module>
        print "ignore this";  hash(maxima(m)) #random due to architecture dependence###line 185:
    sage: print "ignore this";  hash(maxima(m)) #random due to architecture dependence
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 984, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1008, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "matrix_symbolic_dense.pyx", line 383, in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense._maxima_ (sage/matrix/matrix_symbolic_dense.c:3536)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 977, in __call__
        return self(x._sage_())
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/maxima.py", line 1440, in _sage_
        return symbolic_expression_from_maxima_string(repr(self))
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 8515, in symbolic_expression_from_maxima_string
        raise TypeError, "unable to make sense of Maxima expression '%s' in SAGE"%s
    TypeError: unable to make sense of Maxima expression 'matrix([sqrt(2),3],[pi,e])' in SAGE
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/tmp/matrix_symbolic_dense.py", line 377:
    sage: m._maxima_(maxima)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_17[4]>", line 1, in <module>
        m._maxima_(maxima)###line 377:
    sage: m._maxima_(maxima)
      File "matrix_symbolic_dense.pyx", line 383, in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense._maxima_ (sage/matrix/matrix_symbolic_dense.c:3536)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 977, in __call__
        return self(x._sage_())
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/interfaces/maxima.py", line 1440, in _sage_
        return symbolic_expression_from_maxima_string(repr(self))
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 8515, in symbolic_expression_from_maxima_string
        raise TypeError, "unable to make sense of Maxima expression '%s' in SAGE"%s
    TypeError: unable to make sense of Maxima expression 'matrix([sqrt(2),3],[pi,e])' in SAGE
**********************************************************************
```




---

archive/issue_comments_029120.json:
```json
{
    "body": "Attachment [trac_4036-fixes.patch](tarball://root/attachments/some-uuid/ticket4036/trac_4036-fixes.patch) by @mwhansen created at 2008-09-15 03:51:23\n\nThis patch should fix the issues.",
    "created_at": "2008-09-15T03:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29120",
    "user": "@mwhansen"
}
```

Attachment [trac_4036-fixes.patch](tarball://root/attachments/some-uuid/ticket4036/trac_4036-fixes.patch) by @mwhansen created at 2008-09-15 03:51:23

This patch should fix the issues.



---

archive/issue_comments_029121.json:
```json
{
    "body": "We need a review for the four patches together. The issue rlm saw is unrelated to this patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-28T14:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29121",
    "user": "mabshoff"
}
```

We need a review for the four patches together. The issue rlm saw is unrelated to this patch.

Cheers,

Michael



---

archive/issue_comments_029122.json:
```json
{
    "body": "This needs to be rebased against sage-3.2.1.*:\n\n```\nwas@sage:~/build/sage-3.2.1.alpha1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4036/trac_4036.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4036/trac_4036.patch?format=raw\nLoading: [.]\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg import   \"/home/was/.sage/temp/sage/10714/tmp_0.patch\"\napplying /home/was/.sage/temp/sage/10714/tmp_0.patch\npatching file sage/rings/integer_mod.pyx\nHunk #1 FAILED at 361\n1 out of 1 hunk FAILED -- saving rejects to file sage/rings/integer_mod.pyx.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2008-11-27T17:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29122",
    "user": "@williamstein"
}
```

This needs to be rebased against sage-3.2.1.*:

```
was@sage:~/build/sage-3.2.1.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4036/trac_4036.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4036/trac_4036.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/10714/tmp_0.patch"
applying /home/was/.sage/temp/sage/10714/tmp_0.patch
patching file sage/rings/integer_mod.pyx
Hunk #1 FAILED at 361
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/integer_mod.pyx.rej
abort: patch failed to apply
```




---

archive/issue_comments_029123.json:
```json
{
    "body": "Attachment [trac_4036-axiom_interface.patch](tarball://root/attachments/some-uuid/ticket4036/trac_4036-axiom_interface.patch) by @maxthemouse created at 2009-08-17 15:02:46\n\nadd fricas tests to axiom.py",
    "created_at": "2009-08-17T15:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29123",
    "user": "@maxthemouse"
}
```

Attachment [trac_4036-axiom_interface.patch](tarball://root/attachments/some-uuid/ticket4036/trac_4036-axiom_interface.patch) by @maxthemouse created at 2009-08-17 15:02:46

add fricas tests to axiom.py



---

archive/issue_comments_029124.json:
```json
{
    "body": "The content of these patches seems to have already been applied. In fact, most have been expanded with tests for fricas. I added some more tests for fricas, if desired. \n\nAdam",
    "created_at": "2009-08-17T15:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29124",
    "user": "@maxthemouse"
}
```

The content of these patches seems to have already been applied. In fact, most have been expanded with tests for fricas. I added some more tests for fricas, if desired. 

Adam



---

archive/issue_comments_029125.json:
```json
{
    "body": "Thinking about it. I think it would be less confusing if this ticket is just closed and anything new for fricas put into a new one.  ~ Adam",
    "created_at": "2009-08-27T13:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29125",
    "user": "@maxthemouse"
}
```

Thinking about it. I think it would be less confusing if this ticket is just closed and anything new for fricas put into a new one.  ~ Adam



---

archive/issue_comments_029126.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-05T06:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29126",
    "user": "@mwhansen"
}
```

Resolution: duplicate



---

archive/issue_comments_029127.json:
```json
{
    "body": "This was indeed fixed as part of #5111.  I'm going ahead and closing it.",
    "created_at": "2009-10-05T06:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4036#issuecomment-29127",
    "user": "@mwhansen"
}
```

This was indeed fixed as part of #5111.  I'm going ahead and closing it.
