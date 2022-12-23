# Issue 9373: some overhaul in organization of database of common graph generators

Issue created by migration from https://trac.sagemath.org/ticket/9373

Original creator: mvngu

Original creation time: 2010-06-29 15:48:05

Assignee: jason, ncohen, rlm

The database of common graph generators maintains two separate lists of such generators. This entails a lot of work when updating that database as one would need to update two separate lists. Not only that, but having two lists that contain essentially the same information is information duplication. One could update a list and then forgot to update the other list. Better to have one list with links to corresponding generators.


---

Comment by mvngu created at 2010-06-29 17:03:41

Changing status from new to needs_review.


---

Attachment


---

Comment by ncohen created at 2010-07-16 02:50:31

Hello Minh !! I applied this patch on 4.5.rc1, which has a lot of new Graph methods, and found this patch needed to be rebased. I just finished, and your patch is fine for me, thank you for your work ! Here is the rebased version.. Could you give it a final check before setting this to "positive review" ? :-)

Nathann


---

Comment by mvngu created at 2010-07-16 03:09:43

With a rebased patch, some people consider it rather rude to have the rebase author's name in the username field, instead of the original author's name. Your rebased patch clearly has your username. It's like a reviewer replacing the original author's name with their own name, thus claiming credit for authoring the original patch. Perhaps you overlooked this?


---

Comment by ncohen created at 2010-07-16 03:12:44

?.....

I'm terribly sorry....

How can I change this field ? Manually ? :-/

Nathann


---

Attachment

Ok, I just edited the corresponding line and replaced it with what was written in your patch.

I really hadn't thought of it... I'm very very sorry for that :-/

Nathann


---

Comment by mvngu created at 2010-07-16 05:23:55

Thanks, Nathann. Positive review to your rebased patch.


---

Comment by mvngu created at 2010-07-16 05:23:55

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 02:48:17

Resolution: fixed
