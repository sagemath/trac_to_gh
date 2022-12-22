# Issue 960: reconsider how floating point values are printed

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-21 12:41:39

Assignee: somebody


```
 some f-p values are printed like integers, which may confuse the user
 (especially if one copies them with the mouse):
 sage: 2.0^46
 70368744177664.0
 sage: 2.0^47
 140737488355328
 I would expect '140737488355328.' or '1.40737488355328e14' in the 2nd case.
 By the way, typing 140737488355328.0 outputs itself, which is inconsistent,
 since 140737488355328.0-2.0^47 gives 0.0000000000000000.

 Compare also:
 sage: 2.0^99
 633825300114115000000000000000
 sage: 2.0^100
 1.26765060022823e30

My 2 cents,
Paul Z.
```



---

Comment by cwitty created at 2007-10-21 15:13:47

The inconsistency mentioned is because of the automagic behavior of decimal literals, where longer literals get more bits:

```
sage: (2.0^47).prec()
53
sage: (140737488355328.0).prec()
56
```


Maybe this magic behavior should be removed, or somehow modified to be less confusing?  (Although I have no idea how to make it less confusing.)

See also #962, for problems with the current implementation of the precision extension.


---

Comment by malb created at 2007-10-23 22:23:03

Changing assignee from somebody to cwitty.


---

Attachment

I've attached a patch that makes sure that all real numbers include a "." so that they don't get confused with integers.

Here is the behavior after the patch

```
sage:  2.0^47
140737488355328.
sage:  2.0^46
70368744177664.0
sage:  2.0^99
633825300114115000000000000000.
sage:  2.0^100
1.26765060022823e30
sage: 140737488355328.
140737488355328.
sage: a = 2.0^47
sage: a
140737488355328.
sage: a.prec()
53
sage: b = 140737488355328.
sage: b.prec()
53
```



---

Comment by cwitty created at 2007-10-25 06:32:40

Changing assignee from cwitty to mhansen.


---

Comment by cwitty created at 2007-10-27 02:51:54

Resolution: fixed
