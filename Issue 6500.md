# Issue 6500: Improve reference manual coverage for polynomial rings

archive/issues_006500.json:
```json
{
    "body": "Assignee: tba\n\nCC:  jhpalmieri mvngu\n\nAs of 4.1.rc1 very few of the polynomial ring classes are in the reference manual; even the basic constructor function is missing. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6500\n\n",
    "created_at": "2009-07-09T14:39:15Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Improve reference manual coverage for polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6500",
    "user": "davidloeffler"
}
```
Assignee: tba

CC:  jhpalmieri mvngu

As of 4.1.rc1 very few of the polynomial ring classes are in the reference manual; even the basic constructor function is missing. 

Issue created by migration from https://trac.sagemath.org/ticket/6500





---

archive/issue_comments_052868.json:
```json
{
    "body": "The patch I've just uploaded Sphinxifies the docstrings of several modules in sage/rings/polynomial, and adds them to the reference manual.\n\n(CCed to jhpalmieri and mvngu, as I know you have both contributed a great deal to improving the documentation in the past.)",
    "created_at": "2009-07-09T14:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6500#issuecomment-52868",
    "user": "davidloeffler"
}
```

The patch I've just uploaded Sphinxifies the docstrings of several modules in sage/rings/polynomial, and adds them to the reference manual.

(CCed to jhpalmieri and mvngu, as I know you have both contributed a great deal to improving the documentation in the past.)



---

archive/issue_comments_052869.json:
```json
{
    "body": "Hi David,\n\nJust a comment before I review your patch. Can you put your name on the patch? That way, you are identified as the patch's author and it makes it easy to credit you on release notes and release tours. Also, can you put in a commit message in your patch? A commit message should have the ticket number in it. I usually put the ticket number in front of any commit message I write. The template I follow is:\n\ntrac #n: <put commit message here>",
    "created_at": "2009-07-09T15:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6500#issuecomment-52869",
    "user": "mvngu"
}
```

Hi David,

Just a comment before I review your patch. Can you put your name on the patch? That way, you are identified as the patch's author and it makes it easy to credit you on release notes and release tours. Also, can you put in a commit message in your patch? A commit message should have the ticket number in it. I usually put the ticket number in front of any commit message I write. The template I follow is:

trac #n: <put commit message here>



---

archive/issue_comments_052870.json:
```json
{
    "body": "Attachment [trac_6500-polynomial_docstrings.patch](tarball://root/attachments/some-uuid/ticket6500/trac_6500-polynomial_docstrings.patch) by davidloeffler created at 2009-07-09 15:22:57\n\nWell spotted -- I have uploaded another patch (overwriting the previous one) that has my username and a commit message on it. Thanks for the quick response.",
    "created_at": "2009-07-09T15:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6500#issuecomment-52870",
    "user": "davidloeffler"
}
```

Attachment [trac_6500-polynomial_docstrings.patch](tarball://root/attachments/some-uuid/ticket6500/trac_6500-polynomial_docstrings.patch) by davidloeffler created at 2009-07-09 15:22:57

Well spotted -- I have uploaded another patch (overwriting the previous one) that has my username and a commit message on it. Thanks for the quick response.



---

archive/issue_comments_052871.json:
```json
{
    "body": "apply over previous patch",
    "created_at": "2009-07-10T14:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6500#issuecomment-52871",
    "user": "davidloeffler"
}
```

apply over previous patch



---

archive/issue_comments_052872.json:
```json
{
    "body": "Attachment [trac_6500-polynomial_docstrings_2.patch](tarball://root/attachments/some-uuid/ticket6500/trac_6500-polynomial_docstrings_2.patch) by davidloeffler created at 2009-07-10 14:32:18\n\nHere's another patch in the same vein, covering multivariate polynomial rings.",
    "created_at": "2009-07-10T14:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6500#issuecomment-52872",
    "user": "davidloeffler"
}
```

Attachment [trac_6500-polynomial_docstrings_2.patch](tarball://root/attachments/some-uuid/ticket6500/trac_6500-polynomial_docstrings_2.patch) by davidloeffler created at 2009-07-10 14:32:18

Here's another patch in the same vein, covering multivariate polynomial rings.



---

archive/issue_comments_052873.json:
```json
{
    "body": "Source code looks good and the documentation looks good.  I'm attaching a referee's patch which looks large, but the large majority of which contains repetitions of two changes: \"EXAMPLE::\" --> \"EXAMPLES::\" and \".::\" --> \". ::\" (a period followed by :: produces \".:\" in the Sphinx documentation, while if you insert a space, no colons are printed).  Of the other changes, I think the only one worth mentioning is that I changed instances of the \"param\" command used in polynomial_singular_interface.py to INPUT blocks, for consistency with the rest of the documentation.\n\nI don't think my patch needs much review, but I'll keep this marked as \"needs review\".  davidloeffler's two patches get positive reviews from me; if my patch is okay, the whole thing gets a positive review.",
    "created_at": "2009-07-20T02:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6500#issuecomment-52873",
    "user": "jhpalmieri"
}
```

Source code looks good and the documentation looks good.  I'm attaching a referee's patch which looks large, but the large majority of which contains repetitions of two changes: "EXAMPLE::" --> "EXAMPLES::" and ".::" --> ". ::" (a period followed by :: produces ".:" in the Sphinx documentation, while if you insert a space, no colons are printed).  Of the other changes, I think the only one worth mentioning is that I changed instances of the "param" command used in polynomial_singular_interface.py to INPUT blocks, for consistency with the rest of the documentation.

I don't think my patch needs much review, but I'll keep this marked as "needs review".  davidloeffler's two patches get positive reviews from me; if my patch is okay, the whole thing gets a positive review.



---

archive/issue_comments_052874.json:
```json
{
    "body": "Attachment [trac_6500_ref.patch](tarball://root/attachments/some-uuid/ticket6500/trac_6500_ref.patch) by jhpalmieri created at 2009-07-20 02:33:37\n\napply over previous patches",
    "created_at": "2009-07-20T02:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6500#issuecomment-52874",
    "user": "jhpalmieri"
}
```

Attachment [trac_6500_ref.patch](tarball://root/attachments/some-uuid/ticket6500/trac_6500_ref.patch) by jhpalmieri created at 2009-07-20 02:33:37

apply over previous patches



---

archive/issue_comments_052875.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-07-20T02:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6500#issuecomment-52875",
    "user": "jhpalmieri"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_052876.json:
```json
{
    "body": "John's patch looks fine to me -- it applies without problems, the documentation builds without errors, and the formatting fixes all look sensible.",
    "created_at": "2009-07-20T08:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6500#issuecomment-52876",
    "user": "davidloeffler"
}
```

John's patch looks fine to me -- it applies without problems, the documentation builds without errors, and the formatting fixes all look sensible.



---

archive/issue_comments_052877.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-20T13:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6500#issuecomment-52877",
    "user": "mvngu"
}
```

Resolution: fixed
