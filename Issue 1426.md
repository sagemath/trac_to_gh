# Issue 1426: new trac view: tickets ***reported by*** given user

Issue created by migration from https://trac.sagemath.org/ticket/1426

Original creator: zimmerma

Original creation time: 2007-12-08 10:44:15

Assignee: was

I don't know if this is possible, but I wish the possibility to view all tickets 
reported by a user logged in trac (either only active tickets, or active tickets first).
This would enable me to see progress made on those tickets.

Currently it is possible to view ***my tickets***, i.e., tickets ***assigned to me***,
which is quite different :-)

PS: I'm not sure the component "website/wiki" is the right one. Maybe one needs a new component
"trac"?


---

Comment by mabshoff created at 2007-12-09 02:07:43

Hey Paul,

how about `http://sagetrac.org/sage_trac/report/7`? Or do you wish to query for a user that isn't you also?

Cheers,

Michael


---

Comment by zimmerma created at 2007-12-09 21:21:09

Hi Michael,

http://sagetrac.org/sage_trac/report/7 does not do what I want. If I click on it, I get no ticket,
which is normal since no ticket was ***assigned*** to me.

What I'd like to have is a list of ticket I've ***reported***.

Paul


---

Comment by AlexGhitza created at 2007-12-10 14:26:37

Hi Paul,

Just to try this out, I went to http://sagetrac.org/sage_trac/report/7 and noticed the link "Custom Query" toward the top right, underneath the main trac bar.

By default, it has only one field for searching, namely "Owner is".  But under that, to the right, there's an option "Add filter", and one of the possibilities is "Reporter".  You need to get rid of the "Owner is" field by clicking the minus sign at the right, and you're set to search for tickets reported by a certain person.

So good news: it can be done in trac.  Bad news: it's a pain to go through all that every time.  Maybe it's possible to have a short cut for this?

Alex


---

Comment by AlexGhitza created at 2007-12-10 14:33:25

Sorry, me again.

It should be almost trivial for someone who has privileges to do this, to copy the "My Tickets" report and replace "Owned by" by "Reported by".  We could then have something like "Tickets I own" and "Tickets I reported" as two reports easily accessible.

As far as I can tell, though, one needs administrator privileges in order to mess around with the reports.

Alex


---

Comment by dmharvey created at 2007-12-21 01:05:24

hmm ok I think I've done this now, it's report number 9, I'll see if people like it


---

Comment by rlm created at 2007-12-21 02:28:53

Resolution: fixed
