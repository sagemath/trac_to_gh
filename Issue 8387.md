# Issue 8387: help (notebook) examples use deprecated usage.

Issue created by migration from https://trac.sagemath.org/ticket/8387

Original creator: drkirkby

Original creation time: 2010-02-27 15:59:48

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





---

Attachment

"address" --> "interface".  sagenb repo.


---

Comment by mpatel created at 2010-02-27 23:25:20

The `notebook` [docstring](http://www.sagemath.org/doc/reference/sagenb/notebook/notebook_object.html) refers to a chapter "Running the Sage Notebook Securely" in the installation guide.  Does this chapter / section exist?  I can update the patch.


---

Comment by mpatel created at 2010-02-27 23:25:20

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-02-27 23:39:05

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-02-27 23:39:05

Replying to [comment:1 mpatel]:
> The `notebook` [docstring](http://www.sagemath.org/doc/reference/sagenb/notebook/notebook_object.html) refers to a chapter "Running the Sage Notebook Securely" in the installation guide.  Does this chapter / section exist?

There is no such chapter/section in the Installation Guide. Could you remove any mention of "Running the Sage Notebook Securely"?


---

Attachment

Don't refer to non-existent chapter.  Nicer wiki links.  Replaces previous.


---

Comment by mpatel created at 2010-02-28 00:04:57

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-02-28 00:04:57

Done.


---

Comment by drkirkby created at 2010-02-28 00:18:50

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

Comment by drkirkby created at 2010-02-28 00:18:50

Changing assignee from was to drkirkby.


---

Comment by drkirkby created at 2010-02-28 00:22:06

My god, I did manage to make a few mistakes in that lot!! I should have re-read before posting!


```
import sagenb.notebook.notebook_object as n

server_pool=['sage1@localhost']

n.notebook('sage_notebook', port=8000, accounts=True, address='',
         server_pool = server_pool, ulimit='-u 1000 -v 1000000 -t 3600',
    open_viewer=False, timeout=20*60, secure=False, port_tries=0)

}}} 

works, but specifying a server pool at the Sage prompt with something like: 

{{{
notebook(interface='', server_pool=['sage1@localhost'], 
}}}

does not work for me. It might be a Solaris specific issue of course. 

Dave


---

Comment by mpatel created at 2010-02-28 00:36:36

What happens, exactly?


---

Comment by drkirkby created at 2010-02-28 01:00:02

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

Comment by mpatel created at 2010-02-28 01:48:36

It may be better to ask on sage-devel or sage-notebook about this problem.


---

Comment by drkirkby created at 2010-02-28 02:15:51

I thought it was a general problem - not one specific to me. In which case ignore what I said. 

That looks fine to me. Positive review.


---

Comment by drkirkby created at 2010-02-28 02:15:51

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-28 04:24:51

It could well be a general problem(s).  Is #2827 relevant?  I don't have much experience with the `server_pool` option, but sage-devel/notebook regulars should be able to help.


---

Comment by mpatel created at 2010-03-04 22:52:12

Resolution: fixed
