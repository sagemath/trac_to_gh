# Issue 7893: Sage server launching script

Issue created by migration from https://trac.sagemath.org/ticket/7893

Original creator: klee

Original creation time: 2010-01-11 01:53:51

Assignee: tbd

Many users seem to write individually scripts starting and stop a Sage server. It would be good that there is a place where these efforts can be combined.


---

Comment by klee created at 2010-01-11 01:56:11

Changing assignee from tbd to klee.


---

Comment by klee created at 2010-01-11 02:00:14

Anybody is welcome to upload an improved version of the script!


---

Comment by klee created at 2010-10-15 05:39:36

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

Comment by jdemeyer created at 2010-10-15 07:26:15

Using "screen" is not very portable, so I would avoid that.


---

Comment by jdemeyer created at 2010-10-15 07:27:12

Typo: twist.pid -> twistd.pid


---

Comment by klee created at 2010-10-15 09:09:28

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

Comment by cschwan created at 2010-10-16 10:47:39

Look at http://trac.sagemath.org/sage_trac/ticket/381 for a similar effort. On Gentoo I automatically start the Notebook with a runscript - I find it very useful because the only thing I have to do is to open a browser and type in the Notebook's address. It is also possible to access the server from a different PC. To make it a more secure it is run as a different user.

I just added a patch which lets one specify the location of twistd's PID file: http://trac.sagemath.org/sage_trac/ticket/10131 - this might be of interest.


---

Attachment

Runscript starting the Notebook server on Gentoo


---

Comment by cschwan created at 2010-10-16 10:52:45

It should be easy to port the runscript e.g. to debian - as far as I know Debian also has runscript/start-stop-daemon.


---

Comment by leif created at 2012-12-02 16:01:37

Ping.  Shouldn't something like this get shipped with Sage?

Also, the Sage Installation Guide lacks this topic.  (There's a reference from the online FAQ to #381 though.)


---

Comment by leif created at 2012-12-02 16:11:52

Changing keywords from "" to "service daemon mode background".


---

Comment by klee created at 2012-12-03 01:30:27

revised for Sage 5.4; removed "upgrade" command


---

Attachment

revised for Sage 5.4; removed "upgrade" command


---

Comment by klee created at 2016-03-23 04:44:18

Changing status from new to needs_review.


---

Comment by klee created at 2016-03-23 04:44:18

Nowadays the goal of the script can be achieved easily on the OS level using tools such as Upstart in Ubuntu. Even I, the writer of the scipt, ceased using it long time ago.


---

Comment by chapoton created at 2016-05-22 20:18:16

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2016-05-22 20:18:16

ok, then let us close that.


---

Comment by vbraun created at 2016-06-12 12:02:30

Resolution: fixed
