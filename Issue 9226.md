# Issue 9226: README.txt says " Sage builds with GCC >= 3.x" but it does NOT

Issue created by migration from https://trac.sagemath.org/ticket/9226

Original creator: drkirkby

Original creation time: 2010-06-12 11:51:57

Assignee: mvngu

The title pretty much says it all. There is no way Sage will build with any gcc <= 4.0.1. The 'prereq' script will stop any attempt and even if you bypass that stop (by setting the appropiate environment variable), Sage will not build 

I've attached a revised README.txt, which addresses this and

 * The fact gcc, g++ and gfortran need to be the same versions. 
 * Spelling change of Sparc -> SPARC. 
 * Better information about what does and does not work on Solaris.


---

Attachment

Suggested revised README.txt


---

Attachment

Differences from README.txt in Sage 4.4.3


---

Comment by robertwb created at 2010-06-12 16:29:25

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-06-12 16:29:41

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 09:03:01

Replaced SAGE_ROOT/README.txt with the README.txt here in 4.5.2.alpha1.


---

Comment by ddrake created at 2010-07-22 09:03:01

Resolution: fixed


---

Comment by mpatel created at 2010-08-05 02:22:57

Resolution changed from fixed to 


---

Comment by mpatel created at 2010-08-05 02:22:57

Changing status from closed to new.


---

Comment by mpatel created at 2010-08-05 02:22:57

Changing priority from major to blocker.


---

Comment by drkirkby created at 2010-08-05 03:01:17

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-08-05 03:02:27

I just tried to correct a couple of typos in the description and managed to remove the positive review. I've restored it now.


---

Comment by drkirkby created at 2010-08-05 03:02:27

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-05 10:59:07

Resolution: fixed


---

Comment by kcrisman created at 2010-08-05 15:11:56

It's unfortunate that this is so, because there is still a problem, namely that 

```
PPC              Apple Mac OS X 10.4.x, 10.5.x, 10.6.x
```

is by definition wrong, since 10.6.x will only work on Intel chips.  Also see other README.txt updates lurking on Trac, such as #7484, which also fixes #8106; #6055 perhaps should be closed, while #5505 I'm less clear on; #5339 seems closable as dup; #3131 perhaps is not relevant, but while I'm listing all of them...


---

Comment by ddrake created at 2010-08-05 17:17:43

Replying to [comment:10 kcrisman]:
> It's unfortunate that this is so, because there is still a problem, namely that 
> {{{
> PPC              Apple Mac OS X 10.4.x, 10.5.x, 10.6.x
> }}}
> is by definition wrong, since 10.6.x will only work on Intel chips.  Also see other README.txt updates lurking on Trac, such as #7484, which also fixes #8106; #6055 perhaps should be closed, while #5505 I'm less clear on; #5339 seems closable as dup; #3131 perhaps is not relevant, but while I'm listing all of them... 

I would recommend that anyone currently working on fixing the SAGE_ROOT README.txt, the spkg/standard/deps file, or any of the other crucial files that are not under revision control...please take a look at #9433, which will put these files into a Mercurial repository, and make dealing with them reasonable, instead of the current mess. #9433 should actually be pretty easy to review.


---

Comment by kcrisman created at 2010-08-05 17:24:42

> I would recommend that anyone currently working on fixing the SAGE_ROOT README.txt, the spkg/standard/deps file, or any of the other crucial files that are not under revision control...please take a look at #9433, which will put these files into a Mercurial repository, and make dealing with them reasonable, instead of the current mess. #9433 should actually be pretty easy to review.

Yes, I just didn't mention this one since it was a meta-ticket.  I don't feel technically capable of it (not knowing ins and outs of hg), otherwise I would have done so weeks ago :(


---

Comment by drkirkby created at 2010-08-06 17:41:59

Replying to [comment:12 kcrisman]:
> 
> > I would recommend that anyone currently working on fixing the SAGE_ROOT README.txt, the spkg/standard/deps file, or any of the other crucial files that are not under revision control...please take a look at #9433, which will put these files into a Mercurial repository, and make dealing with them reasonable, instead of the current mess. #9433 should actually be pretty easy to review.
> 
> Yes, I just didn't mention this one since it was a meta-ticket.  I don't feel technically capable of it (not knowing ins and outs of hg), otherwise I would have done so weeks ago :(

Same here. I don't feel able to review it. If Dan believes it is an easy review, perhaps he could consider doing it if he has time, as at least two of us don't feel able to do it, and nobody else has stepped up. Yet I am one who agrees this would be a useful addition to Sage. The current system for such files is a bit silly. 

Dave
