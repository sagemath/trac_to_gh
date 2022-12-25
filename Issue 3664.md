# Issue 3664: major updates to root systems

archive/issues_003664.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3664\n\n",
    "created_at": "2008-07-16T00:43:54Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "major updates to root systems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3664",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

CC:  sage-combinat



Issue created by migration from https://trac.sagemath.org/ticket/3664





---

archive/issue_comments_025844.json:
```json
{
    "body": "Attachment [trac_3664-1.patch](tarball://root/attachments/some-uuid/ticket3664/trac_3664-1.patch) by @mwhansen created at 2008-08-06 19:25:09",
    "created_at": "2008-08-06T19:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25844",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3664-1.patch](tarball://root/attachments/some-uuid/ticket3664/trac_3664-1.patch) by @mwhansen created at 2008-08-06 19:25:09



---

archive/issue_comments_025845.json:
```json
{
    "body": "Attachment [trac_3664-2.patch](tarball://root/attachments/some-uuid/ticket3664/trac_3664-2.patch) by @mwhansen created at 2008-08-06 19:26:21",
    "created_at": "2008-08-06T19:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25845",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3664-2.patch](tarball://root/attachments/some-uuid/ticket3664/trac_3664-2.patch) by @mwhansen created at 2008-08-06 19:26:21



---

archive/issue_comments_025846.json:
```json
{
    "body": "This depends on #3662 and #3781 .\n\nCredit goes to Dan Bump, Nicolas Thiery, Nicolas Borie (first contribution I believe), and Mike Hansen.",
    "created_at": "2008-08-06T19:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25846",
    "user": "https://github.com/mwhansen"
}
```

This depends on #3662 and #3781 .

Credit goes to Dan Bump, Nicolas Thiery, Nicolas Borie (first contribution I believe), and Mike Hansen.



---

archive/issue_comments_025847.json:
```json
{
    "body": "I am seeing doctest failures here:\n\n```\nsage -t -long devel/sage/sage/combinat/crystals/spins.py # 2 doctests failed\nsage -t -long devel/sage/sage/combinat/crystals/letters.py # 3 doctests failed\nsage -t -long devel/sage/sage/combinat/crystals/crystals.py # 13 doctests failed\n```\n\nFor example:\n\n```\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/tmp/spins.py\", line 81:\n    sage: len(TensorProductOfCrystals(C,C,generators=[[C.list()[0],C.list()[0]]]))\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[4]>\", line 1, in <module>\n        len(TensorProductOfCrystals(C,C,generators=[[C.list()[Integer(0)],C.list()[Integer(0)]]]))###line 81:\n    sage: len(TensorProductOfCrystals(C,C,generators=[[C.list()[0],C.list()[0]]]))\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/combinat.py\", line 767, in __len__\n        return self.count()\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py\", line 924, in count\n        for x in self.highest_weight_vectors())\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py\", line 924, in <genexpr>\n        for x in self.highest_weight_vectors())\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/tensor_product.py\", line 365, in weight\n        return sum(self[j].weight() for j in range(len(self))) \n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/tensor_product.py\", line 365, in <genexpr>\n        return sum(self[j].weight() for j in range(len(self)))\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py\", line 590, in weight\n        return self.Phi() - self.Epsilon()\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py\", line 686, in Phi\n        return sum(self.phi(i) * self._parent.Lambda()[i-1] for i in self.index_set())\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py\", line 686, in <genexpr>\n        return sum(self.phi(i) * self._parent.Lambda()[i-1] for i in self.index_set())\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/family.py\", line 387, in __getitem__\n        return self.dictionary.__getitem__(i)\n    KeyError: 0\n```\n\n\nCould it be that there is a patch missing in the dependency chain?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-08T23:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25847",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_025848.json:
```json
{
    "body": "Attachment [trac_3664-3.patch](tarball://root/attachments/some-uuid/ticket3664/trac_3664-3.patch) by @mwhansen created at 2008-08-09 03:46:51",
    "created_at": "2008-08-09T03:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25848",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3664-3.patch](tarball://root/attachments/some-uuid/ticket3664/trac_3664-3.patch) by @mwhansen created at 2008-08-09 03:46:51



---

archive/issue_comments_025849.json:
```json
{
    "body": "I added trac_3664-3.patch that fixes the doctest failures.",
    "created_at": "2008-08-09T03:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25849",
    "user": "https://github.com/mwhansen"
}
```

I added trac_3664-3.patch that fixes the doctest failures.



---

archive/issue_events_003883.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-09T22:24:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3664#event-3883"
}
```



---

archive/issue_comments_025850.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.alpha1",
    "created_at": "2008-08-09T22:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25850",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.1.alpha1



---

archive/issue_comments_025851.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-09T22:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3664#issuecomment-25851",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
