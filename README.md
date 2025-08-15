---
layout: default
title: EduController/README.md
---

---

# 🎛️ **EduController：制御理論とAI制御の教育フレームワーク**  
**EduController: Educational Framework for Control Theory and AI Control**

[![Samizo-AITLポータルサイトに戻る](https://img.shields.io/badge/Samizo--AITL%20ポータルサイトに戻る-brightgreen)](https://samizo-aitl.github.io/)  
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 🔗 **公式リンク | Official Links**

| **言語 / Language** | **GitHub Pages 🌐** | **GitHub 💻** |
|---------------------|--------------------|---------------|
| 🇯🇵 **Japanese** | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/EduController) |
| 🇺🇸 **English** | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/en/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/en) |

---

## 📘 **概要 | Overview**

**JP:**  
**EduController** は、**古典制御**から**現代制御**、さらに **AI ベースの次世代型制御**までを体系的に学べる、**段階的かつ実践的な教材プロジェクト**です。Python による制御理論の直感的理解から **HDL 記述**、**LLM 統合設計**まで幅広くサポートします。  

**EN:**  
**EduController** is a **step-by-step**, **practical educational project** covering **classical**, **modern**, and **AI-based next-generation control**. It supports learning from **control theory in Python** to **HDL coding** and **LLM-integrated design**.

---

## 🧭 **構成概要 | Structure Overview**

| **系統 / Track** | **内容（JP）** | **Overview (EN)** |
|------------------|---------------|-------------------|
| 🎛️ **制御理論系 (Part 01〜05)** | 古典制御、状態空間、デジタル制御、実装演習 | Classical control, state-space, digital control, practical implementation |
| 🤖 **AI制御系 (Part 06〜08)** | ニューラルネット、強化学習、データ駆動制御 | Neural networks, reinforcement learning, data-driven control |
| 🧠 **統合・応用制御系 (Part 09〜10)** | LLM統合制御、倒立振子総合制御 | LLM-integrated control, inverted pendulum control |

---

## 📚 **章構成一覧 | Chapter Structure**

### 🎛️ **制御理論系 / Classical & Modern Control**

| **Chapter** | **Title** | **Summary** |
|-------------|-----------|-------------|
| **Part 01** | **古典制御理論 / Classical Control Theory**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part01_classical/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part01_classical) | **PID制御**を中心に、**時間領域・周波数領域**の解析・設計を体系的に学習。<br>*Systematic study of PID control, time-domain and frequency-domain analysis & design.* |
| **Part 02** | **現代制御理論 / Modern Control Theory**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part02_modern/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part02_modern) | **状態空間表現**を基盤とし、**可制御性・可観測性**、**極配置**、**オブザーバ設計**を学ぶ。<br>*Covers state-space representation, controllability, observability, pole placement, observer design.* |
| **Part 03** | **適応制御・ロバスト制御 / Adaptive & Robust Control**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part03_adaptive/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part03_adaptive) | **MRAC**、**H∞制御**、**L1制御**など、パラメータ変動や外乱に強い制御を学ぶ。<br>*MRAC, H∞, L1 control for robustness against parameter variations and disturbances.* |
| **Part 04** | **デジタル制御と信号処理 / Digital Control & Signal Processing**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part04_digital/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part04_digital) | **Z変換**、**離散PID**、**デジタルフィルタ設計**など、デジタル実装向け制御技術を習得。<br>*Z-transform, discrete PID, digital filter design for implementation.* |
| **Part 05** | **実装・応用編 / Implementation & Applications**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part05_practical/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part05_practical) | **Python実装**、**ROS演習**、**FPGA制御**の実システム適用を学ぶ。<br>*Python, ROS practice, FPGA-based control.* [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) |

---

### 🤖 **AI制御系 / AI-based Control**

| **Chapter** | **Title** | **Summary** |
|-------------|-----------|-------------|
| **Part 06** | **ニューラルネットによる制御 / Neural Network Control**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part06_nn_control/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part06_nn_control) | **NN-PID設計**、**逆モデル制御**、ニューラルネットによる高度制御を学ぶ。<br>*NN-PID design, inverse model control using neural networks.* |
| **Part 07** | **強化学習による制御 / Reinforcement Learning Control**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part07_rl_control/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part07_rl_control) | **倒立振子や車両制御にRLを適用**、**DDPG**や**PPO**を実装。<br>*Applying RL to inverted pendulum & vehicle control; implementing DDPG, PPO.* |
| **Part 08** | **データ駆動型制御 / Data-Driven Control**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part08_data_driven/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part08_data_driven) | **Koopman演算子**、**システム同定**を用いたモデルフリー制御を実装。<br>*Model-free control using Koopman operator, system identification.* |

---

### 🧠 **統合・応用制御系 / Integrated Control**

| **Chapter** | **Title** | **Summary** |
|-------------|-----------|-------------|
| **Part 09** | **ハイブリッド制御とLLM統合 / Hybrid Control with LLM Integration**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part09_llm_hybrid) | **FSM×PID×LLM**による三層アーキテクチャで次世代制御設計を実装。<br>*Three-layer architecture (FSM×PID×LLM) for next-gen control.* [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) |
| **Part 10** | **倒立振子の総合制御 / Integrated Control of Inverted Pendulum**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part10_pendulum/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part10_pendulum) | **PID**、**LQR**、**RL**、**HDL実装**を統合した倒立振子制御。<br>*PID, LQR, RL, HDL implementation integrated for inverted pendulum control.* [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) |
