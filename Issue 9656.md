# Issue 9656: Code blocks in the notebook's interactive help get code overlaping it'self

Issue created by migration from Trac.

Original creator: olazo

Original creation time: 2010-08-01 02:32:38

Assignee: olazo

CC:  acleone was mpatel jason

This was reported some time ago in sage-support. As the reporter said, a picture is worth a thousand words, so here's a screenshot.


---

Attachment


---

Attachment

Forces Firefox to recompute span width after jsMath text processing.


---

Comment by timdumol created at 2010-08-19 12:58:58

The problem was caused by jsMath's text processing altering the widths of the spans in the code blocks, without Firefox repositioning and recomputing the widths. This should fix the problem.


---

Comment by timdumol created at 2010-08-19 12:58:58

Changing status from new to needs_review.


---

Comment by mhampton created at 2010-09-17 11:30:53

Changing status from needs_review to needs_work.


---

Comment by mhampton created at 2010-09-17 11:30:53

This fixes the kerning issue but degrades the appearance of code blocks.  Now code examples do not have a white background but do have a little bit of white at the ends of each line, which I think definitely looks worse.  I am not well enough versed in html and css to figure out how to fix this.

I am attaching some screenshots to make this clearer.


---

Comment by mhampton created at 2010-09-17 11:32:02

Note white background example code blocks


---

Attachment

Now only a trailing white background piece within code block.


---

Comment by timdumol created at 2010-09-18 02:43:54

Simplified changes into a one-line patch. Replaces previous.


---

Comment by timdumol created at 2010-09-18 02:44:41

Changing status from needs_work to needs_review.


---

Attachment

Thanks for noting that. I didn't notice. Here's another, simpler, patch.


---

Comment by mhampton created at 2010-09-19 21:48:54

The trac_9556-code-blocks-kerning.2.patch  patch doesn't seem to work for me at all - by that I mean it doesn't fix the kerning issue.  I made a modified sagenb package, did "sage -f sagenb-0.8.2.spkg", and rebuilt everything.


---

Comment by mhampton created at 2010-09-19 21:49:02

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2014-12-19 04:14:22

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

Comment by embray created at 2018-08-10 09:46:06

This appears to be fixed, at least for the examples mentioned in this ticket.  Since SageNB has its own codebase now it's possible it was fixed there without being mentioned back here.  Any future issues against SageNB should be opened at https://github.com/sagemath/sagenb preferably.


---

Comment by embray created at 2018-08-10 09:46:06

Resolution: worksforme


---

Comment by kcrisman created at 2018-08-10 13:11:02

Just for reference, many of the sagenb tickets on Trac were mentioned upstream as cross-links; apparently this one (?) was missed.  The rationale was that for any other upstream project (e.g. Maxima), we'd want a ticket on Trac to confirm it.


---

Comment by embray created at 2018-08-10 13:29:58

Yes, that makes sense.  Often the issue is caught as a "sage bug" first, and an "upstream bug" second.
