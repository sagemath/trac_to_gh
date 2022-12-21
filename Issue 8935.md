# Issue 8935: update README.txt to reflect support for Mac OS X 10.4.x

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-05-09 00:47:30

Assignee: mvngu

CC:  georgsweber kcrisman

As the subject says. This is a follow-up to #8841. See this [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/9b0ed0b58400cc18) thread for some background information.


---

Comment by mvngu created at 2010-05-09 00:49:39

updated README.txt based on Sage 4.4.1


---

Comment by mvngu created at 2010-05-09 00:51:17

Changing status from new to needs_review.


---

Attachment

Here's a diff between the README.txt in Sage 4.4.1 and the updated README.txt on this ticket:

```diff
[mvngu`@`sage sage-4.4.1-8917-magmas]$ diff -Naur README.txt.old README.txt.new 
--- README.txt.old	2010-05-08 17:40:09.761167033 -0700
+++ README.txt.new	2010-05-08 17:44:01.730958793 -0700
`@``@` -95,14 +95,13 `@``@`
   x86_64           64-bit Linux -- Debian, Ubuntu, CentOS (=Red Hat),
                                    Fedora, openSUSE, Mandriva, Arch
   IA-64 Itanium 2  64-bit Linux -- Red Hat, SUSE
-  x86              Apple Mac OS X 10.5.x, 10.6.x
-  PPC              Apple Mac OS X 10.5.x, 10.6.x
+  x86              Apple Mac OS X 10.4.x, 10.5.x, 10.6.x
+  PPC              Apple Mac OS X 10.4.x, 10.5.x, 10.6.x
   Sparc            Solaris 10
 
 Use Sage on Microsoft Windows via VMware.  Active work to port Sage to
 Cygwin (Windows) is in progress.
 
-NOTE: Sage-4.4 worked on OS X 10.4, but Sage-4.4.1 doesn't. 
 
 NOT OFFICIALLY SUPPORTED, BUT NEARLY WORKS
 ------------------------------------------
```



---

Comment by kcrisman created at 2010-05-09 01:08:21

Looks good.


---

Comment by kcrisman created at 2010-05-09 01:08:21

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-09 01:14:19

Resolution: fixed
