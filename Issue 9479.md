# Issue 9479: wrong license in readline SPKG.txt

Issue created by migration from https://trac.sagemath.org/ticket/9479

Original creator: zimmerma

Original creation time: 2010-07-12 12:30:20

Assignee: tbd

CC:  was drkirkby

Keywords: license

In sage 4.4.4, the file SPKG.txt says:

```
## License

 * GPL V2+
```

whereas src/COPYING says:

```
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007
```



---

Attachment

the attached spkg should fix that issue.

Paul


---

Comment by zimmerma created at 2013-08-23 14:39:23

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-08-26 19:08:57

Fixed by #14405 instead.


---

Comment by jdemeyer created at 2013-08-26 19:08:57

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-30 08:44:10

Resolution: duplicate
