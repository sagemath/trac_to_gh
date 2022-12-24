# Issue 4393: Sage 3.1.4: magma related optional doctest failure in sage/structure/element.pyx

archive/issues_004393.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nmabshoff@iras:~/build-3.2.a1/sage-3.2.alpha1-iras> ./sage -t -long -optional devel/sage/sage/structure/element.pyx\nsage -t -long -optional devel/sage/sage/structure/element.pyx\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py\", line 1566:\n    sage: mv = magma(v); mv                     # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_58[3]>\", line 1, in <module>\n        mv = magma(v); mv                     # optional###line 1566:\n    sage: mv = magma(v); mv                     # optional\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 509, in __call__\n        return Expect.__call__(self, x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 993, in _coerce_from_special_method\n        return self(x._interface_init_())\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 509, in __call__\n        return Expect.__call__(self, x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 965, in __call__\n        return cls(self, x, name=name)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1293, in __init__\n        raise TypeError, x\n    TypeError: Error evaluating Magma code.\n    IN:\n[1] := (1, 2, 3);\n    OUT:\n    >> _sage_[1] := (1, 2, 3);\n                    ^\n    Runtime error in elt< ... >: No permutation group context in which to create cycle\n\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py\", line 1568:\n    sage: mv.Type()                             # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_58[4]>\", line 1, in <module>\n        mv.Type()                             # optional###line 1568:\n    sage: mv.Type()                             # optional\n    NameError: name 'mv' is not defined\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py\", line 1570:\n    sage: mv.Parent()                           # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_58[5]>\", line 1, in <module>\n        mv.Parent()                           # optional###line 1570:\n    sage: mv.Parent()                           # optional\n    NameError: name 'mv' is not defined\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py\", line 1574:\n    sage: mv = magma(v); mv                     # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_58[7]>\", line 1, in <module>\n        mv = magma(v); mv                     # optional###line 1574:\n    sage: mv = magma(v); mv                     # optional\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 509, in __call__\n        return Expect.__call__(self, x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 967, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 993, in _coerce_from_special_method\n        return self(x._interface_init_())\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 509, in __call__\n        return Expect.__call__(self, x)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 965, in __call__\n        return cls(self, x, name=name)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1293, in __init__\n        raise TypeError, x\n    TypeError: Error evaluating Magma code.\n    IN:\n[2] := (1/2, 3/4, 5/6);\n    OUT:\n    >> _sage_[2] := (1/2, 3/4, 5/6);\n                    ^\n    Runtime error in elt< ... >: Bad arguments\n\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py\", line 1576:\n    sage: mv.Type()                             # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_58[8]>\", line 1, in <module>\n        mv.Type()                             # optional###line 1576:\n    sage: mv.Type()                             # optional\n    NameError: name 'mv' is not defined\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py\", line 1578:\n    sage: mv.Parent()                           # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_58[9]>\", line 1, in <module>\n        mv.Parent()                           # optional###line 1578:\n    sage: mv.Parent()                           # optional\n    NameError: name 'mv' is not defined\n**********************************************************************\n1 items had failures:\n   6 of  10 in __main__.example_58\n***Test Failed*** 6 failures.\nFor whitespace errors, see the file /home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/.doctest_element.py\n\t [14.7 s]\nexit code: 1024\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4393\n\n",
    "created_at": "2008-10-30T16:35:36Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Sage 3.1.4: magma related optional doctest failure in sage/structure/element.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4393",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
mabshoff@iras:~/build-3.2.a1/sage-3.2.alpha1-iras> ./sage -t -long -optional devel/sage/sage/structure/element.pyx
sage -t -long -optional devel/sage/sage/structure/element.pyx
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py", line 1566:
    sage: mv = magma(v); mv                     # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_58[3]>", line 1, in <module>
        mv = magma(v); mv                     # optional###line 1566:
    sage: mv = magma(v); mv                     # optional
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
[1] := (1, 2, 3);
    OUT:
    >> _sage_[1] := (1, 2, 3);
                    ^
    Runtime error in elt< ... >: No permutation group context in which to create cycle

**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py", line 1568:
    sage: mv.Type()                             # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_58[4]>", line 1, in <module>
        mv.Type()                             # optional###line 1568:
    sage: mv.Type()                             # optional
    NameError: name 'mv' is not defined
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py", line 1570:
    sage: mv.Parent()                           # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_58[5]>", line 1, in <module>
        mv.Parent()                           # optional###line 1570:
    sage: mv.Parent()                           # optional
    NameError: name 'mv' is not defined
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py", line 1574:
    sage: mv = magma(v); mv                     # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_58[7]>", line 1, in <module>
        mv = magma(v); mv                     # optional###line 1574:
    sage: mv = magma(v); mv                     # optional
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
[2] := (1/2, 3/4, 5/6);
    OUT:
    >> _sage_[2] := (1/2, 3/4, 5/6);
                    ^
    Runtime error in elt< ... >: Bad arguments

**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py", line 1576:
    sage: mv.Type()                             # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_58[8]>", line 1, in <module>
        mv.Type()                             # optional###line 1576:
    sage: mv.Type()                             # optional
    NameError: name 'mv' is not defined
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py", line 1578:
    sage: mv.Parent()                           # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_58[9]>", line 1, in <module>
        mv.Parent()                           # optional###line 1578:
    sage: mv.Parent()                           # optional
    NameError: name 'mv' is not defined
**********************************************************************
1 items had failures:
   6 of  10 in __main__.example_58
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/.doctest_element.py
	 [14.7 s]
exit code: 1024
```


Issue created by migration from https://trac.sagemath.org/ticket/4393





---

archive/issue_comments_032335.json:
```json
{
    "body": "Changing assignee from mabshoff to was.",
    "created_at": "2008-10-30T16:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4393#issuecomment-32335",
    "user": "mabshoff"
}
```

Changing assignee from mabshoff to was.



---

archive/issue_comments_032336.json:
```json
{
    "body": "Attachment [sage-4393.patch](tarball://root/attachments/some-uuid/ticket4393/sage-4393.patch) by was created at 2008-10-30 19:51:50",
    "created_at": "2008-10-30T19:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4393#issuecomment-32336",
    "user": "was"
}
```

Attachment [sage-4393.patch](tarball://root/attachments/some-uuid/ticket4393/sage-4393.patch) by was created at 2008-10-30 19:51:50



---

archive/issue_comments_032337.json:
```json
{
    "body": "Positive review. The doctests now pass:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ \n./sage -t -long -optional devel/sage/sage/structure/element.pyx\nsage -t -long -optional devel/sage/sage/structure/element.pyx\n\t [7.0 s]\n \n----------------------------------------------------------------------\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T20:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4393#issuecomment-32337",
    "user": "mabshoff"
}
```

Positive review. The doctests now pass:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ 
./sage -t -long -optional devel/sage/sage/structure/element.pyx
sage -t -long -optional devel/sage/sage/structure/element.pyx
	 [7.0 s]
 
----------------------------------------------------------------------
```


Cheers,

Michael



---

archive/issue_comments_032338.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T20:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4393#issuecomment-32338",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032339.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T20:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4393#issuecomment-32339",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2
