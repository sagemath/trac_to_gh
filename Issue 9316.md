# Issue 9316: Spurious (?) "# File not found" error at end of doctests

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-23 04:19:18

Assignee: wjp

CC:  leif

Many people have reported a "File not found" error that is reported at the end of "make test" when *in fact* a timeout occurred. 

This is caused by some weird code introduced in #7993 (see sage-test):

```
...
    s = os.path.join(SAGE_ROOT, 'local', 'bin', 'sage-%s' % cmd) + ' "%s"' % F
    err = os.system(s)
    # On unix systems, the return value of os.system has the process return
    # value in the second byte.
    err = err // 256

    # Check the process exit code that sage-doctest returns

    if err == 1: # process exit code 1: File not found
        failed.append(sage_test_command(F)+" # File not found")
```



---

Comment by cremona created at 2010-06-23 04:23:04

Example:

```

sage -t  "devel/sage/sage/rings/number_field/number_field_rel.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
Traceback (most recent call last):
  File "/home/john/sage-4.4.4.alpha1/local/bin/sage-doctest", line 798, in <module>
    test_file(argv[1], library_code = library_code)
  File "/home/john/sage-4.4.4.alpha1/local/bin/sage-doctest", line 695, in test_file
    print "The doctested process was killed by signal %s" % (-e)
TypeError: bad operand type for unary -: 'NoneType'
         [8319.2 s]
```

The reason for the timeout was simply that I suspended my laptop for a couple of hours and then woke it up.  But at the end of the test (I was doing "make test" on 4.4.4.alpha1) the error message said

```

The following tests failed:


        sage -t  "devel/sage/sage/rings/number_field/number_field_rel.py" # File not found
```



---

Comment by drkirkby created at 2010-06-23 05:07:41

I agree a timeout can cause this. I tried the patch which is supposed to fix the Mathematica interface, but that timed out after 10,000 seconds with a "File not found" message. 

However, BSD.py is completing well within the time I've set as SAGE_TIMEOUT and SAGE_TIMEOUT_LONG, so I doubt the BSD.py issue was a simple timeout 


```
drkirkby`@`redstart:~$ echo $SAGE_TIMEOUT_LONG
10000
drkirkby`@`redstart:~$ echo $SAGE_TIMEOUT     
1000
```


But BSD.py is taking 205 seconds


```
drkirkby`@`redstart:~/sage-4.4.4.alpha1$ ./sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py
sage -t -long "devel/sage/sage/schemes/elliptic_curves/BSD.py"
         [205.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 205.5 seconds
```


Sure BSD.py will take longer if the machine is more heavily loaded, but it would need a *huge* load to make the test take over 10000 seconds. The load would have to go up by a factor of 48! Given it's my own machine, and nobody else uses it, I have a pretty good idea the load would not have risen that much. 

My Blade 1000 does not have a lot of RAM (only 2 GB), so potentially it could swap if it run out of RAM, but I don't believe that was the problem. It certainly does not have any power saving features - that's why I keep it in the garage and use it as a heater in the Winter! That machine does not hybernate! 

Dave


---

Comment by wjp created at 2010-06-23 08:32:09

This appears to be caused by timeouts not being properly handled by `sage-doctest`. It prints the error message, but then doesn't actually do anything with it. It looks like I completely missed that case when doing #7993. This also explains the strange exception John is seeing. It's reaching code that shouldn't be reached in this case.

In the patch I'm attaching, I'm making `sage-doctest` return exit code 5 for a time out, and `sage-test` and `sage-ptest` will also interpret that that way.

(Note that this will conflict with #8641, but the conflict is easy to resolve.)


---

Comment by wjp created at 2010-06-23 08:32:09

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-06-23 14:28:21

I won't say positive review 100% because someone who knows all the ins and outs should have a quick look at it.    But it works as advertised.  I do wonder if there need to be two separate tests for 

```

sage -t  "devel/sage/sage/calculus/calculus.py"             
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
	 [556.2 s]
```

or if one could immediately sys.exit(5) instead of having two separate timeout messages?  Or this may be a feature - one for the process, one for the file.


---

Comment by drkirkby created at 2010-06-25 06:38:00

I'm still suspicious that the "File not found" error I got with BSD.py (#9273)is anything to do with a timeout problem. Why should a test take 205 seconds on one occasion and over 10000 seconds on another?


---

Comment by wjp created at 2010-06-25 08:35:16

I'd be ok with directly doing a `sys.exit(5)`, I think. Or maybe removing the `print` statements from after the `kill` calls, and only leave the `print` with the `sys.exit(5)` at the end in place.

Another thing in there that doesn't seem to make much sense is the '`err`' string, which never seems to be set, but still is used in one of the `KeyboardInterrupt` checks.


---

Comment by wjp created at 2010-06-27 11:01:43

I submitted a new patch that uses exit code 6 instead of 5, since it turns out 5 is used internally by `sage-ptest`.


---

Attachment

rebased after #8641 and #9243


---

Attachment


---

Comment by wjp created at 2010-07-06 21:04:00

I removed the second print statement so there is no longer a double TIMED OUT message, and rebased the patch to apply after #8641 and #9243.


---

Comment by mpatel created at 2010-07-07 03:32:52

I get

```sh
$ env SAGE_TIMEOUT=10 ./sage -t devel/sage/sage/rings/number_field/number_field_rel.py 
sage -t  "devel/sage/sage/rings/number_field/number_field_rel.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***

         [10.2 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/rings/number_field/number_field_rel.py" # Time out
Total time for all tests: 10.2 seconds
$ echo $?
64
}}}  

Maybe we should print a brief message about increasing `SAGE_TIMEOUT` and `SAGE_TIMEOUT_LONG`, if at least one test times out?

To release manager: Apply only [attachment:scripts9316_timeout_rebased.patch] to 4.5.alpha4 + #8641 + #9243.


---

Comment by mpatel created at 2010-07-07 03:32:52

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-07 03:40:25

Related tickets: #9224, #9225.  Suggestions are welcome!


---

Comment by drkirkby created at 2010-07-08 11:25:53

Replying to [comment:9 mpatel]:
 
> Maybe we should print a brief message about increasing `SAGE_TIMEOUT` and `SAGE_TIMEOUT_LONG`, if at least one test times out?

That does seem very sensible, since these options are not well known. They are now documented in #8263, which adds them to the Installation Guide, but I would agree it would be useful to print this. 

Also see #9449 for yet more issues with doctesting, where the results are confusing. I don't know if tests have passed or failed in some cases.


---

Comment by ddrake created at 2010-07-22 07:59:57

Merged attachment:scripts9316_timeout_rebased.patch in 4.5.2.alpha1.


---

Comment by ddrake created at 2010-07-22 07:59:57

Resolution: fixed
