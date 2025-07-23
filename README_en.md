# 🎛️ EduController: Educational Framework for Control Theory and AI-based Control

**EduController** is a progressive and practical learning project that systematically covers classical control theory, modern control, and next-generation AI-based control.  
It uses **Python-based simulation and visualization** to support intuitive understanding and real-world control system design, including LLM-integrated architectures.

---

- 🇯🇵 [日本語版 READMEはこちら](./README.md)

---

## 🧭 Curriculum Structure: Two Main Tracks

The EduController curriculum consists of 9 parts, divided into the following two tracks:

- 🎓 **Control Theory Track (Part 01–05)**  
  Covers classical to modern control theory, digital implementation, and hands-on practice.

- 🤖 **AI-based Control Track (Part 06–09)**  
  Covers neural networks, reinforcement learning, data-driven control, and LLM-integrated hybrid control.

> Each chapter is independently accessible, but AI-based control assumes basic knowledge of control theory.

---

## 📚 Chapter List (with links)

### 🎓 Control Theory Track

| Part | Directory | Overview |
|------|-----------|----------|
| Part 01 | [part01_classical](./part01_classical/) | Classical Control (PID, frequency response, stability) |
| Part 02 | [part02_modern](./part02_modern/) | Modern Control (State-space, LQR, Kalman filter) |
| Part 03 | [part03_adaptive](./part03_adaptive/) | Adaptive and Robust Control (MRAC, H∞, L1) |
| Part 04 | [part04_digital](./part04_digital/) | Digital Control and DSP (Z-transform, FFT, implementation) |
| Part 05 | [part05_practical](./part05_practical/) | Hands-on Practice (Python, ROS, FPGA examples) |

---

### 🤖 AI-based Control Track

| Part | Directory | Overview |
|------|-----------|----------|
| Part 06 | [part06_nn_control](./part06_nn_control/) | Neural Network Control (NN-PID, inverse modeling) |
| Part 07 | [part07_rl_control](./part07_rl_control/) | Reinforcement Learning Control (Q-learning, DDPG, PPO) |
| Part 08 | [part08_data_driven](./part08_data_driven/) | Data-Driven Control (Koopman, matrix identification) |
| Part 09 | [part09_llm_hybrid](./part09_llm_hybrid/) | LLM-Integrated Hybrid Control (FSM × PID × LLM) |

---

## 🔧 Recommended Tools

- Python: `control`, `scipy`, `matplotlib`, `torch`, `gymnasium`, `stable-baselines3`
- Jupyter Notebook (interactive simulations and visualizations)
- ROS (real-time implementation examples)
- MATLAB / Simulink (optional): for graphical modeling and C code generation using Simulink Coder
- ChatGPT / GPT-4o (LLM integration support)

> 💡 Additional Simulink models and HDL-ready templates are provided in `/matlab_tools/` and `/SoC_DesignKit_by_ChatGPT/`.

---

## 🔩 Implementation Toolkits

In addition to theoretical learning, EduController offers two practical toolkits for design and implementation:

### 🔹 [matlab_tools/](./matlab_tools/)  
Includes Simulink models for:
- Visualizing PID and state-space control systems
- Generating C code via Simulink Coder
- Preparing for HDL-level design by exporting to `c_to_hdl/`

### 🔹 [SoC_DesignKit_by_ChatGPT/](./SoC_DesignKit_by_ChatGPT/)  
Template-based toolkit that supports:
- FSM, PID, and hybrid LLM-based controller generation
- Verilog code generation from C expressions (with ChatGPT support)
- Testbench development and waveform analysis

> These toolkits bridge the gap between **education and implementation**, and support hands-on design flows from Python/Simulink to HDL.

---

## 🚀 Features

- 🔁 Learn classical to AI-based control in a progressive and structured way  
- 🧠 Integrate LLMs like ChatGPT into the control design process  
- 💡 Bridge theory and implementation with intuitive, hands-on exercises  
- 📚 Suitable for courses, workshops, or self-study (MIT Licensed)

---

## 🔗 Related Projects

EduController is integrated with the following related educational and control projects:

### 🧩 [Edusemi v4.x](https://github.com/Samizo-AITL/Edusemi-v4x)  
An educational project for semiconductor design. Covers process, circuit, and layout design along with Python-based automation and SoC implementation.  
**Its special topics section aligns with LLM-integrated hybrid control and AITL-H concepts.**

### 🤖 [AITL-H: Hybrid Intelligent Control](https://github.com/Samizo-AITL/AITL-H)  
A hierarchical intelligent control framework for humanoid systems.  
**Combines FSM (instinct) + PID (reason) + LLM (intelligence)** and is directly connected to **Part 09 of EduController**.

---

## 🧑‍🔬 Author Information

- **Name**: Shinichi Samizo  
- **Education**: M.E. in Electrical and Electronic Engineering, Shinshu University Graduate School  

- **Career**:  
  Joined Seiko Epson Corporation in 1997. Engaged in:  
  - Semiconductor device development (0.35μm to 0.18μm nodes)  
  - Logic/memory integration, high-voltage mixed-signal design  
  - Thin-film piezo actuator development  
  - Commercialization of PrecisionCore printhead technology  

- **Contact**:  
  GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
  Email: [shin3t72@gmail.com](mailto:shin3t72@gmail.com)

---

## 🔖 License

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
This project is open for educational, research, and personal use.

---

💬 [Join the discussion on EduController → GitHub Discussions](https://github.com/Samizo-AITL/EduController/discussions)
