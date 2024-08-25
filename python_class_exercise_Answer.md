## 初級編（30問）

#### exercise01
`print()`関数を使用して、"こんにちは、世界"と表示するプログラムを書きなさい。

```python 
print("こんにちは、世界")
```

#### exercise02
変数`x`に10を代入し、それを`print()`関数で表示しなさい。

```python
x = 10
print(x)
```

#### exercise03
変数`a`に3、`b`に5を代入し、それらを足した結果を表示しなさい。

```python
a = 3
b = 5
print(a + b)
```

#### exercise04
`input()`関数を使って、ユーザーに名前を尋ね、それを表示するプログラムを書きなさい。

```python
name = input("名前を入力してください: ")
print("こんにちは、" + name)
```

#### exercise05
リスト`fruits`に'リンゴ', 'バナナ', 'オレンジ'を格納し、その内容を表示しなさい。

```python
fruits = ['リンゴ', 'バナナ', 'オレンジ']
print(fruits)
```

#### exercise06
リスト`numbers`に1から5までの整数を格納し、その合計を表示しなさい。

```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
```

#### exercise07
2つの整数を入力し、その積を表示するプログラムを書きなさい。

```python
a = int(input("1つ目の数: "))
b = int(input("2つ目の数: "))
print(a * b)
```

#### exercise08
文字列`hello`を3回繰り返して表示しなさい。

```python
print("hello" * 3)
```

#### exercise09
変数`x`の値が10以上かどうかを判定し、結果を表示しなさい。

```python
x = 15
if x >= 10:
    print("xは10以上です")
```

#### exercise10
`for`ループを使って、1から5までの数字を1つずつ表示しなさい。

```python
for i in range(1, 6):
    print(i)
```

exercise11
2つの変数aとbを入れ替えるプログラムを書きなさい。

```python 
a = 5 b = 10 a, b = b, a print(a, b)
```

#### exercise12
`while`ループを使って、1から10までの数を順番に表示しなさい。

```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

#### exercise13
`if`文を使って、入力された数が正の数かどうかを判定するプログラムを書きなさい。

```python
num = int(input("数を入力してください: "))
if num > 0:
    print("正の数です")
else:
    print("正の数ではありません")
```

#### exercise14
リスト`numbers`に1から5までの数字が入っているとします。これらを逆順に表示しなさい。

```python
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])
```

#### exercise15
リストの中にあるすべての要素を2倍にして表示するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(doubled)
```

#### exercise16
`for`ループを使って、リスト`fruits`の中にあるすべての要素を順番に表示しなさい。

```python
fruits = ['リンゴ', 'バナナ', 'オレンジ']
for fruit in fruits:
    print(fruit)
```

#### exercise17
3つの変数`a`, `b`, `c`の中で最大の数を判定するプログラムを書きなさい。

```python
a = 3
b = 8
c = 5
max_value = max(a, b, c)
print("最大値は", max_value)
```

#### exercise18
リストの要素数を表示するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
print("リストの要素数:", len(numbers))
```

#### exercise19
`range()`関数を使って、1から10までの数を表示するプログラムを書きなさい。

```python
for i in range(1, 11):
    print(i)
```

#### exercise20
リスト内の特定の値を削除するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)
```

#### exercise21
2つのリスト`list1`と`list2`を結合して、新しいリストとして表示しなさい。

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)
```

#### exercise22
リストの中の最大値を表示するプログラムを書きなさい。

```python
numbers = [2, 4, 6, 8, 10]
print("最大値:", max(numbers))
```

#### exercise23
3つの異なる文字列を入力させ、それらを1つの文字列に結合して表示しなさい。

```python
str1 = input("1つ目の文字列: ")
str2 = input("2つ目の文字列: ")
str3 = input("3つ目の文字列: ")
combined = str1 + str2 + str3
print(combined)
```

#### exercise24
`if`文を使って、入力された数が偶数か奇数かを判定するプログラムを書きなさい。

```python
num = int(input("数を入力してください: "))
if num % 2 == 0:
    print("偶数です")
else:
    print("奇数です")
```

#### exercise25
`for`ループと`if`文を使って、リストの中にある偶数の要素だけを表示しなさい。

```python
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(num)
```

#### exercise26
`continue`を使って、1から5までの数のうち3だけを飛ばして表示しなさい。

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

#### exercise27
リストの各要素を2乗して表示するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)
```

#### exercise28
リスト内のすべての値が正の数かどうかを判定するプログラムを書きなさい。

```python
numbers = [1, 2, 3, -4, 5]
all_positive = all(x > 0 for x in numbers)
print(all_positive)
```

#### exercise29
リストの中に特定の値が存在するかどうかを確認するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
if 3 in numbers:
    print("3はリストに存在します")
```

#### exercise30
`for`ループを使って、0から9までの数を二乗して表示しなさい。

```python
for i in range(10):
    print(i ** 2)
```

中級編 (30問)
exercise31
2つのリストlist1とlist2があるとします。それらの要素を交互に組み合わせた新しいリストを作成しなさい。

```python 
list1 = [1, 2, 3] list2 = ['a', 'b', 'c'] combined = [item for pair in zip(list1, list2) for item in pair] print(combined)
```

#### exercise32
`for`ループを使って、リスト内のすべての要素を1つずつ左にシフトさせるプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
shifted = numbers[1:] + [numbers[0]]
print(shifted)
```

#### exercise33
`input()`を使って、ユーザーから複数の数値を入力させ、それらの平均値を計算しなさい。

```python
numbers = input("カンマで区切って数値を入力してください: ").split(',')
numbers = [int(num) for num in numbers]
average = sum(numbers) / len(numbers)
print("平均値:", average)
```

#### exercise34
リストの中で、最大の数のインデックス（位置）を表示するプログラムを書きなさい。

```python
numbers = [3, 6, 2, 8, 4]
max_value = max(numbers)
max_index = numbers.index(max_value)
print("最大の数:", max_value, "インデックス:", max_index)
```

#### exercise35
`while`ループを使って、ユーザーにパスワードを入力させ、正しいパスワードが入力されるまでループを続けるプログラムを書きなさい。

```python
correct_password = "secret"
password = ""
while password != correct_password:
    password = input("パスワードを入力してください: ")
print("正しいパスワードが入力されました")
```

#### exercise36
リストの中にある値の合計が100になる最初の位置（インデックス）を見つけるプログラムを書きなさい。

```python
numbers = [10, 20, 30, 40, 50]
cumulative_sum = 0
for i, num in enumerate(numbers):
    cumulative_sum += num
    if cumulative_sum >= 100:
        print("合計が100以上になったインデックス:", i)
        break
```

#### exercise37
ユーザーが指定した回数だけ、ランダムな数値を生成し、その平均値を表示するプログラムを書きなさい。

```python
import random
count = int(input("生成する数値の回数を指定してください: "))
random_numbers = [random.randint(1, 100) for _ in range(count)]
average = sum(random_numbers) / len(random_numbers)
print("生成された数値の平均値:", average)
```

#### exercise38
2つのリスト`list1`と`list2`が完全に一致するかどうかを判定するプログラムを書きなさい。

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
if list1 == list2:
    print("リストは一致しています")
else:
    print("リストは一致していません")
```

#### exercise39
指定した値がリストのどこにあるか（インデックス）を返すプログラムを書きなさい。値がリストに存在しない場合は、-1を返すようにします。

```python
numbers = [10, 20, 30, 40, 50]
value = 30
if value in numbers:
    index = numbers.index(value)
else:
    index = -1
print("値のインデックス:", index)
```

#### exercise40
リスト内のすべての要素を掛け合わせた積を計算するプログラムを書きなさい。

```python
numbers = [2, 3, 4]
product = 1
for num in numbers:
    product *= num
print("積:", product)
```

#### exercise41
2つの文字列を入力させ、それらがアナグラム（文字の順序を入れ替えて同じ文字を使っている単語）かどうかを判定するプログラムを書きなさい。

```python
str1 = input("1つ目の文字列: ")
str2 = input("2つ目の文字列: ")
if sorted(str1) == sorted(str2):
    print("アナグラムです")
else:
    print("アナグラムではありません")
```

#### exercise42
2次元リスト`matrix`の各行の合計を計算して表示しなさい。

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    print("行の合計:", sum(row))
```

#### exercise43
タプル`my_tuple`の中から最大値と最小値を見つけるプログラムを書きなさい。

```python
my_tuple = (5, 3, 9, 1, 7)
print("最大値:", max(my_tuple))
print("最小値:", min(my_tuple))
```

#### exercise44
ユーザーが入力した複数の単語を辞書型に変換し、それぞれの単語とその長さを表示しなさい。

```python
words = input("単語をスペースで区切って入力してください: ").split()
word_dict = {word: len(word) for word in words}
print(word_dict)
```

#### exercise45
リスト内の要素の順序を逆にするプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)
```

#### exercise46
リストの中の重複した要素を削除し、重複のないリストを表示するプログラムを書きなさい。

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)
```

#### exercise47
3つのリスト`list1`, `list2`, `list3`があるとします。それらを使って、全ての要素を掛け合わせた積を計算しなさい。

```python
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]
product = 1
for a in list1:
    for b in list2:
        for c in list3:
            product *= a * b * c
print("積:", product)
```

#### exercise48
リスト内の値がすべて偶数かどうかを確認するプログラムを書きなさい。

```python
numbers = [2, 4, 6, 8]
all_even = all(num % 2 == 0 for num in numbers)
print(all_even)
```

#### exercise49
タプルのリスト`tuples`があるとします。すべてのタプルの中で2番目の要素を合計するプログラムを書きなさい。

```python
tuples = [(1, 2), (3, 4), (5, 6)]
second_elements_sum = sum(t[1] for t in tuples)
print("2番目の要素の合計:", second_elements_sum)
```

#### exercise50
`enumerate()`を使って、リストの中の要素とそのインデックスを同時に表示しなさい。

```python
fruits = ['リンゴ', 'バナナ', 'オレンジ']
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

exercise51
2つのリストlist1とlist2の各要素を足し合わせ、新しいリストを作成しなさい。

```python 
list1 = [1, 2, 3] list2 = [4, 5, 6] summed_list = [a + b for a, b in zip(list1, list2)] print(summed_list)
```

#### exercise52
ユーザーが入力した文から、最も多く出現する文字を見つけるプログラムを書きなさい。

```python
sentence = input("文章を入力してください: ")
most_frequent_char = max(set(sentence), key=sentence.count)
print("最も多く出現する文字:", most_frequent_char)
```

#### exercise53
リスト内の文字列を、アルファベット順にソートしなさい。

```python
fruits = ['オレンジ', 'リンゴ', 'バナナ']
sorted_fruits = sorted(fruits)
print(sorted_fruits)
```

#### exercise54
リスト内の偶数の数を数えるプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5, 6]
even_count = sum(1 for num in numbers if num % 2 == 0)
print("偶数の数:", even_count)
```

#### exercise55
タプルのリスト`tuples`を、各タプルの最初の要素に基づいてソートしなさい。

```python
tuples = [(3, 2), (1, 4), (5, 1)]
sorted_tuples = sorted(tuples, key=lambda x: x[0])
print(sorted_tuples)
```

#### exercise56
文字列のリストを、各文字列の長さに基づいてソートしなさい。

```python
words = ['apple', 'banana', 'cherry']
sorted_words = sorted(words, key=len)
print(sorted_words)
```

#### exercise57
ユーザーが入力した数値リストを、偶数と奇数に分けるプログラムを書きなさい。

```python
numbers = list(map(int, input("数値をスペースで区切って入力してください: ").split()))
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("偶数:", even_numbers)
print("奇数:", odd_numbers)
```

#### exercise58
ユーザーが指定した範囲のフィボナッチ数列を生成するプログラムを書きなさい。

```python
n = int(input("フィボナッチ数列の長さを入力してください: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
print(fib)
```

#### exercise59
リストの要素を、重複を許さずに順番を保持したままフィルタリングするプログラムを書きなさい。

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
filtered_numbers = list(dict.fromkeys(numbers))
print(filtered_numbers)
```

#### exercise60
指定したリスト内のすべての要素の和を計算しなさい。ただし、負の数が出た時点で計算を停止します。

```python
numbers = [1, 2, -3, 4, 5]
total = 0
for num in numbers:
    if num < 0:
        break
    total += num
print("合計:", total)
```


### 上級編 (20問)

#### exercise61
ユーザーが入力した2次元リストを転置するプログラムを書きなさい。

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)
```

#### exercise62
リスト内の要素がすべて異なるかどうかを判定するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
if len(numbers) == len(set(numbers)):
    print("すべての要素が異なります")
else:
    print("重複する要素があります")
```

#### exercise63
2つの2次元リストの要素を、対応する位置で掛け合わせた新しい2次元リストを作成しなさい。

```python
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
product_matrix = [[a * b for a, b in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]
print(product_matrix)
```

#### exercise64
リストの要素がすべて回文であるかどうかを判定するプログラムを書きなさい。

```python
words = ['level', 'radar', 'world']
all_palindrome = all(word == word[::-1] for word in words)
print(all_palindrome)
```

#### exercise65
リスト内の要素をソートする際、奇数は昇順、偶数は降順でソートするプログラムを書きなさい。

```python
numbers = [5, 3, 2, 8, 7, 1]
odds = sorted([num for num in numbers if num % 2 != 0])
evens = sorted([num for num in numbers if num % 2 == 0], reverse=True)
sorted_list = odds + evens
print(sorted_list)
```


exercise66
ユーザーが入力した数値のリストを、正の数、負の数、ゼロに分類するプログラムを書きなさい。

```python 
numbers = list(map(int, input("数値をスペースで区切って入力してください: ").split())) positive = [num for num in numbers if num > 0] negative = [num for num in numbers if num < 0] zero = [num for num in numbers if num == 0] print("正の数:", positive) print("負の数:", negative) print("ゼロ:", zero)
```

#### exercise67
ユーザーが入力した文字列を逆順にして出力するプログラムを書きなさい。

```python
sentence = input("文字列を入力してください: ")
reversed_sentence = sentence[::-1]
print("逆順:", reversed_sentence)
```

#### exercise68
指定したリスト内の要素のうち、最も頻繁に出現する要素を見つけるプログラムを書きなさい。

```python
numbers = [1, 2, 3, 1, 2, 1, 4, 1]
most_frequent = max(set(numbers), key=numbers.count)
print("最も頻繁に出現する要素:", most_frequent)
```

#### exercise69
複数のリストから共通の要素を見つけるプログラムを書きなさい。

```python
list1 = [1, 2, 3]
list2 = [3, 4, 5]
common_elements = list(set(list1) & set(list2))
print("共通の要素:", common_elements)
```

#### exercise70
2次元リストの各行を逆順にしなさい。

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
reversed_matrix = [row[::-1] for row in matrix]
print(reversed_matrix)
```

#### exercise71
指定された2次元リスト内のすべての要素の和を計算しなさい。

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total_sum = sum(sum(row) for row in matrix)
print("総和:", total_sum)
```

#### exercise72
2つの2次元リストを加算するプログラムを書きなさい。

```python
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
sum_matrix = [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]
print(sum_matrix)
```

#### exercise73
指定された2次元リスト内の最大値と最小値を見つけるプログラムを書きなさい。

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_value = max(max(row) for row in matrix)
min_value = min(min(row) for row in matrix)
print("最大値:", max_value)
print("最小値:", min_value)
```

#### exercise74
ユーザーが入力した2次元リストのすべての要素を1次元リストに変換するプログラムを書きなさい。

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [element for row in matrix for element in row]
print(flattened)
```

#### exercise75
2次元リストを、各行ごとに和を計算して出力するプログラムを書きなさい。

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row_sums = [sum(row) for row in matrix]
print(row_sums)
```

### 挑戦問題 (続き)

#### exercise76
2次元リストの対角線上の要素を取り出し、その平均を求めなさい。

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal_elements = [matrix[i][i] for i in range(len(matrix))]
diagonal_avg = sum(diagonal_elements) / len(diagonal_elements)
print("対角線の平均:", diagonal_avg)
```

#### exercise77
リスト内のすべての要素が同じであるかを確認するプログラムを書きなさい。

```python
numbers = [1, 1, 1, 1]
if all(num == numbers[0] for num in numbers):
    print("すべての要素が同じです")
else:
    print("異なる要素があります")
```

#### exercise78
2つのリストの要素が1対1で対応しているかを確認するプログラムを書きなさい。

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
if len(list1) == len(list2):
    print("1対1で対応しています")
else:
    print("対応していません")
```

#### exercise79
ユーザーが入力した文字列内のすべての単語を逆順にして出力するプログラムを書きなさい。

```python
sentence = input("文章を入力してください: ")
words = sentence.split()
reversed_words = ' '.join(reversed(words))
print("逆順の単語:", reversed_words)
```

#### exercise80
2つのリストの要素を交互に結合し、新しいリストを作成するプログラムを書きなさい。

```python
list1 = [1, 3, 5]
list2 = [2, 4, 6]
combined_list = [item for pair in zip(list1, list2) for item in pair]
print(combined_list)
```


exercise81
リスト内の各要素の平方を計算し、新しいリストに保存するプログラムを書きなさい。

```python 
numbers = [1, 2, 3, 4] squared_numbers = [num ** 2 for num in numbers] print("平方リスト:", squared_numbers)
```

#### exercise82
2つの文字列がアナグラムかどうかを判断するプログラムを書きなさい。

```python
str1 = input("最初の文字列を入力してください: ")
str2 = input("2番目の文字列を入力してください: ")
is_anagram = sorted(str1) == sorted(str2)
print("アナグラム:", is_anagram)
```

#### exercise83
ユーザーが入力したリストから、リスト内の各要素の出現回数をカウントして表示するプログラムを書きなさい。

```python
from collections import Counter

items = input("リストの要素をカンマで区切って入力してください: ").split(',')
counter = Counter(items)
for item, count in counter.items():
    print(f"{item}: {count}回")
```

#### exercise84
指定されたリストから、指定された値を含まないリストを作成するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
value_to_remove = 3
filtered_numbers = [num for num in numbers if num != value_to_remove]
print("フィルタリング後のリスト:", filtered_numbers)
```

#### exercise85
リスト内の要素をソートし、昇順で表示するプログラムを書きなさい。

```python
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("ソートされたリスト:", sorted_numbers)
```

#### exercise86
指定された文字列内で最も頻繁に出現する文字を見つけるプログラムを書きなさい。

```python
text = "hello world"
most_common_char = max(set(text), key=text.count)
print("最も頻繁に出現する文字:", most_common_char)
```

#### exercise87
指定されたリスト内のすべての数値の和と平均を計算し、表示するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)
average = total_sum / len(numbers)
print("和:", total_sum)
print("平均:", average)
```

#### exercise88
リスト内の要素を一つ一つ確認し、リスト内のすべての要素が正の数かどうかを判断するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
all_positive = all(num > 0 for num in numbers)
print("すべての要素が正の数:", all_positive)
```

#### exercise89
指定されたリストから、指定された値のインデックスを返すプログラムを書きなさい。

```python
numbers = [10, 20, 30, 40, 50]
value_to_find = 30
index = numbers.index(value_to_find) if value_to_find in numbers else -1
print("値のインデックス:", index)
```

#### exercise90
複数の文字列を含むリストを作成し、そのリストを1つの文字列に結合するプログラムを書きなさい。

```python
strings = ["Python", "is", "fun"]
combined_string = ' '.join(strings)
print("結合した文字列:", combined_string)
```

#### exercise91
リスト内の重複した要素を削除し、一意の要素だけを含むリストを作成するプログラムを書きなさい。

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("一意の要素:", unique_numbers)
```

#### exercise92
指定された範囲内の数値のリストを作成し、そのリストを逆順に並べるプログラムを書きなさい。

```python
start = 1
end = 10
numbers = list(range(start, end + 1))
reversed_numbers = numbers[::-1]
print("逆順のリスト:", reversed_numbers)
```

#### exercise93
指定された文字列内のすべての単語の長さをリストにして表示するプログラムを書きなさい。

```python
text = "This is a test"
word_lengths = [len(word) for word in text.split()]
print("単語の長さ:", word_lengths)
```

#### exercise94
リスト内の要素のうち、最も長い文字列を見つけるプログラムを書きなさい。

```python
strings = ["short", "medium", "verylongstring"]
longest_string = max(strings, key=len)
print("最も長い文字列:", longest_string)
```

#### exercise95
指定されたリスト内の要素をすべて大文字に変換するプログラムを書きなさい。

```python
strings = ["hello", "world"]
uppercase_strings = [string.upper() for string in strings]
print("大文字に変換したリスト:", uppercase_strings)
```

#### exercise96
リストの各要素が文字列の場合、それぞれの要素の長さをリストにして出力するプログラムを書きなさい。

```python
strings = ["hello", "world", "python"]
lengths = [len(string) for string in strings]
print("各文字列の長さ:", lengths)
```

#### exercise97
ユーザーが指定した数のフィボナッチ数列を生成するプログラムを書きなさい。

```python
n = int(input("フィボナッチ数列の要素数を入力してください: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
print("フィボナッチ数列:", fib[:n])
```

#### exercise98
リスト内の数値をすべて平方し、その平方根を計算して出力するプログラムを書きなさい。

```python
import math

numbers = [1, 4, 9, 16]
squared_numbers = [num ** 2 for num in numbers]
square_roots = [math.sqrt(num) for num in squared_numbers]
print("平方根:", square_roots)
```

#### exercise99
指定されたリスト内の文字列の長さが最大の文字列を見つけるプログラムを書きなさい。

```python
strings = ["short", "medium", "verylongstring"]
longest_string = max(strings, key=len)
print("最大長の文字列:", longest_string)
```

#### exercise100
リスト内の数値の平均を計算し、平均値がリスト内のどの数値にも存在するかを確認するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
average = sum(numbers) / len(numbers)
exists_in_list = average in numbers
print("平均:", average)
print("平均値がリスト内に存在するか:", exists_in_list)
```

### 挑戦問題 (続き)

#### exercise81
リストの各要素のすべての組み合わせを生成するプログラムを書きなさい。

```python
from itertools import combinations

items = [1, 2, 3]
all_combinations = list(combinations(items, 2))
print("すべての組み合わせ:", all_combinations)
```


#### exercise82
2つの文字列がアナグラムかどうかを判断するプログラムを書きなさい。

```python
str1 = input("最初の文字列を入力してください: ")
str2 = input("2番目の文字列を入力してください: ")
is_anagram = sorted(str1) == sorted(str2)
print("アナグラム:", is_anagram)
```

#### exercise83
ユーザーが入力したリストから、リスト内の各要素の出現回数をカウントして表示するプログラムを書きなさい。

```python
from collections import Counter

items = input("リストの要素をカンマで区切って入力してください: ").split(',')
counter = Counter(items)
for item, count in counter.items():
    print(f"{item}: {count}回")
```

#### exercise84
指定されたリストから、指定された値を含まないリストを作成するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
value_to_remove = 3
filtered_numbers = [num for num in numbers if num != value_to_remove]
print("フィルタリング後のリスト:", filtered_numbers)
```

#### exercise85
リスト内の要素をソートし、昇順で表示するプログラムを書きなさい。

```python
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("ソートされたリスト:", sorted_numbers)
```

#### exercise86
指定された文字列内で最も頻繁に出現する文字を見つけるプログラムを書きなさい。

```python
text = "hello world"
most_common_char = max(set(text), key=text.count)
print("最も頻繁に出現する文字:", most_common_char)
```

#### exercise87
指定されたリスト内のすべての数値の和と平均を計算し、表示するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)
average = total_sum / len(numbers)
print("和:", total_sum)
print("平均:", average)
```

#### exercise88
リスト内の要素を一つ一つ確認し、リスト内のすべての要素が正の数かどうかを判断するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
all_positive = all(num > 0 for num in numbers)
print("すべての要素が正の数:", all_positive)
```

#### exercise89
指定されたリストから、指定された値のインデックスを返すプログラムを書きなさい。

```python
numbers = [10, 20, 30, 40, 50]
value_to_find = 30
index = numbers.index(value_to_find) if value_to_find in numbers else -1
print("値のインデックス:", index)
```

#### exercise90
複数の文字列を含むリストを作成し、そのリストを1つの文字列に結合するプログラムを書きなさい。

```python
strings = ["Python", "is", "fun"]
combined_string = ' '.join(strings)
print("結合した文字列:", combined_string)
```

#### exercise91
リスト内の重複した要素を削除し、一意の要素だけを含むリストを作成するプログラムを書きなさい。

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("一意の要素:", unique_numbers)
```

#### exercise92
指定された範囲内の数値のリストを作成し、そのリストを逆順に並べるプログラムを書きなさい。

```python
start = 1
end = 10
numbers = list(range(start, end + 1))
reversed_numbers = numbers[::-1]
print("逆順のリスト:", reversed_numbers)
```

#### exercise93
指定された文字列内のすべての単語の長さをリストにして表示するプログラムを書きなさい。

```python
text = "This is a test"
word_lengths = [len(word) for word in text.split()]
print("単語の長さ:", word_lengths)
```

#### exercise94
リスト内の要素のうち、最も長い文字列を見つけるプログラムを書きなさい。

```python
strings = ["short", "medium", "verylongstring"]
longest_string = max(strings, key=len)
print("最も長い文字列:", longest_string)
```

#### exercise95
指定されたリスト内の要素をすべて大文字に変換するプログラムを書きなさい。

```python
strings = ["hello", "world"]
uppercase_strings = [string.upper() for string in strings]
print("大文字に変換したリスト:", uppercase_strings)
```

#### exercise96
リストの各要素が文字列の場合、それぞれの要素の長さをリストにして出力するプログラムを書きなさい。

```python
strings = ["hello", "world", "python"]
lengths = [len(string) for string in strings]
print("各文字列の長さ:", lengths)
```

#### exercise97
ユーザーが指定した数のフィボナッチ数列を生成するプログラムを書きなさい。

```python
n = int(input("フィボナッチ数列の要素数を入力してください: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
print("フィボナッチ数列:", fib[:n])
```

#### exercise98
リスト内の数値をすべて平方し、その平方根を計算して出力するプログラムを書きなさい。

```python
import math

numbers = [1, 4, 9, 16]
squared_numbers = [num ** 2 for num in numbers]
square_roots = [math.sqrt(num) for num in squared_numbers]
print("平方根:", square_roots)
```

#### exercise99
指定されたリスト内の文字列の長さが最大の文字列を見つけるプログラムを書きなさい。

```python
strings = ["short", "medium", "verylongstring"]
longest_string = max(strings, key=len)
print("最大長の文字列:", longest_string)
```

#### exercise100
リスト内の数値の平均を計算し、平均値がリスト内のどの数値にも存在するかを確認するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
average = sum(numbers) / len(numbers)
exists_in_list = average in numbers
print("平均:", average)
print("平均値がリスト内に存在するか:", exists_in_list)
```

### 挑戦問題 (続き)

#### exercise81
リストの各要素のすべての組み合わせを生成するプログラムを書きなさい。

```python
from itertools import combinations

items = [1, 2, 3]
all_combinations = list(combinations(items, 2))
print("すべての組み合わせ:", all_combinations)
```

#### exercise82
複数のファイルを1つに結合し、その内容を新しいファイルに書き込むプログラムを書きなさい。

```python
files = ['file1.txt', 'file2.txt']
with open('combined.txt', 'w') as outfile:
    for fname in files:
        with open(fname) as infile:
            outfile.write(infile.read())
```

#### exercise83
クラスを使用して、学生の情報を管理するシステムを作成しなさい。学生の名前、年齢、成績を保持し、表示するメソッドを実装してください。

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        print(f"名前: {self.name}, 年齢: {self.age}, 成績: {self.grade}")

student = Student("Alice", 20, 90)
student.display_info()
```

#### exercise84
指定されたタプル内の要素をリストに変換し、そのリストのすべての要素を逆順に並べるプログラムを書きなさい。

```python
tup = (1, 2, 3, 4)
lst = list(tup)
reversed_lst = lst[::-1]
print("逆順のリスト:", reversed_lst)
```

#### exercise85
複数のCSVファイルを読み込み、その内容を統合して1つのデータフレームとして表示するプログラムを書きなさい。

```python
import pandas as pd

files = ['file1.csv', 'file2.csv']
df_list = [pd.read_csv(file) for file in files]
combined_df = pd.concat(df_list, ignore_index=True)
print("統合されたデータフレーム:")
print(combined_df)
```

exercise86
リスト内の各要素を指定された回数だけ繰り返して新しいリストを作成するプログラムを書きなさい。

```python 
items = [1, 2, 3] repeat_count = 3 repeated_list = [item for item in items for _ in range(repeat_count)] print("繰り返しリスト:", repeated_list)
```

#### exercise87
ユーザーが指定したリスト内の要素の合計を計算し、その合計が10の倍数かどうかを確認するプログラムを書きなさい。

```python
numbers = [int(x) for x in input("リストの要素をカンマで区切って入力してください: ").split(',')]
total_sum = sum(numbers)
is_multiple_of_10 = total_sum % 10 == 0
print("合計:", total_sum)
print("合計が10の倍数か:", is_multiple_of_10)
```

#### exercise88
指定されたリスト内の最小値と最大値の差を計算するプログラムを書きなさい。

```python
numbers = [5, 2, 9, 1, 5, 6]
min_value = min(numbers)
max_value = max(numbers)
difference = max_value - min_value
print("最小値:", min_value)
print("最大値:", max_value)
print("差:", difference)
```

#### exercise89
リスト内の数値の中央値を計算するプログラムを書きなさい。

```python
import statistics

numbers = [1, 2, 3, 4, 5]
median = statistics.median(numbers)
print("中央値:", median)
```

#### exercise90
指定された数の整数を生成し、その中から偶数のみを抽出して新しいリストを作成するプログラムを書きなさい。

```python
import random

num_count = 10
numbers = [random.randint(1, 100) for _ in range(num_count)]
even_numbers = [num for num in numbers if num % 2 == 0]
print("生成した数:", numbers)
print("偶数のみ:", even_numbers)
```

#### exercise91
指定された範囲内の素数をリストとして生成するプログラムを書きなさい。

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start = 1
end = 30
primes = [num for num in range(start, end + 1) if is_prime(num)]
print("素数リスト:", primes)
```

#### exercise92
指定された文字列内の各単語の出現回数をカウントし、出現回数が最も多い単語を表示するプログラムを書きなさい。

```python
from collections import Counter

text = "this is a test this is only a test"
word_count = Counter(text.split())
most_common_word = word_count.most_common(1)[0][0]
print("最も多く出現する単語:", most_common_word)
```

#### exercise93
2つのリストを結合し、重複を排除した新しいリストを作成するプログラムを書きなさい。

```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
combined_list = list(set(list1 + list2))
print("重複排除後のリスト:", combined_list)
```

#### exercise94
指定された文字列が回文かどうかを判断するプログラムを書きなさい。

```python
text = input("文字列を入力してください: ")
is_palindrome = text == text[::-1]
print("回文か:", is_palindrome)
```

#### exercise95
リスト内の各要素を2倍にして新しいリストを作成するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * 2 for num in numbers]
print("2倍にしたリスト:", doubled_numbers)
```

#### exercise96
指定された文字列内のすべての母音をカウントするプログラムを書きなさい。

```python
text = "programming"
vowels = 'aeiou'
vowel_count = sum(1 for char in text if char in vowels)
print("母音の数:", vowel_count)
```

#### exercise97
指定されたリストの各要素に対して、リスト内の他のすべての要素との合計を計算するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4]
sums = [sum(numbers) - num for num in numbers]
print("各要素を除いた合計:", sums)
```

#### exercise98
指定された数のフィボナッチ数列の中で、最も大きな数が10の倍数であるかを判断するプログラムを書きなさい。

```python
n = int(input("フィボナッチ数列の要素数を入力してください: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
is_last_multiple_of_10 = fib[-1] % 10 == 0
print("最も大きな数:", fib[-1])
print("最も大きな数が10の倍数か:", is_last_multiple_of_10)
```

#### exercise99
リスト内の文字列の長さが奇数の文字列だけを含む新しいリストを作成するプログラムを書きなさい。

```python
strings = ["hello", "world", "python", "code"]
odd_length_strings = [string for string in strings if len(string) % 2 == 1]
print("奇数長の文字列:", odd_length_strings)
```

#### exercise100
指定されたリスト内の文字列の各文字を逆順にして新しいリストを作成するプログラムを書きなさい。

```python
strings = ["hello", "world"]
reversed_strings = [string[::-1] for string in strings]
print("逆順の文字列リスト:", reversed_strings)
```

### 挑戦問題 (続き)

#### exercise86
2つのリストを受け取り、リスト内の要素の共通部分をリストとして返すプログラムを書きなさい。

```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = [item for item in list1 if item in list2]
print("共通部分:", common_elements)
```

#### exercise87
ユーザーが入力した2つの文字列の長さを比較し、長い方の文字列を表示するプログラムを書きなさい。

```python
str1 = input("1つ目の文字列を入力してください: ")
str2 = input("2つ目の文字列を入力してください: ")
longer_str = str1 if len(str1) > len(str2) else str2
print("長い文字列:", longer_str)
```

#### exercise88
指定された範囲内の全素数をリストとして生成し、そのリストをファイルに保存するプログラムを書きなさい。

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start = 1
end = 50
primes = [num for num in range(start, end + 1) if is_prime(num)]

with open('primes.txt', 'w') as file:
    for prime in primes:
        file.write(f"{prime}\n")

print("素数リストをファイルに保存しました。")
```

#### exercise89
指定された文字列をリストの各要素と比較し、文字列がリスト内に存在するかを確認するプログラムを書きなさい。

```python
strings = ["apple", "banana", "cherry"]
search_str = input("検索する文字列を入力してください: ")
exists = search_str in strings
print("文字列がリスト内に存在するか:", exists)
```

#### exercise90
指定された数の要素を持つタプルを生成し、そのタプル内の要素をすべて合計するプログラムを書きなさい。

```python
n = int(input("タプルの要素数を入力してください: "))
tup = tuple(range(1, n + 1))
total_sum = sum(tup)
print("タプル:", tup)

exercise91
与えられたリストをシャッフルし、シャッフル後のリストをファイルに保存するプログラムを書きなさい。

```python import random

items = [1, 2, 3, 4, 5] random.shuffle(items)

with open('shuffled_list.txt', 'w') as file: for item in items: file.write(f"{item}\n")

print("シャッフル後のリストをファイルに保存しました。")


#### exercise92
指定されたリストの各要素に対して、リスト内の他の要素との最大の差を計算するプログラムを書きなさい。

```python
numbers = [1, 2, 3, 4, 5]
max_diff = max(numbers) - min(numbers)
print("リスト内の最大の差:", max_diff)
```

#### exercise93
ユーザーが入力した2つの文字列の各文字を比較し、同じ文字を持つリストを作成するプログラムを書きなさい。

```python
str1 = input("1つ目の文字列を入力してください: ")
str2 = input("2つ目の文字列を入力してください: ")
common_chars = [char for char in str1 if char in str2]
print("共通の文字:", common_chars)
```

#### exercise94
指定された数の要素を持つリストを生成し、そのリストの中で最も頻繁に出現する要素をカウントするプログラムを書きなさい。

```python
from collections import Counter

n = int(input("リストの要素数を入力してください: "))
items = [i % 3 for i in range(n)]  # 例として0, 1, 2が繰り返されるリストを生成
frequency = Counter(items)
most_common_element = frequency.most_common(1)[0]
print("最も頻繁に出現する要素とその数:", most_common_element)
```

#### exercise95
指定された数の要素を持つリストを生成し、各要素の平方根を計算して新しいリストを作成するプログラムを書きなさい。

```python
import math

n = int(input("リストの要素数を入力してください: "))
items = list(range(1, n + 1))
square_roots = [math.sqrt(item) for item in items]
print("各要素の平方根:", square_roots)
```

#### exercise96
指定された数の整数をリストとして生成し、そのリスト内で最も大きな数の平方を計算するプログラムを書きなさい。

```python
import random

n = int(input("リストの要素数を入力してください: "))
numbers = [random.randint(1, 100) for _ in range(n)]
max_value = max(numbers)
squared_max = max_value ** 2
print("リスト:", numbers)
print("最大値の平方:", squared_max)
```

#### exercise97
指定された文字列内のすべての大文字を小文字に変換し、変換後の文字列を表示するプログラムを書きなさい。

```python
text = input("文字列を入力してください: ")
lowercase_text = text.lower()
print("小文字に変換した文字列:", lowercase_text)
```

#### exercise98
ユーザーが指定した数の整数をリストとして生成し、そのリスト内のすべての整数を2で割り、その結果のリストを表示するプログラムを書きなさい。

```python
n = int(input("リストの要素数を入力してください: "))
numbers = [i for i in range(1, n + 1)]
halved_numbers = [num / 2 for num in numbers]
print("リスト内の各要素を2で割った結果:", halved_numbers)
```

#### exercise99
指定されたリスト内の各文字列の長さを計算し、その長さが最大の文字列を表示するプログラムを書きなさい。

```python
strings = ["apple", "banana", "cherry"]
max_length_string = max(strings, key=len)
print("長さが最大の文字列:", max_length_string)
```

#### exercise100
リスト内の各要素に対して、その要素の指数を計算して新しいリストを作成するプログラムを書きなさい。

```python
import math

numbers = [1, 2, 3, 4, 5]
exponents = [math.exp(num) for num in numbers]
print("各要素の指数:", exponents)
```
**exercise121**  
「2つの2次元リスト（行列）を入力として受け取り、行列の積（マトリクス積）を計算するプログラムを書きなさい。」

```python
def matrix_multiplication(A, B):
    # 行列のサイズを取得
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    # 結果行列の初期化
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # 行列の積を計算
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

# サンプル入力
A = [[1, 2], [3, 4], [5, 6]]
B = [[7, 8], [9, 10]]

# 結果の表示
print(matrix_multiplication(A, B))
```
**exercise122**
「与えられた2次元リストを用いて、ユークリッド距離を計算し、2つの座標間の距離を求めるプログラムを書きなさい。」

```python
import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# サンプル入力
coordinates = [[0, 0], [3, 4]]

# ユークリッド距離の計算
distance = euclidean_distance(coordinates[0], coordinates[1])
print(f"距離: {distance}")
```

**exercise123**
「ユーザーから正の整数を入力させ、その数の約数を全てリストに格納し、さらにその約数が素数であるかどうかを判定するプログラムを書きなさい。最終的に素数の約数だけを表示しなさい。」

```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    prime_divisors = [d for d in divisors if is_prime(d)]
    return prime_divisors

# ユーザーからの入力
n = int(input("正の整数を入力してください: "))

# 結果の表示
print(f"{n}の素数の約数: {find_prime_divisors(n)}")
```
**exercise124**
「クラスを使って2次元ベクトルの加算、減算、内積を実装するプログラムを書きなさい。」

```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

# サンプルベクトル
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

# ベクトルの演算
v_add = v1 + v2
v_sub = v1 - v2
v_dot = v1.dot(v2)

# 結果の表示
print(f"ベクトルの加算: {v_add}")
print(f"ベクトルの減算: {v_sub}")
print(f"ベクトルの内積: {v_dot}")
```
**exercise125**
「トーナメント形式のゲームをシミュレーションするプログラムを書きなさい。n人のプレイヤーがランダムに対戦し、各対戦の勝者が次のラウンドに進みます。」

```python
import random

def tournament(players):
    round_num = 1
    while len(players) > 1:
        print(f"ラウンド {round_num}: {players}")
        next_round = []
        for i in range(0, len(players), 2):
            if i + 1 < len(players):
                winner = random.choice([players[i], players[i+1]])
                next_round.append(winner)
            else:
                next_round.append(players[i])  # 奇数の場合、最後のプレイヤーは自動的に次のラウンドに進む
        players = next_round
        round_num += 1
    return players[0]

# サンプルプレイヤー
players = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6']

# トーナメントシミュレーション
winner = tournament(players)
print(f"トーナメントの勝者は: {winner}")
```