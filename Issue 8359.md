# Issue 8359: Coxeter groups as permutation groups

archive/issues_008359.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: Coxeter groups, permutation groups, chevie\n\nPatch in dev on the sage-combinat server\n\nIssue created by migration from https://trac.sagemath.org/ticket/8359\n\n",
    "created_at": "2010-02-25T08:48:26Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Coxeter groups as permutation groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8359",
    "user": "nthiery"
}
```
Assignee: sage-combinat

CC:  sage-combinat

Keywords: Coxeter groups, permutation groups, chevie

Patch in dev on the sage-combinat server

Issue created by migration from https://trac.sagemath.org/ticket/8359





---

archive/issue_comments_074683.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-01T20:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74683",
    "user": "nthiery"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_074684.json:
```json
{
    "body": "This patch was developed and tested on the sage-combinat queue by myself and Mike Hansen. It is ready to go!",
    "created_at": "2013-01-23T15:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74684",
    "user": "aschilling"
}
```

This patch was developed and tested on the sage-combinat queue by myself and Mike Hansen. It is ready to go!



---

archive/issue_comments_074685.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-01-23T15:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74685",
    "user": "aschilling"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074686.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-23T15:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74686",
    "user": "aschilling"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074687.json:
```json
{
    "body": "We made changes to make the doctests pass. Not sure what the problem with the plugins are.",
    "created_at": "2013-01-25T13:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74687",
    "user": "aschilling"
}
```

We made changes to make the doctests pass. Not sure what the problem with the plugins are.



---

archive/issue_comments_074688.json:
```json
{
    "body": "You should never use `except:` without an exception type, otherwise you would catch some unwanted exceptions.  Catch specific exceptions instead (or `except Exception:` if you want to catch all actual exceptions).",
    "created_at": "2013-01-26T12:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74688",
    "user": "jdemeyer"
}
```

You should never use `except:` without an exception type, otherwise you would catch some unwanted exceptions.  Catch specific exceptions instead (or `except Exception:` if you want to catch all actual exceptions).



---

archive/issue_comments_074689.json:
```json
{
    "body": "There is a problem with the documentation:\n\n```\n/release/merger/sage-5.7.beta2/local/lib/python2.7/site-packages/sage/combinat/root_system/coxeter_group.py:docstring of sage.combinat.root_system.coxeter_group.CoxeterGroupAsPermutationGroup.Element.has_descent:3: WARNING: more than one target found for cross-reference u'descents': sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations.ElementMethods.descents, sage.categories.coxeter_groups.CoxeterGroups.ElementMethods.descents, sage.combinat.tableau.Tableau.descents, sage.combinat.sf.ns_macdonald.AugmentedLatticeDiagramFilling.descents, sage.combinat.permutation.Permutation_class.descents, sage.combinat.composition.Composition_class.descents\n```\n",
    "created_at": "2013-01-26T14:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74689",
    "user": "jdemeyer"
}
```

There is a problem with the documentation:

```
/release/merger/sage-5.7.beta2/local/lib/python2.7/site-packages/sage/combinat/root_system/coxeter_group.py:docstring of sage.combinat.root_system.coxeter_group.CoxeterGroupAsPermutationGroup.Element.has_descent:3: WARNING: more than one target found for cross-reference u'descents': sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations.ElementMethods.descents, sage.categories.coxeter_groups.CoxeterGroups.ElementMethods.descents, sage.combinat.tableau.Tableau.descents, sage.combinat.sf.ns_macdonald.AugmentedLatticeDiagramFilling.descents, sage.combinat.permutation.Permutation_class.descents, sage.combinat.composition.Composition_class.descents
```




---

archive/issue_comments_074690.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-01-26T14:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74690",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_074691.json:
```json
{
    "body": "Both issues fixed!",
    "created_at": "2013-01-26T17:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74691",
    "user": "aschilling"
}
```

Both issues fixed!



---

archive/issue_comments_074692.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-01-26T17:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74692",
    "user": "aschilling"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_074693.json:
```json
{
    "body": "Hi Jeroen,\n\nShould we ignore jehova's patchbot failure (the log and shortlog seem empty)?\n\nIs the plugin.startup failure a suggestion for lazy importing CoxeterGroup?\n\nThanks!\n\n               Nicolas",
    "created_at": "2013-02-01T14:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74693",
    "user": "nthiery"
}
```

Hi Jeroen,

Should we ignore jehova's patchbot failure (the log and shortlog seem empty)?

Is the plugin.startup failure a suggestion for lazy importing CoxeterGroup?

Thanks!

               Nicolas



---

archive/issue_comments_074694.json:
```json
{
    "body": "In consultation with Nicolas, I fixed some failing doctests in /combinat/root_systems/coxeter_group.py for type H3.\n\nAnne",
    "created_at": "2013-02-02T19:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74694",
    "user": "aschilling"
}
```

In consultation with Nicolas, I fixed some failing doctests in /combinat/root_systems/coxeter_group.py for type H3.

Anne



---

archive/issue_comments_074695.json:
```json
{
    "body": "Attachment [trac_8359-coxeter-groups-permutation-nt.patch](tarball://root/attachments/some-uuid/ticket8359/trac_8359-coxeter-groups-permutation-nt.patch) by aschilling created at 2013-02-04 23:07:09",
    "created_at": "2013-02-04T23:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74695",
    "user": "aschilling"
}
```

Attachment [trac_8359-coxeter-groups-permutation-nt.patch](tarball://root/attachments/some-uuid/ticket8359/trac_8359-coxeter-groups-permutation-nt.patch) by aschilling created at 2013-02-04 23:07:09



---

archive/issue_comments_074696.json:
```json
{
    "body": "Removed trailing white spaces.\n\nAnne",
    "created_at": "2013-02-04T23:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74696",
    "user": "aschilling"
}
```

Removed trailing white spaces.

Anne



---

archive/issue_comments_074697.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-02-05T08:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8359#issuecomment-74697",
    "user": "jdemeyer"
}
```

Resolution: fixed
