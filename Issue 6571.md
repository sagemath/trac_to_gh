# Issue 6571: Improve iterator of word morphisms

archive/issues_006571.json:
```json
{
    "body": "Assignee: slabbe\n\nCC:  sage-combinat saliola\n\nKeywords: words morphisms\n\nRight now, we can iterate over word morphisms with specific image lengths :\n\n\n```\n    Iterator over morphisms with specific image lengths::\n\n\tsage: map(str, W.iter_morphisms([2, 1]))\n\t['WordMorphism: a->aa, b->a',\n\t 'WordMorphism: a->aa, b->b',\n\t 'WordMorphism: a->ab, b->a',\n\t 'WordMorphism: a->ab, b->b',\n\t 'WordMorphism: a->ba, b->a',\n\t 'WordMorphism: a->ba, b->b',\n\t 'WordMorphism: a->bb, b->a',\n\t 'WordMorphism: a->bb, b->b']\n\tsage: map(str, W.iter_morphisms([2, 2]))\n\t['WordMorphism: a->aa, b->aa',\n\t 'WordMorphism: a->aa, b->ab',\n\t 'WordMorphism: a->aa, b->ba',\n\t 'WordMorphism: a->aa, b->bb',\n\t 'WordMorphism: a->ab, b->aa',\n\t 'WordMorphism: a->ab, b->ab',\n\t 'WordMorphism: a->ab, b->ba',\n\t 'WordMorphism: a->ab, b->bb',\n\t 'WordMorphism: a->ba, b->aa',\n\t 'WordMorphism: a->ba, b->ab',\n\t 'WordMorphism: a->ba, b->ba',\n\t 'WordMorphism: a->ba, b->bb',\n\t 'WordMorphism: a->bb, b->aa',\n\t 'WordMorphism: a->bb, b->ab',\n\t 'WordMorphism: a->bb, b->ba',\n\t 'WordMorphism: a->bb, b->bb']\n\tsage: map(str, W.iter_morphisms([0, 0]))\n\t['WordMorphism: a->, b->']\n\tsage: map(str, W.iter_morphisms([0, 1]))\n\t['WordMorphism: a->, b->a', 'WordMorphism: a->, b->b']\n```\n\n\nI want to iterate over all (non erasing) morphisms! In particuliar, I want the following to work :\n\n\n```\n    sage: W = Words('ab')                 \n    sage: it = W.iter_morphisms()\n    sage: for _ in range(10): print it.next()\n    WordMorphism: a->a, b->a\n    WordMorphism: a->a, b->b\n    WordMorphism: a->b, b->a\n    WordMorphism: a->b, b->b\n    WordMorphism: a->aa, b->a\n    WordMorphism: a->aa, b->b\n    WordMorphism: a->ab, b->a\n    WordMorphism: a->ab, b->b\n    WordMorphism: a->ba, b->a\n    WordMorphism: a->ba, b->b\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6571\n\n",
    "created_at": "2009-07-20T19:27:05Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Improve iterator of word morphisms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6571",
    "user": "slabbe"
}
```
Assignee: slabbe

CC:  sage-combinat saliola

Keywords: words morphisms

Right now, we can iterate over word morphisms with specific image lengths :


```
    Iterator over morphisms with specific image lengths::

	sage: map(str, W.iter_morphisms([2, 1]))
	['WordMorphism: a->aa, b->a',
	 'WordMorphism: a->aa, b->b',
	 'WordMorphism: a->ab, b->a',
	 'WordMorphism: a->ab, b->b',
	 'WordMorphism: a->ba, b->a',
	 'WordMorphism: a->ba, b->b',
	 'WordMorphism: a->bb, b->a',
	 'WordMorphism: a->bb, b->b']
	sage: map(str, W.iter_morphisms([2, 2]))
	['WordMorphism: a->aa, b->aa',
	 'WordMorphism: a->aa, b->ab',
	 'WordMorphism: a->aa, b->ba',
	 'WordMorphism: a->aa, b->bb',
	 'WordMorphism: a->ab, b->aa',
	 'WordMorphism: a->ab, b->ab',
	 'WordMorphism: a->ab, b->ba',
	 'WordMorphism: a->ab, b->bb',
	 'WordMorphism: a->ba, b->aa',
	 'WordMorphism: a->ba, b->ab',
	 'WordMorphism: a->ba, b->ba',
	 'WordMorphism: a->ba, b->bb',
	 'WordMorphism: a->bb, b->aa',
	 'WordMorphism: a->bb, b->ab',
	 'WordMorphism: a->bb, b->ba',
	 'WordMorphism: a->bb, b->bb']
	sage: map(str, W.iter_morphisms([0, 0]))
	['WordMorphism: a->, b->']
	sage: map(str, W.iter_morphisms([0, 1]))
	['WordMorphism: a->, b->a', 'WordMorphism: a->, b->b']
```


I want to iterate over all (non erasing) morphisms! In particuliar, I want the following to work :


```
    sage: W = Words('ab')                 
    sage: it = W.iter_morphisms()
    sage: for _ in range(10): print it.next()
    WordMorphism: a->a, b->a
    WordMorphism: a->a, b->b
    WordMorphism: a->b, b->a
    WordMorphism: a->b, b->b
    WordMorphism: a->aa, b->a
    WordMorphism: a->aa, b->b
    WordMorphism: a->ab, b->a
    WordMorphism: a->ab, b->b
    WordMorphism: a->ba, b->a
    WordMorphism: a->ba, b->b
```


Issue created by migration from https://trac.sagemath.org/ticket/6571





---

archive/issue_comments_053645.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-20T19:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53645",
    "user": "slabbe"
}
```

Changing status from new to assigned.



---

archive/issue_comments_053646.json:
```json
{
    "body": "There is a bug in my patch. Some tests are apparently failing....",
    "created_at": "2009-07-20T20:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53646",
    "user": "slabbe"
}
```

There is a bug in my patch. Some tests are apparently failing....



---

archive/issue_comments_053647.json:
```json
{
    "body": "Failing tests were related to #5600 because the patch I first posted here was depending on `compositions-cleanup-5600-nt.patch`. The patch `word_iter_morphism_6571-sl.patch` should now apply cleanly (including doctests) on sage-4.1.1.alpha0.",
    "created_at": "2009-07-20T20:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53647",
    "user": "slabbe"
}
```

Failing tests were related to #5600 because the patch I first posted here was depending on `compositions-cleanup-5600-nt.patch`. The patch `word_iter_morphism_6571-sl.patch` should now apply cleanly (including doctests) on sage-4.1.1.alpha0.



---

archive/issue_comments_053648.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2009-08-16T05:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53648",
    "user": "AlexGhitza"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_053649.json:
```json
{
    "body": "Attachment [word_iter_morphism_6571-sl.patch](tarball://root/attachments/some-uuid/ticket6571/word_iter_morphism_6571-sl.patch) by slabbe created at 2009-08-19 17:53:42\n\nThis file depends on #6519 as well as on #5600",
    "created_at": "2009-08-19T17:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53649",
    "user": "slabbe"
}
```

Attachment [word_iter_morphism_6571-sl.patch](tarball://root/attachments/some-uuid/ticket6571/word_iter_morphism_6571-sl.patch) by slabbe created at 2009-08-19 17:53:42

This file depends on #6519 as well as on #5600



---

archive/issue_comments_053650.json:
```json
{
    "body": "Since #5600 should be merge soon (it has a positive review), I just uploaded a new patch that uses the benefits of #5600.",
    "created_at": "2009-08-19T18:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53650",
    "user": "slabbe"
}
```

Since #5600 should be merge soon (it has a positive review), I just uploaded a new patch that uses the benefits of #5600.



---

archive/issue_comments_053651.json:
```json
{
    "body": "I made a few changes:\n\n1. As written, the iter_morphisms method is recursive if it is iterating through all morphisms (it calls `self.iter_morphisms(composition)` for all compositions). This is not necessary and it is inefficient. I changed the code to avoid doing this.\n\n2. Switched from `Compositions` to `IntegerListsLex` instead: the patch converted compositions spit out by `Compositions` to lists; so I changed it because compositions are created from the lists output by `IntegerListsLex`.\n\n3. `IntegerListsLex` allows one to specify `min_part`, so I added a `min_length` keyword option (so erasing morphisms can be obtained by taking `min_length=0`). The default is 1 (the current behaviour).",
    "created_at": "2009-08-24T20:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53651",
    "user": "saliola"
}
```

I made a few changes:

1. As written, the iter_morphisms method is recursive if it is iterating through all morphisms (it calls `self.iter_morphisms(composition)` for all compositions). This is not necessary and it is inefficient. I changed the code to avoid doing this.

2. Switched from `Compositions` to `IntegerListsLex` instead: the patch converted compositions spit out by `Compositions` to lists; so I changed it because compositions are created from the lists output by `IntegerListsLex`.

3. `IntegerListsLex` allows one to specify `min_part`, so I added a `min_length` keyword option (so erasing morphisms can be obtained by taking `min_length=0`). The default is 1 (the current behaviour).



---

archive/issue_comments_053652.json:
```json
{
    "body": "Apply on top of word_iter_morphism_6571-sl.patch",
    "created_at": "2009-08-24T20:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53652",
    "user": "saliola"
}
```

Apply on top of word_iter_morphism_6571-sl.patch



---

archive/issue_comments_053653.json:
```json
{
    "body": "Attachment [trac_6571-reviewer.patch](tarball://root/attachments/some-uuid/ticket6571/trac_6571-reviewer.patch) by saliola created at 2009-08-24 20:49:43\n\nIn case it matters: I applied the patches from #5600 before word_iter_morphism_6571-sl.patch.",
    "created_at": "2009-08-24T20:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53653",
    "user": "saliola"
}
```

Attachment [trac_6571-reviewer.patch](tarball://root/attachments/some-uuid/ticket6571/trac_6571-reviewer.patch) by saliola created at 2009-08-24 20:49:43

In case it matters: I applied the patches from #5600 before word_iter_morphism_6571-sl.patch.



---

archive/issue_comments_053654.json:
```json
{
    "body": "This patch applies over the precedent two.",
    "created_at": "2009-08-25T18:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53654",
    "user": "slabbe"
}
```

This patch applies over the precedent two.



---

archive/issue_comments_053655.json:
```json
{
    "body": "Attachment [trac_6571-seb-review.patch](tarball://root/attachments/some-uuid/ticket6571/trac_6571-seb-review.patch) by slabbe created at 2009-08-25 18:53:13\n\nThanks Franco for your good review. I didn't know about `IntegerListsLex`. Allowing erasing morphism is great as well. I just added a small patch to correct a word in a one-line comment. I am currently building the documentation...",
    "created_at": "2009-08-25T18:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53655",
    "user": "slabbe"
}
```

Attachment [trac_6571-seb-review.patch](tarball://root/attachments/some-uuid/ticket6571/trac_6571-seb-review.patch) by slabbe created at 2009-08-25 18:53:13

Thanks Franco for your good review. I didn't know about `IntegerListsLex`. Allowing erasing morphism is great as well. I just added a small patch to correct a word in a one-line comment. I am currently building the documentation...



---

archive/issue_comments_053656.json:
```json
{
    "body": "Attachment [trac_6571-ReST-bug.patch](tarball://root/attachments/some-uuid/ticket6571/trac_6571-ReST-bug.patch) by slabbe created at 2009-08-25 19:44:25\n\nApplies over the precedent three patches.",
    "created_at": "2009-08-25T19:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53656",
    "user": "slabbe"
}
```

Attachment [trac_6571-ReST-bug.patch](tarball://root/attachments/some-uuid/ticket6571/trac_6571-ReST-bug.patch) by slabbe created at 2009-08-25 19:44:25

Applies over the precedent three patches.



---

archive/issue_comments_053657.json:
```json
{
    "body": "There was a bug in the ReST documentation. I just added `trac_6571-ReST-bug.patch` which corrects it. Documentation now builds without warnings. Doctests passed on words.py. I am giving a positive review to Franco's changes.",
    "created_at": "2009-08-25T19:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53657",
    "user": "slabbe"
}
```

There was a bug in the ReST documentation. I just added `trac_6571-ReST-bug.patch` which corrects it. Documentation now builds without warnings. Doctests passed on words.py. I am giving a positive review to Franco's changes.



---

archive/issue_comments_053658.json:
```json
{
    "body": "S\u00e9bastien's documentation changes are good.",
    "created_at": "2009-08-25T19:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53658",
    "user": "saliola"
}
```

Sébastien's documentation changes are good.



---

archive/issue_comments_053659.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-26T21:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6571#issuecomment-53659",
    "user": "mvngu"
}
```

Resolution: fixed
