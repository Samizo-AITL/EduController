# 📊 Part 8: データ駆動型制御（Data-Driven Control）

本章では、数式モデルを前提とせず、**観測データから制御モデルや制御器を構築する手法**を学びます。  
現代制御やAI制御と融合しやすいこの分野は、産業界でも注目されている実用技術です。

---

## 🎯 学習目標 / Learning Objectives

- モデルフリー制御とデータ駆動制御の違いを理解する
- Koopman演算子による線形化と予測モデルの構築を学ぶ
- 動的モード分解（DMD）を用いた系の抽出を体験する
- サブスペース同定法や識別制御の考え方を習得する
- Pythonによる実験実装と可視化を行う

---

## 📁 ディレクトリ構成（予定）

```plaintext
part08_data_driven/
├── theory/
│   ├── 01_model_free_control.md
│   ├── 02_koopman_operator.md
│   ├── 03_dmd.md
│   ├── 04_subspace_id.md
│   └── 05_data_vs_model.md
├── simulation/
│   ├── koopman_linearization.py
│   ├── dmd_analysis.py
│   └── subspace_identification.py
├── notebooks/
│   └── koopman_vs_dmd_visual.ipynb
├── figures/
└── README.md
```

---

## 📚 理論資料（Markdown）

| タイトル                    | ファイル名                                      |
|-----------------------------|-------------------------------------------------|
| モデルフリー制御の基礎       | [`01_model_free_control.md`](./theory/01_model_free_control.md) |
| Koopman演算子と線形化        | [`02_koopman_operator.md`](./theory/02_koopman_operator.md)     |
| 動的モード分解（DMD）        | [`03_dmd.md`](./theory/03_dmd.md)                               |
| サブスペース同定            | [`04_subspace_id.md`](./theory/04_subspace_id.md)               |
| モデルベース制御との比較     | [`05_data_vs_model.md`](./theory/05_data_vs_model.md)           |

---

## 🧪 実験コード（Python）

- [`koopman_linearization.py`](./simulation/koopman_linearization.py)  
- [`dmd_analysis.py`](./simulation/dmd_analysis.py)  
- [`subspace_identification.py`](./simulation/subspace_identification.py)

---

## 📊 可視化Notebook

- [`koopman_vs_dmd_visual.ipynb`](./notebooks/koopman_vs_dmd_visual.ipynb)

---

## 🔜 今後の展開（Next Steps）

- Deep KoopmanやAutoencoderによる次世代識別法
- 制御対象に特化したデータ拡張・識別器設計
- AITL構想への応用（観測に基づく学習制御）
