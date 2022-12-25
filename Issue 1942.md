# Issue 1942: Sage 2.10.1.rc0: sage0.cputime()  broken on 32 bit FC7/8

archive/issues_001942.json:
```json
{
    "body": "Assignee: mabshoff\n\nJaap reports the following on 32 bit FC7/8 with Sage 2.10.1.rc0:\n\n```\n[jaap@paix sage-2.10.1.rc0]$ ./sage -t  devel/sage-main/sage/interfaces/sage0.py\nsage -t  devel/sage-main/sage/interfaces/sage0.py           **********************************************************************\nFile \"sage0.py\", line 143:\n     sage: _= sage0.cputime()     # random output\nException raised:\n     Traceback (most recent call last):\n       File \"/home/jaap/downloads/sage-2.10.1.rc0/local/lib/python2.5/doctest.py\", line 1212, in __run\n         compileflags, 1) in test.globs\n       File \"<doctest __main__.example_2[0]>\", line 1, in <module>\n         _= sage0.cputime()     # random output###line 143:\n     sage: _= sage0.cputime()     # random output\n       File \"/home/jaap/downloads/sage-2.10.1.rc0/local/lib/python2.5/site-packages/sage/interfaces/sage0.py\", line 150, in cputime\n         return eval(self.eval('cputime(%s)'%t))\n       File \"<string>\", line 1\n           1.3517939999999999\n          ^\n      SyntaxError: invalid syntax\n**********************************************************************\nFile \"sage0.py\", line 147:\n     sage: _= sage0.cputime()     # random output\nException raised:\n     Traceback (most recent call last):\n       File \"/home/jaap/downloads/sage-2.10.1.rc0/local/lib/python2.5/doctest.py\", line 1212, in __run\n         compileflags, 1) in test.globs\n       File \"<doctest __main__.example_2[2]>\", line 1, in <module>\n         _= sage0.cputime()     # random output###line 147:\n     sage: _= sage0.cputime()     # random output\n       File \"/home/jaap/downloads/sage-2.10.1.rc0/local/lib/python2.5/site-packages/sage/interfaces/sage0.py\", line 150, in cputime\n         return eval(self.eval('cputime(%s)'%t))\n       File \"<string>\", line 1\n           1.726736\n          ^\n      SyntaxError: invalid syntax\n**********************************************************************\n1 items had failures:\n    2 of   3 in __main__.example_2\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file .doctest_sage0.py\n          [6.9 s]\nexit code: 256 \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1942\n\n",
    "created_at": "2008-01-26T23:10:50Z",
    "labels": [
        "component: packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage 2.10.1.rc0: sage0.cputime()  broken on 32 bit FC7/8",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1942",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Jaap reports the following on 32 bit FC7/8 with Sage 2.10.1.rc0:

```
[jaap@paix sage-2.10.1.rc0]$ ./sage -t  devel/sage-main/sage/interfaces/sage0.py
sage -t  devel/sage-main/sage/interfaces/sage0.py           **********************************************************************
File "sage0.py", line 143:
     sage: _= sage0.cputime()     # random output
Exception raised:
     Traceback (most recent call last):
       File "/home/jaap/downloads/sage-2.10.1.rc0/local/lib/python2.5/doctest.py", line 1212, in __run
         compileflags, 1) in test.globs
       File "<doctest __main__.example_2[0]>", line 1, in <module>
         _= sage0.cputime()     # random output###line 143:
     sage: _= sage0.cputime()     # random output
       File "/home/jaap/downloads/sage-2.10.1.rc0/local/lib/python2.5/site-packages/sage/interfaces/sage0.py", line 150, in cputime
         return eval(self.eval('cputime(%s)'%t))
       File "<string>", line 1
           1.3517939999999999
          ^
      SyntaxError: invalid syntax
**********************************************************************
File "sage0.py", line 147:
     sage: _= sage0.cputime()     # random output
Exception raised:
     Traceback (most recent call last):
       File "/home/jaap/downloads/sage-2.10.1.rc0/local/lib/python2.5/doctest.py", line 1212, in __run
         compileflags, 1) in test.globs
       File "<doctest __main__.example_2[2]>", line 1, in <module>
         _= sage0.cputime()     # random output###line 147:
     sage: _= sage0.cputime()     # random output
       File "/home/jaap/downloads/sage-2.10.1.rc0/local/lib/python2.5/site-packages/sage/interfaces/sage0.py", line 150, in cputime
         return eval(self.eval('cputime(%s)'%t))
       File "<string>", line 1
           1.726736
          ^
      SyntaxError: invalid syntax
**********************************************************************
1 items had failures:
    2 of   3 in __main__.example_2
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_sage0.py
          [6.9 s]
exit code: 256 
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1942





---

archive/issue_comments_012298.json:
```json
{
    "body": "It doesn't happen on FC8 :)\n\nCheers,\n\nMichael",
    "created_at": "2008-01-26T23:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1942#issuecomment-12298",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

It doesn't happen on FC8 :)

Cheers,

Michael



---

archive/issue_comments_012299.json:
```json
{
    "body": "This is ./sage -t -verbose of .../sage0.py on Fedora7",
    "created_at": "2008-01-26T23:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1942#issuecomment-12299",
    "user": "https://github.com/jaapspies"
}
```

This is ./sage -t -verbose of .../sage0.py on Fedora7



---

archive/issue_comments_012300.json:
```json
{
    "body": "Attachment [test_sage0.log](tarball://root/attachments/some-uuid/ticket1942/test_sage0.log) by @jaapspies created at 2008-01-27 13:13:20\n\n\n```\n> > Also, could you try replacing the line 150 by\n> >           s = self.eval('cputime(%s)'%t)\n> >           print \"'%s'\"%s\n> >           return 0\n> > in case my above suggestion doesn't work, and report what gets printed.\n> > \n\nExiting SAGE (CPU time 0m0.00s, Wall time 0m8.03s).\n[jaap@paix sage-2.10.1.rc0]$ ./sage -t  devel/sage-main/sage/interfaces/sage0.py 2>&1 | tee -a test_sage0.log\nsage -t  devel/sage-main/sage/interfaces/sage0.py           **********************************************************************\nFile \"sage0.py\", line 143:\n     sage: _= sage0.cputime()     # random output\nExpected nothing\nGot:\n     ' 1.360792\n     '\n**********************************************************************\nFile \"sage0.py\", line 147:\n     sage: _= sage0.cputime()     # random output\nExpected nothing\nGot:\n     ' 1.7347349999999999\n     '\n**********************************************************************\n1 items had failures:\n    2 of   3 in __main__.example_2\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file .doctest_sage0.py\n          [7.0 s]\nexit code: 256\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n         sage -t  devel/sage-main/sage/interfaces/sage0.py\nTotal time for all tests: 7.0 seconds\n[jaap@paix sage-2.10.1.rc0]$\n\n```\n",
    "created_at": "2008-01-27T13:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1942#issuecomment-12300",
    "user": "https://github.com/jaapspies"
}
```

Attachment [test_sage0.log](tarball://root/attachments/some-uuid/ticket1942/test_sage0.log) by @jaapspies created at 2008-01-27 13:13:20


```
> > Also, could you try replacing the line 150 by
> >           s = self.eval('cputime(%s)'%t)
> >           print "'%s'"%s
> >           return 0
> > in case my above suggestion doesn't work, and report what gets printed.
> > 

Exiting SAGE (CPU time 0m0.00s, Wall time 0m8.03s).
[jaap@paix sage-2.10.1.rc0]$ ./sage -t  devel/sage-main/sage/interfaces/sage0.py 2>&1 | tee -a test_sage0.log
sage -t  devel/sage-main/sage/interfaces/sage0.py           **********************************************************************
File "sage0.py", line 143:
     sage: _= sage0.cputime()     # random output
Expected nothing
Got:
     ' 1.360792
     '
**********************************************************************
File "sage0.py", line 147:
     sage: _= sage0.cputime()     # random output
Expected nothing
Got:
     ' 1.7347349999999999
     '
**********************************************************************
1 items had failures:
    2 of   3 in __main__.example_2
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_sage0.py
          [7.0 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


         sage -t  devel/sage-main/sage/interfaces/sage0.py
Total time for all tests: 7.0 seconds
[jaap@paix sage-2.10.1.rc0]$

```




---

archive/issue_comments_012301.json:
```json
{
    "body": "As William suspected there are some control characters in there, which Jaap confirmed:\n\n```\n> I have to say -- I just don't get why this doesn't work on your FC7 machine.\n> All that it is doing is eval'ing a correct float constant...  I wonder if there\n> are weird hidden invisible control codes in the output or something.\n> \n\nThis is from the log file:\n     ValueError: invalid literal for float(): ^[[0;31m ^[[0m1.8237209999999999\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-01-27T14:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1942#issuecomment-12301",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

As William suspected there are some control characters in there, which Jaap confirmed:

```
> I have to say -- I just don't get why this doesn't work on your FC7 machine.
> All that it is doing is eval'ing a correct float constant...  I wonder if there
> are weird hidden invisible control codes in the output or something.
> 

This is from the log file:
     ValueError: invalid literal for float(): ^[[0;31m ^[[0m1.8237209999999999
```


Cheers,

Michael



---

archive/issue_comments_012302.json:
```json
{
    "body": "Craig opened another ticket for the same issue: #1958. Since we have a patch over there close this as a duplicate.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-28T06:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1942#issuecomment-12302",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Craig opened another ticket for the same issue: #1958. Since we have a patch over there close this as a duplicate.

Cheers,

Michael



---

archive/issue_comments_012303.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-01-28T06:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1942#issuecomment-12303",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_events_002097.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-28T06:37:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1942",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1942#event-2097"
}
```
