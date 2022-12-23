# Issue 2067: tutorial 5.3 misformatting

Issue created by migration from https://trac.sagemath.org/ticket/2067

Original creator: ljpk

Original creation time: 2008-02-05 22:39:43

Assignee: tba

In Section 5.3 of the tutorial, the following string is misformatted:

"bash ./factor20062*17*59bash "


---

Comment by mabshoff created at 2008-09-14 13:36:29

Mmh, is this still a problem? I am not even sure which section to check.

Cheers,

Michael


---

Comment by mvngu created at 2008-09-19 20:41:13

Replying to [ticket:2067 ljpk]:
> In Section 5.3 of the tutorial, the following string is misformatted:
> 
> "bash ./factor20062*17*59bash "


By "tutorial", I assume this refers to the official tutorial on Sage. Then "Section 5.3" of that tutorial can be found online [here](http://www.sagemath.org/doc/tut/node55.html), which shows this

```
bash $ ./factor 2006
2 * 17 * 59
```

The same snippet can also be found within the [PDF version](http://www.sagemath.org/doc-pdf/tut.pdf) of the official tutorial, on page 76. In both the online and PDF versions, I don't see any misformatting at all.

Regards,

Minh Van Nguyen


---

Comment by mvngu created at 2008-09-19 21:08:24

Changing assignee from tba to mvngu.


---

Comment by mabshoff created at 2008-09-19 22:10:52

Yeah, looks fixed to me. Closed. Thanks for tracking this down.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-19 22:10:52

Resolution: fixed
