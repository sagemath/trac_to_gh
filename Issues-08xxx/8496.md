# Issue 8496: Implement canonical heights for elliptic curves over number fields

archive/issues_008496.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8496\n\n",
    "closed_at": "2010-04-19T05:16:32Z",
    "created_at": "2010-03-11T08:14:07Z",
    "labels": [
        "component: elliptic curves"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Implement canonical heights for elliptic curves over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8496",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/8496





---

archive/issue_comments_076529.json:
```json
{
    "body": "Attachment [8496-nf-height.patch](tarball://root/attachments/some-uuid/ticket8496/8496-nf-height.patch) by @robertwb created at 2010-03-11 08:16:56",
    "created_at": "2010-03-11T08:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76529",
    "user": "https://github.com/robertwb"
}
```

Attachment [8496-nf-height.patch](tarball://root/attachments/some-uuid/ticket8496/8496-nf-height.patch) by @robertwb created at 2010-03-11 08:16:56



---

archive/issue_comments_076530.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-11T08:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76530",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076531.json:
```json
{
    "body": "Very good. I was hoping that someone would implemented it soon ! Thanks a lot.\n\nI will have a look at it. (And add more documentation to it : You normalised the height to be independent of the base field, which is one of the two possible normalisations, and it should be documented)",
    "created_at": "2010-03-11T10:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76531",
    "user": "https://github.com/categorie"
}
```

Very good. I was hoping that someone would implemented it soon ! Thanks a lot.

I will have a look at it. (And add more documentation to it : You normalised the height to be independent of the base field, which is one of the two possible normalisations, and it should be documented)



---

archive/issue_comments_076532.json:
```json
{
    "body": "Excellent -- I will look at it too.  I have implemented this more than once, so know the algorithm well.\n\nAny reason not to use ticket #360 which has been patiently waiting for 3 years?",
    "created_at": "2010-03-11T10:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76532",
    "user": "https://github.com/JohnCremona"
}
```

Excellent -- I will look at it too.  I have implemented this more than once, so know the algorithm well.

Any reason not to use ticket #360 which has been patiently waiting for 3 years?



---

archive/issue_comments_076533.json:
```json
{
    "body": "The patch did not apply to 4.3.4.alpha1.\n\n`Hunk #4 FAILED at 1687`\n\nA rebase is needed.",
    "created_at": "2010-03-11T10:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76533",
    "user": "https://github.com/categorie"
}
```

The patch did not apply to 4.3.4.alpha1.

`Hunk #4 FAILED at 1687`

A rebase is needed.



---

archive/issue_comments_076534.json:
```json
{
    "body": "Hmm... #360 looks like it's also about implementing height bounds as well, which I also plan to do if no one beats me to it, but don't want to wait up to get this in. \n\nI'll have to get ahold of an alpha to try and rebase it (and document the normalization choice).",
    "created_at": "2010-03-11T18:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76534",
    "user": "https://github.com/robertwb"
}
```

Hmm... #360 looks like it's also about implementing height bounds as well, which I also plan to do if no one beats me to it, but don't want to wait up to get this in. 

I'll have to get ahold of an alpha to try and rebase it (and document the normalization choice).



---

archive/issue_comments_076535.json:
```json
{
    "body": "I noticed in the docstrings that you specify INPUT variables like this:\n\n```\n        1824         INPUT:: \n        1825\t            v - a non-archimedean place of the base field of the curve, \n \t1826\t                or None, in which case the total nonarchimedian contribution \n \t1827\t                is returned \n \t1828\t         \n \t1829\t            prec - working precision, or None in which case the height  \n \t1830\t                is returned symbolically \n```\n\nI don't think this is so nice in Sphinx, since it is just preformated.  The vast majority of docstrings are formatted like as a list:\n\n```\n        1824            INPUT:\n        1825\t            - ``v`` - a non-archimedean place of the base field of the curve, \n \t1826\t              or None, in which case the total nonarchimedian contribution \n \t1827\t              is returned \n \t1828\t         \n \t1829\t            - ``prec`` - working precision, or None in which case the height  \n \t1830\t              is returned symbolically \n```\n\nNote that:\n   \n* only one colon after \"INPUT\"\n* a dash at the start of each line\n* the indentation is two spaces after the dash.",
    "created_at": "2010-03-12T01:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76535",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_076536.json:
```json
{
    "body": "Changing assignee from @JohnCremona to @williamstein.",
    "created_at": "2010-03-12T01:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76536",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from @JohnCremona to @williamstein.



---

archive/issue_comments_076537.json:
```json
{
    "body": "Is there a reason the 0 is returned in QQ ?\n\nI will later modify this, because I will need the exp() of the local heights for non-archimedean primes as an element in QQ, if I want to implement the p-adic heights over number fields.",
    "created_at": "2010-03-12T09:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76537",
    "user": "https://github.com/categorie"
}
```

Is there a reason the 0 is returned in QQ ?

I will later modify this, because I will need the exp() of the local heights for non-archimedean primes as an element in QQ, if I want to implement the p-adic heights over number fields.



---

archive/issue_comments_076538.json:
```json
{
    "body": "Replying to [comment:7 wuthrich]:\n> Is there a reason the 0 is returned in QQ ?\n\n\nFor consistency with the original code, and for speed (not that it should matter much). \n\n> I will later modify this, because I will need the exp() of the local heights for non-archimedean primes as an element in QQ, if I want to implement the p-adic heights over number fields.\n\n\nYou can do exp of an element of QQ just fine.",
    "created_at": "2010-03-12T10:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76538",
    "user": "https://github.com/robertwb"
}
```

Replying to [comment:7 wuthrich]:
> Is there a reason the 0 is returned in QQ ?


For consistency with the original code, and for speed (not that it should matter much). 

> I will later modify this, because I will need the exp() of the local heights for non-archimedean primes as an element in QQ, if I want to implement the p-adic heights over number fields.


You can do exp of an element of QQ just fine.



---

archive/issue_comments_076539.json:
```json
{
    "body": "Replying to [comment:8 robertwb]:\n> You can do exp of an element of QQ just fine. \n\n\nSure, that is not what I meant. I will put all your code of `nonarchimedian_local_height` into a helper function that returns r and Nv and then the main function will only take log. So that in the p-adic case I can take p-adic logs of the rational Nv.\n\nBut don't worry I will do that when I will implement p-adic height. It was only to remind myself that I should do that.",
    "created_at": "2010-03-12T10:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76539",
    "user": "https://github.com/categorie"
}
```

Replying to [comment:8 robertwb]:
> You can do exp of an element of QQ just fine. 


Sure, that is not what I meant. I will put all your code of `nonarchimedian_local_height` into a helper function that returns r and Nv and then the main function will only take log. So that in the p-adic case I can take p-adic logs of the rational Nv.

But don't worry I will do that when I will implement p-adic height. It was only to remind myself that I should do that.



---

archive/issue_comments_076540.json:
```json
{
    "body": "The code looks ok to me (I spotted one mis-spelling of Silverman!), and I checked that the results agree with magma, but I'll leave the formal review to Chris who has started and wants to add to the documentation.",
    "created_at": "2010-03-13T15:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76540",
    "user": "https://github.com/JohnCremona"
}
```

The code looks ok to me (I spotted one mis-spelling of Silverman!), and I checked that the results agree with magma, but I'll leave the formal review to Chris who has started and wants to add to the documentation.



---

archive/issue_comments_076541.json:
```json
{
    "body": "exported against 4.3.4.alpha1",
    "created_at": "2010-03-15T15:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76541",
    "user": "https://github.com/categorie"
}
```

exported against 4.3.4.alpha1



---

archive/issue_comments_076542.json:
```json
{
    "body": "Attachment [trac_8496_rebased.patch](tarball://root/attachments/some-uuid/ticket8496/trac_8496_rebased.patch) by @categorie created at 2010-03-15 15:30:01\n\nI have put up a rebased patch with a few minor changes. But I have not included yet the documentation on the normalization. You write \"THE BSD formula\", but there is not a unique standard way of stating the conjecture, I fear. Also the question is whether or not you divide the height pairing by two or not. Could you clarify this ?\n\nI deleted the assumption that E was defined over Q. I don't think you will need that. Maybe it is needed that the model is integral, but I do not see where you would require the curve to be defined over Q. Please correct me if I am wrong.\n\nBy the way the diff of our two patches comes mainly from converting tabs to spaces.",
    "created_at": "2010-03-15T15:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76542",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_8496_rebased.patch](tarball://root/attachments/some-uuid/ticket8496/trac_8496_rebased.patch) by @categorie created at 2010-03-15 15:30:01

I have put up a rebased patch with a few minor changes. But I have not included yet the documentation on the normalization. You write "THE BSD formula", but there is not a unique standard way of stating the conjecture, I fear. Also the question is whether or not you divide the height pairing by two or not. Could you clarify this ?

I deleted the assumption that E was defined over Q. I don't think you will need that. Maybe it is needed that the model is integral, but I do not see where you would require the curve to be defined over Q. Please correct me if I am wrong.

By the way the diff of our two patches comes mainly from converting tabs to spaces.



---

archive/issue_comments_076543.json:
```json
{
    "body": "Replying to [comment:11 wuthrich]:\n> I have put up a rebased patch with a few minor changes. But I have not included yet the documentation on the normalization. You write \"THE BSD formula\", but there is not a unique standard way of stating the conjecture, I fear. Also the question is whether or not you divide the height pairing by two or not. Could you clarify this ?\n\n\nOK, I have expanded the normalization section, borrowing heavily from the explanation found in John Cremona's book. \n\n> I deleted the assumption that E was defined over Q. I don't think you will need that. Maybe it is needed that the model is integral, but I do not see where you would require the curve to be defined over Q. Please correct me if I am wrong.\n\n\nYes, you are correct. (There are examples to this effect.) \n\n> By the way the diff of our two patches comes mainly from converting tabs to spaces.\n\n\nThey were not of my doing, but thanks for expunging them.",
    "created_at": "2010-03-15T19:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76543",
    "user": "https://github.com/robertwb"
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

archive/issue_comments_076544.json:
```json
{
    "body": "Rebased and updated, apply only this patch.",
    "created_at": "2010-03-15T19:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76544",
    "user": "https://github.com/robertwb"
}
```

Rebased and updated, apply only this patch.



---

archive/issue_comments_076545.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-15T20:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76545",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076546.json:
```json
{
    "body": "Attachment [8496-nf-height-again.patch](tarball://root/attachments/some-uuid/ticket8496/8496-nf-height-again.patch) by @JohnCremona created at 2010-03-15 20:33:06\n\nNew patch applies fine to 4.3.4.alpha1, and all tests in sage/schemes/elliptic_curves pass (tested both 32 and 64 bit).  Good!",
    "created_at": "2010-03-15T20:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76546",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [8496-nf-height-again.patch](tarball://root/attachments/some-uuid/ticket8496/8496-nf-height-again.patch) by @JohnCremona created at 2010-03-15 20:33:06

New patch applies fine to 4.3.4.alpha1, and all tests in sage/schemes/elliptic_curves pass (tested both 32 and 64 bit).  Good!



---

archive/issue_comments_076547.json:
```json
{
    "body": "This doesn't apply cleanly to Sage 4.4.alpha0; apparently it conflicts with a patch merged into that.  Please rebase it, and we'll try hard to get it into 4.4.alpha1.",
    "created_at": "2010-04-17T04:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76547",
    "user": "https://github.com/jhpalmieri"
}
```

This doesn't apply cleanly to Sage 4.4.alpha0; apparently it conflicts with a patch merged into that.  Please rebase it, and we'll try hard to get it into 4.4.alpha1.



---

archive/issue_comments_076548.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-17T04:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76548",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076549.json:
```json
{
    "body": "Attachment [8496-rebased-4.4.alpha0.patch](tarball://root/attachments/some-uuid/ticket8496/8496-rebased-4.4.alpha0.patch) by @robertwb created at 2010-04-17 19:28:44",
    "created_at": "2010-04-17T19:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76549",
    "user": "https://github.com/robertwb"
}
```

Attachment [8496-rebased-4.4.alpha0.patch](tarball://root/attachments/some-uuid/ticket8496/8496-rebased-4.4.alpha0.patch) by @robertwb created at 2010-04-17 19:28:44



---

archive/issue_comments_076550.json:
```json
{
    "body": "OK, rebased. It looks like it was just deleting some tabs that someone else also deleted, which was easy to fix.",
    "created_at": "2010-04-17T19:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76550",
    "user": "https://github.com/robertwb"
}
```

OK, rebased. It looks like it was just deleting some tabs that someone else also deleted, which was easy to fix.



---

archive/issue_comments_076551.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-17T19:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76551",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076552.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-17T19:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76552",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076553.json:
```json
{
    "body": "I'm remarking this as positive review as there was no content change in the rebase.",
    "created_at": "2010-04-17T19:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76553",
    "user": "https://github.com/robertwb"
}
```

I'm remarking this as positive review as there was no content change in the rebase.



---

archive/issue_comments_076554.json:
```json
{
    "body": "Merged \"8496-rebased-4.4.alpha0.patch\" into 4.4.alpha1.",
    "created_at": "2010-04-19T05:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76554",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "8496-rebased-4.4.alpha0.patch" into 4.4.alpha1.



---

archive/issue_events_020401.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-19T05:16:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8496#event-20401"
}
```



---

archive/issue_comments_076555.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8496#issuecomment-76555",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
