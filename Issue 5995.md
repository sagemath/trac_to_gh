# Issue 5995: Membership testing for modular forms subspaces is hopeless

archive/issues_005995.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @craigcitro\n\nThis is pretty poor, IMHO:\n\n```\nsage: M = ModularForms(17, 4)\nsage: S = M.cuspidal_submodule()\nsage: M.0 == S.0\nTrue\nsage: M.0 in S\nFalse\n```\n\n\nAs far as I can tell at a glance this is happening because `S.__call__(x)` tests whether or not the parent of x has a canonical inclusion map to S; it should probably be testing whether the parent of x has a canonical inclusion map to the *ambient space* of S.\n\nOnce the above is fixed we should also have a method `is_cuspidal()` for modular forms objects, which would be secretly just `self in self.parent().cuspidal_submodule()`. A corresponding `is_eisenstein()` would be good, too.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5995\n\n",
    "created_at": "2009-05-06T10:01:31Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "Membership testing for modular forms subspaces is hopeless",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5995",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @craigcitro

CC:  @craigcitro

This is pretty poor, IMHO:

```
sage: M = ModularForms(17, 4)
sage: S = M.cuspidal_submodule()
sage: M.0 == S.0
True
sage: M.0 in S
False
```


As far as I can tell at a glance this is happening because `S.__call__(x)` tests whether or not the parent of x has a canonical inclusion map to S; it should probably be testing whether the parent of x has a canonical inclusion map to the *ambient space* of S.

Once the above is fixed we should also have a method `is_cuspidal()` for modular forms objects, which would be secretly just `self in self.parent().cuspidal_submodule()`. A corresponding `is_eisenstein()` would be good, too.

Issue created by migration from https://trac.sagemath.org/ticket/5995





---

archive/issue_comments_047596.json:
```json
{
    "body": "apply after #4357 and #5736",
    "created_at": "2009-05-12T08:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5995#issuecomment-47596",
    "user": "https://github.com/loefflerd"
}
```

apply after #4357 and #5736



---

archive/issue_comments_047597.json:
```json
{
    "body": "Attachment [trac_5995.patch](tarball://root/attachments/some-uuid/ticket5995/trac_5995.patch) by @loefflerd created at 2009-05-12 08:53:26\n\nHere's a patch, which adds ` is_cuspidal`, `is_eisenstein`, `is_new` and `is_old`, and corrects a funny glitch whereby elliptic curve newforms consistently claimed not to be cuspidal :-) I wrote the patch and ran tests with this and everything else (including the not-yet-fully-refereed #5968) installed simultaneously, but it should at least apply as long as you have the patches at #4357 and #5736 installed.",
    "created_at": "2009-05-12T08:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5995#issuecomment-47597",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5995.patch](tarball://root/attachments/some-uuid/ticket5995/trac_5995.patch) by @loefflerd created at 2009-05-12 08:53:26

Here's a patch, which adds ` is_cuspidal`, `is_eisenstein`, `is_new` and `is_old`, and corrects a funny glitch whereby elliptic curve newforms consistently claimed not to be cuspidal :-) I wrote the patch and ran tests with this and everything else (including the not-yet-fully-refereed #5968) installed simultaneously, but it should at least apply as long as you have the patches at #4357 and #5736 installed.



---

archive/issue_comments_047598.json:
```json
{
    "body": "Looks good to me.  Patch applies fine to 4.0 and tests in sage/modular/{modform,hecke} pass.",
    "created_at": "2009-05-30T16:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5995#issuecomment-47598",
    "user": "https://github.com/JohnCremona"
}
```

Looks good to me.  Patch applies fine to 4.0 and tests in sage/modular/{modform,hecke} pass.



---

archive/issue_comments_047599.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T06:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5995#issuecomment-47599",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.alpha0.



---

archive/issue_comments_047600.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T06:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5995#issuecomment-47600",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
