# Issue 8915: improve documentation on combinat.dyck_words

archive/issues_008915.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  sage-combinat\n\nKeywords: dyck_words\n\ndocumentation in several functions are missing description\n\n```\n    def associated_parenthesis(self, pos):\n        \"\"\"\n        EXAMPLES::\n        \n            sage: DyckWord([1, 0]).associated_parenthesis(0)\n            1\n```\n\n\nWorking on patch\n\nIssue created by migration from https://trac.sagemath.org/ticket/8915\n\n",
    "created_at": "2010-05-07T16:08:33Z",
    "labels": [
        "documentation",
        "trivial",
        "bug"
    ],
    "title": "improve documentation on combinat.dyck_words",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8915",
    "user": "zabrocki"
}
```
Assignee: mvngu

CC:  sage-combinat

Keywords: dyck_words

documentation in several functions are missing description

```
    def associated_parenthesis(self, pos):
        """
        EXAMPLES::
        
            sage: DyckWord([1, 0]).associated_parenthesis(0)
            1
```


Working on patch

Issue created by migration from https://trac.sagemath.org/ticket/8915





---

archive/issue_comments_082116.json:
```json
{
    "body": "Attachment [trac8915.patch](tarball://root/attachments/some-uuid/ticket8915/trac8915.patch) by zabrocki created at 2010-05-08 17:27:15\n\nDocumentation changes to combinat/dyck_word.py",
    "created_at": "2010-05-08T17:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8915#issuecomment-82116",
    "user": "zabrocki"
}
```

Attachment [trac8915.patch](tarball://root/attachments/some-uuid/ticket8915/trac8915.patch) by zabrocki created at 2010-05-08 17:27:15

Documentation changes to combinat/dyck_word.py



---

archive/issue_comments_082117.json:
```json
{
    "body": "Changing assignee from mvngu to zabrocki.",
    "created_at": "2010-05-08T17:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8915#issuecomment-82117",
    "user": "zabrocki"
}
```

Changing assignee from mvngu to zabrocki.



---

archive/issue_comments_082118.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-08T17:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8915#issuecomment-82118",
    "user": "zabrocki"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082119.json:
```json
{
    "body": "Attachment [trac_8915-reviewer.patch](tarball://root/attachments/some-uuid/ticket8915/trac_8915-reviewer.patch) by mvngu created at 2010-05-09 00:58:53",
    "created_at": "2010-05-09T00:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8915#issuecomment-82119",
    "user": "mvngu"
}
```

Attachment [trac_8915-reviewer.patch](tarball://root/attachments/some-uuid/ticket8915/trac_8915-reviewer.patch) by mvngu created at 2010-05-09 00:58:53



---

archive/issue_comments_082120.json:
```json
{
    "body": "Attachment [trac8915.2.patch](tarball://root/attachments/some-uuid/ticket8915/trac8915.2.patch) by mvngu created at 2010-05-09 01:03:39\n\nThe patch [trac8915.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8915/trac8915.2.patch) is the same as [trac8915.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8915/trac8915.patch), but with the ticket number and a commit message. Changes proposed by the reviewer patch:\n\n* Explain the input wherever possible.\n* Don't go over 79 characters per line wherever possible. This is in accordance with the style guide [PEP 008](http://www.python.org/dev/peps/pep-0008/).\n* Cross reference functions wherever possible.\n* Some typo fixes.\n \nSo only my patch needs review by anyone but me. If my reviewer patch is OK, then the whole ticket is good to go.",
    "created_at": "2010-05-09T01:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8915#issuecomment-82120",
    "user": "mvngu"
}
```

Attachment [trac8915.2.patch](tarball://root/attachments/some-uuid/ticket8915/trac8915.2.patch) by mvngu created at 2010-05-09 01:03:39

The patch [trac8915.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8915/trac8915.2.patch) is the same as [trac8915.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8915/trac8915.patch), but with the ticket number and a commit message. Changes proposed by the reviewer patch:

* Explain the input wherever possible.
* Don't go over 79 characters per line wherever possible. This is in accordance with the style guide [PEP 008](http://www.python.org/dev/peps/pep-0008/).
* Cross reference functions wherever possible.
* Some typo fixes.
 
So only my patch needs review by anyone but me. If my reviewer patch is OK, then the whole ticket is good to go.



---

archive/issue_comments_082121.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-13T13:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8915#issuecomment-82121",
    "user": "slabbe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082122.json:
```json
{
    "body": "All tests still passed in `dyck_word.py`. Documentation coverage is still 100%. Documentation builds fine without syntax warning. ...and the documentation of the file was enhanced.\n\nPositive review.",
    "created_at": "2010-05-13T13:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8915#issuecomment-82122",
    "user": "slabbe"
}
```

All tests still passed in `dyck_word.py`. Documentation coverage is still 100%. Documentation builds fine without syntax warning. ...and the documentation of the file was enhanced.

Positive review.



---

archive/issue_comments_082123.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-17T06:49:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8915#issuecomment-82123",
    "user": "mvngu"
}
```

Resolution: fixed
