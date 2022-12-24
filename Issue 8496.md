# Issue 8496: Implement canonical heights for elliptic curves over number fields

archive/issues_008496.json:
```json
{
    "body": "Assignee: cremona\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8496\n\n",
    "created_at": "2010-03-11T08:14:07Z",
    "labels": [
        "elliptic curves",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Implement canonical heights for elliptic curves over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8496",
    "user": "robertwb"
}
```
Assignee: cremona



Issue created by migration from https://trac.sagemath.org/ticket/8496





---

archive/issue_comments_076656.json:
```json
{
    "body": "Attachment [8496-nf-height.patch](tarball://root/attachments/some-uuid/ticket8496/8496-nf-height.patch) by robertwb created at 2010-03-11 08:16:56",
    "created_at": "2010-03-11T08:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76656",
    "user": "robertwb"
}
```

Attachment [8496-nf-height.patch](tarball://root/attachments/some-uuid/ticket8496/8496-nf-height.patch) by robertwb created at 2010-03-11 08:16:56



---

archive/issue_comments_076657.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-11T08:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76657",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076658.json:
```json
{
    "body": "Very good. I was hoping that someone would implemented it soon ! Thanks a lot.\n\nI will have a look at it. (And add more documentation to it : You normalised the height to be independent of the base field, which is one of the two possible normalisations, and it should be documented)",
    "created_at": "2010-03-11T10:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76658",
    "user": "wuthrich"
}
```

Very good. I was hoping that someone would implemented it soon ! Thanks a lot.

I will have a look at it. (And add more documentation to it : You normalised the height to be independent of the base field, which is one of the two possible normalisations, and it should be documented)



---

archive/issue_comments_076659.json:
```json
{
    "body": "Excellent -- I will look at it too.  I have implemented this more than once, so know the algorithm well.\n\nAny reason not to use ticket #360 which has been patiently waiting for 3 years?",
    "created_at": "2010-03-11T10:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76659",
    "user": "cremona"
}
```

Excellent -- I will look at it too.  I have implemented this more than once, so know the algorithm well.

Any reason not to use ticket #360 which has been patiently waiting for 3 years?



---

archive/issue_comments_076660.json:
```json
{
    "body": "The patch did not apply to 4.3.4.alpha1.\n\n`Hunk #4 FAILED at 1687`\n\nA rebase is needed.",
    "created_at": "2010-03-11T10:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76660",
    "user": "wuthrich"
}
```

The patch did not apply to 4.3.4.alpha1.

`Hunk #4 FAILED at 1687`

A rebase is needed.



---

archive/issue_comments_076661.json:
```json
{
    "body": "Hmm... #360 looks like it's also about implementing height bounds as well, which I also plan to do if no one beats me to it, but don't want to wait up to get this in. \n\nI'll have to get ahold of an alpha to try and rebase it (and document the normalization choice).",
    "created_at": "2010-03-11T18:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76661",
    "user": "robertwb"
}
```

Hmm... #360 looks like it's also about implementing height bounds as well, which I also plan to do if no one beats me to it, but don't want to wait up to get this in. 

I'll have to get ahold of an alpha to try and rebase it (and document the normalization choice).



---

archive/issue_comments_076662.json:
```json
{
    "body": "I noticed in the docstrings that you specify INPUT variables like this:\n\n```\n        1824         INPUT:: \n        1825\t            v - a non-archimedean place of the base field of the curve, \n \t1826\t                or None, in which case the total nonarchimedian contribution \n \t1827\t                is returned \n \t1828\t         \n \t1829\t            prec - working precision, or None in which case the height  \n \t1830\t                is returned symbolically \n```\n\n\nI don't think this is so nice in Sphinx, since it is just preformated.  The vast majority of docstrings are formatted like as a list:\n\n\n```\n        1824            INPUT:\n        1825\t            - ``v`` - a non-archimedean place of the base field of the curve, \n \t1826\t              or None, in which case the total nonarchimedian contribution \n \t1827\t              is returned \n \t1828\t         \n \t1829\t            - ``prec`` - working precision, or None in which case the height  \n \t1830\t              is returned symbolically \n```\n\n\nNote that:\n   \n* only one colon after \"INPUT\"\n* a dash at the start of each line\n* the indentation is two spaces after the dash.",
    "created_at": "2010-03-12T01:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76662",
    "user": "was"
}
```

I noticed in the docstrings that you specify INPUT variables like this:

```
        1824         INPUT:: 
        1825	            v - a non-archimedean place of the base field of the curve, 
 	1826	                or None, in which case the total nonarchimedian contribution 
 	1827	                is returned 
 	1828	         
 	1829	            prec - working precision, or None in which case the height  
 	1830	                is returned symbolically 
```


I don't think this is so nice in Sphinx, since it is just preformated.  The vast majority of docstrings are formatted like as a list:


```
        1824            INPUT:
        1825	            - ``v`` - a non-archimedean place of the base field of the curve, 
 	1826	              or None, in which case the total nonarchimedian contribution 
 	1827	              is returned 
 	1828	         
 	1829	            - ``prec`` - working precision, or None in which case the height  
 	1830	              is returned symbolically 
```


Note that:
   
* only one colon after "INPUT"
* a dash at the start of each line
* the indentation is two spaces after the dash.



---

archive/issue_comments_076663.json:
```json
{
    "body": "Changing assignee from cremona to was.",
    "created_at": "2010-03-12T01:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76663",
    "user": "was"
}
```

Changing assignee from cremona to was.



---

archive/issue_comments_076664.json:
```json
{
    "body": "Is there a reason the 0 is returned in QQ ?\n\nI will later modify this, because I will need the exp() of the local heights for non-archimedean primes as an element in QQ, if I want to implement the p-adic heights over number fields.",
    "created_at": "2010-03-12T09:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76664",
    "user": "wuthrich"
}
```

Is there a reason the 0 is returned in QQ ?

I will later modify this, because I will need the exp() of the local heights for non-archimedean primes as an element in QQ, if I want to implement the p-adic heights over number fields.



---

archive/issue_comments_076665.json:
```json
{
    "body": "Replying to [comment:7 wuthrich]:\n> Is there a reason the 0 is returned in QQ ?\n\nFor consistency with the original code, and for speed (not that it should matter much). \n\n> I will later modify this, because I will need the exp() of the local heights for non-archimedean primes as an element in QQ, if I want to implement the p-adic heights over number fields.\n\nYou can do exp of an element of QQ just fine.",
    "created_at": "2010-03-12T10:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76665",
    "user": "robertwb"
}
```

Replying to [comment:7 wuthrich]:
> Is there a reason the 0 is returned in QQ ?

For consistency with the original code, and for speed (not that it should matter much). 

> I will later modify this, because I will need the exp() of the local heights for non-archimedean primes as an element in QQ, if I want to implement the p-adic heights over number fields.

You can do exp of an element of QQ just fine.



---

archive/issue_comments_076666.json:
```json
{
    "body": "Replying to [comment:8 robertwb]:\n> You can do exp of an element of QQ just fine. \n\nSure, that is not what I meant. I will put all your code of `nonarchimedian_local_height` into a helper function that returns r and Nv and then the main function will only take log. So that in the p-adic case I can take p-adic logs of the rational Nv.\n\nBut don't worry I will do that when I will implement p-adic height. It was only to remind myself that I should do that.",
    "created_at": "2010-03-12T10:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76666",
    "user": "wuthrich"
}
```

Replying to [comment:8 robertwb]:
> You can do exp of an element of QQ just fine. 

Sure, that is not what I meant. I will put all your code of `nonarchimedian_local_height` into a helper function that returns r and Nv and then the main function will only take log. So that in the p-adic case I can take p-adic logs of the rational Nv.

But don't worry I will do that when I will implement p-adic height. It was only to remind myself that I should do that.



---

archive/issue_comments_076667.json:
```json
{
    "body": "The code looks ok to me (I spotted one mis-spelling of Silverman!), and I checked that the results agree with magma, but I'll leave the formal review to Chris who has started and wants to add to the documentation.",
    "created_at": "2010-03-13T15:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76667",
    "user": "cremona"
}
```

The code looks ok to me (I spotted one mis-spelling of Silverman!), and I checked that the results agree with magma, but I'll leave the formal review to Chris who has started and wants to add to the documentation.



---

archive/issue_comments_076668.json:
```json
{
    "body": "exported against 4.3.4.alpha1",
    "created_at": "2010-03-15T15:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76668",
    "user": "wuthrich"
}
```

exported against 4.3.4.alpha1



---

archive/issue_comments_076669.json:
```json
{
    "body": "Attachment [trac_8496_rebased.patch](tarball://root/attachments/some-uuid/ticket8496/trac_8496_rebased.patch) by wuthrich created at 2010-03-15 15:30:01\n\nI have put up a rebased patch with a few minor changes. But I have not included yet the documentation on the normalization. You write \"THE BSD formula\", but there is not a unique standard way of stating the conjecture, I fear. Also the question is whether or not you divide the height pairing by two or not. Could you clarify this ?\n\nI deleted the assumption that E was defined over Q. I don't think you will need that. Maybe it is needed that the model is integral, but I do not see where you would require the curve to be defined over Q. Please correct me if I am wrong.\n\nBy the way the diff of our two patches comes mainly from converting tabs to spaces.",
    "created_at": "2010-03-15T15:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76669",
    "user": "wuthrich"
}
```

Attachment [trac_8496_rebased.patch](tarball://root/attachments/some-uuid/ticket8496/trac_8496_rebased.patch) by wuthrich created at 2010-03-15 15:30:01

I have put up a rebased patch with a few minor changes. But I have not included yet the documentation on the normalization. You write "THE BSD formula", but there is not a unique standard way of stating the conjecture, I fear. Also the question is whether or not you divide the height pairing by two or not. Could you clarify this ?

I deleted the assumption that E was defined over Q. I don't think you will need that. Maybe it is needed that the model is integral, but I do not see where you would require the curve to be defined over Q. Please correct me if I am wrong.

By the way the diff of our two patches comes mainly from converting tabs to spaces.



---

archive/issue_comments_076670.json:
```json
{
    "body": "Replying to [comment:11 wuthrich]:\n> I have put up a rebased patch with a few minor changes. But I have not included yet the documentation on the normalization. You write \"THE BSD formula\", but there is not a unique standard way of stating the conjecture, I fear. Also the question is whether or not you divide the height pairing by two or not. Could you clarify this ?\n\nOK, I have expanded the normalization section, borrowing heavily from the explanation found in John Cremona's book. \n\n> I deleted the assumption that E was defined over Q. I don't think you will need that. Maybe it is needed that the model is integral, but I do not see where you would require the curve to be defined over Q. Please correct me if I am wrong.\n\nYes, you are correct. (There are examples to this effect.) \n\n> By the way the diff of our two patches comes mainly from converting tabs to spaces.\n\nThey were not of my doing, but thanks for expunging them.",
    "created_at": "2010-03-15T19:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76670",
    "user": "robertwb"
}
```

Replying to [comment:11 wuthrich]:
> I have put up a rebased patch with a few minor changes. But I have not included yet the documentation on the normalization. You write "THE BSD formula", but there is not a unique standard way of stating the conjecture, I fear. Also the question is whether or not you divide the height pairing by two or not. Could you clarify this ?

OK, I have expanded the normalization section, borrowing heavily from the explanation found in John Cremona's book. 

> I deleted the assumption that E was defined over Q. I don't think you will need that. Maybe it is needed that the model is integral, but I do not see where you would require the curve to be defined over Q. Please correct me if I am wrong.

Yes, you are correct. (There are examples to this effect.) 

> By the way the diff of our two patches comes mainly from converting tabs to spaces.

They were not of my doing, but thanks for expunging them.



---

archive/issue_comments_076671.json:
```json
{
    "body": "Rebased and updated, apply only this patch.",
    "created_at": "2010-03-15T19:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76671",
    "user": "robertwb"
}
```

Rebased and updated, apply only this patch.



---

archive/issue_comments_076672.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-15T20:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76672",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076673.json:
```json
{
    "body": "Attachment [8496-nf-height-again.patch](tarball://root/attachments/some-uuid/ticket8496/8496-nf-height-again.patch) by cremona created at 2010-03-15 20:33:06\n\nNew patch applies fine to 4.3.4.alpha1, and all tests in sage/schemes/elliptic_curves pass (tested both 32 and 64 bit).  Good!",
    "created_at": "2010-03-15T20:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76673",
    "user": "cremona"
}
```

Attachment [8496-nf-height-again.patch](tarball://root/attachments/some-uuid/ticket8496/8496-nf-height-again.patch) by cremona created at 2010-03-15 20:33:06

New patch applies fine to 4.3.4.alpha1, and all tests in sage/schemes/elliptic_curves pass (tested both 32 and 64 bit).  Good!



---

archive/issue_comments_076674.json:
```json
{
    "body": "This doesn't apply cleanly to Sage 4.4.alpha0; apparently it conflicts with a patch merged into that.  Please rebase it, and we'll try hard to get it into 4.4.alpha1.",
    "created_at": "2010-04-17T04:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76674",
    "user": "jhpalmieri"
}
```

This doesn't apply cleanly to Sage 4.4.alpha0; apparently it conflicts with a patch merged into that.  Please rebase it, and we'll try hard to get it into 4.4.alpha1.



---

archive/issue_comments_076675.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-17T04:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76675",
    "user": "jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076676.json:
```json
{
    "body": "Attachment [8496-rebased-4.4.alpha0.patch](tarball://root/attachments/some-uuid/ticket8496/8496-rebased-4.4.alpha0.patch) by robertwb created at 2010-04-17 19:28:44",
    "created_at": "2010-04-17T19:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76676",
    "user": "robertwb"
}
```

Attachment [8496-rebased-4.4.alpha0.patch](tarball://root/attachments/some-uuid/ticket8496/8496-rebased-4.4.alpha0.patch) by robertwb created at 2010-04-17 19:28:44



---

archive/issue_comments_076677.json:
```json
{
    "body": "OK, rebased. It looks like it was just deleting some tabs that someone else also deleted, which was easy to fix.",
    "created_at": "2010-04-17T19:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76677",
    "user": "robertwb"
}
```

OK, rebased. It looks like it was just deleting some tabs that someone else also deleted, which was easy to fix.



---

archive/issue_comments_076678.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-17T19:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76678",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076679.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-17T19:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76679",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076680.json:
```json
{
    "body": "I'm remarking this as positive review as there was no content change in the rebase.",
    "created_at": "2010-04-17T19:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76680",
    "user": "robertwb"
}
```

I'm remarking this as positive review as there was no content change in the rebase.



---

archive/issue_comments_076681.json:
```json
{
    "body": "Merged \"8496-rebased-4.4.alpha0.patch\" into 4.4.alpha1.",
    "created_at": "2010-04-19T05:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76681",
    "user": "jhpalmieri"
}
```

Merged "8496-rebased-4.4.alpha0.patch" into 4.4.alpha1.



---

archive/issue_comments_076682.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76682",
    "user": "jhpalmieri"
}
```

Resolution: fixed
