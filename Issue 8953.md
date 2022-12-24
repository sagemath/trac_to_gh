# Issue 8953: Perfect graph recognition algorithm

archive/issues_008953.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  rhinton\n\nCostly, but nice enough for small graphs :-)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8953\n\n",
    "created_at": "2010-05-12T01:38:44Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Perfect graph recognition algorithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8953",
    "user": "ncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  rhinton

Costly, but nice enough for small graphs :-)

Issue created by migration from https://trac.sagemath.org/ticket/8953





---

archive/issue_comments_082504.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-12T21:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82504",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082505.json:
```json
{
    "body": "New version dealing with BipartiteGraph graphs. Sorry for the two versions, they are identical ;-)\n\nNathann",
    "created_at": "2010-05-12T21:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82505",
    "user": "ncohen"
}
```

New version dealing with BipartiteGraph graphs. Sorry for the two versions, they are identical ;-)

Nathann



---

archive/issue_comments_082506.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-05-20T20:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82506",
    "user": "ncohen"
}
```

Changing priority from major to minor.



---

archive/issue_comments_082507.json:
```json
{
    "body": "Doctests fail:\n\n```\nsage -t  \"devel/sage-main/sage/graphs/graph.py\"             \n**********************************************************************\nFile \"/Users/rlmill/sage-4.4.4.alpha0/devel/sage-main/sage/graphs/graph.py\", line 1458:\n    sage: g.is_perfect()\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/rlmill/sage-4.4.4.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/rlmill/sage-4.4.4.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/rlmill/sage-4.4.4.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_9[5]>\", line 1, in <module>\n        g.is_perfect()###line 1458:\n    sage: g.is_perfect()\n      File \"/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/graphs/graph.py\", line 1516, in is_perfect\n        counter_example = self.induced_subgraph_search(graphs.CycleGraph(i))\n    AttributeError: 'Graph' object has no attribute 'induced_subgraph_search'\n**********************************************************************\n```\n\nfor example. Also, you should explain what a perfect graph is in the docstring, before quoting the theorem.",
    "created_at": "2010-06-17T20:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82507",
    "user": "rlm"
}
```

Doctests fail:

```
sage -t  "devel/sage-main/sage/graphs/graph.py"             
**********************************************************************
File "/Users/rlmill/sage-4.4.4.alpha0/devel/sage-main/sage/graphs/graph.py", line 1458:
    sage: g.is_perfect()
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.4.4.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[5]>", line 1, in <module>
        g.is_perfect()###line 1458:
    sage: g.is_perfect()
      File "/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/graphs/graph.py", line 1516, in is_perfect
        counter_example = self.induced_subgraph_search(graphs.CycleGraph(i))
    AttributeError: 'Graph' object has no attribute 'induced_subgraph_search'
**********************************************************************
```

for example. Also, you should explain what a perfect graph is in the docstring, before quoting the theorem.



---

archive/issue_comments_082508.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-17T20:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82508",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082509.json:
```json
{
    "body": "Sorryyyyy !! This method has been renamed during the review of the corresponding ticket, and I didn't update this patch... I'll send one in a second !\n\nNathann",
    "created_at": "2010-06-18T10:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82509",
    "user": "ncohen"
}
```

Sorryyyyy !! This method has been renamed during the review of the corresponding ticket, and I didn't update this patch... I'll send one in a second !

Nathann



---

archive/issue_comments_082510.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-18T10:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82510",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082511.json:
```json
{
    "body": "Your new patch applies fine (without #8927 even) and passes all doctests in `sage/graphs`. If you approve of the editing changes in my referee's patch, then set this ticket to positive review!",
    "created_at": "2010-06-18T14:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82511",
    "user": "rlm"
}
```

Your new patch applies fine (without #8927 even) and passes all doctests in `sage/graphs`. If you approve of the editing changes in my referee's patch, then set this ticket to positive review!



---

archive/issue_comments_082512.json:
```json
{
    "body": "Agreed ! :-)\n\nThanksssssssss !\n\nNathann",
    "created_at": "2010-06-18T15:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82512",
    "user": "ncohen"
}
```

Agreed ! :-)

Thanksssssssss !

Nathann



---

archive/issue_comments_082513.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-18T15:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82513",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082514.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-29T00:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82514",
    "user": "rlm"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_082515.json:
```json
{
    "body": "After sage-4.5.alpha1 is released, this will lead to a failed doctest:\n\n\n```\n**********************************************************************\nFile \"/scratch/rlmill/release/sage-4.5.alpha1/devel/sage-main/sage/graphs/graph.py\", line 1629:\n    sage: g.is_perfect()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/rlmill/release/sage-4.5.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/rlmill/release/sage-4.5.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/rlmill/release/sage-4.5.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_11[5]>\", line 1, in <module>\n        g.is_perfect()###line 1629:\n    sage: g.is_perfect()\n      File \"/scratch/rlmill/release/sage-4.5.alpha1/local/lib/python/site-packages/sage/graphs/graph.py\", line 1702, in is_perfect\n        counter_example = self.subgraph_search(graphs.CycleGraph(i), induced = True).complement()\n    AttributeError: 'NoneType' object has no attribute 'complement'  \n**********************************************************************\n```\n",
    "created_at": "2010-06-29T00:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82515",
    "user": "rlm"
}
```

After sage-4.5.alpha1 is released, this will lead to a failed doctest:


```
**********************************************************************
File "/scratch/rlmill/release/sage-4.5.alpha1/devel/sage-main/sage/graphs/graph.py", line 1629:
    sage: g.is_perfect()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/rlmill/release/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/rlmill/release/sage-4.5.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/rlmill/release/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_11[5]>", line 1, in <module>
        g.is_perfect()###line 1629:
    sage: g.is_perfect()
      File "/scratch/rlmill/release/sage-4.5.alpha1/local/lib/python/site-packages/sage/graphs/graph.py", line 1702, in is_perfect
        counter_example = self.subgraph_search(graphs.CycleGraph(i), induced = True).complement()
    AttributeError: 'NoneType' object has no attribute 'complement'  
**********************************************************************
```




---

archive/issue_comments_082516.json:
```json
{
    "body": "1) Sorryyyyyyyyy !!!\n2) Fixed :-)\n\nNathann",
    "created_at": "2010-06-29T07:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82516",
    "user": "ncohen"
}
```

1) Sorryyyyyyyyy !!!
2) Fixed :-)

Nathann



---

archive/issue_comments_082517.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-29T07:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82517",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082518.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-18T09:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82518",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082519.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-19T01:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82519",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082520.json:
```json
{
    "body": "Hello !!! \n\nMy patch applied fine on sage-4.5, though I just updated it... \n\nIt also contains your modifications :-)\n\nNathann",
    "created_at": "2010-07-19T01:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82520",
    "user": "ncohen"
}
```

Hello !!! 

My patch applied fine on sage-4.5, though I just updated it... 

It also contains your modifications :-)

Nathann



---

archive/issue_comments_082521.json:
```json
{
    "body": "Attachment [trac_8953.patch](tarball://root/attachments/some-uuid/ticket8953/trac_8953.patch) by rlm created at 2010-07-19 08:34:02\n\nIt was probably the other patch causing conflict.",
    "created_at": "2010-07-19T08:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82521",
    "user": "rlm"
}
```

Attachment [trac_8953.patch](tarball://root/attachments/some-uuid/ticket8953/trac_8953.patch) by rlm created at 2010-07-19 08:34:02

It was probably the other patch causing conflict.



---

archive/issue_comments_082522.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-19T08:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82522",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082523.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T02:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8953#issuecomment-82523",
    "user": "mpatel"
}
```

Resolution: fixed
