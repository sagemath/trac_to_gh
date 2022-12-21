# Issue 2341: vector subs over symbolic does not work

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-28 04:51:09

Assignee: was

CC:  jason


```
Ricardo Massaro to sage-devel
	
show details 8:28 PM (18 minutes ago)
	
	
Reply
	
	

Hello all,

First of all, I'd like to thank you for Sage, it's really helping me a
lot.

I found a strange behavior that i *think* it's a bug, but I'm not
sure, since I'm a completely newbie to Sage and Python:

sage: a = var('a')
sage: m = matrix(SR, 2, [a,a,a,a])
sage: v = vector(SR, 2, [a,a])

Then,

sage: m.subs(a=1)
[1 1]
[1 1]

but

sage: v.subs(a=1)
(a, a)

I *think* the problem is in the Element.subs() method in devel/sage/
sage/structure/element.pyx. It seems to assume that the generators are
symbols, which is not true in the example vector.

Am I missing something, or is it really a bug?

Here's a dirty fix that apparently fixes this problem, but will likely
beak something else:

   def subs(self, in_dict=None, **kwds):
       v = [a.subs(in_dict, **kwds) for a in self.list()]
       return self.parent()(v)

Thanks,
Ricardo
```



---

Comment by gfurnish created at 2008-04-10 04:38:36

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-04-10 04:38:36

Changing assignee from was to gfurnish.


---

Comment by gfurnish created at 2008-05-21 16:46:46

Fixed in symbolics rewrite.


---

Comment by mhansen created at 2009-06-04 21:24:12

Changing status from assigned to new.


---

Comment by mhansen created at 2009-06-04 21:24:12

Changing assignee from gfurnish to mhansen.


---

Comment by mhansen created at 2009-06-04 21:24:18

Changing status from new to assigned.


---

Comment by kcrisman created at 2009-09-29 17:26:48

Based on 4.1.2.alpha4


---

Attachment

This patch should fix the issue - long overdue!  The fix is to do exactly as the OP suggests, but only in the free module elements - which is precisely what is already done for matrices as well.


---

Comment by jason created at 2009-09-29 20:30:51

Nice!  Thanks for taking care of this.

doctests pass on the free_module_element.pyx file.


---

Comment by mhansen created at 2009-10-15 05:23:07

Resolution: fixed
