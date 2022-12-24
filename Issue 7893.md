# Issue 7893: Sage server launching script

archive/issues_007893.json:
```json
{
    "body": "Assignee: tbd\n\nMany users seem to write individually scripts starting and stop a Sage server. It would be good that there is a place where these efforts can be combined.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7893\n\n",
    "created_at": "2010-01-11T01:53:51Z",
    "labels": [
        "packages: experimental",
        "trivial",
        "enhancement"
    ],
    "title": "Sage server launching script",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7893",
    "user": "klee"
}
```
Assignee: tbd

Many users seem to write individually scripts starting and stop a Sage server. It would be good that there is a place where these efforts can be combined.

Issue created by migration from https://trac.sagemath.org/ticket/7893





---

archive/issue_comments_068655.json:
```json
{
    "body": "Changing assignee from tbd to klee.",
    "created_at": "2010-01-11T01:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68655",
    "user": "klee"
}
```

Changing assignee from tbd to klee.



---

archive/issue_comments_068656.json:
```json
{
    "body": "Anybody is welcome to upload an improved version of the script!",
    "created_at": "2010-01-11T02:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68656",
    "user": "klee"
}
```

Anybody is welcome to upload an improved version of the script!



---

archive/issue_comments_068657.json:
```json
{
    "body": "I revised the script according Donald Alan Morrison's comments:\u00a0 \n\n1) The stop_server function does not do error checking to ensure that \n the pid contained in the pid file actually corresponds to a server \n process: [http://trac.sagemath.org/sage_trac/attachment/ticket/7893/sage-server](http://www.google.com/url?sa=D&q=http://trac.sagemath.org/sage_trac/attachment/ticket/7893/sage-server&usg=AFQjCNFolyoFiY1P1jjri5DIL9m7ZUsTrg) \n\n\n30 \u00a0 \u00a0 \u00a0def stop_server(): \n 31 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0try: \n 32 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0# if sage notebook server is running, \"twist.pid\" is \n created \n 33 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0file = open(os.environ!['HOME'] + '/.sage/ \n sage_notebook.sagenb/twistd.pid', 'r') \n 34 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0pid = file.readline() \n 35 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0file.close() \n 36 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0print \"Stopping sage server...\" \n 37 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0os.system('kill -INT ' + pid) \n 38 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0except IOError: \n 39 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0print \"No sage server running.\" \n\n\nGiven the frequency of reboots for most users, and the cost to the \n user of killing a random process, it would be good to error check \n against the actual running process name. \n\n\n2) It would be good to add some code that waits for SIG_TERM to \n complete, then optionally sends SIG_KILL. \u00a0One can't assume SIG_TERM \n will be handled correctly by the server, especially if it's in a bad \nstate. \n\n\n3) The script should verify the completion of !#2, then delete the pid \nfiles. \n\n\n-Don",
    "created_at": "2010-10-15T05:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68657",
    "user": "klee"
}
```

I revised the script according Donald Alan Morrison's comments:  

1) The stop_server function does not do error checking to ensure that 
 the pid contained in the pid file actually corresponds to a server 
 process: [http://trac.sagemath.org/sage_trac/attachment/ticket/7893/sage-server](http://www.google.com/url?sa=D&q=http://trac.sagemath.org/sage_trac/attachment/ticket/7893/sage-server&usg=AFQjCNFolyoFiY1P1jjri5DIL9m7ZUsTrg) 


30      def stop_server(): 
 31          try: 
 32              # if sage notebook server is running, "twist.pid" is 
 created 
 33              file = open(os.environ!['HOME'] + '/.sage/ 
 sage_notebook.sagenb/twistd.pid', 'r') 
 34              pid = file.readline() 
 35              file.close() 
 36              print "Stopping sage server..." 
 37              os.system('kill -INT ' + pid) 
 38          except IOError: 
 39              print "No sage server running." 


Given the frequency of reboots for most users, and the cost to the 
 user of killing a random process, it would be good to error check 
 against the actual running process name. 


2) It would be good to add some code that waits for SIG_TERM to 
 complete, then optionally sends SIG_KILL.  One can't assume SIG_TERM 
 will be handled correctly by the server, especially if it's in a bad 
state. 


3) The script should verify the completion of !#2, then delete the pid 
files. 


-Don



---

archive/issue_comments_068658.json:
```json
{
    "body": "Using \"screen\" is not very portable, so I would avoid that.",
    "created_at": "2010-10-15T07:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68658",
    "user": "jdemeyer"
}
```

Using "screen" is not very portable, so I would avoid that.



---

archive/issue_comments_068659.json:
```json
{
    "body": "Typo: twist.pid -> twistd.pid",
    "created_at": "2010-10-15T07:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68659",
    "user": "jdemeyer"
}
```

Typo: twist.pid -> twistd.pid



---

archive/issue_comments_068660.json:
```json
{
    "body": "Further revised according to the comment :\n\nLine 50 \"blocks\" (waits syncronously without checking status); also \n half of a second may not be long enough if all memory was used up and \n there was excessive paging in/out from the swap file. \u00a0One alternative \n method is to check for the existence of the pid file periodically for \n a longer period (possibly parameterized), and if it is deleted, \n recheck that the twistd process has indeed exited else send SIGKILL. \n\n\nOtherwise, good refactor. :-) \n\n\n-Don",
    "created_at": "2010-10-15T09:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68660",
    "user": "klee"
}
```

Further revised according to the comment :

Line 50 "blocks" (waits syncronously without checking status); also 
 half of a second may not be long enough if all memory was used up and 
 there was excessive paging in/out from the swap file.  One alternative 
 method is to check for the existence of the pid file periodically for 
 a longer period (possibly parameterized), and if it is deleted, 
 recheck that the twistd process has indeed exited else send SIGKILL. 


Otherwise, good refactor. :-) 


-Don



---

archive/issue_comments_068661.json:
```json
{
    "body": "Look at http://trac.sagemath.org/sage_trac/ticket/381 for a similar effort. On Gentoo I automatically start the Notebook with a runscript - I find it very useful because the only thing I have to do is to open a browser and type in the Notebook's address. It is also possible to access the server from a different PC. To make it a more secure it is run as a different user.\n\nI just added a patch which lets one specify the location of twistd's PID file: http://trac.sagemath.org/sage_trac/ticket/10131 - this might be of interest.",
    "created_at": "2010-10-16T10:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68661",
    "user": "cschwan"
}
```

Look at http://trac.sagemath.org/sage_trac/ticket/381 for a similar effort. On Gentoo I automatically start the Notebook with a runscript - I find it very useful because the only thing I have to do is to open a browser and type in the Notebook's address. It is also possible to access the server from a different PC. To make it a more secure it is run as a different user.

I just added a patch which lets one specify the location of twistd's PID file: http://trac.sagemath.org/sage_trac/ticket/10131 - this might be of interest.



---

archive/issue_comments_068662.json:
```json
{
    "body": "Attachment [sage-notebook-server](tarball://root/attachments/some-uuid/ticket7893/sage-notebook-server) by cschwan created at 2010-10-16 10:49:06\n\nRunscript starting the Notebook server on Gentoo",
    "created_at": "2010-10-16T10:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68662",
    "user": "cschwan"
}
```

Attachment [sage-notebook-server](tarball://root/attachments/some-uuid/ticket7893/sage-notebook-server) by cschwan created at 2010-10-16 10:49:06

Runscript starting the Notebook server on Gentoo



---

archive/issue_comments_068663.json:
```json
{
    "body": "It should be easy to port the runscript e.g. to debian - as far as I know Debian also has runscript/start-stop-daemon.",
    "created_at": "2010-10-16T10:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68663",
    "user": "cschwan"
}
```

It should be easy to port the runscript e.g. to debian - as far as I know Debian also has runscript/start-stop-daemon.



---

archive/issue_comments_068664.json:
```json
{
    "body": "Ping.  Shouldn't something like this get shipped with Sage?\n\nAlso, the Sage Installation Guide lacks this topic.  (There's a reference from the online FAQ to #381 though.)",
    "created_at": "2012-12-02T16:01:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68664",
    "user": "leif"
}
```

Ping.  Shouldn't something like this get shipped with Sage?

Also, the Sage Installation Guide lacks this topic.  (There's a reference from the online FAQ to #381 though.)



---

archive/issue_comments_068665.json:
```json
{
    "body": "Changing keywords from \"\" to \"service daemon mode background\".",
    "created_at": "2012-12-02T16:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68665",
    "user": "leif"
}
```

Changing keywords from "" to "service daemon mode background".



---

archive/issue_comments_068666.json:
```json
{
    "body": "revised for Sage 5.4; removed \"upgrade\" command",
    "created_at": "2012-12-03T01:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68666",
    "user": "klee"
}
```

revised for Sage 5.4; removed "upgrade" command



---

archive/issue_comments_068667.json:
```json
{
    "body": "Attachment [sage-server.zip](tarball://root/attachments/some-uuid/ticket7893/sage-server.zip) by klee created at 2012-12-03 01:30:53\n\nrevised for Sage 5.4; removed \"upgrade\" command",
    "created_at": "2012-12-03T01:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68667",
    "user": "klee"
}
```

Attachment [sage-server.zip](tarball://root/attachments/some-uuid/ticket7893/sage-server.zip) by klee created at 2012-12-03 01:30:53

revised for Sage 5.4; removed "upgrade" command



---

archive/issue_comments_068668.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-03-23T04:44:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68668",
    "user": "klee"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068669.json:
```json
{
    "body": "Nowadays the goal of the script can be achieved easily on the OS level using tools such as Upstart in Ubuntu. Even I, the writer of the scipt, ceased using it long time ago.",
    "created_at": "2016-03-23T04:44:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68669",
    "user": "klee"
}
```

Nowadays the goal of the script can be achieved easily on the OS level using tools such as Upstart in Ubuntu. Even I, the writer of the scipt, ceased using it long time ago.



---

archive/issue_comments_068670.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-05-22T20:18:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68670",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068671.json:
```json
{
    "body": "ok, then let us close that.",
    "created_at": "2016-05-22T20:18:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68671",
    "user": "chapoton"
}
```

ok, then let us close that.



---

archive/issue_comments_068672.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-06-12T12:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7893#issuecomment-68672",
    "user": "vbraun"
}
```

Resolution: fixed
