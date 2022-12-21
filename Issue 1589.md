# Issue 1589: jmol -- using via https is a pain in the butt

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-23 06:55:33

Assignee: was

If you try to use jmol over https, every single time
you display an image it displays the following dialog box:

"Client Authentication: The client is trying to ... Please select
the certificate:"

Then there is a list with no certificates, and a button "Details"
that when clicked does nothing.    

This is really annoying.



---

Comment by robertwb created at 2007-12-23 08:24:10

This is a known issue with java and https. See http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=6186280

However, to use http we might need to sign the applet, which would be a (different) dialog. 

There may be something we can change on the twisted side of things so that it knows not to ask for a client certificate. This I think is our best bet, but I am very unfamiliar with the notebook authentication code (but would be willing to learn).


---

Comment by robertwb created at 2008-01-02 20:11:42

I have confirmed that this is a twisted authentication issue, one can serve applets over https (and have said applets request resources) without this annoying dialog. 

I'm looking into our authentication code now.


---

Attachment

GNUTLS provides two options for client-side certificates, CERT_REQUEST and CERT_REQUIRE, both of which request a certificate. I found the place in the source that uses these constants, and if one sets the value to 0 (unexposed via in the api) a certificate won't be requested. 

The least intrusive change was to spoof CERT_REQUEST=0 in the notebook run script. This finally gets rid of that dialog that's been haunting me for almost a year now (was there with the other java 3d viewers as well).


---

Comment by robertwb created at 2008-01-04 06:05:07

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2008-01-04 06:05:07

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-05 12:10:36

Resolution: fixed


---

Comment by mabshoff created at 2008-01-05 12:10:36

Merged in 2.9.2.
