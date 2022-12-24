# Issue 5962: Comparison in the Gap interface raises an error

archive/issues_005962.json:
```json
{
    "body": "Assignee: was\n\nCC:  wdj\n\nKeywords: gap comparison\n\nOn sage.math with sage-3.4.1, one has\n\n```\nsage: gap('DihedralGroup(8)')==gap('DihedralGroup(8)')\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n...\nRuntimeError: Gap produced error output\nError, no 1st choice method found for `LT' on 2 arguments\n\n   executing $sage1 < $sage2;\n```\n\n\nThe problem seems to be that Gap is unable to compare:\n\n```\nsage: gap('DihedralGroup(8)=DihedralGroup(8)')\nfalse\n```\n\n\nPerhaps it would make sense to try and implement a `__cmp__` method that is more sophisticated than what is done in Gap? \n\nAt least it should be made sure that the `__cmp__` method of the Gap interface does not raise an error.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5962\n\n",
    "created_at": "2009-05-02T17:31:46Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "Comparison in the Gap interface raises an error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5962",
    "user": "SimonKing"
}
```
Assignee: was

CC:  wdj

Keywords: gap comparison

On sage.math with sage-3.4.1, one has

```
sage: gap('DihedralGroup(8)')==gap('DihedralGroup(8)')
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
...
RuntimeError: Gap produced error output
Error, no 1st choice method found for `LT' on 2 arguments

   executing $sage1 < $sage2;
```


The problem seems to be that Gap is unable to compare:

```
sage: gap('DihedralGroup(8)=DihedralGroup(8)')
false
```


Perhaps it would make sense to try and implement a `__cmp__` method that is more sophisticated than what is done in Gap? 

At least it should be made sure that the `__cmp__` method of the Gap interface does not raise an error.


Issue created by migration from https://trac.sagemath.org/ticket/5962





---

archive/issue_comments_047214.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-05T12:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5962#issuecomment-47214",
    "user": "SimonKing"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_047215.json:
```json
{
    "body": "I see no way for a really satisfying solution, as long as GAP can not even compare two objects whose definitions are identical.\n\nHowever, the errors being raised by GAP when comparing elements are now caught in a try-except clause. We have, as doc tests:\n\n```\nsage: gap('DihedralGroup(8)')==gap('DihedralGroup(8)')\nFalse    # sorry, this is what GAP claims.\nsage: gap('SymmetricGroup(8)')<gap('AlternatingGroup(8)')\nTrue\nsage: gap('SymmetricGroup(8)')>gap('AlternatingGroup(8)')\nFalse\nsage: gap('SymmetricGroup(8)')==gap('SymmetricGroup(8)')\nTrue\n```\n\n\nAll but the first of these examples worked before. But the first resulted in an error, which is now fixed.",
    "created_at": "2010-07-05T12:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5962#issuecomment-47215",
    "user": "SimonKing"
}
```

I see no way for a really satisfying solution, as long as GAP can not even compare two objects whose definitions are identical.

However, the errors being raised by GAP when comparing elements are now caught in a try-except clause. We have, as doc tests:

```
sage: gap('DihedralGroup(8)')==gap('DihedralGroup(8)')
False    # sorry, this is what GAP claims.
sage: gap('SymmetricGroup(8)')<gap('AlternatingGroup(8)')
True
sage: gap('SymmetricGroup(8)')>gap('AlternatingGroup(8)')
False
sage: gap('SymmetricGroup(8)')==gap('SymmetricGroup(8)')
True
```


All but the first of these examples worked before. But the first resulted in an error, which is now fixed.



---

archive/issue_comments_047216.json:
```json
{
    "body": "I just found that this ticket needs review since 8 months. Fortunately the patch still works fine. So, any volunteer?",
    "created_at": "2011-03-08T12:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5962#issuecomment-47216",
    "user": "SimonKing"
}
```

I just found that this ticket needs review since 8 months. Fortunately the patch still works fine. So, any volunteer?



---

archive/issue_comments_047217.json:
```json
{
    "body": "Replying to [comment:2 SimonKing]:\n> I just found that this ticket needs review since 8 months. \n> Fortunately the patch still works fine. So, any volunteer?\n\nI have spring break coming up and can try to review it then if no one beats me to it.",
    "created_at": "2011-03-08T13:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5962#issuecomment-47217",
    "user": "wdj"
}
```

Replying to [comment:2 SimonKing]:
> I just found that this ticket needs review since 8 months. 
> Fortunately the patch still works fine. So, any volunteer?

I have spring break coming up and can try to review it then if no one beats me to it.



---

archive/issue_comments_047218.json:
```json
{
    "body": "This patch applies to 4.7.a1 and passes sage -testall. The patch does as claimed (adding some try-except statements) and contains the proper additional examples in the docstrings. Positive review from me.\n\nThanks Simon!",
    "created_at": "2011-03-12T22:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5962#issuecomment-47218",
    "user": "wdj"
}
```

This patch applies to 4.7.a1 and passes sage -testall. The patch does as claimed (adding some try-except statements) and contains the proper additional examples in the docstrings. Positive review from me.

Thanks Simon!



---

archive/issue_comments_047219.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-12T22:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5962#issuecomment-47219",
    "user": "wdj"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047220.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-03-27T13:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5962#issuecomment-47220",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_047221.json:
```json
{
    "body": "Please change the commit message (using hg qrefresh -e) such that the ticket number appears on the first line.",
    "created_at": "2011-03-27T13:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5962#issuecomment-47221",
    "user": "jdemeyer"
}
```

Please change the commit message (using hg qrefresh -e) such that the ticket number appears on the first line.



---

archive/issue_comments_047222.json:
```json
{
    "body": "Attachment [trac_5962_GAP__cmp__.patch](tarball://root/attachments/some-uuid/ticket5962/trac_5962_GAP__cmp__.patch) by SimonKing created at 2011-03-27 14:00:58\n\nAvoid an error being raised when comparing GAP elements. Add doctest.",
    "created_at": "2011-03-27T14:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5962#issuecomment-47222",
    "user": "SimonKing"
}
```

Attachment [trac_5962_GAP__cmp__.patch](tarball://root/attachments/some-uuid/ticket5962/trac_5962_GAP__cmp__.patch) by SimonKing created at 2011-03-27 14:00:58

Avoid an error being raised when comparing GAP elements. Add doctest.



---

archive/issue_comments_047223.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-03-27T14:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5962#issuecomment-47223",
    "user": "SimonKing"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_047224.json:
```json
{
    "body": "Replying to [comment:5 jdemeyer]:\n> Please change the commit message (using hg qrefresh -e) such that the ticket number appears on the first line. \n\nDone.",
    "created_at": "2011-03-27T14:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5962#issuecomment-47224",
    "user": "SimonKing"
}
```

Replying to [comment:5 jdemeyer]:
> Please change the commit message (using hg qrefresh -e) such that the ticket number appears on the first line. 

Done.



---

archive/issue_comments_047225.json:
```json
{
    "body": "Replying to [comment:6 SimonKing]:\n> Done.\n\nThanks!",
    "created_at": "2011-03-27T14:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5962#issuecomment-47225",
    "user": "jdemeyer"
}
```

Replying to [comment:6 SimonKing]:
> Done.

Thanks!



---

archive/issue_comments_047226.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-28T07:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5962#issuecomment-47226",
    "user": "jdemeyer"
}
```

Resolution: fixed
