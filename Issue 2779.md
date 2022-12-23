# Issue 2779: Error message for notebook server already running is misleading

Issue created by migration from https://trac.sagemath.org/ticket/2779

Original creator: justin

Original creation time: 2008-04-02 20:38:45

Assignee: boothby

If I have a notebook server already running, and I start a new one, I get something like this:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.11, Release Date: 2008-03-30                        |
| Type notebook() for the GUI, and license() for information.        |
Please wait while the SAGE Notebook server starts...
...
The notebook files are stored in: /Users/justin/.sage//sage_notebook
Port 8000 is already in use.
Trying next port...
****************************************************
*                                                  *
* Open your web browser to https://localhost:8001  *
*                                                  *
****************************************************
There is an admin account.  If you do not remember the password,
quit the notebook and type notebook(reset=True).
Another twistd server is running, PID 19662

This could either be a previously started instance of your application or a
different application entirely. To start a new one, either run it in some other
directory, or use the --pidfile and --logfile parameters to avoid clashes.
```


It's not clear how to use the second suggestion (using the additional parameters), and I sure couldn't get it to work.

Using an alternate directory does work, but that somehow didn't come through in this error message.




---

Comment by was created at 2008-04-02 21:55:36

Could you suggest a specific better error message?  Oh, and post a patch :-)


---

Comment by timdumol created at 2010-01-16 20:37:24

This new patch should do it. It outputs the following message instead:


```
Another Sage Notebook server is running, PID 13463.

Please either stop the old server or run the new server in a different directory.
```



---

Comment by timdumol created at 2010-01-16 20:37:24

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-16 23:30:15

Outputs a clearer error message (see comment)


---

Attachment


---

Attachment

Positive review for Tim's patch. It works great for me.

I've added a second minor patch (to be applied after `trac_2779-sagenb-error-message.patch`) that moves displaying the "Please open your browser" banner to below the check Tim added.


---

Comment by timdumol created at 2010-01-17 19:58:54

Positive review on the reviewer patch. I'll mark this as positive review now.


---

Comment by timdumol created at 2010-01-17 19:58:54

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-19 03:32:07

Resolution: fixed
