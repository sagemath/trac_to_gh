# Issue 9371: Implement E.two_torsion_rank() over number fields

archive/issues_009371.json:
```json
{
    "body": "Assignee: weigandt\n\nCC:  @JohnCremona\n\nKeywords: elliptic curves, two torsion rank\n\nThe function E.two_torsion_rank() can easily be made to work over number fields. The current implementation over QQ calls E.torsion_subgroup() and makes nontrivial use of Mazur's torsion theorem. This should be more efficient and more general by considering the 2-division polynomial.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9371\n\n",
    "closed_at": "2011-04-12T08:04:54Z",
    "created_at": "2010-06-29T04:12:52Z",
    "labels": [
        "component: elliptic curves"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "Implement E.two_torsion_rank() over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9371",
    "user": "https://trac.sagemath.org/admin/accounts/users/weigandt"
}
```
Assignee: weigandt

CC:  @JohnCremona

Keywords: elliptic curves, two torsion rank

The function E.two_torsion_rank() can easily be made to work over number fields. The current implementation over QQ calls E.torsion_subgroup() and makes nontrivial use of Mazur's torsion theorem. This should be more efficient and more general by considering the 2-division polynomial.

Issue created by migration from https://trac.sagemath.org/ticket/9371





---

archive/issue_comments_088903.json:
```json
{
    "body": "Extend E.two_torsion_rank() method to number fields. Applies to 4.4.4",
    "created_at": "2010-07-01T18:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9371#issuecomment-88903",
    "user": "https://trac.sagemath.org/admin/accounts/users/weigandt"
}
```

Extend E.two_torsion_rank() method to number fields. Applies to 4.4.4



---

archive/issue_comments_088904.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-01T18:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9371#issuecomment-88904",
    "user": "https://trac.sagemath.org/admin/accounts/users/weigandt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088905.json:
```json
{
    "body": "Attachment [trac_9371_two_torsion_rank.patch](tarball://root/attachments/some-uuid/ticket9371/trac_9371_two_torsion_rank.patch) by weigandt created at 2010-07-01 18:37:27",
    "created_at": "2010-07-01T18:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9371#issuecomment-88905",
    "user": "https://trac.sagemath.org/admin/accounts/users/weigandt"
}
```

Attachment [trac_9371_two_torsion_rank.patch](tarball://root/attachments/some-uuid/ticket9371/trac_9371_two_torsion_rank.patch) by weigandt created at 2010-07-01 18:37:27



---

archive/issue_comments_088906.json:
```json
{
    "body": "Looks good: a better method and more general.   However:  why not move the function all the way up to ell_field?  There's no reason at all why the same code would not work over any field of char. not 2, and even in char. 2 (where the result is at most 0 or 1 for supersingular/ordinary curves, but so what).\n\nIf you do that, add extra doctests over (say) finite fields.\nWhile you are at it, one thing about the docstring could be improved:  the short description should fit on one line, so cut it after E(K), and put the rest into a separate ALGORITHM block.\n \n\"Needs work\" sounds negative, so let me elaborate: this is good and with a tiny amount of work would be very good!",
    "created_at": "2010-07-05T16:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9371#issuecomment-88906",
    "user": "https://github.com/JohnCremona"
}
```

Looks good: a better method and more general.   However:  why not move the function all the way up to ell_field?  There's no reason at all why the same code would not work over any field of char. not 2, and even in char. 2 (where the result is at most 0 or 1 for supersingular/ordinary curves, but so what).

If you do that, add extra doctests over (say) finite fields.
While you are at it, one thing about the docstring could be improved:  the short description should fit on one line, so cut it after E(K), and put the rest into a separate ALGORITHM block.
 
"Needs work" sounds negative, so let me elaborate: this is good and with a tiny amount of work would be very good!



---

archive/issue_comments_088907.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-05T16:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9371#issuecomment-88907",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_088908.json:
```json
{
    "body": "new patch, replaced old one, applies to 4.6.2",
    "created_at": "2011-03-23T01:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9371#issuecomment-88908",
    "user": "https://trac.sagemath.org/admin/accounts/users/weigandt"
}
```

new patch, replaced old one, applies to 4.6.2



---

archive/issue_comments_088909.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-23T01:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9371#issuecomment-88909",
    "user": "https://trac.sagemath.org/admin/accounts/users/weigandt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088910.json:
```json
{
    "body": "Attachment [trac_9371_field_two_torsion.patch](tarball://root/attachments/some-uuid/ticket9371/trac_9371_field_two_torsion.patch) by weigandt created at 2011-03-23 01:42:01",
    "created_at": "2011-03-23T01:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9371#issuecomment-88910",
    "user": "https://trac.sagemath.org/admin/accounts/users/weigandt"
}
```

Attachment [trac_9371_field_two_torsion.patch](tarball://root/attachments/some-uuid/ticket9371/trac_9371_field_two_torsion.patch) by weigandt created at 2011-03-23 01:42:01



---

archive/issue_comments_088911.json:
```json
{
    "body": "I think there should be at least 2 more different examples like you had before. Either you can add then I can review or I can add and we will need to find a new reviewer",
    "created_at": "2011-03-23T16:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9371#issuecomment-88911",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

I think there should be at least 2 more different examples like you had before. Either you can add then I can review or I can add and we will need to find a new reviewer



---

archive/issue_comments_088912.json:
```json
{
    "body": "added documentation, replaces previous patch",
    "created_at": "2011-03-23T17:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9371#issuecomment-88912",
    "user": "https://github.com/adeines"
}
```

added documentation, replaces previous patch



---

archive/issue_comments_088913.json:
```json
{
    "body": "Attachment [trac_9371_field_two_torsion.2.patch](tarball://root/attachments/some-uuid/ticket9371/trac_9371_field_two_torsion.2.patch) by gagansekhon created at 2011-03-23 22:06:25\n\nit initially failed sage/interface/r.py, but once I ran it separately and it worked.",
    "created_at": "2011-03-23T22:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9371#issuecomment-88913",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Attachment [trac_9371_field_two_torsion.2.patch](tarball://root/attachments/some-uuid/ticket9371/trac_9371_field_two_torsion.2.patch) by gagansekhon created at 2011-03-23 22:06:25

it initially failed sage/interface/r.py, but once I ran it separately and it worked.



---

archive/issue_comments_088914.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-23T22:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9371#issuecomment-88914",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088915.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-12T08:04:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9371#issuecomment-88915",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_023113.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-12T08:04:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9371",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9371#event-23113"
}
```
