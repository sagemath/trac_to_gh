# Issue 8526: Missing usernames in trac emails

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2010-03-13 18:10:45

Assignee: schilly

CC:  hivert

In a number of emails I get from trac, I see lines like this:


```
Changes (by newvalueoldvalue): 
```


The `newvalueoldvalue` should instead be an actual username. I'm not sure if this is an actual trac bug or if it's something about our configuration. For this ticket, someone should figure that out, and either file a new bug, fix the trac configuration, or file a bug with trac itself (if that's where the issue is).

This came up on the following sage-devel thread: 

http://groups.google.com/group/sage-devel/browse_thread/thread/060f5430428fd945#


---

Comment by mmezzarobba created at 2014-03-04 15:52:27

Fixed a while ago.


---

Comment by mmezzarobba created at 2014-03-04 15:52:27

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-03-05 15:38:30

I got this on 4 march 2014:

```
#11840: sage.symbolic.expression.Expression.collect_common_factors has no
documentation
-------------------------------------+-------------------------------------
       Reporter:  mjo                |        Owner:  mvngu
           Type:  defect             |       Status:  needs_review
       Priority:  major              |    Milestone:  sage-6.2
      Component:  documentation      |   Resolution:
       Keywords:  symbolic,          |    Merged in:
  beginner                           |    Reviewers:
        Authors:  Frédéric Chapoton  |  Work issues:
Report Upstream:  N/A                |       Commit:
         Branch:  u/chapoton/11840   |  06d4fe0e2b1c40cbebd4f72ffd171ba9b2389db6
   Dependencies:                     |     Stopgaps:
-------------------------------------+-------------------------------------
Changes (by {'newvalue': u'Fr\xe9d\xe9ric Chapoton', 'oldvalue': ''}):

 * status:  new => needs_review
 * commit:   => 06d4fe0e2b1c40cbebd4f72ffd171ba9b2389db6
 * branch:   => u/chapoton/11840
 * author:   => Frédéric Chapoton


Comment:

 Here is a git branch with a little bit more documentation for this method.

 I have also taken the opportunity to put raise statement into python3
 format, and to use the trac role to add links to the tickets.
 ----
 New commits:
 ||[http://git.sagemath.org/sage.git/commit/?id=eeeb29316df0b8603bd73367fb6fd527c383692f
 eeeb293]||{{{trac #11840 first step, plus doc python 3 and trac role
 cleanup}}}||
 ||[http://git.sagemath.org/sage.git/commit/?id=06d4fe0e2b1c40cbebd4f72ffd171ba9b2389db6
 06d4fe0]||`trac #11840 details, making sure that tests pass`||

--
Ticket URL: <http://trac.sagemath.org/ticket/11840#comment:4>
Sage <http://www.sagemath.org>
Sage: Creating a Viable Open Source Alternative to Magma, Maple, Mathematica, and MATLAB
```



---

Comment by jdemeyer created at 2014-03-05 15:38:30

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2014-03-05 15:40:43

Also recently:

```
#15857: change the licenses of schemes/toric/points.py,
rings/number_field/splitting_field.py, libs/readline.pyx to GPLv2+ (from
GPLv3+)
-------------------------------------+-------------------------------------
       Reporter:  was                |        Owner:
           Type:  defect             |       Status:  positive_review
       Priority:  major              |    Milestone:  sage-6.2
      Component:  misc               |   Resolution:
       Keywords:                     |    Merged in:
        Authors:  Julian Rüth        |    Reviewers:  Jeroen Demeyer
Report Upstream:  N/A                |  Work issues:
         Branch:                     |       Commit:
  u/saraedum/ticket/15857            |  9566989f4aedf02479a125943e9c0570db0281e9
   Dependencies:                     |     Stopgaps:
-------------------------------------+-------------------------------------
Changes (by {'newvalue': u'Julian R\xfcth', 'oldvalue': ''}):

 * author:   => Julian Rüth


Comment:

 (sorry)

--
Ticket URL: <http://trac.sagemath.org/ticket/15857#comment:12>
Sage <http://www.sagemath.org>
Sage: Creating a Viable Open Source Alternative to Magma, Maple, Mathematica, and MATLAB
```



---

Comment by mkoeppe created at 2016-09-25 00:59:35

This ticket appears to be outdated and should be closed.


---

Comment by mkoeppe created at 2016-09-25 00:59:35

Changing status from needs_work to needs_review.


---

Comment by paulmasson created at 2016-09-25 01:32:07

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2017-01-21 18:03:11

Resolution: invalid
