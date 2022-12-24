# Issue 1646: 'matrix in group' test doesn't work

archive/issues_001646.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe code \n\n\n\n```\nG = SL(2,ZZ)                 \nM = matrix([[1,0],[0,1]])    \nM in G            \n```\n\n\n\nruns possibly forever inside GAP. same for\n\n```\nM = matrix(ZZ,[[1,0],[0,1]])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1646\n\n",
    "created_at": "2007-12-31T17:18:19Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "'matrix in group' test doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1646",
    "user": "@haraldschilly"
}
```
Assignee: @williamstein

The code 



```
G = SL(2,ZZ)                 
M = matrix([[1,0],[0,1]])    
M in G            
```



runs possibly forever inside GAP. same for

```
M = matrix(ZZ,[[1,0],[0,1]])
```


Issue created by migration from https://trac.sagemath.org/ticket/1646





---

archive/issue_comments_010467.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2008-01-24T09:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1646#issuecomment-10467",
    "user": "mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_010468.json:
```json
{
    "body": "This is due to GAP.  Unless we get GAP to fix this, then the best solution would be for SL to override the __contains__ method.",
    "created_at": "2008-01-24T18:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1646#issuecomment-10468",
    "user": "@mwhansen"
}
```

This is due to GAP.  Unless we get GAP to fix this, then the best solution would be for SL to override the __contains__ method.



---

archive/issue_comments_010469.json:
```json
{
    "body": "Changing assignee from @williamstein to joyner.",
    "created_at": "2008-01-24T20:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1646#issuecomment-10469",
    "user": "@wdjoyner"
}
```

Changing assignee from @williamstein to joyner.



---

archive/issue_comments_010470.json:
```json
{
    "body": "Changing component from linear algebra to group_theory.",
    "created_at": "2008-01-24T20:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1646#issuecomment-10470",
    "user": "@wdjoyner"
}
```

Changing component from linear algebra to group_theory.



---

archive/issue_comments_010471.json:
```json
{
    "body": "I've reported this to GAP support.",
    "created_at": "2008-01-24T20:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1646#issuecomment-10471",
    "user": "@wdjoyner"
}
```

I've reported this to GAP support.



---

archive/issue_comments_010472.json:
```json
{
    "body": "from\tLaurent Bartholdi <laurent.bartholdi`@`gmail.com>\nto\tDavid Joyner <wdjoyner`@`gmail.com>,\ncc\tGAP Support <support`@`gap-system.org>,\ndate\tJan 24, 2008 5:36 PM\nsubject\tRe: [GAP Support] membership in SL(2,Z)\nmailed-by\tgmail.com\n\t\nhide details 5:36 PM (27 minutes ago)\n\t\n\t\n\t\nReply\n\t\n\t\nIt's not intentional, and should be fixed. Here's a quick solution:\n\nInstallMethod(\\in,[IsMatrix,IsSpecialLinearGroup],\n function(g,G)\n   return Length(g)=Length(One(G)) and\n             ForAll(g,row->Length(row)=Length(One(g)) and\n             IsOne(DeterminantMat(g));\n end);\n\nneedless to say, there must be lots of other missing methods; e.g. for\ngeneral, symplectic etc. linear groups.\n- Hide quoted text -\n\nOn Jan 24, 2008 9:16 PM, David Joyner <wdjoyner`@`gmail.com> wrote:\n> Hi:\n>\n> I wonder if the behavior of\n>\n> gap> G := SL(2,Integers);\n> SL(2,Integers)\n> gap> g := [[1,0],[0,1]];\n> [ [ 1, 0 ], [ 0, 1 ] ]\n> gap> g in G;\n> user interrupt at ....\n>\n> is intentional: it just hangs, as far as I can tell.\n> Unless I'm doing something wrong, I wonder if\n> an error message should be returned? Perhaps \"method not\n> implemented\" or something?\n>\n> - David Joyner\n>\n> _______________________________________________\n> Support mailing list\n> Support`@`gap-system.org\n> http://mail.gap-system.org/mailman/listinfo/support\n>\n\n\n\n--\nLaurent Bartholdi          \\  laurent.bartholdi<at>gmail<dot>com\nEPFL SB SMA IMB MAD         \\    T\u00e9l\u00e9phone: +41 21-6935458\nStation 8                    \\ Secr\u00e9taire: +41 21-6935471\nCH-1015 Lausanne, Switzerland \\      Fax: +41 21-6930339\nHome address: http://f34.com/68",
    "created_at": "2008-01-24T23:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1646#issuecomment-10472",
    "user": "@wdjoyner"
}
```

from	Laurent Bartholdi <laurent.bartholdi`@`gmail.com>
to	David Joyner <wdjoyner`@`gmail.com>,
cc	GAP Support <support`@`gap-system.org>,
date	Jan 24, 2008 5:36 PM
subject	Re: [GAP Support] membership in SL(2,Z)
mailed-by	gmail.com
	
hide details 5:36 PM (27 minutes ago)
	
	
	
Reply
	
	
It's not intentional, and should be fixed. Here's a quick solution:

InstallMethod(\in,[IsMatrix,IsSpecialLinearGroup],
 function(g,G)
   return Length(g)=Length(One(G)) and
             ForAll(g,row->Length(row)=Length(One(g)) and
             IsOne(DeterminantMat(g));
 end);

needless to say, there must be lots of other missing methods; e.g. for
general, symplectic etc. linear groups.
- Hide quoted text -

On Jan 24, 2008 9:16 PM, David Joyner <wdjoyner`@`gmail.com> wrote:
> Hi:
>
> I wonder if the behavior of
>
> gap> G := SL(2,Integers);
> SL(2,Integers)
> gap> g := [[1,0],[0,1]];
> [ [ 1, 0 ], [ 0, 1 ] ]
> gap> g in G;
> user interrupt at ....
>
> is intentional: it just hangs, as far as I can tell.
> Unless I'm doing something wrong, I wonder if
> an error message should be returned? Perhaps "method not
> implemented" or something?
>
> - David Joyner
>
> _______________________________________________
> Support mailing list
> Support`@`gap-system.org
> http://mail.gap-system.org/mailman/listinfo/support
>



--
Laurent Bartholdi          \  laurent.bartholdi<at>gmail<dot>com
EPFL SB SMA IMB MAD         \    Téléphone: +41 21-6935458
Station 8                    \ Secrétaire: +41 21-6935471
CH-1015 Lausanne, Switzerland \      Fax: +41 21-6930339
Home address: http://f34.com/68



---

archive/issue_comments_010473.json:
```json
{
    "body": "This is a duplicate of #1834, which has been fixed and merged in 3.1.2.alpha4.",
    "created_at": "2008-09-06T22:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1646#issuecomment-10473",
    "user": "@aghitza"
}
```

This is a duplicate of #1834, which has been fixed and merged in 3.1.2.alpha4.



---

archive/issue_comments_010474.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-09-06T22:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1646#issuecomment-10474",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_010475.json:
```json
{
    "body": "Alex,\n\nThanks for finding the dupe. Closed as duplicate.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-06T22:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1646#issuecomment-10475",
    "user": "mabshoff"
}
```

Alex,

Thanks for finding the dupe. Closed as duplicate.

Cheers,

Michael
