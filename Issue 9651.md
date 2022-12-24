# Issue 9651: Addition on CombinatorialFreeModule directly on dictionaries

archive/issues_009651.json:
```json
{
    "body": "Assignee: sage-combinat\n\nKeywords: addition of dictionaries, CombinatorialFreeModule\n\nAt the moment, adding (and taking negative, substracting,...) for CombinatorialFreeModule is not done in a very efficient way.\n\nThis patch\n\n- provides a cythonized version of a pointwise addition of dictionaries, together with multiple options\n\n- uses this addition of dictionaries to provide fast methods for CombinatorialFreeModule\n\n- is (indirectly) based on the patch in Ticket #9648\n\nIssue created by migration from https://trac.sagemath.org/ticket/9651\n\n",
    "created_at": "2010-07-31T18:23:15Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Addition on CombinatorialFreeModule directly on dictionaries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9651",
    "user": "stumpc5"
}
```
Assignee: sage-combinat

Keywords: addition of dictionaries, CombinatorialFreeModule

At the moment, adding (and taking negative, substracting,...) for CombinatorialFreeModule is not done in a very efficient way.

This patch

- provides a cythonized version of a pointwise addition of dictionaries, together with multiple options

- uses this addition of dictionaries to provide fast methods for CombinatorialFreeModule

- is (indirectly) based on the patch in Ticket #9648

Issue created by migration from https://trac.sagemath.org/ticket/9651





---

archive/issue_comments_093622.json:
```json
{
    "body": "Attachment [trac_9651_CombinatorialFreeModule_Addition.patch](tarball://root/attachments/some-uuid/ticket9651/trac_9651_CombinatorialFreeModule_Addition.patch) by stumpc5 created at 2010-07-31 18:40:02\n\nThe patch still needs some doctesting (I have not yet done much, but will do more these days) - in particular, I modified CombinatorialFreeModule._apply_module_morphism and .apply_module_endomorphism. The first method is used in the code for symmetric functions: powersum.py, sfa.py and macdonald.py. Would be nice if someone could check if everything there still works well.\n\nThx, Christian",
    "created_at": "2010-07-31T18:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93622",
    "user": "stumpc5"
}
```

Attachment [trac_9651_CombinatorialFreeModule_Addition.patch](tarball://root/attachments/some-uuid/ticket9651/trac_9651_CombinatorialFreeModule_Addition.patch) by stumpc5 created at 2010-07-31 18:40:02

The patch still needs some doctesting (I have not yet done much, but will do more these days) - in particular, I modified CombinatorialFreeModule._apply_module_morphism and .apply_module_endomorphism. The first method is used in the code for symmetric functions: powersum.py, sfa.py and macdonald.py. Would be nice if someone could check if everything there still works well.

Thx, Christian



---

archive/issue_comments_093623.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-31T18:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93623",
    "user": "stumpc5"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093624.json:
```json
{
    "body": "The patch doesn't apply cleanly to sage-4.5.3.rc0. Applying #9648 first doesn't help.",
    "created_at": "2010-09-06T17:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93624",
    "user": "@dwbump"
}
```

The patch doesn't apply cleanly to sage-4.5.3.rc0. Applying #9648 first doesn't help.



---

archive/issue_comments_093625.json:
```json
{
    "body": "Attachment [trac_9651_CombinatorialFreeModule_Addition-cs.patch](tarball://root/attachments/some-uuid/ticket9651/trac_9651_CombinatorialFreeModule_Addition-cs.patch) by stumpc5 created at 2010-09-19 23:53:54",
    "created_at": "2010-09-19T23:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93625",
    "user": "stumpc5"
}
```

Attachment [trac_9651_CombinatorialFreeModule_Addition-cs.patch](tarball://root/attachments/some-uuid/ticket9651/trac_9651_CombinatorialFreeModule_Addition-cs.patch) by stumpc5 created at 2010-09-19 23:53:54



---

archive/issue_comments_093626.json:
```json
{
    "body": "The revised patch trac_9651_CombinatorialFreeModule_Addition-cs.patch\napplies cleanly to sage 4.6.alpha1 and passes all tests.\n\nBut I haven't been able to confirm that it is a speedup. The results\nof some testing are here:\n\nhttp://groups.google.com/group/sage-combinat-devel/msg/4869cc885ca42bc1",
    "created_at": "2010-09-22T00:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93626",
    "user": "@dwbump"
}
```

The revised patch trac_9651_CombinatorialFreeModule_Addition-cs.patch
applies cleanly to sage 4.6.alpha1 and passes all tests.

But I haven't been able to confirm that it is a speedup. The results
of some testing are here:

http://groups.google.com/group/sage-combinat-devel/msg/4869cc885ca42bc1



---

archive/issue_comments_093627.json:
```json
{
    "body": "Attachment [trac_9651_CombinatorialFreeModule_Addition-cs.2.patch](tarball://root/attachments/some-uuid/ticket9651/trac_9651_CombinatorialFreeModule_Addition-cs.2.patch) by stumpc5 created at 2010-10-16 22:39:42",
    "created_at": "2010-10-16T22:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93627",
    "user": "stumpc5"
}
```

Attachment [trac_9651_CombinatorialFreeModule_Addition-cs.2.patch](tarball://root/attachments/some-uuid/ticket9651/trac_9651_CombinatorialFreeModule_Addition-cs.2.patch) by stumpc5 created at 2010-10-16 22:39:42



---

archive/issue_comments_093628.json:
```json
{
    "body": "includes referees suggestions",
    "created_at": "2010-10-20T13:25:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93628",
    "user": "stumpc5"
}
```

includes referees suggestions



---

archive/issue_comments_093629.json:
```json
{
    "body": "Attachment [trac_9651_CombinatorialFreeModule_Addition-cs.4.patch](tarball://root/attachments/some-uuid/ticket9651/trac_9651_CombinatorialFreeModule_Addition-cs.4.patch) by stumpc5 created at 2010-10-20 18:56:02\n\nincludes more referees suggestions",
    "created_at": "2010-10-20T18:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93629",
    "user": "stumpc5"
}
```

Attachment [trac_9651_CombinatorialFreeModule_Addition-cs.4.patch](tarball://root/attachments/some-uuid/ticket9651/trac_9651_CombinatorialFreeModule_Addition-cs.4.patch) by stumpc5 created at 2010-10-20 18:56:02

includes more referees suggestions



---

archive/issue_comments_093630.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-20T23:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93630",
    "user": "@dwbump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093631.json:
```json
{
    "body": "Positive review!\n\nThere is a thread about this patch in sage-combinat-devel\nresulting in the latest version.\n\nI tested this with sage-4.6.alpha3. After applying\n\n```\ntrac_9648_modulemorphism_codomain_extension.2.patch \ntrac_9651_CombinatorialFreeModule_Addition-cs.4.patch\n```\n\nall tests pass. I also confirmed that the test is a speedup.",
    "created_at": "2010-10-20T23:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93631",
    "user": "@dwbump"
}
```

Positive review!

There is a thread about this patch in sage-combinat-devel
resulting in the latest version.

I tested this with sage-4.6.alpha3. After applying

```
trac_9648_modulemorphism_codomain_extension.2.patch 
trac_9651_CombinatorialFreeModule_Addition-cs.4.patch
```

all tests pass. I also confirmed that the test is a speedup.



---

archive/issue_comments_093632.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-10-23T12:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93632",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093633.json:
```json
{
    "body": "Please remove * * * from the commit message",
    "created_at": "2010-10-23T12:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93633",
    "user": "@jdemeyer"
}
```

Please remove * * * from the commit message



---

archive/issue_comments_093634.json:
```json
{
    "body": "Attachment [trac_9651_CombinatorialFreeModule_Addition-cs.5.patch](tarball://root/attachments/some-uuid/ticket9651/trac_9651_CombinatorialFreeModule_Addition-cs.5.patch) by stumpc5 created at 2010-10-23 17:04:22\n\nReplying to [comment:6 jdemeyer]:\n> Please remove * * * from the commit message\n\ndone!",
    "created_at": "2010-10-23T17:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93634",
    "user": "stumpc5"
}
```

Attachment [trac_9651_CombinatorialFreeModule_Addition-cs.5.patch](tarball://root/attachments/some-uuid/ticket9651/trac_9651_CombinatorialFreeModule_Addition-cs.5.patch) by stumpc5 created at 2010-10-23 17:04:22

Replying to [comment:6 jdemeyer]:
> Please remove * * * from the commit message

done!



---

archive/issue_comments_093635.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-10-23T17:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93635",
    "user": "stumpc5"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_093636.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-01T10:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9651#issuecomment-93636",
    "user": "@jdemeyer"
}
```

Resolution: fixed
