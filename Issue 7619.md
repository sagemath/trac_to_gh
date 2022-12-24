# Issue 7619: Pickling support for finite word defined by callable and iterable

archive/issues_007619.json:
```json
{
    "body": "Assignee: slabbe\n\nCC:  saliola\n\nCurrently pickling doesn't work for finite word defined by iterator and callable :\n\n\n```\nsage: w = Word(iter('abcdefghijkl'))\nsage: loads(dumps(w))\nTraceback (most recent call last):\n...\nPicklingError: Can't pickle <type 'generator'>: attribute lookup __builtin__.generator failed\n```\n\n\nThis is not too hard to support. One just have to expand the iterator to a list  (or a tuple?) and save the list instead:\n\n\n```\nsage: w = Word(iter('abcdefghijkl'))\nsage: loads(dumps(w))\nword: abcdefghijkl\nsage: type(_)\n<class 'sage.combinat.words.word.FiniteWord_list'>\n```\n\n\nThis is more general solution to the problem solved in #7519.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7619\n\n",
    "created_at": "2009-12-08T12:45:18Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Pickling support for finite word defined by callable and iterable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7619",
    "user": "slabbe"
}
```
Assignee: slabbe

CC:  saliola

Currently pickling doesn't work for finite word defined by iterator and callable :


```
sage: w = Word(iter('abcdefghijkl'))
sage: loads(dumps(w))
Traceback (most recent call last):
...
PicklingError: Can't pickle <type 'generator'>: attribute lookup __builtin__.generator failed
```


This is not too hard to support. One just have to expand the iterator to a list  (or a tuple?) and save the list instead:


```
sage: w = Word(iter('abcdefghijkl'))
sage: loads(dumps(w))
word: abcdefghijkl
sage: type(_)
<class 'sage.combinat.words.word.FiniteWord_list'>
```


This is more general solution to the problem solved in #7519.


Issue created by migration from https://trac.sagemath.org/ticket/7619





---

archive/issue_comments_065110.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-08T12:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7619#issuecomment-65110",
    "user": "slabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065111.json:
```json
{
    "body": "The patch save those finite words to list. I wonder if tuple is better or is the same?",
    "created_at": "2009-12-08T12:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7619#issuecomment-65111",
    "user": "slabbe"
}
```

The patch save those finite words to list. I wonder if tuple is better or is the same?



---

archive/issue_comments_065112.json:
```json
{
    "body": "I just uploaded the patch. Pickle is now supported for infinite word defined from a function :\n\n\n```\nsage: w = Word(lambda n:n)\nsage: loads(dumps(w))\nword: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...\n```\n\n\nIt uses the `pickle_function` and `unpickle_function` (which gives a new utility for `datatype` argument)\n\n\n```\nsage: lambda n:n\n<function <lambda> at 0x887e764>\nsage: pickle_function(_)\n\"csage.misc.fpickle\\ncode_ctor\\np1\\n(I1\\nI1\\nI1\\nI67\\nS'|\\\\x00\\\\x00S'\\np2\\n(t(t(S'n'\\ntp3\\nS'<ipython console>'\\np4\\nS'<lambda>'\\np5\\nI1\\nS''\\ntRp6\\n.\"\nsage: Word(_, datatype='pickled_function')\nword: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...\n```\n\n\nSince `pickle_function` fails on `CallableFromListOfWords`, those finite words are expanded as a list in order to be saved:\n\n\n```\nsage: w = Word(range(5)) * Word('abcde')\nsage: type(w)\n<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>\nsage: z = loads(dumps(w))\nsage: z\nword: 01234abcde\nsage: type(z)\n<class 'sage.combinat.words.word.FiniteWord_list'>\n```\n\n\nNeeds review!!",
    "created_at": "2010-01-14T18:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7619#issuecomment-65112",
    "user": "slabbe"
}
```

I just uploaded the patch. Pickle is now supported for infinite word defined from a function :


```
sage: w = Word(lambda n:n)
sage: loads(dumps(w))
word: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...
```


It uses the `pickle_function` and `unpickle_function` (which gives a new utility for `datatype` argument)


```
sage: lambda n:n
<function <lambda> at 0x887e764>
sage: pickle_function(_)
"csage.misc.fpickle\ncode_ctor\np1\n(I1\nI1\nI1\nI67\nS'|\\x00\\x00S'\np2\n(t(t(S'n'\ntp3\nS'<ipython console>'\np4\nS'<lambda>'\np5\nI1\nS''\ntRp6\n."
sage: Word(_, datatype='pickled_function')
word: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...
```


Since `pickle_function` fails on `CallableFromListOfWords`, those finite words are expanded as a list in order to be saved:


```
sage: w = Word(range(5)) * Word('abcde')
sage: type(w)
<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>
sage: z = loads(dumps(w))
sage: z
word: 01234abcde
sage: type(z)
<class 'sage.combinat.words.word.FiniteWord_list'>
```


Needs review!!



---

archive/issue_comments_065113.json:
```json
{
    "body": "Forget about this patch!",
    "created_at": "2010-02-16T22:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7619#issuecomment-65113",
    "user": "slabbe"
}
```

Forget about this patch!



---

archive/issue_comments_065114.json:
```json
{
    "body": "Attachment [trac_7619_pickle_for_FiniteWord_iter_callable-sl.patch](tarball://root/attachments/some-uuid/ticket7619/trac_7619_pickle_for_FiniteWord_iter_callable-sl.patch) by slabbe created at 2010-02-25 10:59:01\n\nDepends on #7520.",
    "created_at": "2010-02-25T10:59:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7619#issuecomment-65114",
    "user": "slabbe"
}
```

Attachment [trac_7619_pickle_for_FiniteWord_iter_callable-sl.patch](tarball://root/attachments/some-uuid/ticket7619/trac_7619_pickle_for_FiniteWord_iter_callable-sl.patch) by slabbe created at 2010-02-25 10:59:01

Depends on #7520.



---

archive/issue_comments_065115.json:
```json
{
    "body": "Changing keywords from \"\" to \"words\".",
    "created_at": "2010-03-02T02:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7619#issuecomment-65115",
    "user": "saliola"
}
```

Changing keywords from "" to "words".



---

archive/issue_comments_065116.json:
```json
{
    "body": "Hello Sebastien. I've taken a look at the patch. Great changes! We can now pickle objects that we could not have pickled before.\n\nThe patch applies cleanly to sage-4.3.3 and all tests passed for `make test`.",
    "created_at": "2010-03-02T02:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7619#issuecomment-65116",
    "user": "saliola"
}
```

Hello Sebastien. I've taken a look at the patch. Great changes! We can now pickle objects that we could not have pickled before.

The patch applies cleanly to sage-4.3.3 and all tests passed for `make test`.



---

archive/issue_comments_065117.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-02T02:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7619#issuecomment-65117",
    "user": "saliola"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065118.json:
```json
{
    "body": "Merged [trac_7619_pickle_for_FiniteWord_iter_callable-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7619/trac_7619_pickle_for_FiniteWord_iter_callable-sl.patch).",
    "created_at": "2010-03-03T14:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7619#issuecomment-65118",
    "user": "mvngu"
}
```

Merged [trac_7619_pickle_for_FiniteWord_iter_callable-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7619/trac_7619_pickle_for_FiniteWord_iter_callable-sl.patch).



---

archive/issue_comments_065119.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7619#issuecomment-65119",
    "user": "mvngu"
}
```

Resolution: fixed
