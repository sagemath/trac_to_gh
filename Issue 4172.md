# Issue 4172: exception in timeit permanetly disables gc

archive/issues_004172.json:
```json
{
    "body": "Assignee: mabshoff\n\n```\nsage: import gc\nsage: gc.isenabled()\nTrue\nsage: %timeit raise RuntimeError, \"test\"\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/Volumes/Place/anakha/Applications/sage/devel/sage-tri/sage/geometry/<ipython console> in <module>()\n\n/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/IPython/iplib.py in ipmagic(self, arg_s)\n    946         else:\n    947             magic_args = self.var_expand(magic_args,1)\n--> 948             return fn(magic_args)\n    949 \n    950     def ipalias(self,arg_s):\n\n/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/IPython/Magic.py in magic_timeit(self, parameter_s)\n   1779             for i in range(1, 10):\n   1780                 number *= 10\n-> 1781                 if timer.timeit(number) >= 0.2:\n   1782                     break\n   1783         \n\n/Volumes/Place/anakha/Applications/sage/local/lib/python/timeit.py in timeit(self, number)\n    159         gcold = gc.isenabled()\n    160         gc.disable()\n--> 161         timing = self.inner(it, self.timer)\n    162         if gcold:\n    163             gc.enable()\n\n/Volumes/Place/anakha/Applications/sage/devel/sage-tri/sage/geometry/<magic-timeit> in inner(_it, _timer)\n\nRuntimeError: test\nsage: gc.isenabled()\nFalse\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4172\n\n",
    "created_at": "2008-09-23T05:44:42Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "exception in timeit permanetly disables gc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4172",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```
Assignee: mabshoff

```
sage: import gc
sage: gc.isenabled()
True
sage: %timeit raise RuntimeError, "test"
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Volumes/Place/anakha/Applications/sage/devel/sage-tri/sage/geometry/<ipython console> in <module>()

/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/IPython/iplib.py in ipmagic(self, arg_s)
    946         else:
    947             magic_args = self.var_expand(magic_args,1)
--> 948             return fn(magic_args)
    949 
    950     def ipalias(self,arg_s):

/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/IPython/Magic.py in magic_timeit(self, parameter_s)
   1779             for i in range(1, 10):
   1780                 number *= 10
-> 1781                 if timer.timeit(number) >= 0.2:
   1782                     break
   1783         

/Volumes/Place/anakha/Applications/sage/local/lib/python/timeit.py in timeit(self, number)
    159         gcold = gc.isenabled()
    160         gc.disable()
--> 161         timing = self.inner(it, self.timer)
    162         if gcold:
    163             gc.enable()

/Volumes/Place/anakha/Applications/sage/devel/sage-tri/sage/geometry/<magic-timeit> in inner(_it, _timer)

RuntimeError: test
sage: gc.isenabled()
False
```

Issue created by migration from https://trac.sagemath.org/ticket/4172





---

archive/issue_comments_030215.json:
```json
{
    "body": "Patch is up at #4353",
    "created_at": "2008-10-23T21:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4172#issuecomment-30215",
    "user": "https://github.com/mwhansen"
}
```

Patch is up at #4353



---

archive/issue_events_009475.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-10-23T21:41:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4172",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4172#event-9475"
}
```



---

archive/issue_comments_030216.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-10-23T21:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4172#issuecomment-30216",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate
