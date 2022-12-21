# Issue 8385: Add hostname, date and time to test.log

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-02-26 23:35:43

Assignee: tbd

Currently, if one runs 


```
$ make test
```


a file


```
$HOME/.sage/tmp/test.log
```


is created with the results of the tests. However, this stops testing two versions of Sage at the same time - even if the tests take place on different machines. 

Hence it would be useful if the log file had the hostname, date and time in it. 

I would suggest a name like


```
test.log-redstart-23:22:57-02:26:2010
```


would be useful to indicate

 * The hostname was "redstart"
 * The time the tests started was "23:22:57"
 * The date the tests started was "02:26:2010"

This would allow multiple versions of Sage to be tested on multiple computers at the same time. 

Adding the Sage version would be nice too, as below for Sage 4.3.3


```
test.log-4.3.3-redstart-23:22:57-02:26:2010
```



Dave 



---

Comment by roed created at 2013-03-28 23:00:15

Changing component from doctest to doctest framework.


---

Comment by jdemeyer created at 2013-05-17 14:02:41

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-05-17 14:02:41

Given that the original problem (writing to `$HOME`) doesn't occur anymore, given that running `make (p)test(long)` twice in the same installation is unlikely and given that it's nice to have easy, predictable filenames for the logfiles, I propose to close this as invalid.


---

Comment by jdemeyer created at 2013-05-19 13:14:22

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-21 07:24:56

Resolution: invalid
