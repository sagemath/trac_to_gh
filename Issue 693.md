# Issue 693: Script to spawn a browser / start notebook.

archive/issues_000693.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein @qed777 @wjp acleone @mwhansen @jdemeyer mvngu\n\nI've had an icon sitting on my desktop for about a week now.  When I click on it, and it starts a notebook in a background terminal and spawns a browser.  I'd like to be able to click it a second time, and open another browser window, instead of the current behavior of attempting to start another notebook.\n\nShould work something like this:\n\n\n```\nif not notebook_is_running:\n    notebook(settings from commandline, open_browser=True)\nelse:\n    open_browser(settings from commandline)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/693\n\n",
    "created_at": "2007-09-19T17:39:28Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "Script to spawn a browser / start notebook.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/693",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: boothby

CC:  @williamstein @qed777 @wjp acleone @mwhansen @jdemeyer mvngu

I've had an icon sitting on my desktop for about a week now.  When I click on it, and it starts a notebook in a background terminal and spawns a browser.  I'd like to be able to click it a second time, and open another browser window, instead of the current behavior of attempting to start another notebook.

Should work something like this:


```
if not notebook_is_running:
    notebook(settings from commandline, open_browser=True)
else:
    open_browser(settings from commandline)
```


Issue created by migration from https://trac.sagemath.org/ticket/693





---

archive/issue_comments_003588.json:
```json
{
    "body": "Modifies `sage -notebook` to launch a browser window if the notebook is already started. Also adds a `sage -nb` shortcut.",
    "created_at": "2009-11-15T15:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3588",
    "user": "https://github.com/TimDumol"
}
```

Modifies `sage -notebook` to launch a browser window if the notebook is already started. Also adds a `sage -nb` shortcut.



---

archive/issue_comments_003589.json:
```json
{
    "body": "Attachment [trac_693-spawn-browser-start-nb.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn-browser-start-nb.patch) by @TimDumol created at 2009-11-15 15:35:46\n\nThis patch should do the trick. Apply to scripts repository.",
    "created_at": "2009-11-15T15:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3589",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_693-spawn-browser-start-nb.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn-browser-start-nb.patch) by @TimDumol created at 2009-11-15 15:35:46

This patch should do the trick. Apply to scripts repository.



---

archive/issue_comments_003590.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-15T15:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3590",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_003591.json:
```json
{
    "body": "Attachment [trac_693-spawn-browser-start-nb.2.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn-browser-start-nb.2.patch) by @TimDumol created at 2009-11-18 13:33:02\n\nChecks if the notebook server is running too, instead of just checking if the PID exists.",
    "created_at": "2009-11-18T13:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3591",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_693-spawn-browser-start-nb.2.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn-browser-start-nb.2.patch) by @TimDumol created at 2009-11-18 13:33:02

Checks if the notebook server is running too, instead of just checking if the PID exists.



---

archive/issue_comments_003592.json:
```json
{
    "body": "I am not sure which method is preferrable, since checking if the notebook server is running does not work if the user has no permission to read `/proc` and to send signals. Please feel free to approve of either patch.",
    "created_at": "2009-11-18T13:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3592",
    "user": "https://github.com/TimDumol"
}
```

I am not sure which method is preferrable, since checking if the notebook server is running does not work if the user has no permission to read `/proc` and to send signals. Please feel free to approve of either patch.



---

archive/issue_comments_003593.json:
```json
{
    "body": "Attachment [trac_693-spawn-browser-start-nb.3.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn-browser-start-nb.3.patch) by @TimDumol created at 2009-11-19 19:31:59\n\nFixes bug with arguments.",
    "created_at": "2009-11-19T19:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3593",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_693-spawn-browser-start-nb.3.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn-browser-start-nb.3.patch) by @TimDumol created at 2009-11-19 19:31:59

Fixes bug with arguments.



---

archive/issue_comments_003594.json:
```json
{
    "body": "Attachment [trac_693-spawn-browser-start-nb.4.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn-browser-start-nb.4.patch) by @TimDumol created at 2009-11-19 19:33:52\n\nSame thing, without actually checking if the Twistd process is running",
    "created_at": "2009-11-19T19:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3594",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_693-spawn-browser-start-nb.4.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn-browser-start-nb.4.patch) by @TimDumol created at 2009-11-19 19:33:52

Same thing, without actually checking if the Twistd process is running



---

archive/issue_comments_003595.json:
```json
{
    "body": "I don't get it.  If I do\n\n```\n$  sage -notebook directory=foo port=8001 & \n$  sage -notebook directory=bar port=8002 \n```\n\nthen when I execute the second line it might just pop up a notebook server pointed at port 8001.   Actually, given the line:\n\n```\ncmd = \"notebook(\" + \",\".join([wrap(v) for v in sys.argv[1:]]) + \",port=\" + SAGENB_PORT + \")\"\n```\n\nI think it would give an error, since port= is specified twice. \n\nThis is because you introduced a new environment variable SAGENB_PORT which isn't documented.  I don't know why it is there.  I think you should get the port from the port= option on the command line.\n\nI think you should get port= from the command line and get rid of the SAGENB_PORT environment variable. \n\nAlso, you use:\n\n```\nDOT_SAGENB = os.environ.get('DOT_SAGENB', os.path.join(os.environ['HOME'], '.sage', 'sage_notebook.sagenb'))\n```\n\nbut actually, you need to use the file `os.path.join(D, 'twistd.pid')` where D is the option specified in directory= in the command line.\n\nFinally, I think this code should be in the notebook(...) command in Sage itself.  It's wrong putting it here in this shell script, because it only half way fixes the problem.  E.g., imagine a user that types the following and leaves that in a console:\n\n```\nsage: notebook()\n```\n\n\nThen in another console, they type\n\n```\nsage: notebook()\n```\n\nInstead of giving an error, it should just given them the notebook.\nIf you put this code that you've just written in the notebook command, then both problems are automatically solved, whereas with the current code location, only half the problem is really solved.\n\nAlso, there is a notebook(fork=True) option, so one can do\n\n\n```\nsage: notebook(fork=True)\nThe notebook files are stored in: sage_notebook.sagenb\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:8001 *\n*                                                *\n**************************************************\n<pexpect.spawn instance at 0x10bb78bd8>\nsage: notebook()\n# get some notebook\n```\n\n\n\n\n\nWilliam",
    "created_at": "2009-11-19T21:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3595",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_003596.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-19T21:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3596",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_003597.json:
```json
{
    "body": "Attachment [trac_693-spawn-nb.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn-nb.patch) by @TimDumol created at 2009-11-21 01:33:39\n\nChanges run_notebook.py to launch a browser to the notebook page should an instance in the directory exist. Apply to sagenb repo. Apply this patch only.",
    "created_at": "2009-11-21T01:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3597",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_693-spawn-nb.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn-nb.patch) by @TimDumol created at 2009-11-21 01:33:39

Changes run_notebook.py to launch a browser to the notebook page should an instance in the directory exist. Apply to sagenb repo. Apply this patch only.



---

archive/issue_comments_003598.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-21T01:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3598",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_003599.json:
```json
{
    "body": "All your points make sense. I have implemented the changes in `run_notebook.py`. I've decided to check if the process is running, since that's also what `twistd` does.",
    "created_at": "2009-11-21T01:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3599",
    "user": "https://github.com/TimDumol"
}
```

All your points make sense. I have implemented the changes in `run_notebook.py`. I've decided to check if the process is running, since that's also what `twistd` does.



---

archive/issue_comments_003600.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-08T17:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3600",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_003601.json:
```json
{
    "body": "On OS X this doesn't work at all.  Depending on what I do either I get two notebook servers running simultaneously on the same directory (bad), or I get \"Another twistd server is running, PID 40940\".\n\nOn OS X there is no /proc filesystem.  However, when I run this code from this patch:\n\n```\n        try:\n            print 1\n            # First check using /proc directory\n            if os.path.exists('/proc/%d'  % twistd_pid):\n                launch_browser_to_nb()\n                return\n            else:\n                remove_pidfile(twistd_pid_path)                \n        except:\n            print 2\n```\n\nI don't see \"2\" printed, i.e., no exception is raised.   That's clear if you read the code -- you don't raise an exception.",
    "created_at": "2009-12-08T17:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3601",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_003602.json:
```json
{
    "body": "Attachment [trac_693-spawn-nb.2.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn-nb.2.patch) by @TimDumol created at 2009-12-09 12:10:35\n\nUses signals only to check if the process exists (as Twisted does)",
    "created_at": "2009-12-09T12:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3602",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_693-spawn-nb.2.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn-nb.2.patch) by @TimDumol created at 2009-12-09 12:10:35

Uses signals only to check if the process exists (as Twisted does)



---

archive/issue_comments_003603.json:
```json
{
    "body": "I have removed the /proc check, since it's what Twisted does anyways.",
    "created_at": "2009-12-09T12:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3603",
    "user": "https://github.com/TimDumol"
}
```

I have removed the /proc check, since it's what Twisted does anyways.



---

archive/issue_comments_003604.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-09T12:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3604",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_003605.json:
```json
{
    "body": "I guess we need to update the patch to take advantage of #2779?",
    "created_at": "2010-01-20T06:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3605",
    "user": "https://github.com/qed777"
}
```

I guess we need to update the patch to take advantage of #2779?



---

archive/issue_comments_003606.json:
```json
{
    "body": "Open browser if server running and `open_viewer=True`.  pep8 clean-ups.  Rebased for queue in comment.  Replaces previous.",
    "created_at": "2010-01-25T06:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3606",
    "user": "https://github.com/qed777"
}
```

Open browser if server running and `open_viewer=True`.  pep8 clean-ups.  Rebased for queue in comment.  Replaces previous.



---

archive/issue_comments_003607.json:
```json
{
    "body": "Attachment [trac_693-spawn_notebook.3.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn_notebook.3.patch) by @qed777 created at 2010-01-25 06:34:48\n\nV3:\n\n* If a server is running and `open_viewer=True`, get the settings from the old `twistedconf.tac` and browse to the server's home page.\n* Use `return` instead of `sys.exit`, in case of command-line invocation.\n* Some [pep8](http://pypi.python.org/pypi/pep8/) changes.\n* Rebased for this queue\n\n```\nsagenb-0.7 / #8051\ntrac_7784-hgignore_update.2.patch\ntrac_5712-interrupt-notification.6.patch\ntrac_6069-missing_pub_ws.2.patch\ntrac_8038-email_plus_addressing_v2.patch\ntrac_7506-notebook_object-documentation.2.patch\ntrac_693-spawn_notebook.3.patch\n```\n",
    "created_at": "2010-01-25T06:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3607",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_693-spawn_notebook.3.patch](tarball://root/attachments/some-uuid/ticket693/trac_693-spawn_notebook.3.patch) by @qed777 created at 2010-01-25 06:34:48

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

archive/issue_comments_003608.json:
```json
{
    "body": "* I think #8473 is related.\n  * V3 applies almost cleanly to SageNB 0.8:\n\n```\napplying trac_693-spawn_notebook.3.patch\npatching file sagenb/notebook/run_notebook.py\nHunk #12 succeeded at 434 with fuzz 2 (offset 3 lines).\nnow at: trac_693-spawn_notebook.3.patch\n```\n",
    "created_at": "2010-06-10T07:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3608",
    "user": "https://github.com/qed777"
}
```

* I think #8473 is related.
  * V3 applies almost cleanly to SageNB 0.8:

```
applying trac_693-spawn_notebook.3.patch
patching file sagenb/notebook/run_notebook.py
Hunk #12 succeeded at 434 with fuzz 2 (offset 3 lines).
now at: trac_693-spawn_notebook.3.patch
```




---

archive/issue_comments_003609.json:
```json
{
    "body": "Apply trac_693-spawn_notebook.3.patch",
    "created_at": "2010-12-29T13:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3609",
    "user": "https://github.com/gvol"
}
```

Apply trac_693-spawn_notebook.3.patch



---

archive/issue_comments_003610.json:
```json
{
    "body": "I'd like to test #8473, which depends on this, but I'm reluctant to do so until someone who knows something about the notebook takes a look at this.  Bug days folks?",
    "created_at": "2011-01-11T04:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3610",
    "user": "https://github.com/kcrisman"
}
```

I'd like to test #8473, which depends on this, but I'm reluctant to do so until someone who knows something about the notebook takes a look at this.  Bug days folks?



---

archive/issue_comments_003611.json:
```json
{
    "body": "Open browser if server running and open_viewer=True. pep8 clean-ups. Rebased for queue in comment. Replaces previous. \n\n <a href=\"http://www.nicetick.com\"><font color=\"#000000\">air jordan</font></a>\n",
    "created_at": "2011-03-15T16:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3611",
    "user": "https://trac.sagemath.org/admin/accounts/users/amog2011"
}
```

Open browser if server running and open_viewer=True. pep8 clean-ups. Rebased for queue in comment. Replaces previous. 

 <a href="http://www.nicetick.com"><font color="#000000">air jordan</font></a>




---

archive/issue_comments_003612.json:
```json
{
    "body": "Replying to [comment:15 amog2011]:\n> Open browser if server running and open_viewer=True. pep8 clean-ups. Rebased for queue in comment. Replaces previous. \nThis is a spam comment. Can someone please remove this 'user'?  I don't know who has permissions for this.",
    "created_at": "2011-03-15T16:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3612",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:15 amog2011]:
> Open browser if server running and open_viewer=True. pep8 clean-ups. Rebased for queue in comment. Replaces previous. 
This is a spam comment. Can someone please remove this 'user'?  I don't know who has permissions for this.



---

archive/issue_comments_003613.json:
```json
{
    "body": "Replying to [comment:16 kcrisman]:\n> Replying to [comment:15 amog2011]:\n> > Open browser if server running and open_viewer=True. pep8 clean-ups. Rebased for queue in comment. Replaces previous. \n> This is a spam comment. Can someone please remove this 'user'?  I don't know who has permissions for this.\n\nMinh has.",
    "created_at": "2011-03-16T11:19:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3613",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:16 kcrisman]:
> Replying to [comment:15 amog2011]:
> > Open browser if server running and open_viewer=True. pep8 clean-ups. Rebased for queue in comment. Replaces previous. 
> This is a spam comment. Can someone please remove this 'user'?  I don't know who has permissions for this.

Minh has.



---

archive/issue_comments_003614.json:
```json
{
    "body": "Replying to [comment:16 kcrisman]:\n> This is a spam comment. Can someone please remove this 'user'?  I don't know who has permissions for this.\n\namog2011 is already banned.",
    "created_at": "2011-03-16T11:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3614",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:16 kcrisman]:
> This is a spam comment. Can someone please remove this 'user'?  I don't know who has permissions for this.

amog2011 is already banned.



---

archive/issue_comments_003615.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-24T21:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3615",
    "user": "https://github.com/gvol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_003616.json:
```json
{
    "body": "I have been using this (with #8473) for some time without problems.  I have also reviewed the code and it looks okay given my limited understanding of the notebook.",
    "created_at": "2011-03-24T21:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3616",
    "user": "https://github.com/gvol"
}
```

I have been using this (with #8473) for some time without problems.  I have also reviewed the code and it looks okay given my limited understanding of the notebook.



---

archive/issue_comments_003617.json:
```json
{
    "body": "Replying to [comment:19 iandrus]:\n> I have been using this (with #8473) for some time without problems.  I have also reviewed the code and it looks okay given my limited understanding of the notebook.\n\nThanks.  It applies just as cleanly (one hunk misses with fuzz) to current SageNB as in the comment above.  This could be added in a new spkg with the Jmol updates.\n\nApply [attachment:trac_693-spawn_notebook.3.patch]",
    "created_at": "2011-03-25T00:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3617",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:19 iandrus]:
> I have been using this (with #8473) for some time without problems.  I have also reviewed the code and it looks okay given my limited understanding of the notebook.

Thanks.  It applies just as cleanly (one hunk misses with fuzz) to current SageNB as in the comment above.  This could be added in a new spkg with the Jmol updates.

Apply [attachment:trac_693-spawn_notebook.3.patch]



---

archive/issue_comments_003618.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-28T07:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/693#issuecomment-3618",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_000759.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-03-28T07:17:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/693",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/693#event-759"
}
```
