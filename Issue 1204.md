# Issue 1204: 2.8.13.alpha0: libs/cremona/constructor.py doctest failures

archive/issues_001204.json:
```json
{
    "body": "Assignee: failure\n\n```\nsage -t  devel/sage-main/sage/libs/cremona/constructor.py   **********************************************************************\nFile \"constructor.py\", line 42:\n    sage: M = CremonaModularSymbols(-1)\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: the level (= -1) must be a positive integer\nGot:\n    Traceback (most recent call last):\n      File \"/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[4]>\", line 1, in <module>\n        M = CremonaModularSymbols(-Integer(1))###line 42:\n    sage: M = CremonaModularSymbols(-1)\n      File \"/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/site-packages/sage/libs/cremona/constructor.py\", line 64, in CremonaModularSymbols\n        return ModularSymbols(level=level, sign=sign, cuspidal=cuspidal, verbose=verbose)\n      File \"homspace.pyx\", line 25, in sage.libs.cremona.homspace.ModularSymbols.__init__\n        raise ValueError, \"the level (= %s) must be at least 2\"%level\n    ValueError: the level (= -1) must be at least 2\n**********************************************************************\nFile \"constructor.py\", line 46:\n    sage: M = CremonaModularSymbols(0)\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: the level (= 0) must be a positive integer\nGot:\n    Traceback (most recent call last):\n      File \"/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[5]>\", line 1, in <module>\n        M = CremonaModularSymbols(Integer(0))###line 46:\n    sage: M = CremonaModularSymbols(0)\n      File \"/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/site-packages/sage/libs/cremona/constructor.py\", line 64, in CremonaModularSymbols\n        return ModularSymbols(level=level, sign=sign, cuspidal=cuspidal, verbose=verbose)\n      File \"homspace.pyx\", line 25, in sage.libs.cremona.homspace.ModularSymbols.__init__\n        raise ValueError, \"the level (= %s) must be at least 2\"%level\n    ValueError: the level (= 0) must be at least 2\n**********************************************************************\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1204\n\n",
    "created_at": "2007-11-18T23:12:55Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "2.8.13.alpha0: libs/cremona/constructor.py doctest failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1204",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: failure

```
sage -t  devel/sage-main/sage/libs/cremona/constructor.py   **********************************************************************
File "constructor.py", line 42:
    sage: M = CremonaModularSymbols(-1)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: the level (= -1) must be a positive integer
Got:
    Traceback (most recent call last):
      File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[4]>", line 1, in <module>
        M = CremonaModularSymbols(-Integer(1))###line 42:
    sage: M = CremonaModularSymbols(-1)
      File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/site-packages/sage/libs/cremona/constructor.py", line 64, in CremonaModularSymbols
        return ModularSymbols(level=level, sign=sign, cuspidal=cuspidal, verbose=verbose)
      File "homspace.pyx", line 25, in sage.libs.cremona.homspace.ModularSymbols.__init__
        raise ValueError, "the level (= %s) must be at least 2"%level
    ValueError: the level (= -1) must be at least 2
**********************************************************************
File "constructor.py", line 46:
    sage: M = CremonaModularSymbols(0)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: the level (= 0) must be a positive integer
Got:
    Traceback (most recent call last):
      File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 1, in <module>
        M = CremonaModularSymbols(Integer(0))###line 46:
    sage: M = CremonaModularSymbols(0)
      File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/site-packages/sage/libs/cremona/constructor.py", line 64, in CremonaModularSymbols
        return ModularSymbols(level=level, sign=sign, cuspidal=cuspidal, verbose=verbose)
      File "homspace.pyx", line 25, in sage.libs.cremona.homspace.ModularSymbols.__init__
        raise ValueError, "the level (= %s) must be at least 2"%level
    ValueError: the level (= 0) must be at least 2
**********************************************************************
```

Issue created by migration from https://trac.sagemath.org/ticket/1204





---

archive/issue_comments_007433.json:
```json
{
    "body": "```\n[01:37] <was_> In fact, now that I think about it, I think I changed the value error slightly.  Oops.\n[01:37] <mabshoff> :)\n[01:37] <was_> Feel free to just change the doctests in your code.  My mistake.\n[01:37] <mabshoff> Ok, it was \"ValueError: the level (= -1) must be at least 2\" but it is now \n[01:38] <mabshoff> \"ValueError: the level (= -1) must be a positive integer\"\n[01:43] <mabshoff> Ok, when I changed the Valueerror the doctest in sage -t  devel/sage-main/sage/libs/cremona/constructor.py passes\n[01:43] <mabshoff> Does it really have to be \\geq 2 or just postive?\n[01:43] <was_> In theory the level must be >= 1.\n[01:44] <was_> In Cremona's program, he didn't do level 1 correctly (it crashes), so it must be >= 2 for Cremona.\n[01:44] <mabshoff> ok\n[01:44] <was_> Level 1 just gives the 0 space anyways, so no problem.\n```\n\nMichael",
    "created_at": "2007-11-19T00:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1204#issuecomment-7433",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

```
[01:37] <was_> In fact, now that I think about it, I think I changed the value error slightly.  Oops.
[01:37] <mabshoff> :)
[01:37] <was_> Feel free to just change the doctests in your code.  My mistake.
[01:37] <mabshoff> Ok, it was "ValueError: the level (= -1) must be at least 2" but it is now 
[01:38] <mabshoff> "ValueError: the level (= -1) must be a positive integer"
[01:43] <mabshoff> Ok, when I changed the Valueerror the doctest in sage -t  devel/sage-main/sage/libs/cremona/constructor.py passes
[01:43] <mabshoff> Does it really have to be \geq 2 or just postive?
[01:43] <was_> In theory the level must be >= 1.
[01:44] <was_> In Cremona's program, he didn't do level 1 correctly (it crashes), so it must be >= 2 for Cremona.
[01:44] <mabshoff> ok
[01:44] <was_> Level 1 just gives the 0 space anyways, so no problem.
```

Michael



---

archive/issue_comments_007434.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-19T00:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1204#issuecomment-7434",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003205.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-19T00:49:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1204",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1204#event-3205"
}
```
