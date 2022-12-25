# Issue 7972: show_identifiers is broken in the notebook; needs to not include globals

archive/issues_007972.json:
```json
{
    "body": "Assignee: @williamstein\n\n`show_identifiers` works fine on the command line, but not in the notebook.\n\n```\nWhen I use show_identifiers() from the command line, the behaviour is\nas described.  But if I use it from a notebook, then it returns an\narray with 1746 elements, even if I call reset().  The first few\nelements are\n\n['paretovariate', 'is_MPolynomial', 'cartan_matrix',\n'is_NumberFieldElement', 'elliptic_curves', 'sleep',\n\nWould it be more sensible not to display these omnipresent\nidentifiers?  It's hard to find my own variables in the mess!\n(I'm on 10.6, core 2 duo, running 4.3, if this is a bug)\n\nCheers,\nFelix\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7972\n\n",
    "created_at": "2010-01-18T06:13:19Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "show_identifiers is broken in the notebook; needs to not include globals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7972",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

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

Issue created by migration from https://trac.sagemath.org/ticket/7972





---

archive/issue_comments_069420.json:
```json
{
    "body": "```\n[sage-support] How to list (and remove) loaded objects in a sage session\n\t\t\t\t\n\tInbox\t\tX\t\n\t\t\t\t\nShing Hing Man\t\nHi, In a Sage session (within notebook or command console) , how to list all ...\n\t\nJan 16 (1 day ago)\nSimon King\t\nHi Shing! AFAIK, it is the same as in Python, so, if you need references, it ...\n\t\nJan 16 (1 day ago)\nSimon King\t\nPS: >... That said: The above reference is just meant as some background info...\n\t\nJan 16 (1 day ago)\nWilliam Stein\t\n2010/1/16 Shing Hing Man <matmsh@yahoo.com>: Use show_identifiers and reset: ...\n\t\nJan 16 (1 day ago)\nShing Hing Man\t\nThanks for all the reply! show_identifiers() and reset() are what I am lookin...\n\t\n7:53 AM (14 hours ago)\n \nReply to all\n \nFelix Lawrence\n to sage-support\n\t\nshow details 9:16 PM (56 minutes ago)\n\t\nOn Jan 17, 11:35 am, William Stein <wst...@gmail.com> wrote:\n> 2010/1/16 Shing Hing Man <mat...@yahoo.com>:\n>\n> > Hi,\n> >   In a Sage session (within notebook or command console) ,  how to\n> > list all the loaded objects and how to remove them from the session ?\n>\n> Use show_identifiers and reset:\n>\n> sage: X = 10\n> sage: show_identifiers()\n> ['X', 'Out', 'variables', 'In', 'view_all']\n> sage: reset()\n> sage: show_identifiers()\n> []\n\nWhen I use show_identifiers() from the command line, the behaviour is\nas described.  But if I use it from a notebook, then it returns an\narray with 1746 elements, even if I call reset().  The first few\nelements are\n\n['paretovariate', 'is_MPolynomial', 'cartan_matrix',\n'is_NumberFieldElement', 'elliptic_curves', 'sleep',\n\nWould it be more sensible not to display these omnipresent\nidentifiers?  It's hard to find my own variables in the mess!\n(I'm on 10.6, core 2 duo, running 4.3, if this is a bug)\n\nCheers,\nFelix\n\n--\nTo post to this group, send email to sage-support@googlegroups.com\nTo unsubscribe from this group, send email to sage-support+unsubscribe@googlegroups.com\nFor more options, visit this group at http://groups.google.com/group/sage-support\nURL: http://www.sagemath.org\n\nReply\n\t\nReply to all\n\t\nForward\n\t\t\n\t\t\nOpen message in new window\n \nSend\n \nSave Now\n \nDiscard\nTo:\t\t \nCc:\t\nBcc:\t\n \tAdd Cc | Add Bcc | Edit Subject    Attach a file    Add event invitation   Canned responses\nSubject:\t\n \t\nAttachment file \t\nAttach a file\nLoading rich text... Rich formatting \u00bb\tCheck SpellingChange language Resume Editing\n \t\n\t \n \nSend\n \nSave Now\n \nDiscard\n \nReply to all\n \nMinh Nguyen\n to sage-support\n\t\nshow details 9:27 PM (45 minutes ago)\n\t\nHi Felix,\n\nOn Mon, Jan 18, 2010 at 4:16 PM, Felix Lawrence\n<felix@physics.usyd.edu.au> wrote:\n\n<SNIP>\n\n> Would it be more sensible not to display these omnipresent\n> identifiers?  It's hard to find my own variables in the mess!\n\nI can replicate this on Linux (the machine mod.math). With a notebook\nsession of Sage 4.3.1.rc0, issue \"show_identifiers()\". Then issue\n\"reset()\" and execute \"show_identifiers()\" again. This time, I\nreceived a NameError:\n\nTraceback (most recent call last):\n File \"<stdin>\", line 1, in <module>\n File \"_sage_input_7.py\", line 4, in <module>\n   open(\"___code___.py\",\"w\").write(_support_.preparse_worksheet_cell(base64.b64decode(\"c2hvd19pZGVudGlmaWVycygp\"),globals())+\"\\n\");\nexecfile(os.path.abspath(\"___code___.py\"))\n File \"\", line 1, in <module>\n\nNameError: name 'base64' is not defined\n\n--\nRegards\nMinh Van Nguyen\n\t\t\n```",
    "created_at": "2010-01-18T06:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7972#issuecomment-69420",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_069421.json:
```json
{
    "body": "Attachment [trac_7972.patch](tarball://root/attachments/some-uuid/ticket7972/trac_7972.patch) by @williamstein created at 2010-01-18 07:09:13",
    "created_at": "2010-01-18T07:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7972#issuecomment-69421",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7972.patch](tarball://root/attachments/some-uuid/ticket7972/trac_7972.patch) by @williamstein created at 2010-01-18 07:09:13



---

archive/issue_comments_069422.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T07:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7972#issuecomment-69422",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069423.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T01:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7972#issuecomment-69423",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069424.json:
```json
{
    "body": "Applying the patch to 4.3, this works.  In the notebook, running reset() then show_identifiers() returns only ['DATA', 'base64'], which are excluded from the call to reset().",
    "created_at": "2010-01-19T01:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7972#issuecomment-69424",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Applying the patch to 4.3, this works.  In the notebook, running reset() then show_identifiers() returns only ['DATA', 'base64'], which are excluded from the call to reset().



---

archive/issue_events_019076.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-19T05:58:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7972",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7972#event-19076"
}
```



---

archive/issue_comments_069425.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T05:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7972#issuecomment-69425",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_019077.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-19T10:02:44Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7972",
    "milestone": "sage-4.3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7972#event-19077"
}
```
