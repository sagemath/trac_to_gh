# Issue 5534: [with patch, positive review] sage.combinat.subword.smallest_positions modifying its input (use #5200)

archive/issues_005534.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat\n\nI came across this function in Sage-Combinat,\n\nsage.combinat.subword.smallest_positions(word, subword, pos=0)\n\nRunning this function not only returns the positions in \"word\" where\n\"subword\" occurs, but it modifies \"subword\" to be this sequence of\npositions.  Is there a reason for this?  It seems to me that it should\nleave \"subword\" unchanged, but maybe I'm not thinking of something.\n\n```\nsage: w = [\"a\", \"b\", \"c\", \"d\"]\nsage: ww = [\"b\", \"d\"]\nsage: sage.combinat.subword.smallest_positions(w, ww)\n[1, 3]\nsage: w\n['a', 'b', 'c', 'd']\nsage: ww\n[1, 3]\n```\n\nThanks,\nSteve\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5534\n\n",
    "closed_at": "2009-04-03T00:57:17Z",
    "created_at": "2009-03-16T20:46:13Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] sage.combinat.subword.smallest_positions modifying its input (use #5200)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5534",
    "user": "https://github.com/nthiery"
}
```
Assignee: @hivert

CC:  sage-combinat

I came across this function in Sage-Combinat,

sage.combinat.subword.smallest_positions(word, subword, pos=0)

Running this function not only returns the positions in "word" where
"subword" occurs, but it modifies "subword" to be this sequence of
positions.  Is there a reason for this?  It seems to me that it should
leave "subword" unchanged, but maybe I'm not thinking of something.

```
sage: w = ["a", "b", "c", "d"]
sage: ww = ["b", "d"]
sage: sage.combinat.subword.smallest_positions(w, ww)
[1, 3]
sage: w
['a', 'b', 'c', 'd']
sage: ww
[1, 3]
```

Thanks,
Steve




Issue created by migration from https://trac.sagemath.org/ticket/5534





---

archive/issue_comments_042939.json:
```json
{
    "body": "Fixed (see the attached patch):\n\nNow:\n\n```\nsage: w = [\"a\", \"b\", \"c\", \"d\"]\nsage: ww = [\"b\", \"d\"]\nsage: sage.combinat.subword.smallest_positions(w, ww)\n[1, 3]\nsage: w\n['a', 'b', 'c', 'd']\nsage: ww\n['b', 'd']\n```\n\nNote the patch only applies on top of #5200\n\nAuthor : Florent Hivert",
    "created_at": "2009-03-17T09:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5534#issuecomment-42939",
    "user": "https://github.com/hivert"
}
```

Fixed (see the attached patch):

Now:

```
sage: w = ["a", "b", "c", "d"]
sage: ww = ["b", "d"]
sage: sage.combinat.subword.smallest_positions(w, ww)
[1, 3]
sage: w
['a', 'b', 'c', 'd']
sage: ww
['b', 'd']
```

Note the patch only applies on top of #5200

Author : Florent Hivert



---

archive/issue_comments_042940.json:
```json
{
    "body": "Changing assignee from @mwhansen to @hivert.",
    "created_at": "2009-03-17T09:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5534#issuecomment-42940",
    "user": "https://github.com/hivert"
}
```

Changing assignee from @mwhansen to @hivert.



---

archive/issue_comments_042941.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-19T17:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5534#issuecomment-42941",
    "user": "https://github.com/hivert"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042942.json:
```json
{
    "body": "This patch causes doctest failures in \n\n```\n\tsage -t -long devel/sage/sage/combinat/subword.py # 23 doctests failed\n\tsage -t -long devel/sage/sage/combinat/subset.py # 10 doctests failed\n```\nFor example\"\n\n```\nsage -t -long \"devel/sage/sage/combinat/subset.py\"          \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/combinat/subset.py\", line 566:\n    sage: [] in S\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_25[3]>\", line 1, in <module>\n        [] in S###line 566:\n    sage: [] in S\n      File \"/scratch/mabshoff/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/subset.py\", line 579, in __contains__\n        return sorted(s) in subword.Subwords(self._s)\n      File \"/scratch/mabshoff/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/subword.py\", line 130, in __contains__\n        if smallest_positions(self.w, w) != False:\n      File \"/scratch/mabshoff/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/subword.py\", line 315, in smallest_positions\n        res = [None] * subword.length()\n    AttributeError: 'list' object has no attribute 'length'\n**********************************************************************\n```\n\nThis is with #5200 merged, so is there another dependency?\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T07:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5534#issuecomment-42942",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch causes doctest failures in 

```
	sage -t -long devel/sage/sage/combinat/subword.py # 23 doctests failed
	sage -t -long devel/sage/sage/combinat/subset.py # 10 doctests failed
```
For example"

```
sage -t -long "devel/sage/sage/combinat/subset.py"          
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/combinat/subset.py", line 566:
    sage: [] in S
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_25[3]>", line 1, in <module>
        [] in S###line 566:
    sage: [] in S
      File "/scratch/mabshoff/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/subset.py", line 579, in __contains__
        return sorted(s) in subword.Subwords(self._s)
      File "/scratch/mabshoff/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/subword.py", line 130, in __contains__
        if smallest_positions(self.w, w) != False:
      File "/scratch/mabshoff/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/subword.py", line 315, in smallest_positions
        res = [None] * subword.length()
    AttributeError: 'list' object has no attribute 'length'
**********************************************************************
```

This is with #5200 merged, so is there another dependency?

Cheers,

Michael



---

archive/issue_comments_042943.json:
```json
{
    "body": "Attachment [subwords_fix-5534-submitted.patch](tarball://root/attachments/some-uuid/ticket5534/subwords_fix-5534-submitted.patch) by @hivert created at 2009-03-28 18:42:54",
    "created_at": "2009-03-28T18:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5534#issuecomment-42943",
    "user": "https://github.com/hivert"
}
```

Attachment [subwords_fix-5534-submitted.patch](tarball://root/attachments/some-uuid/ticket5534/subwords_fix-5534-submitted.patch) by @hivert created at 2009-03-28 18:42:54



---

archive/issue_comments_042944.json:
```json
{
    "body": "Oups !!! It looks like Nicolas last review requirement was simply syntactically wrong. He required to write\n`res = [None] * subword.length()` where he meant  `res = [None] * len(subword)`. The bad think is that no one of use take care to even launch the tests. Shame on us !!!\n\nThe re-sumbmitted patch should work. \n\nCheers,\n\nFlorent",
    "created_at": "2009-03-28T18:47:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5534#issuecomment-42944",
    "user": "https://github.com/hivert"
}
```

Oups !!! It looks like Nicolas last review requirement was simply syntactically wrong. He required to write
`res = [None] * subword.length()` where he meant  `res = [None] * len(subword)`. The bad think is that no one of use take care to even launch the tests. Shame on us !!!

The re-sumbmitted patch should work. 

Cheers,

Florent



---

archive/issue_events_012987.json:
```json
{
    "actor": "https://github.com/nthiery",
    "created_at": "2009-04-02T06:01:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5534",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5534#event-12987"
}
```



---

archive/issue_events_012988.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-03T00:57:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5534",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5534#event-12988"
}
```



---

archive/issue_events_012989.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-03T00:57:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5534",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5534#event-12989"
}
```



---

archive/issue_comments_042945.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-03T00:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5534#issuecomment-42945",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_012990.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-03T00:57:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5534",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5534#event-12990"
}
```



---

archive/issue_comments_042946.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-03T00:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5534#issuecomment-42946",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc0.

Cheers,

Michael
