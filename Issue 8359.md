# Issue 8359: Coxeter groups as permutation groups

archive/issues_008359.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: Coxeter groups, permutation groups, chevie\n\nThis patch adds a function:\n\n```\n    CoxeterGroup(cartan_type, implementation = \"matrix\" / \"permutation\")\n``` \nto construct Coxeter groups. Whenever possible, the Coxeter group is constructed as a permutation group, using data from GAP3/Chevie; otherwise a Weyl group is returned, as a matrix group. An upcoming implementation is by reduced words, using the Coxeter 3 package.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8359\n\n",
    "closed_at": "2013-02-05T08:22:16Z",
    "created_at": "2010-02-25T08:48:26Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.7",
    "title": "Coxeter groups as permutation groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8359",
    "user": "https://github.com/nthiery"
}
```
Assignee: sage-combinat

CC:  sage-combinat

Keywords: Coxeter groups, permutation groups, chevie

This patch adds a function:

```
    CoxeterGroup(cartan_type, implementation = "matrix" / "permutation")
``` 
to construct Coxeter groups. Whenever possible, the Coxeter group is constructed as a permutation group, using data from GAP3/Chevie; otherwise a Weyl group is returned, as a matrix group. An upcoming implementation is by reduced words, using the Coxeter 3 package.

Issue created by migration from https://trac.sagemath.org/ticket/8359





---

archive/issue_comments_074559.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-01T20:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74559",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_074560.json:
```json
{
    "body": "This patch was developed and tested on the sage-combinat queue by myself and Mike Hansen. It is ready to go!",
    "created_at": "2013-01-23T15:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74560",
    "user": "https://github.com/anneschilling"
}
```

This patch was developed and tested on the sage-combinat queue by myself and Mike Hansen. It is ready to go!



---

archive/issue_comments_074561.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-01-23T15:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74561",
    "user": "https://github.com/anneschilling"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074562.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-23T15:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74562",
    "user": "https://github.com/anneschilling"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020032.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-23T15:48:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "milestone": "sage-5.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8359#event-20032"
}
```



---

archive/issue_comments_074563.json:
```json
{
    "body": "We made changes to make the doctests pass. Not sure what the problem with the plugins are.",
    "created_at": "2013-01-25T13:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74563",
    "user": "https://github.com/anneschilling"
}
```

We made changes to make the doctests pass. Not sure what the problem with the plugins are.



---

archive/issue_comments_074564.json:
```json
{
    "body": "You should never use `except:` without an exception type, otherwise you would catch some unwanted exceptions.  Catch specific exceptions instead (or `except Exception:` if you want to catch all actual exceptions).",
    "created_at": "2013-01-26T12:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74564",
    "user": "https://github.com/jdemeyer"
}
```

You should never use `except:` without an exception type, otherwise you would catch some unwanted exceptions.  Catch specific exceptions instead (or `except Exception:` if you want to catch all actual exceptions).



---

archive/issue_comments_074565.json:
```json
{
    "body": "There is a problem with the documentation:\n\n```\n/release/merger/sage-5.7.beta2/local/lib/python2.7/site-packages/sage/combinat/root_system/coxeter_group.py:docstring of sage.combinat.root_system.coxeter_group.CoxeterGroupAsPermutationGroup.Element.has_descent:3: WARNING: more than one target found for cross-reference u'descents': sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations.ElementMethods.descents, sage.categories.coxeter_groups.CoxeterGroups.ElementMethods.descents, sage.combinat.tableau.Tableau.descents, sage.combinat.sf.ns_macdonald.AugmentedLatticeDiagramFilling.descents, sage.combinat.permutation.Permutation_class.descents, sage.combinat.composition.Composition_class.descents\n```",
    "created_at": "2013-01-26T14:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74565",
    "user": "https://github.com/jdemeyer"
}
```

There is a problem with the documentation:

```
/release/merger/sage-5.7.beta2/local/lib/python2.7/site-packages/sage/combinat/root_system/coxeter_group.py:docstring of sage.combinat.root_system.coxeter_group.CoxeterGroupAsPermutationGroup.Element.has_descent:3: WARNING: more than one target found for cross-reference u'descents': sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations.ElementMethods.descents, sage.categories.coxeter_groups.CoxeterGroups.ElementMethods.descents, sage.combinat.tableau.Tableau.descents, sage.combinat.sf.ns_macdonald.AugmentedLatticeDiagramFilling.descents, sage.combinat.permutation.Permutation_class.descents, sage.combinat.composition.Composition_class.descents
```



---

archive/issue_comments_074566.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-01-26T14:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74566",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_074567.json:
```json
{
    "body": "Both issues fixed!",
    "created_at": "2013-01-26T17:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74567",
    "user": "https://github.com/anneschilling"
}
```

Both issues fixed!



---

archive/issue_comments_074568.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-01-26T17:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74568",
    "user": "https://github.com/anneschilling"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_074569.json:
```json
{
    "body": "Hi Jeroen,\n\nShould we ignore jehova's patchbot failure (the log and shortlog seem empty)?\n\nIs the plugin.startup failure a suggestion for lazy importing CoxeterGroup?\n\nThanks!\n\n               Nicolas",
    "created_at": "2013-02-01T14:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74569",
    "user": "https://github.com/nthiery"
}
```

Hi Jeroen,

Should we ignore jehova's patchbot failure (the log and shortlog seem empty)?

Is the plugin.startup failure a suggestion for lazy importing CoxeterGroup?

Thanks!

               Nicolas



---

archive/issue_comments_074570.json:
```json
{
    "body": "In consultation with Nicolas, I fixed some failing doctests in /combinat/root_systems/coxeter_group.py for type H3.\n\nAnne",
    "created_at": "2013-02-02T19:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74570",
    "user": "https://github.com/anneschilling"
}
```

In consultation with Nicolas, I fixed some failing doctests in /combinat/root_systems/coxeter_group.py for type H3.

Anne



---

archive/issue_comments_074571.json:
```json
{
    "body": "Attachment [trac_8359-coxeter-groups-permutation-nt.patch](tarball://root/attachments/some-uuid/ticket8359/trac_8359-coxeter-groups-permutation-nt.patch) by @anneschilling created at 2013-02-04 23:07:09",
    "created_at": "2013-02-04T23:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74571",
    "user": "https://github.com/anneschilling"
}
```

Attachment [trac_8359-coxeter-groups-permutation-nt.patch](tarball://root/attachments/some-uuid/ticket8359/trac_8359-coxeter-groups-permutation-nt.patch) by @anneschilling created at 2013-02-04 23:07:09



---

archive/issue_comments_074572.json:
```json
{
    "body": "Removed trailing white spaces.\n\nAnne",
    "created_at": "2013-02-04T23:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74572",
    "user": "https://github.com/anneschilling"
}
```

Removed trailing white spaces.

Anne



---

archive/issue_comments_074573.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-02-05T08:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74573",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_020033.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-02-05T08:22:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8359#event-20033"
}
```
