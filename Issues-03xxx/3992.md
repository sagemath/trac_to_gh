# Issue 3992: [with patch, with positive review] Sage 3.1.2.alpha2: three tests in sage/interfaces/octave.py need to be optional

archive/issues_003992.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @JohnCremona\n\n```\nsage -t  devel/sage/sage/interfaces/octave.py \n********************************************************************** \nFile \"/home/jec/sage-3.1.2.alpha2/tmp/octave.py\", line 279: \n    sage: octave.set('x', '2') #optonal -- requires Octave \nException raised: \n    Traceback (most recent call last): \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/doctest.py\", \nline 1228, in __run \n        compileflags, 1) in test.globs \n      File \"<doctest __main__.example_10[2]>\", line 1, in <module> \n        octave.set('x', '2') #optonal -- requires Octave###line 279: \n    sage: octave.set('x', '2') #optonal -- requires Octave \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py\", \nline 284, in set \n        out = self.eval(cmd) \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py\", \nline 935, in eval \n        return '\\n'.join([self._eval_line(L, **kwds) for L in \ncode.split('\\n') if L != '']) \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py\", \nline 631, in _eval_line \n        self._start() \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py\", \nline 270, in _start \n        Expect._start(self) \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py\", \nline 455, in _start \n        self.__name, cmd, self._install_hints()) \n    RuntimeError: Unable to start octave because the command 'octave \n--no-line-editing --silent' failed. \n            You must get the program \"octave\" in order to use Octave \n            from SAGE.   You can read all about Octave at \n                    http://www.gnu.org/software/octave/ \n            LINUX / WINDOWS (colinux): \n               Do apt-get install octave as root on your machine \n               (or, in Windows, in the colinux console). \n            OS X: \n               * This website has links to binaries for OS X PowerPC \n                 and OS X Intel builds of the latest version of Octave: \n                         http://hpc.sourceforge.net/ \n                 Once you get the tarball from there, go to the / directory \n                 and type \n                         tar zxvf octave-intel-bin.tar.gz \n                 to extract it to usr/local/...   Make sure /usr/local/bin \n                 is in your PATH.  Then type \"octave\" and verify that \n                 octave starts up. \n               * Darwin ports and fink have Octave as well. \n********************************************************************** \nFile \"/home/jec/sage-3.1.2.alpha2/tmp/octave.py\", line 293: \n    sage: octave.set('x', '2') #optonal -- requires Octave \nException raised: \n    Traceback (most recent call last): \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/doctest.py\", \nline 1228, in __run \n        compileflags, 1) in test.globs \n      File \"<doctest __main__.example_11[2]>\", line 1, in <module> \n        octave.set('x', '2') #optonal -- requires Octave###line 293: \n    sage: octave.set('x', '2') #optonal -- requires Octave \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py\", \nline 284, in set \n        out = self.eval(cmd) \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py\", \nline 935, in eval \n        return '\\n'.join([self._eval_line(L, **kwds) for L in \ncode.split('\\n') if L != '']) \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py\", \nline 631, in _eval_line \n        self._start() \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py\", \nline 270, in _start \n        Expect._start(self) \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py\", \nline 455, in _start \n        self.__name, cmd, self._install_hints()) \n    RuntimeError: Unable to start octave because the command 'octave \n--no-line-editing --silent' failed. \n            You must get the program \"octave\" in order to use Octave \n            from SAGE.   You can read all about Octave at \n                    http://www.gnu.org/software/octave/ \n            LINUX / WINDOWS (colinux): \n               Do apt-get install octave as root on your machine \n               (or, in Windows, in the colinux console). \n            OS X: \n               * This website has links to binaries for OS X PowerPC \n                 and OS X Intel builds of the latest version of Octave: \n                         http://hpc.sourceforge.net/ \n                 Once you get the tarball from there, go to the / directory \n                 and type \n                         tar zxvf octave-intel-bin.tar.gz \n                 to extract it to usr/local/...   Make sure /usr/local/bin \n                 is in your PATH.  Then type \"octave\" and verify that \n                 octave starts up. \n               * Darwin ports and fink have Octave as well. \n********************************************************************** \nFile \"/home/jec/sage-3.1.2.alpha2/tmp/octave.py\", line 306: \n    sage: octave.set('x', '2') #optonal -- requires Octave \nException raised: \n    Traceback (most recent call last): \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/doctest.py\", \nline 1228, in __run \n        compileflags, 1) in test.globs \n      File \"<doctest __main__.example_12[2]>\", line 1, in <module> \n        octave.set('x', '2') #optonal -- requires Octave###line 306: \n    sage: octave.set('x', '2') #optonal -- requires Octave \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py\", \nline 284, in set \n        out = self.eval(cmd) \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py\", \nline 935, in eval \n        return '\\n'.join([self._eval_line(L, **kwds) for L in \ncode.split('\\n') if L != '']) \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py\", \nline 631, in _eval_line \n        self._start() \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py\", \nline 270, in _start \n        Expect._start(self) \n      File \"/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py\", \nline 455, in _start \n        self.__name, cmd, self._install_hints()) \n    RuntimeError: Unable to start octave because the command 'octave \n--no-line-editing --silent' failed. \n            You must get the program \"octave\" in order to use Octave \n            from SAGE.   You can read all about Octave at \n                    http://www.gnu.org/software/octave/ \n            LINUX / WINDOWS (colinux): \n               Do apt-get install octave as root on your machine \n               (or, in Windows, in the colinux console). \n            OS X: \n               * This website has links to binaries for OS X PowerPC \n                 and OS X Intel builds of the latest version of Octave: \n                         http://hpc.sourceforge.net/ \n                 Once you get the tarball from there, go to the / directory \n                 and type \n                         tar zxvf octave-intel-bin.tar.gz \n                 to extract it to usr/local/...   Make sure /usr/local/bin \n                 is in your PATH.  Then type \"octave\" and verify that \n                 octave starts up. \n               * Darwin ports and fink have Octave as well. \n********************************************************************** \n3 items had failures: \n   1 of   3 in __main__.example_10 \n   1 of   3 in __main__.example_11 \n   1 of   3 in __main__.example_12 \n***Test Failed*** 3 failures. \nFor whitespace errors, see the file \n/home/jec/sage-3.1.2.alpha2/tmp/.doctest_octave.py \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3992\n\n",
    "closed_at": "2008-08-29T18:29:24Z",
    "created_at": "2008-08-29T17:07:08Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, with positive review] Sage 3.1.2.alpha2: three tests in sage/interfaces/octave.py need to be optional",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3992",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @JohnCremona

```
sage -t  devel/sage/sage/interfaces/octave.py 
********************************************************************** 
File "/home/jec/sage-3.1.2.alpha2/tmp/octave.py", line 279: 
    sage: octave.set('x', '2') #optonal -- requires Octave 
Exception raised: 
    Traceback (most recent call last): 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/doctest.py", 
line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_10[2]>", line 1, in <module> 
        octave.set('x', '2') #optonal -- requires Octave###line 279: 
    sage: octave.set('x', '2') #optonal -- requires Octave 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py", 
line 284, in set 
        out = self.eval(cmd) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 935, in eval 
        return '\n'.join([self._eval_line(L, **kwds) for L in 
code.split('\n') if L != '']) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 631, in _eval_line 
        self._start() 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py", 
line 270, in _start 
        Expect._start(self) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 455, in _start 
        self.__name, cmd, self._install_hints()) 
    RuntimeError: Unable to start octave because the command 'octave 
--no-line-editing --silent' failed. 
            You must get the program "octave" in order to use Octave 
            from SAGE.   You can read all about Octave at 
                    http://www.gnu.org/software/octave/ 
            LINUX / WINDOWS (colinux): 
               Do apt-get install octave as root on your machine 
               (or, in Windows, in the colinux console). 
            OS X: 
               * This website has links to binaries for OS X PowerPC 
                 and OS X Intel builds of the latest version of Octave: 
                         http://hpc.sourceforge.net/ 
                 Once you get the tarball from there, go to the / directory 
                 and type 
                         tar zxvf octave-intel-bin.tar.gz 
                 to extract it to usr/local/...   Make sure /usr/local/bin 
                 is in your PATH.  Then type "octave" and verify that 
                 octave starts up. 
               * Darwin ports and fink have Octave as well. 
********************************************************************** 
File "/home/jec/sage-3.1.2.alpha2/tmp/octave.py", line 293: 
    sage: octave.set('x', '2') #optonal -- requires Octave 
Exception raised: 
    Traceback (most recent call last): 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/doctest.py", 
line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_11[2]>", line 1, in <module> 
        octave.set('x', '2') #optonal -- requires Octave###line 293: 
    sage: octave.set('x', '2') #optonal -- requires Octave 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py", 
line 284, in set 
        out = self.eval(cmd) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 935, in eval 
        return '\n'.join([self._eval_line(L, **kwds) for L in 
code.split('\n') if L != '']) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 631, in _eval_line 
        self._start() 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py", 
line 270, in _start 
        Expect._start(self) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 455, in _start 
        self.__name, cmd, self._install_hints()) 
    RuntimeError: Unable to start octave because the command 'octave 
--no-line-editing --silent' failed. 
            You must get the program "octave" in order to use Octave 
            from SAGE.   You can read all about Octave at 
                    http://www.gnu.org/software/octave/ 
            LINUX / WINDOWS (colinux): 
               Do apt-get install octave as root on your machine 
               (or, in Windows, in the colinux console). 
            OS X: 
               * This website has links to binaries for OS X PowerPC 
                 and OS X Intel builds of the latest version of Octave: 
                         http://hpc.sourceforge.net/ 
                 Once you get the tarball from there, go to the / directory 
                 and type 
                         tar zxvf octave-intel-bin.tar.gz 
                 to extract it to usr/local/...   Make sure /usr/local/bin 
                 is in your PATH.  Then type "octave" and verify that 
                 octave starts up. 
               * Darwin ports and fink have Octave as well. 
********************************************************************** 
File "/home/jec/sage-3.1.2.alpha2/tmp/octave.py", line 306: 
    sage: octave.set('x', '2') #optonal -- requires Octave 
Exception raised: 
    Traceback (most recent call last): 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/doctest.py", 
line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_12[2]>", line 1, in <module> 
        octave.set('x', '2') #optonal -- requires Octave###line 306: 
    sage: octave.set('x', '2') #optonal -- requires Octave 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py", 
line 284, in set 
        out = self.eval(cmd) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 935, in eval 
        return '\n'.join([self._eval_line(L, **kwds) for L in 
code.split('\n') if L != '']) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 631, in _eval_line 
        self._start() 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py", 
line 270, in _start 
        Expect._start(self) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 455, in _start 
        self.__name, cmd, self._install_hints()) 
    RuntimeError: Unable to start octave because the command 'octave 
--no-line-editing --silent' failed. 
            You must get the program "octave" in order to use Octave 
            from SAGE.   You can read all about Octave at 
                    http://www.gnu.org/software/octave/ 
            LINUX / WINDOWS (colinux): 
               Do apt-get install octave as root on your machine 
               (or, in Windows, in the colinux console). 
            OS X: 
               * This website has links to binaries for OS X PowerPC 
                 and OS X Intel builds of the latest version of Octave: 
                         http://hpc.sourceforge.net/ 
                 Once you get the tarball from there, go to the / directory 
                 and type 
                         tar zxvf octave-intel-bin.tar.gz 
                 to extract it to usr/local/...   Make sure /usr/local/bin 
                 is in your PATH.  Then type "octave" and verify that 
                 octave starts up. 
               * Darwin ports and fink have Octave as well. 
********************************************************************** 
3 items had failures: 
   1 of   3 in __main__.example_10 
   1 of   3 in __main__.example_11 
   1 of   3 in __main__.example_12 
***Test Failed*** 3 failures. 
For whitespace errors, see the file 
/home/jec/sage-3.1.2.alpha2/tmp/.doctest_octave.py 
```

Issue created by migration from https://trac.sagemath.org/ticket/3992





---

archive/issue_comments_028633.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-29T17:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3992#issuecomment-28633",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028634.json:
```json
{
    "body": "Attachment [trac_3992.patch](tarball://root/attachments/some-uuid/ticket3992/trac_3992.patch) by mabshoff created at 2008-08-29 17:22:27\n\nJohn,\n\nsince you hit this can you do the (trivial) review?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-29T17:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3992#issuecomment-28634",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3992.patch](tarball://root/attachments/some-uuid/ticket3992/trac_3992.patch) by mabshoff created at 2008-08-29 17:22:27

John,

since you hit this can you do the (trivial) review?

Cheers,

Michael



---

archive/issue_comments_028635.json:
```json
{
    "body": "Patch applies and pases doctests on both the systems where it failed before.\n\nDone!",
    "created_at": "2008-08-29T18:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3992#issuecomment-28635",
    "user": "https://github.com/JohnCremona"
}
```

Patch applies and pases doctests on both the systems where it failed before.

Done!



---

archive/issue_comments_028636.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha3",
    "created_at": "2008-08-29T18:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3992#issuecomment-28636",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha3



---

archive/issue_events_009151.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-29T18:29:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3992",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3992#event-9151"
}
```



---

archive/issue_comments_028637.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-29T18:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3992#issuecomment-28637",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
