# Issue 4362: Bug fixes in tableaux latex output [with patches at #4355. Needs review.]

archive/issues_004362.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nThe latex output of tableaux is a broke, which affects the latex output in CrystalOfTableaux. Patches that fix this were attached to #4355 but I should have created a new ticket for these since that ticket really proposes something different.\n\nSee #4355 for the patches.\n\nSee http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/3fff0cbc6b44b483?hl=en for discussion. But in a nutshell try \n\n\n```\nlatex(Tableau([[1,2,3],[2,2],[3,4],[4]])) \nlatex(Tableau([[1,1,2,3,4],[2,2,2],[3]])) \nlatex(Tableau([[1],[2],[3],[4]])) \nlatex(Tableau([[1,2,3,4]])) \nlatex(Tableau([[1,2,3,4],[5,6,7,8]])) \nlatex(Tableau([[1,2,3,4],[5,6,7,8],[9]])) \nlatex(Tableau([[1,2,],[5,6],[7,9]])) \nlatex(Tableau([[1,2,],[5,6],[7,9],[9]])) \nlatex(Tableau([[1,2,3,4,5,],[6]])) \nlatex(Tableau([[1,2,3,4,5,],[6],[7],[8],[9]])) \n```\n\n\netc or \n\n\n```\nCrystalOfTableaux(\"A2\",shape=[3,1]).latex_file(\"/home/bump/tmp/test.tex\")\n```\n\n\nto see the defect.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4362\n\n",
    "created_at": "2008-10-24T11:34:13Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Bug fixes in tableaux latex output [with patches at #4355. Needs review.]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4362",
    "user": "https://github.com/dwbump"
}
```
Assignee: @mwhansen

CC:  sage-combinat

The latex output of tableaux is a broke, which affects the latex output in CrystalOfTableaux. Patches that fix this were attached to #4355 but I should have created a new ticket for these since that ticket really proposes something different.

See #4355 for the patches.

See http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/3fff0cbc6b44b483?hl=en for discussion. But in a nutshell try 


```
latex(Tableau([[1,2,3],[2,2],[3,4],[4]])) 
latex(Tableau([[1,1,2,3,4],[2,2,2],[3]])) 
latex(Tableau([[1],[2],[3],[4]])) 
latex(Tableau([[1,2,3,4]])) 
latex(Tableau([[1,2,3,4],[5,6,7,8]])) 
latex(Tableau([[1,2,3,4],[5,6,7,8],[9]])) 
latex(Tableau([[1,2,],[5,6],[7,9]])) 
latex(Tableau([[1,2,],[5,6],[7,9],[9]])) 
latex(Tableau([[1,2,3,4,5,],[6]])) 
latex(Tableau([[1,2,3,4,5,],[6],[7],[8],[9]])) 
```


etc or 


```
CrystalOfTableaux("A2",shape=[3,1]).latex_file("/home/bump/tmp/test.tex")
```


to see the defect.



Issue created by migration from https://trac.sagemath.org/ticket/4362





---

archive/issue_comments_031982.json:
```json
{
    "body": "Attachment [tableaux_output.patch](tarball://root/attachments/some-uuid/ticket4362/tableaux_output.patch) by mabshoff created at 2008-10-24 11:40:20\n\nFirst of Dan's patches from #4355",
    "created_at": "2008-10-24T11:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4362#issuecomment-31982",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [tableaux_output.patch](tarball://root/attachments/some-uuid/ticket4362/tableaux_output.patch) by mabshoff created at 2008-10-24 11:40:20

First of Dan's patches from #4355



---

archive/issue_comments_031983.json:
```json
{
    "body": "Attachment [tableaux_output1.patch](tarball://root/attachments/some-uuid/ticket4362/tableaux_output1.patch) by mabshoff created at 2008-10-24 11:40:42\n\nSecond of Dan's patches from #4355",
    "created_at": "2008-10-24T11:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4362#issuecomment-31983",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [tableaux_output1.patch](tarball://root/attachments/some-uuid/ticket4362/tableaux_output1.patch) by mabshoff created at 2008-10-24 11:40:42

Second of Dan's patches from #4355



---

archive/issue_comments_031984.json:
```json
{
    "body": "Dan, \n\nI have moved the patches from #4355 over here and will delete them on the other ticket. Having patches from another ticket applied via this ticket will only make things more complicated than they need to be.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-24T11:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4362#issuecomment-31984",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Dan, 

I have moved the patches from #4355 over here and will delete them on the other ticket. Having patches from another ticket applied via this ticket will only make things more complicated than they need to be.

Cheers,

Michael



---

archive/issue_comments_031985.json:
```json
{
    "body": "I tested this out on all the examples, and it looks good to me.",
    "created_at": "2008-11-06T22:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4362#issuecomment-31985",
    "user": "https://github.com/mwhansen"
}
```

I tested this out on all the examples, and it looks good to me.



---

archive/issue_comments_031986.json:
```json
{
    "body": "Attachment [tableaux_output2.patch](tarball://root/attachments/some-uuid/ticket4362/tableaux_output2.patch) by @dwbump created at 2008-11-06 23:11:54\n\nNicolas suggested that the tests should reflect the problem. As it turns out the existing tests all have square tableaux (in tensor_product.py, tableau.py and output.py) which is a rare case that is not broke for the original code.\n\nhttp://groups.google.com/group/sage-combinat-devel/msg/cd0de81b0e2f0ae5?hl=en\n\nNicolas posted this before Mike reviewed the patch. In view of Nicolas' comment I'm uploading\na third patch tableaux_output2.patch that makes the tests non-rectangular tableaux\nfor which the original code was broke.",
    "created_at": "2008-11-06T23:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4362#issuecomment-31986",
    "user": "https://github.com/dwbump"
}
```

Attachment [tableaux_output2.patch](tarball://root/attachments/some-uuid/ticket4362/tableaux_output2.patch) by @dwbump created at 2008-11-06 23:11:54

Nicolas suggested that the tests should reflect the problem. As it turns out the existing tests all have square tableaux (in tensor_product.py, tableau.py and output.py) which is a rare case that is not broke for the original code.

http://groups.google.com/group/sage-combinat-devel/msg/cd0de81b0e2f0ae5?hl=en

Nicolas posted this before Mike reviewed the patch. In view of Nicolas' comment I'm uploading
a third patch tableaux_output2.patch that makes the tests non-rectangular tableaux
for which the original code was broke.



---

archive/issue_comments_031987.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-07T16:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4362#issuecomment-31987",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031988.json:
```json
{
    "body": "Merged all three patches in Sage 3.2.rc0. \n\nDan: Please make sure that you post patches and not diffs. I did apply and commit the patches above in your name, so no need to update anything here.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-07T16:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4362#issuecomment-31988",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.2.rc0. 

Dan: Please make sure that you post patches and not diffs. I did apply and commit the patches above in your name, so no need to update anything here.

Cheers,

Michael
