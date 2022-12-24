# Issue 3604: zlib: Conditional jump or move depends on uninitialised value(s)

archive/issues_003604.json:
```json
{
    "body": "Assignee: mabshoff\n\nValgrind says:\n\n```\n==10847== Conditional jump or move depends on uninitialised value(s)\n==10847==    at 0x7D39F9D: longest_match (deflate.c:1121)\n==10847==    by 0x7D3B368: deflate_slow (deflate.c:1595)\n==10847==    by 0x7D39462: deflate (deflate.c:790)\n==10847==    by 0x7C2D96A: PyZlib_compress (zlibmodule.c:166)\n==10847==    by 0x4F0F28: PyCFunction_Call (methodobject.c:73)\n==10847==    by 0x41B0FA: PyObject_Call (abstract.c:1861)\n==10847==    by 0x7B0C9A9: __pyx_pf_4sage_9structure_11sage_object_10SageObject_dumps (sage_object.c:1591)\n==10847==    by 0x4F0F43: PyCFunction_Call (methodobject.c:77)\n==10847==    by 0x41B0FA: PyObject_Call (abstract.c:1861)\n==10847==    by 0x7B197E8: __pyx_pf_4sage_9structure_11sage_object_dumps (sage_object.c:5184)\n==10847==    by 0x4F0F43: PyCFunction_Call (methodobject.c:77)\n==10847==    by 0x494A6E: call_function (ceval.c:3573)\n```\n\nThis corresponds to:\n\n```\ndef dumps(obj, compress=True):\n    \"\"\"\n    dumps(obj):\n\n    Dump obj to a string s.  To recover obj, use loads(s).\n\n    EXAMPLES:\n        sage: a = 2/3\n        sage: s = dumps(a)\n        sage: print len(s)\n        49\n        sage: loads(s)\n        2/3\n    \"\"\"\n    if make_pickle_jar:\n        picklejar(obj)\n    try:\n        return obj.dumps(compress) [this is sage_object.c:5184]\n    except (AttributeError, RuntimeError, TypeError):\n        if compress:\n            return comp.compress(cPickle.dumps(obj, protocol=2))\n        else:\n            return cPickle.dumps(obj, protocol=2)\n```\n\nAnd\n\n```\n    def dumps(self, compress=True):\n        \"\"\"\n        Dump self to a string s, which can later be reconstituted\n        as self using loads(s).\n        \"\"\"\n        # the protocol=2 is very important -- this enables\n        # saving extensions classes (with no attributes).\n        s = cPickle.dumps(self, protocol=2)\n        if compress:\n            return comp.compress(s) [sage_object.c:1591]\n        else:\n            return s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3604\n\n",
    "created_at": "2008-07-08T11:41:58Z",
    "labels": [
        "memleak",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "zlib: Conditional jump or move depends on uninitialised value(s)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3604",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Valgrind says:

```
==10847== Conditional jump or move depends on uninitialised value(s)
==10847==    at 0x7D39F9D: longest_match (deflate.c:1121)
==10847==    by 0x7D3B368: deflate_slow (deflate.c:1595)
==10847==    by 0x7D39462: deflate (deflate.c:790)
==10847==    by 0x7C2D96A: PyZlib_compress (zlibmodule.c:166)
==10847==    by 0x4F0F28: PyCFunction_Call (methodobject.c:73)
==10847==    by 0x41B0FA: PyObject_Call (abstract.c:1861)
==10847==    by 0x7B0C9A9: __pyx_pf_4sage_9structure_11sage_object_10SageObject_dumps (sage_object.c:1591)
==10847==    by 0x4F0F43: PyCFunction_Call (methodobject.c:77)
==10847==    by 0x41B0FA: PyObject_Call (abstract.c:1861)
==10847==    by 0x7B197E8: __pyx_pf_4sage_9structure_11sage_object_dumps (sage_object.c:5184)
==10847==    by 0x4F0F43: PyCFunction_Call (methodobject.c:77)
==10847==    by 0x494A6E: call_function (ceval.c:3573)
```

This corresponds to:

```
def dumps(obj, compress=True):
    """
    dumps(obj):

    Dump obj to a string s.  To recover obj, use loads(s).

    EXAMPLES:
        sage: a = 2/3
        sage: s = dumps(a)
        sage: print len(s)
        49
        sage: loads(s)
        2/3
    """
    if make_pickle_jar:
        picklejar(obj)
    try:
        return obj.dumps(compress) [this is sage_object.c:5184]
    except (AttributeError, RuntimeError, TypeError):
        if compress:
            return comp.compress(cPickle.dumps(obj, protocol=2))
        else:
            return cPickle.dumps(obj, protocol=2)
```

And

```
    def dumps(self, compress=True):
        """
        Dump self to a string s, which can later be reconstituted
        as self using loads(s).
        """
        # the protocol=2 is very important -- this enables
        # saving extensions classes (with no attributes).
        s = cPickle.dumps(self, protocol=2)
        if compress:
            return comp.compress(s) [sage_object.c:1591]
        else:
            return s
```


Issue created by migration from https://trac.sagemath.org/ticket/3604





---

archive/issue_comments_025465.json:
```json
{
    "body": "I suspect the underlying issue to be in zlib itself.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-08T11:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3604#issuecomment-25465",
    "user": "mabshoff"
}
```

I suspect the underlying issue to be in zlib itself.

Cheers,

Michael



---

archive/issue_comments_025466.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-08T11:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3604#issuecomment-25466",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025467.json:
```json
{
    "body": "This happens in many cases, the specific valgrind log is from elementary.py.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-08T11:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3604#issuecomment-25467",
    "user": "mabshoff"
}
```

This happens in many cases, the specific valgrind log is from elementary.py.

Cheers,

Michael



---

archive/issue_comments_025468.json:
```json
{
    "body": "The zlib people say this isn't an actual problem, and fixing it would slow things down, so they won't fix it:\nhttp://bugs.debian.org/cgi-bin/bugreport.cgi?bug=270070",
    "created_at": "2008-07-10T03:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3604#issuecomment-25468",
    "user": "cwitty"
}
```

The zlib people say this isn't an actual problem, and fixing it would slow things down, so they won't fix it:
http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=270070



---

archive/issue_comments_025469.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-19T01:09:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3604#issuecomment-25469",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025470.json:
```json
{
    "body": "This is wontfix, but I have added a suppression for this issue in the latest valgrind.spkg.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-19T01:09:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3604#issuecomment-25470",
    "user": "mabshoff"
}
```

This is wontfix, but I have added a suppression for this issue in the latest valgrind.spkg.

Cheers,

Michael
