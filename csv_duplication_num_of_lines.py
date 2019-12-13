import csv
import pprint

# 2つのCSVファイルを読み込み、各行を配列に入れる（ここでは同じディレクトリに入っているCSVファイルを指定）
# 文字コードはcp932 もし開かなかったら shift-jis か utf-8
# 今渡している sample_a.csv と sample_b.csv は総行数63であり、3行を書き換えているので出力は60になるはず
with open('sample_a.csv', encoding='cp932') as csv_a:
    reader_a = csv.reader(csv_a)
    l_a = [row for row in reader_a]

with open('sample_b.csv', encoding='cp932') as csv_b:
    reader_b = csv.reader(csv_b)
    l_b = [row for row in reader_b]

count = 0

for line_a in l_a:
    for line_b in l_b:
        if line_a == line_b:
            count += 1
            

print('完全に一致している行の数は ' + str(count))
