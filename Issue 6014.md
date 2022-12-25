# Issue 6014: hexads in S(5,6,12) and mathematical blackjack

archive/issues_006014.json:
```json
{
    "body": "Assignee: @rlmill\n\nKeywords: combinatorics, coding theory\n\nThis patch implements kittens, hexads and mathematical blackjack as explained in\n\n\n```\n    R. Curtis, ``The Steiner system $S(5,6,12)$, the Mathieu group $M_{12}$, \n    and the kitten,'' in {\\bf Computational group theory}, ed. M. Atkinson, \n    Academic Press, 1984.\n    J. Conway, ``Hexacode and tetracode - MINIMOG and MOG,'' in {\\bf Computational \n    group theory}, ed. M. Atkinson, Academic Press, 1984.\n    J. Conway and N. Sloane, ``Lexicographic codes: error-correcting codes from \n    game theory,'' IEEE Trans. Infor. Theory32(1986)337-348.\n    J. Kahane and A. Ryba, ``The hexad game,'' Electronic Journal of Combinatorics, 8 (2001) \n    http://www.combinatorics.org/Volume_8/Abstracts/v8i2r11.html\n```\n\n\nIt is used in a book on coding theory I'm writing with Jon-Lark Kim on coding theory, which uses Sage throughout to illustrate error-correcting codes.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6014\n\n",
    "created_at": "2009-05-10T12:56:56Z",
    "labels": [
        "component: coding theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "hexads in S(5,6,12) and mathematical blackjack",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6014",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @rlmill

Keywords: combinatorics, coding theory

This patch implements kittens, hexads and mathematical blackjack as explained in


```
    R. Curtis, ``The Steiner system $S(5,6,12)$, the Mathieu group $M_{12}$, 
    and the kitten,'' in {\bf Computational group theory}, ed. M. Atkinson, 
    Academic Press, 1984.
    J. Conway, ``Hexacode and tetracode - MINIMOG and MOG,'' in {\bf Computational 
    group theory}, ed. M. Atkinson, Academic Press, 1984.
    J. Conway and N. Sloane, ``Lexicographic codes: error-correcting codes from 
    game theory,'' IEEE Trans. Infor. Theory32(1986)337-348.
    J. Kahane and A. Ryba, ``The hexad game,'' Electronic Journal of Combinatorics, 8 (2001) 
    http://www.combinatorics.org/Volume_8/Abstracts/v8i2r11.html
```


It is used in a book on coding theory I'm writing with Jon-Lark Kim on coding theory, which uses Sage throughout to illustrate error-correcting codes.


Issue created by migration from https://trac.sagemath.org/ticket/6014





---

archive/issue_comments_047760.json:
```json
{
    "body": "applies to 3.4.2 and passes sage -testall",
    "created_at": "2009-05-10T12:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6014#issuecomment-47760",
    "user": "https://github.com/wdjoyner"
}
```

applies to 3.4.2 and passes sage -testall



---

archive/issue_comments_047761.json:
```json
{
    "body": "Attachment [trac_6014-hexads.patch](tarball://root/attachments/some-uuid/ticket6014/trac_6014-hexads.patch) by @wdjoyner created at 2009-05-12 00:33:10",
    "created_at": "2009-05-12T00:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6014#issuecomment-47761",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_6014-hexads.patch](tarball://root/attachments/some-uuid/ticket6014/trac_6014-hexads.patch) by @wdjoyner created at 2009-05-12 00:33:10



---

archive/issue_comments_047762.json:
```json
{
    "body": "After reviewing the patch I think that it looks good overall, but there is one major problem.  In setting_up() various global variables are created with information for minimog_shuffle.  The find_hexad() functions take MINIMOG as an argument, but use the minimog_shuffle global variables.  Right now this is the only minimog implemented, but if minimog_modulo11 is implemented in the future, other changes would be needed.\n\nInstead of having the global variables separate from the minimog, why not define a class minimog, which contains all the line, cross, tet, and other information.  This would take care of the above problem, and be better programming practice.  \n\nAlso, is it really that difficult to implement minimog_modulo11?  I think the only problem is that then the minimog can't be defined as a matrix over QQ.  Since there aren't any arithmetic operations being done to the matrix elements, this shouldn't be a real impediment.  If the minimogs are implemented as classes, then a function could be added to convert minimog elements to strings that handles infinity.",
    "created_at": "2009-06-01T18:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6014#issuecomment-47762",
    "user": "https://trac.sagemath.org/admin/accounts/users/dgordon"
}
```

After reviewing the patch I think that it looks good overall, but there is one major problem.  In setting_up() various global variables are created with information for minimog_shuffle.  The find_hexad() functions take MINIMOG as an argument, but use the minimog_shuffle global variables.  Right now this is the only minimog implemented, but if minimog_modulo11 is implemented in the future, other changes would be needed.

Instead of having the global variables separate from the minimog, why not define a class minimog, which contains all the line, cross, tet, and other information.  This would take care of the above problem, and be better programming practice.  

Also, is it really that difficult to implement minimog_modulo11?  I think the only problem is that then the minimog can't be defined as a matrix over QQ.  Since there aren't any arithmetic operations being done to the matrix elements, this shouldn't be a real impediment.  If the minimogs are implemented as classes, then a function could be added to convert minimog elements to strings that handles infinity.



---

archive/issue_comments_047763.json:
```json
{
    "body": "Attachment [trac_6014-hexads2.patch](tarball://root/attachments/some-uuid/ticket6014/trac_6014-hexads2.patch) by @wdjoyner created at 2009-06-03 04:41:37",
    "created_at": "2009-06-03T04:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6014#issuecomment-47763",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_6014-hexads2.patch](tarball://root/attachments/some-uuid/ticket6014/trac_6014-hexads2.patch) by @wdjoyner created at 2009-06-03 04:41:37



---

archive/issue_comments_047764.json:
```json
{
    "body": "This implements the referee's suggestions, passes sage -testall on 4.0.1.a0 on a 64bit ubuntu 9.04 machine(except for the problem with html.py, which was already reported as a separate issue). Also, sage -docbuild reference html worked without errors.\n\nBoth patches need to be applied.",
    "created_at": "2009-06-03T12:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6014#issuecomment-47764",
    "user": "https://github.com/wdjoyner"
}
```

This implements the referee's suggestions, passes sage -testall on 4.0.1.a0 on a 64bit ubuntu 9.04 machine(except for the problem with html.py, which was already reported as a separate issue). Also, sage -docbuild reference html worked without errors.

Both patches need to be applied.



---

archive/issue_comments_047765.json:
```json
{
    "body": "Attachment [trac_6014-hexads3.patch](tarball://root/attachments/some-uuid/ticket6014/trac_6014-hexads3.patch) by @wdjoyner created at 2009-06-03 22:12:29\n\nto be applied after the other two",
    "created_at": "2009-06-03T22:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6014#issuecomment-47765",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_6014-hexads3.patch](tarball://root/attachments/some-uuid/ticket6014/trac_6014-hexads3.patch) by @wdjoyner created at 2009-06-03 22:12:29

to be applied after the other two



---

archive/issue_comments_047766.json:
```json
{
    "body": "Attachment [trac_6014-hexads4.patch](tarball://root/attachments/some-uuid/ticket6014/trac_6014-hexads4.patch) by @wdjoyner created at 2009-06-04 02:36:29",
    "created_at": "2009-06-04T02:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6014#issuecomment-47766",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_6014-hexads4.patch](tarball://root/attachments/some-uuid/ticket6014/trac_6014-hexads4.patch) by @wdjoyner created at 2009-06-04 02:36:29



---

archive/issue_comments_047767.json:
```json
{
    "body": "These patches add the examples suggested by the referee.\n\nOne odd thing is that it appears that a list of elements containing infinity is sorted differently on an intel mac than on an ubuntu machine.\nBecause of this, I had to add a # random comment to a docstring.",
    "created_at": "2009-06-04T02:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6014#issuecomment-47767",
    "user": "https://github.com/wdjoyner"
}
```

These patches add the examples suggested by the referee.

One odd thing is that it appears that a list of elements containing infinity is sorted differently on an intel mac than on an ubuntu machine.
Because of this, I had to add a # random comment to a docstring.



---

archive/issue_comments_047768.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6014#issuecomment-47768",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_events_006269.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-13T21:45:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6014",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6014#event-6269"
}
```
