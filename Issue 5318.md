# Issue 5318: ideas for improving random testers (like #4779)

Issue created by migration from https://trac.sagemath.org/ticket/5318

Original creator: cwitty

Original creation time: 2009-02-20 07:51:47

Assignee: mabshoff

Random testers (like the ones in #4779) should have a structure something like this (untested):


```
def test_foo(n_trials, seed=None, verbose=False):
  with random_seed(seed):
    used_seed = initial_seed()
    try:
        for i in range(n_trials): # or whatever
            ... do test
            ... if verbose, then print out the details of the
                test you're running
    except:
        print "We've detected a failure in random testing."
        print "Please report this bug; you may be the only person"
        print "in the world to see this particular problem!"
        print "initial seed: " + used_seed
        print "trial: " + i
        raise
```


Then the doctests should start with:

```
sage: test_foo(2, seed=0, verbose=True)
... verbose output from two tests; should always be the same across machines, etc.
```

to verify that the test is correctly using the randstate framework, so that failures can be reproduced.

Then you can continue to:

```
sage: test_foo(10)
sage: test_foo(100) # long time
```

which will use truly random seeds (with /dev/urandom).

The above should be adjusted if you want to run the testing function for a very long time; you would want to re-initialize the random seed at least every few seconds, so that if you detect a problem after running for several hours, you don't have to run for the same several hours to reproduce it.

The simplest way is not to loop for long inside the function; instead, do:

```
while True:
    test_foo(100)
```


(That's a lot of boilerplate; maybe this whole setup can be encapsulated in a decorator?)


---

Comment by cwitty created at 2009-02-21 03:05:45

I've attached a patch implementing the above ideas as a decorator, and adapted the random testers from #4779 to use this decorator.

I'm changing the milestone to Sage 3.3.  I don't actually expect to get this patch into 3.3, and I'm happy to rebase it if it doesn't make it; but I didn't want to rule out the possibility :)


---

Comment by nthiery created at 2009-03-18 08:41:03

Hi!

Cool stuff. I am about to give it a thumb up!

Three comments:
 - When the category stuff will be in there, we should merge this into the category-held tests.
   But let's not wait for that.

 - The code is not trivially small, so I would put it in a separate file with the same name as the decorator

 -  while we are at saving on boiler plate: would it be possible for the wrapper
    to also handle the iteration loop?

   One nice side benefit is that the wrapper would be aware of the value of the seed at the begining of each iteration, and therefore could report it in case of trouble (I have not yet played with random generators in python, but I assume that we can access the current value of the seed after a couple random generation). Reproducing  the error would then involve a single iteration.


---

Comment by cwitty created at 2009-03-18 15:27:11

_the code is not trivially small_

Actually, it is; random_testing is 26 lines of code by my count, ignoring docstrings and comments :)

But yes, once you include the tests, the documentation, and the comments, it does look pretty big.  I'll move it into its own file.

I'm not sure what to do about the iteration loop idea.  I wouldn't want iteration to be always handled in the wrapper; for example, that could vastly slow down testing if the tester were written in Cython, or if the testing function needed to do some non-trivial setup before starting the loop.  And there's no good way to tell the wrapper whether the wrapper or the wrappee should handle iteration (it could key off the argument name, but that doesn't sound like a good way).

Also, unfortunately, the primary source of random numbers in Sage (GMP's Mersenne Twister implementation) doesn't let you read back the current state.


---

Attachment

I posted a new patch (and deleted the old version) that moves `@`random_testing into its own file (and adds it to the reference manual).  I didn't implement the other requested feature, of providing an iteration loop, for the reasons mentioned in my previous comment.


---

Comment by nthiery created at 2009-03-31 03:27:03

See #5647 for a follow up.


---

Comment by mabshoff created at 2009-04-01 01:54:30

Merged in Sage 3.4.1.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-01 01:54:30

Resolution: fixed
