# Issue 9813: Improve creation time for p-adic elements

archive/issues_009813.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nKeywords: padic, p-adic\n\nI've implemented coercion morphisms from ZZ and QQ to Zp and Qp.  This drops item creation time from about 20 microseconds to about 1 microsecond on my machine.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9814\n\n",
    "created_at": "2010-08-27T05:29:00Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Improve creation time for p-adic elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9813",
    "user": "roed"
}
```
Assignee: AlexGhitza

Keywords: padic, p-adic

I've implemented coercion morphisms from ZZ and QQ to Zp and Qp.  This drops item creation time from about 20 microseconds to about 1 microsecond on my machine.

Issue created by migration from https://trac.sagemath.org/ticket/9814





---

archive/issue_comments_096773.json:
```json
{
    "body": "Attachment [trac-9814.patch](tarball://root/attachments/some-uuid/ticket9814/trac-9814.patch) by roed created at 2010-08-27 05:32:31\n\nSee the thread http://groups.google.com/group/sage-devel/browse_thread/thread/612ea8f2f9d06e37?pli=1",
    "created_at": "2010-08-27T05:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96773",
    "user": "roed"
}
```

Attachment [trac-9814.patch](tarball://root/attachments/some-uuid/ticket9814/trac-9814.patch) by roed created at 2010-08-27 05:32:31

See the thread http://groups.google.com/group/sage-devel/browse_thread/thread/612ea8f2f9d06e37?pli=1



---

archive/issue_comments_096774.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-27T05:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96774",
    "user": "roed"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096775.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-28T02:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96775",
    "user": "dmharvey"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096776.json:
```json
{
    "body": "seems to work as advertised, but I get lots of doctest failures with -testall, typical example is like this:\n\n\n```\nFile \"/Users/david/sage-4.5.2/devel/sage/sage/rings/padics/padic_generic_element.pyx\", line 1002:\n    sage: R3(-1).square_root() == R3.teichmuller(2) or R3(-1).square_root() == R3.teichmuller(3)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/david/sage-4.5.2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/david/sage-4.5.2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/david/sage-4.5.2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_24[33]>\", line 1, in <module>\n        R3(-Integer(1)).square_root() == R3.teichmuller(Integer(2)) or R3(-Integer(1)).square_root() == R3.teichmuller(Integer(3))###line 1002:\n    sage: R3(-1).square_root() == R3.teichmuller(2) or R3(-1).square_root() == R3.teichmuller(3)\n      File \"/Users/david/sage-4.5.2/local/lib/python/site-packages/sage/rings/padics/padic_generic.py\", line 377, in teichmuller\n        ans = self(x, prec)\n      File \"parent.pyx\", line 861, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6427)\n      File \"map.pyx\", line 478, in sage.categories.map.Map._call_with_args (sage/categories/map.c:3666)\n    NotImplementedError: _call_with_args not overridden to accept arguments for <type 'sage.rings.padics.padic_base_coercion.pAdicCoercion_ZZ_CR'>\n```\n",
    "created_at": "2010-08-28T02:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96776",
    "user": "dmharvey"
}
```

seems to work as advertised, but I get lots of doctest failures with -testall, typical example is like this:


```
File "/Users/david/sage-4.5.2/devel/sage/sage/rings/padics/padic_generic_element.pyx", line 1002:
    sage: R3(-1).square_root() == R3.teichmuller(2) or R3(-1).square_root() == R3.teichmuller(3)
Exception raised:
    Traceback (most recent call last):
      File "/Users/david/sage-4.5.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/david/sage-4.5.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/david/sage-4.5.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[33]>", line 1, in <module>
        R3(-Integer(1)).square_root() == R3.teichmuller(Integer(2)) or R3(-Integer(1)).square_root() == R3.teichmuller(Integer(3))###line 1002:
    sage: R3(-1).square_root() == R3.teichmuller(2) or R3(-1).square_root() == R3.teichmuller(3)
      File "/Users/david/sage-4.5.2/local/lib/python/site-packages/sage/rings/padics/padic_generic.py", line 377, in teichmuller
        ans = self(x, prec)
      File "parent.pyx", line 861, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6427)
      File "map.pyx", line 478, in sage.categories.map.Map._call_with_args (sage/categories/map.c:3666)
    NotImplementedError: _call_with_args not overridden to accept arguments for <type 'sage.rings.padics.padic_base_coercion.pAdicCoercion_ZZ_CR'>
```




---

archive/issue_comments_096777.json:
```json
{
    "body": "Changing component from basic arithmetic to padics.",
    "created_at": "2010-09-02T11:14:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96777",
    "user": "AlexGhitza"
}
```

Changing component from basic arithmetic to padics.



---

archive/issue_comments_096778.json:
```json
{
    "body": "Changing keywords from \"padic, p-adic\" to \"coercion\".",
    "created_at": "2010-09-02T11:14:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96778",
    "user": "AlexGhitza"
}
```

Changing keywords from "padic, p-adic" to "coercion".



---

archive/issue_comments_096779.json:
```json
{
    "body": "Replaces first patch.",
    "created_at": "2010-09-18T21:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96779",
    "user": "roed"
}
```

Replaces first patch.



---

archive/issue_comments_096780.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-18T21:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96780",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096781.json:
```json
{
    "body": "Attachment [trac_9814-2.patch](tarball://root/attachments/some-uuid/ticket9814/trac_9814-2.patch) by roed created at 2010-09-18 21:29:25\n\nWell, that was more work than I expected, but it also fixes some problems with non-uniqueness of p-adic parents.",
    "created_at": "2010-09-18T21:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96781",
    "user": "roed"
}
```

Attachment [trac_9814-2.patch](tarball://root/attachments/some-uuid/ticket9814/trac_9814-2.patch) by roed created at 2010-09-18 21:29:25

Well, that was more work than I expected, but it also fixes some problems with non-uniqueness of p-adic parents.



---

archive/issue_comments_096782.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T01:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96782",
    "user": "dmharvey"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096783.json:
```json
{
    "body": "Excellent. You've restored my faith in Sage :-)",
    "created_at": "2010-09-22T01:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96783",
    "user": "dmharvey"
}
```

Excellent. You've restored my faith in Sage :-)



---

archive/issue_comments_096784.json:
```json
{
    "body": "Good.  The series of patches in 7883 -> 8333 -> 8334 plus a bit of other additional work will fix most of your object creation problems with IntegerMods as well.",
    "created_at": "2010-09-22T01:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96784",
    "user": "roed"
}
```

Good.  The series of patches in 7883 -> 8333 -> 8334 plus a bit of other additional work will fix most of your object creation problems with IntegerMods as well.



---

archive/issue_comments_096785.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-28T08:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96785",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_096786.json:
```json
{
    "body": "Could someone prepend the ticket number to the commit string's first line and restore the positive review?  The first line should also be < 80 characters long, so that `hg log` messages are compact.",
    "created_at": "2010-09-28T08:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96786",
    "user": "mpatel"
}
```

Could someone prepend the ticket number to the commit string's first line and restore the positive review?  The first line should also be < 80 characters long, so that `hg log` messages are compact.



---

archive/issue_comments_096787.json:
```json
{
    "body": "Attachment [trac_9814-3.patch](tarball://root/attachments/some-uuid/ticket9814/trac_9814-3.patch) by davidloeffler created at 2010-09-28 08:21:21\n\nCommit message fixed. Apply only this patch.",
    "created_at": "2010-09-28T08:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96787",
    "user": "davidloeffler"
}
```

Attachment [trac_9814-3.patch](tarball://root/attachments/some-uuid/ticket9814/trac_9814-3.patch) by davidloeffler created at 2010-09-28 08:21:21

Commit message fixed. Apply only this patch.



---

archive/issue_comments_096788.json:
```json
{
    "body": "Done.",
    "created_at": "2010-09-28T08:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96788",
    "user": "davidloeffler"
}
```

Done.



---

archive/issue_comments_096789.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-28T08:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96789",
    "user": "davidloeffler"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_096790.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T10:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9813#issuecomment-96790",
    "user": "mpatel"
}
```

Resolution: fixed
