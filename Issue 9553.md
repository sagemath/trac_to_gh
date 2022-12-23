# Issue 9553: sage -ba (build all) waits for input, making it harder to use in scripts

Issue created by migration from https://trac.sagemath.org/ticket/9553

Original creator: jdemeyer

Original creation time: 2010-07-20 08:44:27

Assignee: was

When doing "sage -ba" from the shell, one gets a prompt:

```
 *** WARNING ***
 You are about to rebuild the entire Sage library.
 This will take a significant amount of time.
 Do you want to proceed? [y/n]
```


Since this waits forever for user input, it is harder to use in non-interactive scripts.  I propose to change the prompt and add a timer such that "sage -ba" continues anyway when nothing has been typed for 30 seconds or so.


---

Comment by jdemeyer created at 2010-07-23 11:09:04

While looking at this bug, I discovered the -ba-force option, which is exactly what I was looking for.  So I propose a small patch to change the prompt to:

```
 *** WARNING ***
 You are about to rebuild the entire Sage library.
 This will take a significant amount of time.
 (use -ba-force instead of -ba to skip this prompt.)
 Do you want to proceed? [y/n]
```



---

Comment by jdemeyer created at 2010-07-23 11:12:07

Changing status from new to needs_review.


---

Attachment

Apply this to the local/bin branch


---

Comment by was created at 2010-07-23 20:17:11

Excellent idea -- I hate interactive prompts, especially ones that it isn't obvious how to get around. That said, I think this line

```
echo " (use -ba-force instead of -ba to skip this prompt.)" 
```

should be

```
echo " (Use -ba-force instead of -ba to skip this prompt.)" 
```



---

Comment by jdemeyer created at 2010-07-24 00:33:13

Replying to [comment:3 was]:
> Excellent idea -- I hate interactive prompts, especially ones that it isn't obvious how to get around. That said, I think this line

As far as I'm concerned, we could even complete remove the prompt and make -ba act like -ba-force.  I never quite understood the point of that prompt anyway.


---

Attachment

"use" --> "Use".  scripts repository.  Apply only this patch.


---

Comment by mpatel created at 2010-08-19 21:52:28

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-19 21:52:28

I've attached an updated patch with William's suggested change.

## To the release manager
Apply only [attachment:trac_9553-use_the_baforce_message.patch], to the scripts repository.


---

Comment by mpatel created at 2010-08-31 03:20:35

Resolution: fixed


---

Comment by leif created at 2010-08-31 05:11:05

What a ticket! I'm not sure if two reviewers are enough to merge this... :D

Since despite its severity it now is, perhaps one should change the title and the description to reflect what the patch really does. ;-)


---

Comment by leif created at 2010-08-31 07:04:01

Thanks!
