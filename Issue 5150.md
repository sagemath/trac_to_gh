# Issue 5150: update Nils-Peter Skoruppa's contributions

Issue created by migration from https://trac.sagemath.org/ticket/5150

Original creator: mvngu

Original creation time: 2009-02-01 12:34:08

Assignee: tba

CC:  mabshoff schilly

Keywords: devmap

As the subject says. The devmap entry of Nils-Peter Skoruppa as listed at



http://www.sagemath.org/development-map.html



doesn't do justice to his contributions. Looking through #3857, notice that he has also contributed to optimizing some binary quadratic forms code.


---

Attachment

The patch `trac_5150.patch` can be applied after applying that of #5148.


---

Comment by mabshoff created at 2009-02-02 01:59:45

This might be troublesome to import into the hg repo, but Harald will see that.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 17:55:32

Harald: #5148 seems to have made it to the website, but this one doesn't seem to have made it yet.


Cheers,

Michael


---

Comment by schilly created at 2009-02-02 18:21:00

Replying to [comment:3 mabshoff]:
> Harald: #5148 seems to have made it to the website, but this one doesn't seem to have made it yet.

oh thx, there were two of them. i changed the order of the listed conributions to begin with something specific and then the non specific item.

note to myself: updated old and new website.


---

Comment by mabshoff created at 2009-02-02 18:23:02

Replying to [comment:4 schilly]:
> Replying to [comment:3 mabshoff]:
> > Harald: #5148 seems to have made it to the website, but this one doesn't seem to have made it yet.
> 
> oh thx, there were two of them. i changed the order of the listed conributions to begin with something specific and then the non specific item.

Cool. Let me know when you are done so I can close this ticket.

> note to myself: updated old and new website.

new website == website on the new VMware image? I updated lrs last night, so hopefully that update won't get lost.

Cheers,

Michael


---

Comment by schilly created at 2009-02-02 18:27:04

Replying to [comment:5 mabshoff]:
> Cool. Let me know when you are done so I can close this ticket.

yes, all done

> 
> > note to myself: updated old and new website.
> 
> new website == website on the new VMware image? I updated lrs last night, so hopefully that update won't get lost.

lrs? please don't overwrite the edited files! william has already deleted them once. since python is newer, i had to edit scripts, changed symlinks, etc. *begging* :)

greetings harald


---

Comment by mabshoff created at 2009-02-02 18:29:29

Replying to [comment:6 schilly]:

> lrs? please don't overwrite the edited files! 

lrs is an spkg, I just ran gen_html. If I am not supposed to do that I won't do it any more.

> william has already deleted them once. since python is newer, i had to edit scripts, changed symlinks, etc. *begging* :)

:)

> greetings harald

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 18:29:47

Updated on the website during the Sage 3.3 release cycle.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 18:29:47

Resolution: fixed
