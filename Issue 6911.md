# Issue 6911: Faster basis of a Hecke algebra

archive/issues_006911.json:
```json
{
    "body": "Assignee: craigcitro\n\nFollowup to #6768, uses algorithm at http://wiki.sagemath.org/days17/projects/presagedays/discussion\n\nIssue created by migration from https://trac.sagemath.org/ticket/6911\n\n",
    "created_at": "2009-09-10T05:48:10Z",
    "labels": [
        "modular forms",
        "major",
        "enhancement"
    ],
    "title": "Faster basis of a Hecke algebra",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6911",
    "user": "robertwb"
}
```
Assignee: craigcitro

Followup to #6768, uses algorithm at http://wiki.sagemath.org/days17/projects/presagedays/discussion

Issue created by migration from https://trac.sagemath.org/ticket/6911





---

archive/issue_comments_057087.json:
```json
{
    "body": "Also discriminants.",
    "created_at": "2009-09-10T05:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6911#issuecomment-57087",
    "user": "robertwb"
}
```

Also discriminants.



---

archive/issue_comments_057088.json:
```json
{
    "body": "Attachment [6911-hecke-basis-disc.patch](tarball://root/attachments/some-uuid/ticket6911/6911-hecke-basis-disc.patch) by robertwb created at 2009-09-10 05:50:13",
    "created_at": "2009-09-10T05:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6911#issuecomment-57088",
    "user": "robertwb"
}
```

Attachment [6911-hecke-basis-disc.patch](tarball://root/attachments/some-uuid/ticket6911/6911-hecke-basis-disc.patch) by robertwb created at 2009-09-10 05:50:13



---

archive/issue_comments_057089.json:
```json
{
    "body": "REFEREE REPORT:\n\n1. Awesome trace of product trick!\n\n2. I think the following range must start at 1 -- otherwise this is potentially (in theory) a major bug:\n\n```\nspan = [self.hecke_operator(n) for n in range(2, bound+1) if not self.is_anemic() or gcd(n, level) == 1] \n```\n\n\n3. \"eisenstein\" should be capitalized below:\n\n```\n \t1182\t        Returns whether self is cuspidal, i.e. has no eisenstein part.\n```\n\n\n4. The patch doesn't seem to apply cleanly to 4.1.2.alpha1:\n\n```\nHunk #4 FAILED at 214\n1 out of 6 hunks FAILED -- saving rejects to file sage/modular/hecke/algebra.py.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2009-09-17T07:47:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6911#issuecomment-57089",
    "user": "was"
}
```

REFEREE REPORT:

1. Awesome trace of product trick!

2. I think the following range must start at 1 -- otherwise this is potentially (in theory) a major bug:

```
span = [self.hecke_operator(n) for n in range(2, bound+1) if not self.is_anemic() or gcd(n, level) == 1] 
```


3. "eisenstein" should be capitalized below:

```
 	1182	        Returns whether self is cuspidal, i.e. has no eisenstein part.
```


4. The patch doesn't seem to apply cleanly to 4.1.2.alpha1:

```
Hunk #4 FAILED at 214
1 out of 6 hunks FAILED -- saving rejects to file sage/modular/hecke/algebra.py.rej
abort: patch failed to apply
```




---

archive/issue_comments_057090.json:
```json
{
    "body": "Attachment [trac_6911-referee-replace_other_patch-apply_only_this.patch](tarball://root/attachments/some-uuid/ticket6911/trac_6911-referee-replace_other_patch-apply_only_this.patch) by was created at 2009-09-19 11:23:38",
    "created_at": "2009-09-19T11:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6911#issuecomment-57090",
    "user": "was"
}
```

Attachment [trac_6911-referee-replace_other_patch-apply_only_this.patch](tarball://root/attachments/some-uuid/ticket6911/trac_6911-referee-replace_other_patch-apply_only_this.patch) by was created at 2009-09-19 11:23:38



---

archive/issue_comments_057091.json:
```json
{
    "body": "Attachment [trac_6911-referee_followup_that_fixes_some_bugs.patch](tarball://root/attachments/some-uuid/ticket6911/trac_6911-referee_followup_that_fixes_some_bugs.patch) by was created at 2009-09-19 11:42:43",
    "created_at": "2009-09-19T11:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6911#issuecomment-57091",
    "user": "was"
}
```

Attachment [trac_6911-referee_followup_that_fixes_some_bugs.patch](tarball://root/attachments/some-uuid/ticket6911/trac_6911-referee_followup_that_fixes_some_bugs.patch) by was created at 2009-09-19 11:42:43



---

archive/issue_comments_057092.json:
```json
{
    "body": "Apply these:\n\n```\ntrac_6911-referee-replace_other_patch-apply_only_this.patch\ntrac_6911-referee_followup_that_fixes_some_bugs.patch \n```\n",
    "created_at": "2009-09-19T11:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6911#issuecomment-57092",
    "user": "was"
}
```

Apply these:

```
trac_6911-referee-replace_other_patch-apply_only_this.patch
trac_6911-referee_followup_that_fixes_some_bugs.patch 
```




---

archive/issue_comments_057093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-19T20:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6911#issuecomment-57093",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057094.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6911-referee-replace_other_patch-apply_only_this.patch`\n2. `trac_6911-referee_followup_that_fixes_some_bugs.patch`",
    "created_at": "2009-09-19T20:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6911#issuecomment-57094",
    "user": "mvngu"
}
```

Merged patches in this order:

1. `trac_6911-referee-replace_other_patch-apply_only_this.patch`
2. `trac_6911-referee_followup_that_fixes_some_bugs.patch`
