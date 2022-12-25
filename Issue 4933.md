# Issue 4933: lots of files in sage.schemes.elliptic_curves are not included in the reference manual

archive/issues_004933.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: documentation\n\nThe following files have useful docstrings but are not included in the ref manual (judging from 3.2.3), all in sage.schemes.elliptic_curves.\n* cm.py\n* ec_database.py\n* ell_field.py\n* ell_local_data.py\n* ell_modular_symbols\n* ell_number_field\n* ell_padic_field\n* ell_point.py\n* ell_tate_curve.py\n* ell_torsion.py\n* kodaira_symbol.py\n* lseries_ell.py\n* padic_lseries.py\n* period_lattice.py\n* sha_tate.py\n* weierstrass_morphism.py\n\nIssue created by migration from https://trac.sagemath.org/ticket/4933\n\n",
    "created_at": "2009-01-03T17:59:06Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "lots of files in sage.schemes.elliptic_curves are not included in the reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4933",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: tba

Keywords: documentation

The following files have useful docstrings but are not included in the ref manual (judging from 3.2.3), all in sage.schemes.elliptic_curves.
* cm.py
* ec_database.py
* ell_field.py
* ell_local_data.py
* ell_modular_symbols
* ell_number_field
* ell_padic_field
* ell_point.py
* ell_tate_curve.py
* ell_torsion.py
* kodaira_symbol.py
* lseries_ell.py
* padic_lseries.py
* period_lattice.py
* sha_tate.py
* weierstrass_morphism.py

Issue created by migration from https://trac.sagemath.org/ticket/4933





---

archive/issue_comments_037363.json:
```json
{
    "body": "Hi,\n\nthe files\n\n* ell_modular_symbols.py\n* ell_tate_curve.py\n* padic_lseries.py\n* sha_tate.py\n\nare not only enhanced in a vital way but also considerably cleaned up docstring- and comment-wise by #4667. The patch there is currently based against 3.3 and needs a rebase concerning two files (ell_rational_field.py, padocs.py) against 3.4 series, and there is still one doctest failure, but nevertheless I do consider #4667 worth of applying before working on this very ticket here!",
    "created_at": "2009-02-25T21:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37363",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Hi,

the files

* ell_modular_symbols.py
* ell_tate_curve.py
* padic_lseries.py
* sha_tate.py

are not only enhanced in a vital way but also considerably cleaned up docstring- and comment-wise by #4667. The patch there is currently based against 3.3 and needs a rebase concerning two files (ell_rational_field.py, padocs.py) against 3.4 series, and there is still one doctest failure, but nevertheless I do consider #4667 worth of applying before working on this very ticket here!



---

archive/issue_comments_037364.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37364",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_037365.json:
```json
{
    "body": "Attachment [trac_4933-1.patch](tarball://root/attachments/some-uuid/ticket4933/trac_4933-1.patch) by @JohnCremona created at 2009-04-15 16:26:46",
    "created_at": "2009-04-15T16:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37365",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_4933-1.patch](tarball://root/attachments/some-uuid/ticket4933/trac_4933-1.patch) by @JohnCremona created at 2009-04-15 16:26:46



---

archive/issue_comments_037366.json:
```json
{
    "body": "I have attached a patch trac_4933-1.patch which does this for three files:\n* ell_number_field.py\n* ell_torsion.py\n* ell_point.py\nwhich is a start.\n\nThe patch rewrites all the docstrings in those files and also adds them to the list of files which are processed by \"sage -docbuild reference\" so that they show up in the reference manual.\n\nTo review/test the patch (which was based on 3.4.1.rc2), you need to apply it and rebuild, and then (1) do  \"sage -t\" is usual on the files affected, and (2) do \"sage -docbuild reference pdf/html/whatever\" to check that the documentation looks good.",
    "created_at": "2009-04-15T16:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37366",
    "user": "https://github.com/JohnCremona"
}
```

I have attached a patch trac_4933-1.patch which does this for three files:
* ell_number_field.py
* ell_torsion.py
* ell_point.py
which is a start.

The patch rewrites all the docstrings in those files and also adds them to the list of files which are processed by "sage -docbuild reference" so that they show up in the reference manual.

To review/test the patch (which was based on 3.4.1.rc2), you need to apply it and rebuild, and then (1) do  "sage -t" is usual on the files affected, and (2) do "sage -docbuild reference pdf/html/whatever" to check that the documentation looks good.



---

archive/issue_comments_037367.json:
```json
{
    "body": "Attachment [trac_4933-2.patch](tarball://root/attachments/some-uuid/ticket4933/trac_4933-2.patch) by @JohnCremona created at 2009-04-16 16:35:28\n\nTwo more;  apply after previous.",
    "created_at": "2009-04-16T16:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37367",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_4933-2.patch](tarball://root/attachments/some-uuid/ticket4933/trac_4933-2.patch) by @JohnCremona created at 2009-04-16 16:35:28

Two more;  apply after previous.



---

archive/issue_comments_037368.json:
```json
{
    "body": "The second patch adds a couple more files (weierstrass_morphism and period_lattice).",
    "created_at": "2009-04-16T16:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37368",
    "user": "https://github.com/JohnCremona"
}
```

The second patch adds a couple more files (weierstrass_morphism and period_lattice).



---

archive/issue_comments_037369.json:
```json
{
    "body": "Attachment [trac_4933-3.patch](tarball://root/attachments/some-uuid/ticket4933/trac_4933-3.patch) by @JohnCremona created at 2009-04-17 14:02:20\n\nIGNORE all previous patches.  This is based on 3.4.1.rc3",
    "created_at": "2009-04-17T14:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37369",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_4933-3.patch](tarball://root/attachments/some-uuid/ticket4933/trac_4933-3.patch) by @JohnCremona created at 2009-04-17 14:02:20

IGNORE all previous patches.  This is based on 3.4.1.rc3



---

archive/issue_comments_037370.json:
```json
{
    "body": "Changing keywords from \"documentation\" to \"documentation, elliptic curves\".",
    "created_at": "2009-04-17T14:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37370",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "documentation" to "documentation, elliptic curves".



---

archive/issue_comments_037371.json:
```json
{
    "body": "The patch trac_4933-3.patch converts the following to rest/sphinx and adds them to the reference manual:\n* ell_number_field\n* ell_local_data\n* ell_torsion\n* ell_point\n* period_lattice\n* weierstrass_morphism\nas well as fixing some glitches in other files (notable ell_rational_field) and adding a few doctests.\n\nAlmost all the changes are in docstrings.  To review this you'll have to build the docs (reference manual) and eyeball the output.\n\nNB I combined more than one earlier patch into one, but failed to get \"sage -hg qfold\" to work, so i nthe patch there are liable to be more than one chunk for each file.",
    "created_at": "2009-04-17T14:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37371",
    "user": "https://github.com/JohnCremona"
}
```

The patch trac_4933-3.patch converts the following to rest/sphinx and adds them to the reference manual:
* ell_number_field
* ell_local_data
* ell_torsion
* ell_point
* period_lattice
* weierstrass_morphism
as well as fixing some glitches in other files (notable ell_rational_field) and adding a few doctests.

Almost all the changes are in docstrings.  To review this you'll have to build the docs (reference manual) and eyeball the output.

NB I combined more than one earlier patch into one, but failed to get "sage -hg qfold" to work, so i nthe patch there are liable to be more than one chunk for each file.



---

archive/issue_comments_037372.json:
```json
{
    "body": "If you're patching ell_rational_field, can you fix the doc string for mwrank?  It looks pretty garbled to me, and I don't know what it's supposed to say...",
    "created_at": "2009-04-17T14:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37372",
    "user": "https://github.com/jhpalmieri"
}
```

If you're patching ell_rational_field, can you fix the doc string for mwrank?  It looks pretty garbled to me, and I don't know what it's supposed to say...



---

archive/issue_comments_037373.json:
```json
{
    "body": "Replying to [comment:7 jhpalmieri]:\n> If you're patching ell_rational_field, can you fix the doc string for mwrank?  It looks pretty garbled to me, and I don't know what it's supposed to say...\n\nIt looks pretty clear to me, except perhaps where it explains the format of the options string.  Perhaps we should just include the output of \"sage -mwrank -h\":\n\n```\nmwrank command line options (can be in any order):\n\n-h      help            prints this info and quits\n-q      quiet           turns OFF banner display\n-v n    verbosity       sets verbosity to n (default=1)\n-o      PARI/GP output  turns ON extra PARI/GP short output (default is OFF)\n-p n    precision       sets precision to n decimals (default=15)\n                        (irrelevant unless compiled with multiprecision option)\n-b n    quartic bound   bound on quartic point search (default=10)\n-x n    n aux           number of aux primes used for sieving (default=6)\n-l      list            turns ON listing of points (default ON unless v=0)\n-t      trace           turns ON trace of quartic equivalence testing (debugging only)\n-s      selmer_only     if set, computes Selmer rank only (default: not set)\n-d      skip_2nd_descent        if set, skips the second descent for curves with 2-torsion (default: not set)\n-S n    sat_bd          upper bound on saturation primes (default=100, -1 for automatic)\n```\n",
    "created_at": "2009-04-17T14:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37373",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:7 jhpalmieri]:
> If you're patching ell_rational_field, can you fix the doc string for mwrank?  It looks pretty garbled to me, and I don't know what it's supposed to say...

It looks pretty clear to me, except perhaps where it explains the format of the options string.  Perhaps we should just include the output of "sage -mwrank -h":

```
mwrank command line options (can be in any order):

-h      help            prints this info and quits
-q      quiet           turns OFF banner display
-v n    verbosity       sets verbosity to n (default=1)
-o      PARI/GP output  turns ON extra PARI/GP short output (default is OFF)
-p n    precision       sets precision to n decimals (default=15)
                        (irrelevant unless compiled with multiprecision option)
-b n    quartic bound   bound on quartic point search (default=10)
-x n    n aux           number of aux primes used for sieving (default=6)
-l      list            turns ON listing of points (default ON unless v=0)
-t      trace           turns ON trace of quartic equivalence testing (debugging only)
-s      selmer_only     if set, computes Selmer rank only (default: not set)
-d      skip_2nd_descent        if set, skips the second descent for curves with 2-torsion (default: not set)
-S n    sat_bd          upper bound on saturation primes (default=100, -1 for automatic)
```




---

archive/issue_comments_037374.json:
```json
{
    "body": ">It looks pretty clear to me, except perhaps where it explains the format of the options string. \n\nDo you mean this part?\n\n``` \n        -  ``options`` - string; passed when starting mwrank.\n           The format is q pprecision vverbosity bhlim_q xnaux chlim_c l t o\n           s d]\n```\n",
    "created_at": "2009-04-17T15:13:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37374",
    "user": "https://github.com/jhpalmieri"
}
```

>It looks pretty clear to me, except perhaps where it explains the format of the options string. 

Do you mean this part?

``` 
        -  ``options`` - string; passed when starting mwrank.
           The format is q pprecision vverbosity bhlim_q xnaux chlim_c l t o
           s d]
```




---

archive/issue_comments_037375.json:
```json
{
    "body": "Replying to [comment:9 jhpalmieri]:\n> >It looks pretty clear to me, except perhaps where it explains the format of the options string. \n> \n> Do you mean this part?\n> {{{ \n>         -  ``options`` - string; passed when starting mwrank.\n>            The format is q pprecision vverbosity bhlim_q xnaux chlim_c l t o\n>            s d]\n> }}}\nYes!",
    "created_at": "2009-04-17T15:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37375",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:9 jhpalmieri]:
> >It looks pretty clear to me, except perhaps where it explains the format of the options string. 
> 
> Do you mean this part?
> {{{ 
>         -  ``options`` - string; passed when starting mwrank.
>            The format is q pprecision vverbosity bhlim_q xnaux chlim_c l t o
>            s d]
> }}}
Yes!



---

archive/issue_comments_037376.json:
```json
{
    "body": "Attachment [trac_4933-3-rebase.patch](tarball://root/attachments/some-uuid/ticket4933/trac_4933-3-rebase.patch) by @JohnCremona created at 2009-04-17 15:52:59\n\nReplaces previous;  based on 3.4.1.rc3 + #5808 patch",
    "created_at": "2009-04-17T15:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37376",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_4933-3-rebase.patch](tarball://root/attachments/some-uuid/ticket4933/trac_4933-3-rebase.patch) by @JohnCremona created at 2009-04-17 15:52:59

Replaces previous;  based on 3.4.1.rc3 + #5808 patch



---

archive/issue_comments_037377.json:
```json
{
    "body": "The new patch (trac_4933-3-rebase.patch) replaces the earlier one as it applies cleanly to 3.4.1.rc3 + ref-warnings.patch from #5808.  It also answers John Palmieri's request to make the docstring for mwrank() less confusing.\n\nI think the reason that this one is smaller is that the previous one applied several patches in succession to the same files, while this one does not.  At least, I hope that is the reason.",
    "created_at": "2009-04-17T15:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37377",
    "user": "https://github.com/JohnCremona"
}
```

The new patch (trac_4933-3-rebase.patch) replaces the earlier one as it applies cleanly to 3.4.1.rc3 + ref-warnings.patch from #5808.  It also answers John Palmieri's request to make the docstring for mwrank() less confusing.

I think the reason that this one is smaller is that the previous one applied several patches in succession to the same files, while this one does not.  At least, I hope that is the reason.



---

archive/issue_comments_037378.json:
```json
{
    "body": "Code looks good, all tests pass, the reference manual looks nice. I'm attaching a referee's patch with two very small changes.",
    "created_at": "2009-04-17T21:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37378",
    "user": "https://github.com/jhpalmieri"
}
```

Code looks good, all tests pass, the reference manual looks nice. I'm attaching a referee's patch with two very small changes.



---

archive/issue_comments_037379.json:
```json
{
    "body": "apply on top of the other patch",
    "created_at": "2009-04-17T21:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37379",
    "user": "https://github.com/jhpalmieri"
}
```

apply on top of the other patch



---

archive/issue_comments_037380.json:
```json
{
    "body": "Attachment [4933-ref.patch](tarball://root/attachments/some-uuid/ticket4933/4933-ref.patch) by @JohnCremona created at 2009-04-17 22:17:00\n\nReplying to [comment:12 jhpalmieri]:\n> Code looks good, all tests pass, the reference manual looks nice. I'm attaching a referee's patch with two very small changes.\n\nThanks John -- I am quite happy with your adjustments.",
    "created_at": "2009-04-17T22:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37380",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [4933-ref.patch](tarball://root/attachments/some-uuid/ticket4933/4933-ref.patch) by @JohnCremona created at 2009-04-17 22:17:00

Replying to [comment:12 jhpalmieri]:
> Code looks good, all tests pass, the reference manual looks nice. I'm attaching a referee's patch with two very small changes.

Thanks John -- I am quite happy with your adjustments.



---

archive/issue_comments_037381.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-18T01:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37381",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037382.json:
```json
{
    "body": "Merged  trac_4933-3-rebase.patch and 4933-ref.patch in Sage 3.4.1.rc4.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T01:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37382",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged  trac_4933-3-rebase.patch and 4933-ref.patch in Sage 3.4.1.rc4.

Cheers,

Michael



---

archive/issue_comments_037383.json:
```json
{
    "body": "This is continued in #5851.",
    "created_at": "2009-04-22T10:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4933#issuecomment-37383",
    "user": "https://github.com/JohnCremona"
}
```

This is continued in #5851.
