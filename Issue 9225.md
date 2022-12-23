# Issue 9225: Indicate progress and elapsed time when running multiple doctests

Issue created by migration from https://trac.sagemath.org/ticket/9225

Original creator: mpatel

Original creation time: 2010-06-12 10:18:49

Assignee: mvngu

CC:  wjp leif rbeezer

When we doctest several files in parallel or in sequence, it might be helpful to print stats relating to the test suite's progress, e.g.,

```sh
$ sage -t monoids/
sage -t  "monoids/monoid.py"
 1/10    1.9 s / 1.9 s
sage -t  "monoids/free_monoid.py"
 2/10    2.0 s / 3.9 s
[...]
```

What other columns would be useful?  Coverage?


---

Comment by mpatel created at 2010-07-07 06:47:40

If we widen the scope here a bit:  We should use [optparse](http://docs.python.org/library/optparse.html), at least, to handle command-line arguments.


---

Comment by mpatel created at 2010-07-09 00:33:19

Changing priority from minor to major.


---

Comment by mpatel created at 2010-07-09 00:33:19

Other possibilities, probably mentioned before and probably for other tickets:

 * "Librarify:" Make it possible to doctest files and objects from the Sage command-line or notebook, e.g.,

```python
sage: doctest('file.sage', long=True, optional=['axiom', 'magma'])
sage: doctest(os.path.join(SAGE_ROOT, 'devel', 'sage', 'sage', 'monoids'), processes=4)
sage: stats = {}     # Collect errors, counts, timings, etc.
sage: doctest(['foo.py', 'bar.pyx'], stats=stats)
sage: def f():
....:     """
....:     sage: f()
....:     1
....:     """
....:     return 1
....: 
sage: doctest(f)
```


 * Doctest the doctesting framework!  I think we could include [comment:ticket:9449:13 this example], at least.

 * An option to run an individual `file.py`'s "examples" (i.e., the files `example_*` functions) in parallel.


---

Comment by mpatel created at 2010-07-15 07:23:14

A way to upload anonymized test stats and system information to a remote server?


---

Comment by mpatel created at 2010-08-08 08:44:35

Also potentially useful: doctesting the same file multiple times in parallel.  I think this is just a matter of generating in `sage-doctest` a unique name, e.g., `.doctest_foo-R3X87S.py` for each run on `foo.py`.


---

Comment by drkirkby created at 2010-08-27 11:46:37

I have a suspicion that some doctests fail when the system is under heavy load. It would be good if the one-minute and perhaps 5 minute load average could be recorded with any failures, along with the dates and time as I mentioned before.


---

Comment by drkirkby created at 2010-08-27 11:48:21

Replying to [comment:5 mpatel]:
> A way to upload anonymized test stats and system information to a remote server?
Yes, but with the option of giving a name if one wishes to. It will make problems easier to manage if people did give a name + email, but certainly make it optional.


---

Comment by mpatel created at 2010-08-27 22:25:14

Replying to [comment:6 mpatel]:
> Also potentially useful: doctesting the same file multiple times in parallel.  I think this is just a matter of generating in `sage-doctest` a unique name, e.g., `.doctest_foo-R3X87S.py` for each run on `foo.py`.

This is #9739.


---

Comment by drkirkby created at 2010-08-27 22:32:07

Replying to [comment:2 mpatel]:
> If we widen the scope here a bit:  We should use [optparse](http://docs.python.org/library/optparse.html), at least, to handle command-line arguments.
Though if you look at that link, it says its been depreciated in favor of `argparse`. 

Dave


---

Comment by mpatel created at 2010-08-28 00:44:40

Replying to [comment:11 drkirkby]:
> Replying to [comment:2 mpatel]:
> > If we widen the scope here a bit:  We should use [optparse](http://docs.python.org/library/optparse.html), at least, to handle command-line arguments.
> Though if you look at that link, it says its been depreciated in favor of `argparse`. 

That's why I inserted "at least," but I should have more specific.  We'll need to upgrade to Python 2.7 to use [argparse](http://docs.python.org/library/argparse.html#module-argparse) readily.  [argparse](http://code.google.com/p/argparse/) used to be an independent project.


---

Comment by leif created at 2010-12-16 02:40:00

Rob, perhaps you could state your personal wishes here, too.

(E.g. `./sage -testall ...` with an option to specify the number of threads IIRC rather than always doing that serially.)


---

Comment by leif created at 2010-12-16 03:04:03

#10458 improves cut & paste of doctest code & output from an actual Sage session, in that it allows also "`....: `" for line continuations. (Previously, for some reason only "`...`" was supported in docstrings; also the confusion with an ellipsis intended to mean arbitrary *output* should be reduced by this ticket.)

Another problem still has to be addressed: The original (non-preparsed) source code of continuation lines gets "lost", i.e. doesn't end up in the end-of-line comments of the generated test files (`.doctest_*`) as it does for ordinary lines, hence also won't be shown on doctest errors or when one doctests in verbose mode.


---

Comment by roed created at 2012-02-06 05:22:50

#12415 will add many of these features.


---

Comment by jdemeyer created at 2013-02-28 16:09:53

As David mentioned, there is a lot of work at #12415. And apart from that, this ticket is extremely vague.


---

Comment by jdemeyer created at 2013-02-28 16:09:53

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-02-28 16:10:00

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-07 08:18:34

Resolution: invalid
