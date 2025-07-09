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

## 🧩 主なトピック / Key Topics

| トピック | 内容 |
|----------|------|
| Koopman制御 | 非線形系を線形作用素として近似・制御 |
| 動的モード分解（DMD） | データからシステムダイナミクスを抽出 |
| サブスペース同定 | 行列演算に基づく状態空間モデルの推定 |
| 識別制御 | 入出力データから制御器を直接設計する手法 |
| 制御対象 | カオス系、実データ系（例：DCモーター）など

---

## 📂 サブフォルダ構成
```
part08_data_driven/
├── theory/         # データ駆動型制御の解説資料
├── notebooks/      # Python実験ノート（Koopman, DMD等）
├── python/         # 実装スクリプト（行列推定、同定制御器等）
├── datasets/       # 制御対象の入出力データ（CSVなど）
├── figures/        # 時系列、スペクトル、同定結果などの図
└── README.md
```
---

## 🛠️ 推奨ツール / Tools

- Python: `numpy`, `scipy`, `matplotlib`, `pandas`, `pykoopman`, `pyDMD`
- データ形式：CSV, NumPy配列
- 可視化：固有値配置、モード構造、再構成誤差 など

---

## 🔗 関連資料

- Brunton & Kutz, “Data-Driven Science & Engineering”
- https://github.com/dynamicslab/pykoopman
- https://mathlab.github.io/PyDMD/
- EduController 第1部との比較視点：モデルベース vs データ駆動

---

## 📌 備考

データ駆動型制御は、AI制御と従来制御の**中間的な位置づけ**にあり、  
実用システムでのモデル構築や予測制御において有用性が高い分野です。  
本章ではデータ分析・行列演算・予測制御の統合を目指します。

---
