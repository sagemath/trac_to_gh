# Issue 1172: change the watkins license in SAGE_ROOT/COPYING

archive/issues_001172.json:
```json
{
    "body": "Assignee: was\n\nChange the watkins license in SAGE_ROOT/COPYING to the following, since Mark Watkins told me to do this.\n\n\n```\nThe SYMPOW COPYING file says:\n\n\nRedistribution and use in source and binary forms, with or without\nmodification, are permitted provided that the following conditions are met:\n * Redistribution of source code must retain the above copyright notice,\n this list of conditions and the following disclaimer.\n * Redistribution in binary form must reproduce the above copyright\n notice, this list of conditions and the following disclaimer in the\n documentation and/or other materials provided with the distribution.\n * If redistribution is done as a part of a compilation that has a more\n restrictive license (such as the GPL), then the fact that SYMPOW has\n a less restrictive license must be made clear to the recipient.\n For example, a line like (include bracketed text if SYMPOW is modified):\n \"This compilation includes [a modification of] SYMPOW whose [original]\n  code has a less-restrictive license than the entire compilation.\"\n should appear in a suitable place in the COPYING and/or LICENSE file.\n\n[followed by the BSD disclaimer]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1172\n\n",
    "created_at": "2007-11-14T23:25:20Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "title": "change the watkins license in SAGE_ROOT/COPYING",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1172",
    "user": "was"
}
```
Assignee: was

Change the watkins license in SAGE_ROOT/COPYING to the following, since Mark Watkins told me to do this.


```
The SYMPOW COPYING file says:


Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
 * Redistribution of source code must retain the above copyright notice,
 this list of conditions and the following disclaimer.
 * Redistribution in binary form must reproduce the above copyright
 notice, this list of conditions and the following disclaimer in the
 documentation and/or other materials provided with the distribution.
 * If redistribution is done as a part of a compilation that has a more
 restrictive license (such as the GPL), then the fact that SYMPOW has
 a less restrictive license must be made clear to the recipient.
 For example, a line like (include bracketed text if SYMPOW is modified):
 "This compilation includes [a modification of] SYMPOW whose [original]
  code has a less-restrictive license than the entire compilation."
 should appear in a suitable place in the COPYING and/or LICENSE file.

[followed by the BSD disclaimer]
```


Issue created by migration from https://trac.sagemath.org/ticket/1172





---

archive/issue_comments_007186.json:
```json
{
    "body": "This was a pretty easy patch to make...",
    "created_at": "2012-06-25T09:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1172#issuecomment-7186",
    "user": "kini"
}
```

This was a pretty easy patch to make...



---

archive/issue_comments_007187.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-25T09:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1172#issuecomment-7187",
    "user": "kini"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_007188.json:
```json
{
    "body": "apply to $SAGE_ROOT",
    "created_at": "2012-06-25T09:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1172#issuecomment-7188",
    "user": "kini"
}
```

apply to $SAGE_ROOT



---

archive/issue_comments_007189.json:
```json
{
    "body": "Attachment [trac_1172-watkins-license.patch](tarball://root/attachments/some-uuid/ticket1172/trac_1172-watkins-license.patch) by ohanar created at 2012-06-25 22:56:23\n\nLooks good to me.",
    "created_at": "2012-06-25T22:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1172#issuecomment-7189",
    "user": "ohanar"
}
```

Attachment [trac_1172-watkins-license.patch](tarball://root/attachments/some-uuid/ticket1172/trac_1172-watkins-license.patch) by ohanar created at 2012-06-25 22:56:23

Looks good to me.



---

archive/issue_comments_007190.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-25T22:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1172#issuecomment-7190",
    "user": "ohanar"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_007191.json:
```json
{
    "body": "The last clause sounds awfully much like the BSD advertising clause.  Are we sure this is GPL-compatible?  IANAL, but it's a natural question to ask.",
    "created_at": "2012-06-26T06:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1172#issuecomment-7191",
    "user": "jdemeyer"
}
```

The last clause sounds awfully much like the BSD advertising clause.  Are we sure this is GPL-compatible?  IANAL, but it's a natural question to ask.



---

archive/issue_comments_007192.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-06-28T07:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1172#issuecomment-7192",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_007193.json:
```json
{
    "body": "Jeroen: should this be merged if your question remains unanswered?",
    "created_at": "2012-06-28T08:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1172#issuecomment-7193",
    "user": "kini"
}
```

Jeroen: should this be merged if your question remains unanswered?



---

archive/issue_comments_007194.json:
```json
{
    "body": "Replying to [comment:5 kini]:\n> Jeroen: should this be merged if your question remains unanswered?\nI guess so.  This patch doesn't change the license, it changes the documentation of the license.  Whether or not this patch gets merged, my question stands.",
    "created_at": "2012-06-28T08:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1172#issuecomment-7194",
    "user": "jdemeyer"
}
```

Replying to [comment:5 kini]:
> Jeroen: should this be merged if your question remains unanswered?
I guess so.  This patch doesn't change the license, it changes the documentation of the license.  Whether or not this patch gets merged, my question stands.



---

archive/issue_comments_007195.json:
```json
{
    "body": "Good point.",
    "created_at": "2012-06-28T08:35:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1172#issuecomment-7195",
    "user": "kini"
}
```

Good point.
