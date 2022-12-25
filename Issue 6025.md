# Issue 6025: Sage 3.4.2: doctest failure in sage/libs/pari/gen.pyx on 64 bit OSX

archive/issues_006025.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t -long \"devel/sage/sage/libs/pari/gen.pyx\"           \n**********************************************************************\nFile \"/Users/mabshoff/sage-3.4.2-64/devel/sage/sage/libs/pari/gen.pyx\", line 8945:\n    sage: pari.finitefield_init(7,2)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mabshoff/sage-3.4.2-64/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/mabshoff/sage-3.4.2-64/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/mabshoff/sage-3.4.2-64/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_291[4]>\", line 1, in <module>\n        pari.finitefield_init(Integer(7),Integer(2))###line 8945:\n    sage: pari.finitefield_init(7,2)\n    RuntimeError\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.4.2-64/devel/sage/sage/libs/pari/gen.pyx\", line 8950:\n    sage: pari.finitefield_init(2,3)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mabshoff/sage-3.4.2-64/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/mabshoff/sage-3.4.2-64/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/mabshoff/sage-3.4.2-64/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_291[5]>\", line 1, in <module>\n        pari.finitefield_init(Integer(2),Integer(3))###line 8950:\n    sage: pari.finitefield_init(2,3)\n    RuntimeError\n**********************************************************************\n1 items had failures:\n   2 of   6 in __main__.example_291\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /Users/mabshoff/sage-3.4.2-64/tmp/.doctest_gen.py\n\t [19.0 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6025\n\n",
    "created_at": "2009-05-12T07:10:05Z",
    "labels": [
        "component: porting",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Sage 3.4.2: doctest failure in sage/libs/pari/gen.pyx on 64 bit OSX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6025",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
sage -t -long "devel/sage/sage/libs/pari/gen.pyx"           
**********************************************************************
File "/Users/mabshoff/sage-3.4.2-64/devel/sage/sage/libs/pari/gen.pyx", line 8945:
    sage: pari.finitefield_init(7,2)
Exception raised:
    Traceback (most recent call last):
      File "/Users/mabshoff/sage-3.4.2-64/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mabshoff/sage-3.4.2-64/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mabshoff/sage-3.4.2-64/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_291[4]>", line 1, in <module>
        pari.finitefield_init(Integer(7),Integer(2))###line 8945:
    sage: pari.finitefield_init(7,2)
    RuntimeError
**********************************************************************
File "/Users/mabshoff/sage-3.4.2-64/devel/sage/sage/libs/pari/gen.pyx", line 8950:
    sage: pari.finitefield_init(2,3)
Exception raised:
    Traceback (most recent call last):
      File "/Users/mabshoff/sage-3.4.2-64/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mabshoff/sage-3.4.2-64/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mabshoff/sage-3.4.2-64/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_291[5]>", line 1, in <module>
        pari.finitefield_init(Integer(2),Integer(3))###line 8950:
    sage: pari.finitefield_init(2,3)
    RuntimeError
**********************************************************************
1 items had failures:
   2 of   6 in __main__.example_291
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/mabshoff/sage-3.4.2-64/tmp/.doctest_gen.py
	 [19.0 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/6025





---

archive/issue_comments_047892.json:
```json
{
    "body": "Attachment [trac-6025.patch](tarball://root/attachments/some-uuid/ticket6025/trac-6025.patch) by @craigcitro created at 2009-05-13 00:22:30\n\nAs William pointed out on the mailing list, this code isn't used anywhere -- so we're just killing the function. The problem is that on 64 bit OSX, a value getting returned loses its top 4 bytes. This is clearly weird, but since this pari function is known to be buggy, we'll just not use it for now and cross our fingers.",
    "created_at": "2009-05-13T00:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6025#issuecomment-47892",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-6025.patch](tarball://root/attachments/some-uuid/ticket6025/trac-6025.patch) by @craigcitro created at 2009-05-13 00:22:30

As William pointed out on the mailing list, this code isn't used anywhere -- so we're just killing the function. The problem is that on 64 bit OSX, a value getting returned loses its top 4 bytes. This is clearly weird, but since this pari function is known to be buggy, we'll just not use it for now and cross our fingers.



---

archive/issue_comments_047893.json:
```json
{
    "body": "Ok, good to go.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-13T17:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6025#issuecomment-47893",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, good to go.

Cheers,

Michael



---

archive/issue_comments_047894.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-13T18:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6025#issuecomment-47894",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_047895.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-13T18:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6025#issuecomment-47895",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_014152.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-13T18:00:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6025",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6025#event-14152"
}
```
