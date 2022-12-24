# Issue 7239: factorization of Cunningham numbers

archive/issues_007239.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mvngu\n\nA small spkg to provide factorization of Cunningham numbers.\n\nThe raw data is from http://cage.ugent.be/~jdemeyer/cunningham\n\nIssue created by migration from https://trac.sagemath.org/ticket/7239\n\n",
    "created_at": "2009-10-18T10:27:05Z",
    "labels": [
        "factorization",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "factorization of Cunningham numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7239",
    "user": "ylchapuy"
}
```
Assignee: tbd

CC:  mvngu

A small spkg to provide factorization of Cunningham numbers.

The raw data is from http://cage.ugent.be/~jdemeyer/cunningham

Issue created by migration from https://trac.sagemath.org/ticket/7239





---

archive/issue_comments_060053.json:
```json
{
    "body": "The package is here: http://yann.laiglechapuy.net/spkg/cunningham_tables-1.0.spkg",
    "created_at": "2009-10-18T10:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60053",
    "user": "ylchapuy"
}
```

The package is here: http://yann.laiglechapuy.net/spkg/cunningham_tables-1.0.spkg



---

archive/issue_comments_060054.json:
```json
{
    "body": "Attachment [trac7239_Cunningham_factorization.patch](tarball://root/attachments/some-uuid/ticket7239/trac7239_Cunningham_factorization.patch) by ylchapuy created at 2009-10-18 11:32:35\n\nbased on 4.1.2",
    "created_at": "2009-10-18T11:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60054",
    "user": "ylchapuy"
}
```

Attachment [trac7239_Cunningham_factorization.patch](tarball://root/attachments/some-uuid/ticket7239/trac7239_Cunningham_factorization.patch) by ylchapuy created at 2009-10-18 11:32:35

based on 4.1.2



---

archive/issue_comments_060055.json:
```json
{
    "body": "mvngu, I add cc'ed you as you were interested in ticket #191",
    "created_at": "2009-10-19T22:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60055",
    "user": "ylchapuy"
}
```

mvngu, I add cc'ed you as you were interested in ticket #191



---

archive/issue_comments_060056.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-26T21:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60056",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060057.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-22T17:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60057",
    "user": "cremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060058.json:
```json
{
    "body": "I tried to install using \"sage -i cunningham_tables-1.0.spkg\" after downloading it, but I had error messages:\n\n```\n...\nFinished extraction\nsage: After decompressing the directory cunningham_tables-1.0 does not exist\nThis means that the corresponding .spkg needs to be downloaded\n...\n```\n\nShould I have applied the patch first?  It would help to give more detailed instructions!\n\nSeparate question:  did you ask Jeroen Demeyer about using his data?",
    "created_at": "2009-11-22T17:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60058",
    "user": "cremona"
}
```

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

archive/issue_comments_060059.json:
```json
{
    "body": "Concerning the package, the failure was of course due to a silly mistake I made. The new spkg should work.\n\nthe procedure you tried was the good one:\n\n* download the spkg\n* install it with `sage -i cunningham_tables-1.0.spkg`\n* apply the patch\n\nConcerning the author of the data I used, I just wrote him an email to ask for an \"official\"comment on this use of the data he collected and will send his answer as soon as I get it.",
    "created_at": "2009-11-23T19:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60059",
    "user": "ylchapuy"
}
```

Concerning the package, the failure was of course due to a silly mistake I made. The new spkg should work.

the procedure you tried was the good one:

* download the spkg
* install it with `sage -i cunningham_tables-1.0.spkg`
* apply the patch

Concerning the author of the data I used, I just wrote him an email to ask for an "official"comment on this use of the data he collected and will send his answer as soon as I get it.



---

archive/issue_comments_060060.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-23T19:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60060",
    "user": "ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060061.json:
```json
{
    "body": "Where is the \"new\" spkg?  Is it still called cunningham_tables-1.0.spkg?  I downloaded it (again, assuming it had changed) but the same thing happened.\n\nI expect Jeroen will be amenable (if necessary I could also ask him as I know him).",
    "created_at": "2009-11-23T20:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60061",
    "user": "cremona"
}
```

Where is the "new" spkg?  Is it still called cunningham_tables-1.0.spkg?  I downloaded it (again, assuming it had changed) but the same thing happened.

I expect Jeroen will be amenable (if necessary I could also ask him as I know him).



---

archive/issue_comments_060062.json:
```json
{
    "body": "the new spkg is at the same address.\nI tested it again and it works for me now.\n\nThe previous one was creating a directory named \"cunningham_tables\" when decompressed, then only difference with the new one is that the directory is now named \"cunningham_tables-1.0\".\nYou might check you have the right one by trying for yourself:\n\n`tar tjf cunningham_tables-1.0.spkg` should answer\n\n```\ncunningham_tables-1.0/\ncunningham_tables-1.0/.hg/\ncunningham_tables-1.0/.hg/store/\ncunningham_tables-1.0/.hg/store/fncache\ncunningham_tables-1.0/.hg/store/undo\ncunningham_tables-1.0/.hg/store/00manifest.i\ncunningham_tables-1.0/.hg/store/00changelog.i\ncunningham_tables-1.0/.hg/store/data/\ncunningham_tables-1.0/.hg/store/data/_s_p_k_g.txt.i\ncunningham_tables-1.0/.hg/store/data/read__cunningham__prime__factors.py.i\ncunningham_tables-1.0/.hg/store/data/spkg-install.i\ncunningham_tables-1.0/.hg/requires\ncunningham_tables-1.0/.hg/dirstate\ncunningham_tables-1.0/.hg/undo.dirstate\ncunningham_tables-1.0/.hg/00changelog.i\ncunningham_tables-1.0/.hg/branch\ncunningham_tables-1.0/.hg/undo.branch\ncunningham_tables-1.0/src/\ncunningham_tables-1.0/src/cunningham_tables/\ncunningham_tables-1.0/src/cunningham_tables/cunningham_prime_factors.sobj\ncunningham_tables-1.0/spkg-install\ncunningham_tables-1.0/SPKG.txt\ncunningham_tables-1.0/read_cunningham_prime_factors.py\n```\n",
    "created_at": "2009-11-23T21:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60062",
    "user": "ylchapuy"
}
```

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

archive/issue_comments_060063.json:
```json
{
    "body": "from Jeroen Demeyer:\n\n\"You are certainly welcome to use this data (I don't think pure data like\nthis can be copyrighted anyway).  I actually know about Sage (even\nthough I use PARI/GP myself) and certainly would like to support the\nproject.  It is not entirely clear what your function should do: it is\nsupposed to be incorporated into the general factor() function or do you\nplan to add a special function somehow?  I'm just asking so that I can\nhelp you better.\n\nYou might also want to have at my fullfactor() PARI/GP package (see\nhttp://cage.ugent.be/~jdemeyer/parigp/fullfactor.html).  This is a\npackage I wrote with some helper functions for factoring (some unrelated\nto the Cunningham tables).  It contains a function factor_cyclo(n) which\nbasically tries to find factors of cyclotomic polynomials in a given\nnumber.  It then looks these factors up in the Cunningham tables.  It\nalso contains some more low-level functions to help with the\nfactorization of numbers of the form `b^e-1` (or divisors of these).\nThe code works but I admit it is not very good-looking.  Note however\nthat this code has been written for PARI/GP 2.4 while Sage still uses\nPARI/GP 2.3 I believe.\n\nBest regards,\nJeroen.\"",
    "created_at": "2009-11-23T22:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60063",
    "user": "ylchapuy"
}
```

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

archive/issue_comments_060064.json:
```json
{
    "body": "Replying to [comment:9 ylchapuy]:\n> the new spkg is at the same address.\n> I tested it again and it works for me now.\n> \n> The previous one was creating a directory named \"cunningham_tables\" when decompressed, then only difference with the new one is that the directory is now named \"cunningham_tables-1.0\".\n> You might check you have the right one by trying for yourself:\n\nOK, what was apparently happening is that when I downloaded the new file, firefox was only getting the cached version -- I had to manually clear the cache!  now I get the correct new version and it installs fine.  I will continue to review this by applying the patch, etc, soon but cannot right now.",
    "created_at": "2009-11-23T22:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60064",
    "user": "cremona"
}
```

Replying to [comment:9 ylchapuy]:
> the new spkg is at the same address.
> I tested it again and it works for me now.
> 
> The previous one was creating a directory named "cunningham_tables" when decompressed, then only difference with the new one is that the directory is now named "cunningham_tables-1.0".
> You might check you have the right one by trying for yourself:

OK, what was apparently happening is that when I downloaded the new file, firefox was only getting the cached version -- I had to manually clear the cache!  now I get the correct new version and it installs fine.  I will continue to review this by applying the patch, etc, soon but cannot right now.



---

archive/issue_comments_060065.json:
```json
{
    "body": "Changing keywords from \"\" to \"integer factorization Cunningham\".",
    "created_at": "2009-12-18T17:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60065",
    "user": "cremona"
}
```

Changing keywords from "" to "integer factorization Cunningham".



---

archive/issue_comments_060066.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-18T17:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60066",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060067.json:
```json
{
    "body": "Sorry for the delay.  I have now successfully installed the spkg and applied the patch (to 4.3.rc0) and everything is working as advertised.\n\nQuestion: Why the leading underscore in the method `_cunningham_prime_factors()`?  Like this the function does not show up in the reference manual or under normal tab completion, so users will not notice its existence.  Since using this is not yet blended in with any other integer factorization code, I fear that people will not genefit from this as much as they might.\n\nAs far as I can see the spkg itself has everything that it should.  So the positive reivew is for BOTH the inclusion of this as an optional spkg AND for the merging of the patch.\n\nNow I'll go on to look at the patch which depends on this one.",
    "created_at": "2009-12-18T17:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60067",
    "user": "cremona"
}
```

Sorry for the delay.  I have now successfully installed the spkg and applied the patch (to 4.3.rc0) and everything is working as advertised.

Question: Why the leading underscore in the method `_cunningham_prime_factors()`?  Like this the function does not show up in the reference manual or under normal tab completion, so users will not notice its existence.  Since using this is not yet blended in with any other integer factorization code, I fear that people will not genefit from this as much as they might.

As far as I can see the spkg itself has everything that it should.  So the positive reivew is for BOTH the inclusion of this as an optional spkg AND for the merging of the patch.

Now I'll go on to look at the patch which depends on this one.



---

archive/issue_comments_060068.json:
```json
{
    "body": "The name `_factor_cunningham` was just intended to be like the existing `_factor_trial_division`.",
    "created_at": "2009-12-18T18:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60068",
    "user": "ylchapuy"
}
```

The name `_factor_cunningham` was just intended to be like the existing `_factor_trial_division`.



---

archive/issue_comments_060069.json:
```json
{
    "body": "Replying to [comment:13 ylchapuy]:\n> The name `_factor_cunningham` was just intended to be like the existing `_factor_trial_division`.\n\nSure -- but that is used internally by factor() so it is more reasonable to have it hidden from the user.  You could add a \"use_cunningham\" flag to the integer factor function?",
    "created_at": "2009-12-18T20:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60069",
    "user": "cremona"
}
```

Replying to [comment:13 ylchapuy]:
> The name `_factor_cunningham` was just intended to be like the existing `_factor_trial_division`.

Sure -- but that is used internally by factor() so it is more reasonable to have it hidden from the user.  You could add a "use_cunningham" flag to the integer factor function?



---

archive/issue_comments_060070.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T10:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60070",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_060071.json:
```json
{
    "body": "Is the optional package [cunningham_tables-1.0.spkg](http://yann.laiglechapuy.net/spkg/cunningham_tables-1.0.spkg) meant to be in the optional spkg repository at http://www.sagemath.org/packages/optional? I don't see it there at all.",
    "created_at": "2010-01-22T17:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60071",
    "user": "mvngu"
}
```

Is the optional package [cunningham_tables-1.0.spkg](http://yann.laiglechapuy.net/spkg/cunningham_tables-1.0.spkg) meant to be in the optional spkg repository at http://www.sagemath.org/packages/optional? I don't see it there at all.



---

archive/issue_comments_060072.json:
```json
{
    "body": "Replying to [comment:17 mvngu]:\n> Is the optional package [cunningham_tables-1.0.spkg](http://yann.laiglechapuy.net/spkg/cunningham_tables-1.0.spkg) meant to be in the optional spkg repository at http://www.sagemath.org/packages/optional? I don't see it there at all.\n\nThere's a link to it above:  can the release manager take it from there and put it in the correct place?",
    "created_at": "2010-01-22T17:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60072",
    "user": "cremona"
}
```

Replying to [comment:17 mvngu]:
> Is the optional package [cunningham_tables-1.0.spkg](http://yann.laiglechapuy.net/spkg/cunningham_tables-1.0.spkg) meant to be in the optional spkg repository at http://www.sagemath.org/packages/optional? I don't see it there at all.

There's a link to it above:  can the release manager take it from there and put it in the correct place?



---

archive/issue_comments_060073.json:
```json
{
    "body": "Replying to [comment:18 cremona]:\n> There's a link to it above:  can the release manager take it from there and put it in the correct place?\n\nDone. See http://www.sagemath.org/packages/optional.",
    "created_at": "2010-01-22T17:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7239#issuecomment-60073",
    "user": "mvngu"
}
```

Replying to [comment:18 cremona]:
> There's a link to it above:  can the release manager take it from there and put it in the correct place?

Done. See http://www.sagemath.org/packages/optional.
