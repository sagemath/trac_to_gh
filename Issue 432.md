# Issue 432: finish implementing deleting the trash (emptying it) in the sage notebook.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-16 09:43:33

Assignee: was

I just never got around to implementing it.


---

Comment by was created at 2007-08-16 09:43:41

Changing component from algebraic geometry to notebook.


---

Comment by was created at 2007-08-16 09:43:41

Changing assignee from was to boothby.


---

Comment by was created at 2007-12-13 18:46:56

Just a remark from a user:

```

> But, when I archived all trash content, it hangs... Closed Firefox,
> VMware Player, reboot - everything was to-o-o-oo slow and buggy,
> almost any loading of saved file caused an error.
> 
> I ended up deleting all sage files and unpacking them again from
> distribution ZIP. Now everything is fast again.
```



---

Attachment

I finally implemented this.  And it's with 100% doctest coverage of new functions, which is a new thing for the notebook (to have any docs at all).


---

Comment by boothby created at 2008-03-16 18:11:31

Works for me.


---

Comment by mabshoff created at 2008-03-17 04:01:40

Merged in Sage 2.10.4.final


---

Comment by mabshoff created at 2008-03-17 04:01:40

Resolution: fixed


---

Comment by bill.p created at 2008-03-18 11:46:42

Tried the patch on 2.10.3 and still had some problems with it - worked sometimes but not others.
Installed 2.10.4.final which includes the patch and it now works fine. Could this be some
interaction with other patches?
Anyway - seems fine under 2.10.4 now.
