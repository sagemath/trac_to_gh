# Issue 9165: cygwin: lcalc does not work for elliptic curves on cygwin

archive/issues_009165.json:
```json
{
    "body": "Assignee: tbd\n\nlcalc works fine for the zeta function on cygwin, evidently:\n\n```\nsage: time lcalc.zeros(4)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.19 s\n[14.1347251, 21.0220396, 25.0108576, 30.4248761]\n```\n\nHowever, it doesn't work for computing with elliptic curves:\n\n```\nsage -t  \"devel/sage/sage/lfunctions/lcalc.py\"              \n  ***   not enough memory\n  ***   not enough memory\n  ***   not enough memory\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/lfunctions/lcalc.py\", line 120:\n    sage: lcalc.zeros(3, EllipticCurve('37a'))     # long\nExpected:\n    [0.000000000, 5.00317001, 6.87039122]\nGot:\n    []\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/lfunctions/lcalc.py\", line 229:\n    sage: E.lseries().values_along_line(0.5, 3, 5)\nExpected:\n    [(0, 0.209951303),\n     (0.500000000, -...e-16),\n     (1.00000000, 0.133768433),\n     (1.50000000, 0.360092864),\n     (2.00000000, 0.552975867)]\nGot:\n    lcalc:  \n    []\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/lfunctions/lcalc.py\", line 374:\n    sage: lcalc.analytic_rank(E)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/sage-4.4.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/wstein/sage-4.4.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/wstein/sage-4.4.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[3]>\", line 1, in <module>\n        lcalc.analytic_rank(E)###line 374:\n    sage: lcalc.analytic_rank(E)\n      File \"/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/lfunctions/lcalc.py\", line 381, in analytic_rank\n        return Z(s[i+6:])\n      File \"integer.pyx\", line 614, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6388)\n    TypeError: unable to convert x (=) to an integer\n**********************************************************************\n3 items had failures:\n   1 of   5 in __main__.example_2\n   1 of   6 in __main__.example_5\n   1 of   4 in __main__.example_8\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_lcalc.py\n\t [17.7 s]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9165\n\n",
    "created_at": "2010-06-07T04:05:45Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cygwin: lcalc does not work for elliptic curves on cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9165",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

lcalc works fine for the zeta function on cygwin, evidently:

```
sage: time lcalc.zeros(4)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.19 s
[14.1347251, 21.0220396, 25.0108576, 30.4248761]
```

However, it doesn't work for computing with elliptic curves:

```
sage -t  "devel/sage/sage/lfunctions/lcalc.py"              
  ***   not enough memory
  ***   not enough memory
  ***   not enough memory
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/lfunctions/lcalc.py", line 120:
    sage: lcalc.zeros(3, EllipticCurve('37a'))     # long
Expected:
    [0.000000000, 5.00317001, 6.87039122]
Got:
    []
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/lfunctions/lcalc.py", line 229:
    sage: E.lseries().values_along_line(0.5, 3, 5)
Expected:
    [(0, 0.209951303),
     (0.500000000, -...e-16),
     (1.00000000, 0.133768433),
     (1.50000000, 0.360092864),
     (2.00000000, 0.552975867)]
Got:
    lcalc:  
    []
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/lfunctions/lcalc.py", line 374:
    sage: lcalc.analytic_rank(E)
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[3]>", line 1, in <module>
        lcalc.analytic_rank(E)###line 374:
    sage: lcalc.analytic_rank(E)
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/lfunctions/lcalc.py", line 381, in analytic_rank
        return Z(s[i+6:])
      File "integer.pyx", line 614, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6388)
    TypeError: unable to convert x (=) to an integer
**********************************************************************
3 items had failures:
   1 of   5 in __main__.example_2
   1 of   6 in __main__.example_5
   1 of   4 in __main__.example_8
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_lcalc.py
	 [17.7 s]
```

Issue created by migration from https://trac.sagemath.org/ticket/9165





---

archive/issue_comments_085430.json:
```json
{
    "body": "Another test failure resulting from lcalc not working:\n\n```\n\nsage -t  \"devel/sage/sage/plot/line.py\"                     \n  ***   not enough memory\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/plot/line.py\", line 375:\n    sage: vals = E.lseries().values_along_line(1-I, 1+10*I, 100) # critical line\nExpected nothing\nGot:\n    lcalc:  \n**********************************************************************\n1 items had failures:\n```",
    "created_at": "2010-06-07T04:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9165#issuecomment-85430",
    "user": "https://github.com/williamstein"
}
```

Another test failure resulting from lcalc not working:

```

sage -t  "devel/sage/sage/plot/line.py"                     
  ***   not enough memory
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/plot/line.py", line 375:
    sage: vals = E.lseries().values_along_line(1-I, 1+10*I, 100) # critical line
Expected nothing
Got:
    lcalc:  
**********************************************************************
1 items had failures:
```



---

archive/issue_comments_085431.json:
```json
{
    "body": "Note gcc gives many compiler warnings and SunStudio refuses to compile the source code. These matters are probably not entirely unrelated.",
    "created_at": "2010-08-02T04:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9165#issuecomment-85431",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Note gcc gives many compiler warnings and SunStudio refuses to compile the source code. These matters are probably not entirely unrelated.



---

archive/issue_comments_085432.json:
```json
{
    "body": "The lfunctions/ directory appears to pass doctests on a recent build of mine on XP.",
    "created_at": "2011-08-02T02:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9165#issuecomment-85432",
    "user": "https://github.com/kcrisman"
}
```

The lfunctions/ directory appears to pass doctests on a recent build of mine on XP.



---

archive/issue_comments_085433.json:
```json
{
    "body": "plot/line.py also passes tests (though many others do not in plot/, perhaps due to \"I\" currently not working).",
    "created_at": "2011-08-02T02:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9165#issuecomment-85433",
    "user": "https://github.com/kcrisman"
}
```

plot/line.py also passes tests (though many others do not in plot/, perhaps due to "I" currently not working).



---

archive/issue_comments_085434.json:
```json
{
    "body": "But there is a segfault on the very first example above.  Strange that the tests pass.",
    "created_at": "2011-08-19T14:36:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9165#issuecomment-85434",
    "user": "https://github.com/kcrisman"
}
```

But there is a segfault on the very first example above.  Strange that the tests pass.



---

archive/issue_comments_085435.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-15T16:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9165#issuecomment-85435",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_events_022549.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2013-01-15T16:23:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9165",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9165#event-22549"
}
```



---

archive/issue_comments_085436.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2013-01-15T16:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9165#issuecomment-85436",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_085437.json:
```json
{
    "body": "These both pass and work \"by hand\" on XP now.  I do get warnings about the new stack size, which keeps going down from 1 MB to .981, .957, .955 with these commands, but they do *work* (as does the one in line.py) so I would suggest a different ticket for handling the stack on Cygwin.\n\nJP, can you confirm these pass on Win 7?  Then we should be set.",
    "created_at": "2013-01-15T16:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9165#issuecomment-85437",
    "user": "https://github.com/kcrisman"
}
```

These both pass and work "by hand" on XP now.  I do get warnings about the new stack size, which keeps going down from 1 MB to .981, .957, .955 with these commands, but they do *work* (as does the one in line.py) so I would suggest a different ticket for handling the stack on Cygwin.

JP, can you confirm these pass on Win 7?  Then we should be set.



---

archive/issue_comments_085438.json:
```json
{
    "body": "For info, this file passes its tests on my Windows 7 install (without #13351).\n\nSo let's close this one.",
    "created_at": "2013-01-30T12:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9165#issuecomment-85438",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

For info, this file passes its tests on my Windows 7 install (without #13351).

So let's close this one.



---

archive/issue_comments_085439.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-30T12:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9165#issuecomment-85439",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022550.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-31T20:36:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9165",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9165#event-22550"
}
```



---

archive/issue_comments_085440.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-01-31T20:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9165#issuecomment-85440",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
