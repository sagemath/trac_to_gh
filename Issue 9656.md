# Issue 9656: Code blocks in the notebook's interactive help get code overlaping it'self

archive/issues_009656.json:
```json
{
    "body": "Assignee: olazo\n\nCC:  acleone @williamstein @qed777 @jasongrout\n\nThis was reported some time ago in sage-support. As the reporter said, a picture is worth a thousand words, so here's a screenshot.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9656\n\n",
    "created_at": "2010-08-01T02:32:38Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Code blocks in the notebook's interactive help get code overlaping it'self",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9656",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```
Assignee: olazo

CC:  acleone @williamstein @qed777 @jasongrout

This was reported some time ago in sage-support. As the reporter said, a picture is worth a thousand words, so here's a screenshot.

Issue created by migration from https://trac.sagemath.org/ticket/9656





---

archive/issue_comments_093558.json:
```json
{
    "body": "Attachment [ugly_help.png](tarball://root/attachments/some-uuid/ticket9656/ugly_help.png) by olazo created at 2010-08-01 02:33:10",
    "created_at": "2010-08-01T02:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93558",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Attachment [ugly_help.png](tarball://root/attachments/some-uuid/ticket9656/ugly_help.png) by olazo created at 2010-08-01 02:33:10



---

archive/issue_comments_093559.json:
```json
{
    "body": "Attachment [trac_9556-code-blocks-kerning.patch](tarball://root/attachments/some-uuid/ticket9656/trac_9556-code-blocks-kerning.patch) by @TimDumol created at 2010-08-19 12:56:27\n\nForces Firefox to recompute span width after jsMath text processing.",
    "created_at": "2010-08-19T12:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93559",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_9556-code-blocks-kerning.patch](tarball://root/attachments/some-uuid/ticket9656/trac_9556-code-blocks-kerning.patch) by @TimDumol created at 2010-08-19 12:56:27

Forces Firefox to recompute span width after jsMath text processing.



---

archive/issue_comments_093560.json:
```json
{
    "body": "The problem was caused by jsMath's text processing altering the widths of the spans in the code blocks, without Firefox repositioning and recomputing the widths. This should fix the problem.",
    "created_at": "2010-08-19T12:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93560",
    "user": "https://github.com/TimDumol"
}
```

The problem was caused by jsMath's text processing altering the widths of the spans in the code blocks, without Firefox repositioning and recomputing the widths. This should fix the problem.



---

archive/issue_comments_093561.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-19T12:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93561",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093562.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-17T11:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93562",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093563.json:
```json
{
    "body": "This fixes the kerning issue but degrades the appearance of code blocks.  Now code examples do not have a white background but do have a little bit of white at the ends of each line, which I think definitely looks worse.  I am not well enough versed in html and css to figure out how to fix this.\n\nI am attaching some screenshots to make this clearer.",
    "created_at": "2010-09-17T11:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93563",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This fixes the kerning issue but degrades the appearance of code blocks.  Now code examples do not have a white background but do have a little bit of white at the ends of each line, which I think definitely looks worse.  I am not well enough versed in html and css to figure out how to fix this.

I am attaching some screenshots to make this clearer.



---

archive/issue_comments_093564.json:
```json
{
    "body": "Note white background example code blocks",
    "created_at": "2010-09-17T11:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93564",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Note white background example code blocks



---

archive/issue_comments_093565.json:
```json
{
    "body": "Attachment [afterpatch.png](tarball://root/attachments/some-uuid/ticket9656/afterpatch.png) by mhampton created at 2010-09-17 11:32:31\n\nNow only a trailing white background piece within code block.",
    "created_at": "2010-09-17T11:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93565",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [afterpatch.png](tarball://root/attachments/some-uuid/ticket9656/afterpatch.png) by mhampton created at 2010-09-17 11:32:31

Now only a trailing white background piece within code block.



---

archive/issue_comments_093566.json:
```json
{
    "body": "Simplified changes into a one-line patch. Replaces previous.",
    "created_at": "2010-09-18T02:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93566",
    "user": "https://github.com/TimDumol"
}
```

Simplified changes into a one-line patch. Replaces previous.



---

archive/issue_comments_093567.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-18T02:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93567",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093568.json:
```json
{
    "body": "Attachment [trac_9556-code-blocks-kerning.2.patch](tarball://root/attachments/some-uuid/ticket9656/trac_9556-code-blocks-kerning.2.patch) by @TimDumol created at 2010-09-18 02:44:41\n\nThanks for noting that. I didn't notice. Here's another, simpler, patch.",
    "created_at": "2010-09-18T02:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93568",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_9556-code-blocks-kerning.2.patch](tarball://root/attachments/some-uuid/ticket9656/trac_9556-code-blocks-kerning.2.patch) by @TimDumol created at 2010-09-18 02:44:41

Thanks for noting that. I didn't notice. Here's another, simpler, patch.



---

archive/issue_comments_093569.json:
```json
{
    "body": "The trac_9556-code-blocks-kerning.2.patch  patch doesn't seem to work for me at all - by that I mean it doesn't fix the kerning issue.  I made a modified sagenb package, did \"sage -f sagenb-0.8.2.spkg\", and rebuilt everything.",
    "created_at": "2010-09-19T21:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93569",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

The trac_9556-code-blocks-kerning.2.patch  patch doesn't seem to work for me at all - by that I mean it doesn't fix the kerning issue.  I made a modified sagenb package, did "sage -f sagenb-0.8.2.spkg", and rebuilt everything.



---

archive/issue_comments_093570.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-19T21:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93570",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093571.json:
```json
{
    "body": "I haven't seen this in a while, but I'm not sure if it could still happen with MathJax.\n\nCurrent code, however in roughly the same place and same file\n\n```\n // Call MathJax on the final output.\nif (status === 'd' ) {\ntry {\nMathJax.Hub.Queue([\"Typeset\",MathJax.Hub,cell_output]);\n} catch (e) {\ncell_output.innerHTML = 'Error typesetting mathematics' + cell_output.innerHTML;\ncell_output_nowrap.innerHTML = 'Error typesetting mathematics' +\ncell_output_nowrap.innerHTML;\n}\n}\n```\n",
    "created_at": "2014-12-19T04:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93571",
    "user": "https://github.com/kcrisman"
}
```

I haven't seen this in a while, but I'm not sure if it could still happen with MathJax.

Current code, however in roughly the same place and same file

```
 // Call MathJax on the final output.
if (status === 'd' ) {
try {
MathJax.Hub.Queue(["Typeset",MathJax.Hub,cell_output]);
} catch (e) {
cell_output.innerHTML = 'Error typesetting mathematics' + cell_output.innerHTML;
cell_output_nowrap.innerHTML = 'Error typesetting mathematics' +
cell_output_nowrap.innerHTML;
}
}
```




---

archive/issue_comments_093572.json:
```json
{
    "body": "This appears to be fixed, at least for the examples mentioned in this ticket.  Since SageNB has its own codebase now it's possible it was fixed there without being mentioned back here.  Any future issues against SageNB should be opened at https://github.com/sagemath/sagenb preferably.",
    "created_at": "2018-08-10T09:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93572",
    "user": "https://github.com/embray"
}
```

This appears to be fixed, at least for the examples mentioned in this ticket.  Since SageNB has its own codebase now it's possible it was fixed there without being mentioned back here.  Any future issues against SageNB should be opened at https://github.com/sagemath/sagenb preferably.



---

archive/issue_comments_093573.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2018-08-10T09:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93573",
    "user": "https://github.com/embray"
}
```

Resolution: worksforme



---

archive/issue_comments_093574.json:
```json
{
    "body": "Just for reference, many of the sagenb tickets on Trac were mentioned upstream as cross-links; apparently this one (?) was missed.  The rationale was that for any other upstream project (e.g. Maxima), we'd want a ticket on Trac to confirm it.",
    "created_at": "2018-08-10T13:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93574",
    "user": "https://github.com/kcrisman"
}
```

Just for reference, many of the sagenb tickets on Trac were mentioned upstream as cross-links; apparently this one (?) was missed.  The rationale was that for any other upstream project (e.g. Maxima), we'd want a ticket on Trac to confirm it.



---

archive/issue_comments_093575.json:
```json
{
    "body": "Yes, that makes sense.  Often the issue is caught as a \"sage bug\" first, and an \"upstream bug\" second.",
    "created_at": "2018-08-10T13:29:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9656#issuecomment-93575",
    "user": "https://github.com/embray"
}
```

Yes, that makes sense.  Often the issue is caught as a "sage bug" first, and an "upstream bug" second.
