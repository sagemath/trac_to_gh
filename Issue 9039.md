# Issue 9039: major error in E.sha().bound_kato() for E an elliptic curve

archive/issues_009039.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  @categorie\n\nDoes not check for primes of bad reduction at all!!\n\nIssue created by migration from https://trac.sagemath.org/ticket/9039\n\n",
    "created_at": "2010-05-25T00:37:50Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "major error in E.sha().bound_kato() for E an elliptic curve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9039",
    "user": "https://github.com/rlmill"
}
```
Assignee: @JohnCremona

CC:  @categorie

Does not check for primes of bad reduction at all!!

Issue created by migration from https://trac.sagemath.org/ticket/9039





---

archive/issue_comments_083537.json:
```json
{
    "body": "I haven't yet fixed the documentation results, since the returned lists are different, mainly to highlight the differences... Also I'm not entirely sure I have the code exactly right, maybe you can verify this. I also think that the references need updating/completing.\n\nInput is welcome! Here are the doc differences:\n\n```\nsage -t -long \"devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\"\nSaturation index bound = 265\nWARNING: saturation at primes p > 100 will not be done;  \npoints may be unsaturated at primes between 100 and index bound\nFailed to saturate MW basis at primes [ ]\n*** saturation possibly incomplete at primes [ ]\n**********************************************************************\nFile \"/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\", line 876:\n    sage: E.sha().bound_kato()\nExpected:\n    [2, 3, 5]\nGot:\n    [2]\n**********************************************************************\nFile \"/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\", line 879:\n    sage: E.sha().bound_kato()\nExpected:\n    [2, 3, 5]\nGot:\n    [2]\n**********************************************************************\nFile \"/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\", line 882:\n    sage: E.sha().bound_kato()\nExpected:\n    [2, 3]\nGot:\n    [2]\n**********************************************************************\nFile \"/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\", line 888:\n    sage: E.sha().bound_kato()                 # long time (about 1 second)\nExpected:\n    [2, 3, 5]\nGot:\n    [2, 5, 23]\n**********************************************************************\nFile \"/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\", line 896:\n    sage: E.sha().bound_kato()                 # long time (< 10 seconds)\nExpected:\n    [2, 3, 7]\nGot:\n    [2, 7, 29]\n**********************************************************************\n1 items had failures:\n   5 of  15 in __main__.example_8\n***Test Failed*** 5 failures.\nFor whitespace errors, see the file /Users/rlmill/.sage//tmp/.doctest_sha_tate.py\n\t [154.4 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long \"devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\"\nTotal time for all tests: 154.4 seconds\n```",
    "created_at": "2010-05-25T01:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9039#issuecomment-83537",
    "user": "https://github.com/rlmill"
}
```

I haven't yet fixed the documentation results, since the returned lists are different, mainly to highlight the differences... Also I'm not entirely sure I have the code exactly right, maybe you can verify this. I also think that the references need updating/completing.

Input is welcome! Here are the doc differences:

```
sage -t -long "devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py"
Saturation index bound = 265
WARNING: saturation at primes p > 100 will not be done;  
points may be unsaturated at primes between 100 and index bound
Failed to saturate MW basis at primes [ ]
*** saturation possibly incomplete at primes [ ]
**********************************************************************
File "/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py", line 876:
    sage: E.sha().bound_kato()
Expected:
    [2, 3, 5]
Got:
    [2]
**********************************************************************
File "/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py", line 879:
    sage: E.sha().bound_kato()
Expected:
    [2, 3, 5]
Got:
    [2]
**********************************************************************
File "/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py", line 882:
    sage: E.sha().bound_kato()
Expected:
    [2, 3]
Got:
    [2]
**********************************************************************
File "/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py", line 888:
    sage: E.sha().bound_kato()                 # long time (about 1 second)
Expected:
    [2, 3, 5]
Got:
    [2, 5, 23]
**********************************************************************
File "/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py", line 896:
    sage: E.sha().bound_kato()                 # long time (< 10 seconds)
Expected:
    [2, 3, 7]
Got:
    [2, 7, 29]
**********************************************************************
1 items had failures:
   5 of  15 in __main__.example_8
***Test Failed*** 5 failures.
For whitespace errors, see the file /Users/rlmill/.sage//tmp/.doctest_sha_tate.py
	 [154.4 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py"
Total time for all tests: 154.4 seconds
```



---

archive/issue_comments_083538.json:
```json
{
    "body": "In principle, I agree with the changes. Certainly the additive primes must go in that list.\n\nWhen it comes to the the condition on the mod-p representation, I would propose to wait. I have submitted a correction for the article proving this. But before I get the confirmation that everything is fine now, I would not want to change this back in sage. Also there will be other places as in p_primary_bound where a change will be needed in that case.\n\nDo you want to wait ? Or do you want to fix the issue with the additive first and open another ticket when/if the corrections are accepted ?\n\nChris.",
    "created_at": "2010-05-25T14:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9039#issuecomment-83538",
    "user": "https://github.com/categorie"
}
```

In principle, I agree with the changes. Certainly the additive primes must go in that list.

When it comes to the the condition on the mod-p representation, I would propose to wait. I have submitted a correction for the article proving this. But before I get the confirmation that everything is fine now, I would not want to change this back in sage. Also there will be other places as in p_primary_bound where a change will be needed in that case.

Do you want to wait ? Or do you want to fix the issue with the additive first and open another ticket when/if the corrections are accepted ?

Chris.



---

archive/issue_comments_083539.json:
```json
{
    "body": "Chris,\n\nReplying to [comment:2 wuthrich]:\n> Do you want to wait ? Or do you want to fix the issue with the additive first and open another ticket when/if the corrections are accepted ?\n\n\nI am not in favor of waiting. Let's get the patch up to speed with what is currently known and verified, and update the function once we're ready to.\n\nIn order to get an acceptable patch for now, are you saying that the only change should be to add in the additive primes? If so I can modify my patch to do only that.",
    "created_at": "2010-05-25T16:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9039#issuecomment-83539",
    "user": "https://github.com/rlmill"
}
```

Chris,

Replying to [comment:2 wuthrich]:
> Do you want to wait ? Or do you want to fix the issue with the additive first and open another ticket when/if the corrections are accepted ?


I am not in favor of waiting. Let's get the patch up to speed with what is currently known and verified, and update the function once we're ready to.

In order to get an acceptable patch for now, are you saying that the only change should be to add in the additive primes? If so I can modify my patch to do only that.



---

archive/issue_comments_083540.json:
```json
{
    "body": "Yes, the list should contain 2, all primes of additive reduction and all for which the mod-p representation is not surjective.",
    "created_at": "2010-05-25T21:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9039#issuecomment-83540",
    "user": "https://github.com/categorie"
}
```

Yes, the list should contain 2, all primes of additive reduction and all for which the mod-p representation is not surjective.



---

archive/issue_comments_083541.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-25T22:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9039#issuecomment-83541",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083542.json:
```json
{
    "body": "The new patch gives doctest changes as well. Are you sure that this is correct (mod-p vs. p-adic rep'n surjective, etc.) for p=3? If it is, then it's all ready for review.",
    "created_at": "2010-05-25T22:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9039#issuecomment-83542",
    "user": "https://github.com/rlmill"
}
```

The new patch gives doctest changes as well. Are you sure that this is correct (mod-p vs. p-adic rep'n surjective, etc.) for p=3? If it is, then it's all ready for review.



---

archive/issue_comments_083543.json:
```json
{
    "body": "Ooops, you are right. Elkies describes these curves (they are rare) and shows that they do not contain SL_2(Z_p) in the p-adic Galois image. And that is needed for Kato's theorem 12.5. I have the vague feeling that one could lower it to the case of mod-p-surjectivity with some work, but I am sure it is not yet known if that is true.\n\nThat makes the check at 3 quite painful. Maybe we should just include 3 by default. I will look at the galois representations in sage soon again. Maybe I find an easy way to check it for p=3.\n\nChris.",
    "created_at": "2010-05-26T09:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9039#issuecomment-83543",
    "user": "https://github.com/categorie"
}
```

Ooops, you are right. Elkies describes these curves (they are rare) and shows that they do not contain SL_2(Z_p) in the p-adic Galois image. And that is needed for Kato's theorem 12.5. I have the vague feeling that one could lower it to the case of mod-p-surjectivity with some work, but I am sure it is not yet known if that is true.

That makes the check at 3 quite painful. Maybe we should just include 3 by default. I will look at the galois representations in sage soon again. Maybe I find an easy way to check it for p=3.

Chris.



---

archive/issue_comments_083544.json:
```json
{
    "body": "Attachment [trac_9039.patch](tarball://root/attachments/some-uuid/ticket9039/trac_9039.patch) by @rlmill created at 2010-05-27 22:32:57\n\nChris,\n\nTake a look at the newest patch. This should provide a correct version of `bound_kato`.",
    "created_at": "2010-05-27T22:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9039#issuecomment-83544",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9039.patch](tarball://root/attachments/some-uuid/ticket9039/trac_9039.patch) by @rlmill created at 2010-05-27 22:32:57

Chris,

Take a look at the newest patch. This should provide a correct version of `bound_kato`.



---

archive/issue_comments_083545.json:
```json
{
    "body": "All tests passed. This small but important change must go in !\nThanks, Robert.",
    "created_at": "2010-05-28T13:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9039#issuecomment-83545",
    "user": "https://github.com/categorie"
}
```

All tests passed. This small but important change must go in !
Thanks, Robert.



---

archive/issue_comments_083546.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-28T13:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9039#issuecomment-83546",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022128.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-04T15:28:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9039#event-22128"
}
```



---

archive/issue_comments_083547.json:
```json
{
    "body": "I'm merging this in, since Robert begged me to, and it's a 1-line fix I understand well, that has very, very low chance of causing any trouble elsewhere.",
    "created_at": "2010-06-04T15:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9039#issuecomment-83547",
    "user": "https://github.com/williamstein"
}
```

I'm merging this in, since Robert begged me to, and it's a 1-line fix I understand well, that has very, very low chance of causing any trouble elsewhere.



---

archive/issue_comments_083548.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-04T15:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9039#issuecomment-83548",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_022129.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-04T15:28:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9039",
    "milestone": "sage-4.4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9039#event-22129"
}
```
