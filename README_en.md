# 🎛️ **EduController**: Educational Framework for Control Theory and AI-based Control

**EduController** is a **progressive** and **practical learning project** that systematically covers **classical control theory**, **modern control**, and **next-generation AI-based control**.  
It uses **Python-based simulation and visualization** to support **intuitive understanding** and **real-world control system design**, including **LLM-integrated architectures**.

---

🇯🇵 [日本語版 READMEはこちら](./README.md)

---

## 🧭 **Overview: Three Tracks – Classical, AI-based, and Hybrid Control**

EduController consists of 10 chapters, organized into the following three tracks:

- 🎓 **Classical & Modern Control (Part 01–05)**  
  Systematic study of classical control, state-space modeling, digital control, and practical implementation

- 🤖 **AI-based Control (Part 06–08)**  
  Step-by-step learning of neural networks, reinforcement learning, and data-driven control methods

- 🧠 **Hybrid & Applied Control (Part 09–10)**  
  Comprehensive integration using LLMs and real-world applications like inverted pendulum control

> ※ Each chapter can be studied independently. However, AI-based and hybrid control parts assume prior knowledge of classical control theory.

---

## 📚 **Chapter Structure (with Links)**

### 🎓 **Classical & Modern Control**

| Part | Directory | Overview |
|------|-----------|----------|
| **Part 01** | [part01_classical](./part01_classical/) | **PID control, Bode plot, stability analysis** |
| **Part 02** | [part02_modern](./part02_modern/) | **State-space modeling, LQR, Kalman filter** |
| **Part 03** | [part03_adaptive](./part03_adaptive/) | **Adaptive & robust control (MRAC, H∞, L1)** |
| **Part 04** | [part04_digital](./part04_digital/) | **Digital control, Z-transform, DSP implementation** |
| **Part 05** | [part05_practical](./part05_practical/) | **Python coding, ROS practice, FPGA-based control** |

### 🤖 **AI-based Control**

| Part | Directory | Overview |
|------|-----------|----------|
| **Part 06** | [part06_nn_control](./part06_nn_control/) | **Neural network control (NN-PID, inverse models)** |
| **Part 07** | [part07_rl_control](./part07_rl_control/) | **Reinforcement learning (Q-learning, DDPG, PPO)** |
| **Part 08** | [part08_data_driven](./part08_data_driven/) | **Data-driven control (Koopman, system identification)** |

### 🧠 **Hybrid & Applied Control**

| Part | Directory | Overview |
|------|-----------|----------|
| **Part 09** | [part09_llm_hybrid](./part09_llm_hybrid/) | **LLM-integrated hybrid control (FSM × PID × LLM)** |
| **Part 10** | [part10_pendulum](./part10_pendulum/) | **Comprehensive inverted pendulum control (PID / LQR / DDPG / HDL)** |

---

## 🔧 Recommended Tools

- **Python**: `control`, `scipy`, `matplotlib`, `torch`, `gymnasium`, `stable-baselines3`
- **Jupyter Notebook**: for **interactive simulations** and **visualizations**
- **ROS**: for **real-time control implementation**
- **MATLAB / Simulink**: for **graphical modeling** and **C code generation**
- **ChatGPT / GPT-4o**: for **LLM integration** and **design support**

> 💡 Additional **Simulink models** and **HDL-ready templates** are provided in `/matlab_tools/` and `/SoC_DesignKit_by_ChatGPT/`

---

## 🔩 Implementation Toolkits

In addition to theory, **EduController** provides practical support via two toolkits:

### 🔹 **[matlab_tools/](./matlab_tools/)**  
Includes **Simulink models** for:
- **Visualizing PID and state-space control**
- **C code generation** via **Simulink Coder**
- Exporting to `c_to_hdl/` for **HDL design**

### 🔹 **[SoC_DesignKit_by_ChatGPT/](./SoC_DesignKit_by_ChatGPT/)**  
A **template-based toolkit** supporting:
- FSM / PID / LLM-based controller generation
- **Verilog conversion** using **ChatGPT prompts**
- **Testbench setup** and **waveform analysis**

> These toolkits connect **education ↔ design ↔ implementation** for **end-to-end learning**

---

## 📂 Directory Structure

```plaintext
EduController/
├── part01_classical/               # Classical control (gain, Bode, phase margin)
├── part02_modern/                  # Modern control (state-space, controllability)
├── part03_adaptive/                # Adaptive control (MRAC, H∞, L1)
├── part04_digital/                 # Digital control (Z-transform, FFT)
├── part05_practical/               # Practical control with Python, ROS, FPGA
├── part06_nn_control/              # Neural network controllers (NN-PID)
├── part07_rl_control/              # Reinforcement learning (DDPG, PPO)
├── part08_data_driven/             # Data-driven control (Koopman, system ID)
├── part09_llm_hybrid/              # LLM-integrated hybrid control
├── part10_pendulum/                # Hybrid control of inverted pendulum (PID, LQR, RL, HDL)
│
├── SoC_DesignKit_by_ChatGPT/       # HDL design templates for FSM/PID/LLM
│   ├── fsm/                        # FSM YAML + Mermaid templates
│   ├── pid/                        # Verilog PID examples
│   ├── llm/                        # FSM × LLM control templates
│   ├── c_to_hdl/                   # C to Verilog prompt templates
│   ├── testbench/                  # Simulation and waveform analysis
│   ├── execution_logs/             # ChatGPT conversation logs
│   ├── prompts/control_templates/  # Design prompts for ChatGPT
│   └── template_mapping_matrix.md  # Template-to-module mapping table
│
├── matlab_tools/                   # Simulink design and C export
│   ├── pid_simulink_example.slx
│   ├── state_space_example.slx
│   ├── model_to_code.md
│   └── getting_started.md
│
├── README.md                       # Japanese main README
└── README_en.md                    # English main README
```

> 📘 See each subfolder's `README.md` for detailed content

---

## 🚀 Features

- 🔁 Learn **control theory** from basics to **AI-integrated design**
- 🧠 **ChatGPT-based design support** with reusable prompt templates
- 💻 Bridge **Simulink**, **Python**, and **HDL design**
- 🎓 Ideal for **education**, **self-study**, and **PoC prototyping**

---

## 🔗 Related Projects

- 🧩 **[Edusemi v4.x](https://github.com/Samizo-AITL/Edusemi-v4x)**  
  Semiconductor fundamentals + SoC design curriculum  
  Includes special topics aligned with **Part 09 (LLM Hybrid)**

- 🤖 **[AITL-H](https://github.com/Samizo-AITL/AITL-H)**  
  Three-layer intelligent control: **FSM × PID × LLM**  
  Applies hybrid logic to **robotics**, **adaptive control**, and **SoC implementation**

---

## 👤 **Author Information**

**Shinichi Samizo**  
- **M.S. in Electrical and Electronic Engineering, Shinshu University**  
- Former **Seiko Epson** Corporation Engineer (since 1997)

📌 **Areas of Expertise**:  
- **Semiconductor Devices (Logic, Memory, High-Voltage Integrated with Logic)**  
- **Inkjet Thin-Film Piezoelectric Actuators**  
- **PrecisionCore Printhead Development, BOM Management, ISO Education**

📬 **Contact**  
- ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)  
- 🐦 [https://x.com/shin3t72](https://x.com/shin3t72)  
- 💻 [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/)

---

## 🔖 License

MIT License © 2025 **Shinichi Samizo**  
Freely usable for **education**, **research**, and **technical training**

---

💬 [Join the discussion → GitHub Discussions](https://github.com/Samizo-AITL/EduController/discussions)

---
