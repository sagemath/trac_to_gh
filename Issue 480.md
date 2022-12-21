# Issue 480: Make Sage work with SELinux on Linux

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-22 21:37:55

Assignee: mabshoff

CC:  was vbraun

Fedora Core 7 has SELinux turned on per default. Sage should support running when SELinux is activated. 

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-22 21:38:07

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-12-06 20:00:26

From http://www.ittvis.com/services/techtip.asp?ttid=3092:

```
To rectify this issue, you can either:

    * Change the default security context for IDL by issuing the command:

      chcon -t texrel_shlib_t /usr/local/rsi/idl_6.1/bin/bin.linux.x86/*.so
```


Cheers,

M ichael


---

Comment by mhansen created at 2007-12-24 06:27:21


```
On my CENTOS 5 system, I found the SELinux errors can be avoided by setting SELinux to "permissive" rather than "enforced."  "Disabled" was not necessary.  Lots of software seems to be affected by the new tighted SELinux settings, including Mathematica.
Thanks for your great work on SAGE!
```



---

Comment by mhansen created at 2012-05-28 07:15:34

Is this still valid?


---

Comment by mhansen created at 2012-05-28 07:15:44

Changing keywords from "" to "sd40.5".


---

Comment by mhansen created at 2012-05-28 07:15:44

Changing status from new to needs_info.


---

Comment by mhansen created at 2012-08-01 06:43:39

Changing status from needs_info to needs_review.


---

Comment by mhansen created at 2012-08-01 06:43:39

I think we can closed this as invalid since SELinux has been incorporated to the 2.6 kernel for quite awhile now.


---

Comment by mhansen created at 2012-08-01 06:44:34

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-08-01 12:23:55

Resolution: worksforme
