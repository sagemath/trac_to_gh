# Issue 3003: Bugfix for to_tableau() method of CrystalOfTableaux elements (with patch; needs review)

archive/issues_003003.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nKeywords: crystals, tableaux\n\nCurrent behaviour:\n    sage: C = CrystalOfTableaux(['A',3],shape=[2,1])\n    sage: h = C.highest_weight_vector()\n    sage: t = h.to_tableau()\n    sage: w = t.to_word(); w\n    [2, 1, 1]\n    sage: type(w[0])\n    <class 'sage.combinat.crystals.letters.Crystal_of_letters_type_A_element'>\n    sage: t.evaluation()\n    <BOOM>\n\nThis patch ensures we get a tableau of integers instead of a tableau of crystal elements.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3003\n\n",
    "created_at": "2008-04-22T17:14:31Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Bugfix for to_tableau() method of CrystalOfTableaux elements (with patch; needs review)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3003",
    "user": "jbandlow"
}
```
Assignee: mhansen

CC:  sage-combinat

Keywords: crystals, tableaux

Current behaviour:
    sage: C = CrystalOfTableaux(['A',3],shape=[2,1])
    sage: h = C.highest_weight_vector()
    sage: t = h.to_tableau()
    sage: w = t.to_word(); w
    [2, 1, 1]
    sage: type(w[0])
    <class 'sage.combinat.crystals.letters.Crystal_of_letters_type_A_element'>
    sage: t.evaluation()
    <BOOM>

This patch ensures we get a tableau of integers instead of a tableau of crystal elements.

Issue created by migration from https://trac.sagemath.org/ticket/3003





---

archive/issue_comments_020658.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-22T17:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3003#issuecomment-20658",
    "user": "jbandlow"
}
```

Attachment



---

archive/issue_comments_020659.json:
```json
{
    "body": "The elements of crystals of letters look like integers because their __repr__ method returns an integer string but they are not. Before the patch it is possible to accidentally build tableaux whose entries are crystal of letter elements. The patch looks obviously correct to me. I'm not sure  this bugfix requires a doctest.",
    "created_at": "2008-04-22T17:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3003#issuecomment-20659",
    "user": "bump"
}
```

The elements of crystals of letters look like integers because their __repr__ method returns an integer string but they are not. Before the patch it is possible to accidentally build tableaux whose entries are crystal of letter elements. The patch looks obviously correct to me. I'm not sure  this bugfix requires a doctest.



---

archive/issue_comments_020660.json:
```json
{
    "body": "I know that Dan did a review, but we still need a formal vote. Since there is a test case that Jason posted we should add it as a doctest. If it runs long we should add #long to it.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-22T20:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3003#issuecomment-20660",
    "user": "mabshoff"
}
```

I know that Dan did a review, but we still need a formal vote. Since there is a test case that Jason posted we should add it as a doctest. If it runs long we should add #long to it.

Cheers,

Michael



---

archive/issue_comments_020661.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-22T22:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3003#issuecomment-20661",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_020662.json:
```json
{
    "body": "Looks good to me.  I added a little test in 3003.patch -- that's the one that should be applied.",
    "created_at": "2008-04-22T22:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3003#issuecomment-20662",
    "user": "mhansen"
}
```

Looks good to me.  I added a little test in 3003.patch -- that's the one that should be applied.



---

archive/issue_comments_020663.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-23T11:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3003#issuecomment-20663",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020664.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-23T11:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3003#issuecomment-20664",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha0
