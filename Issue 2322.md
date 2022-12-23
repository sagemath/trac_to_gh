# Issue 2322: [with patch] dsage patch for 2.10.3

Issue created by migration from https://trac.sagemath.org/ticket/2322

Original creator: yi

Original creation time: 2008-02-26 18:06:30

Assignee: was

This is the flattened patch. Please let me know if there are any problems applying it. It's based against 2.10.2.


---

Comment by yi created at 2008-02-26 18:08:51

Patch located here:
http://sage.math.washington.edu/home/yqiang/dsage-2.10.3.patch

I could not attach it because it exceeded the maximum file size =)


---

Comment by mabshoff created at 2008-02-26 18:20:37

I assume that this is the patch that was reviewed by William and rlm yesterday? In case it is please have one of them add formal positive review to this so it can be merged.


---

Comment by mabshoff created at 2008-02-26 18:21:46

Oops, wrong text box: Here we go again: It would also be nice to have a high level changelog at this ticket to indicate the changes made. I assume this also includes Timothy's patch from #2280?

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-26 18:24:26

For the record: Patch applies fine against my tree, so I can merge once I get the positive review.

Cheers,

Michael


---

Comment by yi created at 2008-02-26 18:24:33

high level changelog


---

Attachment

From the changelog it looks like we depend on SQLAlchemy, i.e. #2205. Is that correct?

Cheers,

Michael


---

Comment by yi created at 2008-02-26 22:06:35

Yes this is correct. I couldn't find a way to specify dependencies in trac, that would be a nice feature =). For the record

dsage depends on sqlalchemy which depends on setuptools.


---

Comment by yi created at 2008-03-01 23:52:12

Here are the exact steps needed to apply the patch and make everything work correctly:

1) Apply dsage-2.10.3.patch. NOTE: Do not panic at the dirstate message. It
will be fixed by step 2.
2) Remove sage/dsage/doc
3) Remove sage/dsage/dist_functions/nodoctest.py
4) Remove dsage_server.py from $SAGE_ROOT/local/bin


---

Comment by rlm created at 2008-03-01 23:55:11

Looks good to me, apply.

Comments:

1. Every single function should have some sort of descriptive text saying what it is doing, even if it doesn't have a doctest since dsage is an exception to the rule. However, to avoid bitrot, this isn't blocking the patch.

2. There are some obsolete code snippets that still use SQLite that need to be removed.


---

Comment by rlm created at 2008-03-02 00:27:29

NOTE:

In step 2), you actually need 'hg rm sage/dsage/doc', and in step 3), 'hg rm sage/dsage/dist_functions/nodoctest.py' from the branch root. Step 4), you just delete the file.

There is also a step 5): after everything else, apply:

http://sage.math.washington.edu/home/rlmill/2322-step5.patch

Also, we tested everything against 2.10.3.rc0 (with SQLAlchemy installed), and the instructions worked, and all the tests passed.

This is definitely ready to merge. -- RLM


---

Comment by mabshoff created at 2008-03-14 17:47:59

Resolution: fixed


---

Comment by mabshoff created at 2008-03-14 17:47:59

Merged in Sage 2.10.4.alpha0 - I followed all five steps and did commit after step three.
