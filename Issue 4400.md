# Issue 4400: Sage 3.1.4: magma related doctest failures in sage/interfaces/magma.py

archive/issues_004400.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is a strange one:\n\n```\nmabshoff@iras:~/build-3.2.a1/sage-3.2.alpha1-iras> ./sage -t -long -optional devel/sage/sage/interfaces/magma.py\nsage -t -long -optional devel/sage/sage/interfaces/magma.py \n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py\", line 1390:\n    sage: a.sage()                        # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[3]>\", line 1, in <module>\n        a.sage()                        # optional###line 1390:\n    sage: a.sage()                        # optional\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1406, in sage\n        return self._sage_()\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1433, in _sage_\n        z, preparse = self.Sage(nvals = 2)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1213, in __call__\n        nvals = nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 754, in function_call\n        return self._do_call(fun, nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 798, in _do_call\n        out = self.eval(cmd)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 383, in eval\n        raise RuntimeError, \"Error evaluating Magma code.\\nIN:%s\\nOUT:%s\"%(x, ans)\n    RuntimeError: Error evaluating Magma code.\n    IN:\n[15], _sage_[22] := Sage(_sage_[3]);\n    OUT:\n    >> _sage_[15], _sage_[22] := Sage(_sage_[3]);\n                              ^\n    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py\", line 1392:\n    sage: a._sage_()                      # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[4]>\", line 1, in <module>\n        a._sage_()                      # optional###line 1392:\n    sage: a._sage_()                      # optional\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1433, in _sage_\n        z, preparse = self.Sage(nvals = 2)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1213, in __call__\n        nvals = nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 754, in function_call\n        return self._do_call(fun, nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 798, in _do_call\n        out = self.eval(cmd)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 383, in eval\n        raise RuntimeError, \"Error evaluating Magma code.\\nIN:%s\\nOUT:%s\"%(x, ans)\n    RuntimeError: Error evaluating Magma code.\n    IN:\n[19], _sage_[28] := Sage(_sage_[8]);\n    OUT:\n    >> _sage_[19], _sage_[28] := Sage(_sage_[8]);\n                              ^\n    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py\", line 1394:\n    sage: type(a.sage())                  # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[5]>\", line 1, in <module>\n        type(a.sage())                  # optional###line 1394:\n    sage: type(a.sage())                  # optional\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1406, in sage\n        return self._sage_()\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1433, in _sage_\n        z, preparse = self.Sage(nvals = 2)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1213, in __call__\n        nvals = nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 754, in function_call\n        return self._do_call(fun, nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 798, in _do_call\n        out = self.eval(cmd)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 383, in eval\n        raise RuntimeError, \"Error evaluating Magma code.\\nIN:%s\\nOUT:%s\"%(x, ans)\n    RuntimeError: Error evaluating Magma code.\n    IN:\n[29], _sage_[30] := Sage(_sage_[3]);\n    OUT:\n    >> _sage_[29], _sage_[30] := Sage(_sage_[3]);\n                              ^\n    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py\", line 1400:\n    sage: b = a.sage(); b             # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[8]>\", line 1, in <module>\n        b = a.sage(); b             # optional###line 1400:\n    sage: b = a.sage(); b             # optional\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1406, in sage\n        return self._sage_()\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1433, in _sage_\n        z, preparse = self.Sage(nvals = 2)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1213, in __call__\n        nvals = nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 754, in function_call\n        return self._do_call(fun, nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 798, in _do_call\n        out = self.eval(cmd)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 383, in eval\n        raise RuntimeError, \"Error evaluating Magma code.\\nIN:%s\\nOUT:%s\"%(x, ans)\n    RuntimeError: Error evaluating Magma code.\n    IN:\n[32], _sage_[33] := Sage(_sage_[26]);\n    OUT:\n    >> _sage_[32], _sage_[33] := Sage(_sage_[26]);\n                              ^\n    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py\", line 1402:\n    sage: type(b)                         # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[9]>\", line 1, in <module>\n        type(b)                         # optional###line 1402:\n    sage: type(b)                         # optional\n    NameError: name 'b' is not defined\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py\", line 1404:\n    sage: c = magma(b); c                 # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[10]>\", line 1, in <module>\n        c = magma(b); c                 # optional###line 1404:\n    sage: c = magma(b); c                 # optional\n    NameError: name 'b' is not defined\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py\", line 1406:\n    sage: c.Type()                        # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[11]>\", line 1, in <module>\n        c.Type()                        # optional###line 1406:\n    sage: c.Type()                        # optional\n    NameError: name 'c' is not defined\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py\", line 1411:\n    sage: z = m.sage(); z                      # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[13]>\", line 1, in <module>\n        z = m.sage(); z                      # optional###line 1411:\n    sage: z = m.sage(); z                      # optional\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1406, in sage\n        return self._sage_()\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1433, in _sage_\n        z, preparse = self.Sage(nvals = 2)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1213, in __call__\n        nvals = nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 754, in function_call\n        return self._do_call(fun, nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 798, in _do_call\n        out = self.eval(cmd)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 383, in eval\n        raise RuntimeError, \"Error evaluating Magma code.\\nIN:%s\\nOUT:%s\"%(x, ans)\n    RuntimeError: Error evaluating Magma code.\n    IN:\n[26], _sage_[34] := Sage(_sage_[4]);\n    OUT:\n    >> _sage_[26], _sage_[34] := Sage(_sage_[4]);\n                              ^\n    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py\", line 1413:\n    sage: type(z)                              # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[14]>\", line 1, in <module>\n        type(z)                              # optional###line 1413:\n    sage: type(z)                              # optional\n    NameError: name 'z' is not defined\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py\", line 1419:\n    sage: b = m.sage(); b                     # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[17]>\", line 1, in <module>\n        b = m.sage(); b                     # optional###line 1419:\n    sage: b = m.sage(); b                     # optional\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1406, in sage\n        return self._sage_()\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1433, in _sage_\n        z, preparse = self.Sage(nvals = 2)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1213, in __call__\n        nvals = nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 754, in function_call\n        return self._do_call(fun, nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 798, in _do_call\n        out = self.eval(cmd)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 383, in eval\n        raise RuntimeError, \"Error evaluating Magma code.\\nIN:%s\\nOUT:%s\"%(x, ans)\n    RuntimeError: Error evaluating Magma code.\n    IN:\n[3], _sage_[35] := Sage(_sage_[4]);\n    OUT:\n    >> _sage_[3], _sage_[35] := Sage(_sage_[4]);\n                             ^\n    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py\", line 1423:\n    sage: b == a                             # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[18]>\", line 1, in <module>\n        b == a                             # optional###line 1423:\n    sage: b == a                             # optional\n    NameError: name 'b' is not defined\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py\", line 1429:\n    sage: m.sage()                           # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[21]>\", line 1, in <module>\n        m.sage()                           # optional###line 1429:\n    sage: m.sage()                           # optional\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1406, in sage\n        return self._sage_()\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1433, in _sage_\n        z, preparse = self.Sage(nvals = 2)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 1213, in __call__\n        nvals = nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 754, in function_call\n        return self._do_call(fun, nvals)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 798, in _do_call\n        out = self.eval(cmd)\n      File \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 383, in eval\n        raise RuntimeError, \"Error evaluating Magma code.\\nIN:%s\\nOUT:%s\"%(x, ans)\n    RuntimeError: Error evaluating Magma code.\n    IN:\n[8], _sage_[37] := Sage(_sage_[4]);\n    OUT:\n    >> _sage_[8], _sage_[37] := Sage(_sage_[4]);\n                             ^\n    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)\n**********************************************************************\n1 items had failures:\n  12 of  22 in __main__.example_49\n***Test Failed*** 12 failures.\nFor whitespace errors, see the file /home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/.doctest_magma.py\n\t [52.9 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long -optional devel/sage/sage/interfaces/magma.py\nTotal time for all tests: 52.9 seconds\n}\n\nIssue created by migration from https://trac.sagemath.org/ticket/4400\n\n",
    "created_at": "2008-10-30T17:29:35Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage 3.1.4: magma related doctest failures in sage/interfaces/magma.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4400",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

This is a strange one:

```
mabshoff@iras:~/build-3.2.a1/sage-3.2.alpha1-iras> ./sage -t -long -optional devel/sage/sage/interfaces/magma.py
sage -t -long -optional devel/sage/sage/interfaces/magma.py 
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py", line 1390:
    sage: a.sage()                        # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[3]>", line 1, in <module>
        a.sage()                        # optional###line 1390:
    sage: a.sage()                        # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1406, in sage
        return self._sage_()
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1433, in _sage_
        z, preparse = self.Sage(nvals = 2)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1213, in __call__
        nvals = nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 754, in function_call
        return self._do_call(fun, nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 798, in _do_call
        out = self.eval(cmd)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 383, in eval
        raise RuntimeError, "Error evaluating Magma code.\nIN:%s\nOUT:%s"%(x, ans)
    RuntimeError: Error evaluating Magma code.
    IN:
[15], _sage_[22] := Sage(_sage_[3]);
    OUT:
    >> _sage_[15], _sage_[22] := Sage(_sage_[3]);
                              ^
    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py", line 1392:
    sage: a._sage_()                      # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[4]>", line 1, in <module>
        a._sage_()                      # optional###line 1392:
    sage: a._sage_()                      # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1433, in _sage_
        z, preparse = self.Sage(nvals = 2)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1213, in __call__
        nvals = nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 754, in function_call
        return self._do_call(fun, nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 798, in _do_call
        out = self.eval(cmd)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 383, in eval
        raise RuntimeError, "Error evaluating Magma code.\nIN:%s\nOUT:%s"%(x, ans)
    RuntimeError: Error evaluating Magma code.
    IN:
[19], _sage_[28] := Sage(_sage_[8]);
    OUT:
    >> _sage_[19], _sage_[28] := Sage(_sage_[8]);
                              ^
    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py", line 1394:
    sage: type(a.sage())                  # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[5]>", line 1, in <module>
        type(a.sage())                  # optional###line 1394:
    sage: type(a.sage())                  # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1406, in sage
        return self._sage_()
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1433, in _sage_
        z, preparse = self.Sage(nvals = 2)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1213, in __call__
        nvals = nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 754, in function_call
        return self._do_call(fun, nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 798, in _do_call
        out = self.eval(cmd)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 383, in eval
        raise RuntimeError, "Error evaluating Magma code.\nIN:%s\nOUT:%s"%(x, ans)
    RuntimeError: Error evaluating Magma code.
    IN:
[29], _sage_[30] := Sage(_sage_[3]);
    OUT:
    >> _sage_[29], _sage_[30] := Sage(_sage_[3]);
                              ^
    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py", line 1400:
    sage: b = a.sage(); b             # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[8]>", line 1, in <module>
        b = a.sage(); b             # optional###line 1400:
    sage: b = a.sage(); b             # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1406, in sage
        return self._sage_()
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1433, in _sage_
        z, preparse = self.Sage(nvals = 2)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1213, in __call__
        nvals = nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 754, in function_call
        return self._do_call(fun, nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 798, in _do_call
        out = self.eval(cmd)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 383, in eval
        raise RuntimeError, "Error evaluating Magma code.\nIN:%s\nOUT:%s"%(x, ans)
    RuntimeError: Error evaluating Magma code.
    IN:
[32], _sage_[33] := Sage(_sage_[26]);
    OUT:
    >> _sage_[32], _sage_[33] := Sage(_sage_[26]);
                              ^
    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py", line 1402:
    sage: type(b)                         # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[9]>", line 1, in <module>
        type(b)                         # optional###line 1402:
    sage: type(b)                         # optional
    NameError: name 'b' is not defined
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py", line 1404:
    sage: c = magma(b); c                 # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[10]>", line 1, in <module>
        c = magma(b); c                 # optional###line 1404:
    sage: c = magma(b); c                 # optional
    NameError: name 'b' is not defined
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py", line 1406:
    sage: c.Type()                        # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[11]>", line 1, in <module>
        c.Type()                        # optional###line 1406:
    sage: c.Type()                        # optional
    NameError: name 'c' is not defined
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py", line 1411:
    sage: z = m.sage(); z                      # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[13]>", line 1, in <module>
        z = m.sage(); z                      # optional###line 1411:
    sage: z = m.sage(); z                      # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1406, in sage
        return self._sage_()
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1433, in _sage_
        z, preparse = self.Sage(nvals = 2)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1213, in __call__
        nvals = nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 754, in function_call
        return self._do_call(fun, nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 798, in _do_call
        out = self.eval(cmd)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 383, in eval
        raise RuntimeError, "Error evaluating Magma code.\nIN:%s\nOUT:%s"%(x, ans)
    RuntimeError: Error evaluating Magma code.
    IN:
[26], _sage_[34] := Sage(_sage_[4]);
    OUT:
    >> _sage_[26], _sage_[34] := Sage(_sage_[4]);
                              ^
    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py", line 1413:
    sage: type(z)                              # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[14]>", line 1, in <module>
        type(z)                              # optional###line 1413:
    sage: type(z)                              # optional
    NameError: name 'z' is not defined
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py", line 1419:
    sage: b = m.sage(); b                     # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[17]>", line 1, in <module>
        b = m.sage(); b                     # optional###line 1419:
    sage: b = m.sage(); b                     # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1406, in sage
        return self._sage_()
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1433, in _sage_
        z, preparse = self.Sage(nvals = 2)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1213, in __call__
        nvals = nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 754, in function_call
        return self._do_call(fun, nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 798, in _do_call
        out = self.eval(cmd)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 383, in eval
        raise RuntimeError, "Error evaluating Magma code.\nIN:%s\nOUT:%s"%(x, ans)
    RuntimeError: Error evaluating Magma code.
    IN:
[3], _sage_[35] := Sage(_sage_[4]);
    OUT:
    >> _sage_[3], _sage_[35] := Sage(_sage_[4]);
                             ^
    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py", line 1423:
    sage: b == a                             # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[18]>", line 1, in <module>
        b == a                             # optional###line 1423:
    sage: b == a                             # optional
    NameError: name 'b' is not defined
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/magma.py", line 1429:
    sage: m.sage()                           # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[21]>", line 1, in <module>
        m.sage()                           # optional###line 1429:
    sage: m.sage()                           # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1406, in sage
        return self._sage_()
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1433, in _sage_
        z, preparse = self.Sage(nvals = 2)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 1213, in __call__
        nvals = nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 754, in function_call
        return self._do_call(fun, nvals)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 798, in _do_call
        out = self.eval(cmd)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 383, in eval
        raise RuntimeError, "Error evaluating Magma code.\nIN:%s\nOUT:%s"%(x, ans)
    RuntimeError: Error evaluating Magma code.
    IN:
[8], _sage_[37] := Sage(_sage_[4]);
    OUT:
    >> _sage_[8], _sage_[37] := Sage(_sage_[4]);
                             ^
    Runtime error in :=: Expected to assign 2 value(s) but only computed 1 value(s)
**********************************************************************
1 items had failures:
  12 of  22 in __main__.example_49
***Test Failed*** 12 failures.
For whitespace errors, see the file /home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/.doctest_magma.py
	 [52.9 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long -optional devel/sage/sage/interfaces/magma.py
Total time for all tests: 52.9 seconds
}

Issue created by migration from https://trac.sagemath.org/ticket/4400





---

archive/issue_comments_032304.json:
```json
{
    "body": "Accidentally two extcode patches were not merged in 3.2.alpha1, so this cause the above failures. Applying them fixes the problem. Invalid. \n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T23:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4400#issuecomment-32304",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Accidentally two extcode patches were not merged in 3.2.alpha1, so this cause the above failures. Applying them fixes the problem. Invalid. 

Cheers,

Michael



---

archive/issue_comments_032305.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-10-30T23:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4400#issuecomment-32305",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid
