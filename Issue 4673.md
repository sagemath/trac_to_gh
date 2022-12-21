# Issue 4673: Introduce generic pools just like for the Integer class

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-12-02 12:59:06

Assignee: robertwb

CC:  robertwb

This is a substitution for #2930 since the idea is good, but the implementation was not the way to go. 

The general idea is that we should have pools for certain objects like CDF to make the creation quicker. Code like that exists for Integers, so it would be nice to generalize them.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-23 02:47:44

Changing type from defect to enhancement.
