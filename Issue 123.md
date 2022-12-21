# Issue 123: make "current branch notification" nicer

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-10-09 23:31:55

Assignee: somebody

When I start up SAGE in a non-main branch, it prints the branch name. It should print something nicer, like "Current branch is: ..."



---

Comment by moretti created at 2006-10-10 05:48:04

Resolution: fixed


---

Comment by moretti created at 2006-10-10 05:48:04

Replying to [ticket:123 dmharvey]:
> When I start up SAGE in a non-main branch, it prints the branch name. It should print something nicer, like "Current branch is: ..."

Fixed in hg_sage patch 1403:c01f39e80b67 and hg_scripts patch 52:7dafe792dbfc.
