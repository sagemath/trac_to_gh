# Issue 7897: Macaulay2 interface update/improvement for version 1.3.1

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2010-01-11 20:53:30

Assignee: was

Keywords: Macaulay2, interface

These patches change the prompt detection/stripping and update doctests to cause no errors with Macaulay2 1.3.1.

Improvements/fixes achieved:
 - examples in Macaulay2 documentation (which include input prompts) do not break the interaction with Sage;
 - empty/whitespace/comment lines can be executed;
 - multiline commands can be executed;
 - stripping output prompts will not cut error messages if they occur (e.g. the first call "help Thing" currently shows some errors in Macaulay2).

This is done by:
 - changing input and input continuation prompts;
 - starting with a big line number to make all output labels of the same width;
 - making sure that only output labels and spaces are stripped from the output.

Side effects / Remaining issues:
 - "restart" command of Macaulay2 is handled separately when it is called like "macaulay2.restart()" since we need to repeat prompt adjustments;
 - this command cannot be used in the string code passed to Macaulay2, since it will cause a lock. Since this should not cause loss of data (if the user intentionally tried to restart Macaulay2), I think this is OK. Correct checking of all the code for "restart" in it would involve also checking if it is inside string constants. 

These patches make tickets #7882 and #7888 unnecessary.


---

Comment by novoselt created at 2010-01-11 20:54:23

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-01-12 02:45:40

I changed my mind about importance of "restart" command in the middle of the code after seeing a talk today. So the patch is rewritten to allow it everywhere. All doctests still pass with both patches applied.


---

Attachment


---

Comment by novoselt created at 2010-02-01 04:37:25

Renamed patches and commit messages to follow conventions. Apply both patches starting with "trac_7897"


---

Comment by mhansen created at 2010-07-09 01:12:44

Looks good to me.


---

Comment by mhansen created at 2010-07-09 01:12:44

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-07-09 01:13:16

Also apply #5467 and #7915.


---

Comment by mpatel created at 2010-07-21 03:30:48

Resolution: fixed
