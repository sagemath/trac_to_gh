# Issue 3160: change is_planar for graphs to return bool

Issue created by migration from https://trac.sagemath.org/ticket/3160

Original creator: was

Original creation time: 2008-05-11 19:00:51

Assignee: rlm


```
+1 on making this change. It's very unusual for an is_ function to
return anything but a bool :)
- Hide quoted text -

On Sun, May 11, 2008 at 11:34 AM, Robert Miller <rlmillster@gmail.com> wrote:
>
>>  On the other hand, that Jerin was confused maybe strongly suggests
>>  you might want to change the is_planar function to return True or
>>  False, and have another function or a flag to get the nonplanar
>>  subgroup.  In most of Sage foo.is_*() returns True or False, so maybe
>>  is_planar() is confusing, especially from a readability point of view.
>
> I think I agree. The default behavior should be True/False, and an
> option to return the present tuple should be available.
>
>
```



---

Attachment


---

Comment by rlm created at 2008-05-12 16:50:10

-1 point for not testing before submitting!


---

Attachment

Merged both patches in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-12 18:46:30

Resolution: fixed
