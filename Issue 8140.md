# Issue 8140: words.CharacteristicSturmianWord does not do what it says

archive/issues_008140.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  abmasse\n\nThe doc of `words.CharacteristicSturmianWord` says :\n\n\n```\nINPUT:\n-  ``cf`` - an iterator outputting integers (thought of as a\n               continued fraction)\n```\n\n\nBut it does not do what it says. In fact the following \n\n\n```\nsage: cf = CFF(1/golden_ratio^2)\nsage: words.CharacteristicSturmianWord(cf)\nword: 0010001001000100010010001001000100010010...\n```\n\n\nshould output the same as\n\n\n```\nsage: words.FibonacciWord()\nword: 0100101001001010010100100101001001010010...\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8140\n\n",
    "created_at": "2010-01-31T23:52:08Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "words.CharacteristicSturmianWord does not do what it says",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8140",
    "user": "slabbe"
}
```
Assignee: sage-combinat

CC:  abmasse

The doc of `words.CharacteristicSturmianWord` says :


```
INPUT:
-  ``cf`` - an iterator outputting integers (thought of as a
               continued fraction)
```


But it does not do what it says. In fact the following 


```
sage: cf = CFF(1/golden_ratio^2)
sage: words.CharacteristicSturmianWord(cf)
word: 0010001001000100010010001001000100010010...
```


should output the same as


```
sage: words.FibonacciWord()
word: 0100101001001010010100100101001001010010...
```



Issue created by migration from https://trac.sagemath.org/ticket/8140





---

archive/issue_comments_071569.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-01T00:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8140#issuecomment-71569",
    "user": "slabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071570.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-02-01T21:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8140#issuecomment-71570",
    "user": "slabbe"
}
```

Attachment



---

archive/issue_comments_071571.json:
```json
{
    "body": "I just uploaded the patch : I corrected a sphinx warning. I hope it will not create conflicts if Alexandre started a review...",
    "created_at": "2010-02-01T21:05:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8140#issuecomment-71571",
    "user": "slabbe"
}
```

I just uploaded the patch : I corrected a sphinx warning. I hope it will not create conflicts if Alexandre started a review...



---

archive/issue_comments_071572.json:
```json
{
    "body": "I reviewed this patch and made the following minor modifications, mostly in the documentation:\n- I gave three different equivalent definitions of characteristic Sturmian word as presented in the Lothaire book.\n- I changed the name of the variable `cf` for `slope` in the characteristic Sturmian.\n- I modified the NotImplementedError raised by the three functions by a ValueError. It seems more appropriate since values of slope are in general assumed to be in (0,1). S\u00e9bastien, if you still insist on keeping NotImplementedError, I would put a different message, something like \"not implemented for values out of (0,1)\"\n- I made other minor changes and updated the examples in consequence.\nAll tests passed, the code seems good and correct the problem mentionned in this ticket. The doc is alright too.",
    "created_at": "2010-02-03T14:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8140#issuecomment-71572",
    "user": "abmasse"
}
```

I reviewed this patch and made the following minor modifications, mostly in the documentation:
- I gave three different equivalent definitions of characteristic Sturmian word as presented in the Lothaire book.
- I changed the name of the variable `cf` for `slope` in the characteristic Sturmian.
- I modified the NotImplementedError raised by the three functions by a ValueError. It seems more appropriate since values of slope are in general assumed to be in (0,1). Sébastien, if you still insist on keeping NotImplementedError, I would put a different message, something like "not implemented for values out of (0,1)"
- I made other minor changes and updated the examples in consequence.
All tests passed, the code seems good and correct the problem mentionned in this ticket. The doc is alright too.



---

archive/issue_comments_071573.json:
```json
{
    "body": "Attachment\n\nFew minor changes -- I let S\u00e9bastien check if he approves the changes",
    "created_at": "2010-02-03T14:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8140#issuecomment-71573",
    "user": "abmasse"
}
```

Attachment

Few minor changes -- I let Sébastien check if he approves the changes



---

archive/issue_comments_071574.json:
```json
{
    "body": "Attachment\n\nApplies over the two precedent patches.",
    "created_at": "2010-02-04T17:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8140#issuecomment-71574",
    "user": "slabbe"
}
```

Attachment

Applies over the two precedent patches.



---

archive/issue_comments_071575.json:
```json
{
    "body": "I agree with your changes. I fix the doc (the irrationality of alpha is necessary for the lower and upper mechanical word to be equal). I also added `rename_keyword` of the `cf` argument that you removed for backward compatibility.\n\nI give a positive review to Alexandre's changes. Alexandre, I let you change the status of the ticket to positive review if you agree with my two patches.",
    "created_at": "2010-02-04T17:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8140#issuecomment-71575",
    "user": "slabbe"
}
```

I agree with your changes. I fix the doc (the irrationality of alpha is necessary for the lower and upper mechanical word to be equal). I also added `rename_keyword` of the `cf` argument that you removed for backward compatibility.

I give a positive review to Alexandre's changes. Alexandre, I let you change the status of the ticket to positive review if you agree with my two patches.



---

archive/issue_comments_071576.json:
```json
{
    "body": "Full name in those boxes helps the release managers when writing the release notes.",
    "created_at": "2010-02-04T17:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8140#issuecomment-71576",
    "user": "slabbe"
}
```

Full name in those boxes helps the release managers when writing the release notes.



---

archive/issue_comments_071577.json:
```json
{
    "body": "Rechecked the three functions after applying all three patches and everything looks fine. All tests passed, the doc built with Sphinx looks alright too and I agree with the last minor changes of S\u00e9bastien. Positive review as well !\nThanks for the info about the full names in the boxes, I wasn't sure what to do about that.",
    "created_at": "2010-02-04T21:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8140#issuecomment-71577",
    "user": "abmasse"
}
```

Rechecked the three functions after applying all three patches and everything looks fine. All tests passed, the doc built with Sphinx looks alright too and I agree with the last minor changes of Sébastien. Positive review as well !
Thanks for the info about the full names in the boxes, I wasn't sure what to do about that.



---

archive/issue_comments_071578.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-04T21:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8140#issuecomment-71578",
    "user": "abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071579.json:
```json
{
    "body": "The commit string for the third patch is not sufficiently descriptive.  I've refreshed it in my queue for 4.3.3.alpha0: `#8140: Added rename_keyword for the cf argument`.  Please let me know if this is not good enough!",
    "created_at": "2010-02-10T14:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8140#issuecomment-71579",
    "user": "mpatel"
}
```

The commit string for the third patch is not sufficiently descriptive.  I've refreshed it in my queue for 4.3.3.alpha0: `#8140: Added rename_keyword for the cf argument`.  Please let me know if this is not good enough!



---

archive/issue_comments_071580.json:
```json
{
    "body": "Replying to [comment:7 mpatel]:\n> The commit string for the third patch is not sufficiently descriptive.  I've refreshed it in my queue for 4.3.3.alpha0: `#8140: Added rename_keyword for the cf argument`.  Please let me know if this is not good enough!\n\nIt is perfect (sorry, I forgot to write the description).",
    "created_at": "2010-02-10T14:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8140#issuecomment-71580",
    "user": "slabbe"
}
```

Replying to [comment:7 mpatel]:
> The commit string for the third patch is not sufficiently descriptive.  I've refreshed it in my queue for 4.3.3.alpha0: `#8140: Added rename_keyword for the cf argument`.  Please let me know if this is not good enough!

It is perfect (sorry, I forgot to write the description).



---

archive/issue_comments_071581.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8140#issuecomment-71581",
    "user": "mpatel"
}
```

Resolution: fixed
