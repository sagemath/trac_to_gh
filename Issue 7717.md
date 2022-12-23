# Issue 7717: sage -coverage enhancement

Issue created by migration from https://trac.sagemath.org/ticket/7717

Original creator: roed

Original creation time: 2009-12-17 01:44:07

Assignee: mvngu

Keywords: coverage

Adds features to the sage-coverage script.

- rewrite for modularity and easier addition of features
- changes the score of the file to reflect the presence or absence of a TestSuite.run or equivalent test.
- adds option to check cdef'd functions
- adds option to check docstrings on classes
- adds option to check for the existence of INPUT block
- adds option to check that parameters are all listed in the INPUT block.
- adds option to check for the existence of OUTPUT block

So that we don't bring our coverage level way down, these aren't turned on automatically.  Instead, they can be invoked from the command line by using options ( -cdefs, -classes, -input, -output and -params)


---

Comment by roed created at 2009-12-17 01:46:11

Duplicate of 7716: please delete.


---

Comment by mvngu created at 2009-12-17 01:47:40

Resolution: duplicate


---

Comment by mvngu created at 2009-12-17 01:47:40

Closing this as a duplicate of #7716.
