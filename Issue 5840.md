# Issue 5840: update SageTeX spkg to version 2.0.2

archive/issues_005840.json:
```json
{
    "body": "Assignee: ddrake\n\nI've made a new spkg for SageTeX. It now has a proper Mercurial repository layout, improved spkg-check, documentation about TeXShop, and more examples.\n\nThe spkg is available from http://sage.math.washington.edu/home/drake/code/sage/st/sagetex-2.0.2.spkg.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5840\n\n",
    "created_at": "2009-04-21T04:16:23Z",
    "labels": [
        "packages: optional",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "update SageTeX spkg to version 2.0.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5840",
    "user": "ddrake"
}
```
Assignee: ddrake

I've made a new spkg for SageTeX. It now has a proper Mercurial repository layout, improved spkg-check, documentation about TeXShop, and more examples.

The spkg is available from http://sage.math.washington.edu/home/drake/code/sage/st/sagetex-2.0.2.spkg.

Issue created by migration from https://trac.sagemath.org/ticket/5840





---

archive/issue_comments_045915.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-21T04:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5840#issuecomment-45915",
    "user": "ddrake"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045916.json:
```json
{
    "body": "This looks good to me.  I installed and used it today too.",
    "created_at": "2009-05-06T03:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5840#issuecomment-45916",
    "user": "jason"
}
```

This looks good to me.  I installed and used it today too.



---

archive/issue_comments_045917.json:
```json
{
    "body": "Okay, there's a yet newer version that I'd prefer get reviewed -- it has a \"pause/unpause\" feature that the author of TeXShop requested. The new spkg is: http://sage.math.washington.edu/home/drake/code/sage/st/sagetex-2.1.1.spkg. Changing this back to \"needs review\"...sorry Jason. :)",
    "created_at": "2009-05-15T06:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5840#issuecomment-45917",
    "user": "ddrake"
}
```

Okay, there's a yet newer version that I'd prefer get reviewed -- it has a "pause/unpause" feature that the author of TeXShop requested. The new spkg is: http://sage.math.washington.edu/home/drake/code/sage/st/sagetex-2.1.1.spkg. Changing this back to "needs review"...sorry Jason. :)



---

archive/issue_comments_045918.json:
```json
{
    "body": "This looks great.  The one nitpicky detail that needs to be fixed (and then this is a positive review) is that the changelog inside of SPKG.txt does not mention the update to 2.1.1.  When that is fixed, change this to positive review.\n\nGreat work!",
    "created_at": "2009-05-28T06:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5840#issuecomment-45918",
    "user": "jason"
}
```

This looks great.  The one nitpicky detail that needs to be fixed (and then this is a positive review) is that the changelog inside of SPKG.txt does not mention the update to 2.1.1.  When that is fixed, change this to positive review.

Great work!



---

archive/issue_comments_045919.json:
```json
{
    "body": "I updated SPKG.txt as requested. It feels slightly illicit to change my own ticket to \"positive review\", but Jason said so... :)",
    "created_at": "2009-05-28T08:21:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5840#issuecomment-45919",
    "user": "ddrake"
}
```

I updated SPKG.txt as requested. It feels slightly illicit to change my own ticket to "positive review", but Jason said so... :)



---

archive/issue_comments_045920.json:
```json
{
    "body": "Do we include a sagetex spkg currently?",
    "created_at": "2009-06-01T00:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5840#issuecomment-45920",
    "user": "mhansen"
}
```

Do we include a sagetex spkg currently?



---

archive/issue_comments_045921.json:
```json
{
    "body": "Replying to [comment:9 mhansen]:\n> Do we include a sagetex spkg currently?\n\nAFAIK it's supposed to be in the optional repository, but there were issues with spkgs there disappearing. In IRC, mabshoff has said that he wouldn't update or add new spkgs to the optional repo until someone figured out why spkgs were disappearing and fixed the problem.",
    "created_at": "2009-06-01T01:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5840#issuecomment-45921",
    "user": "ddrake"
}
```

Replying to [comment:9 mhansen]:
> Do we include a sagetex spkg currently?

AFAIK it's supposed to be in the optional repository, but there were issues with spkgs there disappearing. In IRC, mabshoff has said that he wouldn't update or add new spkgs to the optional repo until someone figured out why spkgs were disappearing and fixed the problem.



---

archive/issue_comments_045922.json:
```json
{
    "body": "Merged in the optional package repo.",
    "created_at": "2009-06-01T01:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5840#issuecomment-45922",
    "user": "mhansen"
}
```

Merged in the optional package repo.



---

archive/issue_comments_045923.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T01:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5840#issuecomment-45923",
    "user": "mhansen"
}
```

Resolution: fixed
