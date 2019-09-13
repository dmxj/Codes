# -*- coding: utf-8 -* -
'''
prettytable使用方法，生成漂亮的表格
pip install prettytable
'''
from prettytable import PrettyTable

table = PrettyTable(["animal", "ferocity"])
table.add_row(["wolverine", 100])
table.add_row(["grizzly", 87])
table.add_row(["Rabbit of Caerbannog", 110])
table.add_row(["cat", -1])
table.add_row(["platypus", 23])
table.add_row(["dolphin", 63])
table.add_row(["albatross", 44])
table.sort_key("ferocity")
table.reversesort = True

print(table)
# 打印如下：
'''
+----------------------+----------+
|        animal        | ferocity |
+----------------------+----------+
|      wolverine       |   100    |
|       grizzly        |    87    |
| Rabbit of Caerbannog |   110    |
|         cat          |    -1    |
|       platypus       |    23    |
|       dolphin        |    63    |
|      albatross       |    44    |
+----------------------+----------+
'''