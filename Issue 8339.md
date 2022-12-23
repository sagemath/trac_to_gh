# Issue 8339: Message of the day for notebook server

Issue created by migration from https://trac.sagemath.org/ticket/8339

Original creator: cremona

Original creation time: 2010-02-23 22:46:08

Assignee: was

CC:  embray jdemeyer fbissey

Keywords: notebook

From sage-devel 2010-02-22:

Here's a suggestion for the notebook:   allow the admin user to set a
"message of the day" which would be seen either on the login page
itself, or as a pop-up or similar after logging in.

Example:  after the server has just been upgraded to a new version
(like 4.3.3 recently) users could be alerted of this change (and yes,
I know that the version number is displayed right above the login box,
but how many users will actually notice that it has changed)?

As an admin I would also find this useful as a way of communicating
with the user base on my server.

The existence and text of the MOTD should be settable from the usual
admin notebook settings screen.





---

Comment by drkirkby created at 2010-02-23 23:31:17

A great idea. 

If the contents of the message written by the admininstrator could be stored in a plain text file, then it would offer the possibility of generating that file dynamically, to do things like 

 * Announce "Merry Christmas" on 25th December 
 * Show the load average
 * Show the uptime
 * etc etc. 

Of the the message was stored as a bit of simple HTML, then again it could be modified outside Sage if wanted. 

Dave


---

Comment by chapoton created at 2019-06-15 07:27:08

Changing status from new to needs_review.


---

Comment by chapoton created at 2019-06-15 07:27:08

legacy sagenb is deprecated, so this can be closed


---

Comment by fbissey created at 2019-06-15 07:43:16

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2019-06-15 12:40:53

Resolution: invalid


---

Comment by chapoton created at 2019-06-15 12:40:53

close 3 old invalid tickets
