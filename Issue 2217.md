# Issue 2217: splitting field function for number fields

archive/issues_002217.json:
```json
{
    "body": "Assignee: was\n\nCC:  abrochard\n\n\n```\nI agree that this would be a useful funtion to have.  I would call it\nsplitting_field() with a description similar to that of root_field() \n\n...\n\nIn the meantim you should be able to work with what is available as follows:\n\nsage: QQx.<x>=QQ[]\nsage: f=(x^2-2)*(x^2-3)\nsage: F=NumberField([p for p,n in f.factor()],'a')\nsage: F2=F.absolute_field('b')\nsage: F2.structure()\n\n(Isomorphism from Number Field in b with defining polynomial x^4 -\n10*x^2 + 1 to Number Field in a0 with defining polynomial x^2 - 3 over\nits base field,\n Isomorphism from Number Field in a0 with defining polynomial x^2 - 3\nover its base field to Number Field in b with defining polynomial x^4\n- 10*x^2 + 1)\n\nHere F is first defined as a relative extension, with generators a0,a1\nsatisfying the equations:\n\nsage: a0,a1=F.gens()\nsage: a0^2, a1^2\n(3, 2)\n\nthen F2 is the associated absolute field, with F2.structure() giving\nmaps from each of these into the other.\n\nsage: F2toF, FtoF2=F2.structure()\nsage: FtoF2(a0)\n-1/2*b^3 + 11/2*b\nsage: FtoF2(a0).minpoly()\nx^2 - 3\nsage: FtoF2(a1)\n-1/2*b^3 + 9/2*b\nsage: FtoF2(a1).minpoly()\nx^2 - 2\n\n\n```\n\n\nSee the thread at http://groups.google.com/group/sage-devel/browse_thread/thread/32fe12de12d5f6a5/c91753b5e65fe7b9#c91753b5e65fe7b9\n\nIssue created by migration from https://trac.sagemath.org/ticket/2217\n\n",
    "created_at": "2008-02-20T03:50:21Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.1",
    "title": "splitting field function for number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2217",
    "user": "jason"
}
```
Assignee: was

CC:  abrochard


```
I agree that this would be a useful funtion to have.  I would call it
splitting_field() with a description similar to that of root_field() 

...

In the meantim you should be able to work with what is available as follows:

sage: QQx.<x>=QQ[]
sage: f=(x^2-2)*(x^2-3)
sage: F=NumberField([p for p,n in f.factor()],'a')
sage: F2=F.absolute_field('b')
sage: F2.structure()

(Isomorphism from Number Field in b with defining polynomial x^4 -
10*x^2 + 1 to Number Field in a0 with defining polynomial x^2 - 3 over
its base field,
 Isomorphism from Number Field in a0 with defining polynomial x^2 - 3
over its base field to Number Field in b with defining polynomial x^4
- 10*x^2 + 1)

Here F is first defined as a relative extension, with generators a0,a1
satisfying the equations:

sage: a0,a1=F.gens()
sage: a0^2, a1^2
(3, 2)

then F2 is the associated absolute field, with F2.structure() giving
maps from each of these into the other.

sage: F2toF, FtoF2=F2.structure()
sage: FtoF2(a0)
-1/2*b^3 + 11/2*b
sage: FtoF2(a0).minpoly()
x^2 - 3
sage: FtoF2(a1)
-1/2*b^3 + 9/2*b
sage: FtoF2(a1).minpoly()
x^2 - 2


```


See the thread at http://groups.google.com/group/sage-devel/browse_thread/thread/32fe12de12d5f6a5/c91753b5e65fe7b9#c91753b5e65fe7b9

Issue created by migration from https://trac.sagemath.org/ticket/2217





---

archive/issue_comments_014659.json:
```json
{
    "body": "Note that this approach does not give the splitting field.  It gives a field containing at least one root of each factor of the original polynomial, but that still might not be the splitting field.\n\nLater in the thread mentioned above, I give a technique using internals of qqbar which I believe does give the splitting field (perhaps inefficiently).",
    "created_at": "2008-02-21T03:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14659",
    "user": "cwitty"
}
```

Note that this approach does not give the splitting field.  It gives a field containing at least one root of each factor of the original polynomial, but that still might not be the splitting field.

Later in the thread mentioned above, I give a technique using internals of qqbar which I believe does give the splitting field (perhaps inefficiently).



---

archive/issue_comments_014660.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-20T19:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14660",
    "user": "davidloeffler"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_014661.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-20T19:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14661",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_014662.json:
```json
{
    "body": "Add splitting_field() function",
    "created_at": "2011-11-10T16:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14662",
    "user": "jdemeyer"
}
```

Add splitting_field() function



---

archive/issue_comments_014663.json:
```json
{
    "body": "Attachment [2217_splitting_field.patch](tarball://root/attachments/some-uuid/ticket2217/2217_splitting_field.patch) by abrochard created at 2012-08-18 17:52:00",
    "created_at": "2012-08-18T17:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14663",
    "user": "abrochard"
}
```

Attachment [2217_splitting_field.patch](tarball://root/attachments/some-uuid/ticket2217/2217_splitting_field.patch) by abrochard created at 2012-08-18 17:52:00



---

archive/issue_comments_014664.json:
```json
{
    "body": "Jeroen, what is the status of the patch here?",
    "created_at": "2012-09-17T05:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14664",
    "user": "roed"
}
```

Jeroen, what is the status of the patch here?



---

archive/issue_comments_014665.json:
```json
{
    "body": "I totally forgot about this.  I might be good to revisit this.",
    "created_at": "2012-09-17T06:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14665",
    "user": "jdemeyer"
}
```

I totally forgot about this.  I might be good to revisit this.



---

archive/issue_comments_014666.json:
```json
{
    "body": "I originally had plans for some speed-ups, but since the code works fine, I guess it can be reviewed.",
    "created_at": "2012-09-17T06:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14666",
    "user": "jdemeyer"
}
```

I originally had plans for some speed-ups, but since the code works fine, I guess it can be reviewed.



---

archive/issue_comments_014667.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-09-17T06:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14667",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_014668.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-03-01T04:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14668",
    "user": "mmanes"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_014669.json:
```json
{
    "body": "I ran all standard tests, and everything passed.\n\nI was trying to test functionality, but I'm confused by the differences file.  All of the old examples seem to work, and none of the new ones work.\n\nIn the first example, I get:\n\n\n\n```\nsage: G = NumberField(x^3 - x - 1,'a').galois_closure('b').galois_group(); G\n\nGalois group of Number Field in b with defining polynomial x^6 - 14*x^4\n+ 20*x^3 + 49*x^2 - 140*x + 307\n```\n\n\n\nThe expected output seems to have been changed *from* this result to \n\n\n\n```\nNumber Field in b with defining polynomial x^6 - 6*x^4 + 9*x^2 + 23 \n```\n\n\n\nThese fields are isomorphic, but I've tried the example on three machines, and all of them give the first thing as the output.\n\nSimilarly, the second example doesn't work:\n\n\n\n```\nsage: G.subgroup([ G(1), G([(1,2,3),(4,5,6)]), G([(1,3,2),(4,6,5)]) ]) \n\nTraceback (click to the left of this block for traceback)\n...\nTypeError: permutation [(1, 2, 3), (4, 5, 6)] not in Galois group of\nNumber Field in b with defining polynomial x^6 - 14*x^4 + 20*x^3 +\n49*x^2 - 140*x + 307\n\n```\n\n\nBut the original example (now deleted) does work:\n\n\n\n```\nsage: G.subgroup([ G(1), G([(1,5,2),(3,4,6)]), G([(1,2,5),(3,6,4)])])\n\nSubgroup [(), (1,5,2)(3,4,6), (1,2,5)(3,6,4)] of Galois group of Number\nField in b with defining polynomial x^6 - 14*x^4 + 20*x^3 + 49*x^2 -\n140*x + 307\n\n```\n",
    "created_at": "2013-03-01T04:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14669",
    "user": "mmanes"
}
```

I ran all standard tests, and everything passed.

I was trying to test functionality, but I'm confused by the differences file.  All of the old examples seem to work, and none of the new ones work.

In the first example, I get:



```
sage: G = NumberField(x^3 - x - 1,'a').galois_closure('b').galois_group(); G

Galois group of Number Field in b with defining polynomial x^6 - 14*x^4
+ 20*x^3 + 49*x^2 - 140*x + 307
```



The expected output seems to have been changed *from* this result to 



```
Number Field in b with defining polynomial x^6 - 6*x^4 + 9*x^2 + 23 
```



These fields are isomorphic, but I've tried the example on three machines, and all of them give the first thing as the output.

Similarly, the second example doesn't work:



```
sage: G.subgroup([ G(1), G([(1,2,3),(4,5,6)]), G([(1,3,2),(4,6,5)]) ]) 

Traceback (click to the left of this block for traceback)
...
TypeError: permutation [(1, 2, 3), (4, 5, 6)] not in Galois group of
Number Field in b with defining polynomial x^6 - 14*x^4 + 20*x^3 +
49*x^2 - 140*x + 307

```


But the original example (now deleted) does work:



```
sage: G.subgroup([ G(1), G([(1,5,2),(3,4,6)]), G([(1,2,5),(3,6,4)])])

Subgroup [(), (1,5,2)(3,4,6), (1,2,5)(3,6,4)] of Galois group of Number
Field in b with defining polynomial x^6 - 14*x^4 + 20*x^3 + 49*x^2 -
140*x + 307

```




---

archive/issue_comments_014670.json:
```json
{
    "body": "Attachment [trac_2217_correction.patch](tarball://root/attachments/some-uuid/ticket2217/trac_2217_correction.patch) by chapoton created at 2013-08-04 19:46:23\n\nhere is a patch to correct the failing doctest\n\nlet us see if the bot is happy\n\napply 2217_splitting_field.patch\u200b trac_2217_correction.patch\u200b",
    "created_at": "2013-08-04T19:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14670",
    "user": "chapoton"
}
```

Attachment [trac_2217_correction.patch](tarball://root/attachments/some-uuid/ticket2217/trac_2217_correction.patch) by chapoton created at 2013-08-04 19:46:23

here is a patch to correct the failing doctest

let us see if the bot is happy

apply 2217_splitting_field.patch​ trac_2217_correction.patch​



---

archive/issue_comments_014671.json:
```json
{
    "body": "ok, the bot is happy. Now the ticket needs review.",
    "created_at": "2013-08-21T09:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14671",
    "user": "chapoton"
}
```

ok, the bot is happy. Now the ticket needs review.



---

archive/issue_comments_014672.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-08-21T09:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14672",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_014673.json:
```json
{
    "body": "I am about to test and review this, which will also involve converting the patches to a git branch.  And rebasing, since the patches do not apply cleanly to the develop branch \n(6.1.beta2).",
    "created_at": "2013-12-31T09:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14673",
    "user": "cremona"
}
```

I am about to test and review this, which will also involve converting the patches to a git branch.  And rebasing, since the patches do not apply cleanly to the develop branch 
(6.1.beta2).



---

archive/issue_comments_014674.json:
```json
{
    "body": "Hang on John, I was planning to do that and make some simplifications also.",
    "created_at": "2013-12-31T10:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14674",
    "user": "jdemeyer"
}
```

Hang on John, I was planning to do that and make some simplifications also.



---

archive/issue_comments_014675.json:
```json
{
    "body": "Replying to [comment:14 jdemeyer]:\n> Hang on John, I was planning to do that and make some simplifications also.\n\nI did not see this comment until after I had finished, so I may have been wasting my time.  I had to apply the changes manually since I could not get the patches to apply.  Shall I still upload my new branch?  I have a commit which includes both the patches and passes all tests -- but have not yet started the real review process, i.e. reading the code.",
    "created_at": "2013-12-31T10:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14675",
    "user": "cremona"
}
```

Replying to [comment:14 jdemeyer]:
> Hang on John, I was planning to do that and make some simplifications also.

I did not see this comment until after I had finished, so I may have been wasting my time.  I had to apply the changes manually since I could not get the patches to apply.  Shall I still upload my new branch?  I have a commit which includes both the patches and passes all tests -- but have not yet started the real review process, i.e. reading the code.



---

archive/issue_comments_014676.json:
```json
{
    "body": "Replying to [comment:15 cremona]:\n> Shal I still upload by new branch?\nOf course you should. My point was mainly that I wanted to make some changes to my patch, so you should wait to review it.",
    "created_at": "2013-12-31T10:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14676",
    "user": "jdemeyer"
}
```

Replying to [comment:15 cremona]:
> Shal I still upload by new branch?
Of course you should. My point was mainly that I wanted to make some changes to my patch, so you should wait to review it.



---

archive/issue_comments_014677.json:
```json
{
    "body": "New commits:",
    "created_at": "2013-12-31T10:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14677",
    "user": "cremona"
}
```

New commits:



---

archive/issue_comments_014678.json:
```json
{
    "body": "OK, so here is a branch which implements your two patches.  I will not do any more until asked, and hope that this will save you effort!  I also hope that this will not hide your genuine authorship of the new code.",
    "created_at": "2013-12-31T10:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14678",
    "user": "cremona"
}
```

OK, so here is a branch which implements your two patches.  I will not do any more until asked, and hope that this will save you effort!  I also hope that this will not hide your genuine authorship of the new code.



---

archive/issue_comments_014679.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-01-02T11:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14679",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_014680.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-01-02T23:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14680",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_014681.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-01-02T23:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14681",
    "user": "jdemeyer"
}
```

New commits:



---

archive/issue_comments_014682.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-01-02T23:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14682",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_014683.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-01-02T23:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14683",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_014684.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-01-02T23:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14684",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_014685.json:
```json
{
    "body": "I am looking at your new commits.  At first I assumed that your commits were based on mine uploaded earlier, but when pulling yours on top of mine failed I guessed the truth.  This is of course fine -- except that some people might now argue otherwise:  during the time when my commit was attached to this ticket, it is possible that other people pulled it and based further work, new tickets etc, all on my unreviewed commit.  That would have been stupid of them, but some of the comments on the recent sage-devel thread make it clear that git purists would never so this.  I won't tell anyone if you do not! ;)",
    "created_at": "2014-01-03T09:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14685",
    "user": "cremona"
}
```

I am looking at your new commits.  At first I assumed that your commits were based on mine uploaded earlier, but when pulling yours on top of mine failed I guessed the truth.  This is of course fine -- except that some people might now argue otherwise:  during the time when my commit was attached to this ticket, it is possible that other people pulled it and based further work, new tickets etc, all on my unreviewed commit.  That would have been stupid of them, but some of the comments on the recent sage-devel thread make it clear that git purists would never so this.  I won't tell anyone if you do not! ;)



---

archive/issue_comments_014686.json:
```json
{
    "body": "Replying to [comment:26 cremona]:\n> during the time when my commit was attached to this ticket, it is possible that other people pulled it and based further work, new tickets etc, all on my unreviewed commit.\nI absolutely understand your point, but I think I indicated that this was work in progress so I felt it was safe to \"rewrite history\". Now that it's `needs_review`, I will no longer rewrite history.\n\nConcerning authorship: I did indeed reset the author name back to myself (`git commit --amend --author Demeyer`), and that's already rewriting history.",
    "created_at": "2014-01-03T09:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14686",
    "user": "jdemeyer"
}
```

Replying to [comment:26 cremona]:
> during the time when my commit was attached to this ticket, it is possible that other people pulled it and based further work, new tickets etc, all on my unreviewed commit.
I absolutely understand your point, but I think I indicated that this was work in progress so I felt it was safe to "rewrite history". Now that it's `needs_review`, I will no longer rewrite history.

Concerning authorship: I did indeed reset the author name back to myself (`git commit --amend --author Demeyer`), and that's already rewriting history.



---

archive/issue_comments_014687.json:
```json
{
    "body": "Understood.  I am happy (and quite impressed!) with the new code and am just testing, using the verbose option so I can see what is happening.",
    "created_at": "2014-01-03T09:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14687",
    "user": "cremona"
}
```

Understood.  I am happy (and quite impressed!) with the new code and am just testing, using the verbose option so I can see what is happening.



---

archive/issue_comments_014688.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-01-03T10:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14688",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_014689.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-01-03T10:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14689",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_014690.json:
```json
{
    "body": "Still needs-review or will you be making more commits?!",
    "created_at": "2014-01-03T10:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14690",
    "user": "cremona"
}
```

Still needs-review or will you be making more commits?!



---

archive/issue_comments_014691.json:
```json
{
    "body": "Code looks very good, and I am happy with the results of testing.  I have looked at the commits on branch u/jdemeyer/ticket/2217 up to commit c50eb3e...",
    "created_at": "2014-01-03T11:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14691",
    "user": "cremona"
}
```

Code looks very good, and I am happy with the results of testing.  I have looked at the commits on branch u/jdemeyer/ticket/2217 up to commit c50eb3e...



---

archive/issue_comments_014692.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-01-03T11:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14692",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_014693.json:
```json
{
    "body": "Thanks, I didn't expect such a quick review.\n\nAm I allowed to add more examples/doctests?",
    "created_at": "2014-01-03T11:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14693",
    "user": "jdemeyer"
}
```

Thanks, I didn't expect such a quick review.

Am I allowed to add more examples/doctests?



---

archive/issue_comments_014694.json:
```json
{
    "body": "Replying to [comment:33 jdemeyer]:\n> Thanks, I didn't expect such a quick review.\n> \n> Am I allowed to add more examples/doctests?\n\nOf course!  I think there are already a lot of examples, which I liked.  If you are going to make some more changes I would be happy to look at them, so I'll now mark the ticket as needs work, and when you are ready put it back to needs review.  While you are at it, the description of the class containing a pair (polynomial, degree multiple) is slightly confusing since it refers to other polynomials in the class, whereas you actually deal with lists of instances of these.\n\n\nI am currently working on another branch so the next review will not be so quick!",
    "created_at": "2014-01-03T11:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14694",
    "user": "cremona"
}
```

Replying to [comment:33 jdemeyer]:
> Thanks, I didn't expect such a quick review.
> 
> Am I allowed to add more examples/doctests?

Of course!  I think there are already a lot of examples, which I liked.  If you are going to make some more changes I would be happy to look at them, so I'll now mark the ticket as needs work, and when you are ready put it back to needs review.  While you are at it, the description of the class containing a pair (polynomial, degree multiple) is slightly confusing since it refers to other polynomials in the class, whereas you actually deal with lists of instances of these.


I am currently working on another branch so the next review will not be so quick!



---

archive/issue_comments_014695.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2014-01-03T11:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14695",
    "user": "cremona"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_014696.json:
```json
{
    "body": "Replying to [comment:34 cremona]:\n> I am currently working on another branch so the next review will not be so quick!\nIn that case, perhaps I prefer to leave this ticket and continue on a new ticket. Sorry for the mess.",
    "created_at": "2014-01-03T12:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14696",
    "user": "jdemeyer"
}
```

Replying to [comment:34 cremona]:
> I am currently working on another branch so the next review will not be so quick!
In that case, perhaps I prefer to leave this ticket and continue on a new ticket. Sorry for the mess.



---

archive/issue_comments_014697.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-01-03T12:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14697",
    "user": "jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_014698.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-01-05T02:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2217#issuecomment-14698",
    "user": "vbraun"
}
```

Resolution: fixed
