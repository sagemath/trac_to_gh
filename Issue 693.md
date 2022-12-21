# Issue 693: Script to spawn a browser / start notebook.

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2007-09-19 17:39:28

Assignee: boothby

CC:  was mpatel wjp acleone mhansen jdemeyer mvngu

I've had an icon sitting on my desktop for about a week now.  When I click on it, and it starts a notebook in a background terminal and spawns a browser.  I'd like to be able to click it a second time, and open another browser window, instead of the current behavior of attempting to start another notebook.

Should work something like this:


```
if not notebook_is_running:
    notebook(settings from commandline, open_browser=True)
else:
    open_browser(settings from commandline)
```



---

Comment by timdumol created at 2009-11-15 15:35:03

Modifies `sage -notebook` to launch a browser window if the notebook is already started. Also adds a `sage -nb` shortcut.


---

Attachment

This patch should do the trick. Apply to scripts repository.


---

Comment by timdumol created at 2009-11-15 15:35:46

Changing status from new to needs_review.


---

Attachment

Checks if the notebook server is running too, instead of just checking if the PID exists.


---

Comment by timdumol created at 2009-11-18 13:33:55

I am not sure which method is preferrable, since checking if the notebook server is running does not work if the user has no permission to read `/proc` and to send signals. Please feel free to approve of either patch.


---

Attachment

Fixes bug with arguments.


---

Attachment

Same thing, without actually checking if the Twistd process is running


---

Comment by was created at 2009-11-19 21:36:25

I don't get it.  If I do

```
$  sage -notebook directory=foo port=8001 & 
$  sage -notebook directory=bar port=8002 
```

then when I execute the second line it might just pop up a notebook server pointed at port 8001.   Actually, given the line:

```
cmd = "notebook(" + ",".join([wrap(v) for v in sys.argv[1:]]) + ",port=" + SAGENB_PORT + ")"
```

I think it would give an error, since port= is specified twice. 

This is because you introduced a new environment variable SAGENB_PORT which isn't documented.  I don't know why it is there.  I think you should get the port from the port= option on the command line.

I think you should get port= from the command line and get rid of the SAGENB_PORT environment variable. 

Also, you use:

```
DOT_SAGENB = os.environ.get('DOT_SAGENB', os.path.join(os.environ['HOME'], '.sage', 'sage_notebook.sagenb'))
```

but actually, you need to use the file `os.path.join(D, 'twistd.pid')` where D is the option specified in directory= in the command line.

Finally, I think this code should be in the notebook(...) command in Sage itself.  It's wrong putting it here in this shell script, because it only half way fixes the problem.  E.g., imagine a user that types the following and leaves that in a console:

```
sage: notebook()
```


Then in another console, they type

```
sage: notebook()
```

Instead of giving an error, it should just given them the notebook.
If you put this code that you've just written in the notebook command, then both problems are automatically solved, whereas with the current code location, only half the problem is really solved.

Also, there is a notebook(fork=True) option, so one can do


```
sage: notebook(fork=True)
The notebook files are stored in: sage_notebook.sagenb
**************************************************
*                                                *
* Open your web browser to http://localhost:8001 *
*                                                *
**************************************************
<pexpect.spawn instance at 0x10bb78bd8>
sage: notebook()
# get some notebook
```





William


---

Comment by was created at 2009-11-19 21:36:25

Changing status from needs_review to needs_work.


---

Attachment

Changes run_notebook.py to launch a browser to the notebook page should an instance in the directory exist. Apply to sagenb repo. Apply this patch only.


---

Comment by timdumol created at 2009-11-21 01:34:47

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2009-11-21 01:34:47

All your points make sense. I have implemented the changes in `run_notebook.py`. I've decided to check if the process is running, since that's also what `twistd` does.


---

Comment by was created at 2009-12-08 17:03:56

Changing status from needs_review to needs_work.


---

Comment by was created at 2009-12-08 17:03:56

On OS X this doesn't work at all.  Depending on what I do either I get two notebook servers running simultaneously on the same directory (bad), or I get "Another twistd server is running, PID 40940".

On OS X there is no /proc filesystem.  However, when I run this code from this patch:

```
        try:
            print 1
            # First check using /proc directory
            if os.path.exists('/proc/%d'  % twistd_pid):
                launch_browser_to_nb()
                return
            else:
                remove_pidfile(twistd_pid_path)                
        except:
            print 2
```

I don't see "2" printed, i.e., no exception is raised.   That's clear if you read the code -- you don't raise an exception.


---

Attachment

Uses signals only to check if the process exists (as Twisted does)


---

Comment by timdumol created at 2009-12-09 12:11:20

I have removed the /proc check, since it's what Twisted does anyways.


---

Comment by timdumol created at 2009-12-09 12:11:20

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-01-20 06:54:28

I guess we need to update the patch to take advantage of #2779?


---

Comment by mpatel created at 2010-01-25 06:26:45

Open browser if server running and `open_viewer=True`.  pep8 clean-ups.  Rebased for queue in comment.  Replaces previous.


---

Attachment

V3:

 * If a server is running and `open_viewer=True`, get the settings from the old `twistedconf.tac` and browse to the server's home page.
 * Use `return` instead of `sys.exit`, in case of command-line invocation.
 * Some [pep8](http://pypi.python.org/pypi/pep8/) changes.
 * Rebased for this queue

```
sagenb-0.7 / #8051
trac_7784-hgignore_update.2.patch
trac_5712-interrupt-notification.6.patch
trac_6069-missing_pub_ws.2.patch
trac_8038-email_plus_addressing_v2.patch
trac_7506-notebook_object-documentation.2.patch
trac_693-spawn_notebook.3.patch
```



---

Comment by mpatel created at 2010-06-10 07:16:02

* I think #8473 is related.
 * V3 applies almost cleanly to SageNB 0.8:

```
applying trac_693-spawn_notebook.3.patch
patching file sagenb/notebook/run_notebook.py
Hunk #12 succeeded at 434 with fuzz 2 (offset 3 lines).
now at: trac_693-spawn_notebook.3.patch
```



---

Comment by iandrus created at 2010-12-29 13:18:20

Apply trac_693-spawn_notebook.3.patch


---

Comment by kcrisman created at 2011-01-11 04:11:36

I'd like to test #8473, which depends on this, but I'm reluctant to do so until someone who knows something about the notebook takes a look at this.  Bug days folks?


---

Comment by amog2011 created at 2011-03-15 16:37:10

Open browser if server running and open_viewer=True. pep8 clean-ups. Rebased for queue in comment. Replaces previous. 

 <a href="http://www.nicetick.com"><font color="#000000">air jordan</font></a>



---

Comment by kcrisman created at 2011-03-15 16:50:04

Replying to [comment:15 amog2011]:
> Open browser if server running and open_viewer=True. pep8 clean-ups. Rebased for queue in comment. Replaces previous. 
This is a spam comment. Can someone please remove this 'user'?  I don't know who has permissions for this.


---

Comment by jdemeyer created at 2011-03-16 11:19:28

Replying to [comment:16 kcrisman]:
> Replying to [comment:15 amog2011]:
> > Open browser if server running and open_viewer=True. pep8 clean-ups. Rebased for queue in comment. Replaces previous. 
> This is a spam comment. Can someone please remove this 'user'?  I don't know who has permissions for this.

Minh has.


---

Comment by mvngu created at 2011-03-16 11:28:34

Replying to [comment:16 kcrisman]:
> This is a spam comment. Can someone please remove this 'user'?  I don't know who has permissions for this.

amog2011 is already banned.


---

Comment by iandrus created at 2011-03-24 21:45:27

Changing status from needs_review to positive_review.


---

Comment by iandrus created at 2011-03-24 21:45:27

I have been using this (with #8473) for some time without problems.  I have also reviewed the code and it looks okay given my limited understanding of the notebook.


---

Comment by kcrisman created at 2011-03-25 00:46:37

Replying to [comment:19 iandrus]:
> I have been using this (with #8473) for some time without problems.  I have also reviewed the code and it looks okay given my limited understanding of the notebook.

Thanks.  It applies just as cleanly (one hunk misses with fuzz) to current SageNB as in the comment above.  This could be added in a new spkg with the Jmol updates.

Apply [attachment:trac_693-spawn_notebook.3.patch]


---

Comment by jdemeyer created at 2011-03-28 07:17:55

Resolution: fixed
