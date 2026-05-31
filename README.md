# 🐧 CSV to VCF Converter

A Python script that converts contact data from a CSV file into a VCF (vCard) file that can be directly imported into Android devices.

---

## Background

At my workplace, we manage a large set of Android contacts that need to be updated regularly — phone numbers change, new contacts get added, and the list gets reorganized by area every month. On top of that, we use a specific emoji prefix on each contact name so that anyone can instantly tell whether a contact has been recently updated.

Before this tool existed, this process took about **2 hours every month** — manually editing contacts on the phone one by one.

Now, the workflow is:
1. Update the contact list in Google Sheets
2. Export as CSV
3. Run this script
4. Import the generated `.vcf` file into Android

The whole thing takes about **10 minutes**.

---

## Features

- Reads contact data from a CSV file
- Supports contacts with **one or two phone numbers**
- Automatically adds a custom emoji prefix to each contact name
- Outputs a `.vcf` file compatible with Android contacts import
- Skips empty rows automatically

---

## Requirements

- Python 3.x
- No external libraries needed (uses built-in `csv` module)

---

## CSV Format

The script expects a CSV file with a header row. Columns should be in this order:

```
Name, Phone1, Phone2 (optional)
```

Example (`test.csv`):
```
Name,Phone1,Phone2
Ohno Takashi,6271895,666-6627-1895
Ogawa Hikaru,3198075,777-3317-8075
Kojima Rio,5042136,
```

> Note: All names and phone numbers in this repo are fictional and used for testing only.

---

## Usage

1. Place your CSV file in the same directory as `main.py`
2. Open `main.py` and update these two lines near the top:

```python
new_list = load_data('your_file.csv')  # ← your CSV filename
emoji = '🐧'                            # ← your emoji prefix
```

3. Run the script:

```bash
python main.py
```

4. A file called `My_new_VCF.vcf` will be created in the same directory.
5. Transfer it to your Android device and open it to import contacts.

---

## How the Emoji Works

By changing the emoji each month, it becomes easy to visually identify which contacts are newly updated — just look for the new emoji in your contacts list.

---

## File Structure

```
CSV-to-VCF-converter/
│
├── main.py        # Main script
├── test.csv       # Sample CSV (fictional data)
└── README.md
```

---

---

# 🐧 CSV to VCF コンバーター

CSVファイルの連絡先データを、Androidに直接インポートできるVCF（vCard）ファイルへ変換するPythonスクリプトです。

---

## 背景

職場では、大量のAndroid連絡先を毎月管理する必要があります。担当エリアの変更や電話番号の追加・変更が頻繁にあり、更新のたびに手作業で一件ずつ修正していました。また、最近更新した連絡先かどうかを一目でわかるように、名前の先頭に特定の絵文字をつけるルールもあります。

このツールを作る前は、毎月この作業に**約2時間**かかっていました。

このスクリプトを使えば：
1. Google Sheetsで連絡先リストを更新
2. CSVでエクスポート
3. スクリプトを実行
4. 生成された`.vcf`ファイルをAndroidにインポート

これだけで、作業時間が**約10分**に短縮されました。

---

## 機能

- CSVファイルから連絡先データを読み込む
- **電話番号が1件または2件**の連絡先に対応
- 名前の先頭に絵文字を自動追加
- Androidの連絡先インポートに対応した`.vcf`ファイルを出力
- 空行は自動でスキップ

---

## 必要環境

- Python 3.x
- 外部ライブラリ不要（標準の`csv`モジュールを使用）

---

## CSVフォーマット

ヘッダー行あり、カラムの順番は以下の通り：

```
名前, 電話番号1, 電話番号2（任意）
```

例（`test.csv`）:
```
Name,Phone1,Phone2
Ohno Takashi,6271895,666-6627-1895
Ogawa Hikaru,3198075,777-3317-8075
Kojima Rio,5042136,
```

> ※ このリポジトリ内の名前・電話番号はすべてテスト用の架空のデータです。

---

## 使い方

1. CSVファイルを`main.py`と同じディレクトリに置く
2. `main.py`の上部にある以下の2行を変更する：

```python
new_list = load_data('your_file.csv')  # ← 自分のCSVファイル名
emoji = '🐧'                            # ← 使用する絵文字
```

3. スクリプトを実行：

```bash
python main.py
```

4. 同じディレクトリに`My_new_VCF.vcf`が生成される
5. Androidに転送して開くと、連絡先としてインポートできる

---

## 絵文字の使い方について

毎月使う絵文字を変えることで、連絡先リストを見たときに「この絵文字がついてる連絡先は今月更新した」とすぐ判断できます。

---

## ファイル構成

```
CSV-to-VCF-converter/
│
├── main.py        # メインスクリプト
├── test.csv       # サンプルCSV（架空データ）
└── README.md
```
