# Issue 3555: [with patch; needs review] notebook -- fix bug where it saved the notebook every tie it checked for idle worksheets

archive/issues_003555.json:
```json
{
    "body": "Assignee: boothby\n\nThe attached patch fixed a tiny bug in the notebook where it was saving the notebook to disk whenever checking for idle timeouts on worksheets.  Since the idle timeout check is small this had major unintended consequences in that it was constantly causing the notebook to get saved to disk *twice*.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3555\n\n",
    "created_at": "2008-07-06T00:06:04Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch; needs review] notebook -- fix bug where it saved the notebook every tie it checked for idle worksheets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3555",
    "user": "was"
}
```
Assignee: boothby

The attached patch fixed a tiny bug in the notebook where it was saving the notebook to disk whenever checking for idle timeouts on worksheets.  Since the idle timeout check is small this had major unintended consequences in that it was constantly causing the notebook to get saved to disk *twice*.

Issue created by migration from https://trac.sagemath.org/ticket/3555





---

archive/issue_comments_025142.json:
```json
{
    "body": "Attachment [sage-3555.patch](tarball://root/attachments/some-uuid/ticket3555/sage-3555.patch) by mabshoff created at 2008-07-06 09:17:02\n\nPatch looks good to me:\n\n```\n[02:12am] mabshoff: wstein: I am looking at #3555:\n[02:12am] mabshoff: The logic is that the notebook has been idle for some amount of time.\n[02:13am] wstein: yes.\n[02:13am] wstein: Those functions get called every so often.\n[02:13am] mabshoff: Well, some worksheets which have been idle for some time get terminated.\n[02:13am] wstein: If the elapsed walltime is sufficiently large they do something and reset their timer.\n[02:13am] mabshoff: But we do not save the notebook in that case since we do it in some other place already?\n[02:13am] wstein: More precisely \"idle and not being viewed\"\n[02:13am] wstein: Yes.\n[02:14am] mabshoff: ok\n[02:14am] mabshoff: Patch looks go to me and I will merge it then now.\n[02:14am] wstein: It was just me being way too paranoid before because the early notebook\n[02:14am] wstein: crashed a lot.\n[02:14am] wstein: OK.\n[02:14am] mabshoff: Yes.\n[02:14am] mabshoff: I don't recall the notebook server crashing.\n[02:14am] wstein: That was before your time.\n```\n",
    "created_at": "2008-07-06T09:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3555#issuecomment-25142",
    "user": "mabshoff"
}
```

Attachment [sage-3555.patch](tarball://root/attachments/some-uuid/ticket3555/sage-3555.patch) by mabshoff created at 2008-07-06 09:17:02

Patch looks good to me:

```
[02:12am] mabshoff: wstein: I am looking at #3555:
[02:12am] mabshoff: The logic is that the notebook has been idle for some amount of time.
[02:13am] wstein: yes.
[02:13am] wstein: Those functions get called every so often.
[02:13am] mabshoff: Well, some worksheets which have been idle for some time get terminated.
[02:13am] wstein: If the elapsed walltime is sufficiently large they do something and reset their timer.
[02:13am] mabshoff: But we do not save the notebook in that case since we do it in some other place already?
[02:13am] wstein: More precisely "idle and not being viewed"
[02:13am] wstein: Yes.
[02:14am] mabshoff: ok
[02:14am] mabshoff: Patch looks go to me and I will merge it then now.
[02:14am] wstein: It was just me being way too paranoid before because the early notebook
[02:14am] wstein: crashed a lot.
[02:14am] wstein: OK.
[02:14am] mabshoff: Yes.
[02:14am] mabshoff: I don't recall the notebook server crashing.
[02:14am] wstein: That was before your time.
```




---

archive/issue_comments_025143.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-06T09:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3555#issuecomment-25143",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025144.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-06T09:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3555#issuecomment-25144",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha2
