# Issue 8388: pickle the paths of Rauzy diagrams

Issue created by migration from Trac.

Original creator: vdelecroix

Original creation time: 2010-02-27 16:55:51

Assignee: vdelecroix

CC:  sage-combinat tmonteil

Keywords: pickle of a nested class

There is a pickle error with the nested class RauzyDiagram.Path in sage.combinat.iet.template


```
sage: p = iet.Permutation('a b c','c b a')
sage: r = p.rauzy_diagram()
sage: g = r.path(p, 't', 'b')
sage: dumps(g)
PicklingError Traceback(most recent call last)
...
PicklingError: Can't pickle <class 'sage.combinat.iet.labelled.Path'>: attribute lookup sage.combinat.iet.labelled.Path failed
```


A __metaclass__ must be defined for RauzyDiagram.


---

Comment by vdelecroix created at 2010-02-27 17:00:17

Changing keywords from "pickle of a nested class" to "pickle,  nested class".


---

Comment by hivert created at 2010-02-27 18:31:45

Replying to [comment:1 vdelecroix]:
Do you want it to be reviewed (you didn't check need review). I'm volunteering to review it as soon as #8386 is reviewed.


---

Comment by vdelecroix created at 2010-02-27 22:28:50

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2010-02-27 22:28:50

Changing component from algebra to combinatorics.


---

Comment by chapoton created at 2011-06-11 20:29:38

please add a commit message to your patch (using sage -hg qrefresh -e) starting with #8388 (to make the bot more happy)


---

Comment by chapoton created at 2011-06-11 21:08:22

Does it really depends on #8386 ? The buildbot was happier before I added this dependency.


---

Comment by ncohen created at 2011-10-01 15:10:27

Hellooo !!!!

This ticket can be set to positive review after two changes :

    * That it be rebased against a recent version of Sage. The patch applies with a hunk right now
    * That the commit message be changed so as to contain the ticket's number, or the release manager will have to shout `:-D` 

Nathann


---

Comment by ncohen created at 2011-10-01 15:10:27

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2011-10-01 15:11:14

Oh, and let me just add that I was glad to review this ticket : I had to learn what a metaclass was. Great explanation there :

http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python

Nathann


---

Attachment

Depends on ticket 8386.


---

Comment by vdelecroix created at 2012-04-29 19:44:47

The test error was due to 8386.


---

Comment by vdelecroix created at 2012-04-29 19:44:47

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2012-07-27 20:42:43

Please fill in your real name as Author.


---

Comment by chapoton created at 2012-08-29 19:42:47

apply trac_8388_pickling_path.patch


---

Comment by chapoton created at 2012-08-29 19:52:05

apply trac_8388_pickling_path.v2.patch


---

Comment by chapoton created at 2013-05-23 20:15:56

apply trac_8388_pickling_path.v2.patch


---

Attachment


---

Comment by chapoton created at 2013-08-29 11:12:45

apply trac_8388_pickling_path.v2.patch


---

Comment by chapoton created at 2013-09-15 14:52:38

ok, good enough for me


---

Comment by chapoton created at 2013-09-15 14:52:38

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-10-07 06:49:17

Resolution: fixed
