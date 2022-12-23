# Issue 4057: Possible improvements to ? and ?? for R functions

Issue created by migration from https://trac.sagemath.org/ticket/4057

Original creator: aginiewicz

Original creation time: 2008-09-04 03:13:47

Assignee: was

Things are different in notebook and console:

  * Because of underline trick, in notebook headings in docstring consists of only underline!
  * Source display in console would look better with additional new line char and one empty line after source output and before "Constructor Docstring", the docstring in console is better, underline trick works as expected, but there could also be one empty line before "Constructor Docstring"
    * btw - is Constructor Docstring really needed? I think the source is enough and we don't have to include same docstring for every R function, it's already available as docstring for r interpreter itself... it's not included in docstring in notebook so I guess we could live without it, if it is the case, no need to add empty line before it!
  * getting source of R function through notebook by ?? don't work at all...


---

Comment by aginiewicz created at 2008-09-04 03:15:04

a simple (and probably not best) way to deal with "underline only" problem in notebook docstring for R functions


---

Comment by mabshoff created at 2008-09-04 03:15:50

Resolution: invalid


---

Attachment

Hi,

this is some laundry list of things and should be first discussed on sage-devel before opening clearly defined tickets. Trac is not a discussion forum :)

Invalid.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-04 03:25:45

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-09-04 03:25:45

Resolution changed from invalid to 


---

Comment by aginiewicz created at 2008-09-04 03:34:00

when limited to one issue, defect seems to fit better to this one...


---

Comment by aginiewicz created at 2008-09-04 03:34:00

Changing type from enhancement to defect.


---

Comment by aginiewicz created at 2008-09-04 04:15:33

Changing status from reopened to new.


---

Comment by aginiewicz created at 2008-09-04 04:15:33

Changing assignee from was to aginiewicz.


---

Comment by aginiewicz created at 2008-09-04 04:15:33

(forgot to assign ticket to myself)


---

Comment by TimothyClemans created at 2008-09-08 11:45:41

See http://sage.math.washington.edu/home/tclemans/R_docstring_before_after.png for the before and after screenshots.


---

Comment by aginiewicz created at 2008-09-15 21:10:21

better solution to problem


---

Attachment

I attached better fix of problem, it fixes not only the r.sth? notation but also not fixed by previous - r.help("sth") - also it doesn't add check related to R in generic module so I guess previous was bad


---

Comment by was created at 2008-11-27 18:31:32

apply this and the patch right above this.


---

Attachment

REFEREE REPORT:

Looks good, but needs to *only* delete the underline in embedded mode.  I've attached a patch to do that.


---

Comment by mabshoff created at 2008-11-28 21:52:04

Resolution: fixed


---

Comment by mabshoff created at 2008-11-28 21:52:04

Merged underline_trick.2.patch and sage-4057-part2.patch in Sage 3.2.1.rc0.

Andrzej: Your patch was a diff, please make sure to post proper hg patches in the future. I have committed this patch in your name to the repo for proper credit.

Cheers,

Michael


---

Comment by aginiewicz created at 2008-11-28 23:41:01

I know, the patch was attached before the one from which I found out earlier you prefer hg patch :)...

thanks for including this anyway,
cheers,
Andrzej.
