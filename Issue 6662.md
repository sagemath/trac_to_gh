# Issue 6662: [with patch, needs review] sampling from a general discrete probability distribution

Issue created by migration from Trac.

Original creator: carlohamalainen

Original creation time: 2009-07-31 14:32:08

Assignee: mhampton

CC:  kohel

This patch exposes the general discrete distribution code in the Gnu Scientific Library (GSL). It provides a fast way to sample from a user-defined discrete probability distribution, and it also extends the DiscreteProbabilitySpace class by allowing sampling from the defined distribution.


---

Comment by carlohamalainen created at 2009-07-31 14:35:20

Why is the reference manual formatting broken? After doing "sage -docbuild reference html" the examples in the entry "Interface to gsl discrete random variable generator" in Probability have examples that are not formatted. Why? What's going wrong with the docstring formatting in my pyx file?


---

Attachment


---

Comment by carlohamalainen created at 2009-07-31 17:32:34

Fixed the docstring formatting.


---

Comment by wdj created at 2009-08-02 02:13:43

I can try to test this, but I'm wondering how (for example) do I generate a list of 10 numbers in (0.1,2.3) randomly having the normal distribution with mean 1 and standard deviation 2? (Similar question for other common distributions.)


---

Comment by wdj created at 2009-08-02 10:24:12

This patch installs fine with 4.1.1.a1 on an amd64 machine running ubuntu 9.04. It passes sage -testall, except for the known failures.

I'm a little concerned about the docstrings. If I were more of a probability expert maybe this would not be an issue but not being an expert (which maybe is a good thing?) I don't see how to use it to do some basic sampling which might be useful for teaching a first course in probability.


---

Comment by carlohamalainen created at 2009-08-06 17:32:35

I only wrote an interface to one particular discrete distribution in gsl. I'll add stuff for normal distribution, binomial, etc later this month (travelling and no time to do Sage).


---

Comment by mvngu created at 2009-09-09 10:40:18

Closing this as a duplicate of #6662.


---

Comment by mvngu created at 2009-09-09 10:40:18

Resolution: duplicate


---

Comment by kcrisman created at 2011-06-15 18:37:32

You mean #6827!  That wasted 20 minutes for me, Minh.

 :)
