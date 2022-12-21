# Issue 7183: HP-UX issue: Evert package "date: bad format character - s

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-10 10:32:35

Assignee: tbd

CC:  david.kirkby@onetel.ne

I assume this is in one of the files that gets called for every single .spkg. It appears 'date -s' is not portable




---

Comment by jdemeyer created at 2015-09-08 12:45:40

Changing component from build to porting: AIX or HP-UX.


---

Comment by jdemeyer created at 2015-09-08 14:42:47

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-09-08 14:42:47

I don't think that `date -s` is still used somewhere.


---

Comment by jdemeyer created at 2015-09-08 14:42:55

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-09-12 14:05:56

Resolution: fixed


---

Comment by drkirkby created at 2015-09-12 15:18:00

Where's the fix that received positive receive, and so allowed the ticket to be closed? 

It seems a lot of tickets are now getting positive review and closed, where there is no actual fix.


---

Comment by jdemeyer created at 2015-09-12 22:33:05

Replying to [comment:6 drkirkby]:
> Where's the fix that received positive receive, and so allowed the ticket to be closed? 
> 
> It seems a lot of tickets are now getting positive review and closed, where there is no actual fix. 

1. This ticket has seen no activity at all in years.
2. I haven't seen any report of this problem in years (usually, when there is really a problem, it pops up on `sage-devel` now and then).
3. I grepped the Sage sources and couldn't find anything like `date -s`.

If you really think there is still a problem, feel free to re-open the ticket but with more concrete info than just "I assume this is in one of the files that gets called for every single .spkg".
