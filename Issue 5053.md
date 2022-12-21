# Issue 5053: If the hostname of the computer has a "-" in it, then no tempfiles will ever be deleted from $DOT_SAGE/temp!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-22 11:23:30

Assignee: cwitty

This is because host-name and host_name get confused.


---

Attachment

For being consistent, replace '-' with '_'. This yields a proper cleaning of temp-files


---

Comment by SimonKing created at 2009-01-24 21:08:43

Apparently, the pid of any sub process is written in a temporary file, in a folder whose name is derived from the hostname.

And apparently, when writing these files, any '-' in the hostname will be replaced by '_'. But this replacement is ignored in the `sage-cleaner` script.

So, the obvious solution is to replace '-' by '_' in the `sage-cleaner`. This is what my patch does.

I tested the following: 
 * change the hostname into 'test-test_test'
 * before applying the patch, folders 'test_test_test' (sic!) are created in SAGE_TMP. But the `sage-cleaner` does not clean them
 * after applying the patch, the same folders are created, but this time they are removed after leaving sage.
 * don't forget to change back to your original hostname ;-)


---

Comment by SimonKing created at 2009-01-25 07:58:56

To be applied after the first patch: Allow hostnames containing '/' and '\'


---

Attachment

To be applied after the first patch. Allows hostnames that contain '/' or '\'


---

Comment by SimonKing created at 2009-01-25 08:12:17

I had a short discussion with William: 

A related issue occurs when the hostname contains a slash '/'. Namely, the file name obtained from the hostname would be interpreted as a _path_ name, yielding an error! Again, a possible solution is to replace '/' by '_', both in `sage/misc/misc.py` and in the `sage-cleaner`. Since the reason is more or less the same, William suggested to discuss this on the same ticket.

And similarly, there may be problems when the hostname contains a backslash '\'. So, I did the according replacement.

There is only one situation in which this idea might be a problem:
 * There are two hosts whose names coincide after the replacements
 * These hosts share DOT_SAGE
 * By coincidence, two Sage processes running on these two hosts have the same `pid`.

This situation would yield a collision, but it seems to be *extremely unlikely*.

*Conclusion*
 There are hostnames containing a slash (I think I have seen one in nature...). So, in the current setting, a bug would occur. My patches (all three together) fix this bug. 
 The price to pay is another bug that would occur in an extremely unlikely setting.

I tested my patches with the hostnames `test-test_test`, `test/test` and `test\test`.


---

Comment by mabshoff created at 2009-01-29 03:46:23

cwitty pointed out in IRC that `/` and `\` probably aren't even legal for hostnames, but what the heck: positive review.

I am curious how the problem about those two characters come up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 03:50:27

Merged all three patches in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 03:50:27

Resolution: fixed
