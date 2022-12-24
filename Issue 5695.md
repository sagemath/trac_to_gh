# Issue 5695: Sgae 3.4.1.rc1: doctest failure in combinat/words/words.py on 32 bit boxen

archive/issues_005695.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  hivert saliola\n\nThis looks like fallout from #5308:\n\n```\nsage -t -long \"devel/sage/sage/combinat/words/words.py\"     \n**********************************************************************\nFile \"/Users/mabshoff/sage-3.4.1.rc1/devel/sage/sage/combinat/words/words.py\", line 760:\n    sage: Words(7,13).cardinality()\nExpected:\n    96889010407L               \nGot:\n    96889010407\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.4.1.rc1/devel/sage/sage/combinat/words/words.py\", line 763:\n    sage: Words(['a','b','c','d','e','f','g'],13).cardinality()\nExpected:\n    96889010407L               \nGot:\n    96889010407\n**********************************************************************\n1 items had failures:\n   2 of  12 in __main__.example_31\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /Users/mabshoff/sage-3.4.1.rc1/tmp/.doctest_words.py\n\t [18.4 s]\nexit code: 1024\n```\n\n\nTrivial patch coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5695\n\n",
    "created_at": "2009-04-06T18:31:14Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "Sgae 3.4.1.rc1: doctest failure in combinat/words/words.py on 32 bit boxen",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5695",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  hivert saliola

This looks like fallout from #5308:

```
sage -t -long "devel/sage/sage/combinat/words/words.py"     
**********************************************************************
File "/Users/mabshoff/sage-3.4.1.rc1/devel/sage/sage/combinat/words/words.py", line 760:
    sage: Words(7,13).cardinality()
Expected:
    96889010407L               
Got:
    96889010407
**********************************************************************
File "/Users/mabshoff/sage-3.4.1.rc1/devel/sage/sage/combinat/words/words.py", line 763:
    sage: Words(['a','b','c','d','e','f','g'],13).cardinality()
Expected:
    96889010407L               
Got:
    96889010407
**********************************************************************
1 items had failures:
   2 of  12 in __main__.example_31
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/mabshoff/sage-3.4.1.rc1/tmp/.doctest_words.py
	 [18.4 s]
exit code: 1024
```


Trivial patch coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5695





---

archive/issue_comments_044519.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-06T18:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5695#issuecomment-44519",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044520.json:
```json
{
    "body": "Attachment [trac_5695.patch](tarball://root/attachments/some-uuid/ticket5695/trac_5695.patch) by mabshoff created at 2009-04-06 18:42:43\n\nFranco or Florent, since either one of you broke this in #5308 feel free to review this trivial and obvious patch :P\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T18:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5695#issuecomment-44520",
    "user": "mabshoff"
}
```

Attachment [trac_5695.patch](tarball://root/attachments/some-uuid/ticket5695/trac_5695.patch) by mabshoff created at 2009-04-06 18:42:43

Franco or Florent, since either one of you broke this in #5308 feel free to review this trivial and obvious patch :P

Cheers,

Michael



---

archive/issue_comments_044521.json:
```json
{
    "body": "OK, I don't want Franco or Florent to be offended.\n\nBut this patch is trivial and obvious.\n\nPositive review :)\n\nJaap",
    "created_at": "2009-04-06T18:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5695#issuecomment-44521",
    "user": "jsp"
}
```

OK, I don't want Franco or Florent to be offended.

But this patch is trivial and obvious.

Positive review :)

Jaap



---

archive/issue_comments_044522.json:
```json
{
    "body": "Oops !!! I solved the problem in #5308 but it seems I completely forgot to update the doctests in words ! One hundred apologies.\n\nBy the way since it is not yet merged I can also add my positive review :)\n\nFlorent",
    "created_at": "2009-04-06T19:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5695#issuecomment-44522",
    "user": "hivert"
}
```

Oops !!! I solved the problem in #5308 but it seems I completely forgot to update the doctests in words ! One hundred apologies.

By the way since it is not yet merged I can also add my positive review :)

Florent



---

archive/issue_comments_044523.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-06T21:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5695#issuecomment-44523",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044524.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T21:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5695#issuecomment-44524",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael
