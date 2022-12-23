# Issue 5148: corrections to Andrey Novoseltsev's devmap entry

Issue created by migration from https://trac.sagemath.org/ticket/5148

Original creator: mvngu

Original creation time: 2009-02-01 05:50:56

Assignee: tba

CC:  mabshoff schilly

Keywords: devmap

As the subject says. The corrections was pointed out by Michael Abshoff. This is a joint effort with Michael Abshoff and Harald Schilly.


---

Attachment

The patch `trac_5148.patch` makes some corrections to the details of Andrey Novoseltsev in the Sage [dev-map](http://www.sagemath.org/development-map.html). The diff was generated against this XML file:



http://www.sagemath.org/res/contributors.xml


---

Comment by mabshoff created at 2009-02-02 01:59:27

This might be troublesome to import into the hg repo, but Harald will see that.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 02:02:50

Harald, 

please let us know via a comment on the ticket that you have updated the Dev map. I will then properly close this ticket.

Cheers,

Michael


---

Comment by schilly created at 2009-02-02 11:08:14

Replying to [comment:3 mabshoff]:
> please let us know via a comment on the ticket that you have updated the Dev map. I will then properly close this ticket.

Hi, the "problem" is, there are now two websites, the current one and the new one. I've edited the current one and the new one, so you can close this ticket now. But I want to avoid this duplicate work in the future.

Also for the future, it would be easier if you, mvngu, just send me the new .xml file with all edits at once and no diffs.


---

Comment by mabshoff created at 2009-02-02 17:53:38

Resolution: fixed


---

Comment by mabshoff created at 2009-02-02 17:53:38

Updated on the website during the Sage 3.3 release cycle.

Cheers,

Michael


---

Comment by mvngu created at 2009-02-03 00:54:41

Replying to [comment:4 schilly]:
> Also for the future, it would be easier if you, mvngu, just send me the new .xml file with all edits at once and no diffs. 
Do you mean a process like this: Download the XML file http://www.sagemath.org/res/contributors.xml and edit it. Then attach the locally modified XML file to a ticket and CC you on that ticket? Or email the modified XML file to your Gmail account?


---

Comment by schilly created at 2009-02-03 09:36:56

Replying to [comment:6 mvngu]:
> Do you mean a process like this: Download the XML file http://www.sagemath.org
> /res/contributors.xml and edit it. Then attach the locally modified XML file to a ticket and CC 
> you on that ticket? 

yes, attach to a ticket is the best way, because i can download it directly from trac into the web directory (1-step) and you know exactly what's on the web. i'm also not updating it, since i'm emailing you changes i would do - do don't worry with diffs! Therefore you can also bunch together all changes in one ticket.

greez h


---

Comment by mabshoff created at 2009-02-03 15:38:00

I would still like to see diffs since they make it obvious what changed and in case something goes wrong it is much easier to see *what* happened when.

Cheers,

Michael


---

Comment by schilly created at 2009-02-03 15:40:10

Replying to [comment:8 mabshoff]:
> I would still like to see diffs since they make it obvious what changed and in case something goes wrong it is much easier to see *what* happened when.
> 

ok, well, good point.
