# 日本語ネガポジ解析

## 概要
日本語の文章のネガティブ-ポジティブを解析するPythonスクリプトです。
文章内の単語ごとにネガティブかポジティブかを判定します。

## 使い方

### スクリプトとして使う

```sh
./negpos_counter.py --str "あのプログラムは素晴らしい"

# 単語単位に分割してネガティブ・ポジティブを判定します。
# {'positive': 1, 'neutral': 0, 'negative': 0}

# ファイル内容を読み込んで解析することもできます
./negpos_counter.py --file path
```

### ライブラリとして使う
NegPosCheckerクラスをimportして単語単位での判定ができます。

```py
from jp_negapos.negapos_checker import NegPosChecker

word = '素晴らしい'

checker = NegPosChecker()

result = checker.check(word)

print(result) # 1
```

checkメソッドの返り値（int）は以下のとおりです。
* ポジティブの場合：1
* ネガティブの場合：-1
* ニュートラルの場合：0
* 辞書に存在しない場合：None

## Requirements
* janome
* six

## References
1. 小林のぞみ，乾健太郎，松本裕治，立石健二，福島俊一. 意見抽出のための評価表現の収集. 自然言語処理，Vol.12, No.3, pp.203-222, 2005. / Nozomi Kobayashi, Kentaro Inui, Yuji Matsumoto, Kenji Tateishi. Collecting Evaluative Expressions for Opinion Extraction, Journal of Natural Language Processing 12(3), 203-222, 2005.
2. 東山昌彦, 乾健太郎, 松本裕治, 述語の選択選好性に着目した名詞評価極性の獲得, 言語処理学会第14回年次大会論文集, pp.584-587, 2008. / Masahiko Higashiyama, Kentaro Inui, Yuji Matsumoto. Learning Sentiment of Nouns from Selectional Preferences of Verbs and Adjectives, Proceedings of the 14th Annual Meeting of the Association for Natural Language Processing, pp.584-587, 2008.
