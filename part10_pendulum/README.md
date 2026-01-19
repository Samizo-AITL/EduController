---
layout: clean
title: Part10
permalink: /part10_pendulum/
---

---

# 🎯 Part 10：倒立振子の総合制御  
*Hybrid Control of the Inverted Pendulum*

---

## 🔗 公式リンク | *Official Links*

| 🌐 言語 / Language | GitHub Pages | GitHub Repository |
|------------------|-------------|-------------------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part10_pendulum/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part10_pendulum) |

---

## 📘 このパートを読む前に  
*Before You Start This Part*

本パートでは、**倒立振子**を題材として、  
制御設計における **PID制御の特性と限界**、  
および **FSM（有限状態機械）を重ねることで何が整理されるのか** を体系的に整理します。

*In this part, the inverted pendulum is used as a case study to examine the characteristics and limitations of PID control, and to clarify what can (and cannot) be structured by overlaying an FSM (Finite State Machine).*

倒立振子は制御工学において古典的かつ象徴的な対象ですが、  
本教材の目的は **安定化手法の網羅** や **高度な制御理論の紹介** ではありません。

*Although the inverted pendulum is a classical benchmark in control theory, this material does not aim to exhaustively cover stabilization methods or advanced control theories.*

本パートでは、以下の観点に焦点を当てます。

*Instead, the focus is placed on the following practical questions:*

- ⚙️ PID制御が **成立しやすい条件** と **破綻しやすい条件**  
  *Conditions under which PID control works well, and conditions under which it fails*
- 🧩 FSMを重ねたときに **整理できる点** と **依然として残る制約**  
  *What FSMs help clarify, and what limitations still remain*

以降の章では、これらを **倒立振子モデル** に基づいて段階的に確認していきます。

*The following chapters walk through these issues step by step using an inverted pendulum model.*

---

## 🗂 内容構成  
*Structure of This Part*

本パートは、**以下の4章のみ** で完結します。

*This part is intentionally concise and consists of only the following four chapters.*

| 📄 ファイル / File | 📖 内容 / Description |
|---|---|
| [10-1_model.md](./10-1_model.md) | 倒立振子の非線形モデル、線形化、状態空間表現<br>*Nonlinear model, linearization, and state-space representation* |
| [10-2_pid_limit.md](./10-2_pid_limit.md) | PID制御が成立する条件と、成立しない理由<br>*When PID works—and why it breaks down* |
| [10-3_fsm_overlay.md](./10-3_fsm_overlay.md) | FSMを被せた場合の改善点と限界<br>*Improvements and limits of FSM overlay* |
| [10-4_Example.md](./10-4_Example.md) | 設計上の実例（成立条件と破綻条件の整理）<br>*Design examples: success and failure conditions* |

---

## 📖 読み方（重要）  
*How to Read (Important)*

**⚠️ 必ず次の順で読んでください。**

*⚠️ Please read the chapters in the following order.*

1. [10-1_model.md](./10-1_model.md)  
2. [10-2_pid_limit.md](./10-2_pid_limit.md)  
3. [10-3_fsm_overlay.md](./10-3_fsm_overlay.md)  
4. [10-4_Example.md](./10-4_Example.md)  

途中の章を飛ばすと、**結論を誤解する可能性があります。**

*Skipping chapters may lead to misunderstanding the conclusions.*

---

## ✅ できること／❌ できないこと  
*What You Can and Cannot Do*

### ✅ できること  
*What You Will Be Able to Do*

- 📐 倒立振子の **数式モデル** を理解できる  
  *Understand the mathematical model of an inverted pendulum*
- 🔍 PID制御が **なぜ破綻するのか** を説明できる  
  *Explain why PID control fails in certain situations*
- 🧠 FSMを導入すると **何が整理され、何が解決しないか** を把握できる  
  *Distinguish what FSMs can clarify and what they cannot solve*

### ❌ できないこと  
*What This Part Does Not Cover*

- 🤖 倒立振子を「誰でも安定化」できるようにはならない  
  *It does not guarantee universal stabilization*
- 📊 LQR・MPC・RLの実装方法は扱わない  
  *Implementation of LQR, MPC, or RL is not covered*
- 🏭 実機制御を保証するものではない  
  *No guarantee for real-world hardware control*

---

## 🧭 位置づけ  
*Position in EduController*

本教材は **EduController** における、次の問いに答えるためのものです。

*This part addresses the following core question within EduController:*

> なぜ「PIDだけ」では足りず、  
> それでも「PIDを捨てるべきではない」のか？  

> *Why is “PID alone” insufficient,  
> yet PID should not be discarded?*

---

## ⚠️ 注意事項  
*Notes*

- ✏️ 数式は **教育目的の簡略モデル** です  
  *Equations are simplified for educational purposes*
- 🔧 実装・実機適用は **読者の責任** で行ってください  
  *Implementation and hardware application are the reader’s responsibility*

---

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | **三溝 真一**（Shinichi Samizo） |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-black?logo=github)](https://github.com/Samizo-AITL) |
| **📜 ライセンス / License** |[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/EduController/#-ライセンス--license)<br>コード / Code: [MIT](https://opensource.org/licenses/MIT)<br>教材テキスト / Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>図表 / Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

⬅️ **[前章 / Previous Chapter](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/)**  
*LLM統合・ハイブリッド制御（FSM×PID×LLMなど）を扱います。*  
*Covers LLM-integrated hybrid control such as FSM×PID×LLM.*

🏠 **[トップページ / Back to Home](https://samizo-aitl.github.io/EduController/)**

---
