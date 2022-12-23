# Issue 8840: about  CSRF attacks

Issue created by migration from https://trac.sagemath.org/ticket/8840

Original creator: aliajouz

Original creation time: 2010-05-02 00:17:50

Assignee: jason, was

CC:  chapoton

sage contain Multiple cross site reference vulnerability
because authority does not checked before preforming an action

*CSRF attacks explain:*
If create a file on my domain called "blah.jpg". It's really a php file, renamed.
The PHP file redirects you back to the referring host (or any host I want to really), to a special URL.
That URL takes an action based on the submitted data.
I then use an img  tag <img> to link to my "image" on your site.

When you view the page, your browser makes a request to that image, and that request is then redirected to the page on your site. Your browser won't display the image (or will display a broken image) but that's not important. What's important is that you just executed an action without knowing it.

Some examples of  CSRF attacks in sage :

1) upload a worksheet
2) create worksheet
3) change email 
4) .............
...........
.............
...........


*example:*
1- login in at
http://alpha.sagenb.org/

2- open this published worksheet
http://alpha.sagenb.org/home/pub/16/

3-go to your home you will see that I uploaded a worksheet to your account .





---

Comment by aliajouz created at 2010-05-02 00:18:28

Changing assignee from jason, was to aliajouz.


---

Comment by kcrisman created at 2014-12-19 04:43:26

This is probably a big reason why public worksheets are currently disabled...

https://github.com/sagemath/sagenb/issues/319


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by chapoton created at 2020-09-08 17:59:48

Resolution: invalid
