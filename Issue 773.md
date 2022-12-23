# Issue 773: SAGE drops . from path

Issue created by migration from https://trac.sagemath.org/ticket/773

Original creator: was

Original creation time: 2007-10-01 19:05:57

Assignee: was


```
was@ubuntu:~/sd5/ant$ export PATH=.:$PATH
was@ubuntu:~/sd5/ant$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.5.1, Release Date: 2007-09-26                     |
| Type notebook() for the GUI, and license() for information.        |
os.ensage: os.environ['PATH']
'/home/was/s/local/polymake/bin/:/home/was/s:/home/was/s/local/bin:/home/was/s.dev:/usr/local/bin/:/home/was/bin:/home/was/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games'
```



---

Comment by cwitty created at 2007-12-11 02:48:03

I'm guessing this is caused by the following lines from expect.py...

```
# . in user's path causes *HUGE* trouble, e.g., pexpect will try to
# run a directory name!
p = os.environ['PATH'].split(':')
os.environ['PATH'] = ':'.join([v for v in p if v.strip() != '.'])
```


These lines were added by William Stein:

```
changeset:   2329:cccccf17fcd6
user:        William Stein <wstein@gmail.com>
date:        Thu Jan 11 14:10:46 2007 -0800
summary:     Make sure . is not in user's path.
```



---

Attachment


---

Comment by was created at 2009-01-23 10:15:13

The attached new spkg and deleting the code cwitty pointed out completely fixes this problem.


---

Comment by rlm created at 2009-01-24 14:56:31

Looks good.


---

Comment by mabshoff created at 2009-01-28 17:54:11

I did some further cleanups in SPKG.txt and also add .hgignore. The result is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha3/pexpect-2.0.p3.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 18:03:55

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 18:03:55

Resolution: fixed
