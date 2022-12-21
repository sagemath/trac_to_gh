# Issue 386: Enhance "attach <file>" in the notebook

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-06-07 19:24:48

Assignee: boothby

I noticed that the natural progression for someone who starts to work with sage is that they start with using the notebook exclusively. Any "def"d functions are simply defined in a cell in the worksheet (with all scrollbar problems that go with it). As they progress, and want to test their routine in different situations, this method becomes cumbersome: they have to copy the cell content to other worksheets if they want to run tests in other worksheets and the usual problems arise by having several copies lying around: Edits in one version are not propagated to the other.

This would be the natural moment to explain that the user should put his/her routines in, say, file.sage instead and attach it in any worksheet that is used. Ultimately, the user should probably learn how to use an independent, high quality source code editor to work with the files, but it would be nice if there were an intermediate step: An easy way to create, edit and attach a file within the scope of the notebook, but accessible from all worksheets, much like the "saved objects".

A hackish way is the following, assuming that /home/nobody is writable for the notebook UID:

```
%sh
cat > /home/nobody/file.sage <<EOFEOFEOF
#######################################
## file.sage
def facto(n):
  if n == 1:
    return 1
  else:
    return n*facto(n-1)

EOFEOFEOF 
```

This causes all kinds of interesting errors, since the cell directory may not exist or may have been deleted by the system for, to me, no apparent reason. In all cases, however, the code has the desired effect of creating the file.

Now, after

```
attach "/home/nobody/file.sage"
```


the user can use the routine "facto" in the worksheet and in fact, editing the %sh cell and executing it will lead to sage rereading file.sage the next time around, effecting the edit in the worksheet.

Would it be possible to have a less hackish way of establishing this? In fact, once a full force source code editor is part of sage, perhaps the most useful thing would be if one could open a tab/window on one of those "attach" files rather than having to do the editing in cells.

I understand that the security implications of stuff like this are even worse than just the shielded environment and may require some serious thinking to resolve, but lowering the threshold of doing actual programming in sage should increase the number of developers/contributors.

While you're at it, why not put the files under mercurial control as well and provide some nice tools in the notebook to view the various revisions?


---

Comment by was created at 2009-11-19 21:21:49

I implemented this already... via the DATA --> Upload or Create File function.  That does exactly what this ticket is about.  Of course, this ticket has some vague revision control stuff, but that's too vague for a single ticket.  So I'm closing this.


---

Comment by was created at 2009-11-19 21:21:49

Resolution: fixed


---

Comment by mvngu created at 2009-12-08 23:40:07

Replying to [comment:2 was]:
> So I'm closing this. 

Do you know in which version of Sage was the feature described in this ticket was merged? If it was merged in Sage 4.3, was it alpha0 or alpha1?


---

Comment by was created at 2009-12-09 05:31:45

> Do you know in which version of Sage was the feature described in this ticket was 
> merged? If it was merged in Sage 4.3, was it alpha0 or alpha1? 

It was back in 2008 sometime...
