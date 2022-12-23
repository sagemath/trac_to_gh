# Issue 8233: concatenation of words should preserve the data type represention when possible

archive/issues_008233.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  abmasse\n\nThis concerns word represented by str, tuple and list :\n\n\n```\nsage: u = Word(range(10))\nsage: type(u)\n<class 'sage.combinat.words.word.FiniteWord_list'>\nsage: type(u*u)\n<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>\n```\n\n\n```\nsage: v = Word('asdgadsf')\nsage: type(v)\n<class 'sage.combinat.words.word.FiniteWord_str'>\nsage: type(v*v)\n<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>\n```\n\n\n```\nsage: v = Word((2,3,5,21,34,6))\nsage: type(v)\n<class 'sage.combinat.words.word.FiniteWord_tuple'>\nsage: type(v*v)\n<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8233\n\n",
    "created_at": "2010-02-10T16:16:17Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "concatenation of words should preserve the data type represention when possible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8233",
    "user": "slabbe"
}
```
Assignee: sage-combinat

CC:  abmasse

This concerns word represented by str, tuple and list :


```
sage: u = Word(range(10))
sage: type(u)
<class 'sage.combinat.words.word.FiniteWord_list'>
sage: type(u*u)
<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>
```


```
sage: v = Word('asdgadsf')
sage: type(v)
<class 'sage.combinat.words.word.FiniteWord_str'>
sage: type(v*v)
<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>
```


```
sage: v = Word((2,3,5,21,34,6))
sage: type(v)
<class 'sage.combinat.words.word.FiniteWord_tuple'>
sage: type(v*v)
<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>
```


Issue created by migration from https://trac.sagemath.org/ticket/8233





---

archive/issue_comments_072726.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-11T18:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72726",
    "user": "slabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072727.json:
```json
{
    "body": "Forget about this patch!",
    "created_at": "2010-02-25T11:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72727",
    "user": "slabbe"
}
```

Forget about this patch!



---

archive/issue_comments_072728.json:
```json
{
    "body": "Attachment\n\nDepends on #7619.",
    "created_at": "2010-02-28T14:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72728",
    "user": "slabbe"
}
```

Attachment

Depends on #7619.



---

archive/issue_comments_072729.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-03-01T13:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72729",
    "user": "slabbe"
}
```

Attachment



---

archive/issue_comments_072730.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-03T08:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72730",
    "user": "abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072731.json:
```json
{
    "body": "Changing keywords from \"\" to \"word, concatenation\".",
    "created_at": "2010-03-03T08:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72731",
    "user": "abmasse"
}
```

Changing keywords from "" to "word, concatenation".



---

archive/issue_comments_072732.json:
```json
{
    "body": "Tested on sage-4.3.3 after having applied ticket #7619. All tests passed, looking at the documentation with `browse_sage_doc` reveals nothing to be corrected. The improvement seems very reasonable and the code looks fine. Positive review !",
    "created_at": "2010-03-03T08:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72732",
    "user": "abmasse"
}
```

Tested on sage-4.3.3 after having applied ticket #7619. All tests passed, looking at the documentation with `browse_sage_doc` reveals nothing to be corrected. The improvement seems very reasonable and the code looks fine. Positive review !



---

archive/issue_comments_072733.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T08:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72733",
    "user": "mhansen"
}
```

Resolution: fixed
