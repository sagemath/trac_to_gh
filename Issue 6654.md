# Issue 6654: [with patch, needs review] new features in group algebra category

Issue created by migration from Trac.

Original creator: vferay

Original creation time: 2009-07-29 13:16:54

Assignee: mhansen

Keywords: group algebra, center

I added features in the category of group algebras (especially linked to the center).

Moreover, the symmetric group algebra now is a parent of this category.


---

Comment by wdj created at 2009-08-15 23:25:37

This patch failed to pply for me:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: gpalg
sage: hg_sage.apply("/Users/davidjoyner/sagefiles/grotrac_6647_permutationgroup_improvement.patch")
/Users/davidjoyner/sagefiles/group_algebras_feature_central_vf.patch
/Users/davidjoyner/sagefiles/groups
sage: hg_sage.apply("/Users/davidjoyner/sagefiles/group_algebras_feature_central_vf.patch")cd "/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/devel/sage" && hg status
/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/devel/sage" && hg status
cd "/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/devel/sage" && hg import   "/Users/davidjoyner/sagefiles/group_algebras_feature_central_vf.patch"
applying /Users/davidjoyner/sagefiles/group_algebras_feature_central_vf.patch
unable to find 'sage/categories/group_algebras.py' for patching
3 out of 3 hunks FAILED -- saving rejects to file sage/categories/group_algebras.py.rej
unable to find 'sage/categories/monoid_algebras.py' for patching
1 out of 1 hunks FAILED -- saving rejects to file sage/categories/monoid_algebras.py.rej
patching file sage/combinat/symmetric_group_algebra.py
Hunk #2 FAILED at 121
Hunk #3 FAILED at 131
Hunk #5 FAILED at 430
3 out of 5 hunks FAILED -- saving rejects to file sage/combinat/symmetric_group_algebra.py.rej
abort: patch failed to apply
```

| Sage Version 4.1.1.rc2, Release Date: 2009-08-06                   |
| Type notebook() for the GUI, and license() for information.        |
DO you know what the problem is?


---

Comment by vferay created at 2009-09-10 10:19:36

This patch must be applied after Nicolas Thiéry's patches on categories (I do not know which one exactly). So please do not use import to test it but apply it with qpush.


---

Comment by vferay created at 2009-10-13 14:17:39

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2012-08-29 10:05:20

Apply [attachment:group_algebras_feature_central_vf.patch.new_version]


---

Comment by chapoton created at 2012-09-08 07:32:34

apply only group_algebras_feature_central_vf.v2.patch


---

Comment by chapoton created at 2012-09-08 07:32:34

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2012-09-08 09:09:34

apply only group_algebras_feature_central_vf.v2.patch


---

Comment by chapoton created at 2012-09-08 12:00:12

clean up of doc


---

Attachment

apply only group_algebras_feature_central_vf.v2.patch


---

Comment by chapoton created at 2012-09-09 18:20:30

Given that the bot is happy, and that I have done my best to check the doc, I give a positive review.


---

Comment by chapoton created at 2012-09-09 18:20:30

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-09-11 07:57:52

Resolution: fixed
