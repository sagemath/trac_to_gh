# Issue 6294: lisp command in sage is now totally broken (because of ecl switch)

archive/issues_006294.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @maxthemouse\n\n\n```\nwstein@bsd:~/build/sage-4.0.2.alpha3$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: lisp.eval('(+ 2 3)')\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n| Sage Version 4.0.2.alpha3, Release Date: 2009-06-13                |\n| Type notebook() for the GUI, and license() for information.        |\n/Users/was/.sage/temp/bsd.local/80207/_Users_was__sage_init_sage_0.py in <module>()\n\n/Users/was/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/lisp.pyc in eval(self, code, strip, **kwds)\n    116         \"\"\"\n    117         with gc_disabled():\n--> 118             self._synchronize()\n    119             code = str(code)\n    120             code = code.strip()\n\n/Users/was/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/lisp.pyc in _synchronize(self)\n    192         E = self._expect\n    193         if E is None:\n--> 194             self._start()\n    195             E = self._expect\n    196         r = random.randrange(2147483647)\n\n/Users/was/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/lisp.pyc in _start(self, *args, **kwds)\n    186             True\n    187         \"\"\"\n--> 188         Expect._start(self, *args, **kwds)\n    189         self.__in_seq = 1\n    190 \n\n/Users/was/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in _start(self, alt_message, block_during_init)\n    457             failed_to_start.append(self.__name)\n    458             raise RuntimeError, \"Unable to start %s because the command '%s' failed.\\n%s\"%(\n--> 459                 self.__name, cmd, self._install_hints())\n    460 \n    461         os.chdir(current_path)\n\nRuntimeError: Unable to start Lisp because the command 'clisp-noreadline --silent -on-error abort' failed.\n\nsage: \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6294\n\n",
    "created_at": "2009-06-15T09:21:19Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "lisp command in sage is now totally broken (because of ecl switch)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6294",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @maxthemouse


```
wstein@bsd:~/build/sage-4.0.2.alpha3$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: lisp.eval('(+ 2 3)')
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
| Sage Version 4.0.2.alpha3, Release Date: 2009-06-13                |
| Type notebook() for the GUI, and license() for information.        |
/Users/was/.sage/temp/bsd.local/80207/_Users_was__sage_init_sage_0.py in <module>()

/Users/was/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/lisp.pyc in eval(self, code, strip, **kwds)
    116         """
    117         with gc_disabled():
--> 118             self._synchronize()
    119             code = str(code)
    120             code = code.strip()

/Users/was/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/lisp.pyc in _synchronize(self)
    192         E = self._expect
    193         if E is None:
--> 194             self._start()
    195             E = self._expect
    196         r = random.randrange(2147483647)

/Users/was/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/lisp.pyc in _start(self, *args, **kwds)
    186             True
    187         """
--> 188         Expect._start(self, *args, **kwds)
    189         self.__in_seq = 1
    190 

/Users/was/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in _start(self, alt_message, block_during_init)
    457             failed_to_start.append(self.__name)
    458             raise RuntimeError, "Unable to start %s because the command '%s' failed.\n%s"%(
--> 459                 self.__name, cmd, self._install_hints())
    460 
    461         os.chdir(current_path)

RuntimeError: Unable to start Lisp because the command 'clisp-noreadline --silent -on-error abort' failed.

sage: 
```


Issue created by migration from https://trac.sagemath.org/ticket/6294





---

archive/issue_comments_050137.json:
```json
{
    "body": "Attachment [trac_6294-lisp_interface.patch](tarball://root/attachments/some-uuid/ticket6294/trac_6294-lisp_interface.patch) by @maxthemouse created at 2009-07-12 11:32:24\n\nAll I did was change the clisp command to ecl and the tests passed. The exception is version and I could not find an equivalent for ecl in the manual. For now I just put a string to refer to the console which does print the version number. I did not attempt to fill in any of the \"NotImplemented\" methods.\n\nAdam",
    "created_at": "2009-07-12T11:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6294#issuecomment-50137",
    "user": "https://github.com/maxthemouse"
}
```

Attachment [trac_6294-lisp_interface.patch](tarball://root/attachments/some-uuid/ticket6294/trac_6294-lisp_interface.patch) by @maxthemouse created at 2009-07-12 11:32:24

All I did was change the clisp command to ecl and the tests passed. The exception is version and I could not find an equivalent for ecl in the manual. For now I just put a string to refer to the console which does print the version number. I did not attempt to fill in any of the "NotImplemented" methods.

Adam



---

archive/issue_comments_050138.json:
```json
{
    "body": "I applied the patch on Sage 4.1.1. Lisp interface seems to work properly, code seems clean, and the doctests passed.",
    "created_at": "2009-08-30T09:40:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6294#issuecomment-50138",
    "user": "https://github.com/TimDumol"
}
```

I applied the patch on Sage 4.1.1. Lisp interface seems to work properly, code seems clean, and the doctests passed.



---

archive/issue_comments_050139.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-30T12:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6294#issuecomment-50139",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_006536.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-30T12:23:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6294",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6294#event-6536"
}
```
