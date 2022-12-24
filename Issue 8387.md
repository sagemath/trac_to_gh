# Issue 8387: help (notebook) examples use deprecated usage.

archive/issues_008387.json:
```json
{
    "body": "Assignee: was\n\nCC:  was mvngu\n\nUsing Sage 4.3.3\n\nhelp(notebook) shows \n\n\n```\n |      - ``interface`` -- string (default: ``'localhost'``), address\n |        of network interface to listen on; give ``''`` to listen on\n |        all interfaces.  You may use ``address`` here for backwards\n |        compatibility, but this is deprecated and will be removed in\n |        the future.\n\n```\n\n\nThen the second and fourth examples use 'address'. \n\n\n```\n |         notebook(address='', secure=True)\n\n |         notebook(address='', server_pool=['sage1@localhost'],\n |         ulimit='-v 500000', accounts=True)\n\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8387\n\n",
    "created_at": "2010-02-27T15:59:48Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "help (notebook) examples use deprecated usage.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8387",
    "user": "drkirkby"
}
```
Assignee: was

CC:  was mvngu

Using Sage 4.3.3

help(notebook) shows 


```
 |      - ``interface`` -- string (default: ``'localhost'``), address
 |        of network interface to listen on; give ``''`` to listen on
 |        all interfaces.  You may use ``address`` here for backwards
 |        compatibility, but this is deprecated and will be removed in
 |        the future.

```


Then the second and fourth examples use 'address'. 


```
 |         notebook(address='', secure=True)

 |         notebook(address='', server_pool=['sage1@localhost'],
 |         ulimit='-v 500000', accounts=True)

```




Issue created by migration from https://trac.sagemath.org/ticket/8387





---

archive/issue_comments_075066.json:
```json
{
    "body": "Attachment [trac_8387-nb_object_docstring.patch](tarball://root/attachments/some-uuid/ticket8387/trac_8387-nb_object_docstring.patch) by mpatel created at 2010-02-27 23:17:33\n\n\"address\" --> \"interface\".  sagenb repo.",
    "created_at": "2010-02-27T23:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75066",
    "user": "mpatel"
}
```

Attachment [trac_8387-nb_object_docstring.patch](tarball://root/attachments/some-uuid/ticket8387/trac_8387-nb_object_docstring.patch) by mpatel created at 2010-02-27 23:17:33

"address" --> "interface".  sagenb repo.



---

archive/issue_comments_075067.json:
```json
{
    "body": "The `notebook` [docstring](http://www.sagemath.org/doc/reference/sagenb/notebook/notebook_object.html) refers to a chapter \"Running the Sage Notebook Securely\" in the installation guide.  Does this chapter / section exist?  I can update the patch.",
    "created_at": "2010-02-27T23:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75067",
    "user": "mpatel"
}
```

The `notebook` [docstring](http://www.sagemath.org/doc/reference/sagenb/notebook/notebook_object.html) refers to a chapter "Running the Sage Notebook Securely" in the installation guide.  Does this chapter / section exist?  I can update the patch.



---

archive/issue_comments_075068.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-27T23:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75068",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075069.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-27T23:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75069",
    "user": "mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075070.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> The `notebook` [docstring](http://www.sagemath.org/doc/reference/sagenb/notebook/notebook_object.html) refers to a chapter \"Running the Sage Notebook Securely\" in the installation guide.  Does this chapter / section exist?\n\nThere is no such chapter/section in the Installation Guide. Could you remove any mention of \"Running the Sage Notebook Securely\"?",
    "created_at": "2010-02-27T23:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75070",
    "user": "mvngu"
}
```

Replying to [comment:1 mpatel]:
> The `notebook` [docstring](http://www.sagemath.org/doc/reference/sagenb/notebook/notebook_object.html) refers to a chapter "Running the Sage Notebook Securely" in the installation guide.  Does this chapter / section exist?

There is no such chapter/section in the Installation Guide. Could you remove any mention of "Running the Sage Notebook Securely"?



---

archive/issue_comments_075071.json:
```json
{
    "body": "Attachment [trac_8387-nb_object_docstring.2.patch](tarball://root/attachments/some-uuid/ticket8387/trac_8387-nb_object_docstring.2.patch) by mpatel created at 2010-02-28 00:04:29\n\nDon't refer to non-existent chapter.  Nicer wiki links.  Replaces previous.",
    "created_at": "2010-02-28T00:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75071",
    "user": "mpatel"
}
```

Attachment [trac_8387-nb_object_docstring.2.patch](tarball://root/attachments/some-uuid/ticket8387/trac_8387-nb_object_docstring.2.patch) by mpatel created at 2010-02-28 00:04:29

Don't refer to non-existent chapter.  Nicer wiki links.  Replaces previous.



---

archive/issue_comments_075072.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-28T00:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75072",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075073.json:
```json
{
    "body": "Done.",
    "created_at": "2010-02-28T00:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75073",
    "user": "mpatel"
}
```

Done.



---

archive/issue_comments_075074.json:
```json
{
    "body": "I see you have changed one bit to \n\n\n```\nnotebook(interface='', server_pool=['sage1@localhost'], \n```\n\n\nDoes the server_pool bit actually work? It certainly does not for me. I find the only way to Sage to use another account is to put something like in a python file, and get python to load it at startup. Otherwise, ussing server_pool in the way documented fails. \n\n\n```\nserver_pool=['sage1@localhost']\n\nn.notebook('sage_notebook', port=8000, accounts=True, address='',\n         server_pool = server_pool, ulimit='-u 1000 -v 1000000 -t 3600',\n    open_viewer=False, timeout=20*60, secure=False, port_tries=0)\n\n```\n\n\n\n\nPerhaps this is outside the ticket, but if it does not work, perhaps its better to remove any examples showing how to user server_pool. \n\nDave",
    "created_at": "2010-02-28T00:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75074",
    "user": "drkirkby"
}
```

I see you have changed one bit to 


```
notebook(interface='', server_pool=['sage1@localhost'], 
```


Does the server_pool bit actually work? It certainly does not for me. I find the only way to Sage to use another account is to put something like in a python file, and get python to load it at startup. Otherwise, ussing server_pool in the way documented fails. 


```
server_pool=['sage1@localhost']

n.notebook('sage_notebook', port=8000, accounts=True, address='',
         server_pool = server_pool, ulimit='-u 1000 -v 1000000 -t 3600',
    open_viewer=False, timeout=20*60, secure=False, port_tries=0)

```




Perhaps this is outside the ticket, but if it does not work, perhaps its better to remove any examples showing how to user server_pool. 

Dave



---

archive/issue_comments_075075.json:
```json
{
    "body": "Changing assignee from was to drkirkby.",
    "created_at": "2010-02-28T00:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75075",
    "user": "drkirkby"
}
```

Changing assignee from was to drkirkby.



---

archive/issue_comments_075076.json:
```json
{
    "body": "My god, I did manage to make a few mistakes in that lot!! I should have re-read before posting!\n\n\n```\nimport sagenb.notebook.notebook_object as n\n\nserver_pool=['sage1@localhost']\n\nn.notebook('sage_notebook', port=8000, accounts=True, address='',\n         server_pool = server_pool, ulimit='-u 1000 -v 1000000 -t 3600',\n    open_viewer=False, timeout=20*60, secure=False, port_tries=0)\n\n```\n \n\nworks, but specifying a server pool at the Sage prompt with something like: \n\n\n```\nnotebook(interface='', server_pool=['sage1@localhost'], \n```\n\n\ndoes not work for me. It might be a Solaris specific issue of course. \n\nDave",
    "created_at": "2010-02-28T00:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75076",
    "user": "drkirkby"
}
```

My god, I did manage to make a few mistakes in that lot!! I should have re-read before posting!


```
import sagenb.notebook.notebook_object as n

server_pool=['sage1@localhost']

n.notebook('sage_notebook', port=8000, accounts=True, address='',
         server_pool = server_pool, ulimit='-u 1000 -v 1000000 -t 3600',
    open_viewer=False, timeout=20*60, secure=False, port_tries=0)

```
 

works, but specifying a server pool at the Sage prompt with something like: 


```
notebook(interface='', server_pool=['sage1@localhost'], 
```


does not work for me. It might be a Solaris specific issue of course. 

Dave



---

archive/issue_comments_075077.json:
```json
{
    "body": "What happens, exactly?",
    "created_at": "2010-02-28T00:36:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75077",
    "user": "mpatel"
}
```

What happens, exactly?



---

archive/issue_comments_075078.json:
```json
{
    "body": "I'm 99% sure that supplying the serverpool on the command line with:\n\n$ sage -notebook \n\nfails, but I believe the problem I had last night (see below) goes away if I don't use a server pool. \n\n\n```             \nTraceback (click to the left of this block for traceback)\n...\nNameError: name '_interact_' is not defined\n\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_3.py\", line 8, in <module>\n    _interact_.SAGE_CELL_ID=1\nNameError: name '_interact_' is not defined \n```\n\n\nPerhaps I need to spend more time double-checking this, but my belief was the options were not propagating properly. \n\nDave",
    "created_at": "2010-02-28T01:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75078",
    "user": "drkirkby"
}
```

I'm 99% sure that supplying the serverpool on the command line with:

$ sage -notebook 

fails, but I believe the problem I had last night (see below) goes away if I don't use a server pool. 


```             
Traceback (click to the left of this block for traceback)
...
NameError: name '_interact_' is not defined

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_3.py", line 8, in <module>
    _interact_.SAGE_CELL_ID=1
NameError: name '_interact_' is not defined 
```


Perhaps I need to spend more time double-checking this, but my belief was the options were not propagating properly. 

Dave



---

archive/issue_comments_075079.json:
```json
{
    "body": "It may be better to ask on sage-devel or sage-notebook about this problem.",
    "created_at": "2010-02-28T01:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75079",
    "user": "mpatel"
}
```

It may be better to ask on sage-devel or sage-notebook about this problem.



---

archive/issue_comments_075080.json:
```json
{
    "body": "I thought it was a general problem - not one specific to me. In which case ignore what I said. \n\nThat looks fine to me. Positive review.",
    "created_at": "2010-02-28T02:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75080",
    "user": "drkirkby"
}
```

I thought it was a general problem - not one specific to me. In which case ignore what I said. 

That looks fine to me. Positive review.



---

archive/issue_comments_075081.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-28T02:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75081",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075082.json:
```json
{
    "body": "It could well be a general problem(s).  Is #2827 relevant?  I don't have much experience with the `server_pool` option, but sage-devel/notebook regulars should be able to help.",
    "created_at": "2010-02-28T04:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75082",
    "user": "mpatel"
}
```

It could well be a general problem(s).  Is #2827 relevant?  I don't have much experience with the `server_pool` option, but sage-devel/notebook regulars should be able to help.



---

archive/issue_comments_075083.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-04T22:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8387#issuecomment-75083",
    "user": "mpatel"
}
```

Resolution: fixed
