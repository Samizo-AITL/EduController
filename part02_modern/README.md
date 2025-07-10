# 🧠 Part 2: モダン制御理論（Modern Control Theory）

本章では、状態空間表現を基盤としたモダン制御理論を学びます。  
可制御性・可観測性を前提とし、極配置による状態フィードバック、オブザーバ（状態推定器）設計までを扱います。

---

## 🧭 章構成と教材一覧

| No | 章タイトル | 内容概要 |
|----|------------|----------|
| 01 | [状態空間表現の基礎](theory/01_state_space.md) | $Ax+Bu$, $Cx+Du$ の構造と意味、行列モデル化 |
| 02 | [可制御性と可観測性](theory/02_controllability.md) | Kalmanのランク条件、状態操作・推定の可否判定 |
| 03 | [状態フィードバックと極配置](theory/03_state_feedback.md) | 極配置法による閉ループ極の設計、可制御性の役割 |
| 04 | [オブザーバ設計と状態推定](theory/04_observer_design.md) | $L$ゲイン設計と $A-LC$ の安定化、推定誤差の収束 |

---

## 💻 実行スクリプト一覧

| スクリプト名 | 内容 |
|--------------|------|
| [`state_feedback.py`](simulation/state_feedback.py) | フィードバックゲイン $K$ の設計と応答可視化（予定） |
| [`observer_design.py`](simulation/observer_design.py) | オブザーバゲイン $L$ 設計と拡張系の応答確認 |

---

## 🧪 Jupyterノートブック（予定）

| ノートブック名 | 内容 |
|----------------|------|
| `state_feedback_demo.ipynb` | 状態フィードバックの対話可視化（未作成） |
| `observer_design_demo.ipynb` | オブザーバの推定精度と制御応答（未作成） |

---

## 🖼️ 教材図・シミュレーション出力（`figures/`）

| 図ファイル | 内容 |
|------------|------|
| `observer_response.png` | オブザーバ付き制御系のステップ応答グラフ |
| その他 | 状態空間モデル図、極配置概念図（今後追加予定） |

---

## ⚙️ 実行環境と依存ライブラリ

```bash
pip install control matplotlib numpy
```

	•	Python 3.8〜3.12 で動作確認済み
	•	control.place, control.ctrb, control.obsv など使用
	•	推奨：VSCode + Python, または Jupyter Lab

---

## 🧠 学習の流れとポイント
	1.	状態空間表現：行列でモデル化し、動的システムを数式化
	2.	可制御性/可観測性：設計可能か、推定可能かの判別
	3.	状態フィードバック：閉ループ極を望ましい位置に配置
	4.	オブザーバ設計：センサから得られない状態を推定し活用

---

## 📚 参考資料
	•	「現代制御理論入門」森北出版
	•	Ogata, Modern Control Engineering
	•	Pythonライブラリ：control, numpy, matplotlib

---

