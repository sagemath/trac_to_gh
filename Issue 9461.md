# Issue 9461: Doctest failures with sage -t -randorder=X

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-09 05:28:56

Assignee: mvngu

CC:  jmantysalo

Start with a build of 4.5.alpha4 for which all long doctests pass.  Run, e.g.,

```sh
$ ./sage -t -long -sagenb -randorder=12345 devel/sage
```

Many tests fail.


---

Comment by mpatel created at 2010-07-09 05:34:36

[Here](http://sage.math.washington.edu/home/mpatel/trac/9461) are raw test logs from parallel testing on sage.math.  I made these with, e.g.,

```sh
$ nohup nice -n 19 ./sage -tp 22 -long -sagenb -randorder=X devel/sage  > ptestlong_randorderX.log &
```



---

Comment by jmantysalo created at 2016-07-25 06:46:02

I suggest that for a while we use keyword "random_test_failure" for these.

Volker suggested adding `# seed0` tag to tests that should not be run when `--randorder` is not zero (i.e. the default). I guess that it is a good idea, but maybe we should see some examples first. #21054 is clearly an error; #21080 fails in a line with comment "needed until #19269 is fixed"; `src/sage/graphs/base/graph_backends.pyx` gives a deprecation warning.
