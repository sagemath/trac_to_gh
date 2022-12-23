# Issue 3017: invalid link after make install

Issue created by migration from https://trac.sagemath.org/ticket/3017

Original creator: zimmerma

Original creation time: 2008-04-24 12:54:29

Assignee: mabshoff

An invalid link is present in sage 3.0 (after make install):

```
[root@achille local]# ls -l ./sage-3.0/sage/local/lib/python2.5/site-packages/polybori/polybori
lrwxrwxrwx 1 zimmerma cacao 39 2008-04-24 14:43 ./sage-3.0/sage/local/lib/python2.5/site-packages/polybori/polybori -> ../../../share/polybori/pyroot/polybori
```



---

Comment by mabshoff created at 2008-04-26 05:10:40

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-26 05:10:40

This link is actually pointing to hyperspace *before* make install and due to our spkg-install. It is easy to fix, so I am on it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-26 05:30:26

The updated spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.1/alpha0/polybori-0.3.1.p2.spkg

fixes the issue.

Cheers,

Michael


---

Comment by mhansen created at 2008-04-26 06:48:48

Looks good to me.


---

Comment by mabshoff created at 2008-04-26 06:49:59

Merged in Sage 3.0.1.alpha0


---

Comment by mabshoff created at 2008-04-26 06:49:59

Resolution: fixed
