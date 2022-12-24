# Issue 7271: some small polybori interface fixes

archive/issues_007271.json:
```json
{
    "body": "Assignee: malb\n\nCC:  burcin polybori drkirkby\n\nKeywords: polybori, crypto\n\n* implement var()\n  * variables() is an iterator\n\nIssue created by migration from https://trac.sagemath.org/ticket/7271\n\n",
    "created_at": "2009-10-23T16:41:21Z",
    "labels": [
        "commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "some small polybori interface fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7271",
    "user": "malb"
}
```
Assignee: malb

CC:  burcin polybori drkirkby

Keywords: polybori, crypto

* implement var()
  * variables() is an iterator

Issue created by migration from https://trac.sagemath.org/ticket/7271





---

archive/issue_comments_060475.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-23T16:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60475",
    "user": "malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060476.json:
```json
{
    "body": "Why does variables() return an iterator?  It returns a tuple for pretty much everything else in Sage.  See #7077",
    "created_at": "2009-10-23T17:49:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60476",
    "user": "mhansen"
}
```

Why does variables() return an iterator?  It returns a tuple for pretty much everything else in Sage.  See #7077



---

archive/issue_comments_060477.json:
```json
{
    "body": "Because that's what PolyBoRi expects internally.",
    "created_at": "2009-10-23T18:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60477",
    "user": "malb"
}
```

Because that's what PolyBoRi expects internally.



---

archive/issue_comments_060478.json:
```json
{
    "body": "Can you explain in a bit more detail?  How is PolyBoRi using that method?",
    "created_at": "2009-10-23T18:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60478",
    "user": "mhansen"
}
```

Can you explain in a bit more detail?  How is PolyBoRi using that method?



---

archive/issue_comments_060479.json:
```json
{
    "body": "Hi Mike, sorry for being so brief earlier, I was in a rush.\n\nPolyBoRi calls this function from various functions which are called by the `groebner_basis` function. The ones I could find quickly are:\n\n\n```\npolybori-0.6/pyroot/polybori/rank.py:    return p.lex_lead().variables().next()\npolybori-0.6/pyroot/polybori/ll.py:      return Monomial(v).variables().next().index()\npolybori-0.6/testsuite/py/parsegat.py:    return p.lead().variables().next()\n```\n\n\nAs you can see, it calls next() immediatly on the result of `variables()`. Right now, certain GB computations will fail with an `AttributeError` because of this.",
    "created_at": "2009-10-23T22:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60479",
    "user": "malb"
}
```

Hi Mike, sorry for being so brief earlier, I was in a rush.

PolyBoRi calls this function from various functions which are called by the `groebner_basis` function. The ones I could find quickly are:


```
polybori-0.6/pyroot/polybori/rank.py:    return p.lex_lead().variables().next()
polybori-0.6/pyroot/polybori/ll.py:      return Monomial(v).variables().next().index()
polybori-0.6/testsuite/py/parsegat.py:    return p.lead().variables().next()
```


As you can see, it calls next() immediatly on the result of `variables()`. Right now, certain GB computations will fail with an `AttributeError` because of this.



---

archive/issue_comments_060480.json:
```json
{
    "body": "I just received word that this will be changed in PolyBoRi.",
    "created_at": "2009-10-23T22:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60480",
    "user": "malb"
}
```

I just received word that this will be changed in PolyBoRi.



---

archive/issue_comments_060481.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-26T07:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60481",
    "user": "PolyBoRi"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060482.json:
```json
{
    "body": "http://bitbucket.org/brickenstein/polybori/changeset/48fab65072e9/\n\nhttp://bitbucket.org/brickenstein/polybori/changeset/e238ae62b9e6/\n\nRegarding parsegat, as you can see, I moved a corrected version between our repositories (similar one-liner). But there is no dependency on parsegat.py .\nThe only funny thing about the recent versions of parsegat.py is that, you\ncan see a poor mathetician trying to recognize patterns from bad encoded circuits.\nI still have nightmares from it.",
    "created_at": "2009-10-26T07:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60482",
    "user": "PolyBoRi"
}
```

http://bitbucket.org/brickenstein/polybori/changeset/48fab65072e9/

http://bitbucket.org/brickenstein/polybori/changeset/e238ae62b9e6/

Regarding parsegat, as you can see, I moved a corrected version between our repositories (similar one-liner). But there is no dependency on parsegat.py .
The only funny thing about the recent versions of parsegat.py is that, you
can see a poor mathetician trying to recognize patterns from bad encoded circuits.
I still have nightmares from it.



---

archive/issue_comments_060483.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-28T16:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60483",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060484.json:
```json
{
    "body": "I prepared a new SPKG and a new patch.\n\nThe SPKG is available at:\n\n  http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.3.r1647-20091028.spkg",
    "created_at": "2009-10-28T16:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60484",
    "user": "malb"
}
```

I prepared a new SPKG and a new patch.

The SPKG is available at:

  http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.3.r1647-20091028.spkg



---

archive/issue_comments_060485.json:
```json
{
    "body": "Attachment [polybori_fixes.patch](tarball://root/attachments/some-uuid/ticket7271/polybori_fixes.patch) by malb created at 2009-10-28 16:28:09",
    "created_at": "2009-10-28T16:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60485",
    "user": "malb"
}
```

Attachment [polybori_fixes.patch](tarball://root/attachments/some-uuid/ticket7271/polybori_fixes.patch) by malb created at 2009-10-28 16:28:09



---

archive/issue_comments_060486.json:
```json
{
    "body": "Mike, I reversed the iterator change in the latest patch. Can you review it?",
    "created_at": "2009-10-28T16:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60486",
    "user": "malb"
}
```

Mike, I reversed the iterator change in the latest patch. Can you review it?



---

archive/issue_comments_060487.json:
```json
{
    "body": "I am attaching a new deps file to this ticket, to address \n\n   http://groups.google.com/group/sage-devel/browse_thread/thread/122f067d8947148d/",
    "created_at": "2009-11-02T10:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60487",
    "user": "malb"
}
```

I am attaching a new deps file to this ticket, to address 

   http://groups.google.com/group/sage-devel/browse_thread/thread/122f067d8947148d/



---

archive/issue_comments_060488.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket7271/deps) by malb created at 2009-11-02 10:43:07\n\nThe only thing changed in the deps file (which isn't under revision control) is that PolyBoRi now depends on M4RI",
    "created_at": "2009-11-02T10:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60488",
    "user": "malb"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket7271/deps) by malb created at 2009-11-02 10:43:07

The only thing changed in the deps file (which isn't under revision control) is that PolyBoRi now depends on M4RI



---

archive/issue_comments_060489.json:
```json
{
    "body": "There are several issues I am aware of with m4ri, which should perhaps be sorted out before code is added that depends on it. \n\n#7171 - Although reported against HP-UX, this is more serious, as it is broken on Solaris too. \n#7037 - libm4ri thinks the C compiler is broken\n\nI beleive the current version of PolyBoRi might actually build with Sun's compiler, but this would stop that, if it has a dependancy which does not.",
    "created_at": "2009-11-18T15:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60489",
    "user": "drkirkby"
}
```

There are several issues I am aware of with m4ri, which should perhaps be sorted out before code is added that depends on it. 

#7171 - Although reported against HP-UX, this is more serious, as it is broken on Solaris too. 
#7037 - libm4ri thinks the C compiler is broken

I beleive the current version of PolyBoRi might actually build with Sun's compiler, but this would stop that, if it has a dependancy which does not.



---

archive/issue_comments_060490.json:
```json
{
    "body": "Oops, for some reason I was not aware of this ticket despite being CCed on it. Nor of #7375, which aims to address the issues in M4RI, so my comments are probably out of place. I will look at #7375 soon, but would be unable to review this ticket. \n\nDave",
    "created_at": "2009-11-18T15:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60490",
    "user": "drkirkby"
}
```

Oops, for some reason I was not aware of this ticket despite being CCed on it. Nor of #7375, which aims to address the issues in M4RI, so my comments are probably out of place. I will look at #7375 soon, but would be unable to review this ticket. 

Dave



---

archive/issue_comments_060491.json:
```json
{
    "body": "Hi, I was wondering if I someone could review this ticket now that the M4RI issues are resolved?",
    "created_at": "2009-12-03T14:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60491",
    "user": "malb"
}
```

Hi, I was wondering if I someone could review this ticket now that the M4RI issues are resolved?



---

archive/issue_comments_060492.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-07T08:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60492",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060493.json:
```json
{
    "body": "The patch looks good.  I'll add it first thing after 4.3, which should hopefully be out in the next day or two.",
    "created_at": "2009-12-07T08:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60493",
    "user": "mhansen"
}
```

The patch looks good.  I'll add it first thing after 4.3, which should hopefully be out in the next day or two.



---

archive/issue_comments_060494.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T03:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7271#issuecomment-60494",
    "user": "mhansen"
}
```

Resolution: fixed
