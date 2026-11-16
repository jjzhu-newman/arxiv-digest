# 10/1 arXiv 兴趣摘要（工作日）

扫了今天（美西 10/1，周四）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。新稿量：cond-mat 约 91、quant-ph 约 226（另有交叉与替换未计入主计数）。按兴趣锚点筛了 **11 篇**，全部为今日新投稿（未收替换稿；交叉里若干 NN 波函数未挤进终选）。用户机器 DESKTOP-00O6NSD 在线，已对本地 Zotero 只读核对：**11 篇均未见于库中**。

**建议先翻这三篇：**
1. **Designing Strongly Correlated Quantum Phases of Matter with Foundation Neural-Network Quantum States** —— Foundation NNQS 对阻挫 Heisenberg 做可微反设计，自发落到 J₁-J₂-δ 并给出新 QSL 候选——NNQS × 反设计。
2. **Entropy-Driven Altermagnetism from Thermal Magnons** —— 加热熵驱动的交错磁：磁振子劈裂增熵、降自由能并给出有限温相——altermagnetism 热力学通道。
3. **Interferometric Readout of Momentum-Space Topology in a Programmable Dissipative Photonic Circuit** —— 可编程耗散光子线路干涉读出非厄米 SSH 的 Zak 相与例外点绕数——非厄米拓扑实验读出。

---

### 1. Designing Strongly Correlated Quantum Phases of Matter with Foundation Neural-Network Quantum States
Alessandro Sinibaldi · Luciano Loris Viteritti · Riccardo Rende · Federico Becca · Giuseppe Carleo · [2609.40209](https://arxiv.org/abs/2609.40209) · cond-mat.str-el · new

**为何相关：** 用 Foundation 神经网络量子态对强关联哈密顿量做可微反设计，并落在与交错磁相关的 J₁-J₂-δ 模型上找到新量子自旋液体候选——NNQS × 反设计核心。

要点：将一族哈密顿量的基态编码进单一变分波函数，使任意目标性质对耦合可微，从而在耦合空间做梯度搜索。在方格子阻挫 Heisenberg 上，单耦合复现 J₁-J₂ 非磁窗口；放开对角耦合后出现连接方格与各向异性三角格的扩展非磁区。八耦合搜索自发收敛到对角耦合在邻接 plaquettes 上交替的 J₁-J₂-δ 模型（近期与 altermagnetism 相关）；有限尺寸标度至 16×16 显示无磁/二聚/plaquette 序，提出新的方格 QSL 候选。

---

### 2. Entropy-Driven Altermagnetism from Thermal Magnons
Tanaya Halder · Ashis K. Nandy · Anamitra Mukherjee · [2609.40002](https://arxiv.org/abs/2609.40002) · cond-mat.str-el · new

**为何相关：** 提出加热熵驱动的交错磁不稳定性：动量依赖磁振子劈裂增熵、降自由能——altermagnetism 的热力学新通道。

要点：在极小方格反铁磁中，交换调制因产生动量依赖磁振子劈裂而提高磁振子熵，从而稳定交错磁相。给出该交换调制态的不稳定性判据与温控重入行为，并与 Néel 序重叠定义有限温交错磁相。变分自旋波、自旋–格子 Monte Carlo 与团簇对角化支持熵驱动机制；所得态具有横向自旋电导，提示与足够软的物理模式耦合时可由热诱导实现交错磁。

---

### 3. Interferometric Readout of Momentum-Space Topology in a Programmable Dissipative Photonic Circuit
Andrea Cataldo · Emil J. Bergholtz · Daniel Leykam · Jun Gao · Ali W. Elshaari · [2609.38352](https://arxiv.org/abs/2609.38352) · quant-ph · new

**为何相关：** 可编程耗散光子线路中用干涉读出动量空间拓扑，区分非厄米 SSH 的 Zak 相与例外点诱导的相干绕数——非厄米拓扑 × 实验平台。

要点：非厄米动力学的拓扑编码在体演化相位中，但强耗散压制携带相位的振幅。作者用可编程光子集成电路经幺正膨胀在合成动量空间实现该动力学，并以相移干涉恢复相位。对非厄米 SSH，方法区分平凡/非平凡 Zak 相，并给出例外点诱导的相干绕数 q=±1；经 Rice–Mele 泵扩展到合成环面，得到平凡/非平凡循环的第一陈数 Ch₁=0,1，展示强耗散下可编程读出动量空间拓扑的路径。

---

### 4. Spin Birefringence and Spin Polarized Transmission across p-wave Altermagnetic Heterostructure
Yong-Mei Zhang · Zhi-Ping Niu · [2609.39174](https://arxiv.org/abs/2609.39174) · cond-mat.mes-hall · new

**为何相关：** 正常金属/ p 波交错磁异质结中的自旋双折射与自旋极化透射——altermagnetism 的输运指纹。

要点：对 N/AM 界面与 N/AM/N 结构造波函数匹配，得到反射/透射系数与自旋极化。电子从正常金属入射到交错磁时分裂为 ± 支并以不同折射角传播，+ 支可出现全内反射，临界角由入射条件与 AM 材料参数决定。异质结中自旋上下电子传播方向相同但透射概率不同，透射与极化随结区长度周期性变化，给出可观测的自旋双折射与极化输运特征。

---

### 5. Phonon-mediated closing of topological Floquet gaps in graphene: Non-phenomenological analysis
Royi Ledermann · Rave Hanoch Saadon · Adam Herling · Ofer Neufeld · [2609.39817](https://arxiv.org/abs/2609.39817) · cond-mat.mtrl-sci · new

**为何相关：** 非唯象电子–声子耦合下圆偏振激光驱动石墨烯的 Floquet 拓扑能隙被光学声子显著压闭——Floquet × 拓扑为何难观测。

要点：石墨烯 Floquet 拓扑带仍缺直接观测。计入非唯象 e–ph 后，大零点运动使 Floquet 带显著展宽；更大位移的 Γ 点光学声子即使无仪器展宽也可使 Floquet 能隙约减半，并可诱导额外平带等结构。结果提示声子介导的能隙压闭是石墨烯 Floquet 拓扑难以建立的重要微观原因，超越纯唯象退相干描述。

---

### 6. Dynamic distributed quantum sensing of radio-frequency fields via time-bin entanglement
Vedansh Nehra · Richard Birrittella · Benjamin Malia · Nicholas J. Barton 等 · [2609.39831](https://arxiv.org/abs/2609.39831) · quant-ph · new

**为何相关：** 用时间二进制纠缠比特做分布式量子传感，把动态射频相位相干映射为静态光学相位——量子传感/雷达直接相关。

要点：以时间二进制 Bell 态替代传统偏振探针，利用本征双时间差分采样结构感知射频场。相对静态偏振编码协议，本方案可相干映射动态 RF 相位；将时间二进制间隔匹配 RF/IF 半周期（对跖采样）时，理论给出相对单次静态偏振编码约 6 dB 灵敏度增益，并保留每对纠缠相对 SQL 的 3 dB 优势，面向动态射频场的分布式传感。

---

### 7. Exponential separation in sensing continuous signals via squeezing
Francesco Anna Mele · Nadine Meister · Haimeng Zhao · Senrui Chen · Hsin-Yuan Huang · [2609.38678](https://arxiv.org/abs/2609.38678) · quant-ph · new

**为何相关：** 对连续演化信号证明压缩度可带来指数级传感时间分离——量子计量资源理论的新结果。

要点：传统量子传感多针对固定信号；引力波与电磁场等应用中信号连续变化，且可自适应选择制备/控制/测量时刻。作者对特征尺度为 T 的连续信号证明：压缩至少 ω(√log T) 时传感时间为 poly(T)，而压缩至多 o(√log T) 时必须指数级传感时间，确立压缩在连续信号传感中的指数分离。

---

### 8. Dissipation accelerates quantum and classical simulation of open-system dynamics
Armando Angrisani · Ricard Puig · Yanting Teng · Zoë Holmes · [2609.40174](https://arxiv.org/abs/2609.40174) · quant-ph · new

**为何相关：** 一类 Pauli 噪声（含退极化）可指数压制 Heisenberg 演化可观测量的高权重分量，从而加速开放系统的量子与经典模拟——开放系统 × 可模拟性。

要点：直觉上耗散通道增加硬件开销，但作者证明广泛的 Pauli 噪声可指数压制高权重算符分量。对有界度 Lindblad 动力学，这允许在量子硬件上更高效的可观测量模拟，并在经典端改善张量网络/截断方案。结果把“噪声有害”翻转为：特定耗散可成为开放系统模拟的计算资源。

---

### 9. Quantum quenches of scar states in the Affleck-Kennedy-Lieb-Tasaki model via Clifford augmented tensor network simulation
Azar C. Nakhl · Ben Harper · Muhammad Usman · Thomas Quella · [2609.38848](https://arxiv.org/abs/2609.38848) · cond-mat.str-el · new

**为何相关：** 用 qudit Clifford 增强张量网络模拟 AKLT 模型瘢痕态淬灭并量化 magic——纠缠/非稳定子性 × 多体瘢痕。

要点：Clifford 增强方法利用稳定子结构高效模拟量子线路与多体系统，并便于量化非稳定子性（magic）。作者以 qudit Clifford 增强模拟探测 AKLT 基态与瘢痕态的 magic，发现二者高度 magical；进而研究瘢痕态量子淬灭动力学中 magic 的演化，展示该框架在拓扑/瘢痕多体中的可用性。

---

### 10. Engineered Dissipation for Thermal-State Tracking Across Quantum Criticality
Saikat Mistry · Dibyajyoti Sahu · Suhas Gangadharaiah · [2609.39084](https://arxiv.org/abs/2609.39084) · quant-ph · new

**为何相关：** 用主方程框架设计耗散，使系统在穿越量子临界点时跟踪指定热态轨迹——开放系统 × 临界控制。

要点：有限时间驱动跨越量子临界点会产生非绝热激发与相干；既有耗散工程多刻画固定环境如何改写临界动力学，而非主动导向指定热轨迹。本文发展主方程层面的耗散设计，使系统在临界穿越中跟踪预定热态，补充相干控制，为开放多体中的态制备与临界动力学操控提供可操作路径。

---

### 11. A Data-Free Physics-Informed Neural Operator for Level-Set Interface Advection
Muhammad Akbar Khan · [2609.38195](https://arxiv.org/abs/2609.38195) · cs.LG · new

**为何相关：** 无数据物理信息神经算子学习 level-set 界面平流，仅用输运残差与几何约束训练——PINN/神经算子。

要点：界面问题算子通常依赖待替换求解器的参考解造数。本文构造 data-free 物理信息神经算子：界面为方程未知量，算子将初始界面映射到给定流场下的全时空轨迹；训练仅用输运残差与几何约束，目标中全程不出现参考解。展示纯方程驱动训练对 level-set 界面动力学的可行性，契合物理信息算子学习方向。

