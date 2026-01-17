---
layout: clean
title: Part10
permalink: /part10_pendulum/
---

---

# 🎯 Part 10：倒立振子の総合制御 / Hybrid Control of Inverted Pendulum

---

## 🔗 公式リンク | *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part10_pendulum/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part10_pendulum) 

---

## このパートを読む前に

本パートは、倒立振子を用いて  
**制御設計における「PIDの限界」と「構造化の効果と限界」**を示すことを目的とする。

倒立振子は有名な制御問題だが、本教材では  
「安定化できるかどうか」や  
「高度な制御理論を紹介すること」  
を主目的とはしていない。

あくまで次の問いに答えるための題材である。

> なぜ PID 制御は、  
> 条件によっては正しく機能し、  
> 条件が変わると簡単に破綻するのか？

> そして、  
> FSM のような構造を重ねることで  
> 何が整理され、何が依然として解決しないのか？

この問いに興味がない場合、  
本パートを読む必要はない。

---

## 内容構成

本パートは、以下の3章のみで完結している。

| ファイル | 内容 |
|---|---|
| [10-1_model.md](./10-1_model.md) | 倒立振子の非線形モデル、線形化、状態空間表現 |
| [10-2_pid_limit.md](./10-2_pid_limit.md) | PID制御が成立する条件と、成立しない理由 |
| [10-3_fsm_overlay.md](./10-3_fsm_overlay.md) | FSMを被せた場合の改善点と限界 |

---

## 読み方（重要）

**必ずこの順で読むこと。**

1. [10-1_model.md](./10-1_model.md)  
2. [10-2_pid_limit.md](./10-2_pid_limit.md)  
3. [10-3_fsm_overlay.md](./10-3_fsm_overlay.md)  

途中の章を飛ばすと、結論を誤解する。

---

## できること／できないこと

### できること
- 倒立振子の **数式モデル** を理解できる
- PID制御が **なぜ破綻するか** を説明できる
- FSMを入れると **何が整理され、何が解決しないか** が分かる

### できないこと
- 倒立振子を「誰でも安定化」できるようにはならない
- LQR・MPC・RLの実装方法は扱わない
- 実機制御を保証するものではない

---

## 位置づけ

本教材は **EduController** における次の問いに答えるためのものだ。

> なぜ「PIDだけ」では足りず、  
> それでも「PIDを捨てるべきではない」のか？

---

## 注意

- 数式は教育目的の簡略モデルである  
- 実装・実機適用は読者の責任で行うこと  

---

## 🔗 **関連リンク / Related Links**

- 📚 [EduController トップへ戻る / Back to EduController Home](https://samizo-aitl.github.io/EduController/)  
- 🤖 [AITL-H: FSM × PID × LLM アーキテクチャ](https://github.com/Samizo-AITL/AITL-H)  
- ✏️ [SamizoGPT: ChatGPT プロンプト集](https://github.com/Samizo-AITL/SamizoGPT)

---

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | **三溝 真一**（Shinichi Samizo） |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |
| **📜 ライセンス / License** | [![Hybrid License](https://img.shields.io/badge/License-Hybrid-blueviolet?style=for-the-badge)](https://samizo-aitl.github.io/EduController/#-ライセンス--license)<br>コード / Code: [MIT](https://opensource.org/licenses/MIT)<br>教材テキスト / Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>図表 / Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

**⬅️ [前章 / Previous Chapter](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/)**  
LLM統合・ハイブリッド制御（FSM×PID×LLMなど）を扱います。  
Covers LLM-integrated hybrid control such as FSM×PID×LLM.

**🏠 [トップページ / Back to Home](https://samizo-aitl.github.io/EduController/)**
