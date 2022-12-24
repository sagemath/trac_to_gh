# Issue 8347: Test the positivity of the real part of a number field element

archive/issues_008347.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  sage-combinat\n\nKeywords: test, positivity, real\n\ntest if an element of a number field is positive or negative. \n\nEspecially for real element of a CyclotomicField, we need this test for theory representation of complex reflection groups.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8347\n\n",
    "created_at": "2010-02-24T15:40:31Z",
    "labels": [
        "number fields",
        "critical",
        "enhancement"
    ],
    "title": "Test the positivity of the real part of a number field element",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8347",
    "user": "nborie"
}
```
Assignee: davidloeffler

CC:  sage-combinat

Keywords: test, positivity, real

test if an element of a number field is positive or negative. 

Especially for real element of a CyclotomicField, we need this test for theory representation of complex reflection groups.

Issue created by migration from https://trac.sagemath.org/ticket/8347





---

archive/issue_comments_074519.json:
```json
{
    "body": "Attachment [test_positivity_cyclotomic_field-nb.patch](tarball://root/attachments/some-uuid/ticket8347/test_positivity_cyclotomic_field-nb.patch) by nborie created at 2010-02-24 15:42:52",
    "created_at": "2010-02-24T15:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74519",
    "user": "nborie"
}
```

Attachment [test_positivity_cyclotomic_field-nb.patch](tarball://root/attachments/some-uuid/ticket8347/test_positivity_cyclotomic_field-nb.patch) by nborie created at 2010-02-24 15:42:52



---

archive/issue_comments_074520.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-24T15:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74520",
    "user": "nborie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074521.json:
```json
{
    "body": "I am clearly not a speciallist for this kind of job. There is two propositions to solve this problem. The second one comes after some remarks from some guys at Sage Days 20....",
    "created_at": "2010-02-24T16:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74521",
    "user": "nborie"
}
```

I am clearly not a speciallist for this kind of job. There is two propositions to solve this problem. The second one comes after some remarks from some guys at Sage Days 20....



---

archive/issue_comments_074522.json:
```json
{
    "body": "Attachment [test_positivity_cyclotomic_field_2-nb.patch](tarball://root/attachments/some-uuid/ticket8347/test_positivity_cyclotomic_field_2-nb.patch) by nborie created at 2010-02-24 16:20:47",
    "created_at": "2010-02-24T16:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74522",
    "user": "nborie"
}
```

Attachment [test_positivity_cyclotomic_field_2-nb.patch](tarball://root/attachments/some-uuid/ticket8347/test_positivity_cyclotomic_field_2-nb.patch) by nborie created at 2010-02-24 16:20:47



---

archive/issue_comments_074523.json:
```json
{
    "body": "Here comes a third version which say True if an algebraic complex number is a real positive and False otherwise. (Another suggest from another people....)\n\nFeel free to give some advises about :\n- the name of this method\n- the test (usable not only in Coxeter Group theory)\n- the way to implement this\n- ....",
    "created_at": "2010-02-24T20:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74523",
    "user": "nborie"
}
```

Here comes a third version which say True if an algebraic complex number is a real positive and False otherwise. (Another suggest from another people....)

Feel free to give some advises about :
- the name of this method
- the test (usable not only in Coxeter Group theory)
- the way to implement this
- ....



---

archive/issue_comments_074524.json:
```json
{
    "body": "should one test all 3 patches, or only the last one?",
    "created_at": "2010-02-25T14:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74524",
    "user": "zimmerma"
}
```

should one test all 3 patches, or only the last one?



---

archive/issue_comments_074525.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-02-25T14:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74525",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_074526.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-25T15:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74526",
    "user": "nborie"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_074527.json:
```json
{
    "body": "Hi Paul,\n\nThis is a question of design. As Nicolas Thiery and Jean Michel got a look on the two first propositions, they ask me to do the third one. You can just look the two first and confirm the disign was not the better... But if you want to test, just test the last one which seems to be the better solution (No error and just True/Flase answering...).\n\nSo, just review the third patch.\n\nThanks for all.",
    "created_at": "2010-02-25T15:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74527",
    "user": "nborie"
}
```

Hi Paul,

This is a question of design. As Nicolas Thiery and Jean Michel got a look on the two first propositions, they ask me to do the third one. You can just look the two first and confirm the disign was not the better... But if you want to test, just test the last one which seems to be the better solution (No error and just True/Flase answering...).

So, just review the third patch.

Thanks for all.



---

archive/issue_comments_074528.json:
```json
{
    "body": "I've reviewed the 3rd patch.\n\nI noticed a few typos: `dependant` should be `dependent`, `embendding` should be\n`embedding`.\n\nAlso I don't understand why `long time` since the tests are fast.\n\nFinally a test is missing with a `None` result (apparently the last test should return None\ninstead of False).",
    "created_at": "2010-02-25T18:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74528",
    "user": "zimmerma"
}
```

I've reviewed the 3rd patch.

I noticed a few typos: `dependant` should be `dependent`, `embendding` should be
`embedding`.

Also I don't understand why `long time` since the tests are fast.

Finally a test is missing with a `None` result (apparently the last test should return None
instead of False).



---

archive/issue_comments_074529.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-25T18:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74529",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074530.json:
```json
{
    "body": "I removed the # long time guards. I changed the description of the ticket and I changed the doc of the function (It now does what it is described in the doc... (I hope so...)). I configured my emacs with aspell (It is really time to do it!!!!!). I am very very very sorry to have presented a so much horrible work on the trac. Feel free to scold me very loudly! I hope you didn't lose too much time on that...",
    "created_at": "2010-02-26T08:51:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74530",
    "user": "nborie"
}
```

I removed the # long time guards. I changed the description of the ticket and I changed the doc of the function (It now does what it is described in the doc... (I hope so...)). I configured my emacs with aspell (It is really time to do it!!!!!). I am very very very sorry to have presented a so much horrible work on the trac. Feel free to scold me very loudly! I hope you didn't lose too much time on that...



---

archive/issue_comments_074531.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-26T08:51:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74531",
    "user": "nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074532.json:
```json
{
    "body": "Small documentation suggestion:\n\n- First state what the function does mathematically\n- Then give the algorithm, and mention that the result is guaranteed to be correct, and that this is achieved by increasing the approximation order until the decision can be taken. It would be nice to include a complexity result (given the order of a root, and the size of the rational coefficient, one should be able to give an upper bound on the required approximation order)\n\nThanks for your useful work on this!",
    "created_at": "2010-02-26T13:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74532",
    "user": "nthiery"
}
```

Small documentation suggestion:

- First state what the function does mathematically
- Then give the algorithm, and mention that the result is guaranteed to be correct, and that this is achieved by increasing the approximation order until the decision can be taken. It would be nice to include a complexity result (given the order of a root, and the size of the rational coefficient, one should be able to give an upper bound on the required approximation order)

Thanks for your useful work on this!



---

archive/issue_comments_074533.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-28T19:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74533",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074534.json:
```json
{
    "body": "another problem:\n\n```\nsage: K.<a> = QuadraticField(-3)\nsage: (a-a).is_real_positive() \n...\nTypeError: Unable to convert number to real interval.\n```\n\n\nPaul",
    "created_at": "2010-02-28T19:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74534",
    "user": "zimmerma"
}
```

another problem:

```
sage: K.<a> = QuadraticField(-3)
sage: (a-a).is_real_positive() 
...
TypeError: Unable to convert number to real interval.
```


Paul



---

archive/issue_comments_074535.json:
```json
{
    "body": "Attachment [test_positivity_cyclotomic_field_3-nb.patch](tarball://root/attachments/some-uuid/ticket8347/test_positivity_cyclotomic_field_3-nb.patch) by nborie created at 2010-02-28 20:11:08",
    "created_at": "2010-02-28T20:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74535",
    "user": "nborie"
}
```

Attachment [test_positivity_cyclotomic_field_3-nb.patch](tarball://root/attachments/some-uuid/ticket8347/test_positivity_cyclotomic_field_3-nb.patch) by nborie created at 2010-02-28 20:11:08



---

archive/issue_comments_074536.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-28T20:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74536",
    "user": "nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074537.json:
```json
{
    "body": "I tryed to improve the doc according the advises of Nicolas. I also fix the problem that Paul pointed.",
    "created_at": "2010-02-28T20:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74537",
    "user": "nborie"
}
```

I tryed to improve the doc according the advises of Nicolas. I also fix the problem that Paul pointed.



---

archive/issue_comments_074538.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-01T17:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74538",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074539.json:
```json
{
    "body": "I am ok with the new patch.\n\nFor the release manager: apply only `test_positivity_cyclotomic_field_3-nb.patch`.",
    "created_at": "2010-03-01T17:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74539",
    "user": "zimmerma"
}
```

I am ok with the new patch.

For the release manager: apply only `test_positivity_cyclotomic_field_3-nb.patch`.



---

archive/issue_comments_074540.json:
```json
{
    "body": "Thanks a lot for your patience and multireview.",
    "created_at": "2010-03-01T17:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74540",
    "user": "nborie"
}
```

Thanks a lot for your patience and multireview.



---

archive/issue_comments_074541.json:
```json
{
    "body": "Merged [test_positivity_cyclotomic_field_3-nb.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8347/test_positivity_cyclotomic_field_3-nb.patch).\n\n\n\nNicolas: you should put a sensible commit message in your patch, together with the ticket number.",
    "created_at": "2010-03-03T14:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74541",
    "user": "mvngu"
}
```

Merged [test_positivity_cyclotomic_field_3-nb.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8347/test_positivity_cyclotomic_field_3-nb.patch).



Nicolas: you should put a sensible commit message in your patch, together with the ticket number.



---

archive/issue_comments_074542.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8347#issuecomment-74542",
    "user": "mvngu"
}
```

Resolution: fixed
