# Issue 6958: [with patch, not ready] prove_BSD function for elliptic curves over QQ

archive/issues_006958.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @williamstein\n\nComments welcome!\n\nIssue created by migration from https://trac.sagemath.org/ticket/6958\n\n",
    "created_at": "2009-09-19T03:13:09Z",
    "labels": [
        "component: elliptic curves"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "[with patch, not ready] prove_BSD function for elliptic curves over QQ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6958",
    "user": "https://github.com/rlmill"
}
```
Assignee: @loefflerd

CC:  @williamstein

Comments welcome!

Issue created by migration from https://trac.sagemath.org/ticket/6958





---

archive/issue_comments_057444.json:
```json
{
    "body": "Attachment [trac_6958.patch](tarball://root/attachments/some-uuid/ticket6958/trac_6958.patch) by @rlmill created at 2009-09-19 18:26:31",
    "created_at": "2009-09-19T18:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6958#issuecomment-57444",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_6958.patch](tarball://root/attachments/some-uuid/ticket6958/trac_6958.patch) by @rlmill created at 2009-09-19 18:26:31



---

archive/issue_comments_057445.json:
```json
{
    "body": "Given the nature of this function, i.e., it should never raise an exception with the default inputs, I think it should run successfully for all curves of conductor up to 100 (say) before getting into Sage.  It fails already on 11a2.\n\n\n```\nfor E in cremona_curves([1..100]+[389]):\n    print E.cremona_label(), E.prove_BSD(verbosity=2)\n```\n\n\n\n```\n11a1 p = 2: true by 2-descent\nTrue for p not in {2, 5} by Kolyvagin.\nTrue for p=5 by Mazur\n[]\n11a2 p = 2: true by 2-descent\nTrue for p not in {2, 5} by Kolyvagin.\n---------------------------------------------------------------------------\nAssertionError                            Traceback (most recent call last)\n\n/Users/wstein/.sage/temp/flat.local/1342/_Users_wstein__sage_init_sage_0.py in <module>()\n\n/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in prove_BSD(self, verbosity, simon, proof)\n   5270         # Kato's bound\n   5271         if rank == 0 and not E.has_cm():\n-> 5272             assert E.optimal_curve() == E\n   5273             L_over_Omega = E.lseries().L_ratio()\n   5274             kato_primes = Sha.bound_kato()\n\nAssertionError: \n```\n\n\nAlso, I think the fix for the above is to just switch to the optimal curve.  \n\nOK, done by changing the code that raises the error to:\n\n```\n            # We can replace E by the corresponding optimal curve without changing truth\n            # of BSD at p.\n            E = E.optimal_curve()\n```\n\n\nA quicker test once we always first switch to the optimal curve is to do:\n\n```\nfor E in cremona_optimal_curves([1..100]):\n    print E.cremona_label()\n    try:\n        E.prove_BSD(verbosity=2)\n    except Exception, msg:\n        print \"** problem !!\", msg\n```\n\n\nThis test passes right now up to 91, then this hangs forever (=15 minutes):\n\n```\n90c1\np = 2: true by 2-descent\nTrue for p not in {2, 3} by Kolyvagin.\n...\n```\n\n\nWith set_verbose(2) we see that:\n\n```\nTrue for p not in {2, 3} by Kolyvagin.\nverbose 1 (6244: heegner.py, heegner_index) computing heegner point height...\nverbose 1 (6244: heegner.py, heegner_index) Height of heegner point = 41.383? (time = 0.195229)\nverbose 1 (6244: heegner.py, heegner_index) Heegner height bound = 41.384\nverbose 1 (6244: heegner.py, heegner_index) CPS bound = 8.48553581472\nverbose 1 (6244: heegner.py, heegner_index) Search would have to be up to height = 18.832\nverbose 1 (6244: heegner.py, heegner_index) doing point search\n...\n```\n\nso doing the index bound as a future patch is the way to go.",
    "created_at": "2009-09-19T22:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6958#issuecomment-57445",
    "user": "https://github.com/williamstein"
}
```

Given the nature of this function, i.e., it should never raise an exception with the default inputs, I think it should run successfully for all curves of conductor up to 100 (say) before getting into Sage.  It fails already on 11a2.


```
for E in cremona_curves([1..100]+[389]):
    print E.cremona_label(), E.prove_BSD(verbosity=2)
```



```
11a1 p = 2: true by 2-descent
True for p not in {2, 5} by Kolyvagin.
True for p=5 by Mazur
[]
11a2 p = 2: true by 2-descent
True for p not in {2, 5} by Kolyvagin.
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

/Users/wstein/.sage/temp/flat.local/1342/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in prove_BSD(self, verbosity, simon, proof)
   5270         # Kato's bound
   5271         if rank == 0 and not E.has_cm():
-> 5272             assert E.optimal_curve() == E
   5273             L_over_Omega = E.lseries().L_ratio()
   5274             kato_primes = Sha.bound_kato()

AssertionError: 
```


Also, I think the fix for the above is to just switch to the optimal curve.  

OK, done by changing the code that raises the error to:

```
            # We can replace E by the corresponding optimal curve without changing truth
            # of BSD at p.
            E = E.optimal_curve()
```


A quicker test once we always first switch to the optimal curve is to do:

```
for E in cremona_optimal_curves([1..100]):
    print E.cremona_label()
    try:
        E.prove_BSD(verbosity=2)
    except Exception, msg:
        print "** problem !!", msg
```


This test passes right now up to 91, then this hangs forever (=15 minutes):

```
90c1
p = 2: true by 2-descent
True for p not in {2, 3} by Kolyvagin.
...
```


With set_verbose(2) we see that:

```
True for p not in {2, 3} by Kolyvagin.
verbose 1 (6244: heegner.py, heegner_index) computing heegner point height...
verbose 1 (6244: heegner.py, heegner_index) Height of heegner point = 41.383? (time = 0.195229)
verbose 1 (6244: heegner.py, heegner_index) Heegner height bound = 41.384
verbose 1 (6244: heegner.py, heegner_index) CPS bound = 8.48553581472
verbose 1 (6244: heegner.py, heegner_index) Search would have to be up to height = 18.832
verbose 1 (6244: heegner.py, heegner_index) doing point search
...
```

so doing the index bound as a future patch is the way to go.



---

archive/issue_comments_057446.json:
```json
{
    "body": "Attachment [trac-6958-referee_followup.patch](tarball://root/attachments/some-uuid/ticket6958/trac-6958-referee_followup.patch) by @rlmill created at 2009-09-19 22:38:57\n\nFor the second patch, proof=False and proof=True are reversed for the doctest on 389a.",
    "created_at": "2009-09-19T22:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6958#issuecomment-57446",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac-6958-referee_followup.patch](tarball://root/attachments/some-uuid/ticket6958/trac-6958-referee_followup.patch) by @rlmill created at 2009-09-19 22:38:57

For the second patch, proof=False and proof=True are reversed for the doctest on 389a.



---

archive/issue_comments_057447.json:
```json
{
    "body": "OK, William agrees to my fixes and I to his. Positive review!",
    "created_at": "2009-09-19T22:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6958#issuecomment-57447",
    "user": "https://github.com/rlmill"
}
```

OK, William agrees to my fixes and I to his. Positive review!



---

archive/issue_comments_057448.json:
```json
{
    "body": "The patch `trac_6958-typos_followup.patch` results in a hunk failure:\n\n```\n[mvngu@mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6958/trac_6958-typos_followup.patch && hg qpush\nadding trac_6958-typos_followup.patch to series file\napplying trac_6958-typos_followup.patch\npatching file sage/schemes/elliptic_curves/ell_rational_field.py\nHunk #1 FAILED at 5688\n1 out of 5 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_rational_field.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nErrors during apply, please fix and refresh trac_6958-typos_followup.patch\n```\n",
    "created_at": "2009-09-24T15:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6958#issuecomment-57448",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch `trac_6958-typos_followup.patch` results in a hunk failure:

```
[mvngu@mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6958/trac_6958-typos_followup.patch && hg qpush
adding trac_6958-typos_followup.patch to series file
applying trac_6958-typos_followup.patch
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #1 FAILED at 5688
1 out of 5 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_rational_field.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_6958-typos_followup.patch
```




---

archive/issue_comments_057449.json:
```json
{
    "body": "Attachment [trac_6958-typos_followup.patch](tarball://root/attachments/some-uuid/ticket6958/trac_6958-typos_followup.patch) by @mwhansen created at 2009-10-05 07:03:29",
    "created_at": "2009-10-05T07:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6958#issuecomment-57449",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6958-typos_followup.patch](tarball://root/attachments/some-uuid/ticket6958/trac_6958-typos_followup.patch) by @mwhansen created at 2009-10-05 07:03:29



---

archive/issue_comments_057450.json:
```json
{
    "body": "I've attached a new version of `trac_6958-typos_followup.patch` which removes the failing hunk since the doctest that it changed had been removed.",
    "created_at": "2009-10-05T07:04:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6958#issuecomment-57450",
    "user": "https://github.com/mwhansen"
}
```

I've attached a new version of `trac_6958-typos_followup.patch` which removes the failing hunk since the doctest that it changed had been removed.



---

archive/issue_comments_057451.json:
```json
{
    "body": "Remove assignee @loefflerd.",
    "created_at": "2009-10-09T09:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6958#issuecomment-57451",
    "user": "https://github.com/loefflerd"
}
```

Remove assignee @loefflerd.



---

archive/issue_comments_057452.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T16:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6958#issuecomment-57452",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007182.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-10-15T16:13:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6958",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6958#event-7182"
}
```
