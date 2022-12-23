# Issue 4309: Kerberos authentification for SAGE notebook

Issue created by migration from https://trac.sagemath.org/ticket/4309

Original creator: kkilger

Original creation time: 2008-10-16 17:30:31

Assignee: was

CC:  embray jdemeyer fbissey

This patch adds Kerberos authentification support for the SAGE notebook. It also adds the options krb_srv, krb_realm for the notebook() command.

This patch however depends on pykerberos which depends on kerberos which depends on a couple of other libraries all in all a little less size than SAGE itself and all not in SAGE :-). Nevertheless ... 

Greetings, 
Kilian. 


---

Attachment


---

Comment by TimothyClemans created at 2008-11-09 21:35:46

This doesn't apply in sage-3.2.alpha1


---

Attachment


---

Comment by TimothyClemans created at 2008-11-09 23:58:32

Kerberos shouldn't be required to use the notebook. Make Kerberos authentication optional.


---

Comment by TimothyClemans created at 2008-11-10 00:00:25

my.patch is replaced by sage-3950_1.patch and applies in sage-3.2.alpha1


---

Attachment


---

Comment by TimothyClemans created at 2008-11-10 02:08:50

OK now Kerberos isn't required.


---

Attachment


---

Comment by TimothyClemans created at 2008-11-10 04:31:03

Changing component from user interface to notebook.


---

Comment by TimothyClemans created at 2008-11-10 04:31:03

Changing assignee from was to kkilger.


---

Comment by was created at 2008-11-29 03:01:03

Hi,

I like the design of this patch and how the kerberos stuff is optional.  

Unfortunately, this is hard to referee if you don't explain to me how to install pykerberos.  Also, the patch itself should contain code that says "hey, you need kerberos, and here's how to install it" when the user turns on kerberos via an option to notebook, but 

```
import kerberos
```

fails.  That could be either a paragraph of text, an optional spkg to install, or a link to a wiki page that describes what to do.  

OK?

Thanks!


---

Comment by chapoton created at 2019-06-16 18:29:58

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2019-06-16 18:29:58

notebook is deprecated, so this can probably be closed


---

Comment by fbissey created at 2019-06-16 18:32:59

Changing status from needs_review to positive_review.


---

Comment by fbissey created at 2019-06-16 18:32:59

Yes.


---

Comment by chapoton created at 2019-06-16 20:08:07

Resolution: wontfix
