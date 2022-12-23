# Issue 6892: [with patch, needs review] change dollar signs to backticks

Issue created by migration from https://trac.sagemath.org/ticket/6892

Original creator: jhpalmieri

Original creation time: 2009-09-04 21:26:11

Assignee: jhpalmieri

In [a discussion on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8fa0d854b6928f2b?tvc=2), people thought it was a good idea to allow the use of dollar signs, not just backquotes, to delimit math in Sage docstrings.  The attached patch does this.  It does this by working with the autodoc extension to Sphinx: autodoc reads the docstring, which then gets processed by the new function `process_dollars`, which does various regular expression search-and-replacements.

Consequences of this: if you want to use a literal dollar sign in a docstring, you have to escape it with a  backslash.  If you have some complicated math with lots of nested math/text constructions like "\text{blah $x=y$ blah}", this might screw up.  It will handle one nesting, turning

```
$f(x) = \text{zero if $x$ is prime}$
```

into

```
`f(x) = \text{zero if $x$ is prime}`
```

and leaving 

```
`f(z) = \text{two if $z$ is an integer}`
```

unchanged; these should be processed correctly by both the html and pdf documentation builders.

The patch also changes some docstrings: either fixing minor misformattings which I noticed while testing this, or fixing things which break (like a docstring with a math environment with a missing closing dollar sign) when dollar signs are converted to backquotes.

Seems to work with Sphinx versions 0.5.1 (currently included in Sage) and 0.6.3 (see #6586).


---

Attachment


---

Comment by ddrake created at 2009-09-16 03:03:28

minor rebase for 4.1.2.alpha1; tiny changes to conf.py and ambient_g0.py


---

Attachment

rebased against 4.1.2.alpha2, plus a little documentation


---

Comment by jhpalmieri created at 2009-09-22 03:01:57

Apply only trac_6892-dollars-rebased.patch.  This adds a little documentation in the developer's guide about using dollar signs instead of backticks.


---

Comment by mhansen created at 2009-10-05 07:35:51

Looks good to me.


---

Comment by mhansen created at 2009-10-16 04:49:03

Resolution: fixed
