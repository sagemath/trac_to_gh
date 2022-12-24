# Issue 4672: plot functions do not work with ?? because they are wrapped in @options

archive/issues_004672.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: bar_chart??\nType:\t\tfunction\nBase Class:\t<type 'function'>\nString Form:\t<function bar_chart at 0x88b4b1c>\nNamespace:\tInteractive\nFile:\t\t/home/jason/sage/local/lib/python2.5/site-packages/sage/plot/misc.py\nDefinition:\tbar_chart(*args, **kwds)\nSource:\n        @wraps(func)\n        def wrapper(*args, **kwds):\n            options = copy(wrapper.options)\n            if self.original_opts:\n                options['__original_opts'] = kwds\n            options.update(kwds)\n            return func(*args, **options)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4672\n\n",
    "created_at": "2008-12-02T05:43:05Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "plot functions do not work with ?? because they are wrapped in @options",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4672",
    "user": "jason"
}
```
Assignee: was


```
sage: bar_chart??
Type:		function
Base Class:	<type 'function'>
String Form:	<function bar_chart at 0x88b4b1c>
Namespace:	Interactive
File:		/home/jason/sage/local/lib/python2.5/site-packages/sage/plot/misc.py
Definition:	bar_chart(*args, **kwds)
Source:
        @wraps(func)
        def wrapper(*args, **kwds):
            options = copy(wrapper.options)
            if self.original_opts:
                options['__original_opts'] = kwds
            options.update(kwds)
            return func(*args, **options)
```


Issue created by migration from https://trac.sagemath.org/ticket/4672





---

archive/issue_comments_035194.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-02T06:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4672#issuecomment-35194",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035195.json:
```json
{
    "body": "Attachment [trac_4672.patch](tarball://root/attachments/some-uuid/ticket4672/trac_4672.patch) by mhansen created at 2008-12-02 06:00:34",
    "created_at": "2008-12-02T06:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4672#issuecomment-35195",
    "user": "mhansen"
}
```

Attachment [trac_4672.patch](tarball://root/attachments/some-uuid/ticket4672/trac_4672.patch) by mhansen created at 2008-12-02 06:00:34



---

archive/issue_comments_035196.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2008-12-02T06:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4672#issuecomment-35196",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_035197.json:
```json
{
    "body": "Code looks reasonable, applies (with fuzz) to my Sage 3.2, and fixes the issue pointed out above, so positive review.",
    "created_at": "2008-12-02T06:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4672#issuecomment-35197",
    "user": "jason"
}
```

Code looks reasonable, applies (with fuzz) to my Sage 3.2, and fixes the issue pointed out above, so positive review.



---

archive/issue_comments_035198.json:
```json
{
    "body": "I also tried the code, etc., and it looks good, so another positive review from me. \n\nWhen I was reviewing though I noticed that, which has nothing a priori to do with this ticket but is worrisome. \n\n```\nsage: a = plot(sin)\nsage: a == loads(dumps(a))\nFalse\n```\n",
    "created_at": "2008-12-02T17:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4672#issuecomment-35198",
    "user": "was"
}
```

I also tried the code, etc., and it looks good, so another positive review from me. 

When I was reviewing though I noticed that, which has nothing a priori to do with this ticket but is worrisome. 

```
sage: a = plot(sin)
sage: a == loads(dumps(a))
False
```




---

archive/issue_comments_035199.json:
```json
{
    "body": "This patch breaks one doctest:\n\n```\nsage -t -long \"devel/sage/sage/combinat/sloane_functions.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/combinat/sloane_functions.py\", line 156:\n    sage: sloane.A000045._sage_src_()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[2]>\", line 1, in <module>\n        sloane.A000045._sage_src_()###line 156:\n    sage: sloane.A000045._sage_src_()\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/combinat/sloane_functions.py\", line 160, in _sage_src_\n        return sage_getsource(self.__class__)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/misc/sageinspect.py\", line 367, in sage_getsource\n        return obj._sage_src_()\n    TypeError: unbound method _sage_src_() must be called with A000045 instance as first argument (got nothing instead)\n**********************************************************************\n1 items had failures:\n   1 of   3 in __main__.example_5\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/tmp/.doctest_sloane_functions.py\n\t [6.6 s]\nexit code: 1024\n```\n",
    "created_at": "2008-12-03T10:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4672#issuecomment-35199",
    "user": "mabshoff"
}
```

This patch breaks one doctest:

```
sage -t -long "devel/sage/sage/combinat/sloane_functions.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/combinat/sloane_functions.py", line 156:
    sage: sloane.A000045._sage_src_()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[2]>", line 1, in <module>
        sloane.A000045._sage_src_()###line 156:
    sage: sloane.A000045._sage_src_()
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/combinat/sloane_functions.py", line 160, in _sage_src_
        return sage_getsource(self.__class__)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 367, in sage_getsource
        return obj._sage_src_()
    TypeError: unbound method _sage_src_() must be called with A000045 instance as first argument (got nothing instead)
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/tmp/.doctest_sloane_functions.py
	 [6.6 s]
exit code: 1024
```




---

archive/issue_comments_035200.json:
```json
{
    "body": "Attachment [trac_4672-2.patch](tarball://root/attachments/some-uuid/ticket4672/trac_4672-2.patch) by mhansen created at 2008-12-04 10:57:08",
    "created_at": "2008-12-04T10:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4672#issuecomment-35200",
    "user": "mhansen"
}
```

Attachment [trac_4672-2.patch](tarball://root/attachments/some-uuid/ticket4672/trac_4672-2.patch) by mhansen created at 2008-12-04 10:57:08



---

archive/issue_comments_035201.json:
```json
{
    "body": "I've attached a second patch which fixes the issue.",
    "created_at": "2008-12-04T10:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4672#issuecomment-35201",
    "user": "mhansen"
}
```

I've attached a second patch which fixes the issue.



---

archive/issue_comments_035202.json:
```json
{
    "body": "Mike's second patch fixes the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T14:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4672#issuecomment-35202",
    "user": "mabshoff"
}
```

Mike's second patch fixes the issue.

Cheers,

Michael



---

archive/issue_comments_035203.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha0",
    "created_at": "2008-12-04T14:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4672#issuecomment-35203",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha0



---

archive/issue_comments_035204.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-04T14:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4672#issuecomment-35204",
    "user": "mabshoff"
}
```

Resolution: fixed
