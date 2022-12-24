# Issue 8446: avoid 0^0 in Selmer groups of number fields

archive/issues_008446.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  cremona\n\nIn the case of a trivial number field, such as\n\n```\nK.<a> = NumberField(polygen(QQ))\n```\n\nthe Selmer group function doesn't work, since the generator `a` of the number field is 0, and when we're constructing polynomials we use the form `coeff*a**i`. However, if `i==0`, we get an `ArithmeticError` since Sage does not have conventions for `0^0`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8446\n\n",
    "created_at": "2010-03-05T16:28:40Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "avoid 0^0 in Selmer groups of number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8446",
    "user": "rlm"
}
```
Assignee: davidloeffler

CC:  cremona

In the case of a trivial number field, such as

```
K.<a> = NumberField(polygen(QQ))
```

the Selmer group function doesn't work, since the generator `a` of the number field is 0, and when we're constructing polynomials we use the form `coeff*a**i`. However, if `i==0`, we get an `ArithmeticError` since Sage does not have conventions for `0^0`.

Issue created by migration from https://trac.sagemath.org/ticket/8446





---

archive/issue_comments_075933.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-05T16:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8446",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8446#issuecomment-75933",
    "user": "rlm"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075934.json:
```json
{
    "body": "Attachment [trac_8446.patch](tarball://root/attachments/some-uuid/ticket8446/trac_8446.patch) by rlm created at 2010-03-07 19:58:53",
    "created_at": "2010-03-07T19:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8446",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8446#issuecomment-75934",
    "user": "rlm"
}
```

Attachment [trac_8446.patch](tarball://root/attachments/some-uuid/ticket8446/trac_8446.patch) by rlm created at 2010-03-07 19:58:53



---

archive/issue_comments_075935.json:
```json
{
    "body": "Attachment [trac_8446_microfix.patch](tarball://root/attachments/some-uuid/ticket8446/trac_8446_microfix.patch) by davidloeffler created at 2010-04-20 09:38:02\n\napply over previous patch",
    "created_at": "2010-04-20T09:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8446",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8446#issuecomment-75935",
    "user": "davidloeffler"
}
```

Attachment [trac_8446_microfix.patch](tarball://root/attachments/some-uuid/ticket8446/trac_8446_microfix.patch) by davidloeffler created at 2010-04-20 09:38:02

apply over previous patch



---

archive/issue_comments_075936.json:
```json
{
    "body": "Looks fine, and all doctests pass. FWIW, I think that there should be a doctest in `_S_class_group_and_units`, not just in `selmer_group`, as that's where the problem actually occurs; and the docstring for `selmer_group` contains the literal string `\\t` so it should be a raw string. Hence the tiny second patch. I'm giving this a positive review modulo that, so please set it to positive review if you're happy with the second patch. \n\nBTW, I tried using this for some some relative extensions and discovered two separate new bugs in the process, #8721 and #8722. Neither of these actually has anything to do with this patch as such, it's preexisting brokenness. I know what's causing #8722; I'll upload a patch shortly -- any chance you could review it for me?",
    "created_at": "2010-04-20T09:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8446",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8446#issuecomment-75936",
    "user": "davidloeffler"
}
```

Looks fine, and all doctests pass. FWIW, I think that there should be a doctest in `_S_class_group_and_units`, not just in `selmer_group`, as that's where the problem actually occurs; and the docstring for `selmer_group` contains the literal string `\t` so it should be a raw string. Hence the tiny second patch. I'm giving this a positive review modulo that, so please set it to positive review if you're happy with the second patch. 

BTW, I tried using this for some some relative extensions and discovered two separate new bugs in the process, #8721 and #8722. Neither of these actually has anything to do with this patch as such, it's preexisting brokenness. I know what's causing #8722; I'll upload a patch shortly -- any chance you could review it for me?



---

archive/issue_comments_075937.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-20T21:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8446",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8446#issuecomment-75937",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075938.json:
```json
{
    "body": "Re #8722 - I will be happy to review it eventually, but no guarantees at this very moment, since I'm finishing up my dissertation and preparing to defend it next month.",
    "created_at": "2010-04-20T21:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8446",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8446#issuecomment-75938",
    "user": "rlm"
}
```

Re #8722 - I will be happy to review it eventually, but no guarantees at this very moment, since I'm finishing up my dissertation and preparing to defend it next month.



---

archive/issue_comments_075939.json:
```json
{
    "body": "Understood -- hope it goes well!",
    "created_at": "2010-04-20T22:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8446",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8446#issuecomment-75939",
    "user": "davidloeffler"
}
```

Understood -- hope it goes well!



---

archive/issue_comments_075940.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-23T17:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8446",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8446#issuecomment-75940",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_075941.json:
```json
{
    "body": "Merged into 4.4.alpha2:\n- trac_8446.patch\n- trac_8446_microfix.patch",
    "created_at": "2010-04-23T17:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8446",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8446#issuecomment-75941",
    "user": "jhpalmieri"
}
```

Merged into 4.4.alpha2:
- trac_8446.patch
- trac_8446_microfix.patch
