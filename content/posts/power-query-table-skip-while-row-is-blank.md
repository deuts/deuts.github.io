---
title: Power Query Table.Skip While Row Is Blank
date: 2023-07-23T17:36:50+08:00
summary: Use the Table.Skip function the dynamic way.
tags:
  - power-query
slug: power-query-table-skip-while-row-is-blank
---

There are times that you you want to use the Table.Skip Power Query function, but the number of rows you want to skip varies from file to file in your folder. You want the number of rows to be dynamic.

The function below will count the number of rows under the column `Column4` while the rows are nulls.

```
Table.Skip(Source, each [Column4] = null)
```

Watch the [video](https://youtu.be/A5KxZhuwhv4?t=269).
