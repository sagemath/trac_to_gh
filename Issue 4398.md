# Issue 4398: Sage 3.1.4: magma related optional doctest failure in sage/sage/modules/free_module.py

archive/issues_004398.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nmabshoff@iras:~/build-3.2.a1/sage-3.2.alpha1-iras> ./sage -t -long -optional devel/sage/sage/modules/free_module.py\nsage -t -long -optional devel/sage/sage/modules/free_module.py\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/free_module.py\", line 1554:\n    sage: magma(FreeModule(Integers(8), 2))             # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_52[2]>\", line 1, in <module>\n        magma(FreeModule(Integers(Integer(8)), Integer(2)))             # optional###line 1554:\n    sage: magma(FreeModule(Integers(8), 2))             # optional\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 509, in __call__\n        return Expect.__call__(self, x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 993, in _coerce_from_special_method\n        return self(x._interface_init_())\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 509, in __call__\n        return Expect.__call__(self, x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 965, in __call__\n        return cls(self, x, name=name)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1293, in __init__\n        raise TypeError, x\n    TypeError: Error evaluating Magma code.\n    IN:\n[1] := Ambient free module of rank 2 over Ring of integers modulo 8;\n    OUT:\n    >> _sage_[1] := Ambient free module of rank 2 over Ring of integers modulo 8;\n                            ^\n    User error: bad syntax\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/free_module.py\", line 1557:\n    sage: magma(FreeModule(QQ, 9))                      # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_52[3]>\", line 1, in <module>\n        magma(FreeModule(QQ, Integer(9)))                      # optional###line 1557:\n    sage: magma(FreeModule(QQ, 9))                      # optional\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 509, in __call__\n        return Expect.__call__(self, x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 993, in _coerce_from_special_method\n        return self(x._interface_init_())\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 509, in __call__\n        return Expect.__call__(self, x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 965, in __call__\n        return cls(self, x, name=name)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1293, in __init__\n        raise TypeError, x\n    TypeError: Error evaluating Magma code.\n    IN:\n[2] := Vector space of dimension 9 over Rational Field;\n    OUT:\n    >> _sage_[2] := Vector space of dimension 9 over Rational Field;\n                           ^\n    User error: bad syntax\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/free_module.py\", line 1560:\n    sage: magma(FreeModule(QQ['x'], 2))                 # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_52[4]>\", line 1, in <module>\n        magma(FreeModule(QQ['x'], Integer(2)))                 # optional###line 1560:\n    sage: magma(FreeModule(QQ['x'], 2))                 # optional\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 509, in __call__\n        return Expect.__call__(self, x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 993, in _coerce_from_special_method\n        return self(x._interface_init_())\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 509, in __call__\n        return Expect.__call__(self, x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 965, in __call__\n        return cls(self, x, name=name)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1293, in __init__\n        raise TypeError, x\n    TypeError: Error evaluating Magma code.\n    IN:\n[3] := Ambient free module of rank 2 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field;\n    OUT:\n    In file \"/home/mabshoff/.sage//temp/iras/20303//interface//tmp20303\", line 1, column 22:\n    >> _sage_[3] := Ambient free module of rank 2 over the principal ideal domain \n                            ^\n    User error: bad syntax\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/free_module.py\", line 1565:\n    sage: magma(M)                                      # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_52[7]>\", line 1, in <module>\n        magma(M)                                      # optional###line 1565:\n    sage: magma(M)                                      # optional\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 509, in __call__\n        return Expect.__call__(self, x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 991, in _coerce_from_special_method\n        return (x.__getattribute__(s))(self)\n      File \"sage_object.pyx\", line 370, in sage.structure.sage_object.SageObject._magma_ (sage/structure/sage_object.c:3379)\n      File \"sage_object.pyx\", line 415, in sage.structure.sage_object.SageObject._magma_convert_ (sage/structure/sage_object.c:3509)\n      File \"sage_object.pyx\", line 246, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2186)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 509, in __call__\n        return Expect.__call__(self, x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 965, in __call__\n        return cls(self, x, name=name)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1293, in __init__\n        raise TypeError, x\n    TypeError: Error evaluating Magma code.\n    IN:\n[4] := RSpace(IntegerRing(), 2, [ 1  0]\n    [ 0 -1]);\n    OUT:\n    >> _sage_[4] := RSpace(IntegerRing(), 2, [ 1  0]\n                                                  ^\n    User error: bad syntax\n\n    >> [ 0 -1]);\n              ^\n    User error: bad syntax\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4398\n\n",
    "created_at": "2008-10-30T17:08:26Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Sage 3.1.4: magma related optional doctest failure in sage/sage/modules/free_module.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4398",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein


```
mabshoff@iras:~/build-3.2.a1/sage-3.2.alpha1-iras> ./sage -t -long -optional devel/sage/sage/modules/free_module.py
sage -t -long -optional devel/sage/sage/modules/free_module.py
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/free_module.py", line 1554:
    sage: magma(FreeModule(Integers(8), 2))             # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[2]>", line 1, in <module>
        magma(FreeModule(Integers(Integer(8)), Integer(2)))             # optional###line 1554:
    sage: magma(FreeModule(Integers(8), 2))             # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 993, in _coerce_from_special_method
        return self(x._interface_init_())
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1293, in __init__
        raise TypeError, x
    TypeError: Error evaluating Magma code.
    IN:
[1] := Ambient free module of rank 2 over Ring of integers modulo 8;
    OUT:
    >> _sage_[1] := Ambient free module of rank 2 over Ring of integers modulo 8;
                            ^
    User error: bad syntax
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/free_module.py", line 1557:
    sage: magma(FreeModule(QQ, 9))                      # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[3]>", line 1, in <module>
        magma(FreeModule(QQ, Integer(9)))                      # optional###line 1557:
    sage: magma(FreeModule(QQ, 9))                      # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 993, in _coerce_from_special_method
        return self(x._interface_init_())
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1293, in __init__
        raise TypeError, x
    TypeError: Error evaluating Magma code.
    IN:
[2] := Vector space of dimension 9 over Rational Field;
    OUT:
    >> _sage_[2] := Vector space of dimension 9 over Rational Field;
                           ^
    User error: bad syntax
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/free_module.py", line 1560:
    sage: magma(FreeModule(QQ['x'], 2))                 # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[4]>", line 1, in <module>
        magma(FreeModule(QQ['x'], Integer(2)))                 # optional###line 1560:
    sage: magma(FreeModule(QQ['x'], 2))                 # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 993, in _coerce_from_special_method
        return self(x._interface_init_())
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1293, in __init__
        raise TypeError, x
    TypeError: Error evaluating Magma code.
    IN:
[3] := Ambient free module of rank 2 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field;
    OUT:
    In file "/home/mabshoff/.sage//temp/iras/20303//interface//tmp20303", line 1, column 22:
    >> _sage_[3] := Ambient free module of rank 2 over the principal ideal domain 
                            ^
    User error: bad syntax
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/free_module.py", line 1565:
    sage: magma(M)                                      # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[7]>", line 1, in <module>
        magma(M)                                      # optional###line 1565:
    sage: magma(M)                                      # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 991, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "sage_object.pyx", line 370, in sage.structure.sage_object.SageObject._magma_ (sage/structure/sage_object.c:3379)
      File "sage_object.pyx", line 415, in sage.structure.sage_object.SageObject._magma_convert_ (sage/structure/sage_object.c:3509)
      File "sage_object.pyx", line 246, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2186)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1293, in __init__
        raise TypeError, x
    TypeError: Error evaluating Magma code.
    IN:
[4] := RSpace(IntegerRing(), 2, [ 1  0]
    [ 0 -1]);
    OUT:
    >> _sage_[4] := RSpace(IntegerRing(), 2, [ 1  0]
                                                  ^
    User error: bad syntax

    >> [ 0 -1]);
              ^
    User error: bad syntax
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4398





---

archive/issue_comments_032296.json:
```json
{
    "body": "Attachment [sage-4398.patch](tarball://root/attachments/some-uuid/ticket4398/sage-4398.patch) by @williamstein created at 2008-10-30 21:12:15",
    "created_at": "2008-10-30T21:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4398#issuecomment-32296",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4398.patch](tarball://root/attachments/some-uuid/ticket4398/sage-4398.patch) by @williamstein created at 2008-10-30 21:12:15



---

archive/issue_comments_032297.json:
```json
{
    "body": "Positive review since the patch fixes the Magma optional doctests.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T20:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4398#issuecomment-32297",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review since the patch fixes the Magma optional doctests.

Cheers,

Michael



---

archive/issue_events_004643.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-10-31T20:20:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4398",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4398#event-4643"
}
```



---

archive/issue_comments_032298.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T20:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4398#issuecomment-32298",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_032299.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T20:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4398#issuecomment-32299",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
