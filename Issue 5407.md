# Issue 5407: fractional gens?  not good -- (QQ^3).gen(4/3) gives (0,1,0)

archive/issues_005407.json:
```json
{
    "body": "Assignee: was\n\nThis patch fixes the bug. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5407\n\n",
    "created_at": "2009-03-01T05:59:34Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "fractional gens?  not good -- (QQ^3).gen(4/3) gives (0,1,0)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5407",
    "user": "was"
}
```
Assignee: was

This patch fixes the bug. 

Issue created by migration from https://trac.sagemath.org/ticket/5407





---

archive/issue_comments_041794.json:
```json
{
    "body": "Nice try wstein :)\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T06:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5407#issuecomment-41794",
    "user": "mabshoff"
}
```

Nice try wstein :)

Cheers,

Michael



---

archive/issue_comments_041795.json:
```json
{
    "body": "One doctest failure:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.4.alpha1$ ./sage -t -long devel/sage/sage/modules/free_module.py\nsage -t -long \"devel/sage/sage/modules/free_module.py\"      \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.alpha1/devel/sage/sage/modules/free_module.py\", line 1438:\n    sage: (QQ^3).gen(4/3)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.4.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_37[7]>\", line 1, in <module>\n        (QQ**Integer(3)).gen(Integer(4)/Integer(3))###line 1438:\n    sage: (QQ^3).gen(4/3)\n      File \"/scratch/mabshoff/sage-3.4.alpha1/local/lib/python2.5/site-packages/sage/modules/free_module.py\", line 1445, in gen\n        return self.basis()[i]\n      File \"rational.pyx\", line 236, in sage.rings.rational.Rational.__index__ (sage/rings/rational.c:4371)\n    TypeError: rational is not an integer\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T06:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5407#issuecomment-41795",
    "user": "mabshoff"
}
```

One doctest failure:

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.alpha1$ ./sage -t -long devel/sage/sage/modules/free_module.py
sage -t -long "devel/sage/sage/modules/free_module.py"      
**********************************************************************
File "/scratch/mabshoff/sage-3.4.alpha1/devel/sage/sage/modules/free_module.py", line 1438:
    sage: (QQ^3).gen(4/3)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_37[7]>", line 1, in <module>
        (QQ**Integer(3)).gen(Integer(4)/Integer(3))###line 1438:
    sage: (QQ^3).gen(4/3)
      File "/scratch/mabshoff/sage-3.4.alpha1/local/lib/python2.5/site-packages/sage/modules/free_module.py", line 1445, in gen
        return self.basis()[i]
      File "rational.pyx", line 236, in sage.rings.rational.Rational.__index__ (sage/rings/rational.c:4371)
    TypeError: rational is not an integer
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_041796.json:
```json
{
    "body": "This is an updated Version of Wiliam's patch",
    "created_at": "2009-03-02T04:30:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5407#issuecomment-41796",
    "user": "mabshoff"
}
```

This is an updated Version of Wiliam's patch



---

archive/issue_comments_041797.json:
```json
{
    "body": "Attachment [trac_5407.patch](tarball://root/attachments/some-uuid/ticket5407/trac_5407.patch) by mabshoff created at 2009-03-02 04:31:12\n\nOk, the problem has been fixed.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T04:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5407#issuecomment-41797",
    "user": "mabshoff"
}
```

Attachment [trac_5407.patch](tarball://root/attachments/some-uuid/ticket5407/trac_5407.patch) by mabshoff created at 2009-03-02 04:31:12

Ok, the problem has been fixed.

Cheers,

Michael



---

archive/issue_comments_041798.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T04:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5407#issuecomment-41798",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041799.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-02T04:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5407#issuecomment-41799",
    "user": "mabshoff"
}
```

Resolution: fixed
