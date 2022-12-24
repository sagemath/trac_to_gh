# Issue 9383: Adding quadratic_forms Code to the Reference Manual

archive/issues_009383.json:
```json
{
    "body": "Assignee: mvngu\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9383\n\n",
    "created_at": "2010-06-29T21:02:50Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Adding quadratic_forms Code to the Reference Manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9383",
    "user": "annahaensch"
}
```
Assignee: mvngu



Issue created by migration from https://trac.sagemath.org/ticket/9383





---

archive/issue_comments_089206.json:
```json
{
    "body": "Attachment [trac_9383.patch](tarball://root/attachments/some-uuid/ticket9383/trac_9383.patch) by annahaensch created at 2010-07-01 05:28:01\n\nquadratic_forms reference manual docbuild",
    "created_at": "2010-07-01T05:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89206",
    "user": "annahaensch"
}
```

Attachment [trac_9383.patch](tarball://root/attachments/some-uuid/ticket9383/trac_9383.patch) by annahaensch created at 2010-07-01 05:28:01

quadratic_forms reference manual docbuild



---

archive/issue_comments_089207.json:
```json
{
    "body": "This is half of the quadratic_forms documentation, I'll post the second half in an updated patch tomorrow.",
    "created_at": "2010-07-01T05:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89207",
    "user": "annahaensch"
}
```

This is half of the quadratic_forms documentation, I'll post the second half in an updated patch tomorrow.



---

archive/issue_comments_089208.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-07-01T05:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89208",
    "user": "annahaensch"
}
```

Changing priority from major to minor.



---

archive/issue_comments_089209.json:
```json
{
    "body": "Use instead of trac_9383.patch",
    "created_at": "2010-07-01T20:44:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89209",
    "user": "annahaensch"
}
```

Use instead of trac_9383.patch



---

archive/issue_comments_089210.json:
```json
{
    "body": "Attachment [trac_9383_v2.patch](tarball://root/attachments/some-uuid/ticket9383/trac_9383_v2.patch) by annahaensch created at 2010-07-01 20:54:40\n\nThis patch should complete the reference documentation for quadratic forms.  It's still returning a warning that the file is not contained in a toctree.  Ideas?",
    "created_at": "2010-07-01T20:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89210",
    "user": "annahaensch"
}
```

Attachment [trac_9383_v2.patch](tarball://root/attachments/some-uuid/ticket9383/trac_9383_v2.patch) by annahaensch created at 2010-07-01 20:54:40

This patch should complete the reference documentation for quadratic forms.  It's still returning a warning that the file is not contained in a toctree.  Ideas?



---

archive/issue_comments_089211.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-01T20:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89211",
    "user": "annahaensch"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089212.json:
```json
{
    "body": "Attachment [trac_9383_v3.patch](tarball://root/attachments/some-uuid/ticket9383/trac_9383_v3.patch) by annahaensch created at 2010-07-12 12:51:14\n\nUse in place of all previous patches",
    "created_at": "2010-07-12T12:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89212",
    "user": "annahaensch"
}
```

Attachment [trac_9383_v3.patch](tarball://root/attachments/some-uuid/ticket9383/trac_9383_v3.patch) by annahaensch created at 2010-07-12 12:51:14

Use in place of all previous patches



---

archive/issue_comments_089213.json:
```json
{
    "body": "It looks to me like you forgot to do \"hg add\" on your new file doc/en/reference/quadratic_forms.rst. Hence when I apply the patch to a new clone and build, I get an error \n`/storage/masiao/sage-4.5.2.alpha1/devel/sage/doc/en/reference/index.rst:40: (WARNING/2) toctree references unknown document u'quadratic_forms'`\nand nothing new appears in the ref manual.\n\nDavid",
    "created_at": "2010-07-28T19:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89213",
    "user": "davidloeffler"
}
```

It looks to me like you forgot to do "hg add" on your new file doc/en/reference/quadratic_forms.rst. Hence when I apply the patch to a new clone and build, I get an error 
`/storage/masiao/sage-4.5.2.alpha1/devel/sage/doc/en/reference/index.rst:40: (WARNING/2) toctree references unknown document u'quadratic_forms'`
and nothing new appears in the ref manual.

David



---

archive/issue_comments_089214.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-28T19:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89214",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089215.json:
```json
{
    "body": "BTW: the reference manual building code can behave very oddly when files have been deleted -- because of the way that the Sphinx parser caches its environment, it's next to impossible to squash the \"document not included in any toctree\" error, except by creating a new clean clone and applying your patch to that.",
    "created_at": "2010-07-28T19:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89215",
    "user": "davidloeffler"
}
```

BTW: the reference manual building code can behave very oddly when files have been deleted -- because of the way that the Sphinx parser caches its environment, it's next to impossible to squash the "document not included in any toctree" error, except by creating a new clean clone and applying your patch to that.



---

archive/issue_comments_089216.json:
```json
{
    "body": "Attachment [trac_9383_v4.patch](tarball://root/attachments/some-uuid/ticket9383/trac_9383_v4.patch) by davidloeffler created at 2010-08-03 13:57:41\n\nreplaces all previous patches",
    "created_at": "2010-08-03T13:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89216",
    "user": "davidloeffler"
}
```

Attachment [trac_9383_v4.patch](tarball://root/attachments/some-uuid/ticket9383/trac_9383_v4.patch) by davidloeffler created at 2010-08-03 13:57:41

replaces all previous patches



---

archive/issue_comments_089217.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2010-08-03T13:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89217",
    "user": "davidloeffler"
}
```

Changing priority from minor to major.



---

archive/issue_comments_089218.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-03T13:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89218",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089219.json:
```json
{
    "body": "Changing keywords from \"\" to \"quadratic forms\".",
    "created_at": "2010-08-03T13:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89219",
    "user": "davidloeffler"
}
```

Changing keywords from "" to "quadratic forms".



---

archive/issue_comments_089220.json:
```json
{
    "body": "Here's a new patch, against 4.5.2.rc0, incorporating Anna's work and extending it by adding the modules `count_local_2` and `special_values`. \n\nThe results are a little scruffy in places, but that will be much easier to sort out once the modules have been added and people can see the results!",
    "created_at": "2010-08-03T14:01:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89220",
    "user": "davidloeffler"
}
```

Here's a new patch, against 4.5.2.rc0, incorporating Anna's work and extending it by adding the modules `count_local_2` and `special_values`. 

The results are a little scruffy in places, but that will be much easier to sort out once the modules have been added and people can see the results!



---

archive/issue_comments_089221.json:
```json
{
    "body": "I'm OK with the attachment [attachment:trac_9383_v4.patch]. Note that it adds the following modules to the reference manual:\n\n\n```\nsage/quadratic_forms/quadratic_form \nsage/quadratic_forms/binary_qf \nsage/quadratic_forms/constructions \nsage/quadratic_forms/random_quadraticform \nsage/quadratic_forms/special_values \nsage/quadratic_forms/count_local_2\n```\n\n\nThe attachment make numerous ReST changes to the following modules, but does not add them to the reference manual:\n\n\n```\nsage/quadratic_forms/quadratic_form__automorphisms.py\nsage/quadratic_forms/quadratic_form__count_local_2.py\nsage/quadratic_forms/quadratic_form__equivalence_testing.py\nsage/quadratic_forms/quadratic_form__genus.py\nsage/quadratic_forms/quadratic_form__local_density_congruence.py\nsage/quadratic_forms/quadratic_form__local_density_interfaces.py\nsage/quadratic_forms/quadratic_form__local_field_invariants.py\nsage/quadratic_forms/quadratic_form__local_normal_form.py\nsage/quadratic_forms/quadratic_form__local_representation_conditions.py\nsage/quadratic_forms/quadratic_form__mass.py\nsage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py\nsage/quadratic_forms/quadratic_form__mass__Siegel_densities.py\nsage/quadratic_forms/quadratic_form__neighbors.py\nsage/quadratic_forms/quadratic_form__reduction_theory.py\nsage/quadratic_forms/quadratic_form__siegel_product.py\nsage/quadratic_forms/quadratic_form__split_local_covering.py\nsage/quadratic_forms/quadratic_form__ternary_Tornaria.py\nsage/quadratic_forms/quadratic_form__theta.py\nsage/quadratic_forms/quadratic_form__variable_substitutions.py\n```\n\n\nThe [attachment:trac_9383_v4.patch] receives a positive review as is. If you want, you could open another ticket to add the missing modules to the reference manual.",
    "created_at": "2010-09-21T07:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89221",
    "user": "mvngu"
}
```

I'm OK with the attachment [attachment:trac_9383_v4.patch]. Note that it adds the following modules to the reference manual:


```
sage/quadratic_forms/quadratic_form 
sage/quadratic_forms/binary_qf 
sage/quadratic_forms/constructions 
sage/quadratic_forms/random_quadraticform 
sage/quadratic_forms/special_values 
sage/quadratic_forms/count_local_2
```


The attachment make numerous ReST changes to the following modules, but does not add them to the reference manual:


```
sage/quadratic_forms/quadratic_form__automorphisms.py
sage/quadratic_forms/quadratic_form__count_local_2.py
sage/quadratic_forms/quadratic_form__equivalence_testing.py
sage/quadratic_forms/quadratic_form__genus.py
sage/quadratic_forms/quadratic_form__local_density_congruence.py
sage/quadratic_forms/quadratic_form__local_density_interfaces.py
sage/quadratic_forms/quadratic_form__local_field_invariants.py
sage/quadratic_forms/quadratic_form__local_normal_form.py
sage/quadratic_forms/quadratic_form__local_representation_conditions.py
sage/quadratic_forms/quadratic_form__mass.py
sage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py
sage/quadratic_forms/quadratic_form__mass__Siegel_densities.py
sage/quadratic_forms/quadratic_form__neighbors.py
sage/quadratic_forms/quadratic_form__reduction_theory.py
sage/quadratic_forms/quadratic_form__siegel_product.py
sage/quadratic_forms/quadratic_form__split_local_covering.py
sage/quadratic_forms/quadratic_form__ternary_Tornaria.py
sage/quadratic_forms/quadratic_form__theta.py
sage/quadratic_forms/quadratic_form__variable_substitutions.py
```


The [attachment:trac_9383_v4.patch] receives a positive review as is. If you want, you could open another ticket to add the missing modules to the reference manual.



---

archive/issue_comments_089222.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-21T07:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89222",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089223.json:
```json
{
    "body": "Replying to [comment:7 mvngu]:\n> The attachment make numerous ReST changes to the following modules, but does not add them to the reference manual:\n> \n> {{{\n> sage/quadratic_forms/quadratic_form__automorphisms.py\n> sage/quadratic_forms/quadratic_form__count_local_2.py\n> sage/quadratic_forms/quadratic_form__equivalence_testing.py\n> sage/quadratic_forms/quadratic_form__genus.py\n> sage/quadratic_forms/quadratic_form__local_density_congruence.py\n> sage/quadratic_forms/quadratic_form__local_density_interfaces.py\n> sage/quadratic_forms/quadratic_form__local_field_invariants.py\n> sage/quadratic_forms/quadratic_form__local_normal_form.py\n> sage/quadratic_forms/quadratic_form__local_representation_conditions.py\n> sage/quadratic_forms/quadratic_form__mass.py\n> sage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py\n> sage/quadratic_forms/quadratic_form__mass__Siegel_densities.py\n> sage/quadratic_forms/quadratic_form__neighbors.py\n> sage/quadratic_forms/quadratic_form__reduction_theory.py\n> sage/quadratic_forms/quadratic_form__siegel_product.py\n> sage/quadratic_forms/quadratic_form__split_local_covering.py\n> sage/quadratic_forms/quadratic_form__ternary_Tornaria.py\n> sage/quadratic_forms/quadratic_form__theta.py\n> sage/quadratic_forms/quadratic_form__variable_substitutions.py\n> }}}\n> \n> The [attachment:trac_9383_v4.patch] receives a positive review as is. If you want, you could open another ticket to add the missing modules to the reference manual.\n\nNo, there is no need to do this. The functions from those modules are all imported into quadratic__form.py; they are divided into separate modules solely in order to keep the size of the top-level file manageable. The ReST parser follows these imports, so adding the separate files to the manual as well would just mean everything was in there twice.\n\nThanks for the review, anyway!\n\nDavid",
    "created_at": "2010-09-21T15:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89223",
    "user": "davidloeffler"
}
```

Replying to [comment:7 mvngu]:
> The attachment make numerous ReST changes to the following modules, but does not add them to the reference manual:
> 
> {{{
> sage/quadratic_forms/quadratic_form__automorphisms.py
> sage/quadratic_forms/quadratic_form__count_local_2.py
> sage/quadratic_forms/quadratic_form__equivalence_testing.py
> sage/quadratic_forms/quadratic_form__genus.py
> sage/quadratic_forms/quadratic_form__local_density_congruence.py
> sage/quadratic_forms/quadratic_form__local_density_interfaces.py
> sage/quadratic_forms/quadratic_form__local_field_invariants.py
> sage/quadratic_forms/quadratic_form__local_normal_form.py
> sage/quadratic_forms/quadratic_form__local_representation_conditions.py
> sage/quadratic_forms/quadratic_form__mass.py
> sage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py
> sage/quadratic_forms/quadratic_form__mass__Siegel_densities.py
> sage/quadratic_forms/quadratic_form__neighbors.py
> sage/quadratic_forms/quadratic_form__reduction_theory.py
> sage/quadratic_forms/quadratic_form__siegel_product.py
> sage/quadratic_forms/quadratic_form__split_local_covering.py
> sage/quadratic_forms/quadratic_form__ternary_Tornaria.py
> sage/quadratic_forms/quadratic_form__theta.py
> sage/quadratic_forms/quadratic_form__variable_substitutions.py
> }}}
> 
> The [attachment:trac_9383_v4.patch] receives a positive review as is. If you want, you could open another ticket to add the missing modules to the reference manual.

No, there is no need to do this. The functions from those modules are all imported into quadratic__form.py; they are divided into separate modules solely in order to keep the size of the top-level file manageable. The ReST parser follows these imports, so adding the separate files to the manual as well would just mean everything was in there twice.

Thanks for the review, anyway!

David



---

archive/issue_comments_089224.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T09:10:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9383#issuecomment-89224",
    "user": "mpatel"
}
```

Resolution: fixed
