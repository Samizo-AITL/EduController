---
layout: clean
title: Appendix (Expert)
permalink: /part09_llm_hybrid/appendix_expert/
---

# 📎 Appendix: 専門家向け補足 / Expert Addendum

## 1) 制御理論上の前提 / Control-Theoretic Assumptions
- **PIDは最内周**：安定性・応答を担保する唯一の実時間ループ。  
  *PID is the innermost, real-time loop guaranteeing stability and response.*  
- **LLMは再設計層**：運転中の安定性を直接保証しない。提案は **オフライン/監督下** で適用。  
  *LLM is a redesign advisory layer; proposals are applied offline/under supervision, not in the hard RT loop.*  
- 設計検証：Bode/Nyquist/Root-Locus、ゲイン余裕/位相余裕の確認。  
  *Verification via Bode/Nyquist/Root-Locus; verify gain/phase margins.*  

## 2) タイミング制約 / Timing Constraints
| 層 | 周期 / Cycle | 目的 / Purpose |
|---|---|---|
| PID | 0.5–5 ms（対象依存） | 実時間安定化 *Real-time stabilization* |
| FSM | 10–100 ms | モード切替 *Mode switching* |
| LLM | ≥ 100 ms–秒オーダ | 例外対応・再設計 *Exception handling / redesign* |

> LLMは**ハードリアルタイム非対応**。PID/FSMのタイミングを乱さない非同期呼び出しが原則。  
> *LLM is not hard real-time; invoke asynchronously so it never blocks PID/FSM deadlines.*

## 3) レイヤ契約(API) / Layer Contracts (API)
### PID API（例）
```python
u = pid.step(ref: float, y: float) -> float
pid.tune(Kp, Ki, Kd)
pid.reset()
```
### FSM API（例）
```python
s_next = fsm.transition(s_curr, event) -> state
fsm.inject_exception(exc_class)  # maps to recovery state
```
### LLM 提案インタフェース / LLM Proposal Interface
```json
{
  "type": "tuning" | "rule_patch" | "goal_update",
  "payload": {...},
  "risk": "low|medium|high",
  "justification": "text"
}
```
> **適用ガード / Guards**：`risk != high` かつ ヒト承認、ロールバック可・トレーサブル。  
> *Apply only if risk ≠ high and human-approved; must be reversible and traceable.*

## 4) フォールト分類とLLM関与 / Fault Taxonomy & LLM Involvement
- **S1（即時停止）**：オーバーカレント、異常温度 → LLM不介入、FSMが安全停止。  
  *Immediate stop; no LLM involvement, FSM triggers safe-stop.*  
- **S2（縮退運転）**：センサ片系断 → LLMが暫定推定/回避策を提案（人間承認後）。  
  *Degraded mode; LLM proposes mitigation after human approval.*  
- **S3（改善提案）**：性能劣化、エネルギー最適化 → LLMがチューニング/ルール改訂案を提示。  
  *Optimization; LLM proposes tuning or rule patches.*  

## 5) 検証チェックリスト / Verification Checklist
- [ ] プラント近似の検証（同定/モデル誤差上限）  
- [ ] PIDマージン（PM, GM）と飽和・アンチワインドアップ設計  
- [ ] FSM遷移の完全性（デッドロック/ライブロックなし）  
- [ ] 例外状態の安全帰着（safe state）  
- [ ] LLM提案のA/B検証（シミュレーション→HIL→実機）  
- [ ] 監査ログ（誰が・いつ・何を適用したか）  

## 6) 用語集 / Glossary
- **Safe-stop**：安全停止。*Controlled shutdown to a safe state.*  
- **Degraded mode**：縮退運転。*Operation with limited functionality.*  
- **Rule patch**：FSM遷移ルールの差分更新。*Delta update to FSM rules.*
