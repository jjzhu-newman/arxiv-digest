# 9/17 arXiv 兴趣摘要（工作日）

扫了今天新上线的 `cond-mat`、`quant-ph`、`math-ph`、`hep-th`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。新文量不小（cond-mat 新稿约 74、quant-ph 约 76），按你的兴趣锚点筛了 **12 篇**；Zotero 本轮因本机库路径权限读不到，未做去重对照。

**建议先翻这三篇：**
1. **Altermagnetic Magnons in Dipolar Nanomagnet Arrays**（偶极纳米磁体阵列里的交错磁振子）——直接打在 altermagnetism / 自旋电子学上。
2. **Liouvillian exceptional points in the emergence of quantum synchronization**——开放系统 + Liouvillian 例外点，和你关心的非厄米/耗散动力学很贴。
3. **Fixed Points, Floquet Entanglement Asymmetry, and Quantum Mpemba Effects**——Floquet × 纠缠不对称，几何图像清晰。

---

### 1. Altermagnetic Magnons in Dipolar Nanomagnet Arrays
Rhea Hoyer, Ephraim Spindler 等 · [2609.18398](https://arxiv.org/abs/2609.18398) · cond-mat.mes-hall · new

**为何相关：** 把 altermagnetism 从自旋守恒的电子能带图景，推到纯偶极耦合的纳米磁体阵列与 magnonics。

要点：在仅有偶极相互作用、自旋不守恒的 mesoscopic 阵列里，只要几何上装上交错磁对称，仍可得到动量依赖的自旋劈裂 magnon 带，本征态可保持强自旋极化，Bloch 区呈现典型 d-wave 自旋期望图案；自旋波传播因此高度方向依赖，是可调的合成交错磁功能平台。

---

### 2. Liouvillian exceptional points in the emergence of quantum synchronization
Carlos Ortega Taberner, Rosalind E. Cotton, Paul R. Eastham · [2609.18867](https://arxiv.org/abs/2609.18867) · quant-ph / mes-hall / optics · new

**为何相关：** 用量子 Liouvillian 的例外点 cascade 解释耦合激光/凝聚体的同步转变，落在开放系统与非厄米谱结构交叉点。

要点：经典/半经典里不同吸引子拓扑对应广义例外点；量子理论中，弱耦合独立振荡与强耦合同步对应慢模谱与本征矩阵的不同形态。沿谱流跟踪可见，同步转变由受广义 PT 对称保护的慢模例外点级联控制，说明量子 Liouvillian 奇异点如何组织不同动力学相区。

---

### 3. Fixed Points, Floquet Entanglement Asymmetry, and Quantum Mpemba Effects
Jayashish Das, Filiberto Ares, Arnab Kundu · [2609.17724](https://arxiv.org/abs/2609.17724) · hep-th / stat-mech / quant-ph · cross

**为何相关：** Floquet 驱动下的纠缠不对称与量子 Mpemba，用共形映射不动点把非平衡纠缠动力学几何化。

要点：对带全局 U(1) 的二维 CFT 做周期驱动，用迭代 Möbius 等共形映射描述动力学。局域算符插入制备的对称破缺激发，其纠缠不对称的增长/衰减/振荡/饱和，由算符插入点、子系统与映射不动点的相对位置决定；同一几何语言也覆盖局域对称恢复与正/反 Mpemba 效应。

---

### 4. Lindbladian quantum chaos beyond classical strange attractors
Ángel L. Corps, Armando Relaño · [2609.18464](https://arxiv.org/abs/2609.18464) · new

**为何相关：** 耗散多体自旋的 Liouvillian 混沌与随机矩阵统计，补开放系统“瞬态混沌”一侧。

要点：两耦合集体自旋的耗散系统在经典极限有稳定不动点吸引子，但弛豫前的瞬态已显混沌；量子侧对应 Liouvillian 相关谱段进入随机矩阵统计，且对弛豫有贡献的模数目显著增多——说明开放系统混沌不必依赖经典奇怪吸引子。

---

### 5. A first introduction to Matrix Product State algorithms for the integration of Lindblad equation
Christophe Chatelain · [2609.18841](https://arxiv.org/abs/2609.18841) · cross

**为何相关：** 一维开量子格点的 Lindblad 积分 MPS/TEBD 方法入门，方便对照开放系统数值工具箱。

要点：比较四种基于 MPS、可视为 TEBD 向开放系统推广的算法：两种直接积分矢量化 Lindblad（其一显式保密度矩阵正定），另两种走其他路径；面向入门读者梳理取舍与实现要点。

---

### 6. Lecture notes on Physics Informed Neural Networks, Neural Operators, and their applications
Alessandro Bombini · [2609.17638](https://arxiv.org/abs/2609.17638) · physics.comp-ph · new

**为何相关：** PINN / Neural Operator 课程讲义，覆盖 PIKAN、FNO、Mixture-of-Models 等近期变体。

要点：从零实现 PINN 与 Neural Operator（PyTorch 与 PhysicsNeMo），并讨论工程/物理/油藏等应用场景；适合当一版较新的方法总览而非单点结果。

---

### 7. Hybrid coupling with numerics-informed neural networks and the overlapping Schwarz alternating method
George Chumbipuma 等 · [2609.17841](https://arxiv.org/abs/2609.17841) · math-ph · new

**为何相关：** 物理/数值信息神经网络与经典全阶模型的混合耦合，Schwarz 交替部署，贴 PINN 落地与多尺度求解。

要点：在二维强对流（Pe∼10⁶）平流–扩散上，整体 NINN 可不依赖区域分解就训准；再用重叠乘性 Schwarz，把预训练子域 NINN（权重固定）与相邻 FOM 耦合。对比“自上而下”（全域 FOM–FOM Schwarz 取边界）与“自下而上”（子域合成边界、无需全域求解）两种训练边界数据策略。

---

### 8. Fourier Analysis of Parametrized Interactive Quantum Classifiers
Fábio Novaes 等 · [2609.17991](https://arxiv.org/abs/2609.17991) · quant-ph · new

**为何相关：** 受开放系统启发的交互式量子分类器，给出约化信道的闭式与 Fourier 特征图解释。

要点：IQC 用目标比特–环境哈密顿量交互做分类；本文推出单目标比特参数化 IQC 的约化量子信道闭式，明确哈密顿参数如何控制输出的常数/正弦/余弦分量，并据此推广到矩阵参数化环境哈密顿、可产生不可分 Fourier 结构的编码族。

---

### 9. Continuous variable distributed quantum sensing in integrated photonics
Bethany Puzio 等 · [2609.19092](https://arxiv.org/abs/2609.19092) · quant-ph · new

**为何相关：** 集成光量子网络上的连续变量分布式量子传感，直接落在量子传感兴趣点。

要点：片上生成四模纠缠探针，测量四个相位的线性组合；相对散粒噪声极限有约 0.199(16) dB 的纠缠增强（可分态约 0.041 dB）。纠缠制备、验证与四通道集成零差探测均在片上完成，强调相对体光学架构的可扩展性。

---

### 10. A Programmable Rydberg Quantum Bus for Nonlocal Connectivity
X. Jin 等 · [2609.18447](https://arxiv.org/abs/2609.18447) · quant-ph · new

**为何相关：** Rydberg 链作量子总线实现可编程非局域连接，并含 Floquet 工程的手性传输。

要点：色散区虚激发介导空间分离数据单元之间的可控相互作用（Green 函数连分数解析）；机制不限于单激发，可支持 Floquet 手性传输、力学振子远程纠缠，以及对不需要偶极交换的破坏性干涉抑制。在完整长程 Rydberg、位置涨落与有限寿命下模拟仍稳健。

---

### 11. Landscape geometry of Majorana zero modes in inhomogeneous superconductors
Guo-Jian Qiao, Zhi-Lei Zhang 等 · [2609.18138](https://arxiv.org/abs/2609.18138) · new

**为何相关：** 非均匀超导器件里 Majorana 零模是否存活的实空间“地貌”判据，贴拓扑物态与器件现实。

要点：平移对称破缺后 Bloch 拓扑不变量不够用；把空间坐标当演化参数，把零能方程改写成一阶动力学系统，用实空间景观几何回答给定非均匀构型下 MZM 是否存在/如何形变，面向实际器件而非理想晶体。

---

### 12. High-performance orbital-torque magnetic memory on the 300-mm platform
Dinggui Zeng, Yang Gao 等 · [2609.18008](https://arxiv.org/abs/2609.18008) · new

**为何相关：** 轨道力矩 / 自旋轨道力矩 MRAM 在 300 mm 平台上的器件推进，贴近自旋电子学应用侧。

要点：针对 SOT-MRAM 写/读效率与位元面积瓶颈，报告在 300 mm 工艺上的高性能轨道力矩磁存储结果，强调开关速度、耐久与集成可行性（细节见全文器件指标）。

---

今天没有特别扎眼的“非厄米趋肤效应 / Hatano–Nelson”新稿；开放系统侧更集中在 **Liouvillian 例外点、Lindblad 混沌与 MPS 求解**，物态侧 **交错磁振子** 最抢眼。若只要精读，优先 18398 → 18867 → 17724。
