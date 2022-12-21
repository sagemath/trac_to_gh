# Issue 3776: [with patch, needs review] cookies don't work for admin users

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-08-05 18:42:13

Assignee: boothby

The Notebook is unusable for Admin users.


---

Attachment


---

Comment by TimothyClemans created at 2008-08-05 18:48:55

Note: there is a script for applying the various Notebook patches. The base is sage-3.0.6.

http://sage.math.washington.edu/home/tclemans/uw_contract_work/apply_patches.sage


---

Comment by mabshoff created at 2008-08-05 23:44:27

Replying to [comment:1 TimothyClemans]:
> Note: there is a script for applying the various Notebook patches. The base is sage-3.0.6.
> 
> http://sage.math.washington.edu/home/tclemans/uw_contract_work/apply_patches.sage

Hi Timothy,

please still provide dependencies to the "previous" ticket in the dependency chain. I am not going to just import a bunch of patches :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-12 18:46:22

One ought to verify that this patch also fixes #3817.

Cheers,

Michael


---

Comment by was created at 2008-08-12 22:17:27

Great work!


---

Comment by mabshoff created at 2008-08-13 00:03:08

Merged in Sage 3.1.alpha2


---

Comment by mabshoff created at 2008-08-13 00:03:08

Resolution: fixed
