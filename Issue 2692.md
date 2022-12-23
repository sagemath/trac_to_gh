# Issue 2692: [with patch; needs review] bug displaying list of published worksheets

Issue created by migration from https://trac.sagemath.org/ticket/2692

Original creator: was

Original creation time: 2008-03-28 00:39:36

Assignee: boothby




---

Attachment


```
[08:24] <mabshoff> wstein: What was the issue with "internal server error" and the notebook?
[08:24] <wstein> There was just a 1-line bug in making a list of user names.
[08:24] <mabshoff> ok
[08:24] <wstein> This came up in displaying the list of published notebooks.
[08:25] <wstein> I think it was never hit before because whatever combinations of events needed hadn't
[08:25] <wstein> been triggerd.
[08:25] <wstein> But with 2,800 accounts on sagenb.org, that sort of thing is bound to come up, I guess.
[08:25] <mabshoff> ok. is that a ticket yet?
[08:25] <mabshoff> :)
[08:25] <wstein> It's a ticket and fixed.
[08:25] <mabshoff> ok. Did I miss that or isn't it merged yet?
[08:25] <wstein> http://trac.sagemath.org/sage_trac/ticket/2692
[08:26] <mabshoff> k
[08:26] <mabshoff> So join() failed in that case?
[08:26] <wstein> modabvar coverage is currently 77%
[08:26] <wstein> Yes, since join takes strings.
[08:27] <mabshoff> ok, positive review then.
[08:27] <mabshoff> It seems that it worked by accident previously?
[08:27] <wstein> yep
[08:27] <mabshoff> :)
```



---

Comment by mabshoff created at 2008-03-28 08:04:02

Resolution: fixed


---

Comment by mabshoff created at 2008-03-28 08:04:02

Merged in Sage 2.11.alpha2
