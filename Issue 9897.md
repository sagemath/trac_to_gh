# Issue 9897: Clean up and add functions to sage/libs/pari/decl.pxi

archive/issues_009897.json:
```json
{
    "body": "Assignee: was\n\nCC:  leif\n\n* Add a file `sage/libs/pari/declinl.pxi` for declarations of inline functions.\n  * Some clean up of `sage/libs/pari/decl.pxi`, in particular removing duplicate functions\n\nIssue created by migration from https://trac.sagemath.org/ticket/9898\n\n",
    "created_at": "2010-09-11T13:24:02Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "title": "Clean up and add functions to sage/libs/pari/decl.pxi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9897",
    "user": "jdemeyer"
}
```
Assignee: was

CC:  leif

* Add a file `sage/libs/pari/declinl.pxi` for declarations of inline functions.
  * Some clean up of `sage/libs/pari/decl.pxi`, in particular removing duplicate functions

Issue created by migration from https://trac.sagemath.org/ticket/9898





---

archive/issue_comments_098396.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-12T09:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9897#issuecomment-98396",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098397.json:
```json
{
    "body": "s/seperate/separate/\n\ns/This files/This file/",
    "created_at": "2010-09-12T13:18:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9897#issuecomment-98397",
    "user": "leif"
}
```

s/seperate/separate/

s/This files/This file/



---

archive/issue_comments_098398.json:
```json
{
    "body": "Replying to [comment:3 leif]:\n> s/seperate/separate/\n> \n> s/This files/This file/\n\nDone.",
    "created_at": "2010-09-16T17:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9897#issuecomment-98398",
    "user": "jdemeyer"
}
```

Replying to [comment:3 leif]:
> s/seperate/separate/
> 
> s/This files/This file/

Done.



---

archive/issue_comments_098399.json:
```json
{
    "body": "Did you upload the wrong patch?\n\nI just noticed the typos are back...",
    "created_at": "2010-09-19T20:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9897#issuecomment-98399",
    "user": "leif"
}
```

Did you upload the wrong patch?

I just noticed the typos are back...



---

archive/issue_comments_098400.json:
```json
{
    "body": "The `global t0` in `gequal_long()` is superfluous.",
    "created_at": "2010-09-19T20:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9897#issuecomment-98400",
    "user": "leif"
}
```

The `global t0` in `gequal_long()` is superfluous.



---

archive/issue_comments_098401.json:
```json
{
    "body": "Attachment\n\nDone.",
    "created_at": "2010-09-20T07:24:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9897#issuecomment-98401",
    "user": "jdemeyer"
}
```

Attachment

Done.



---

archive/issue_comments_098402.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-20T14:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9897#issuecomment-98402",
    "user": "leif"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098403.json:
```json
{
    "body": "Ok, I've now also tested this with Sage 4.6.alpha1 and #9876 (PARI 2.4.3.svn-12577.p7) on Ubuntu 9.04 x86 and Ubuntu 10.04 x86_64 (both `ptestlong`).\n\nPatch is up-to-date, so positive review.\n\nI've (of course?) not checked if all functions really come from the PARI source files they're claimed to come from. ;-)\n\nIt's up to you to convince Mitesh to merge it into 4.6.alpha2. :)",
    "created_at": "2010-09-20T14:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9897#issuecomment-98403",
    "user": "leif"
}
```

Ok, I've now also tested this with Sage 4.6.alpha1 and #9876 (PARI 2.4.3.svn-12577.p7) on Ubuntu 9.04 x86 and Ubuntu 10.04 x86_64 (both `ptestlong`).

Patch is up-to-date, so positive review.

I've (of course?) not checked if all functions really come from the PARI source files they're claimed to come from. ;-)

It's up to you to convince Mitesh to merge it into 4.6.alpha2. :)



---

archive/issue_comments_098404.json:
```json
{
    "body": "Perhaps one should mention that `pari/declinl.pxi` gets included by `pari/decl.pxi`.\n\nAdd svn snapshot number?",
    "created_at": "2010-09-26T14:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9897#issuecomment-98404",
    "user": "leif"
}
```

Perhaps one should mention that `pari/declinl.pxi` gets included by `pari/decl.pxi`.

Add svn snapshot number?



---

archive/issue_comments_098405.json:
```json
{
    "body": "Adds authors to files in sage/libs/pari, apply on top of 9898_pari_decl.patch",
    "created_at": "2010-09-26T17:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9897#issuecomment-98405",
    "user": "jdemeyer"
}
```

Adds authors to files in sage/libs/pari, apply on top of 9898_pari_decl.patch



---

archive/issue_comments_098406.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:10 leif]:\n> Perhaps one should mention that `pari/declinl.pxi` gets included by `pari/decl.pxi`.\nDone.\n\n> Add svn snapshot number?\nI don't think that is so relevant (those files would not look that much different for other SVN snapshot numbers). Besides, people can still look at the ticket #9343 for more information.",
    "created_at": "2010-09-26T17:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9897#issuecomment-98406",
    "user": "jdemeyer"
}
```

Attachment

Replying to [comment:10 leif]:
> Perhaps one should mention that `pari/declinl.pxi` gets included by `pari/decl.pxi`.
Done.

> Add svn snapshot number?
I don't think that is so relevant (those files would not look that much different for other SVN snapshot numbers). Besides, people can still look at the ticket #9343 for more information.



---

archive/issue_comments_098407.json:
```json
{
    "body": "Replying to [comment:11 jdemeyer]:\n> [...] people can still look at the ticket #9343 for more information.\n\n:-)\n\nBtw, is [08-15](http://en.wikipedia.org/wiki/08/15) a [*symbolic*](http://de.wikipedia.org/wiki/08/15_%28Redewendung%29) date?\n\nPositive review for the second patch, too.",
    "created_at": "2010-09-26T17:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9897#issuecomment-98407",
    "user": "leif"
}
```

Replying to [comment:11 jdemeyer]:
> [...] people can still look at the ticket #9343 for more information.

:-)

Btw, is [08-15](http://en.wikipedia.org/wiki/08/15) a [*symbolic*](http://de.wikipedia.org/wiki/08/15_%28Redewendung%29) date?

Positive review for the second patch, too.



---

archive/issue_comments_098408.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T10:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9897#issuecomment-98408",
    "user": "mpatel"
}
```

Resolution: fixed
