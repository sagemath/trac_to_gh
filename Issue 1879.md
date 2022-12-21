# Issue 1879: notebook -- registering redirects to annoying url

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-21 18:36:29

Assignee: boothby


```
On Jan 21, 2008 7:24 AM, Martin Albrecht <> wrote:
>
> > I also made it so the notebook doesn't require a funny port, so it should
> > work fine if you're behind some sort of firewall  that doesn't allow
> > connections to ports.   Finally, I  reduced the number of security
> > warnings.
>
> I am behind such a funny firewall and it doesn't work for me. I don't have an
> account on this particular NB server yet and registering times out because it
> redirects to http:sage.math.washington.edu:8101/register. This is where the
> firewall won't let me connect.

That's annoying.  I wonder why that happens.  In any case, if you register you
only get sent to 8101 *after* you register -- your registration should still go
through fine.  You can then login by manually going to sagenb.org (or going
back with the browser back button).

```



---

Attachment


---

Comment by was created at 2008-03-17 04:30:45

Excellent!

Works perfectly for me.


---

Comment by mabshoff created at 2008-03-17 04:35:14

Merged in Sage 2.10.4.final


---

Comment by mabshoff created at 2008-03-17 04:35:14

Resolution: fixed
