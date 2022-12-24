# Issue 4954: Words_over_Alphabet should check the type of input alphabet

archive/issues_004954.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nKeywords: words alphabet\n\nDo\n\n\n```\nsage: W=Words('ab')\nsage: W.alphabet?\n```\n\n\nand you get the following help example :\n\n\n```\nsage: from sage.combinat.words.words import Words_over_Alphabet\nsage: W = Words_over_Alphabet([1,2,3])\nsage: W.alphabet()\n[1, 2, 3]\nsage: from sage.combinat.words.words import OrderedAlphabet\nsage: W = Words_over_Alphabet(OrderedAlphabet('ab'))\nsage: W.alphabet()\nOrdered Alphabet ['a', 'b']\n```\n\n\nThe first of the above example is misleading. In fact, it is not usable :\n\n\n```\nsage: from sage.combinat.words.words import Words_over_Alphabet\nsage: W = Words_over_Alphabet([1,2,3])\nsage: W.alphabet()\n[1, 2, 3]\nsage: W([1,1,1,2,1,3])\nTraceback (most recent call last):\n...\nAttributeError: 'list' object has no attribute 'rank'\n```\n\n\nThe problem comes from the fact that Words_over_Alphabet doesn't check the input alphabet before asigning it to self._alphabet(). It should either do `alphabet=OrderedAlphabet(alphabet)` before or check the type of the input alphabet with a isinstance.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4954\n\n",
    "created_at": "2009-01-07T21:07:20Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Words_over_Alphabet should check the type of input alphabet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4954",
    "user": "@seblabbe"
}
```
Assignee: @mwhansen

CC:  sage-combinat

Keywords: words alphabet

Do


```
sage: W=Words('ab')
sage: W.alphabet?
```


and you get the following help example :


```
sage: from sage.combinat.words.words import Words_over_Alphabet
sage: W = Words_over_Alphabet([1,2,3])
sage: W.alphabet()
[1, 2, 3]
sage: from sage.combinat.words.words import OrderedAlphabet
sage: W = Words_over_Alphabet(OrderedAlphabet('ab'))
sage: W.alphabet()
Ordered Alphabet ['a', 'b']
```


The first of the above example is misleading. In fact, it is not usable :


```
sage: from sage.combinat.words.words import Words_over_Alphabet
sage: W = Words_over_Alphabet([1,2,3])
sage: W.alphabet()
[1, 2, 3]
sage: W([1,1,1,2,1,3])
Traceback (most recent call last):
...
AttributeError: 'list' object has no attribute 'rank'
```


The problem comes from the fact that Words_over_Alphabet doesn't check the input alphabet before asigning it to self._alphabet(). It should either do `alphabet=OrderedAlphabet(alphabet)` before or check the type of the input alphabet with a isinstance.

Issue created by migration from https://trac.sagemath.org/ticket/4954





---

archive/issue_comments_037667.json:
```json
{
    "body": "Changing assignee from @mwhansen to @seblabbe.",
    "created_at": "2009-01-07T21:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4954#issuecomment-37667",
    "user": "@seblabbe"
}
```

Changing assignee from @mwhansen to @seblabbe.



---

archive/issue_comments_037668.json:
```json
{
    "body": "This problem was solved by #6519 :\n\n\n```\nsage: from sage.combinat.words.words import Words_over_Alphabet\nsage: W = Words_over_Alphabet([1,2,3])\nsage: W.alphabet()\n[1, 2, 3]\nsage: W([1,1,1,2,1,3])\nword: 111213\n```\n\n\n\n```\nsage: Y = Words_over_Alphabet('abcde')\nsage: Y.alphabet()\n'abcde'\nsage: Y('abababacde')\nword: abababacde\n```\n\n\nSo, I propose that this ticket be closed.",
    "created_at": "2009-07-22T20:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4954#issuecomment-37668",
    "user": "@seblabbe"
}
```

This problem was solved by #6519 :


```
sage: from sage.combinat.words.words import Words_over_Alphabet
sage: W = Words_over_Alphabet([1,2,3])
sage: W.alphabet()
[1, 2, 3]
sage: W([1,1,1,2,1,3])
word: 111213
```



```
sage: Y = Words_over_Alphabet('abcde')
sage: Y.alphabet()
'abcde'
sage: Y('abababacde')
word: abababacde
```


So, I propose that this ticket be closed.



---

archive/issue_comments_037669.json:
```json
{
    "body": "Closing this as a duplicate of #6519.",
    "created_at": "2009-07-22T20:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4954#issuecomment-37669",
    "user": "mvngu"
}
```

Closing this as a duplicate of #6519.



---

archive/issue_comments_037670.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-07-22T20:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4954#issuecomment-37670",
    "user": "mvngu"
}
```

Resolution: duplicate
