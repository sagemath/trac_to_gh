# Issue 3231: Use the randgen framework to set the seeds for controlled Magma, Singular, etc. sessions

Issue created by migration from https://trac.sagemath.org/ticket/3231

Original creator: malb

Original creation time: 2008-05-16 23:14:33

Assignee: was

If e.g. Magma is started from Sage then the seed parameter (`-S seed`) should be set using the randgen framework maybe.


---

Comment by cwitty created at 2009-02-24 02:15:43

Changing status from new to assigned.


---

Comment by cwitty created at 2009-02-24 02:15:43

Changing assignee from was to cwitty.


---

Comment by tscholl2 created at 2015-05-25 22:53:25

New commits:


---

Comment by git created at 2015-05-26 13:46:34

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-05-26 15:48:43

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscholl2 created at 2015-05-26 15:51:50

Changing status from new to needs_review.


---

Comment by tscholl2 created at 2015-05-26 15:55:26

I added a `set_seed` function on a lot of the interfaces such as gap, gp, magma, maxima, R, and singular. This allows setting the seed for the corresponding random number generator.

This made solving the ticket very easy by just calling "set_seed" when the interface is started with `_start`.

I think someone should rewrite the `randstate` class to use these methods if possible. However that would require someone with more cython knowledge.

Also `set_seed` still needs to be implemented on a few more interfaces, but those are not free so they are not as easy to test with.


---

Comment by malb created at 2015-05-27 09:23:43

Maybe this ticket should be repurposed then and another ticket created to realise the integration into the randgen() framework? It'd be a shame if this bitrots.


---

Comment by tscholl2 created at 2015-05-27 14:31:08

I think this ticket is fine because it's still a step in the right direction. In my mind the best framework would be for every interface to have a `set_seed` function like these. Then `randstate` would have methods that take in an instance of an interface and set it's seed using that method. Right now there is no control over multiple instances of interfaces, which it seems like there could/should be, and it might even simplify some of the `randstate` code.

Also `randstate` would still set seeds for non-interfaces such as libraries like `libc` and `python.random` (or wrap the random calls as it does). All of the `set_seed` methods I wrote default to `interface.rand_seed` on startup which uses `randstate`, so I think this fit the description of this ticket.

I think the next ticket should be specifically about `randstate` and be dependent on this one. I am worried repurposing this ticket to do both might be a bit much. Or did you have something else in mind?


---

Comment by malb created at 2015-05-28 10:23:20

I agree: let's deal with what you've done in this ticket (and change the description accordingly) and then open another follow up ticket which deals with the `randstate` business.


---

Comment by git created at 2015-05-29 02:36:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-05-29 02:41:03

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscholl2 created at 2015-05-29 02:54:58

I repurposed this ticket to match the new directions for the `randstate` class. This ticket is now focused on setting the seeds for the interfaces as the code I uploaded does for many of the interfaces.

There will be a new ticket to rewrite the `randstate` class to use these methods as well as allow for setting the seed on particular instances of interfaces. This may force a small change in the `randstate` api, but that is for the next ticket.


---

Comment by malb created at 2015-06-12 17:28:09

Changing status from needs_review to needs_work.


---

Comment by malb created at 2015-06-12 17:28:09

In /src/sage/interfaces/interface.py the new function


```
+    def get_seed(self):
+        return self._seed
```


lacks documentation and a doctest. The next two functions lack doctests (I know it's silly)

Other than that, it looks good to me.


---

Comment by git created at 2015-06-12 20:12:50

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscholl2 created at 2015-06-12 20:17:22

Woops, examples are always helpful!

I added documentation and doctests to the functions in interfaces. I copied them out of octave's file, hopefully that works.


---

Comment by tscholl2 created at 2015-06-12 20:17:22

Changing status from needs_work to needs_review.


---

Comment by malb created at 2015-06-13 09:55:23

Changing status from needs_review to needs_info.


---

Comment by malb created at 2015-06-13 09:55:23

Why does your patch drop `set_seed` for Gap? 

I'd also say, if possible, then it shouldn't be tested with the Octave example: Octave is optional, e.g. Singular is not. Secondly, the closer to the actual code, the better. So if we can instantiate an `Interface` object directly that'd be best.


---

Comment by git created at 2015-06-13 14:23:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-06-13 14:30:02

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscholl2 created at 2015-06-13 14:32:40

There was actually two `set_seed` for Gap. The file was long and I accidentally copied another to a slightly different place. You can still see the actual `set_seed` function under the total diff.

These new pushes change the doc tests in `interface.py` to use Singular (so less optional packages) and also use an instance of `Interface` directly. This is ok for `rand_seed` and `get_seed` but not for `set_seed` as that has to be implemented by the specific interface. Do you think we need a doc test which raises the `NotImplementedError`?


---

Comment by malb created at 2015-06-15 07:31:37

Changing status from needs_info to positive_review.


---

Comment by malb created at 2015-06-15 07:31:37

Looks good to me. 

I guess technically we should actually doctest a `NotImplementedError` but I'll leave it up to you.


---

Comment by git created at 2015-06-15 15:07:03

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:


---

Comment by git created at 2015-06-15 15:07:03

Changing status from positive_review to needs_review.


---

Comment by tscholl2 created at 2015-06-15 15:08:15

I added a doc test for the `set_seed` method for the general interface. It was easy to add.


---

Comment by malb created at 2015-06-15 16:36:09

Changing status from needs_review to positive_review.


---

Comment by malb created at 2015-06-15 16:36:09

Looks good to me.


---

Comment by vbraun created at 2015-06-15 20:23:53


```
sage -t --long src/sage/interfaces/magma.py  # 2 doctests failed
sage -t --long src/sage/interfaces/octave.py  # 2 doctests failed
sage -t --long src/sage/interfaces/scilab.py  # 2 doctests failed
sage -t --long src/sage/repl/interpreter.py  # 1 doctest failed
```



---

Comment by vbraun created at 2015-06-15 20:23:53

Changing status from positive_review to needs_work.


---

Comment by tscholl2 created at 2015-06-17 02:54:58

I get the first 3 errors if I run `sage -t --long src/sage/interfaces/magma.py` but not if I run `./sage -t --long src/sage/interfaces/magma.py`. Shouldn't I only be checking if it runs with the version of Sage on the branch and not the user's systems' version?

The last error seems to be something I didn't notice. Apparently some of the interfaces keep a counter of the commands used and label things with it. The `set_seed` function for some interfaces raises this counter because it needs to call a command in the interface. So running the test in `src/sage/repl/interpreter.py` the counter is off from what it used to be.

This error doesn't occur if I comment out line 626 in `src/sage/interfaces/maxima.py`:

```
625 # set random seed
626 self.set_seed(self._seed)
```


I'm not sure what to do about this. It seems like there is a few options:

* We could reset the counter after the `set_seed` function is called (I actually don't know if this is possible yet).
* We could change all the doc tests in functions which use this counter and increment it manually.
* We could not run `set_seed` on start and leave it up to the user to run it.

Martin, do you have any suggestions on which way to proceed?


---

Comment by malb created at 2015-06-18 14:39:44

Ah, crap my comments from yesterday seem not to have arrived:

- You are not seeing these errors because you have octave et al. installed in your local development environment. In other words: some doctests are not marked optional but you should be marked optional. 

- I'd just update the doctest, `set_seed()` is a proper call, so no point in resetting the counter.


---

Comment by git created at 2015-06-18 16:10:13

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscholl2 created at 2015-06-18 18:32:32

I added `# optional -` tags to the corresponding doc tests. I think I got all of them, but someone should check. Strangely enough, this also fixed the other test `sage -t --long src/sage/repl/interpreter.py`. Which may mean that either it wasn't actually counting the calls to the interpreter, or something else happened with the optional flags which affected it.


---

Comment by tscholl2 created at 2015-06-18 18:32:32

Changing status from needs_work to needs_review.


---

Comment by malb created at 2015-06-19 08:10:46

I still get 


```
sage -t --warn-long 33.6 src/sage/repl/interpreter.py  # 1 doctest failed
**********************************************************************
File "src/sage/repl/interpreter.py", line 561, in sage.repl.interpreter.InterfaceShellTransformer.preparse_imports_from_sage
Failed example:
    ift.preparse_imports_from_sage('2 + maxima(a)')
Expected:
    '2 +  sage1 '
Got:
    '2 +  sage4 '
```


but the other three are gone.


---

Comment by malb created at 2015-06-19 08:10:46

Changing status from needs_review to needs_work.


---

Comment by git created at 2015-06-21 17:47:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscholl2 created at 2015-06-21 17:54:16

I removed some white space and changed a doctest in `src/sage/repl/interpreter.py`.

The doc test was failing because `maxima` now calls `set_seed` on startup which uses several calls to the maxima interpreter. Therefore instead of getting back `2 +  sage1`, it should get back `2 + sage4`.


---

Comment by tscholl2 created at 2015-06-21 17:54:16

Changing status from needs_work to needs_review.


---

Comment by malb created at 2015-06-22 13:09:34

tests pass here & looks good.


---

Comment by malb created at 2015-06-22 13:09:34

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-06-22 22:25:10

Resolution: fixed
