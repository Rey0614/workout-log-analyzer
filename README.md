# Workout Log Analyser

このプロジェクトは筋トレの記録csvから、種目ごとの最高重量を自動で抽出する。

## なぜ作ったか
このプログラミングを作った理由としては、私の筋肉の成長の速さやどういった時に停滞期に陥っているかのような傾向を知るのに良いと思ったため。

## 使い方
必要なものとしては筋トレ記録がされているcsvファイルとそれを操作するためのpythonのコードが書かれたファイル。それらが存在するディレクトリの中で

 python3 load_data.py
を実行するとコードが動く。

## 実行結果
```bash
Smith machine bench press: 40.0
Dumbbell incline press: 45.0
Dumbbell lateral raise: 20.0
Dips: 40.0
Triceps push down: 40.0
Lat pulldown: 45.0
Barbell row: 20.0
One handed rows: 15.0
Face pull: 25.0
Dumbbell curl: 12.5
Back squat: 60.0
Leg press: 110.0
Bench press: 50.0
Chest press: 60.0
Assisted pull up: 40.0
Chest supported row: 25.0
Overhead press: 35.0
Shoulder press: 20.0
Leg extension: 50.0
Chest fly machine: 90.0
Arm curl: 10.0
Foot-Assisted Chest Press: 20.0
```
まだ試用段階であるため、見栄えは良くないが、書き出すことができ、また、それぞれの値を取り出すことも可能なので、pandasなどのライブラリを使って、データ分析が可能な状態。

## 詰まった点と解決
一番詰まった点は、記録の仕方の外れ値をどう扱うか。dipsの表記の仕方が途中で変わっている。
```
2026-08-06,Dips,7th from top,10
2026-08-14,Dips,40,10
```
理由は単純でジムでの表記が変わったからなのだが、もちろんこれだとfloat()が文字列を数値に変換できずValueErrorが起きてしまう。解決方法としては３つあり、dipsの種目自体を無視する、変更前のものは無視をする、変更前のものをプログラミングで数値に変更する（数値が分かった上で）の中で私は数値を変更することを選んだ。そのためには、正確に何が書いてあるかを調べた上で、そのすべての文字を数字と置き換える必要がある。その際、一旦、dipsだけを取り出して、文字の確認をしようとしたたが、効率的なやり方を知らない上に、既存のコードと混乱することもあり、骨が折れた。また、treadmillに関しても同じことが言えるが、これに関しては、不定期だったことと、筋肉の傾向を知るのに重要ではないと考え、省いた。その処理に関してはtry exceptを使った。
