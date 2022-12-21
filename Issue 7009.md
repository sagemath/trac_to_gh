# Issue 7009: Formatted output options for ciphertext

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-09-25 05:41:55

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

