# Issue 7878: remove any spaces in output of testcc.sh and testcxx.sh

Issue created by migration from https://trac.sagemath.org/ticket/7878

Original creator: drkirkby

Original creation time: 2010-01-09 19:11:05

Assignee: GeorgSWeber

One of the scripts recently added to sage in ticket #7505 has an extra space in the output when the Sun compiler is used on Solaris. The revised version just used 'sed' to strip out any spaces. 

The problem was not see on the testcc.sh, but I thought it prudent to do do both scripts the same. 


---

Attachment


---

Comment by drkirkby created at 2010-01-10 02:22:36

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-11 20:26:00

## How to test
To test this patch you will need to have Sun Studio installed. 


```
$ local/bin/testcc.sh /opt/sunstudio12.1/bin/cc 
drkirkby@hawk:~/sage-4.3.1.alpha1$ local/bin/testcc.sh /opt/sunstudio12.1/bin/cc 
Sun_Studio
drkirkby@hawk:~/sage-4.3.1.alpha1$ local/bin/testcxx.sh /opt/sunstudio12.1/bin/CC 
Sun_Studio
drkirkby@hawk:~/sage-4.3.1.alpha1$ local/bin/testcxx.sh /opt/sunstudio12.1/bin/CC  | wc 
       1       1      12
drkirkby@hawk:~/sage-4.3.1.alpha1$ local/bin/testcc.sh /opt/sunstudio12.1/bin/cc | wc 
       1       1      11
```


Note how the current version of testcxx.sh outputs 12 characters, not 11. There is an extra space. With the attached patch, any spaces are removed, so the outputs from the two commands are identical. This is important if one wishes to test that the compilers are the same.


---

Comment by jsp created at 2010-01-27 22:47:54

Before:



```
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ local/bin/testcc.sh /opt/sunstudio12.1/bin/cc 
Sun_Studio
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ local/bin/testcxx.sh /opt/sunstudio12.1/bin/CC
Sun_Studio 
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ local/bin/testcxx.sh /opt/sunstudio12.1/bin/CC  | wc
      1       1      12
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ local/bin/testcc.sh /opt/sunstudio12.1/bin/cc | wc
      1       1      11

```


After the patch




```
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ local/bin/testcxx.sh /opt/sunstudio12.1/bin/CC  | wc
      1       1      11
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ local/bin/testcc.sh /opt/sunstudio12.1/bin/cc | wc 
      1       1      11

```



Works ok, so positive review

Jaap


---

Comment by jsp created at 2010-01-27 22:47:54

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-31 00:11:07

Merged [remove-spaces-7878.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7878/remove-spaces-7878.patch) in the base spkg repository. drkirkby: please remember to put the ticket number in your patches. Such information is very useful for tracking down bugs and the ticket in which they were introduced.


---

Comment by mvngu created at 2010-01-31 00:11:07

Resolution: fixed
