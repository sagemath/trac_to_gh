# Issue 1644: Enable email notification of trac tickets

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2007-12-31 08:01:20

Assignee: was

CC:  michael.abshoff@googlemail.com

Keywords: trac

I think it would a real improvement to enable email notifications of trac tickets you are watching ala bugzilla style.  This makes it much easier to keep track of tickets you are interested in and prevents you from forgetting about them.  Also, it will allow us to set up a mailing list which keeps track of all changes to all trac tickets.  For more information on how to set this up, consult 

http://trac.edgewall.org/wiki/TracNotification


---

Comment by mabshoff created at 2007-12-31 08:19:58

This has been much requested feature. I just checked trac.ini and I hopefully fixed the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 08:31:19

Let's see if those changes work this time.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 08:41:05

Now that I am editing the right file hopefully this might make a difference.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 08:42:34

Ok, now we are getting somewhere. Hopefully this time the config works.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 09:25:34

Ok, now hopefully the CC to sage-trac will work.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 09:28:47

Ok, that wasn't a good idea. Let's try it again.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 09:35:05

Ok, one more test to make sure the message shows up in sage-trac as is. I set the "from" field to Williams's gmail address.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 09:39:42

ok, now everything works as expected.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 09:39:42

Resolution: fixed


---

Comment by mabshoff created at 2007-12-31 09:48:57

Hopefully the footer of the email notification is now fixed.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 09:51:23

Oops, something is escaping the '"'. Fixed.

Cheers,

Michael
