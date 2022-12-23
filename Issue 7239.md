# Issue 7239: factorization of Cunningham numbers

Issue created by migration from https://trac.sagemath.org/ticket/7239

Original creator: ylchapuy

Original creation time: 2009-10-18 10:27:05

Assignee: tbd

CC:  mvngu

A small spkg to provide factorization of Cunningham numbers.

The raw data is from http://cage.ugent.be/~jdemeyer/cunningham


---

Comment by ylchapuy created at 2009-10-18 10:30:48

The package is here: http://yann.laiglechapuy.net/spkg/cunningham_tables-1.0.spkg


---

Attachment

based on 4.1.2


---

Comment by ylchapuy created at 2009-10-19 22:28:09

mvngu, I add cc'ed you as you were interested in ticket #191


---

Comment by ylchapuy created at 2009-10-26 21:59:20

Changing status from new to needs_review.


---

Comment by cremona created at 2009-11-22 17:56:52

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2009-11-22 17:56:52

I tried to install using "sage -i cunningham_tables-1.0.spkg" after downloading it, but I had error messages:

```
...
Finished extraction
sage: After decompressing the directory cunningham_tables-1.0 does not exist
This means that the corresponding .spkg needs to be downloaded
...
```

Should I have applied the patch first?  It would help to give more detailed instructions!

Separate question:  did you ask Jeroen Demeyer about using his data?


---

Comment by ylchapuy created at 2009-11-23 19:59:35

Concerning the package, the failure was of course due to a silly mistake I made. The new spkg should work.

the procedure you tried was the good one:

     * download the spkg
     * install it with `sage -i cunningham_tables-1.0.spkg`
     * apply the patch

Concerning the author of the data I used, I just wrote him an email to ask for an "official"comment on this use of the data he collected and will send his answer as soon as I get it.


---

Comment by ylchapuy created at 2009-11-23 19:59:35

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2009-11-23 20:55:31

Where is the "new" spkg?  Is it still called cunningham_tables-1.0.spkg?  I downloaded it (again, assuming it had changed) but the same thing happened.

I expect Jeroen will be amenable (if necessary I could also ask him as I know him).


---

Comment by ylchapuy created at 2009-11-23 21:49:03

the new spkg is at the same address.
I tested it again and it works for me now.

The previous one was creating a directory named "cunningham_tables" when decompressed, then only difference with the new one is that the directory is now named "cunningham_tables-1.0".
You might check you have the right one by trying for yourself:

`tar tjf cunningham_tables-1.0.spkg` should answer

```
cunningham_tables-1.0/
cunningham_tables-1.0/.hg/
cunningham_tables-1.0/.hg/store/
cunningham_tables-1.0/.hg/store/fncache
cunningham_tables-1.0/.hg/store/undo
cunningham_tables-1.0/.hg/store/00manifest.i
cunningham_tables-1.0/.hg/store/00changelog.i
cunningham_tables-1.0/.hg/store/data/
cunningham_tables-1.0/.hg/store/data/_s_p_k_g.txt.i
cunningham_tables-1.0/.hg/store/data/read__cunningham__prime__factors.py.i
cunningham_tables-1.0/.hg/store/data/spkg-install.i
cunningham_tables-1.0/.hg/requires
cunningham_tables-1.0/.hg/dirstate
cunningham_tables-1.0/.hg/undo.dirstate
cunningham_tables-1.0/.hg/00changelog.i
cunningham_tables-1.0/.hg/branch
cunningham_tables-1.0/.hg/undo.branch
cunningham_tables-1.0/src/
cunningham_tables-1.0/src/cunningham_tables/
cunningham_tables-1.0/src/cunningham_tables/cunningham_prime_factors.sobj
cunningham_tables-1.0/spkg-install
cunningham_tables-1.0/SPKG.txt
cunningham_tables-1.0/read_cunningham_prime_factors.py
```



---

Comment by ylchapuy created at 2009-11-23 22:42:31

from Jeroen Demeyer:

"You are certainly welcome to use this data (I don't think pure data like
this can be copyrighted anyway).  I actually know about Sage (even
though I use PARI/GP myself) and certainly would like to support the
project.  It is not entirely clear what your function should do: it is
supposed to be incorporated into the general factor() function or do you
plan to add a special function somehow?  I'm just asking so that I can
help you better.

You might also want to have at my fullfactor() PARI/GP package (see
http://cage.ugent.be/~jdemeyer/parigp/fullfactor.html).  This is a
package I wrote with some helper functions for factoring (some unrelated
to the Cunningham tables).  It contains a function factor_cyclo(n) which
basically tries to find factors of cyclotomic polynomials in a given
number.  It then looks these factors up in the Cunningham tables.  It
also contains some more low-level functions to help with the
factorization of numbers of the form `b^e-1` (or divisors of these).
The code works but I admit it is not very good-looking.  Note however
that this code has been written for PARI/GP 2.4 while Sage still uses
PARI/GP 2.3 I believe.

Best regards,
Jeroen."


---

Comment by cremona created at 2009-11-23 22:48:40

Replying to [comment:9 ylchapuy]:
> the new spkg is at the same address.
> I tested it again and it works for me now.
> 
> The previous one was creating a directory named "cunningham_tables" when decompressed, then only difference with the new one is that the directory is now named "cunningham_tables-1.0".
> You might check you have the right one by trying for yourself:

OK, what was apparently happening is that when I downloaded the new file, firefox was only getting the cached version -- I had to manually clear the cache!  now I get the correct new version and it installs fine.  I will continue to review this by applying the patch, etc, soon but cannot right now.


---

Comment by cremona created at 2009-12-18 17:05:29

Changing keywords from "" to "integer factorization Cunningham".


---

Comment by cremona created at 2009-12-18 17:05:29

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2009-12-18 17:05:29

Sorry for the delay.  I have now successfully installed the spkg and applied the patch (to 4.3.rc0) and everything is working as advertised.

Question: Why the leading underscore in the method `_cunningham_prime_factors()`?  Like this the function does not show up in the reference manual or under normal tab completion, so users will not notice its existence.  Since using this is not yet blended in with any other integer factorization code, I fear that people will not genefit from this as much as they might.

As far as I can see the spkg itself has everything that it should.  So the positive reivew is for BOTH the inclusion of this as an optional spkg AND for the merging of the patch.

Now I'll go on to look at the patch which depends on this one.


---

Comment by ylchapuy created at 2009-12-18 18:29:46

The name `_factor_cunningham` was just intended to be like the existing `_factor_trial_division`.


---

Comment by cremona created at 2009-12-18 20:07:44

Replying to [comment:13 ylchapuy]:
> The name `_factor_cunningham` was just intended to be like the existing `_factor_trial_division`.

Sure -- but that is used internally by factor() so it is more reasonable to have it hidden from the user.  You could add a "use_cunningham" flag to the integer factor function?


---

Comment by rlm created at 2010-01-13 10:02:28

Resolution: fixed


---

Comment by mvngu created at 2010-01-22 17:04:32

Is the optional package [cunningham_tables-1.0.spkg](http://yann.laiglechapuy.net/spkg/cunningham_tables-1.0.spkg) meant to be in the optional spkg repository at http://www.sagemath.org/packages/optional? I don't see it there at all.


---

Comment by cremona created at 2010-01-22 17:13:49

Replying to [comment:17 mvngu]:
> Is the optional package [cunningham_tables-1.0.spkg](http://yann.laiglechapuy.net/spkg/cunningham_tables-1.0.spkg) meant to be in the optional spkg repository at http://www.sagemath.org/packages/optional? I don't see it there at all.

There's a link to it above:  can the release manager take it from there and put it in the correct place?


---

Comment by mvngu created at 2010-01-22 17:30:44

Replying to [comment:18 cremona]:
> There's a link to it above:  can the release manager take it from there and put it in the correct place?

Done. See http://www.sagemath.org/packages/optional.
