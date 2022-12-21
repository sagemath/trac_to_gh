# Issue 8654: add "sage -sqlite3" command line option

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-06 16:49:12

Assignee: jason

Just like "sage -gap", we should have "sage -sqlite3" to run the command line sqlite3 database included with Sage.


---

Comment by ohanar created at 2010-11-12 11:02:19

#21 fixes this.


---

Comment by ohanar created at 2011-09-13 01:51:15

Changing status from new to needs_review.


---

Attachment

Since #21 probably needs to be rewritten from scratch by now.


---

Comment by was created at 2011-09-28 04:44:30

Changing status from needs_review to positive_review.


---

Comment by was created at 2011-09-28 04:44:30

Nice.  I'm glad you implemented this.  Works fine.


---

Comment by jdemeyer created at 2011-10-04 08:14:18

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-10-04 08:14:38

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2011-10-04 08:14:38

[attachment:8654_test.patch] needs review.


---

Comment by jdemeyer created at 2011-10-10 10:18:00

Ping.  Needs review.


---

Comment by leif created at 2011-10-29 21:40:31

Changing status from needs_review to needs_work.


---

Comment by leif created at 2011-10-29 21:40:31

Testing for the exact version number in `sage/tests/cmdline.py` is certainly suboptimal.


`install_scripts()` (in `sage/misc/dist.py`) needs to be updated, too.


----

Could do some bikeshedding here:

 * The following

```sh
    some_program "$`@`"
    exit $?
```

   should be just

```sh
    exec some_program "$`@`"
```

   (perhaps followed by `exit $?` if we want to go triple-safe).

 * The help messages should use the long option form (`--foo` rather than `-foo`). 

   Stating that `sage -foobar` runs Sage's version of `foobar` foreach foobar \in {A,...,Z} is of questionable value.

 * Doing

```sh
if [ foo = bar -o foo = BAR ]; then
    ...
fi

if [ foo = baz -o foo = BAZ ]; then
    ...
fi

if [ foo = whatever ]; then
    ...
fi
```

   is very poor.  It should simply be

```sh
case foo in
    bar|BAR)
        ...
        ;;
    baz|BAZ)
        ...
        ;;
    ...
esac
```

   which is faster, safer, easier to read and also less error-prone.


One could change _all_ of these at once on a separate ticket, but it's IMHO dumb to always replicate the same bad code again.  So I'd change it at least in the new parts (and in general those one touches anyway or the ones near to them.)


---

Comment by ohanar created at 2011-10-30 00:46:31

Replying to [comment:10 leif]:
> Could do some bikeshedding here: 

> ... 

> One could change _all_ of these at once on a separate ticket, but it's IMHO dumb to always replicate the same bad code again.  So I'd change it at least in the new parts (and in general those one touches anyway or the ones near to them.)

See #21, although that patch will probably need to get rewritten with argparse now that optparse has been deprecated.


---

Attachment

Add test for --sqlite3 command line option


---

Comment by jdemeyer created at 2011-10-30 11:09:28

Replying to [comment:10 leif]:
> Testing for the exact version number in `sage/tests/cmdline.py` is certainly suboptimal.
Changed.

> `install_scripts()` (in `sage/misc/dist.py`) needs to be updated, too.
Done.

> One could change _all_ of these at once on a separate ticket, but it's IMHO dumb to always replicate the same bad code again.  So I'd change it at least in the new parts (and in general those one touches anyway or the ones near to them.)
Well, I agree that we should change all this in a separate ticket (I guess #21 is the place to be).  By copying the same so-called "bad" code we at least have consistency which is also a good thing.  If every command line option is implemented in a different way, that will make the code harder to understand.  Moreover, this ticket is not the correct place to discuss what the "right" code is.


---

Comment by jdemeyer created at 2011-10-30 11:09:28

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-11-02 01:26:01

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2011-11-02 01:26:01

Looks good to me.


---

Comment by jdemeyer created at 2011-11-02 08:29:58

Many thanks for the review, this has taken long enough.


---

Comment by jdemeyer created at 2011-11-03 08:51:31

Resolution: fixed


---

Comment by jdemeyer created at 2011-11-03 16:14:43

Milestone sage-4.7.3 deleted
