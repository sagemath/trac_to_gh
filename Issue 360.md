# Issue 360: Port Cremona's implementation of elliptic curve height bounds to SAGE

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-04-27 16:15:33

Assignee: was

CC:  cremona pbruin

John Cremona has implemented a wide range of height bounds for elliptic curves in 
this magma program:

  http://www.maths.nott.ac.uk/personal/jec/ftp/progs/magma/nfhtbound.m

(see also attached file).  Upon my request he GPL'd this program.  Thus we can
legally port it line-by-line to SAGE.  

william


---

Attachment


---

Comment by roed created at 2007-10-13 00:32:41

Changing assignee from was to roed.


---

Comment by roed created at 2007-10-13 00:32:41

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-16 09:05:00

Has there been any progress here? What is the status of this in general? Now that John is a full Sage developer wouldn't it be something he would do the best job at?

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-07 04:03:47

Hi John,

I am curious how much of this code has found its way into Sage and it this ticket can be closed. I did add you to the CC field.

Cheers,

Michael


---

Comment by cremona created at 2008-04-07 08:21:23

Replying to [comment:4 mabshoff]:
> Hi John,
> 
> I am curious how much of this code has found its way into Sage and it this ticket can be closed. I did add you to the CC field.
> 

None of this is in Sage at all yet.  Over Q the functionality is there (provided by eclib) but not over number fields.

It's something I could do, yes.  So please keep the ticket open.

> Cheers,
> 
> Michael


---

Comment by mabshoff created at 2008-04-07 14:00:13

Replying to [comment:5 cremona]:
> Replying to [comment:4 mabshoff]:
> > Hi John,

Hi John,

> > 
> > I am curious how much of this code has found its way into Sage and it this ticket can be closed. I did add you to the CC field.
> > 
> 
> None of this is in Sage at all yet.  Over Q the functionality is there (provided by eclib) but not over number fields.
> 
> It's something I could do, yes.  So please keep the ticket open.

Sure. I just wanted to make sure that the ticket hadn't already been solved. If you plan to work on it you might want to take ownership of this ticket since roed is rather busy these days.
 
> > Cheers,
> > 
> > Michael

Cheers,

Michael


---

Comment by cremona created at 2008-04-07 19:42:15

By the way, before this (=height bounds) is done we should also implement heights on elliptic curves over number fields.  For this reason I have changed the ticket's summary description as well as taking ownership.


---

Comment by cremona created at 2008-04-07 19:42:15

Changing assignee from roed to cremona.


---

Comment by cremona created at 2008-04-07 19:42:15

Changing status from assigned to new.


---

Comment by davidloeffler created at 2009-07-20 19:45:43

Changing component from number theory to elliptic curves.


---

Comment by davidloeffler created at 2009-07-20 19:45:43

Assigned to new "elliptic curves" component.


---

Comment by cremona created at 2010-03-15 20:35:23

Implementation of heights in done in #8496 so should be available from 4.3.4.

Hence I changed the ticket's title back so that it only refers to height bounds.


---

Comment by chapoton created at 2018-04-04 18:12:59

Changing status from new to needs_info.


---

Comment by chapoton created at 2018-04-04 18:12:59

Is this still pertinent in any way ?


---

Comment by cremona created at 2018-04-04 18:34:24

It is all now implemented, by Robert Bradshaw with some input from me: see sage/schemes/elliptic_curves/height.py.  So this ticket is redundant.


---

Comment by chapoton created at 2018-04-04 18:35:02

thanks


---

Comment by chapoton created at 2018-04-04 18:35:02

Changing status from needs_info to positive_review.


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix
