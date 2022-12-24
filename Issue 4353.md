# Issue 4353: [with patch, needs review] make sure garbage collection is reenabled after an exception in timeit.

archive/issues_004353.json:
```json
{
    "body": "Assignee: cwitty\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4353\n\n",
    "created_at": "2008-10-23T21:38:38Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] make sure garbage collection is reenabled after an exception in timeit.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4353",
    "user": "mhansen"
}
```
Assignee: cwitty



Issue created by migration from https://trac.sagemath.org/ticket/4353





---

archive/issue_comments_031966.json:
```json
{
    "body": "Attachment [trac_4353.patch](tarball://root/attachments/some-uuid/ticket4353/trac_4353.patch) by anakha created at 2008-10-23 22:01:21\n\nThis fixes the problem with timeit() but not with the magic version (%timeit).\n\nBut I realize that this one is a python problem.\n\n\n```\nsage: def f(): raise RuntimeError\n....: \nsage: gc.enable()\nsage: gc.isenabled()\nTrue\nsage: %timeit f()\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (17, 0))\n\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/Volumes/Place/anakha/Applications/sage/devel/<ipython console> in <module>()\n\n/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/IPython/iplib.pyc in ipmagic(self, arg_s)\n    958         else:\n    959             magic_args = self.var_expand(magic_args,1)\n--> 960             return fn(magic_args)\n    961 \n    962     def ipalias(self,arg_s):\n\n/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/IPython/Magic.pyc in magic_timeit(self, parameter_s)\n   1796             for i in range(1, 10):\n   1797                 number *= 10\n-> 1798                 if timer.timeit(number) >= 0.2:\n   1799                     break\n   1800         \n\n/Volumes/Place/anakha/Applications/sage/local/lib/python/timeit.pyc in timeit(self, number)\n    159         gcold = gc.isenabled()\n    160         gc.disable()\n--> 161         timing = self.inner(it, self.timer)\n    162         if gcold:\n    163             gc.enable()\n\n/Volumes/Place/anakha/Applications/sage/devel/<magic-timeit> in inner(_it, _timer)\n\n/Volumes/Place/anakha/Applications/sage/devel/<ipython console> in f()\n\nRuntimeError: \nsage: gc.isenabled()\nFalse\n```\n",
    "created_at": "2008-10-23T22:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4353#issuecomment-31966",
    "user": "anakha"
}
```

Attachment [trac_4353.patch](tarball://root/attachments/some-uuid/ticket4353/trac_4353.patch) by anakha created at 2008-10-23 22:01:21

This fixes the problem with timeit() but not with the magic version (%timeit).

But I realize that this one is a python problem.


```
sage: def f(): raise RuntimeError
....: 
sage: gc.enable()
sage: gc.isenabled()
True
sage: %timeit f()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (17, 0))

---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Volumes/Place/anakha/Applications/sage/devel/<ipython console> in <module>()

/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/IPython/iplib.pyc in ipmagic(self, arg_s)
    958         else:
    959             magic_args = self.var_expand(magic_args,1)
--> 960             return fn(magic_args)
    961 
    962     def ipalias(self,arg_s):

/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/IPython/Magic.pyc in magic_timeit(self, parameter_s)
   1796             for i in range(1, 10):
   1797                 number *= 10
-> 1798                 if timer.timeit(number) >= 0.2:
   1799                     break
   1800         

/Volumes/Place/anakha/Applications/sage/local/lib/python/timeit.pyc in timeit(self, number)
    159         gcold = gc.isenabled()
    160         gc.disable()
--> 161         timing = self.inner(it, self.timer)
    162         if gcold:
    163             gc.enable()

/Volumes/Place/anakha/Applications/sage/devel/<magic-timeit> in inner(_it, _timer)

/Volumes/Place/anakha/Applications/sage/devel/<ipython console> in f()

RuntimeError: 
sage: gc.isenabled()
False
```




---

archive/issue_comments_031967.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-26T03:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4353#issuecomment-31967",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha1



---

archive/issue_comments_031968.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T03:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4353#issuecomment-31968",
    "user": "mabshoff"
}
```

Resolution: fixed
