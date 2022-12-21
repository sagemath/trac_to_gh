# Issue 3649: Add option to disable the Notebook registration email

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-07-12 18:28:44

Assignee: boothby

From https://groups.google.com/group/sage-support/browse_thread/thread/1fc876f97a69eb5e

```
When you sign up for a Sage Notebook account, Sage sends an e-mail to
the address you provide giving you a link to complete the
registration.

First of all, the "Sign up for a Sage Notebook account" says that the
e-mail is needed if you forget your password, but makes no mention of
the fact that the e-mail will be needed immediately to complete the
registration process. If Sage asks for a user's e-mail address, it
should correctly indicate what that e-mail address is for. Otherwise,
e-mail from the Sage notebook is technically spam.

Secondly, I am running the Sage notebook on a machine which my
college's support staff will not allow to run a mail server (all of
the mail on campus needs to be handled by their own antiquated
servers, which has less storage space than my iPod to store e-mail for
2000 users). Is there any way to turn off the sending of e-mail from
the Sage Notebook?

-- Greg

-- 
Gregory D. Landweber
Assistant Professor of Mathematics
Bard College 
```

Robert Bradshaw replied:

```
Thanks for the clarification. This can easily be resolved by  
commenting out line ~1716 of sage/server/notebook/twist.py. This  
should probably be made optional and configurable somewhere.

- Robert 
```


Cheers,

Michael


---

Comment by TimothyClemans created at 2008-07-14 00:34:51

Changing assignee from boothby to TimothyClemans.


---

Comment by TimothyClemans created at 2008-07-14 00:34:51

Changing status from new to assigned.


---

Comment by TimothyClemans created at 2008-07-14 00:34:51

Lines to copy out are   


```
1984            # Send a confirmation message to the user.
1985            try:
1986                send_mail(self, fromaddr, destaddr, "Sage Notebook Registration",body)
1987                waiting[key] = filled_in['username']
1988            except ValueError:
1989                pass
```


If 3.0.6 comes out few days after August 1st then instead of copying this out I'll make the email inputbox optional by the admin with the default set to False.

'email_system' = False


---

Attachment


---

Comment by TimothyClemans created at 2008-08-03 22:13:15

Point #1 addressed by extcode-3649_1.patch. I'm starting to address #2. I will make email optional. If email services are off then automated account recovery will be disabled.


---

Attachment


---

Comment by TimothyClemans created at 2008-08-04 20:21:18

Note: there is a script for applying the various Notebook patches. The base is sage-3.0.6.

http://sage.math.washington.edu/home/tclemans/uw_contract_work/apply_patches.sage


---

Comment by was created at 2008-08-05 05:01:19

WOW, this is very very nice; works perfectly. 

Enthusiastic positive review.


---

Comment by mabshoff created at 2008-08-10 00:29:18

Resolution: fixed


---

Comment by mabshoff created at 2008-08-10 00:29:18

Merged in Sage 3.1.alpha1
