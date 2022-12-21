# Issue 6666: [with patch] implement analytic modular symbols algorithm and cusp transformation matrix

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-08-02 18:52:08

Assignee: was

CC:  pbruin cremona




---

Attachment


---

Comment by davidloeffler created at 2013-07-25 17:23:57

Changing component from number theory to modular forms.


---

Comment by chapoton created at 2013-10-17 19:07:38

Here is a rebased patch.

apply trac_6666-rebased-5.12.patch


---

Comment by chapoton created at 2013-10-17 19:08:45

Changing status from needs_work to needs_info.


---

Comment by chapoton created at 2013-10-17 19:08:45

Changing keywords from "" to "period, modular symbol".


---

Comment by was created at 2013-10-17 19:16:33

Frédéric Chapoton -- whoever you are -- I'm extremely happy seeing all the work you're doing on modular forms related functionality in Sage!!!!!!  

+1000

 -- William Stein


---

Comment by chapoton created at 2013-10-17 19:36:59

Thanks William. I am in algebra and combinatorics, not a number theorist, but I am trying to help nevertheless.

for the patchbot: 

apply trac_6666-rebased-5.12.patch


---

Comment by was created at 2013-10-17 19:41:13

Replying to [comment:6 chapoton]:
> Thanks William. I am in algebra and combinatorics, not a number theorist, but I am trying to help nevertheless.
> 

Thanks.  I'm in number theory, not algebra/combinatorics, but I hope Sage has been helpful to people in algebra/combinatorics :-)


---

Comment by chapoton created at 2013-10-20 11:38:52

Changing status from needs_info to needs_review.


---

Comment by chapoton created at 2013-10-20 11:38:52

ok, the bot has turned green. Needs review


---

Comment by chapoton created at 2013-10-25 18:14:44

new patch, rebased on 5.13.beta1

apply trac_6666-rebased-5.12.patch


---

Comment by chapoton created at 2013-10-26 09:33:00

So there is numerical noise. Could somebody remind me what is the proper way to handle that ?

Use `...` or use `# rel tol` or use `# abs tol` ?


---

Comment by chapoton created at 2013-10-27 16:53:04

new patch, with numerical tolerance

apply trac_6666-rebased-5.12.patch


---

Comment by chapoton created at 2013-10-27 16:57:30

apply trac_6666-rebased-5.12.patch


---

Attachment


---

Comment by chapoton created at 2013-11-25 17:59:34

new patch, with lazy import

apply trac_6666-rebased-5.12.patch


---

Comment by chapoton created at 2013-12-02 21:16:38

New commits:


---

Comment by git created at 2014-01-04 18:52:34

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-12-20 03:32:48

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2014-12-22 21:26:00

The most important part of this ticket (periods of newforms) was implemented in a more general context (and with better precision handling) in #11215.  The new commit reorganises the code, moves it to a more logical place (in my opinion) and uses the `period()` method of #11215.


---

Comment by chapoton created at 2015-01-24 17:14:21

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2015-01-24 17:14:21

Looks good to me.

I allowed myself a few minor changes.
----
New commits:


---

Comment by pbruin created at 2015-01-24 22:57:45

Replying to [comment:22 chapoton]:
> Looks good to me.
Thanks for the review!
> I allowed myself a few minor changes.
I'm not disputing your changes to the whitespace here, but note that PEP 8 does not say that there should be spaces around _all_ operators, only the relational ones.  From https://www.python.org/dev/peps/pep-0008/:

>> If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator.
>> Yes:
>> {{{
>> i = i + 1
>> submitted += 1
>> x = x*2 - 1
>> hypot2 = x*x + y*y
>> c = (a+b) * (a-b)
>> }}}
>> No:
>> {{{
>> i=i+1
>> submitted +=1
>> x = x * 2 - 1
>> hypot2 = x * x + y * y
>> c = (a + b) * (a - b)
>> }}}
Actually, in the case of `c = ...`, I would personally prefer the "no" option or even `(a + b)*(a - b)`, which is closer to standard mathematical typesetting, but in any case this is a matter of taste.


---

Comment by vbraun created at 2015-01-25 16:25:50

Resolution: fixed
