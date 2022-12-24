# Issue 4926: convert sage.schemes.* docstrings to Sphinx

archive/issues_004926.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4926\n\n",
    "created_at": "2009-01-01T22:55:55Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "convert sage.schemes.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4926",
    "user": "mhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4926





---

archive/issue_comments_037375.json:
```json
{
    "body": "Patch at http://sage.math.washington.edu/home/mhansen/trac_4926.patch",
    "created_at": "2009-01-02T02:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4926#issuecomment-37375",
    "user": "mhansen"
}
```

Patch at http://sage.math.washington.edu/home/mhansen/trac_4926.patch



---

archive/issue_comments_037376.json:
```json
{
    "body": "Review (from reading the html output):\n\nSchemes section\n\n* base_extend(): missing newline before EXAMPLES\n* projective_embedding(): bad indentation for second INPUT block\n* affine_patch() has a comma at the start of a line\n* projective_embedding(): bad indentation for second INPUT block (again)\n\nElliptic and Plane Curves section\n\n* typo in arithmetic_genus():  \"normalization\"\n* division_polynomial(): bad indentation in the (rather long) explanation of input parameter two_torsion_multiplicity; some math-mode missing here too.\n\n[I noticed that the functions are sorted into alphabetical order, with upper case before lower case.  Can we make it case-insensitive?  For example, S_integral_points() comes right near the top.]\n\n* typo in heegner_index: \"currently\"\n* modular_degree(): in one place algorithm 'ec' is mentioned instead of 'sympow'.\n* regulator_of_points: bad indentation of INPUT\n* tamagawa_exponent(): bad math translation of $C_2\\times C_2$.\n* group_law (in formal_group):  missing subscript tage on t1, t2;  bad exponent \"prec\". same in mult_by_n() and possibly elsewhere.\n* frobenius_expansion_by_series(): the 2nd and 3rd large displays are merged.  I think \"where\" should be on a separate line in between.\n* \"p-adic functions from ell_rational_field.py, moved here to reduce\" is a sill name.  I suggest renameing to simply \"p-adic functions\", perhaps with \"miscellaneous\".\n\nHyperelliptic curve section:\n\n* At bottom of section \"Conductor and Reduction Types for Genus 2 Curves\": the reference to the paper of Liu looks all wrong.",
    "created_at": "2009-01-03T17:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4926#issuecomment-37376",
    "user": "cremona"
}
```

Review (from reading the html output):

Schemes section

* base_extend(): missing newline before EXAMPLES
* projective_embedding(): bad indentation for second INPUT block
* affine_patch() has a comma at the start of a line
* projective_embedding(): bad indentation for second INPUT block (again)

Elliptic and Plane Curves section

* typo in arithmetic_genus():  "normalization"
* division_polynomial(): bad indentation in the (rather long) explanation of input parameter two_torsion_multiplicity; some math-mode missing here too.

[I noticed that the functions are sorted into alphabetical order, with upper case before lower case.  Can we make it case-insensitive?  For example, S_integral_points() comes right near the top.]

* typo in heegner_index: "currently"
* modular_degree(): in one place algorithm 'ec' is mentioned instead of 'sympow'.
* regulator_of_points: bad indentation of INPUT
* tamagawa_exponent(): bad math translation of $C_2\times C_2$.
* group_law (in formal_group):  missing subscript tage on t1, t2;  bad exponent "prec". same in mult_by_n() and possibly elsewhere.
* frobenius_expansion_by_series(): the 2nd and 3rd large displays are merged.  I think "where" should be on a separate line in between.
* "p-adic functions from ell_rational_field.py, moved here to reduce" is a sill name.  I suggest renameing to simply "p-adic functions", perhaps with "miscellaneous".

Hyperelliptic curve section:

* At bottom of section "Conductor and Reduction Types for Genus 2 Curves": the reference to the paper of Liu looks all wrong.



---

archive/issue_comments_037377.json:
```json
{
    "body": "I forgot to say:  patch applies ok to 3.2.3.final.  I have not tried editing the source to fix the things I found, since I don't know how to check the result.",
    "created_at": "2009-01-03T17:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4926#issuecomment-37377",
    "user": "cremona"
}
```

I forgot to say:  patch applies ok to 3.2.3.final.  I have not tried editing the source to fix the things I found, since I don't know how to check the result.



---

archive/issue_comments_037378.json:
```json
{
    "body": "Attachment [trac_4926-2.patch](tarball://root/attachments/some-uuid/ticket4926/trac_4926-2.patch) by mhansen created at 2009-01-11 04:43:49",
    "created_at": "2009-01-11T04:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4926#issuecomment-37378",
    "user": "mhansen"
}
```

Attachment [trac_4926-2.patch](tarball://root/attachments/some-uuid/ticket4926/trac_4926-2.patch) by mhansen created at 2009-01-11 04:43:49



---

archive/issue_comments_037379.json:
```json
{
    "body": "I've posted a patch which addresses these changes.",
    "created_at": "2009-01-11T04:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4926#issuecomment-37379",
    "user": "mhansen"
}
```

I've posted a patch which addresses these changes.



---

archive/issue_comments_037380.json:
```json
{
    "body": "Looks good now.  Pass!",
    "created_at": "2009-01-13T21:55:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4926#issuecomment-37380",
    "user": "cremona"
}
```

Looks good now.  Pass!



---

archive/issue_comments_037381.json:
```json
{
    "body": "Attachment [sage.schemes-final.patch](tarball://root/attachments/some-uuid/ticket4926/sage.schemes-final.patch) by mhansen created at 2009-02-21 19:22:08",
    "created_at": "2009-02-21T19:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4926#issuecomment-37381",
    "user": "mhansen"
}
```

Attachment [sage.schemes-final.patch](tarball://root/attachments/some-uuid/ticket4926/sage.schemes-final.patch) by mhansen created at 2009-02-21 19:22:08



---

archive/issue_comments_037382.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4926#issuecomment-37382",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037383.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4926#issuecomment-37383",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael
