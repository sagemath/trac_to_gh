# Issue 7009: Formatted output options for ciphertext

archive/issues_007009.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  mvngu\n\nKeywords: formatted ciphertext\n\nA formatting option for ciphertext might break the ciphertext into blocks separated by spaces, with a maximum number of blocks per line, as it is often displayed.\n\nSo parameters like `block_size=5, max_blocks=7` would produce\n\n\n```\nWKLVL VDVWU LQJRI WHAWL HQFRG HGIRU PLQKW\nRGHPR QVWUD WHKRZ DIRUP DWWLQ JFRPP DQGIR\nUFLSK HUWHA WPLJK WEUHD NWKHW HAWLQ WREOR\nFNVRI OHWWH UVDVL VRIWH QGRQH\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7009\n\n",
    "created_at": "2009-09-25T05:41:55Z",
    "labels": [
        "component: cryptography",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Formatted output options for ciphertext",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7009",
    "user": "https://github.com/rbeezer"
}
```
Assignee: somebody

CC:  mvngu

Keywords: formatted ciphertext

A formatting option for ciphertext might break the ciphertext into blocks separated by spaces, with a maximum number of blocks per line, as it is often displayed.

So parameters like `block_size=5, max_blocks=7` would produce


```
WKLVL VDVWU LQJRI WHAWL HQFRG HGIRU PLQKW
RGHPR QVWUD WHKRZ DIRUP DWWLQ JFRPP DQGIR
UFLSK HUWHA WPLJK WEUHD NWKHW HAWLQ WREOR
FNVRI OHWWH UVDVL VRIWH QGRQH
```


Issue created by migration from https://trac.sagemath.org/ticket/7009


