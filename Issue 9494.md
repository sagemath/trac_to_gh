# Issue 9494: Add a doctest to benchmark.py

Issue created by migration from Trac.

Original creator: demosd235

Original creation time: 2010-07-14 09:28:21

Assignee: mvngu

Demo at SD23.5, also increases coverage!


---

Comment by demosd235 created at 2010-07-14 09:33:30

Add a comment to a ticket here.


---

Comment by demosd235 created at 2010-07-14 09:33:49

Is this ready yet?


---

Comment by demosd235 created at 2010-07-14 09:33:49

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2010-12-01 12:51:56

According to http://www.sagemath.org/doc/developer/conventions.html#docstring-markup-with-rest-and-sphinx it should be `EXAMPLES:` instead of `EXAMPLE::`.

It's enough to put only 3 dots between `<BLANKLINE>` and `System` but this is okay as well.


---

Comment by mariah created at 2011-05-26 15:43:41

Changing status from needs_review to needs_work.


---

Comment by rbeezer created at 2011-08-22 07:09:35

Changing status from needs_work to needs_info.


---

Comment by rbeezer created at 2011-08-22 07:09:35

If an "EXAMPLES" block just has one example, then it is OK to drop the S.  And if there is no prose before the test, then a double-colon can be used to indicate verbatim text next.

There are excess ... but they cause no harm.  This ticket looks good to me.  Am I missing something?  It looks ready for a positive review to me.

I am working on this as a high-priority ticket for Bug Days 32.

Rob


---

Comment by benjaminfjones created at 2011-08-23 00:46:11

The patch looks good to me and passes doctests:


```

bjones`@`sage:~/sage/sage-4.7.1/devel/sage$ ../../sage -t sage/tests/benchmark.py 
sage -t  "devel/sage-9494/sage/tests/benchmark.py"          
	 [8.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 8.6 seconds
```


I'm giving it a positive review.


---

Comment by benjaminfjones created at 2011-08-23 00:47:08

Changing status from needs_info to needs_review.


---

Comment by benjaminfjones created at 2011-08-23 00:47:16

Changing status from needs_review to positive_review.


---

Comment by was created at 2011-08-24 23:45:20

Changing keywords from "" to "sd32".


---

Comment by leif created at 2011-09-16 06:38:19

Actually, `mpoly_all()` needs work, since it is apparently unable to interrupt (e.g.) Mathematica a second time.

On redhawk, where `/home` still isn't mounted, Mathematica is installed but fails to startup (prompting the user), such that I get:

```sh
leif`@`redhawk:/$ time sage -c "from sage.tests.benchmark import mpoly_all; mpoly_all()" 



Compute (x_0 + ... + x_99) * (x_100 + ... + x_200) over Rational Field (use singular for Sage mult.)
  System      min         avg         max         trials          cpu or wall
* sage        0.049767    0.049767    0.049767    1                  0.049767w
Unable to start magma
computation timed out because alarm was set for 60 seconds
Unable to start macaulay2 because the command 'M2 --no-debug --no-readline --silent -e 'ZZ#{Standard,Core#"private dictionary"#"InputPrompt"} = lineno -> "_EGAS_ : ";ZZ#{Standard,Core#"private dictionary"#"InputContinuationPrompt"} = lineno -> "_EGAS_ : ";printWidth = 0;lineNumber = 10^9;'' failed.




Compute (x_0 + ... + x_199) * (x_200 + ... + x_400) over Rational Field (use singular for Sage mult.)
  System      min         avg         max         trials          cpu or wall
* sage        0.089736    0.089736    0.089736    1                  0.089736w
Unable to start magma
Interrupting Mathematica...
```

which does not terminate.

What is this doctest supposed to "test" at all?

The output is random, so it doesn't really test anything, except perhaps which external programs are installed, but that's nothing subject to a doctest, so IMHO this ticket should either be closed as invalid, or the "doctest" (i.e., the example) should be marked `# not tested`, at least until `mpoly_all()` got fixed.


---

Comment by leif created at 2011-09-16 06:38:19

Changing status from positive_review to needs_work.


---

Attachment

marked mpoly_all() as not tested


---

Comment by benjaminfjones created at 2012-04-07 23:52:22

Changing status from needs_work to needs_review.


---

Comment by benjaminfjones created at 2012-04-07 23:53:56

I marked `mpoly_all()` as `# not tested`. The new patch applied cleanly to 5.0.beta12 and passes tests on `sage.math.washington.edu` where Mma is installed. I'm running tests on redhawk now to double check.


---

Comment by benjaminfjones created at 2012-04-08 04:06:28

There seems to still be an issue with the Mma installation on redhawk and the `mpoly_all()` test is still unable to interrupt the crashed process all the time:


```
Compute (x_1 + 2*x_2 + 3*x_3 + ... + 128*x_128) * (129 * x_129 + ... + 257*x_257) over Rational Field (use singular for Sage mult.)
  System      min         avg         max         trials          cpu or wall
* sage        0.049826    0.049826    0.049826    1                  0.049826w
Unable to start magma
Mathematica crashed -- automatically restarting.
computation timed out because alarm was set for 60 seconds
Unable to start macaulay2 because the command 'M2 --no-debug --no-readline --silent -e 'ZZ#{Standard,Core#"private dictionary"#"InputPrompt"} = lineno -> "_EGAS_ : ";ZZ#{Standard,Core#"private dictionary"#"InputContinuationPrompt"} = lineno -> "_EGAS_ : ";printWidth = 0;lineNumber = 10^9;'' failed.




Compute (x_1 + 2*x_2 + 3*x_3 + ... + 256*x_256) * (257 * x_257 + ... + 513*x_513) over Rational Field (use singular for Sage mult.)
  System      min         avg         max         trials          cpu or wall
* sage        0.149662    0.149662    0.149662    1                  0.149662w
Unable to start magma
Interrupting Mathematica...
^C
Unable to start macaulay2 because the command 'M2 --no-debug --no-readline --silent -e 'ZZ#{Standard,Core#"private dictionary"#"InputPrompt"} = lineno -> "_EGAS_ : ";ZZ#{Standard,Core#"private dictionary"#"InputContinuationPrompt"} = lineno -> "_EGAS_ : ";printWidth = 0;lineNumber = 10^9;'' failed.
```


But I'd say that's an issue for another ticket.


---

Comment by rws created at 2014-02-14 16:13:41

Moved patch to git.
----
New commits:


---

Comment by rws created at 2014-02-14 16:13:41

Changing status from needs_review to positive_review.


---

Comment by git created at 2014-02-20 17:23:36

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:


---

Comment by git created at 2014-02-20 17:23:36

Changing status from positive_review to needs_review.


---

Comment by rws created at 2014-02-20 17:45:20

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-23 07:46:26

Resolution: fixed
