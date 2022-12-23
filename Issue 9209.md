# Issue 9209: Sage build can go wrong if there is a python install in /usr/local.

Issue created by migration from https://trac.sagemath.org/ticket/9209

Original creator: drkirkby

Original creation time: 2010-06-10 23:45:54

Assignee: GeorgSWeber

CC:  jason

There are at least two failed reports of Sage failing to build properly if there is an installation of python in /usr/local

 * http://groups.google.com/group/sage-solaris/browse_thread/thread/5dcc7ed68d279f67?hl=en
 * http://groups.google.com/group/sage-devel/browse_thread/thread/37a67ce63e68d55b?hl=en-GB

where an installation in /usr/local of python screw up Sage. 

In my own case, the only way I could find to stop the install in /usr/local preventing Sage building, was to execute as root


```
chmod 000 /usr/local/lib/libpython2.6.a /usr/local/lib/python2.6
```


Dave


---

Comment by drkirkby created at 2010-06-11 00:48:45

Changing assignee from GeorgSWeber to drkirkby.


---

Comment by drkirkby created at 2010-06-11 00:49:01

Remove assignee drkirkby.


---

Comment by drkirkby created at 2010-06-11 00:49:27

Set assignee to GeorgSWeber.


---

Comment by aapitzsch created at 2015-01-09 14:41:13

Does this still happen?


---

Comment by jdemeyer created at 2017-04-19 13:14:42

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2017-04-19 13:14:49

Changing status from needs_review to positive_review.


---

Comment by embray created at 2017-07-13 07:54:31

Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).


---

Comment by embray created at 2017-07-13 07:54:31

Resolution: wontfix
