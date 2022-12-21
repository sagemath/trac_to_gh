# Issue 3555: [with patch; needs review] notebook -- fix bug where it saved the notebook every tie it checked for idle worksheets

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-06 00:06:04

Assignee: boothby

The attached patch fixed a tiny bug in the notebook where it was saving the notebook to disk whenever checking for idle timeouts on worksheets.  Since the idle timeout check is small this had major unintended consequences in that it was constantly causing the notebook to get saved to disk *twice*.


---

Attachment

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

Comment by mabshoff created at 2008-07-06 09:19:35

Resolution: fixed


---

Comment by mabshoff created at 2008-07-06 09:19:35

Merged in Sage 3.0.4.alpha2
