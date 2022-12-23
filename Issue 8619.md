# Issue 8619: add check for SELinux to sage prereq script

Issue created by migration from https://trac.sagemath.org/ticket/8619

Original creator: was

Original creation time: 2010-03-28 19:09:54

Assignee: GeorgSWeber


```
SELINUX
--------

On Linux, if you get this error message:

    " restore segment prot after reloc: Permission denied "

the problem is probably related to SELinux. See the following URL for
further information:

```


    http://www.ittvis.com/services/techtip.asp?ttid=3092

It would be better if the prereq script when sage first builds were to check for selinux.   This could be done possibly following the above link which says to look at /etc/sysconfig/selinux.  

There are some relevant emails in late March 2010 from John Bussoletti in sage-support about this.


---

Comment by was created at 2010-03-29 04:12:07


```
The command "sestatus" returns the following text on my system:
       SELinux Status:                 enabled
       SELinuxfs mount:                /selinux
       Current mode:                   permissive
       Mode from config file:          permissive
       Policy version:                 24
       Policy from config file:                targeted

So it seems that if you grep for "Current mode" and find either "disabled"
or "permissive", sage should build, but if you encounter "enabled" then it
may fail to build those apps that make the stack executable.

On my system sestatus is in /usr/sbin.

John Bussoletti
```



---

Comment by jdemeyer created at 2013-12-29 11:22:11

Given that I have never seen any complaints about SELinux (and the solution seems to be to compile with `-fPIC` which we already do), this can be closed as "worksforme".


---

Comment by jdemeyer created at 2013-12-29 11:23:31

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-12-29 11:23:39

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-04 02:37:19

Resolution: worksforme
