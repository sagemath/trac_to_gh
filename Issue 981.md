# Issue 981: bug in the method conjugacy_classes_subgroups

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2007-10-24 14:16:00

Assignee: wdj

CC:  sage-combinat

there is a bug in the module permgroup.py, at line 1226,
the method conjugacy_classes_subgroups calls PermutationGroupElement;
I think it should be PermutationGroup.
reported by Biel


---

Comment by wdj created at 2007-10-24 16:38:21

Patch is here:
http://sage.math.washington.edu/home/wdj/patches/permgp-patch.hg
Passes sage -t. Created agains sage 2.8.3 on a suse amd64 machine,
so may be a bit old....


---

Comment by malb created at 2007-10-24 19:14:33

applied to 2.8.9.alpha1


---

Comment by malb created at 2007-10-24 19:14:37

Resolution: fixed
