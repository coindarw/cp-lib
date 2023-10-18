import json
from collections import OrderedDict
import re
import sys
import pprint

# VSCodeのスニペットのjsonを適当にパースしてmarkdownを吐く

# e.g.
# python3 description.py cpp.json

# スニペットのdescriptionのところにカテゴリを入れて分類する。
# サブカテゴリまで入力でき、CAT, SUBCATのところにハードコードしているやつをいじると変えられる
# コロンまでがカテゴリ（かサブカテゴリ）でそれ以降は説明
# ”ad:graph:ダイクストラ法”なら
#   カテゴリ: アルゴリズム，データ構造
#   サブカテゴリ: グラフ理論
#   説明: ダイクストラ法


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 description.py <path to json file>")
        sys.exit(1)

    path = sys.argv[1]

    # jsonを読み込む
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)

    # 各カテゴリー名
    CAT = OrderedDict([('unclassified', '未分類'), ('sc', 'ショートカット系'), ('io', '入出力系'), (
        'const', '定数とか'), ('func', '簡単な関数'), ('template', 'テンプレ'), ('ad', 'アルゴリズム，データ構造'), ('cp', '競プロ効率化用の関数，クラス'), ('debug', 'デバッグ，テスト関連')])
    SUBCAT = OrderedDict([('unclassified_sub', '未分類'), ('math', '数学系'), ('graph', 'グラフ理論'),
                          ('others', 'その他便利なやつ'), ('seg', 'SegTree派生のデータ構造'), ('string', '文字列関連'), ('geometry', '幾何')])

    # 整理した後のスニペット一覧
    od = OrderedDict()

    for cat, catdesc in CAT.items():
        od[cat] = OrderedDict()
        od[cat]['unclassified_sub'] = OrderedDict()

    # 各スニペットを分類
    for k, v in data.items():
        category = None
        subcategory = None
        description = v['description']
        body = v['body']

        for cat, catdesc in CAT.items():
            m = re.match(r'^' + cat + r':(.*)', v['description'])
            if m:
                category = cat
                s = m.group(1)
                for subcat, subcatdesc in SUBCAT.items():
                    sm = re.match(r'^' + subcat + r':(.*)', s)
                    if sm:
                        subcategory = subcat
                        description = sm.group(1)
                        break
                if not subcategory:
                    description = s
                break
        v['description'] = description
        if category:
            if subcategory:
                if subcategory in od[category]:
                    od[category][subcategory][k] = v
                else:
                    od[category][subcategory] = OrderedDict()
                    od[category][subcategory][k] = v
            else:
                od[category]['unclassified_sub'][k] = v
        else:
            od['unclassified']['unclassified_sub'][k] = v

    with open(path.split(sep='.')[-2] + '_description.md', 'w', encoding='utf-8') as f:
        f.write('# ' + path + '\n\n')
        f.write('[TOC]\n\n')
        for cat, subcategories in od.items():
            # 要素がある（サブカテゴリーが存在するor未分類要素が存在する）ならカテゴリー名と要素を表示
            if len(subcategories) >= 2 or len(subcategories['unclassified_sub']) > 0:
                f.write('## ' + CAT[cat] + '\n\n')
            else:
                continue

            for subcategory, elements in subcategories.items():
                if len(subcategories) >= 2 and len(elements) > 0:
                    f.write('### ' + SUBCAT[subcategory] + '\n\n')

                for name, element in elements.items():
                    f.write('<details>\n')
                    if not element['description']:
                        f.write(
                            '<summary>{} ({})</summary>\n\n'.format(name, element['prefix']))
                    else:
                        f.write('<summary>{} ({})\t{}</summary>\n\n'.format(name,
                                                                            element['prefix'], element['description']))
                    f.write('```{}.cpp\n'.format(name))
                    f.write(element['body'].replace('\r\n', '\n'))
                    f.write('\n```\n</details>\n\n')
                f.write('\n')
