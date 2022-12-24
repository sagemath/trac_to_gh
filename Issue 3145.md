# Issue 3145: documentation and defaults for the 'view' function

archive/issues_003145.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: latex, view\n\nI'm attaching a patch with, I suppose, three changes (two of which are minor) to the 'view' function:\n1. longer (and I think clearer) documentation\n2. no 'center' option anymore. I don't think centering things in displayed equations has any effect in LaTeX.\n3. changed default value of 'sep' from '$$ $$' to *.  I have two reasons for this: I think the output looks better this way, and I think that the default value of '$$ $$' is misleading: someone might infer that it's playing the role of the variables 'math_left' and 'math_right' in _latex_file, when in fact it's just adding some vertical space between the output lines.  If you don't like having a default of *, then I would suggest changing it to something like '\\\\vspace{5mm}' which gives a better idea of what 'sep' actually does and even implies how one might change it (by changing the length).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3145\n\n",
    "created_at": "2008-05-09T19:16:33Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "documentation and defaults for the 'view' function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3145",
    "user": "@jhpalmieri"
}
```
Assignee: cwitty

Keywords: latex, view

I'm attaching a patch with, I suppose, three changes (two of which are minor) to the 'view' function:
1. longer (and I think clearer) documentation
2. no 'center' option anymore. I don't think centering things in displayed equations has any effect in LaTeX.
3. changed default value of 'sep' from '$$ $$' to *.  I have two reasons for this: I think the output looks better this way, and I think that the default value of '$$ $$' is misleading: someone might infer that it's playing the role of the variables 'math_left' and 'math_right' in _latex_file, when in fact it's just adding some vertical space between the output lines.  If you don't like having a default of *, then I would suggest changing it to something like '\\vspace{5mm}' which gives a better idea of what 'sep' actually does and even implies how one might change it (by changing the length).

Issue created by migration from https://trac.sagemath.org/ticket/3145





---

archive/issue_comments_021819.json:
```json
{
    "body": "patch to sage/misc/latex.py",
    "created_at": "2008-05-09T19:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3145#issuecomment-21819",
    "user": "@jhpalmieri"
}
```

patch to sage/misc/latex.py



---

archive/issue_comments_021820.json:
```json
{
    "body": "Attachment [latex.patch](tarball://root/attachments/some-uuid/ticket3145/latex.patch) by @jhpalmieri created at 2008-05-09 19:21:47\n\nSorry, I didn't look at the preview carefully enough.  In item 3, the default for 'sep' is changed from '$$ $$' to the empty string (two single quotes with no space between them), which I haven't yet figured out how to type here...",
    "created_at": "2008-05-09T19:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3145#issuecomment-21820",
    "user": "@jhpalmieri"
}
```

Attachment [latex.patch](tarball://root/attachments/some-uuid/ticket3145/latex.patch) by @jhpalmieri created at 2008-05-09 19:21:47

Sorry, I didn't look at the preview carefully enough.  In item 3, the default for 'sep' is changed from '$$ $$' to the empty string (two single quotes with no space between them), which I haven't yet figured out how to type here...



---

archive/issue_comments_021821.json:
```json
{
    "body": "mercurial patch (instead of diff), to replace previous patch",
    "created_at": "2008-05-25T16:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3145#issuecomment-21821",
    "user": "@jhpalmieri"
}
```

mercurial patch (instead of diff), to replace previous patch



---

archive/issue_comments_021822.json:
```json
{
    "body": "Attachment [3145.patch](tarball://root/attachments/some-uuid/ticket3145/3145.patch) by @craigcitro created at 2008-06-15 21:59:00",
    "created_at": "2008-06-15T21:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3145#issuecomment-21822",
    "user": "@craigcitro"
}
```

Attachment [3145.patch](tarball://root/attachments/some-uuid/ticket3145/3145.patch) by @craigcitro created at 2008-06-15 21:59:00



---

archive/issue_comments_021823.json:
```json
{
    "body": "Changing keywords from \"latex, view\" to \"latex, view, editor_wstein\".",
    "created_at": "2008-06-15T21:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3145#issuecomment-21823",
    "user": "@craigcitro"
}
```

Changing keywords from "latex, view" to "latex, view, editor_wstein".



---

archive/issue_comments_021824.json:
```json
{
    "body": "REFEREE REPORT:\n\n1. The new docs say \"If in notebook mode, this embeds a png image in the output.\".  That is not true.  view uses jsmath to typeset output -- this does not in any way involve png's.\n\n2. There absolutely have to be some doctests added, e.g., examples illustrating what this function does.  E.g., you can in the doctest set the system to be in EMBEDDED_MODE, then get html  output, or something. \n\n3. I agree with removing center and the sep, i.e., with the core changes.\n\n4.. I can't actually apply this patch to either sage-3.0.2 or sage-3.0.2.alpha2:\n\n```\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/3145/3145.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/3145/3145.patch?format=raw\nLoading: [.]\ncd \"/home/was/build/sage-3.0.3.alpha2/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.0.3.alpha2/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.0.3.alpha2/devel/sage\" && hg import   \"/home/was/.sage/temp/sage/32714/tmp_1.patch\"\napplying /home/was/.sage/temp/sage/32714/tmp_1.patch\npatching file sage/misc/latex.py\nHunk #1 FAILED at 423\nHunk #2 FAILED at 452\n2 out of 2 hunks FAILED -- saving rejects to file sage/misc/latex.py.rej\nabort: patch failed to apply\nsage: \n```\n\n\nSo please do what you can from above and let me know.",
    "created_at": "2008-06-16T00:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3145#issuecomment-21824",
    "user": "@williamstein"
}
```

REFEREE REPORT:

1. The new docs say "If in notebook mode, this embeds a png image in the output.".  That is not true.  view uses jsmath to typeset output -- this does not in any way involve png's.

2. There absolutely have to be some doctests added, e.g., examples illustrating what this function does.  E.g., you can in the doctest set the system to be in EMBEDDED_MODE, then get html  output, or something. 

3. I agree with removing center and the sep, i.e., with the core changes.

4.. I can't actually apply this patch to either sage-3.0.2 or sage-3.0.2.alpha2:

```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/3145/3145.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/3145/3145.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.0.3.alpha2/devel/sage" && hg status
cd "/home/was/build/sage-3.0.3.alpha2/devel/sage" && hg status
cd "/home/was/build/sage-3.0.3.alpha2/devel/sage" && hg import   "/home/was/.sage/temp/sage/32714/tmp_1.patch"
applying /home/was/.sage/temp/sage/32714/tmp_1.patch
patching file sage/misc/latex.py
Hunk #1 FAILED at 423
Hunk #2 FAILED at 452
2 out of 2 hunks FAILED -- saving rejects to file sage/misc/latex.py.rej
abort: patch failed to apply
sage: 
```


So please do what you can from above and let me know.



---

archive/issue_comments_021825.json:
```json
{
    "body": "Attachment [3145-new.patch](tarball://root/attachments/some-uuid/ticket3145/3145-new.patch) by @jhpalmieri created at 2008-06-16 04:59:19\n\nI've tried to address these issues.  I've also changed the documentation a little more, to reflect the fact that 'xdvi' is not required: dvi files are not necessarily displayed by xdvi -- see \n\n[http://trac.sagemath.org/sage_trac/ticket/3137](http://trac.sagemath.org/sage_trac/ticket/3137)\n\nSo I've tried to change the references to xdvi to be more accurate.",
    "created_at": "2008-06-16T04:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3145#issuecomment-21825",
    "user": "@jhpalmieri"
}
```

Attachment [3145-new.patch](tarball://root/attachments/some-uuid/ticket3145/3145-new.patch) by @jhpalmieri created at 2008-06-16 04:59:19

I've tried to address these issues.  I've also changed the documentation a little more, to reflect the fact that 'xdvi' is not required: dvi files are not necessarily displayed by xdvi -- see 

[http://trac.sagemath.org/sage_trac/ticket/3137](http://trac.sagemath.org/sage_trac/ticket/3137)

So I've tried to change the references to xdvi to be more accurate.



---

archive/issue_comments_021826.json:
```json
{
    "body": "(This latest patch was built using Sage 3.0.2.)",
    "created_at": "2008-06-16T05:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3145#issuecomment-21826",
    "user": "@jhpalmieri"
}
```

(This latest patch was built using Sage 3.0.2.)



---

archive/issue_comments_021827.json:
```json
{
    "body": "Attachment [sage-3145-new-part2of2.patch](tarball://root/attachments/some-uuid/ticket3145/sage-3145-new-part2of2.patch) by @williamstein created at 2008-06-19 23:33:44\n\npart 2 of 2",
    "created_at": "2008-06-19T23:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3145#issuecomment-21827",
    "user": "@williamstein"
}
```

Attachment [sage-3145-new-part2of2.patch](tarball://root/attachments/some-uuid/ticket3145/sage-3145-new-part2of2.patch) by @williamstein created at 2008-06-19 23:33:44

part 2 of 2



---

archive/issue_comments_021828.json:
```json
{
    "body": "I did some slight changes in the followup patch.  This is now good to go.\n\nApply sage-3145-new.patch and sage-3145-new-part2of2.patch.",
    "created_at": "2008-06-19T23:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3145#issuecomment-21828",
    "user": "@williamstein"
}
```

I did some slight changes in the followup patch.  This is now good to go.

Apply sage-3145-new.patch and sage-3145-new-part2of2.patch.



---

archive/issue_comments_021829.json:
```json
{
    "body": "Great, I was thinking about similar changes too.  I like it.",
    "created_at": "2008-06-20T02:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3145#issuecomment-21829",
    "user": "@jhpalmieri"
}
```

Great, I was thinking about similar changes too.  I like it.



---

archive/issue_comments_021830.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T11:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3145#issuecomment-21830",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021831.json:
```json
{
    "body": "Merged sage-3145-new.patch and sage-3145-new-part2of2.patch in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T11:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3145#issuecomment-21831",
    "user": "mabshoff"
}
```

Merged sage-3145-new.patch and sage-3145-new-part2of2.patch in Sage 3.0.4.alpha0
