# Issue 9628: Live tutorial docs missing some equations

Issue created by migration from https://trac.sagemath.org/ticket/9628

Original creator: mikexstudios

Original creation time: 2010-07-28 21:07:39

Assignee: mvngu

Keywords: live, tutorial, documentation, missing

I didn't check every page, but on http://sagenb.org/doc/live/tutorial/tour_algebra.html in the Solving Differential Equations section, some of the mass-spring differential equations are not shown.

If you compare that same section to the static tutorial, you will see the typeset equations (as images): http://sagenb.org/doc/static/tutorial/tour_algebra.html

This same problem also happens in other sections on that page.


---

Comment by kcrisman created at 2014-11-20 16:21:03

This is apparently resolved (perhaps it was a pre-mathjax issue), but I think that there _is_ a very minor thing that in the live documentation the two equations in the system  somehow are typeset directly next to each other.

```

.. math::

    m_1 x_1'' + (k_1+k_2) x_1 - k_2 x_2 = 0

    m_2 x_2''+ k_2 (x_2-x_1) = 0,

```

somehow isn't rendering properly.


---

Comment by kcrisman created at 2014-11-20 16:21:03

Changing priority from minor to trivial.
