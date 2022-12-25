# Issue 7519: Allowing the choice of word datatype for images under WordMorphism

archive/issues_007519.json:
```json
{
    "body": "Assignee: @seblabbe\n\nCC:  @videlec @saliola\n\nBy default, the image of a word under a morphism is given by a iterator which is good because it is returned in constant time but which is bad because it is not directly picklable.\n\n\n```\nsage: m = WordMorphism({0:[0,1], 1:[1,0,0,1]})\nsage: print m\nWordMorphism: 0->01, 1->1001\nsage: W = m.domain()\nsage: w = W([0,1,1,1])\nsage: type(w)\n<class 'sage.combinat.words.word.FiniteWord_list'>\nsage: z = m(w)\nsage: type(z)\n<class 'sage.combinat.words.word.FiniteWord_iter_with_caching'>\nsage: loads(dumps(z))\nTraceback (most recent call last):\n...\nPicklingError: Can't pickle <type 'generator'>: attribute lookup __builtin__.generator failed\n```\n\n\nThis patch allows one to suggest under which datatype to represent the word :\n\n\n```\nsage: m = WordMorphism({0:[0,1], 1:[1,0,0,1]})\nsage: z = m([0,1,1,1], datatype='list')\nsage: type(z)\n<class 'sage.combinat.words.word.FiniteWord_list'>\nsage: loads(dumps(z))\nword: 01100110011001\n```\n\n\nIt also leaves the current default behavior :\n\n\n```\nsage: m = WordMorphism({0:[0,1], 1:[1,0,0,1]})\nsage: m([0,1,1,1])\nword: 01100110011001\nsage: type(_)\n<class 'sage.combinat.words.word.FiniteWord_iter_with_caching'>\n```\n\n\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7519\n\n",
    "created_at": "2009-11-23T12:38:31Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Allowing the choice of word datatype for images under WordMorphism",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7519",
    "user": "https://github.com/seblabbe"
}
```
Assignee: @seblabbe

CC:  @videlec @saliola

By default, the image of a word under a morphism is given by a iterator which is good because it is returned in constant time but which is bad because it is not directly picklable.


```
sage: m = WordMorphism({0:[0,1], 1:[1,0,0,1]})
sage: print m
WordMorphism: 0->01, 1->1001
sage: W = m.domain()
sage: w = W([0,1,1,1])
sage: type(w)
<class 'sage.combinat.words.word.FiniteWord_list'>
sage: z = m(w)
sage: type(z)
<class 'sage.combinat.words.word.FiniteWord_iter_with_caching'>
sage: loads(dumps(z))
Traceback (most recent call last):
...
PicklingError: Can't pickle <type 'generator'>: attribute lookup __builtin__.generator failed
```


This patch allows one to suggest under which datatype to represent the word :


```
sage: m = WordMorphism({0:[0,1], 1:[1,0,0,1]})
sage: z = m([0,1,1,1], datatype='list')
sage: type(z)
<class 'sage.combinat.words.word.FiniteWord_list'>
sage: loads(dumps(z))
word: 01100110011001
```


It also leaves the current default behavior :


```
sage: m = WordMorphism({0:[0,1], 1:[1,0,0,1]})
sage: m([0,1,1,1])
word: 01100110011001
sage: type(_)
<class 'sage.combinat.words.word.FiniteWord_iter_with_caching'>
```







Issue created by migration from https://trac.sagemath.org/ticket/7519





---

archive/issue_comments_063579.json:
```json
{
    "body": "Attachment [trac_7519_wordmorphism_datatype_choice-sl.patch](tarball://root/attachments/some-uuid/ticket7519/trac_7519_wordmorphism_datatype_choice-sl.patch) by @seblabbe created at 2009-11-23 12:56:33",
    "created_at": "2009-11-23T12:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7519#issuecomment-63579",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_7519_wordmorphism_datatype_choice-sl.patch](tarball://root/attachments/some-uuid/ticket7519/trac_7519_wordmorphism_datatype_choice-sl.patch) by @seblabbe created at 2009-11-23 12:56:33



---

archive/issue_comments_063580.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-23T12:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7519#issuecomment-63580",
    "user": "https://github.com/seblabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063581.json:
```json
{
    "body": "This patch seems to depend on #7405.\n\nPatches apply cleanly on top of sage-4.3.alpha0.\n\nThe doctests in sage.combinat.words pass.\n\nI'm running the full test suite now. Will report back soon.",
    "created_at": "2009-11-23T15:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7519#issuecomment-63581",
    "user": "https://github.com/saliola"
}
```

This patch seems to depend on #7405.

Patches apply cleanly on top of sage-4.3.alpha0.

The doctests in sage.combinat.words pass.

I'm running the full test suite now. Will report back soon.



---

archive/issue_comments_063582.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-23T16:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7519#issuecomment-63582",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063583.json:
```json
{
    "body": "Tests pass. Positive review.",
    "created_at": "2009-11-23T16:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7519#issuecomment-63583",
    "user": "https://github.com/saliola"
}
```

Tests pass. Positive review.



---

archive/issue_comments_063584.json:
```json
{
    "body": "Great. Thank you Franco for the quick review.",
    "created_at": "2009-11-23T16:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7519#issuecomment-63584",
    "user": "https://github.com/seblabbe"
}
```

Great. Thank you Franco for the quick review.



---

archive/issue_events_017840.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-29T05:45:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7519",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7519#event-17840"
}
```



---

archive/issue_comments_063585.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7519#issuecomment-63585",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
