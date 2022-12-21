# Issue 406: notebook -- improve support for other system modes

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-07-27 03:01:47

Assignee: boothby


```
On 7/26/07, Dan Christensen <jdc`@`uwo.ca> wrote:
> Some other minor issues about using GAP within the notebook, under
> 2.7.1.  I've put my entire worksheet in GAP mode using the menu at
> the top.  The following things don't work correctly:
> 
> 0) If I type something that gives an error in GAP, the error
> message is buried in a python exception/backtrace.
> 
> 1) If I type "?SymmetricGroup" (which works within GAP), all I see
> is
> 
>    Help: Showing `Reference: SymmetricGroup'
>    Page from 104
> 
> It's similar with other "?foo" commands.
> 
> 2) If I type "SymmetricGroup?" and hit tab, it shows me help about
> sage's wrapped SymmetricGroup function.  I don't think this will
> be helpful for functions not wrapped by sage.
> 
> 3) When I try to use tab completion, it inserts "gap." before the
> command (and probably ignores functions not wrapper by sage).

I am aware of each of these issues (which also happen with
the other interfaces).  They are *not* features in my mind, but
bugs, and they need to be fixed by somebody (either me or
somebody else). 

William
```



---

Comment by jdc created at 2007-07-27 16:46:15

4) If I use GAP Print(...) commands in a short notebook entry, I see the output.  But if the entry is longer, I don't see the output.


---

Comment by was created at 2008-05-10 21:27:18

In order to focus this ticket, I've broken up each issue into separate
tickets and made this ticket just issue 3 in the original description, which is below

```
On 7/26/07, Dan Christensen <jdc`@`uwo.ca> wrote:
> Some other minor issues about using GAP within the notebook, under
> 2.7.1.  I've put my entire worksheet in GAP mode using the menu at
> the top.  The following things don't work correctly:
> 
> 0) If I type something that gives an error in GAP, the error
> message is buried in a python exception/backtrace.
> 
> 1) If I type "?SymmetricGroup" (which works within GAP), all I see
> is
> 
>    Help: Showing `Reference: SymmetricGroup'
>    Page from 104
> 
> It's similar with other "?foo" commands.
> 
> 2) If I type "SymmetricGroup?" and hit tab, it shows me help about
> sage's wrapped SymmetricGroup function.  I don't think this will
> be helpful for functions not wrapped by sage.
> 
> 3) When I try to use tab completion, it inserts "gap." before the
> command (and probably ignores functions not wrapper by sage).

I am aware of each of these issues (which also happen with
the other interfaces).  They are *not* features in my mind, but
bugs, and they need to be fixed by somebody (either me or
somebody else). 

William
```



---

Attachment


---

Comment by was created at 2008-05-10 22:13:33

Changing priority from major to blocker.


---

Comment by was created at 2008-05-10 22:13:33

Changing type from enhancement to defect.


---

Comment by was created at 2008-05-10 22:13:33

Trac #406:

    1. Fix the problem where hitting tab when switched into another worksheet
       mode sticks system. at the front of each completion.  Similar fixes 
       for help via foo([tab key}] and source code via foo??[tab]. 

    2. When switching systems, get rid of the very annoying 
       confirmation dialog.   (Just commented it out for now.)

    3. Fix *very serious* bug that prevented loading a worksheet that was set
       to an optional mode.   In sage-3.0.1 loading a worksheet that is in
       an optional mode (e.g., mathematica or maple or Magma, say) was
       completely broken.  This patch fixes that problem. 

NOTE: This patch has no new tests illustrating that ift fixes
anything, since we have no automated way of testing any of the
above right now.


---

Comment by nbruin created at 2008-05-11 00:06:42

Patch works for me -- I have only tested that tab completion for magma is now useful.
In terms of refereeing the patch, I only understood the x[len(prepend):] bit and that seems plausible to me.


---

Comment by mhampton created at 2008-05-12 09:04:53

This seems to fix the problem (part 3, that is, the others are #3152).  I tested it in R mode, latex mode, gap mode, and python mode.  All of these saved/reloaded OK, and were robust under switching between modes.  Command completion appears fixed in R and gap (btw it would be pretty cool to have latex command completion but I assume that would be a pain).  
Since this is a second opinion I think it is time to give a full positive review and start merging it in.


---

Comment by mabshoff created at 2008-05-12 10:59:39

Merged in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-12 10:59:39

Resolution: fixed
