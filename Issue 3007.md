# Issue 3007: gap.Factorization? is useless

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-23 17:09:20

Assignee: was

See this thread.  The solution suggested by Steve Linton below does *not* work exactly as suggested.


```


Forwarded conversation
Subject: [sage-support] Documentation with several entries
------------------------

From: Hector Villafuerte <hectorvd`@`gmail.com>
Date: Tue, Apr 22, 2008 at 5:12 PM
To: sage-support`@`googlegroups.com



Hi,
while trying this:
sage: gap.Factorization?

I got this...

Type:        <class 'sage.interfaces.gap.GapFunction'>
Definition:  gap.Factorization( [noargspec] )
Docstring:
Help: several entries match this topic - type ?2 to get match [2]

[1] Reference: factorization
[2] Reference: Factorization


Which I can't get to work in either the Notebook or the command line. Any ideas?
Thanks!
--
 Hector

--~--~---------~--~----~------------~-------~--~----~
To post to this group, send email to sage-support`@`googlegroups.com
To unsubscribe from this group, send email to sage-support-unsubscribe`@`googlegroups.com
For more options, visit this group at http://groups.google.com/group/sage-support
URLs: http://www.sagemath.org
-~----------~----~----~----~------~----~------~--~---

----------
From: William Stein <wstein`@`gmail.com>
Date: Wed, Apr 23, 2008 at 7:42 AM
To: Steve Linton <sal`@`cs.st-and.ac.uk>


Any thoughts about how to disambiguate this sort of thing in the context
of Sage?  Of course, you can just plead that you work on the gap interface
almost 2.5 years ago and remember nothing :-)
--
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org
----------
From: Steve Linton <sal`@`cs.st-and.ac.uk>
Date: Wed, Apr 23, 2008 at 8:34 AM
To: William Stein <wstein`@`gmail.com>


gap.2? might just work.

You simply need to send GAP ?2 or HELP("2");

The message is being generated from HELP_SHOW_MATCHES in lib/helpbase.gi (line
713). I dare say we could move that message to a global variable so that you
could change it to  "type gap.2? ...." in a future release.

       Steve
--
Steve Linton    School of Computer Science  &
     Centre for Interdisciplinary Research in Computational Algebra
            University of St Andrews    Tel   +44 (1334) 463269
http://www.cs.st-and.ac.uk/~sal          Fax   +44 (1334) 463278
The University is a charity registered in Scotland : No SC013532



-- 
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org 
```



---

Comment by AlexGhitza created at 2009-01-23 02:42:37

Changing type from defect to enhancement.


---

Comment by iandrus created at 2012-06-05 18:47:46

The following works except that it's not properly offset, i.e. you have to hit space a few times before you find the documentation for `Factorization`.


```
sage: gap.Factorization?
Type:		GapFunction
Base Class:	<class 'sage.interfaces.gap.GapFunction'>
String Form:	Factorization
Namespace:	Interactive
Loaded File:	/Users/gvol/SageStuff/sage-5.0.rc0/local/lib/python2.7/site-packages/sage/interfaces/gap.py
Source File:	/Users/gvol/SageStuff/sage-5.0.rc0/devel/sage/sage/interfaces/gap.py
Definition:	gap.Factorization(self, *args, **kwds)
Docstring:
    Help: several entries match this topic - type ?2 to get match [2]
    
    [1] Reference: factorization
    [2] Reference: Factorization

Call def:	gap.Factorization(self, *args, **kwds)

Call docstring:
    x.__init__(...) initializes x; see help(type(x)) for signature


sage: gap."2"?
...the real documentation...
```



---

Comment by iandrus created at 2013-03-10 22:24:40

Changing status from new to needs_review.


---

Comment by iandrus created at 2013-03-10 22:24:40

This has been fixed in 5.7.


---

Comment by tscrim created at 2013-03-20 23:12:02

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-29 18:55:55

Resolution: worksforme
