# Issue 9336: Improve doctest coverage for sage/rings/number_field

archive/issues_009336.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  cremona\n\nKeywords: doctest\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9336\n\n",
    "created_at": "2010-06-25T15:10:10Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "title": "Improve doctest coverage for sage/rings/number_field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9336",
    "user": "davidloeffler"
}
```
Assignee: davidloeffler

CC:  cremona

Keywords: doctest



Issue created by migration from https://trac.sagemath.org/ticket/9336





---

archive/issue_comments_088145.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-25T15:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9336#issuecomment-88145",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088146.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-26T06:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9336#issuecomment-88146",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088147.json:
```json
{
    "body": "Good job!  Patch applies to 4.4.4 and tests pass and docs build fine.\n\nAfter this the number_fields directory scores as follows:\n\n```\n\nSCORE sage/rings/number_field//unit_group.py: 100% (15 of 15)\nSCORE sage/rings/number_field//number_field_element.pyx: 81% (91 of 111)\nSCORE sage/rings/number_field//totallyreal.pyx: 100% (4 of 4)\nSCORE sage/rings/number_field//number_field_base.pyx: 72% (8 of 11)\nSCORE sage/rings/number_field//order.py: 100% (62 of 62)\nSCORE sage/rings/number_field//number_field_element_quadratic.pyx: 95% (42 of 44)\nSCORE sage/rings/number_field//number_field.py: 100% (183 of 183)\nSCORE sage/rings/number_field//number_field_ideal.py: 92% (72 of 78)\nSCORE sage/rings/number_field//totallyreal_dsage.py: 13% (2 of 15)\nSCORE sage/rings/number_field//maps.py: 100% (23 of 23)\nSCORE sage/rings/number_field//number_field_rel.py: 91% (62 of 68)\nSCORE sage/rings/number_field//totallyreal_data.pyx: 100% (7 of 7)\nSCORE sage/rings/number_field//small_primes_of_degree_one.py: 100% (4 of 4)\nSCORE sage/rings/number_field//galois_group.py: 100% (29 of 29)\nSCORE sage/rings/number_field//number_field_ideal_rel.py: 78% (22 of 28)\nSCORE sage/rings/number_field//totallyreal_rel.py: 60% (3 of 5)\nSCORE sage/rings/number_field//morphism.py: 100% (22 of 22)\nSCORE sage/rings/number_field//class_group.py: 72% (13 of 18)\nSCORE sage/rings/number_field//number_field_morphisms.pyx: 100% (13 of 13)\nSCORE sage/rings/number_field//totallyreal_phc.py: 100% (2 of 2)\n```\n",
    "created_at": "2010-06-26T06:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9336#issuecomment-88147",
    "user": "cremona"
}
```

Good job!  Patch applies to 4.4.4 and tests pass and docs build fine.

After this the number_fields directory scores as follows:

```

SCORE sage/rings/number_field//unit_group.py: 100% (15 of 15)
SCORE sage/rings/number_field//number_field_element.pyx: 81% (91 of 111)
SCORE sage/rings/number_field//totallyreal.pyx: 100% (4 of 4)
SCORE sage/rings/number_field//number_field_base.pyx: 72% (8 of 11)
SCORE sage/rings/number_field//order.py: 100% (62 of 62)
SCORE sage/rings/number_field//number_field_element_quadratic.pyx: 95% (42 of 44)
SCORE sage/rings/number_field//number_field.py: 100% (183 of 183)
SCORE sage/rings/number_field//number_field_ideal.py: 92% (72 of 78)
SCORE sage/rings/number_field//totallyreal_dsage.py: 13% (2 of 15)
SCORE sage/rings/number_field//maps.py: 100% (23 of 23)
SCORE sage/rings/number_field//number_field_rel.py: 91% (62 of 68)
SCORE sage/rings/number_field//totallyreal_data.pyx: 100% (7 of 7)
SCORE sage/rings/number_field//small_primes_of_degree_one.py: 100% (4 of 4)
SCORE sage/rings/number_field//galois_group.py: 100% (29 of 29)
SCORE sage/rings/number_field//number_field_ideal_rel.py: 78% (22 of 28)
SCORE sage/rings/number_field//totallyreal_rel.py: 60% (3 of 5)
SCORE sage/rings/number_field//morphism.py: 100% (22 of 22)
SCORE sage/rings/number_field//class_group.py: 72% (13 of 18)
SCORE sage/rings/number_field//number_field_morphisms.pyx: 100% (13 of 13)
SCORE sage/rings/number_field//totallyreal_phc.py: 100% (2 of 2)
```




---

archive/issue_comments_088148.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-27T19:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9336#issuecomment-88148",
    "user": "fwclarke"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_088149.json:
```json
{
    "body": "Just one little niggle: according to the developer's guide, code like\n\n```\n        try: \n            return self.list()[0] \n        except: \n            raise ValueError, \"Set is empty\"\n```\n\n(lines 91 to 94 in the patched morphism.py) should be avoided.  Better would be\n\n```\n        try: \n            return self[0] \n        except IndexError: \n            raise ValueError, \"Set is empty\"\n```\n",
    "created_at": "2010-06-27T19:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9336#issuecomment-88149",
    "user": "fwclarke"
}
```

Just one little niggle: according to the developer's guide, code like

```
        try: 
            return self.list()[0] 
        except: 
            raise ValueError, "Set is empty"
```

(lines 91 to 94 in the patched morphism.py) should be avoided.  Better would be

```
        try: 
            return self[0] 
        except IndexError: 
            raise ValueError, "Set is empty"
```




---

archive/issue_comments_088150.json:
```json
{
    "body": "OK, I agree that would be better.",
    "created_at": "2010-06-28T04:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9336#issuecomment-88150",
    "user": "cremona"
}
```

OK, I agree that would be better.



---

archive/issue_comments_088151.json:
```json
{
    "body": "Attachment\n\npatch against 4.4.4",
    "created_at": "2010-06-28T08:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9336#issuecomment-88151",
    "user": "davidloeffler"
}
```

Attachment

patch against 4.4.4



---

archive/issue_comments_088152.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-28T08:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9336#issuecomment-88152",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088153.json:
```json
{
    "body": "Here's a new patch, which explicitly checks whether the length of the list is 0 rather than using try/except.",
    "created_at": "2010-06-28T08:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9336#issuecomment-88153",
    "user": "davidloeffler"
}
```

Here's a new patch, which explicitly checks whether the length of the list is 0 rather than using try/except.



---

archive/issue_comments_088154.json:
```json
{
    "body": "Replying to [comment:6 davidloeffler]:\n> Here's a new patch ...\n\nThat works fine, so back to positive review.",
    "created_at": "2010-06-28T17:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9336#issuecomment-88154",
    "user": "fwclarke"
}
```

Replying to [comment:6 davidloeffler]:
> Here's a new patch ...

That works fine, so back to positive review.



---

archive/issue_comments_088155.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-28T17:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9336#issuecomment-88155",
    "user": "fwclarke"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088156.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9336#issuecomment-88156",
    "user": "mpatel"
}
```

Resolution: fixed
