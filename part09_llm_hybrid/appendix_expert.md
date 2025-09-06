---
layout: clean
title: Appendix_Expert
permalink: /part09_llm_hybrid/appendix_expert.html
---

---

# 📑 Appendix: 専門家向け補足資料 / Expert Supplement

---

本補足資料では、Part09の内容をさらに専門家向けに深掘りします。  
*This appendix provides a deeper dive into the concepts in Part09, targeting experts.*

---

## 🔬 **制御工学 × LLM の接点 / Intersection of Control Engineering and LLMs**

- PID は **安定性と性能保証** を担う最内層制御  
  *PID handles stability and performance assurance as the innermost control.*  
- FSM は **モード遷移の形式化** を担う離散制御  
  *FSM provides formalized mode transitions as discrete control.*  
- LLM は **知識注入・例外処理・再設計** を担う外層知性  
  *LLM contributes knowledge injection, exception handling, and redesign as the outer intelligence layer.*  

---

## 📐 **数理比較 / Mathematical Comparison**

### PID 制御
$$
u(t) = K_p e(t) + K_i \int_0^t e(\tau) d\tau + K_d \frac{de(t)}{dt}
$$

- 比例項: 応答速度  
- 積分項: 定常偏差除去  
- 微分項: 外乱抑制  

### Attention 機構
$$
\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

- 過去系列の動的加重  
- PIDゲイン調整の類似機構として解釈可能  

---

## ⚙️ **設計原則 / Design Principles**

1. **PID** = 不変の安定ループ  
   *Fixed stability loop.*  
2. **FSM** = 状態管理とモード切替  
   *State management and mode switching.*  
3. **LLM** = 故障時・例外時の再設計  
   *Redesign triggered in faults/exceptions.*  

---

## 📚 **推奨文献 / Recommended References**

- Åström, K. J., & Murray, R. M. (2010). *Feedback Systems*. Princeton University Press.  
- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction*. MIT Press.  
- Vaswani, A. et al. (2017). *Attention is All You Need*. NeurIPS.  

---

**⬅️ [Part 9 トップに戻る](index.md)**  
**🏠 [トップページ](../index.md)**
