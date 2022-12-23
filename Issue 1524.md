# Issue 1524: fix various issues with #1239

Issue created by migration from https://trac.sagemath.org/ticket/1524

Original creator: was

Original creation time: 2007-12-15 08:07:58

Assignee: was


```
[12:01am] cwitty-rvw-1473: and you're confident that incidentally merging the extcode patches from 1239 doesn't hurt anything?
[12:01am] wstein-1183: yes.
[12:01am] wstein-1183: wait!
[12:02am] wstein-1183: It will completely break things
[12:02am] wstein-1183: I.e., it will break simon 2 descent
[12:02am] wstein-1183: however, I think robert is fixing the updated simon 2 descent now.
[12:02am] wstein-1183: There is nothing truly broken about that -- it just needs some polish.
[12:02am] wstein-1183: So I would recommend merging 1472 and 1239, but opening a ticket to polish 1239.
[12:03am] wstein-1183: Since 1239 works.
[12:03am] wstein-1183: it's just easy to get lies from some of the new functions 
[12:03am] jkantor: linking may be fine, but that would be about all . . .
[12:04am] cwitty-rvw-1473: Sounds good to me.  Do you want to change your review of 1239, and open the new ticket?
[12:04am] wstein-1183: yes
```



---

Comment by robertwb created at 2007-12-15 08:44:26

This was resolved in #1239 after all...


---

Comment by robertwb created at 2007-12-15 08:44:26

Changing priority from blocker to major.


---

Comment by robertwb created at 2007-12-15 08:44:26

Resolution: duplicate
