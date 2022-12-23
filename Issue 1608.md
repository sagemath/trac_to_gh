# Issue 1608: jsmath fonts -- these should ship with Sage itself and be *vastly* easier to install

Issue created by migration from https://trac.sagemath.org/ticket/1608

Original creator: was

Original creation time: 2007-12-27 04:31:05

Assignee: boothby

CC:  was mhansen jason kini

It is incredibly confusing for most people to install the jsmath fonts.  Morever, that they must download them off an external site is terrible -- what if they install Sage on an internal network or laptop with no net access, and need the fonts.  The fonts should be included in Sage, and the "you should install the jsmath fonts" warning should be much nicer and directly give a link to the fonts.


---

Comment by mabshoff created at 2007-12-29 17:36:26

See also #1624.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-23 02:49:10

Changing type from defect to enhancement.


---

Comment by wdj created at 2009-01-23 02:59:51

Having just started using the Notebook (for teaching), I totally agree with the complaint in this ticket.


---

Comment by timdumol created at 2009-11-15 15:52:14

Image fonts are already included in sagenb. Please close this.


---

Comment by mhansen created at 2009-11-15 15:58:04

Resolution: invalid


---

Comment by was created at 2009-11-16 19:15:52

Resolution changed from invalid to 


---

Comment by was created at 2009-11-16 19:15:52

> Image fonts are already included in sagenb. Please close this. 

You totally misunderstood the point of this ticket.


---

Comment by was created at 2009-11-16 19:15:52

Changing status from closed to new.


---

Comment by timdumol created at 2009-11-16 21:58:30

Replying to [comment:8 was]:
> > Image fonts are already included in sagenb. Please close this. 
> 
> You totally misunderstood the point of this ticket. 

Yes, now I get it. Sorry for that.


---

Comment by was created at 2009-11-17 07:29:46

> Yes, now I get it. Sorry for that. 

No problem.   I should actually write code for this though :-)


---

Comment by kcrisman created at 2012-06-12 20:36:25

Since #9774 now has positive review, apparently this should be closed?  Jason is the person who said so on #9774, but I'll leave it to him or someone else to give the final say-so.


---

Comment by kcrisman created at 2012-06-12 20:36:25

Changing status from new to needs_review.


---

Comment by jason created at 2012-06-12 21:21:18

There are several different kinds of fonts that MathJax can use, including STIX fonts (which come with browsers like Firefox, IIRC), as well as some custom fonts that are distributed in #9774.  We did NOT include in #9774 the image fonts (way too big), which is what this ticket is about.  We could have an optional spkg for mathjax image fonts.  Most browsers use the fonts that we do include with #9774, but there will still probably be some older browsers that will need image fonts.

So I'd say: don't close this ticket, but make it specific: an optional spkg for mathjax png image fonts.


---

Comment by kcrisman created at 2012-06-12 21:26:35

Changing status from needs_review to needs_work.


---

Comment by boothby created at 2020-03-29 02:02:41

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:02:41

Closing deprecated notebook tickets
