# Issue 4564: [with patch, needs review] implement long long -> mpz_t

archive/issues_004564.json:
```json
{
    "body": "Assignee: somebody\n\nFor some reason, there is no function to do this shipped with gmp...\n\nIssue created by migration from https://trac.sagemath.org/ticket/4564\n\n",
    "created_at": "2008-11-20T13:02:49Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] implement long long -> mpz_t",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4564",
    "user": "robertwb"
}
```
Assignee: somebody

For some reason, there is no function to do this shipped with gmp...

Issue created by migration from https://trac.sagemath.org/ticket/4564





---

archive/issue_comments_034182.json:
```json
{
    "body": "Attachment [4564-mpz-longlong.patch](tarball://root/attachments/some-uuid/ticket4564/4564-mpz-longlong.patch) by craigcitro created at 2008-11-20 23:00:09\n\nSo the code here looks good. I even pulled out my old G4 and tested it on a big-endian machine, and everything worked fine.\n\nI do have one question, though: doesn't the `mpz_set_longlong` belong somewhere more generic than `integer.pyx`? I would have put it somewhere in libcsage. Of course, then it wouldn't be so easy to raise the exception ...",
    "created_at": "2008-11-20T23:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4564#issuecomment-34182",
    "user": "craigcitro"
}
```

Attachment [4564-mpz-longlong.patch](tarball://root/attachments/some-uuid/ticket4564/4564-mpz-longlong.patch) by craigcitro created at 2008-11-20 23:00:09

So the code here looks good. I even pulled out my old G4 and tested it on a big-endian machine, and everything worked fine.

I do have one question, though: doesn't the `mpz_set_longlong` belong somewhere more generic than `integer.pyx`? I would have put it somewhere in libcsage. Of course, then it wouldn't be so easy to raise the exception ...



---

archive/issue_comments_034183.json:
```json
{
    "body": "Yeah, probably does belong in libcsage... I'm going to be moving stuff around when I split up cdefs anyways. I was just concentrating more on divisors at that point ;).",
    "created_at": "2008-11-20T23:11:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4564#issuecomment-34183",
    "user": "robertwb"
}
```

Yeah, probably does belong in libcsage... I'm going to be moving stuff around when I split up cdefs anyways. I was just concentrating more on divisors at that point ;).



---

archive/issue_comments_034184.json:
```json
{
    "body": "That works. Let's merge this now, then, and worry about it later. Maybe open a ticket for the cdefs cleanup and mention this, so we don't forget?",
    "created_at": "2008-11-20T23:12:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4564#issuecomment-34184",
    "user": "craigcitro"
}
```

That works. Let's merge this now, then, and worry about it later. Maybe open a ticket for the cdefs cleanup and mention this, so we don't forget?



---

archive/issue_comments_034185.json:
```json
{
    "body": "See #846. I'm planning on doing that today.",
    "created_at": "2008-11-20T23:15:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4564#issuecomment-34185",
    "user": "robertwb"
}
```

See #846. I'm planning on doing that today.



---

archive/issue_comments_034186.json:
```json
{
    "body": "I am seeing a doctest failure here:\n\n```\nsage -t -long devel/sage/sage/rings/integer.pyx             \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/integer.pyx\", line 199:\n    sage: sage: _test_mpz_set_longlong(100000000000)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[6]>\", line 1\n         sage: _test_mpz_set_longlong(Integer(100000000000))###line 199:\n    sage: sage: _test_mpz_set_longlong(100000000000)\n          ^\n     SyntaxError: invalid syntax\n**********************************************************************\n1 items had failures:\n```\n\n\nI guess this is caused by an extra \"sage: \" in that line. I am editing the patch to fix this.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T05:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4564#issuecomment-34186",
    "user": "mabshoff"
}
```

I am seeing a doctest failure here:

```
sage -t -long devel/sage/sage/rings/integer.pyx             
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/integer.pyx", line 199:
    sage: sage: _test_mpz_set_longlong(100000000000)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[6]>", line 1
         sage: _test_mpz_set_longlong(Integer(100000000000))###line 199:
    sage: sage: _test_mpz_set_longlong(100000000000)
          ^
     SyntaxError: invalid syntax
**********************************************************************
1 items had failures:
```


I guess this is caused by an extra "sage: " in that line. I am editing the patch to fix this.

Cheers,

Michael



---

archive/issue_comments_034187.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T05:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4564#issuecomment-34187",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha0



---

archive/issue_comments_034188.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T05:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4564#issuecomment-34188",
    "user": "mabshoff"
}
```

Resolution: fixed
