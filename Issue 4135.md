# Issue 4135: [with patch, needs review] notebook -- user management features

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-09-16 16:38:32

Assignee: boothby

New features:
- Reset a user's password
- Add a new user
- Suspend/unsuspend a user
- Temporary password shown for each user if one is set (Created by password reset and add user)


---

Comment by TimothyClemans created at 2008-09-16 16:45:46

Depends on #4134 and #2407


---

Comment by ddrake created at 2008-09-26 05:32:00

I'm trying to review this, but I can't get the patches to apply. I'm starting from a clean 3.1.2 tree. Which patches should I apply, and in what order? Should I use a different version to apply patches against?


---

Comment by TimothyClemans created at 2008-09-29 18:57:24

This ticket has been rebased.


---

Comment by jason created at 2008-09-29 21:11:19

It seems that the /user page isn't found with an existing notebook.  I created a new notebook and the /users page came up.


---

Comment by TimothyClemans created at 2008-09-29 21:15:13

I've had trouble in the pass with getting administrative users recognized by the Notebook.


---

Comment by ddrake created at 2008-09-30 01:40:34

I've applied all the necessary patches to a 3.1.3alpha1 tree, but when I try to start Sage, I get:

```
/var/tmp/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/server/notebook/twist.py in <module>()
   1935     return False
   1936 
-> 1937 from sage.server.notebook.template import registration_page_template
   1938 from sage.server.notebook.template import login_page_template
   1939 

/var/tmp/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/server/notebook/template.py in <module>()
     38 templates = ['login', 'yes_no', 'failed_login', 'register', 'admin_add_user']
     39 for name in templates:
---> 40     G[name + '_template'] =  PageTemplate(pjoin(path, '%s.template'%name))
     41 
     42 def login_page_template(accounts, default_user, is_username_error=False, is_password_error=False, welcome=None, recover=False):

/var/tmp/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/server/notebook/template.py in __init__(self, filename)
     27 class PageTemplate:
     28     def __init__(self, filename):
---> 29         file = open(filename, 'r')
     30         self.__template = Template(file.read())
     31         file.close()

IOError: [Errno 2] No such file or directory: '/var/tmp/sage-3.1.3.alpha1/data/extcode/notebook/templates/admin_add_user.template'
```

That's just the last part of the traceback; the rest doesn't seem so interesting...but let me know if you want to see it.

I've looked through the patches from 4134, 2407, and this ticket, and I don't see where the file `admin_add_user.template` is created. I have all those patches applied (except 4134, which has already been merged); how do I get that file?


---

Comment by TimothyClemans created at 2008-09-30 02:03:25

Replying to [comment:7 ddrake]:
> I've looked through the patches from 4134, 2407, and this ticket, and I don't see where the file `admin_add_user.template` is created. I have all those patches applied (except 4134, which has already been merged); how do I get that file?

Did you do ` hg_extcode.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4135/extcode-4135_1.patch') `


---

Comment by jason created at 2008-09-30 02:57:43

Or if you're using queues and don't want to mess up your tree, go to $SAGE_ROOT/data/extcode and do:


```
hg qinit
hg qimport /path/to/extcode-patch
hg qpush
```



---

Comment by mhansen created at 2008-10-24 00:02:48

Timothy, what is the relationship between this patch and #3923, #3937, and #3949.


---

Comment by TimothyClemans created at 2008-11-11 01:23:52

Apply just extcode-4135_1.patch and sage-4145_3.patch


---

Comment by TimothyClemans created at 2008-11-11 01:24:09

Changing assignee from boothby to TimothyClemans.


---

Comment by TimothyClemans created at 2008-11-11 01:24:09

Changing status from new to assigned.


---

Comment by TimothyClemans created at 2008-11-11 01:24:09

Changing type from defect to enhancement.


---

Comment by TimothyClemans created at 2008-11-11 05:20:28

Depends on #3950


---

Comment by TimothyClemans created at 2008-11-11 05:33:00

Don't apply extcode-4135_1.patch afterall


---

Comment by TimothyClemans created at 2008-12-20 20:07:05

Apply sage-4135_3.patch and sage-4135_4.patch


---

Attachment


---

Comment by mabshoff created at 2009-02-02 05:13:03

Can we get a review for this since this patch is holding up several other patches?

Cheers,

Michael


---

Comment by ddrake created at 2009-02-03 00:24:17

I applied mhansen's patch to a clean 3.3.alpha3 tree, deleted my .sage/sage_notebook directory to start fresh, but I still get problems: I log in, click "Manage Users", click "Add user", then put in a name and hit "Create account". The resulting page is blank and has the title "Error | Sage Notebook".

If I hit the back button to get back to the "add a user" page, then click cancel, I get to the user management page, which lists the user I tried to add.

If I click on the user's name, I go to the usual "home page", and it lists the user's name as if I am logged in as that user...but I thought I was logged in as admin? If I then click on Settings, I can go to the user management page and...well, manage users.

Right now, this patch seems to need work. Am I doing something wrong?


---

Attachment


---

Comment by TimothyClemans created at 2009-03-16 19:42:11

There was a bug in the error_message.html template.


---

Comment by ddrake created at 2009-03-16 23:26:32

I've applied the patch to a 3.4 tree and all the bits seem to work.


---

Attachment

trac_4135.2.patch rebased for 3.4.1.rc2


---

Comment by ddrake created at 2009-04-14 01:05:44

I've rebased this patch for 3.4.1.rc2 and give it a slightly weak positive review -- I still don't know Twisted or the notebook code terribly well, and would appreciate it if someone who knows it better would also take a look at this patch.


---

Comment by mabshoff created at 2009-04-24 02:39:59

Hmm, given this is rather crucial and hard to test code I would be happy if someone else did take another look, so "needs review" to attract someone else.

Cheers,

Michael


---

Comment by timdumol created at 2009-07-27 13:37:21

Applied patch to r12658.

Everything works perfectly except for the cancel link in the Account Settings page. It links to /home, leading to a 404 Error. I believe /home/<username>/ is the proper way to link it.


---

Comment by ddrake created at 2009-07-27 22:38:00

Replying to [comment:24 timdumol]:
> Applied patch to r12658.
> 
> Everything works perfectly except for the cancel link in the Account Settings page. It links to /home, leading to a 404 Error. I believe /home/<username>/ is the proper way to link it.

I see the same error. I put in a `<pre>{{ debug()|e }}</pre>` bit (see http://jinja.pocoo.org/1/documentation/designerdoc) into `account_settings.html` and it looks like the template engine is not getting a username.


---

Comment by wjp created at 2009-09-01 17:32:16

For the cancel button not working, see the patch at #6856. (I created that ticket before seeing the issue was already mentioned here.)


---

Comment by wjp created at 2009-09-01 18:30:55

I don't understand how (or if?) this patch implements the mentioned temporary password functionality. There is a new '__temporary_password' variable, but that doesn't seem to be used.


---

Comment by ddrake created at 2009-09-01 23:49:14

Replying to [comment:27 wjp]:
> I don't understand how (or if?) this patch implements the mentioned temporary password functionality. There is a new '__temporary_password' variable, but that doesn't seem to be used.

When one adds a new user, you get a page saying "The temporary password for the new user foo is 52oN5g2a". Unfortunately, that password does not seem to be temporary; the new user can log in and out, and back in again with that password. When I read "temporary password", I think that the user will be able to log in once, and then be forced to change the password right away.

Another problem with the temporary password page is that the title of the page is "Error", even though there's no error.

That said: this patch, along with #6856 (which I just positively reviewed) does give us the basic functionality for adding users and resetting passwords from inside the notebook, which is something I'd really like. The last patch applies cleanly to 4.1.1. What do people think of merging this and opening a new ticket to fix the temporary password bits? (Or changing this patch so that it doesn't claim that the new password is temporary?)


---

Comment by wjp created at 2009-09-02 09:00:42

I'd agree with not holding up this patch because of this, because it is already a very useful feature to have.

This patch does probably have to be rebased against #6568, though.


---

Comment by ddrake created at 2009-09-03 03:07:13

rebased against 4.1.1 + #6568


---

Attachment

Rebased patch up. This should apply cleanly to the release manager's 4.1.2.alpha tree. I am going to change this to a positive review and open a new ticket for the temporary password business.

Release manager: apply only attachment:trac_4135.4.patch.


---

Comment by ddrake created at 2009-09-03 03:19:49

The temporary password ticket is #6871.


---

Comment by mvngu created at 2009-09-03 06:34:01

I got two hunk failures when merging `trac_4135.4.patch`:

```
[mvngu`@`mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4135/trac_4135.4.patch && hg qpush
adding trac_4135.4.patch to series file
applying trac_4135.4.patch
patching file sage/server/notebook/twist.py
Hunk #6 FAILED at 217
Hunk #69 FAILED at 1747
2 out of 102 hunks FAILED -- saving rejects to file sage/server/notebook/twist.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_4135.4.patch
```

This might depend on #6742, #6840, and #6568.


---

Comment by ddrake created at 2009-09-03 08:11:48

Replying to [comment:32 mvngu]:
> I got two hunk failures when merging `trac_4135.4.patch`:

(snip)

> This might depend on #6742, #6840, and #6568.

I tried applying the patch here on top of a 4.1.1 tree that already had the patches from those three tickets applied, and I get a different hunk that won't apply. Perhaps I'll wait for the alpha0 tarball to be released and rebase the patch here based on that...or, you could `hg serve` your merge tree and let me pull from that.


---

Attachment

rebased against mvngu's 4.1.2.alpha0 merge tree


---

Comment by mvngu created at 2009-09-03 10:40:01

Merged `trac_4135.5.patch`. See #6874 for a follow-up to this ticket.


---

Comment by mvngu created at 2009-09-03 10:40:01

Resolution: fixed
