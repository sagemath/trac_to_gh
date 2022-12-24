# Issue 8215: The empty word is a factor of a word

archive/issues_008215.json:
```json
{
    "body": "Assignee: slabbe\n\nCC:  sage-combinat abmasse\n\nKeywords: empty word\n\nThe following three results should be True.\n\n\n```\nsage: Word().is_factor(Word())\nFalse\nsage: Word().is_factor(Word('abad'))\nFalse\nsage: Word().is_factor(Word([0,1,2]))\nFalse\nsage: Word('').is_factor(Word('abad'))\nFalse\nsage: Word([]).is_factor(Word([0,1,2]))\nFalse\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8215\n\n",
    "created_at": "2010-02-08T14:16:09Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "The empty word is a factor of a word",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8215",
    "user": "slabbe"
}
```
Assignee: slabbe

CC:  sage-combinat abmasse

Keywords: empty word

The following three results should be True.


```
sage: Word().is_factor(Word())
False
sage: Word().is_factor(Word('abad'))
False
sage: Word().is_factor(Word([0,1,2]))
False
sage: Word('').is_factor(Word('abad'))
False
sage: Word([]).is_factor(Word([0,1,2]))
False
```


Issue created by migration from https://trac.sagemath.org/ticket/8215





---

archive/issue_comments_072442.json:
```json
{
    "body": "Attachment [trac_8215_empty_word-sl.patch](tarball://root/attachments/some-uuid/ticket8215/trac_8215_empty_word-sl.patch) by slabbe created at 2010-02-08 14:19:39",
    "created_at": "2010-02-08T14:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8215#issuecomment-72442",
    "user": "slabbe"
}
```

Attachment [trac_8215_empty_word-sl.patch](tarball://root/attachments/some-uuid/ticket8215/trac_8215_empty_word-sl.patch) by slabbe created at 2010-02-08 14:19:39



---

archive/issue_comments_072443.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-08T14:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8215#issuecomment-72443",
    "user": "slabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072444.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-10T10:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8215#issuecomment-72444",
    "user": "abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072445.json:
```json
{
    "body": "Tested on sage 4.3.1. Doc builds fine, all tests passed and it fixes the bug. Not much more to say... Positive review !",
    "created_at": "2010-02-10T10:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8215#issuecomment-72445",
    "user": "abmasse"
}
```

Tested on sage 4.3.1. Doc builds fine, all tests passed and it fixes the bug. Not much more to say... Positive review !



---

archive/issue_comments_072446.json:
```json
{
    "body": "Changing assignee from slabbe to mpatel.",
    "created_at": "2010-02-11T14:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8215#issuecomment-72446",
    "user": "mpatel"
}
```

Changing assignee from slabbe to mpatel.



---

archive/issue_comments_072447.json:
```json
{
    "body": "Changing assignee from mpatel to slabbe.",
    "created_at": "2010-02-11T14:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8215#issuecomment-72447",
    "user": "mpatel"
}
```

Changing assignee from mpatel to slabbe.



---

archive/issue_comments_072448.json:
```json
{
    "body": "Oops!",
    "created_at": "2010-02-11T14:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8215#issuecomment-72448",
    "user": "mpatel"
}
```

Oops!



---

archive/issue_comments_072449.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8215#issuecomment-72449",
    "user": "mpatel"
}
```

Resolution: fixed
