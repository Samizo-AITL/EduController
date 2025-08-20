---
layout: clean
title: testbench/
permalink: /SoC_DesignKit_by_ChatGPT/testbench/
---

# 🧪 testbench/
[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/SoC_DesignKit_by_ChatGPT/testbench)

このディレクトリは、**C→HDL 変換後のRTL**を検証するためのサンプルとテンプレートをまとめています。  
*This directory provides samples and templates to verify **RTL after C→HDL conversion**.*

## 使い方 / How to Use
1. `c_to_hdl/` で生成した Verilog を `rtl/` に配置  
   *Place generated Verilog into `rtl/`*
2. `tb/` のテストベンチを実行（Icarus/Verilator 等）  
   *Run testbenches in `tb/` (Icarus/Verilator, etc.)*
3. 参照結果と波形で **C と RTL の一致**を確認  
   *Check **C vs RTL** equivalence via logs/waves*

## 構成 / Layout
- `rtl/` … 生成したRTLを置く / *generated RTL here*  
- `tb/` … テストベンチ / *testbenches*  
- `scripts/` … 実行スクリプト / *run scripts*

## 関連 / Related
- [`c_to_hdl/`](/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/)  
- [`matlab_tools/`](/EduController/matlab_tools/)
