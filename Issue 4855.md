# Issue 4855: make the ecm pexpect interface use files for large transfers

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-12-22 23:02:48

Assignee: was

This is a followup to $4814 to properly fix the interface. 

I suspect that the interface also leaks file handles which causes it to stop working after a while. This issue can be split off if the it cannot be fixed in a timely manner or if there is a patch for the other issue.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-23 02:43:18

Changing type from defect to enhancement.
