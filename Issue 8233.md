# Issue 8233: concatenation of words should preserve the data type represention when possible

archive/issues_008233.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  abmasse\n\nThis concerns word represented by str, tuple and list :\n\n```\nsage: u = Word(range(10))\nsage: type(u)\n<class 'sage.combinat.words.word.FiniteWord_list'>\nsage: type(u*u)\n<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>\n```\n\n```\nsage: v = Word('asdgadsf')\nsage: type(v)\n<class 'sage.combinat.words.word.FiniteWord_str'>\nsage: type(v*v)\n<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>\n```\n\n```\nsage: v = Word((2,3,5,21,34,6))\nsage: type(v)\n<class 'sage.combinat.words.word.FiniteWord_tuple'>\nsage: type(v*v)\n<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8233\n\n",
    "created_at": "2010-02-10T16:16:17Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "concatenation of words should preserve the data type represention when possible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8233",
    "user": "https://github.com/seblabbe"
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

archive/issue_comments_072604.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-11T18:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72604",
    "user": "https://github.com/seblabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072605.json:
```json
{
    "body": "Forget about this patch!",
    "created_at": "2010-02-25T11:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72605",
    "user": "https://github.com/seblabbe"
}
```

Forget about this patch!



---

archive/issue_comments_072606.json:
```json
{
    "body": "Attachment [trac_8233_word_concatenation-sl.2.patch](tarball://root/attachments/some-uuid/ticket8233/trac_8233_word_concatenation-sl.2.patch) by @seblabbe created at 2010-02-28 14:16:43\n\nDepends on #7619.",
    "created_at": "2010-02-28T14:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72606",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8233_word_concatenation-sl.2.patch](tarball://root/attachments/some-uuid/ticket8233/trac_8233_word_concatenation-sl.2.patch) by @seblabbe created at 2010-02-28 14:16:43

Depends on #7619.



---

archive/issue_comments_072607.json:
```json
{
    "body": "Attachment [trac_8233_word_concatenation-sl.patch](tarball://root/attachments/some-uuid/ticket8233/trac_8233_word_concatenation-sl.patch) by @seblabbe created at 2010-03-01 13:21:19",
    "created_at": "2010-03-01T13:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72607",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8233_word_concatenation-sl.patch](tarball://root/attachments/some-uuid/ticket8233/trac_8233_word_concatenation-sl.patch) by @seblabbe created at 2010-03-01 13:21:19



---

archive/issue_comments_072608.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-03T08:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72608",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072609.json:
```json
{
    "body": "Changing keywords from \"\" to \"word, concatenation\".",
    "created_at": "2010-03-03T08:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72609",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing keywords from "" to "word, concatenation".



---

archive/issue_comments_072610.json:
```json
{
    "body": "Tested on sage-4.3.3 after having applied ticket #7619. All tests passed, looking at the documentation with `browse_sage_doc` reveals nothing to be corrected. The improvement seems very reasonable and the code looks fine. Positive review !",
    "created_at": "2010-03-03T08:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72610",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Tested on sage-4.3.3 after having applied ticket #7619. All tests passed, looking at the documentation with `browse_sage_doc` reveals nothing to be corrected. The improvement seems very reasonable and the code looks fine. Positive review !



---

archive/issue_events_019695.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-03-06T08:52:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8233#event-19695"
}
```



---

archive/issue_comments_072611.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T08:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8233#issuecomment-72611",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
