# 9/22 arXiv 兴趣摘要（工作日）

扫了今天（美西 9/22，周二）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。新稿量：cond-mat 约 144、quant-ph 约 113。按兴趣锚点筛了 **11 篇**（含 1 篇光学向交叉上架、但与非厄米时间晶体直接相关）。Zotero 本轮本机未连上，未做库内去重对照。

**建议先翻这三篇：**
1. **Non-Hermitian Topology from Edge Transport in Hermitian Quantum Anomalous Hall Systems** —— 全局厄米的量子反常霍尔体系里，手征边模与扩散边模耦合出本征非互易输运，把非厄米皮肤效应写进可测的 Hall-bar 观测量。
2. **Ferroelectric switching of odd-parity magnon spin splitting** —— 室温铁电切换 BiFeO₃ 中的奇宇称磁振子自旋劈裂，补上 altermagnetism / 补偿磁体在玻色集体激发侧的实验缺口。
3. **Superconducting qubit based on altermagnets** —— 用超导体–交错磁–超导体结的可编程电流–相位关系，设计一类兼具大非谐性与电荷噪声防护的类 transmon 比特。

---

### 1. Non-Hermitian Topology from Edge Transport in Hermitian Quantum Anomalous Hall Systems
Humian Zhou, Ming Lu, Chui-Zhen Chen, X. C. Xie · [2609.23099](https://arxiv.org/abs/2609.23099) · cond-mat.mes-hall · new

**为何相关：** 不靠外加增益/损耗工程，在全局厄米的拓扑霍尔体系里“长出”非厄米拓扑与皮肤效应，和你关心的非厄米拓扑落地场景很贴。

要点：单向手征边模与扩散型正常边模并存时，有效边输运可用连续 Hatano–Nelson 描述，非互易本征出现。电化学势与局域热耗散呈现依赖手征性的指数空间轮廓，纵向电导随尺寸指数衰减而霍尔电导相对稳健；把皮肤效应直接编码进 Hall-bar 可观测量。

---

### 2. Ferroelectric switching of odd-parity magnon spin splitting
Yuhan Liang, Xingyu Yan 等 · [2609.24182](https://arxiv.org/abs/2609.24182) · cond-mat.mtrl-sci · new

**为何相关：** 交错磁里常见偶宇称自旋织构；奇宇称自旋劈裂在电子能带侧已有讨论，磁振子侧此前缺实验，本文给出室温铁电可编程证据。

要点：以多铁 BiFeO₃ 的输运为探针，对称分析与自旋波计算表明旋磁序支持奇宇称磁振子自旋纹理。铁电极化翻转可开关该劈裂，且在室温工作——把“电压写自旋织构”推进到绝缘磁体中的集体玻色激发。

---

### 3. Superconducting qubit based on altermagnets
Xue-Feng Pan, Xin-Lei Hei, Franco Nori, Peng-Bo Li · [2609.24759](https://arxiv.org/abs/2609.24759) · quant-ph / supr-con · new

**为何相关：** 把 altermagnetism 的动量依赖自旋劈裂嵌进 Josephson 工程，直接接到超导量子比特设计。

要点：在 SC–altermagnet–SC 结中按器件几何定制电流–相位关系，得到可编程 Josephson 势。基于此提出类 transmon 架构：大非谐性，并利用相干双库珀对隧穿增强对退相干的鲁棒性；在 \(2\phi\) 结区因宇称保护抑制电荷噪声，磁通可精细调谐。

---

### 4. Correlation-assisted spin-selective metallicity in strained and bilayer altermagnets
Marnin J. Di Nunzio, Frank Lechermann, Ilya M. Eremin · [2609.23150](https://arxiv.org/abs/2609.23150) · cond-mat.str-el · new

**为何相关：** 在最小 Hubbard 型单层/双层模型里，系统看关联、掺杂、单轴应变与层间耦合如何塑造交错磁序与自旋极化费米面。

要点：Hartree–Fock 与旋转不变奴隶玻色子法对照，显示交错磁序对准粒子重整化稳健，且磁序出现与准粒子相干性丧失可分离。单层掺杂有显著粒子–空穴不对称；掺杂加单轴应变可在近半满处给出全自旋极化费米面。双层堆叠决定铁磁/反铁磁层间耦合，进而调控自旋选择金属性。

---

### 5. Non-Hermitian quantum phase transitions in the XY model induced by staggered imaginary Dzyaloshinskii–Moriya interaction
Hong Jiang, Xiang-Ping Jiang, Yan-Chao Li · [2609.23721](https://arxiv.org/abs/2609.23721) · quant-ph / stat-mech · new

**为何相关：** 交错虚 DM 驱动的非厄米 XY 链，精确对角化后给出例外边界与 \(\mathcal{RT}\) 破缺相，并检验常用量子信息探针是否失效。

要点：\(D<1\) 可经交错非幺正变换映到厄米 XY，相界可解析；\(D=1\) 为准粒子本征值/矢量聚并的例外边界；\(D>1\) 整体落在 \(\mathcal{RT}\) 破缺区并含两类 \(z\) 铁磁相。纠缠熵、量子失协、相干性等常规探针抓不住 \(\mathcal{RT}\) 破缺转变，文中据此提出更合适的诊断量。

---

### 6. Non-Hermitian photonic time quasicrystal
Shuhang Chen, Zhi Zheng, Qi Zhu · [2609.24327](https://arxiv.org/abs/2609.24327) · physics.optics / cond-mat.dis-nn · cross

**为何相关：** 时间域非厄米 Aubry–André–Harper 类比，把 Floquet/时间晶体放大与 Avila 加速度等准周期算子理论接到可观测光学响应。

要点：把非公度时间调制延拓到复相位平面后，体放大率随复化坐标分成若干整数相，每相内斜率锁定为整数（Avila 加速度）。该量子化响应在保持解析相位结构的介电调制缺陷下仍存活；不同整数相的输入频率获得指数级分离的放大，形成光谱选择。

---

### 7. Critical Touching of Temporal Entanglement Transitions
Ting-Long Wang, Shi-Xin Zhang, Shuai Yin, Yi-Fan Jiang · [2609.23513](https://arxiv.org/abs/2609.23513) · cond-mat.stat-mech / quant-ph · new

**为何相关：** 周期驱动下的时间纠缠转变（TET）通常像一级相变的线性交叉；本文给出“临界相切”的连续型时间纠缠转变。

要点：在周期驱动横场 \(J_1\)-\(J_2\) Ising 链中，两个 TET 可合并为临界相切：主导 Schmidt 能级相切而不交换，是时间域的连续相变类比。临界频率附近时间纠缠谱与动力学标度可解析/数值刻画，拓展非平衡纠缠相变分类。

---

### 8. Universal Response Functions in Driven Dissipative Tunneling Dynamics
Krishna Kingkar Pathak · [2609.22328](https://arxiv.org/abs/2609.22328) · cond-mat.stat-mech · new

**为何相关：** Floquet 调制与耗散记忆同时存在时，势垒隧穿是否仍服从普适响应——直接落在驱动开放系统动力学。

要点：半经典瞬子框架纳入 Floquet 与欧姆环境耦合后，隧穿指数分解为体系依赖的静态部分与两参数普适函数（归一化驱动频率 × 耗散强度）。说明周期驱动与非局域耗散记忆并存时，宏观响应仍可由少数无量纲控制量刻画。

---

### 9. Physics-Informed Classical and Quantum Neural Networks for One-Dimensional Schrödinger Eigenvalue Problems
Tariq Mahmood, Waqas Arshad, Bilal Naseer, Alfredo Raya · [2609.22189](https://arxiv.org/abs/2609.22189) · quant-ph / cs.LG · new

**为何相关：** 把 PINN 与物理信息量子神经网络（PIQNN）并排放在可精确求解的 1D 薛定谔本征问题上，贴 PINN / 量子–经典混合求解线。

要点：谐振子、无限/有限方势阱三类基准；复合损失含方程残差、归一化、边界与本征态正交，无需监督标签。结果与精确谱及 Numerov、有限差分、谱方法对照，比较经典 PINN 与 PIQNN 在精度与训练行为上的差异。

---

### 10. Bootstrap certification of string order in quantum spin chains
Sagnik Banerjee, Haoyu Guo, Debanjan Chowdhury · [2609.22420](https://arxiv.org/abs/2609.22420) · cond-mat.str-el / quant-ph · new

**为何相关：** 多体 bootstrap 不显式写变分波函数，却要认证诊断拓扑相的长程弦关联——成本原先指数爆炸，本文用弦算符代数压到多项式。

要点：把裸弦与端点修饰弦当作原对象，与局域词构成闭算符代数，半定规划成本随弦长多项式增长，一次计算给出各长度弦关联估计。在基态能量被钉在窗口内后，对目标弦给出严格双边界；在 cluster Ising 与自旋-1 链上与 DMRG 对照。

---

### 11. Watching Quantum Models Think: Hilbert-Space Interpretability in Quantum Transformer Blocks
Diego Iacopetta, Andrea Gasparini · [2609.23016](https://arxiv.org/abs/2609.23016) · quant-ph / cs.LG · new

**为何相关：** 量子 Transformer 块里跟踪互信息、纠缠熵与保真度，把 QML 的可解释性做进希尔伯特空间结构本身。

要点：全相干变分电路含注意力与前馈的量子类比；在四类已知依赖结构任务上，学到的互信息矩阵与真依赖对齐（lookup 任务 AUC≈0.69），关掉纠缠门准确率从满分塌到近随机。展示量子模型可走“先天可解释”路线，而不只是再造黑箱。
