# 🔄 Part 3: 適応制御・ロバスト制御（Adaptive and Robust Control）

本章では、制御対象の変動や不確かさに対応するための制御理論を扱います。  
モデル不整合・パラメータ変動に強い制御系を設計するための基礎を学びます。

---

## 🎯 学習目標 / Learning Objectives

- 制御対象が変化する場合の課題と適応戦略を理解する
- MRAC（モデル参照型適応制御）の構造と設計法を学ぶ
- L1適応制御の基本思想を理解する
- ゲインスケジューリングによる準適応戦略を学ぶ
- H∞制御・μ解析によるロバスト性評価の概念を把握する
- 代表的な適応制御系をPython/MATLABで実装する

---

## 🧩 主なトピック / Key Topics

| トピック | 内容 |
|----------|------|
| 適応制御の分類 | 直接法 vs 間接法、オンライン推定の有無 |
| MRAC | モデル参照によるパラメータ調整系（MITルールなど） |
| L1適応制御 | 高速推定と安定性の両立（低帯域出力） |
| ゲインスケジューリング | 外部パラメータに応じた制御ゲイン切替 |
| ロバスト制御概念 | モデル誤差に対するH∞制御の耐性設計 |
| Python/MATLAB演習 | オンライン学習、リアルタイム適応シミュレーションなど

---

## 📂 サブフォルダ構成
```
part3_adaptive/
├── theory/         # 適応・ロバスト制御の基礎理論
├── examples/       # 時変系、不確かさを含む制御対象例
├── python/         # Pythonコード（MRAC, L1, gain scheduling）
├── matlab/         # MATLAB版適応制御実装
├── figures/        # 構成図・応答グラフなど
└── README.md
```
---

## 🛠️ 推奨ツール / Tools

- Python: `numpy`, `control`, `sympy`, `matplotlib`
- MATLAB: `Robust Control Toolbox`, `Simulink`
- Jupyter / Simulink を使った適応挙動の可視化推奨

---

## 🔗 関連資料

- Ioannou & Sun, “Robust Adaptive Control”
- Narendra & Annaswamy, “Stable Adaptive Systems”
- H∞制御とμ解析入門（Zhou & Doyle）
- L1 Control Primer: https://arc.aiaa.org/doi/10.2514/1.G003472

---

## 📌 備考

適応制御は、状態推定と制御設計を**リアルタイムで行う**点が重要です。  
本章では「学習しながら制御する」系の入門を目指します。

---
