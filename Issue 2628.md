# Issue 2628: Literate notebook

Issue created by migration from Trac.

Original creator: dunfield

Original creation time: 2008-03-21 15:42:05

Assignee: boothby

A key advantage of notebook interfaces over the command-line is that they can allow for literate programming, that is, interspersing of formated text and code.  Literate programming  allows the user to explore their ideas both in theory and code simultaneously, and is particularly useful in mathematics were writing comments in pure ASCII is cumbersome and distracting.   Moreover, literate notebooks can be used as record of a computation (e.g. as the basis for an appendix to a paper), as an interactive tutorial for Sage, or for education (e.g. a calculus notebook using the "interact" feature to explore quadric surfaces).   Both Mathematica and Maple have extensive literate programming features. 

A simple way to provide this in Sage would be to have input cells of type "%latex" and "%html" behave as follows.  

1) After (successfully) evaluating such a cell, the input would be hidden and only the output would be shown.  This output would be shifted to the left compared to where it is now so that the Sage input/output is indented relative to the text.  

2) To edit, the user would (double?) click on the output and the input box would reappear.  

See the attached files for an example worksheet with mock-up of output.

Overlap with SageTeX:

Dan Drake's excellent SageTeX also provides literate programming for Sage.   In practice, this is rather different than what is proposed here.   In particular, SageTeX is awkward to use to write Sage code in compared to the notebook because because of the multi-step (latex/sage/latex) process.   The strength of SageTeX is the quality of the final output and the fact that you have the whole of LaTeX to work with.   It would be nice if the notebook was able to export a SageTeX file.  (cf. Ticket #66)




---

Comment by dunfield created at 2008-03-21 15:43:11

Mockup


---

Attachment

"Source" for mockup


---

Attachment


---

Comment by dunfield created at 2008-04-03 12:08:12

In a sage-dev thread where folks also requested this feature, William pointed out the following work-around:

Have you ever tried clicking the blue edit button in the upper right side of the screen?  It gives you a plain text representation  of the worksheet.  You can enter arbitrary HTML between the  cells (the !` `), and it appears looking more professional  when you click the "Save and Use" button.   In fact, internally  all the text between subsequent !` ` compute cells *is*  a TextCell.  There is also one bonus -- if you put math in $'s or $$'s, it will get typeset as mathematics.


---

Comment by mhansen created at 2009-01-19 13:53:40

I think this can probably be closed since TinyMCE (at #4705) was added.


---

Comment by mhansen created at 2009-01-19 13:53:46

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2009-01-19 13:53:46

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-22 09:38:37

Resolution: fixed


---

Comment by mhansen created at 2009-01-22 09:38:37

I put a link on #66 back to this ticket.  I think we can close this now as being fixed by TinyMCE.
