# 9/21 arXiv 兴趣摘要（工作日）

扫了今天（美西 9/21，周一）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。新稿量：cond-mat 约 72、quant-ph 约 47。按兴趣锚点筛了 **12 篇**。Zotero 只读对照：这 12 个 arXiv 号库中均未命中（新文预期如此）；库内相关主题存量大致为 altermagnetism 相关条目数百、non-Hermitian 相关更多，未把已有文献当新发现硬推。

**建议先翻这三篇：**
1. **Autonomous stabilization of many-body entanglement with Floquet Hamiltonians and weak measurement** —— Floquet 工程非原生相互作用，再配弱测量耗散漏斗，直接打在开放系统 × 多体纠缠上。
2. **Symmetry Classification of Multipolar Orders … MagSymMultipoles** —— 把 altermagnetism 放进任意阶多极矩对称分类与自动化工具，方便对照材料与张量性质。
3. **Universal Eigenvector Statistics of Non-Hermitian Random Matrices** —— 非厄米本征矢量重叠的普适统计，覆盖十个对称类，和开放/非厄米动力学响应直接挂钩。

---

### 1. Autonomous stabilization of many-body entanglement with Floquet Hamiltonians and weak measurement
Charlotte Franke, Dorian A. Gangloff · [2609.21086](https://arxiv.org/abs/2609.21086) · quant-ph · new

**为何相关：** Floquet 哈密顿工程 + 弱测量耗散，把多体纠缠稳到目标态，是开放系统与驱动控制的交叉点。

要点：单纯耗散常会把纠缠毁掉，但若与相干相互作用巧妙配合，可把系统“漏斗”进目标纠缠态。多数平台原生相互作用与耗散通道难配对；文中提出把 Floquet 工程出的非原生相干项与弱测量交错，在可实现设定下自主稳定多体纠缠。

---

### 2. Symmetry Classification of Multipolar Orders in Crystals: Theory, Property Tensors and Automated Analysis with MagSymMultipoles
Maxime Braun, Quintin N. Meier · [2609.22030](https://arxiv.org/abs/2609.22030) · cond-mat.mtrl-sci · new

**为何相关：** 统一笛卡尔多极分解框架，明确列出 altermagnetism 等相所允许的多极序与性质张量。

要点：铁电、线性磁电、交错磁等相都可归到电/磁多极序。文中给出任意阶普通/环/极向多极的对称分类，并从晶体与磁对称判定铁性/反铁性允许分量；配套 MagSymMultipoles 做自动化分析，便于材料筛选与张量性质对照。

---

### 3. Universal Eigenvector Statistics of Non-Hermitian Random Matrices
Ze Chen, Zhenyu Xiao, Shinsei Ryu · [2609.22079](https://arxiv.org/abs/2609.22079) · cond-mat.stat-mech / mes-hall / quant-ph · new

**为何相关：** 非厄米本征矢量非正交性决定响应与动力学；给出谱体与原点附近重叠的解析普适式。

要点：用费米子 replica 非线性 σ 模型，把十个对称类的本征矢量重叠与对应厄米能级统计、拓扑扇区一一对应；大矩阵极限下给出解析，并在物理模型上数值核对。是读非厄米开放系统“响应敏感度”时很好的统计参照。

---

### 4. Floquet-spin-orbit compensation and flat- and quadratic-band contact in the α-T₃ lattice
Imtiaz Khan 等 · [2609.21586](https://arxiv.org/abs/2609.21586) · cond-mat.mes-hall / str-el · new

**为何相关：** Floquet 光场与本征自旋轨道补偿，在 α-T₃（石墨烯–dice 插值）里控制准能带简并与平带接触。

要点：圆偏光 Floquet 与内禀 SOC 对打，可分别实现谷–自旋、自旋–能带、平带–色散带三类成对简并。强调平带是连续哈密顿的精确性质而非两带近似假象；适合对照驱动拓扑与自旋轨道工程。

---

### 5. Non-Hermitian impurity scattering in graphene: Boltzmann transport and thermoelectric response
Juan A. Cañas 等 · [2609.22023](https://arxiv.org/abs/2609.22023) · cond-mat.mes-hall · new

**为何相关：** 把非厄米杂质（复势局域增益/损耗）嵌进石墨烯输运与热电响应。

要点：有限程圆对称复势下精确分波散射，得到非幺正 S 矩阵，并分开动量弛豫截面与净载流子交换截面；再接到 Boltzmann 层面讨论电导与热电。是“材料里的非厄米散射”一条很落地的线。

---

### 6. Ultimate Information Rate for Quantum Sensing under Multilevel Relaxation
Changhun Oh, Seok Hyung Lie, Youngrong Lim · [2609.21418](https://arxiv.org/abs/2609.21418) · quant-ph · new

**为何相关：** 多能级弛豫量子传感器在任意自适应控制下的信息率上界，贴量子传感极限。

要点：弱场耦合基态与多个会衰回基态的激发态（单激发时退化为振幅阻尼传感）。证明终极信息率恰等于与信号耦合的亮态平均寿命；虽有多衰减模，仍构造显式策略达到该界。

---

### 7. Persistent Quantum-Enhanced Frequency Sensing with T^{-3/2} Scaling
Clayton Z.C. Ho 等 · [2609.22046](https://arxiv.org/abs/2609.22046) · quant-ph / physics.atom-ph · new

**为何相关：** 用量子外差（Qdyne）把 Fock 态增强与退相干受限询问时间解耦，追求“持久”量子优势。

要点：非经典态增益往往伴随更快退相干，实际灵敏度难提升。文中把 Fock 增强嵌进 Qdyne，在短 τ 取量子增益，总积分时间 T 上给出 T^{-3/2} 标度的持续优势，回应“有用量子优势为何稀缺”。

---

### 8. Floquet physics from quantized light-matter interaction: geometric phases, gauge consistency, and entanglement
Beatriz Pérez-González, Sigmund Kohler, Mónica Benito · [2609.21741](https://arxiv.org/abs/2609.21741) · quant-ph / mes-hall · new

**为何相关：** 在大光子数相位基下，从全量子光–物质问题导出经典 Floquet，并讨论几何相、规范与纠缠。

要点：不把腔场换成经典轨迹或平均场解耦，仍由量子问题直接涌现时间依赖薛定谔方程；准能与光子扇区平移能级一一对应。把 Floquet 工程与腔 QED 接到同一量子图景，并审视几何相与纠缠的一致性问题。

---

### 9. Uhlmann Geometry of Fixed-Rank Density Matrices: A Fiber-Bundle Approach
Xu-Yang Hou, Hao Guo · [2609.21875](https://arxiv.org/abs/2609.21875) · quant-ph · new

**为何相关：** 固定秩混态（约化态、退相干自由子空间等）的 Uhlmann 丛不再平凡，可承载更有诊断力的几何/拓扑量。

要点：满秩密度矩阵态空间可缩、Uhlmann 丛拓扑平凡，相位难当稳健诊断；固定秩混态支撑随参数可变，纤维丛结构更丰富。用纤维丛语言整理其几何，对开放系统混态物相判据有直接参考价值。

---

### 10. Entanglement-Inducing Quantum Markov Processes
J. Fransson, A. P. Sowa · [2609.21438](https://arxiv.org/abs/2609.21438) · math-ph / quant-ph · new

**为何相关：** 非线性非局域演化（Schrödinger–Dirichlet）可从可分初态生成纠缠，区别于保积结构的常规平均场闭包。

要点：与 Bose–Hubbard、广义玻色子相关；核心方程非线性、非局域，动力学不必保持直积结构。分析方法走正有理数乘法群上的调和分析；为“开放/有效马尔可夫型过程如何造纠缠”提供新模型。

---

### 11. Asymptotics for Frequency Redundancies in Quantum Machine Learning Models
Felix Paul, Bhilahari Jeevanesan, Peter Jung · [2609.21916](https://arxiv.org/abs/2609.21916) · quant-ph · new

**为何相关：** 量子傅里叶模型（QFM）频率谱冗余如何由数据重上传哈密顿本征值塑造，影响表达力与可训练性。

要点：用生成函数给出若干结构化本征值选择（等差、单比特 Pauli 编码等）的精确与渐近冗余分布；说明层间相同本征值设定下冗余如何趋于特定剖面，便于对照 QML 设计里的频谱瓶颈。

---

### 12. Nonlocal Magic Spreading in Many-body Quantum Dynamics: From Chaotic Evolution to Quasi-particle Picture in Integrable Models
Sreemayee Aditya, Piotr Sierant, Xhek Turkeshi · [2609.20951](https://arxiv.org/abs/2609.20951) · quant-ph / stat-mech · new

**为何相关：** 把 nonlocal magic（局域基变换后仍剩的 magic）接到纠缠哈密顿涨落（entanglement capacity），看混沌与可积动力学中的传播。

要点：纠缠与 magic 互补；nonlocal magic 刻画“抹不掉”的非稳定性资源。文中把它与 entanglement capacity 联系起来，从而在混沌到可积的广谱动力学里给出可解析控制的预言，补充多体纠缠动力学工具箱。
