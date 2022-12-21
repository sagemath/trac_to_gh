# Issue 9319: extend and improve "sage -merge"

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-06-23 21:22:54

Assignee: GeorgSWeber

CC:  leif

Two issues and/or suggestions for "sage -merge":

 - if a ticket (like #9278) _removes_ a file from the Sage library, then 'sage -merge' runs 'sage -tp 2 -long' with no argument, and this doesn't succeed.  So we should catch this case and deal with it.

 - 'sage -merge' should detect whether each patch file has a properly formatted commit message, and either automatically prepend "#NUM" to it, or allow the release manager to edit it, before applying it.



---

Comment by ddrake created at 2010-07-22 06:03:20

script that checks a patch's metadata; for demonstration purposes


---

Attachment

attachment:check_patch_metadata.py is a script that, given a patch file and a ticket number, will check to see that the commit message contains the ticket number in the first line, and if it doesn't, it will prepend "ticket xxxx:" to the commit message and save the resulting patch in a a file with ".fixed" appended. It should be easy to integrate this into sage-apply-ticket.

It bails if it cannot find a commit message or username in the patch. It issues a warning if it can't find a date, node ID or parent but continues. As a guess, I think "sage -merge" should fail if there's no commit message or username, and in the other cases, issue the warning and ask the user if they want to continue.


---

Comment by jdemeyer created at 2013-05-19 13:17:18

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-05-19 13:17:18

`sage -merge` is gone (#14417).


---

Comment by jdemeyer created at 2013-05-19 13:17:28

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-21 07:22:55

Resolution: invalid
