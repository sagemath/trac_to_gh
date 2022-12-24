# Issue 6929: Docs in functional and a few ring methods

archive/issues_006929.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: integer, integral closure\n\nThis patch mostly brings misc/functional.py to (nearly) 100%, but also does a few useful things like allow MUCH wider usage of the functional base_field and say that the integer ring is, in fact, integrally closed!\n\nIssue created by migration from https://trac.sagemath.org/ticket/6929\n\n",
    "created_at": "2009-09-14T19:54:27Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Docs in functional and a few ring methods",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6929",
    "user": "kcrisman"
}
```
Assignee: tba

Keywords: integer, integral closure

This patch mostly brings misc/functional.py to (nearly) 100%, but also does a few useful things like allow MUCH wider usage of the functional base_field and say that the integer ring is, in fact, integrally closed!

Issue created by migration from https://trac.sagemath.org/ticket/6929





---

archive/issue_comments_057270.json:
```json
{
    "body": "Attachment [trac_6929-functional-doctests.patch](tarball://root/attachments/some-uuid/ticket6929/trac_6929-functional-doctests.patch) by kcrisman created at 2009-09-14 19:56:21",
    "created_at": "2009-09-14T19:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6929#issuecomment-57270",
    "user": "kcrisman"
}
```

Attachment [trac_6929-functional-doctests.patch](tarball://root/attachments/some-uuid/ticket6929/trac_6929-functional-doctests.patch) by kcrisman created at 2009-09-14 19:56:21



---

archive/issue_comments_057271.json:
```json
{
    "body": "rebased against 4.1.2.alpha2. apply only this patch",
    "created_at": "2009-09-23T03:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6929#issuecomment-57271",
    "user": "jhpalmieri"
}
```

rebased against 4.1.2.alpha2. apply only this patch



---

archive/issue_comments_057272.json:
```json
{
    "body": "Attachment [trac_6929-rebased.patch](tarball://root/attachments/some-uuid/ticket6929/trac_6929-rebased.patch) by jhpalmieri created at 2009-09-23 04:25:53\n\nThe patch needed to be rebased (only the changes in rings/ring.pyx).  I also added one fix (referee's prerogative: changing ``n`th` to ``n^{th}`` in misc/functional.py) to avoid a warning when building the reference manual.\n\nLooks good, all tests pass, positive review.",
    "created_at": "2009-09-23T04:25:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6929#issuecomment-57272",
    "user": "jhpalmieri"
}
```

Attachment [trac_6929-rebased.patch](tarball://root/attachments/some-uuid/ticket6929/trac_6929-rebased.patch) by jhpalmieri created at 2009-09-23 04:25:53

The patch needed to be rebased (only the changes in rings/ring.pyx).  I also added one fix (referee's prerogative: changing ``n`th` to ``n^{th}`` in misc/functional.py) to avoid a warning when building the reference manual.

Looks good, all tests pass, positive review.



---

archive/issue_comments_057273.json:
```json
{
    "body": "set username as kcrisman",
    "created_at": "2009-09-24T11:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6929#issuecomment-57273",
    "user": "mvngu"
}
```

set username as kcrisman



---

archive/issue_comments_057274.json:
```json
{
    "body": "Attachment [trac_6929-rebased-v2.patch](tarball://root/attachments/some-uuid/ticket6929/trac_6929-rebased-v2.patch) by mvngu created at 2009-09-24 11:46:18\n\nThe patch `trac_6929-rebased-v2.patch` is the same as `trac_6929-rebased.patch`. The only difference is that `trac_6929-rebased-v2.patch` sets the username to that of kcrisman's. That way, the patch would be committed in his name. Even after a rebase, the username of the original author should remain in the rebased patch.",
    "created_at": "2009-09-24T11:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6929#issuecomment-57274",
    "user": "mvngu"
}
```

Attachment [trac_6929-rebased-v2.patch](tarball://root/attachments/some-uuid/ticket6929/trac_6929-rebased-v2.patch) by mvngu created at 2009-09-24 11:46:18

The patch `trac_6929-rebased-v2.patch` is the same as `trac_6929-rebased.patch`. The only difference is that `trac_6929-rebased-v2.patch` sets the username to that of kcrisman's. That way, the patch would be committed in his name. Even after a rebase, the username of the original author should remain in the rebased patch.



---

archive/issue_comments_057275.json:
```json
{
    "body": "But how do you DO that?",
    "created_at": "2009-09-24T12:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6929#issuecomment-57275",
    "user": "kcrisman"
}
```

But how do you DO that?



---

archive/issue_comments_057276.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> But how do you DO that?\n\n1. Download the patch `trac_6929-rebased.patch` to a local machine.\n2. Open `trac_6929-rebased.patch` in a text editor.\n3. Change the line\n {{{\n# User J. H. Palmieri <palmieri`@`math.washington.edu>\n }}}\n to \n {{{\n# User Karl-Dieter Crisman <kcrisman`@`gmail.com>\n }}}\n1. Upload the patch with the modified username to the trac server.",
    "created_at": "2009-09-24T13:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6929#issuecomment-57276",
    "user": "mvngu"
}
```

Replying to [comment:5 kcrisman]:
> But how do you DO that?

1. Download the patch `trac_6929-rebased.patch` to a local machine.
2. Open `trac_6929-rebased.patch` in a text editor.
3. Change the line
 {{{
# User J. H. Palmieri <palmieri`@`math.washington.edu>
 }}}
 to 
 {{{
# User Karl-Dieter Crisman <kcrisman`@`gmail.com>
 }}}
1. Upload the patch with the modified username to the trac server.



---

archive/issue_comments_057277.json:
```json
{
    "body": "I see, quite manually.  I was wondering whether that was possible in HG, but I like this better.  Perhaps the instructions are a little TOO clear... :)",
    "created_at": "2009-09-24T13:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6929#issuecomment-57277",
    "user": "kcrisman"
}
```

I see, quite manually.  I was wondering whether that was possible in HG, but I like this better.  Perhaps the instructions are a little TOO clear... :)



---

archive/issue_comments_057278.json:
```json
{
    "body": "Merged `trac_6929-rebased-v2.patch`.",
    "created_at": "2009-09-24T14:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6929#issuecomment-57278",
    "user": "mvngu"
}
```

Merged `trac_6929-rebased-v2.patch`.



---

archive/issue_comments_057279.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-24T14:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6929#issuecomment-57279",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057280.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6929#issuecomment-57280",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
