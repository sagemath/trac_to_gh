# Issue 2746: [with patch; needs review] Support for writing test-related files in SAGE_TESTDIR

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-04-01 01:23:11

Assignee: failure

I've attached my changeset that causes all writes that occur when running doctests to be written inside SAGE_TESTDIR.

One thing I'm uncertain about is what should happen with the line
"cat $SAGE_TESTLOG >> $SAGE_ROOT/test.log".

At the moment, I leave it in, and there's an error at the end of the block of tests.  I would recommend removing it and just making $SAGE_ROOT/test.log be a symlink to $SAGE_ROOT/tmp/test.log in the default SAGE install.


---

Attachment


---

Comment by mabshoff created at 2008-04-03 09:17:52

There is a small reject due to #2621 having been merged, but after resolving the merge conflict both patches apply cleanly. I am doing some more extensive testing before giving this a positive review, but so far things look good.

Cheers,

Michael


---

Attachment

check if SAGE_TEST is not empty


---

Comment by mabshoff created at 2008-04-03 10:35:32

If SAGE_TEST is empty things go wrong. I have attached a patch that fixes the issue. Positive review since this is useful "as-is". A couple suggestions for a follow up patch:
 
 * make sure that SAGE_TEST is writable
 * delete the .doctest file once the doctest finishes
 * document SAGE_TEST :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-03 10:35:56

Resolution: fixed


---

Comment by mabshoff created at 2008-04-03 10:35:56

Merged all three patches in Sage 3.0.alpah1
