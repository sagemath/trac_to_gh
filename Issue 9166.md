# Issue 9166: cygwin: sympow does not work on cygwin

archive/issues_009166.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @mwhansen\n\nBasically, Mark Watkins program Sympow is completely broken on Microsoft Windows (Cygwin):\n\n\n```\n\nsage -t  \"devel/sage/sage/lfunctions/sympow.py\"             \n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/lfunctions/sympow.py\", line 213:\n    sage: sympow.modular_degree(EllipticCurve('11a'))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/sage-4.4.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/wstein/sage-4.4.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/wstein/sage-4.4.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[2]>\", line 1, in <module>\n        sympow.modular_degree(EllipticCurve('11a'))###line 213:\n    sage: sympow.modular_degree(EllipticCurve('11a'))\n      File \"/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/lfunctions/sympow.py\", line 229, in modular_degree\n        raise RuntimeError, \"failed to compute modular degree\"\n    RuntimeError: failed to compute modular degree\n\n... etc.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9166\n\n",
    "created_at": "2010-06-07T04:22:20Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cygwin: sympow does not work on cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9166",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @mwhansen

Basically, Mark Watkins program Sympow is completely broken on Microsoft Windows (Cygwin):


```

sage -t  "devel/sage/sage/lfunctions/sympow.py"             
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/lfunctions/sympow.py", line 213:
    sage: sympow.modular_degree(EllipticCurve('11a'))
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[2]>", line 1, in <module>
        sympow.modular_degree(EllipticCurve('11a'))###line 213:
    sage: sympow.modular_degree(EllipticCurve('11a'))
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/lfunctions/sympow.py", line 229, in modular_degree
        raise RuntimeError, "failed to compute modular degree"
    RuntimeError: failed to compute modular degree

... etc.
```


Issue created by migration from https://trac.sagemath.org/ticket/9166





---

archive/issue_comments_085441.json:
```json
{
    "body": "Another failure that is caused by sympow not working:\n\n```\n\nsage -t  \"devel/sage/sage/modular/abvar/abvar.py\"           \n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/modular/abvar/abvar.py\", line 3305:\n    sage: E.modular_degree()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/sage-4.4.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/wstein/sage-4.4.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/wstein/sage-4.4.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_84[8]>\", line 1, in <module>\n        E.modular_degree()###line 3305:\n    sage: E.modular_degree()\n      File \"/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3311, in modular_degree\n        m = sympow.modular_degree(self)\n      File \"/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/lfunctions/sympow.py\", line 229, in modular_degree\n        raise RuntimeError, \"failed to compute modular degree\"\n    RuntimeError: failed to compute modular degree\n```\n",
    "created_at": "2010-06-07T04:38:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9166#issuecomment-85441",
    "user": "https://github.com/williamstein"
}
```

Another failure that is caused by sympow not working:

```

sage -t  "devel/sage/sage/modular/abvar/abvar.py"           
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/modular/abvar/abvar.py", line 3305:
    sage: E.modular_degree()
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_84[8]>", line 1, in <module>
        E.modular_degree()###line 3305:
    sage: E.modular_degree()
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 3311, in modular_degree
        m = sympow.modular_degree(self)
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/lfunctions/sympow.py", line 229, in modular_degree
        raise RuntimeError, "failed to compute modular degree"
    RuntimeError: failed to compute modular degree
```




---

archive/issue_comments_085442.json:
```json
{
    "body": "Another failure:\n\n```\n\nsage -t  \"devel/sage/sage/modular/hecke/submodule.py\"       \n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/modular/hecke/submodule.py\", line 497:\n    sage: EllipticCurve('128a').congruence_number()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/sage-4.4.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/wstein/sage-4.4.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/wstein/sage-4.4.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_16[19]>\", line 1, in <module>\n        EllipticCurve('128a').congruence_number()###line 497:\n    sage: EllipticCurve('128a').congruence_number()\n      File \"/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3404, in congruence_number\n        m = self.modular_degree()\n      File \"/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3311, in modular_degree\n        m = sympow.modular_degree(self)\n      File \"/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/lfunctions/sympow.py\", line 229, in modular_degree\n        raise RuntimeError, \"failed to compute modular degree\"\n    RuntimeError: failed to compute modular degree\n\n```\n",
    "created_at": "2010-06-07T04:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9166#issuecomment-85442",
    "user": "https://github.com/williamstein"
}
```

Another failure:

```

sage -t  "devel/sage/sage/modular/hecke/submodule.py"       
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/modular/hecke/submodule.py", line 497:
    sage: EllipticCurve('128a').congruence_number()
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_16[19]>", line 1, in <module>
        EllipticCurve('128a').congruence_number()###line 497:
    sage: EllipticCurve('128a').congruence_number()
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 3404, in congruence_number
        m = self.modular_degree()
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 3311, in modular_degree
        m = sympow.modular_degree(self)
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/lfunctions/sympow.py", line 229, in modular_degree
        raise RuntimeError, "failed to compute modular degree"
    RuntimeError: failed to compute modular degree

```




---

archive/issue_comments_085443.json:
```json
{
    "body": "Sympow doesn't work for me on Arch Linux, GCC 4.5.0\n\nThese doctests fail for me:\n\n\u00a0\u00a0 \u00a0 \u00a0 \u00a0sage -t \u00a0\"devel/sage/sage/modular/hecke/submodule.py\"\n\n\u00a0\u00a0 \u00a0 \u00a0 \u00a0sage -t \u00a0\"devel/sage/sage/modular/abvar/abvar.py\"\n\n\u00a0\u00a0 \u00a0 \u00a0 \u00a0sage -t \u00a0\"devel/sage/sage/lfunctions/sympow.py\"\n\n\u00a0\u00a0 \u00a0 \u00a0 \u00a0sage -t \u00a0\"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"",
    "created_at": "2010-07-20T10:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9166#issuecomment-85443",
    "user": "https://trac.sagemath.org/admin/accounts/users/retry"
}
```

Sympow doesn't work for me on Arch Linux, GCC 4.5.0

These doctests fail for me:

        sage -t  "devel/sage/sage/modular/hecke/submodule.py"

        sage -t  "devel/sage/sage/modular/abvar/abvar.py"

        sage -t  "devel/sage/sage/lfunctions/sympow.py"

        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"



---

archive/issue_comments_085444.json:
```json
{
    "body": "test.log with failures",
    "created_at": "2010-07-20T10:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9166#issuecomment-85444",
    "user": "https://trac.sagemath.org/admin/accounts/users/retry"
}
```

test.log with failures



---

archive/issue_comments_085445.json:
```json
{
    "body": "Attachment [test.log](tarball://root/attachments/some-uuid/ticket9166/test.log) by drkirkby created at 2010-08-11 23:29:55\n\nReplying to [comment:3 retry]:\n> Sympow doesn't work for me on Arch Linux, GCC 4.5.0\n\nThat's now\n* Cygwin\n* Arch Linux\n* Solaris 10 on x86 #9703.\n* OpenSolaris on x86 \n\nThe pseudo C code is not valid C. It tried to return functions from those declared as void, so its not clear to me what the intended behaviour. \n\nI've tried to build this with the Sun C compiler, but it refuses to compile it. \n\nDave",
    "created_at": "2010-08-11T23:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9166#issuecomment-85445",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [test.log](tarball://root/attachments/some-uuid/ticket9166/test.log) by drkirkby created at 2010-08-11 23:29:55

Replying to [comment:3 retry]:
> Sympow doesn't work for me on Arch Linux, GCC 4.5.0

That's now
* Cygwin
* Arch Linux
* Solaris 10 on x86 #9703.
* OpenSolaris on x86 

The pseudo C code is not valid C. It tried to return functions from those declared as void, so its not clear to me what the intended behaviour. 

I've tried to build this with the Sun C compiler, but it refuses to compile it. 

Dave



---

archive/issue_comments_085446.json:
```json
{
    "body": "Ticket #9703, which I'll merge into 4.5.3.alpha2, should fix the problems here.  If someone can confirm that they do, I'll close this ticket.",
    "created_at": "2010-08-23T23:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9166#issuecomment-85446",
    "user": "https://github.com/qed777"
}
```

Ticket #9703, which I'll merge into 4.5.3.alpha2, should fix the problems here.  If someone can confirm that they do, I'll close this ticket.



---

archive/issue_comments_085447.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-08-25T21:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9166#issuecomment-85447",
    "user": "https://github.com/qed777"
}
```

Resolution: duplicate



---

archive/issue_events_022551.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-25T21:22:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9166",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9166#event-22551"
}
```



---

archive/issue_events_022552.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-25T21:22:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9166",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9166#event-22552"
}
```
