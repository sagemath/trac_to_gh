# Issue 7972: show_identifiers is broken in the notebook; needs to not include globals

Issue created by migration from https://trac.sagemath.org/ticket/7972

Original creator: was

Original creation time: 2010-01-18 06:13:19

Assignee: was

`show_identifiers` works fine on the command line, but not in the notebook.

```
When I use show_identifiers() from the command line, the behaviour is
as described.  But if I use it from a notebook, then it returns an
array with 1746 elements, even if I call reset().  The first few
elements are

['paretovariate', 'is_MPolynomial', 'cartan_matrix',
'is_NumberFieldElement', 'elliptic_curves', 'sleep',

Would it be more sensible not to display these omnipresent
identifiers?  It's hard to find my own variables in the mess!
(I'm on 10.6, core 2 duo, running 4.3, if this is a bug)

Cheers,
Felix

```



---

Comment by was created at 2010-01-18 06:13:56


```
[sage-support] How to list (and remove) loaded objects in a sage session
				
	Inbox		X	
				
Shing Hing Man	
Hi, In a Sage session (within notebook or command console) , how to list all ...
	
Jan 16 (1 day ago)
Simon King	
Hi Shing! AFAIK, it is the same as in Python, so, if you need references, it ...
	
Jan 16 (1 day ago)
Simon King	
PS: >... That said: The above reference is just meant as some background info...
	
Jan 16 (1 day ago)
William Stein	
2010/1/16 Shing Hing Man <matmsh@yahoo.com>: Use show_identifiers and reset: ...
	
Jan 16 (1 day ago)
Shing Hing Man	
Thanks for all the reply! show_identifiers() and reset() are what I am lookin...
	
7:53 AM (14 hours ago)
 
Reply to all
 
Felix Lawrence
 to sage-support
	
show details 9:16 PM (56 minutes ago)
	
On Jan 17, 11:35 am, William Stein <wst...@gmail.com> wrote:
> 2010/1/16 Shing Hing Man <mat...@yahoo.com>:
>
> > Hi,
> >   In a Sage session (within notebook or command console) ,  how to
> > list all the loaded objects and how to remove them from the session ?
>
> Use show_identifiers and reset:
>
> sage: X = 10
> sage: show_identifiers()
> ['X', 'Out', 'variables', 'In', 'view_all']
> sage: reset()
> sage: show_identifiers()
> []
|
When I use show_identifiers() from the command line, the behaviour is
as described.  But if I use it from a notebook, then it returns an
array with 1746 elements, even if I call reset().  The first few
elements are

['paretovariate', 'is_MPolynomial', 'cartan_matrix',
'is_NumberFieldElement', 'elliptic_curves', 'sleep',

Would it be more sensible not to display these omnipresent
identifiers?  It's hard to find my own variables in the mess!
(I'm on 10.6, core 2 duo, running 4.3, if this is a bug)

Cheers,
Felix

--
To post to this group, send email to sage-support@googlegroups.com
To unsubscribe from this group, send email to sage-support+unsubscribe@googlegroups.com
For more options, visit this group at http://groups.google.com/group/sage-support
URL: http://www.sagemath.org

Reply
	
Reply to all
	
Forward
		
		
Open message in new window
 
Send
 
Save Now
 
Discard
To:		 
Cc:	
Bcc:	
 	Add Cc | Add Bcc | Edit Subject    Attach a file    Add event invitation   Canned responses
Subject:	
 	
Attachment file 	
Attach a file
Loading rich text... Rich formatting »	Check SpellingChange language Resume Editing
 	
	 
 
Send
 
Save Now
 
Discard
 
Reply to all
 
Minh Nguyen
 to sage-support
	
show details 9:27 PM (45 minutes ago)
	
Hi Felix,
|
On Mon, Jan 18, 2010 at 4:16 PM, Felix Lawrence
<felix@physics.usyd.edu.au> wrote:

<SNIP>

> Would it be more sensible not to display these omnipresent
> identifiers?  It's hard to find my own variables in the mess!

I can replicate this on Linux (the machine mod.math). With a notebook
session of Sage 4.3.1.rc0, issue "show_identifiers()". Then issue
"reset()" and execute "show_identifiers()" again. This time, I
received a NameError:

Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "_sage_input_7.py", line 4, in <module>
   open("___code___.py","w").write(_support_.preparse_worksheet_cell(base64.b64decode("c2hvd19pZGVudGlmaWVycygp"),globals())+"\n");
execfile(os.path.abspath("___code___.py"))
 File "", line 1, in <module>

NameError: name 'base64' is not defined

--
Regards
Minh Van Nguyen
		
```



---

Attachment


---

Comment by was created at 2010-01-18 07:09:26

Changing status from new to needs_review.


---

Comment by flawrence created at 2010-01-19 01:05:57

Changing status from needs_review to positive_review.


---

Comment by flawrence created at 2010-01-19 01:05:57

Applying the patch to 4.3, this works.  In the notebook, running reset() then show_identifiers() returns only ['DATA', 'base64'], which are excluded from the call to reset().


---

Comment by rlm created at 2010-01-19 05:58:02

Resolution: fixed
