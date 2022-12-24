# Issue 3664: major updates to root systems

archive/issues_003664.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3664\n\n",
    "created_at": "2008-07-16T00:43:54Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "major updates to root systems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3664",
    "user": "mhansen"
}
```
Assignee: mhansen

CC:  sage-combinat



Issue created by migration from https://trac.sagemath.org/ticket/3664





---

archive/issue_comments_025898.json:
```json
{
    "body": "Attachment [trac_3664-1.patch](tarball://root/attachments/some-uuid/ticket3664/trac_3664-1.patch) by mhansen created at 2008-08-06 19:25:09",
    "created_at": "2008-08-06T19:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25898",
    "user": "mhansen"
}
```

Attachment [trac_3664-1.patch](tarball://root/attachments/some-uuid/ticket3664/trac_3664-1.patch) by mhansen created at 2008-08-06 19:25:09



---

archive/issue_comments_025899.json:
```json
{
    "body": "Attachment [trac_3664-2.patch](tarball://root/attachments/some-uuid/ticket3664/trac_3664-2.patch) by mhansen created at 2008-08-06 19:26:21",
    "created_at": "2008-08-06T19:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25899",
    "user": "mhansen"
}
```

Attachment [trac_3664-2.patch](tarball://root/attachments/some-uuid/ticket3664/trac_3664-2.patch) by mhansen created at 2008-08-06 19:26:21



---

archive/issue_comments_025900.json:
```json
{
    "body": "This depends on #3662 and #3781 .\n\nCredit goes to Dan Bump, Nicolas Thiery, Nicolas Borie (first contribution I believe), and Mike Hansen.",
    "created_at": "2008-08-06T19:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25900",
    "user": "mhansen"
}
```

This depends on #3662 and #3781 .

Credit goes to Dan Bump, Nicolas Thiery, Nicolas Borie (first contribution I believe), and Mike Hansen.



---

archive/issue_comments_025901.json:
```json
{
    "body": "I am seeing doctest failures here:\n\n```\nsage -t -long devel/sage/sage/combinat/crystals/spins.py # 2 doctests failed\nsage -t -long devel/sage/sage/combinat/crystals/letters.py # 3 doctests failed\nsage -t -long devel/sage/sage/combinat/crystals/crystals.py # 13 doctests failed\n```\n\nFor example:\n\n```\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/tmp/spins.py\", line 81:\n    sage: len(TensorProductOfCrystals(C,C,generators=[[C.list()[0],C.list()[0]]]))\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[4]>\", line 1, in <module>\n        len(TensorProductOfCrystals(C,C,generators=[[C.list()[Integer(0)],C.list()[Integer(0)]]]))###line 81:\n    sage: len(TensorProductOfCrystals(C,C,generators=[[C.list()[0],C.list()[0]]]))\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/combinat.py\", line 767, in __len__\n        return self.count()\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py\", line 924, in count\n        for x in self.highest_weight_vectors())\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py\", line 924, in <genexpr>\n        for x in self.highest_weight_vectors())\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/tensor_product.py\", line 365, in weight\n        return sum(self[j].weight() for j in range(len(self))) \n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/tensor_product.py\", line 365, in <genexpr>\n        return sum(self[j].weight() for j in range(len(self)))\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py\", line 590, in weight\n        return self.Phi() - self.Epsilon()\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py\", line 686, in Phi\n        return sum(self.phi(i) * self._parent.Lambda()[i-1] for i in self.index_set())\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py\", line 686, in <genexpr>\n        return sum(self.phi(i) * self._parent.Lambda()[i-1] for i in self.index_set())\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/family.py\", line 387, in __getitem__\n        return self.dictionary.__getitem__(i)\n    KeyError: 0\n```\n\n\nCould it be that there is a patch missing in the dependency chain?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-08T23:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25901",
    "user": "mabshoff"
}
```

I am seeing doctest failures here:

```
sage -t -long devel/sage/sage/combinat/crystals/spins.py # 2 doctests failed
sage -t -long devel/sage/sage/combinat/crystals/letters.py # 3 doctests failed
sage -t -long devel/sage/sage/combinat/crystals/crystals.py # 13 doctests failed
```

For example:

```
File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/tmp/spins.py", line 81:
    sage: len(TensorProductOfCrystals(C,C,generators=[[C.list()[0],C.list()[0]]]))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[4]>", line 1, in <module>
        len(TensorProductOfCrystals(C,C,generators=[[C.list()[Integer(0)],C.list()[Integer(0)]]]))###line 81:
    sage: len(TensorProductOfCrystals(C,C,generators=[[C.list()[0],C.list()[0]]]))
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/combinat.py", line 767, in __len__
        return self.count()
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py", line 924, in count
        for x in self.highest_weight_vectors())
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py", line 924, in <genexpr>
        for x in self.highest_weight_vectors())
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/tensor_product.py", line 365, in weight
        return sum(self[j].weight() for j in range(len(self))) 
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/tensor_product.py", line 365, in <genexpr>
        return sum(self[j].weight() for j in range(len(self)))
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py", line 590, in weight
        return self.Phi() - self.Epsilon()
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py", line 686, in Phi
        return sum(self.phi(i) * self._parent.Lambda()[i-1] for i in self.index_set())
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py", line 686, in <genexpr>
        return sum(self.phi(i) * self._parent.Lambda()[i-1] for i in self.index_set())
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/family.py", line 387, in __getitem__
        return self.dictionary.__getitem__(i)
    KeyError: 0
```


Could it be that there is a patch missing in the dependency chain?

Cheers,

Michael



---

archive/issue_comments_025902.json:
```json
{
    "body": "Attachment [trac_3664-3.patch](tarball://root/attachments/some-uuid/ticket3664/trac_3664-3.patch) by mhansen created at 2008-08-09 03:46:51",
    "created_at": "2008-08-09T03:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25902",
    "user": "mhansen"
}
```

Attachment [trac_3664-3.patch](tarball://root/attachments/some-uuid/ticket3664/trac_3664-3.patch) by mhansen created at 2008-08-09 03:46:51



---

archive/issue_comments_025903.json:
```json
{
    "body": "I added trac_3664-3.patch that fixes the doctest failures.",
    "created_at": "2008-08-09T03:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25903",
    "user": "mhansen"
}
```

I added trac_3664-3.patch that fixes the doctest failures.



---

archive/issue_comments_025904.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.alpha1",
    "created_at": "2008-08-09T22:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25904",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.1.alpha1



---

archive/issue_comments_025905.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-09T22:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25905",
    "user": "mabshoff"
}
```

Resolution: fixed
