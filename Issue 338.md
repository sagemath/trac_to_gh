# Issue 338: In doc browser make hyper links to referenced code in SAGE library

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2007-03-31 17:42:35

Assignee: boothby

For example:
On page http://sagenb.com/doc_browser?/const/?node72.html, reference to sage/modular/dims.py would be a hyper link to the actual code.
On page http://sagenb.com/doc_browser?/prog/?node15.html, reference to SAGE_ROOT/devel/sage/sage/graphs/graph.py would be a hyper link to the actual code.


---

Comment by TimothyClemans created at 2007-03-31 18:40:27

Changing assignee from boothby to TimothyClemans.


---

Comment by TimothyClemans created at 2007-03-31 18:40:27

Changing status from new to assigned.


---

Comment by kini created at 2012-06-23 09:18:57

The URLs in the ticket description don't exist.


---

Comment by kini created at 2012-06-23 09:18:57

Changing status from new to needs_info.


---

Comment by kcrisman created at 2013-01-29 20:48:29

This can be closed.  Keshav, I think this is WELL before you were aware of Sage - it dates from the days when there was no login process of any kind, if I'm not mistaken.  Ah, those were the days ;-)

Anyway, the real issue is that although within each piece of the Sage documentation it's easy to create hyperlinks, but not between different sets (e.g. the developer guide and the reference manual).  For instance, the first example is referring to [here](http://sagenb.org/doc/static/constructions/modular_forms.html?highlight=modular#genus-formulas).  But that has been discussed before, and this is too vague and outdated to be able to really doable.

Or what do you think?  Could this ticket be repurposed to the actual problem, and is that worthwhile?


---

Comment by chapoton created at 2018-04-17 07:44:31

Changing status from needs_info to positive_review.


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates
