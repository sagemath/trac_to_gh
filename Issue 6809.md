# Issue 6809: abstract_methods_of_class

archive/issues_006809.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: abstract methods\n\nImplement a utility abstract_methods_of_class which lists all the optional and mandatory abstract methods of the class.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6809\n\n",
    "created_at": "2009-08-22T22:57:13Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "abstract_methods_of_class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6809",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

Keywords: abstract methods

Implement a utility abstract_methods_of_class which lists all the optional and mandatory abstract methods of the class.



Issue created by migration from https://trac.sagemath.org/ticket/6809





---

archive/issue_comments_055944.json:
```json
{
    "body": "Attachment [trac_6809_abstract_methods_of_class.patch](tarball://root/attachments/some-uuid/ticket6809/trac_6809_abstract_methods_of_class.patch) by @nthiery created at 2009-10-16 11:03:12",
    "created_at": "2009-10-16T11:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6809#issuecomment-55944",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_6809_abstract_methods_of_class.patch](tarball://root/attachments/some-uuid/ticket6809/trac_6809_abstract_methods_of_class.patch) by @nthiery created at 2009-10-16 11:03:12



---

archive/issue_comments_055945.json:
```json
{
    "body": "New version with is_optional method",
    "created_at": "2009-10-16T11:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6809#issuecomment-55945",
    "user": "https://github.com/hivert"
}
```

New version with is_optional method



---

archive/issue_comments_055946.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-16T11:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6809#issuecomment-55946",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_055947.json:
```json
{
    "body": "Attachment [trac_6809_abstract_methods_of_class.2.patch](tarball://root/attachments/some-uuid/ticket6809/trac_6809_abstract_methods_of_class.2.patch) by @hivert created at 2009-10-16 11:41:13\n\nI'm done reviewing this patch. It is good upto a small detail: the code access to a private attribute. I've added an accessor method. \n\nI just uploaded a new version of the patch after review which add a is_optional method for better encapsulation (as suggested by former comment in the code).\n\nNicolas: please add a positive review when you finished reviewing my changes.\n\nCheers,\n\nFlorent",
    "created_at": "2009-10-16T11:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6809#issuecomment-55947",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_6809_abstract_methods_of_class.2.patch](tarball://root/attachments/some-uuid/ticket6809/trac_6809_abstract_methods_of_class.2.patch) by @hivert created at 2009-10-16 11:41:13

I'm done reviewing this patch. It is good upto a small detail: the code access to a private attribute. I've added an accessor method. 

I just uploaded a new version of the patch after review which add a is_optional method for better encapsulation (as suggested by former comment in the code).

Nicolas: please add a positive review when you finished reviewing my changes.

Cheers,

Florent



---

archive/issue_comments_055948.json:
```json
{
    "body": "During his review of my change Nicolas spotted a missing blank line after 'EXAMPLE::'... I'm re-uploading the patch...\n\nCheers,\n\nFlorent",
    "created_at": "2009-10-16T11:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6809#issuecomment-55948",
    "user": "https://github.com/hivert"
}
```

During his review of my change Nicolas spotted a missing blank line after 'EXAMPLE::'... I'm re-uploading the patch...

Cheers,

Florent



---

archive/issue_comments_055949.json:
```json
{
    "body": "Added missing blank line",
    "created_at": "2009-10-16T11:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6809#issuecomment-55949",
    "user": "https://github.com/hivert"
}
```

Added missing blank line



---

archive/issue_comments_055950.json:
```json
{
    "body": "Attachment [trac_6809_abstract_methods_of_class.3.patch](tarball://root/attachments/some-uuid/ticket6809/trac_6809_abstract_methods_of_class.3.patch) by @hivert created at 2009-10-16 11:58:03\n\nAfter Blank line added, Nicolas allows me to put the positive review. \n\nOnly apply the last trac_6809_abstract_methods_of_class.3.patch\n\nFlorent",
    "created_at": "2009-10-16T11:58:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6809#issuecomment-55950",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_6809_abstract_methods_of_class.3.patch](tarball://root/attachments/some-uuid/ticket6809/trac_6809_abstract_methods_of_class.3.patch) by @hivert created at 2009-10-16 11:58:03

After Blank line added, Nicolas allows me to put the positive review. 

Only apply the last trac_6809_abstract_methods_of_class.3.patch

Florent



---

archive/issue_comments_055951.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-16T11:58:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6809#issuecomment-55951",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055952.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-19T13:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6809#issuecomment-55952",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
