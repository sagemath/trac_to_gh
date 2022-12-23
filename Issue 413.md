# Issue 413: saving non-evaluated cells

Issue created by migration from https://trac.sagemath.org/ticket/413

Original creator: was

Original creation time: 2007-08-09 07:45:41

Assignee: boothby


```
On 8/6/07, Ted Kosan <ted.kosan@gmail.com> wrote:
> I am in the process of developing a standard format that typical
> students can follow when using the Sage notebook.  Part of this
> pattern consists of creating cells which contain only comments, like
> the description of a problem that is being solved.  Since comments are
> not executable code, a person would not normally think to press
> <shift><enter> in these cells.
> 
> Unfortunately, if text is entered into a cell without pressing
> <shift><enter>, this text is lost even after the "Save" or "Save and
> close" buttons are pressed.
> 
> Can the behavior of these buttons be changed so that all text in all
> cells is saved when they are pressed?

Yes, definitely.
```



---

Comment by was created at 2007-08-09 07:48:12


```
I think actually whenever text in any cell has changed and

   (1) the cell looses focus, or
   (2) the user clicks "save",

then the contents of that cell should be sent back to the server.
I hate entering a little comment at the top of an input
cell before a 20-second computation, and having to re-run
the computation just to record the comment. 
```



---

Comment by boothby created at 2008-03-17 04:17:30

Resolution: duplicate


---

Comment by boothby created at 2008-03-17 04:17:30

duplicated by #1590
