# Issue 2935: notebook: internal server error sage-3.0.alpha5

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2008-04-15 18:11:04

Assignee: boothby

Trying to delete some old worksheets, this happened:


```
[jaap`@`paix sage-3.0.alpha5]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.alpha5, Release Date: 2008-04-15                  |
| Type notebook() for the GUI, and license() for information.        |

sage: notebook()
The notebook files are stored in: /home/jaap/.sage//sage_notebook
Port 8000 is already in use.
Trying next port...
****************************************************
*                                                  *
* Open your web browser to https://localhost:8001  *
*                                                  *
****************************************************
There is an admin account.  If you do not remember the password,
quit the notebook and type notebook(reset=True).
Removing stale pidfile /home/jaap/.sage/sage_notebook/twistd.pd
2008-04-15 19:54:17+0200 [-] Log opened.
2008-04-15 19:54:17+0200 [-] twistd 8.0.1 (/home/jaap/downloads/sage-3.0.alpha5/local/bin/python 2.5.1) starting up
2008-04-15 19:54:17+0200 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008-04-15 19:54:17+0200 [-] twisted.web2.channel.http.HTTPFactory starting on 8001
2008-04-15 19:54:17+0200 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0xa6cdc4c>
2008-04-15 19:55:24+0200 [HTTPChannel,3,127.0.0.1] /home/jaap/downloads/sage-3.0.alpha5/local/lib/python2.5/site-packages/twisted/internet/defer.py:262: exceptions.DeprecationWarning: Don't pass strings (like 'Bad token') to failure.Failure (replacing with a DefaultException).
2008-04-15 19:55:24+0200 [HTTPChannel,3,127.0.0.1] Exception rendering:
2008-04-15 19:55:24+0200 [HTTPChannel,3,127.0.0.1] Unhandled Error
        Traceback (most recent call last):
        Failure: twisted.python.failure.DefaultException: Bad token


}}

Jaap




---

Comment by mabshoff created at 2008-04-15 19:12:22

Well, there already seems to be a notebook running on port 8000, so could that have something to do with that? Can you check and report back?

Do we support more than one notebook running from the same Sage instance?

Cheers,

Michael


---

Comment by jsp created at 2008-04-15 20:03:28

Replying to [comment:1 mabshoff]:
> Well, there already seems to be a notebook running on port 8000, so could that have something to do with that? Can you check and report back?
>

No, this is not the case. No notebook on port 8000.

 
> Do we support more than one notebook running from the same Sage instance?
> 

I don't think so. I would love to have the possibility to run
more notebooks from different versions of sage!



Jaap


> Cheers,
> 
> Michael


---

Comment by was created at 2008-04-16 21:44:01

Neither tom nor I can replicate this.

Could you try with a fresh NOTEBOOK directory?  E.g.,

  sage: notebook(directory = 'foo')

william


---

Comment by jsp created at 2008-04-16 22:43:05

Let me tell what I did a few minutes ago.

I created a worksheet 'test' with sage-2.11, saved it and quit.

Started the notebook under sage-3.0.alpha5, selected 'test' and clicked on delete.

With the error mentioned above :(

Worksheets created with earlier versions and with alpha5 don't give this error!

Jaap


---

Comment by jsp created at 2008-04-16 22:57:06

Follow up: selecting an old ws and clicking on 'Archive' cased the same error here.


---

Comment by jsp created at 2008-04-17 19:55:30

I reproduced this failure on a different machine Fedora 8, 32 bits with a ws
made under sage-2.11. using Firefox-2.0.0.13.

Narrowing(?) this down: I get the same failure under sage-2.11 :(

Starting the notebook and selecting nothing(!) clicking on Archive or Delete gives the internal server error. Both on Fedora 7 and 8.



Jaap


---

Comment by jsp created at 2008-04-17 21:50:21

Replying to [comment:6 jsp]:
> I reproduced this failure on a different machine Fedora 8, 32 bits with a ws
> made under sage-2.11. using Firefox-2.0.0.13.
> 
> Narrowing(?) this down: I get the same failure under sage-2.11 :(
> 
> Starting the notebook and selecting nothing(!) clicking on Archive or Delete gives the internal server error. Both on Fedora 7 and 8.
> 
> 
> 
> Jaap


Even with sage-2.10.4, just clicking in the overview on Delete:


```
[jaap`@`paix sage-2.10.4]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.4, Release Date: 2008-03-16                      |
| Type notebook() for the GUI, and license() for information.        |

sage: notebook()
The notebook files are stored in: /home/jaap/.sage//sage_notebook
Port 8000 is already in use.
Trying next port...
****************************************************
*                                                  *
* Open your web browser to https://localhost:8001  *
*                                                  *
****************************************************
There is an admin account.  If you do not remember the password,
quit the notebook and type notebook(reset=True).
Removing stale pidfile /home/jaap/.sage/sage_notebook/twistd.pd
2008/04/17 23:11 +0200 [-] Log opened.
2008/04/17 23:11 +0200 [-] twistd 2.5.0 (/home/jaap/downloads/sage-2.10.4/local/bin/python 2.5.1) starting up
2008/04/17 23:11 +0200 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008/04/17 23:11 +0200 [-] Loading sage_notebook/twistedconf.tac...
2008/04/17 23:12 +0200 [-] Loaded.
2008/04/17 23:12 +0200 [-] twisted.web2.channel.http.HTTPFactory starting on 8001
2008/04/17 23:12 +0200 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0x8b9082c>
2008/04/17 23:12 +0200 [HTTPChannel,1,127.0.0.1] /home/jaap/downloads/sage-2.10.4/local/lib/python2.5/site-packages/twisted/internet/defer.py:259: exceptions.DeprecationWarning: Don't pass strings (like 'Bad token') to failure.Failure (replacing with a DefaultException).
2008/04/17 23:12 +0200 [HTTPChannel,1,127.0.0.1] Exception rendering:
2008/04/17 23:12 +0200 [HTTPChannel,1,127.0.0.1] Unhandled Error
        Traceback (most recent call last):
        Failure: twisted.python.failure.DefaultException: Bad token




```



So I'm flabbergasted

Jaap


---

Comment by jsp created at 2008-04-18 13:48:33

This issue seems to be introduced with sage-2.10.1.

In sage-2.9 clicking on the Archive button gives a warning.

I put up some screen shots here: http://sage.math.washington.edu/home/jsp/screenshots/s1/

Jaap


---

Comment by mabshoff created at 2008-04-18 20:33:33

Could this have something to do with encoding? Jaap: what is the locale you use?

Cheers,

Michael


---

Comment by jsp created at 2008-04-18 20:44:35

Replying to [comment:9 mabshoff]:
> Could this have something to do with encoding? Jaap: what is the locale you use?
> 
> Cheers,
> 
> Michael


Don't think so. My Fedora install is just English (American). I do not use
any localization.

Jaap


---

Comment by was created at 2008-04-20 17:23:30

Can anybody but Jaap replicate this problem?


---

Comment by jsp created at 2008-04-22 15:55:19

How about this:

```
William Stein wrote:
>
> 
> Please do
>    sage: hg_sage.pull()
> 
> then
> 
>    sage -br
> 
> and try that test again

Something strange was going on with the notebook(), but
after hg_sage.pull() and ./sage -br the notebook
starts in Firefox with still the problem I have reported in trac #2935.

But when I start firefox by hand:  https://localhost:8001/
everything seems to work!

Jaap


```



---

Comment by jsp created at 2008-04-22 16:45:41

Once again this is what I do now to avoid the error:

Start the notebook in sage-3.0.

Close the notebook tab in firefox.

Connect to https://localhost:8001/

Now I have a notebook running in which I can Archive en Delete worksheets.

Jaap


---

Comment by was created at 2008-05-10 23:17:43

Since nobody else can replicate this, and it could just be some weird cookie corruption on Jaap's computer (or a weird firefox bug), I'm closing this as invalid.


---

Comment by was created at 2008-05-10 23:17:43

Resolution: invalid
