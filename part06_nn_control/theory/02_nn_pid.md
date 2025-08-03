---
layout: default
title: 01. PID制御の基礎
---

<!-- MathJax support for both inline and block math -->
<script type="text/javascript">
  window.MathJax = {
    tex: { inlineMath: [['$', '$'], ['\\(', '\\)']] },
    svg: { fontCache: 'global' }
  };
</script>
<script type="text/javascript"
  async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

# 🧠 02. NN-PID制御：ニューラルネットによるPID補完制御

本章では、従来のPID制御にニューラルネット（NN）を組み合わせた  
**NN-PID制御**（Neural Network-aided PID Control）について学びます。

PIDの堅牢性とNNの柔軟性を組み合わせることで、非線形系や外乱変動に強い制御が可能になります。

---

## 🎯 学習目標 / Learning Objectives

- NN-PID制御の基本構造と学習方法を理解する  
- 学習可能な制御ゲイン・補正器の設計方法を知る  
- PyTorch等を用いたNN-PIDの訓練と評価を実装する  
- PID制御との違いや利点・課題を整理する

---

## 🔧 1. NN-PIDの構成

### ベース：標準PID制御

$$
u(t) = K_p e(t) + K_i \int e(t) dt + K_d \frac{de(t)}{dt}
$$

### NN-PID構成例①：NNによる誤差補正項

$$
u(t) = u_{\text{PID}}(t) + f_\theta(e(t), \dot{e}(t), \int e(t) dt)
$$

### NN-PID構成例②：NNがPIDゲインを動的生成

$$
K_p(t), K_i(t), K_d(t) = f_\theta(x(t))  
\quad \Rightarrow \quad u(t) = K_p(t)e(t) + ...
$$

> 📌 いずれの方式も、NNは**非線形性や時変性の補償**に強みを発揮します。

---

## 🧠 2. 学習方法

| 学習方式         | 説明                              | メリット / 注意点                    |
|------------------|-----------------------------------|-------------------------------------|
| 教師あり学習     | 最適入力データを教師にして回帰     | 安定・再現性高いが教師が必要         |
| 強化学習         | 報酬に基づき最適なNN制御則を学習   | 自律性高いが学習時間・安定性が課題   |
| エンドツーエンド | 時系列データから直接NNを学習       | 高精度だが訓練データ整備が必須       |

---

## 🧪 3. 実験構成と実装例

### 📦 実験構成例（倒立振子）

| 項目      | 内容                                      |
|-----------|-------------------------------------------|
| 入力      | $e(t)$, $\dot{e}(t)$, $\int e(t)dt$ 等      |
| 出力      | 制御入力 $u(t)$（モータトルクなど）       |
| NN構成    | MLP（多層パーセプトロン）またはLSTMなど   |
| 実装      | `nn_pid_control.py` + `train_nn_pid.ipynb`

---

## 📊 4. 古典PIDとの比較

| 項目       | PID制御                     | NN-PID制御                        |
|------------|-----------------------------|-----------------------------------|
| 設計法     | 手動 / ゲイン調整           | 学習ベース（関数近似）            |
| 適応性     | 時間不変が前提               | 状態依存で動的に変化可能          |
| 実装難易度 | 低                          | 高（学習・訓練が必要）            |
| 利点       | 安定・解釈性あり             | 非線形性・複雑系に強い            |

---

## 📘 今後の展開

- `nn_pid_control.py`：PyTorchによるNN-PID実装  
- `train_nn_pid.ipynb`：学習可視化と応答評価  
- `04_ai_vs_classical.md`：PIDとの統合戦略（AITL-Hへの布石）

---

## 📚 参考文献

- Tang et al. “Neural Network PID Control for Nonlinear Systems”, 2018  
- DeepX, ControlNet 等の事例  
- 本教材の [part06_nn_control/] 以下のコード・ノートブック群

---
