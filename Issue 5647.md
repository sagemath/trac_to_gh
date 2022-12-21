# Issue 5647: Random testing improvement (follow up to #5318)

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-03-31 03:14:10

Assignee: mabshoff

Improve #5318 to allow for the additional syntax:

  random_testing(tester, handle_iteration = True)

In that case, the wrapper function would handle all the iteration running boiler plate. When the seed is not specified by the caller, the boilerplate  could further set explicitly the seed in randstate.pyx to a random value at each iteration. Then, reproducing the bug would involve running a single iteration.

With a bit of magic one could allow for the following syntactic sugar

    `@`random_testing(handle_iteration = True)
    def tester(...):
        ...

Possible implementation: when random_testing receives only keyword arguments, without a function, it returns a copy of itself with partial specialization of those keyword arguments (using e.g. the upcoming default_keyword patch by Mike Hansen)


---

Comment by mderickx created at 2017-08-11 12:51:51

Changing component from doctest coverage to doctest framework.
