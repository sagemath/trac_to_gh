# Issue 6322: optional doctest failure -- another mistake in bordeaux lectures

archive/issues_006322.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t -long --optional devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/bordeaux_2008/nf_galois_groups.rst\", line 92:\n    sage: K.galois_group(type=\"gap\", algorithm='magma')    # optional\nExpected:\n    verbose...\n    Galois group Transitive group number 2 of degree 3 of\n    the Number Field in a with defining polynomial x^3 - 2\nGot:\n    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 - 2\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_2\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_nf_galois_groups.py\n\t [12.4 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6322\n\n",
    "created_at": "2009-06-16T14:52:53Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "title": "optional doctest failure -- another mistake in bordeaux lectures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6322",
    "user": "was"
}
```
Assignee: tbd


```
sage -t -long --optional devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/bordeaux_2008/nf_galois_groups.rst", line 92:
    sage: K.galois_group(type="gap", algorithm='magma')    # optional
Expected:
    verbose...
    Galois group Transitive group number 2 of degree 3 of
    the Number Field in a with defining polynomial x^3 - 2
Got:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 - 2
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_nf_galois_groups.py
	 [12.4 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/6322





---

archive/issue_comments_050450.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-10-10T18:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50450",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050451.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2015-10-10T18:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50451",
    "user": "chapoton"
}
```

Changing priority from major to minor.



---

archive/issue_comments_050452.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-10-10T18:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50452",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_050453.json:
```json
{
    "body": "Did you actually test it? I don't have magma, but if you tell me that the doctest passes, I believe you.",
    "created_at": "2015-10-10T20:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50453",
    "user": "jdemeyer"
}
```

Did you actually test it? I don't have magma, but if you tell me that the doctest passes, I believe you.



---

archive/issue_comments_050454.json:
```json
{
    "body": "I do not have magma either. Do we know somebody that has magma ?",
    "created_at": "2015-10-10T20:34:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50454",
    "user": "chapoton"
}
```

I do not have magma either. Do we know somebody that has magma ?



---

archive/issue_comments_050455.json:
```json
{
    "body": "Replying to [comment:8 chapoton]:\n> I do not have magma either.\n\nThen why do you care about this ticket???",
    "created_at": "2015-10-10T21:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50455",
    "user": "jdemeyer"
}
```

Replying to [comment:8 chapoton]:
> I do not have magma either.

Then why do you care about this ticket???



---

archive/issue_comments_050456.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-12T17:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50456",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_050457.json:
```json
{
    "body": "It appears that:\n\n1) I do have `magma` now\n2) The test requires `database_gap`\n\nThis has been tested, and needs review again.",
    "created_at": "2015-10-12T17:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50457",
    "user": "chapoton"
}
```

It appears that:

1) I do have `magma` now
2) The test requires `database_gap`

This has been tested, and needs review again.



---

archive/issue_comments_050458.json:
```json
{
    "body": "ok, the tests do pass with magma and database_gap and also without both\n\ni am not quite sure of the way to put 2 optional conditions on the same line\n\nJeroen, could you please set a positive review if this is correct ?",
    "created_at": "2015-10-17T20:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50458",
    "user": "chapoton"
}
```

ok, the tests do pass with magma and database_gap and also without both

i am not quite sure of the way to put 2 optional conditions on the same line

Jeroen, could you please set a positive review if this is correct ?



---

archive/issue_comments_050459.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-10-17T20:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50459",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050460.json:
```json
{
    "body": "The usual syntax is\n\n```\n# optional - magma database_gap\n```\n\nI don't know if what you did works or not, but it's better to change it.",
    "created_at": "2015-10-17T20:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50460",
    "user": "jdemeyer"
}
```

The usual syntax is

```
# optional - magma database_gap
```

I don't know if what you did works or not, but it's better to change it.



---

archive/issue_comments_050461.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-17T20:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50461",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_050462.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-10-17T20:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50462",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050463.json:
```json
{
    "body": "done",
    "created_at": "2015-10-17T20:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50463",
    "user": "chapoton"
}
```

done



---

archive/issue_comments_050464.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-10-17T20:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50464",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050465.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-10-18T19:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6322#issuecomment-50465",
    "user": "vbraun"
}
```

Resolution: fixed
