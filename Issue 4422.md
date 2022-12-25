# Issue 4422: create new optional sympow_data.spkg

archive/issues_004422.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @orlitzky @dimpase @isuruf\n\nSympow can use additional data files, but we do not install them. So create an optional spkg that recreates those data since they might be dependent on the big size as well as the endianess of the box. To get various optional doctests to pass run \n\n```\nsympow -new_data 2\nsympow -new_data 1d0\nsympow -new_data 1d1\nsympow -new_data 1d2\n```\n\nfrom $SAGE_LOCAL. There might be other useful sets of data to create. We should ping Mark Watkins about the issue.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4422\n\n",
    "created_at": "2008-11-02T02:35:04Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "create new optional sympow_data.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4422",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @orlitzky @dimpase @isuruf

Sympow can use additional data files, but we do not install them. So create an optional spkg that recreates those data since they might be dependent on the big size as well as the endianess of the box. To get various optional doctests to pass run 

```
sympow -new_data 2
sympow -new_data 1d0
sympow -new_data 1d1
sympow -new_data 1d2
```

from $SAGE_LOCAL. There might be other useful sets of data to create. We should ping Mark Watkins about the issue.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4422





---

archive/issue_comments_032454.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2017-09-13T12:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4422#issuecomment-32454",
    "user": "https://github.com/koffie"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_032455.json:
```json
{
    "body": "Setting spkg proposals that have not seen recent activity to \"sage-wishlist\".",
    "created_at": "2020-06-19T18:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4422#issuecomment-32455",
    "user": "https://github.com/mkoeppe"
}
```

Setting spkg proposals that have not seen recent activity to "sage-wishlist".



---

archive/issue_comments_032456.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2020-06-19T18:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4422#issuecomment-32456",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_032457.json:
```json
{
    "body": "I think this might be obsolete. When we upgrade sympow, the new version will install some architecture-independent data files by default, and generate the others as needed (caching them in `$HOME/.sympow`). The following is what I have installed from the Gentoo package, and the new sympow SPKG will be similar:\n\n\n```\n$ equery f sympow\n * Searching for sympow ...\n * Contents of sci-mathematics/sympow-2.023.6:\n...\n/usr/share/sympow/datafiles\n/usr/share/sympow/datafiles/A012M.txt\n/usr/share/sympow/datafiles/A012S.txt\n/usr/share/sympow/datafiles/A013M.txt\n/usr/share/sympow/datafiles/A013S.txt\n/usr/share/sympow/datafiles/A014M.txt\n/usr/share/sympow/datafiles/A014S.txt\n/usr/share/sympow/datafiles/A015M.txt\n/usr/share/sympow/datafiles/A015S.txt\n/usr/share/sympow/datafiles/A016M.txt\n/usr/share/sympow/datafiles/A016S.txt\n/usr/share/sympow/datafiles/A017M.txt\n/usr/share/sympow/datafiles/A017S.txt\n/usr/share/sympow/datafiles/A018M.txt\n/usr/share/sympow/datafiles/A018S.txt\n/usr/share/sympow/datafiles/A019M.txt\n/usr/share/sympow/datafiles/A019S.txt\n/usr/share/sympow/datafiles/A01OM.txt\n/usr/share/sympow/datafiles/A01OS.txt\n/usr/share/sympow/datafiles/M02HM.txt\n/usr/share/sympow/datafiles/M02HS.txt\n/usr/share/sympow/datafiles/M02LM.txt\n/usr/share/sympow/datafiles/M02LS.txt\n/usr/share/sympow/datafiles/m01EM.txt\n/usr/share/sympow/datafiles/m01ES.txt\n/usr/share/sympow/datafiles/m02EM.txt\n/usr/share/sympow/datafiles/m02ES.txt\n/usr/share/sympow/datafiles/param_data\n/usr/share/sympow/standard1.gp\n/usr/share/sympow/standard2.gp\n/usr/share/sympow/standard3.gp\n```\n\n\n```\n$ find ~/.sympow/\n/home/mjo/.sympow/\n/home/mjo/.sympow/datafiles\n/home/mjo/.sympow/datafiles/le64\n/home/mjo/.sympow/datafiles/le64/A014M.bin\n/home/mjo/.sympow/datafiles/le64/A01OM.bin\n/home/mjo/.sympow/datafiles/le64/A015M.bin\n/home/mjo/.sympow/datafiles/le64/M02LM.bin\n/home/mjo/.sympow/datafiles/le64/M02HM.bin\n/home/mjo/.sympow/datafiles/le64/A017M.bin\n/home/mjo/.sympow/datafiles/le64/A012M.bin\n/home/mjo/.sympow/datafiles/le64/m01EM.bin\n/home/mjo/.sympow/datafiles/le64/A016M.bin\n/home/mjo/.sympow/datafiles/le64/A013M.bin\n/home/mjo/.sympow/datafiles/le64/A018M.bin\n/home/mjo/.sympow/datafiles/param_data\n```\n",
    "created_at": "2020-06-26T22:49:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4422#issuecomment-32457",
    "user": "https://github.com/orlitzky"
}
```

I think this might be obsolete. When we upgrade sympow, the new version will install some architecture-independent data files by default, and generate the others as needed (caching them in `$HOME/.sympow`). The following is what I have installed from the Gentoo package, and the new sympow SPKG will be similar:


```
$ equery f sympow
 * Searching for sympow ...
 * Contents of sci-mathematics/sympow-2.023.6:
...
/usr/share/sympow/datafiles
/usr/share/sympow/datafiles/A012M.txt
/usr/share/sympow/datafiles/A012S.txt
/usr/share/sympow/datafiles/A013M.txt
/usr/share/sympow/datafiles/A013S.txt
/usr/share/sympow/datafiles/A014M.txt
/usr/share/sympow/datafiles/A014S.txt
/usr/share/sympow/datafiles/A015M.txt
/usr/share/sympow/datafiles/A015S.txt
/usr/share/sympow/datafiles/A016M.txt
/usr/share/sympow/datafiles/A016S.txt
/usr/share/sympow/datafiles/A017M.txt
/usr/share/sympow/datafiles/A017S.txt
/usr/share/sympow/datafiles/A018M.txt
/usr/share/sympow/datafiles/A018S.txt
/usr/share/sympow/datafiles/A019M.txt
/usr/share/sympow/datafiles/A019S.txt
/usr/share/sympow/datafiles/A01OM.txt
/usr/share/sympow/datafiles/A01OS.txt
/usr/share/sympow/datafiles/M02HM.txt
/usr/share/sympow/datafiles/M02HS.txt
/usr/share/sympow/datafiles/M02LM.txt
/usr/share/sympow/datafiles/M02LS.txt
/usr/share/sympow/datafiles/m01EM.txt
/usr/share/sympow/datafiles/m01ES.txt
/usr/share/sympow/datafiles/m02EM.txt
/usr/share/sympow/datafiles/m02ES.txt
/usr/share/sympow/datafiles/param_data
/usr/share/sympow/standard1.gp
/usr/share/sympow/standard2.gp
/usr/share/sympow/standard3.gp
```


```
$ find ~/.sympow/
/home/mjo/.sympow/
/home/mjo/.sympow/datafiles
/home/mjo/.sympow/datafiles/le64
/home/mjo/.sympow/datafiles/le64/A014M.bin
/home/mjo/.sympow/datafiles/le64/A01OM.bin
/home/mjo/.sympow/datafiles/le64/A015M.bin
/home/mjo/.sympow/datafiles/le64/M02LM.bin
/home/mjo/.sympow/datafiles/le64/M02HM.bin
/home/mjo/.sympow/datafiles/le64/A017M.bin
/home/mjo/.sympow/datafiles/le64/A012M.bin
/home/mjo/.sympow/datafiles/le64/m01EM.bin
/home/mjo/.sympow/datafiles/le64/A016M.bin
/home/mjo/.sympow/datafiles/le64/A013M.bin
/home/mjo/.sympow/datafiles/le64/A018M.bin
/home/mjo/.sympow/datafiles/param_data
```

