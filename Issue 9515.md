# Issue 9515: make an optional spkg for PyCryptoPlus

archive/issues_009515.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @mwhansen mvngu @williamstein\n\nSee\n\n\u00a0 http://wiki.yobi.be/wiki/PyCryptoPlus\n\nand\u00a0\n\n\u00a0 http://groups.google.com/group/sage-devel/browse_thread/thread/500063cfaa2961b0/\u00a0\n\nIssue created by migration from https://trac.sagemath.org/ticket/9515\n\n",
    "created_at": "2010-07-16T09:26:40Z",
    "labels": [
        "component: cryptography",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "make an optional spkg for PyCryptoPlus",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9515",
    "user": "https://github.com/malb"
}
```
Assignee: mvngu

CC:  @mwhansen mvngu @williamstein

See

  http://wiki.yobi.be/wiki/PyCryptoPlus

and 

  http://groups.google.com/group/sage-devel/browse_thread/thread/500063cfaa2961b0/ 

Issue created by migration from https://trac.sagemath.org/ticket/9515





---

archive/issue_comments_091327.json:
```json
{
    "body": "I've uploaded an SPKG to\n\nhttp://sage.math.washington.edu/home/malb/spkgs/pycryptoplus-20100809-git.spkg",
    "created_at": "2010-08-09T11:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9515#issuecomment-91327",
    "user": "https://github.com/malb"
}
```

I've uploaded an SPKG to

http://sage.math.washington.edu/home/malb/spkgs/pycryptoplus-20100809-git.spkg



---

archive/issue_comments_091328.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-09T11:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9515#issuecomment-91328",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091329.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n\nApplied find and passed sage -testall to 4.5.2.rc0 on a 10.6.4 mac. Testing on ubuntu now.",
    "created_at": "2010-08-09T13:57:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9515#issuecomment-91329",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:2 malb]:

Applied find and passed sage -testall to 4.5.2.rc0 on a 10.6.4 mac. Testing on ubuntu now.



---

archive/issue_comments_091330.json:
```json
{
    "body": "Replying to [comment:3 wdj]:\n> Replying to [comment:2 malb]:\n> \n> Applied find and passed sage -testall to 4.5.2.rc0 on a 10.6.4 mac. Testing on ubuntu now.\n\nApplied fine to 4.5.2 on 32bit ubuntu 10.04 and passed sage -testall.\n\nAre there other tests needed, such as solaris or cygwin?",
    "created_at": "2010-08-10T16:44:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9515#issuecomment-91330",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:3 wdj]:
> Replying to [comment:2 malb]:
> 
> Applied find and passed sage -testall to 4.5.2.rc0 on a 10.6.4 mac. Testing on ubuntu now.

Applied fine to 4.5.2 on 32bit ubuntu 10.04 and passed sage -testall.

Are there other tests needed, such as solaris or cygwin?



---

archive/issue_comments_091331.json:
```json
{
    "body": "Replying to [comment:4 wdj]:\n\n> Applied fine to 4.5.2 on 32bit ubuntu 10.04 and passed sage -testall. Are there other tests needed, such as solaris or cygwin?\n\nI doubt it, since (a) this is a pure Python package and (b) this is an optional SPKG anyway.",
    "created_at": "2010-08-10T17:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9515#issuecomment-91331",
    "user": "https://github.com/malb"
}
```

Replying to [comment:4 wdj]:

> Applied fine to 4.5.2 on 32bit ubuntu 10.04 and passed sage -testall. Are there other tests needed, such as solaris or cygwin?

I doubt it, since (a) this is a pure Python package and (b) this is an optional SPKG anyway.



---

archive/issue_comments_091332.json:
```json
{
    "body": "Replying to [comment:5 malb]:\n> Replying to [comment:4 wdj]:\n> \n> > Applied fine to 4.5.2 on 32bit ubuntu 10.04 and passed sage -testall. Are there other tests needed, such as solaris or cygwin?\n> \n> I doubt it, since (a) this is a pure Python package and (b) this is an optional SPKG anyway.\n\nI also checked that the SPKG.txt and\nspkg-install file follow the conventions in \nhttp://www.sagemath.org/doc/developer/producing_spkgs.html#creating-a-new-spkg\n\nI have emailed D Kirkby separately regarding the solaris issue. I'm\nabout to give this a positive review after hearing back from him.",
    "created_at": "2010-08-10T17:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9515#issuecomment-91332",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:5 malb]:
> Replying to [comment:4 wdj]:
> 
> > Applied fine to 4.5.2 on 32bit ubuntu 10.04 and passed sage -testall. Are there other tests needed, such as solaris or cygwin?
> 
> I doubt it, since (a) this is a pure Python package and (b) this is an optional SPKG anyway.

I also checked that the SPKG.txt and
spkg-install file follow the conventions in 
http://www.sagemath.org/doc/developer/producing_spkgs.html#creating-a-new-spkg

I have emailed D Kirkby separately regarding the solaris issue. I'm
about to give this a positive review after hearing back from him.



---

archive/issue_comments_091333.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-10T17:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9515#issuecomment-91333",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091334.json:
```json
{
    "body": "Replying to [comment:6 wdj]:\n\n> \n> I have emailed D Kirkby separately regarding the solaris issue. I'm\n> about to give this a positive review after hearing back from him.\n> \n\n\nDave Kirkby replied that the script will run on solaris as well.",
    "created_at": "2010-08-10T18:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9515#issuecomment-91334",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:6 wdj]:

> 
> I have emailed D Kirkby separately regarding the solaris issue. I'm
> about to give this a positive review after hearing back from him.
> 


Dave Kirkby replied that the script will run on solaris as well.



---

archive/issue_comments_091335.json:
```json
{
    "body": "I've updated the Author(s) and Reviewer(s) fields.  Please correct them, if I'm wrong.\n\nMike, Minh, or William, could one of you merge this package into the optional spkg repository?  I don't have the privileges to do this.",
    "created_at": "2010-08-14T23:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9515#issuecomment-91335",
    "user": "https://github.com/qed777"
}
```

I've updated the Author(s) and Reviewer(s) fields.  Please correct them, if I'm wrong.

Mike, Minh, or William, could one of you merge this package into the optional spkg repository?  I don't have the privileges to do this.



---

archive/issue_comments_091336.json:
```json
{
    "body": "Replying to [comment:8 mpatel]:\n> Mike, Minh, or William, could one of you merge this package into the optional spkg repository?  I don't have the privileges to do this.\n\nDone. See the updated page\n\nhttp://www.sagemath.org/packages/optional/",
    "created_at": "2010-08-15T04:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9515#issuecomment-91336",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:8 mpatel]:
> Mike, Minh, or William, could one of you merge this package into the optional spkg repository?  I don't have the privileges to do this.

Done. See the updated page

http://www.sagemath.org/packages/optional/



---

archive/issue_comments_091337.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-15T06:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9515#issuecomment-91337",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_091338.json:
```json
{
    "body": "Thank you, Minh.",
    "created_at": "2010-08-15T06:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9515#issuecomment-91338",
    "user": "https://github.com/qed777"
}
```

Thank you, Minh.
