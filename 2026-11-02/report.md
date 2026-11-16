# 11/02 arXiv 兴趣摘要（工作日）

扫了今天（美西 11/02，周一）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Monday, 2 November 2026**；新投稿：cond-mat 81、quant-ph 74、hep-th 23、math-ph 12、cs.LG 111、stat.ML 12（交叉与替换未计入）。已排除此前已荐的 314 篇。主题上交错磁（Berry 曲率四极矩三阶霍尔、Cr–MnTe 铁磁/交错磁共存、自旋分流临界散射）与 Floquet/光致拓扑（石墨烯光致 Haldane 隙、时空等离激元晶体例外点）较集中；非厄米侧有片上磁子–声子例外点/无反射态与 PT 对称反铁磁亚隙二次谐波，以及 Liouvillian 光谱快照方法；NNQS 有莫尔原子单重–三重态神经量子态，另有超导处理器上的 Laughlin 型 FCI 与加权超图态量子计量。按兴趣锚点筛了 **11 篇**（全部为新投稿；未收替换稿；跳过假阳性如 Burgers 方程 PINN 硬约束投影、活体转子手性软物质、SKFitter 紧束缚拟合工具、天线有限元量子线性求解、位错脱钉/III–V 生长/Bi-2212 涡旋钉扎等弱 PINN 命中，以及宽泛全同粒子 Colloquium、纯数学 port-Hamiltonian/Potts 混合、引力远区 PN、弱相关通用 QML 硬件分类题等）。本日用户机 Zotero 库不可用，仅对 10/30 缓存的 arXiv ID 列表（187）做只读核对：**短名单无同 ID**（当日新稿几乎不可能撞库）；主题近邻未逐条标注。

**建议先翻这三篇：**
1. **Observation of light-induced Haldane gap in graphene** —— 圆偏振光驱动单层石墨烯中用 trARPES 直接观测到 Dirac 点光致 Haldane 隙，并伴随动量分辨 Floquet–Bloch 边带——Floquet Chern × 实验拓扑态。
2. **Berry curvature quadrupole induced third-order anomalous Hall effect in altermagnetic KV₂Se₂O** —— d 波交错磁 KV₂Se₂O 中 Berry 曲率偶极与体积分均被对称性禁戒，三阶反常霍尔由 Berry 曲率四极矩主导，并用 Wannier 插值自洽计算——交错磁 × 非线性量子几何输运。
3. **Intertwined ferromagnetic and altermagnetic orders in Cr-doped MnTe** —— Cr 掺杂 MnTe 中铁磁与交错磁可均匀共存且热力学上仍可区分：谁先有序会把对方变成交叉或压制面外剩磁，SOC 还让铁磁矩选择交错磁畴流形——交错磁 × 铁磁共存实验。

---

### 1. Observation of light-induced Haldane gap in graphene
Fei Wang · Xuanxi Cai · Wanying Chen 等 · [arXiv:2610.42115](https://arxiv.org/abs/2610.42115) · cond-mat.mes-hall · new

**为何相关：** 圆偏振光驱动单层石墨烯中用 trARPES 直接观测到 Dirac 点光致 Haldane 隙，并伴随动量分辨 Floquet–Bloch 边带——Floquet Chern × 实验拓扑态。

要点：圆偏振光被预言可在石墨烯 Dirac 点动态打破时间反演并打开拓扑非平凡隙，但该隙本身长期缺乏直接光谱证据。作者用时间–角度分辨光电子能谱观测到：隙仅在圆偏振泵浦下与光场同步出现，线偏振则无；同时在动量空间分辨到 Floquet–Bloch 边带，边带间距与泵浦光子能量一致。结果首次给出光致 Haldane 隙的直接光谱指纹，把 Floquet 拓扑相从输运/间接证据推进到能带结构层面的观测。

*Zotero：本日无法访问实时库；10/30 缓存 ID 列表中无同 ID。*

---

### 2. Berry curvature quadrupole induced third-order anomalous Hall effect in altermagnetic KV₂Se₂O
Jiacheng Yao · Zhuocheng Lu · Zhichao Guo 等 · [arXiv:2610.41274](https://arxiv.org/abs/2610.41274) · cond-mat.mes-hall · new

**为何相关：** d 波交错磁 KV₂Se₂O 中 Berry 曲率偶极与体积分均被对称性禁戒，三阶反常霍尔由 Berry 曲率四极矩主导，并用 Wannier 插值自洽计算——交错磁 × 非线性量子几何输运。

要点：交错磁兼具补偿磁序与动量依赖自旋劈裂，是非线性量子几何输运的理想平台。对所考虑的 d 波交错磁，反幺正对称 TC₄z 强制动量积分 Berry 曲率为零，反演对称又禁戒 Berry 曲率偶极，故 Berry 曲率四极矩（BCQ）可贡献按 τ² 标度的非线性霍尔响应。作者给出可从第一性原理 Wannier 紧束缚哈密顿量直接计算 BCQ 的规范协变插值公式，并应用于 KV₂Se₂O：动量分辨显示主导贡献来自旋–轨道耦合诱导的避免交叉，把能隙结构与符号翻转的非线性电导直接相连。

*Zotero：本日无法访问实时库；10/30 缓存 ID 列表中无同 ID。*

---

### 3. Intertwined ferromagnetic and altermagnetic orders in Cr-doped MnTe
Jonathan M. DeStefano · Yaofeng Xie · Guodong Ren 等 · [arXiv:2610.40870](https://arxiv.org/abs/2610.40870) · cond-mat.mtrl-sci · new

**为何相关：** Cr 掺杂 MnTe 中铁磁与交错磁可均匀共存且热力学上仍可区分：谁先有序会把对方变成交叉或压制面外剩磁，SOC 还让铁磁矩选择交错磁畴流形——交错磁 × 铁磁共存实验。

要点：铁磁与交错磁均破时间反演，但晶体对称下二者序参量禁止直接双线性耦合，能否保持热力学上可区分又相互强烈影响一直未决。作者在 Cr 掺杂 MnTe 中证明二者可均匀共存：调节铁磁有序温度跨过几乎不变的 Néel 温度后，若交错磁先出现则铁磁转变退化为交叉；若铁磁先出现则交错磁起序会强烈压制面外铁磁剩磁。自旋–轨道耦合进一步给出对称性选择的相互作用，使铁磁矩的面外/面内分量分别偏置时间反演（Z₂）与取向（Z₃）交错磁畴扇区。

*Zotero：本日无法访问实时库；10/30 缓存 ID 列表中无同 ID。*

---

### 4. Magnetic control of reflectionless states and an intrinsic-mode exceptional point in a magnon-phonon coupling system
Mingyuan Ma · Jiongjie Wang · Chong Chen 等 · [arXiv:2610.41851](https://arxiv.org/abs/2610.41851) · cond-mat.mtrl-sci · new

**为何相关：** 片上磁子–声子异质结中用二维磁场调控实现近零反射的无反射态，并独立把本征模谱扫过例外点——非厄米 × 磁子自旋电子学 × 实验。

要点：无反射态与例外点是非厄米体系的标志性奇异响应，但在紧凑集成平台上独立实现与调谐仍难。作者在 FeGaB–32°YX-LiNbO₃ 异质结的片上磁子–声子系统中展示二维磁控：磁场大小调谐磁子–声子失谐，把低损耗反射零点扫过实频轴，得到近乎消失反射的可调无反射态；测得的复 S₁₁ 绕反射零奇点闭合一周累积 −2π 相位卷绕。独立地，旋转磁场调谐耦合强度，使本征模谱跨越例外点，表现为实部/虚部分裂的交换。统一的一端口输入–输出模型把测量与非厄米谱结构联系起来。

*Zotero：本日无法访问实时库；10/30 缓存 ID 列表中无同 ID。*

---

### 5. Singlet-Triplet Transition of Rotating Moiré Atoms in a Magnetic Field
Conor Smith · Yubo Yang · Shiwei Zhang 等 · [arXiv:2610.40786](https://arxiv.org/abs/2610.40786) · cond-mat.str-el · new

**为何相关：** 服从磁周期边界、含完整朗道能级混合的神经量子态，映射双电子莫尔原子的单重–三重态转变与旋转最大密度液滴——NNQS × 莫尔关联。

要点：莫尔超晶格可把若干电子束缚在势阱极小处，形成少电子“莫尔原子”。作者用满足磁周期边界、包含完整朗道能级混合并处理两自旋扇区的神经量子态，作为阱深与磁场的函数绘制双电子莫尔原子基态。强场下每个原子是自旋三重态最大密度液滴，具有 〈L_z〉=−1 与持续环流，是近期成像的莫尔“Wigner 分子晶体”的旋转对应物；加深势阱驱动到非旋转自旋单重态。转变点处轨道磁矩随自旋极化翻转而变号，可用磁强计联合读出。工作把 NNQS 直接接到莫尔原子的量子点类单重–三重态物理。

*Zotero：本日无法访问实时库；10/30 缓存 ID 列表中无同 ID。*

---

### 6. Subsonic terahertz plasmon instability in space-time plasmonic crystals
H. Terças · J. L. Figueiredo · P. Cosme · [arXiv:2610.40880](https://arxiv.org/abs/2610.40880) · cond-mat.mes-hall · new

**为何相关：** 行波周期调制下的二维电子流体形成时空等离激元晶体：Bragg 隙闭合给出例外点并触发 Krein 型不稳定性，即便实验室系亚音速漂移亦可自放大——Floquet × 例外点。

要点：作者用流体力学结合 Floquet–Bloch 理论研究二维电子流体在有效等离激元速度行波周期调制下的集体波动力学。行波调制构成运动的等离激元晶体，共动系中能带由有效漂移速度决定；布里渊区边缘 Bragg 隙闭合产生例外点，并通过正/负能量模耦合触发 Krein 型不稳定性。解析给出阈值与增长率，表明即便实验室系电子漂移保持亚音速也可自放大；非线性流体方程数值模拟确认理论，并演化到由相干 Floquet–Bloch 模主导的饱和态。结果把时空等离激元晶体指认为波放大与非厄米 Floquet 物理的新平台。

*Zotero：本日无法访问实时库；10/30 缓存 ID 列表中无同 ID。*

---

### 7. Quantum-Geometric Subgap Second-Harmonic Generation in PT-Symmetric Antiferromagnetic Insulators
Shakeel Ahmad · Fei Xue · [arXiv:2610.41167](https://arxiv.org/abs/2610.41167) · cond-mat.mes-hall · new

**为何相关：** PT 对称反铁磁绝缘体中识别由带间 Hermitian 联络实部主导的本征亚隙二次谐波产生，在层陈相增强并随 Néel 序变号——PT × 量子几何 × 反铁磁读出。

要点：量子几何在输运与光学响应中作用已较明确，但时间反演奇的 Riemannian 联络对完全亚隙响应的贡献仍少被讨论。作者在 PT 对称反铁磁体中识别本征二次谐波产生：主要由带间 Hermitian 联络的实部主导，且完全来自虚跃迁。在双层 MnBi₂Te₄ 中，该响应在平庸相仍存，在层陈相增强，并随 Néel 序变号，从而在无载流子、无实激发条件下提供量子几何探针与反铁磁序的相位敏感读出。

*Zotero：本日无法访问实时库；10/30 缓存 ID 列表中无同 ID。*

---

### 8. Liouvillian spectral snapshots: A reduced-subspace approach for time-dependent and noisy open quantum systems
Hans Christiansen · André Melo · Jens Paaske 等 · [arXiv:2610.40808](https://arxiv.org/abs/2610.40808) · quant-ph · new

**为何相关：** 对时变驱动与有色经典噪声下的开放量子系统，用若干扰动点的慢衰减 Liouvillian 本征算符压缩成可复用约化子空间——开放系统 × Liouvillian 谱方法。

要点：驱动–耗散量子器件常在时变驱动与时间关联经典噪声下工作；当扰动与本征动力学同量级时，旋转波与马尔可夫近似易失效，需直接模拟时变主方程，对长时亚稳态切换与多噪声实现平均尤其昂贵。作者提出 Liouvillian 光谱快照（LSS）：在若干自适应采样的扰动值处计算缓慢衰减、低频的 Liouvillian 本征算符并压缩为公共基，把主方程投影到刻画粗粒动力学的低维子空间。该基只需构建一次即可跨噪声实现与参数复用，显著降低系综平均与参数扫描成本。

*Zotero：本日无法访问实时库；10/30 缓存 ID 列表中无同 ID。*

---

### 9. Preparation of a Laughlin-like fractional Chern insulator on a superconducting quantum processor
Kamil Dutkiewicz · Bárbara Andrade · Geza Giedke 等 · [arXiv:2610.41017](https://arxiv.org/abs/2610.41017) · quant-ph · new

**为何相关：** 在超导量子处理器上用经典优化变分线路制备环面 Laughlin 型分数量子陈绝缘体及带两个准空穴的态，并分辨准空穴环流——拓扑序 × 数字量子模拟。

要点：分数量子陈绝缘体是分数量子霍尔态的晶格类比，承载拓扑序与任意子激发，是量子模拟的高难度目标。作者在 IBM Nighthawk 超导处理器上，用经典优化的变分线路实现玻色 FCI：目标态是环面上长程母哈密顿量的精确零能 Laughlin 型基态，消除物理边缘并利于小系统触及分数量子霍尔物理。在 4×4 量子比特格子上制备四玻色子 FCI 基态与含两个准空穴的三玻色子态；粒子密度与关联复现特征结构，重构的手性磁化电流分辨准空穴环流图案，为数字模拟分数化激发与编织测量铺路。

*Zotero：本日无法访问实时库；10/30 缓存 ID 列表中无同 ID。*

---

### 10. Weighted hypergraph states as a resource for quantum metrology
B. J. Alexander · M. S. Tame · [arXiv:2610.42129](https://arxiv.org/abs/2610.42129) · quant-ph · new

**为何相关：** 按图拓扑划分子类的加权超图态在宽边权区间上量子 Fisher 信息优于可分态与标准加权图态，高阶超边还提升抗退相干能力——量子计量 × 纠缠资源。

要点：量子关联可把传感精度推过经典极限，但所需关联资源态往往难制备与保存。作者研究加权超图态族，按底层图拓扑识别具有增强计量性能的子类；结合量子 Fisher 信息与 Dicke 态基表示，证明这些子类在对应弱受控操作的宽边权区间上优于可分态与标准加权图态基准。给出任意 N 的解析公式，并以 N=4 详析；通过局域退相干临界概率表明，为 N 量子比特加入高阶加权超边可增强计量鲁棒性，使态在更高噪声水平仍保有量子优势。

*Zotero：本日无法访问实时库；10/30 缓存 ID 列表中无同 ID。*

---

### 11. Spin conservation protects the altermagnetic spin-splitter current from critical scattering
Yunxi Jiang · Hao Yu · [arXiv:2610.41419](https://arxiv.org/abs/2610.41419) · cond-mat.mes-hall · new

**为何相关：** 临界磁涨落下交错磁自旋分流电流仅当涨落守恒自旋时才与电荷流同受保护；正向自旋翻转会以准粒子速率均衡两自旋布居——交错磁 × 自旋分流输运。

要点：磁相变附近临界涨落强烈散射电子，但电荷流仍可存活，因长波涨落几乎不改变速度方向。在交错磁中电场还驱动自旋流（自旋分流效应），而近乎前向的自旋翻转会把电子送到几乎同速的另一自旋带。作者求解含完整碰撞算子（并计入磁序变化）的玻尔兹曼方程：自旋守恒涨落以与电荷弛豫相当的速率松弛自旋流；前向翻转则以二维中随关联长度线性增长的准粒子速率均衡等能两自旋布居。因此相同电阻率的涨落可使自旋分流比朝相反方向变化；能量守恒保护由占据态能带位移携带的自旋流分量，自旋劈裂在费米线间距超过关联长度倒数后阻断前向翻转。

*Zotero：本日无法访问实时库；10/30 缓存 ID 列表中无同 ID。*

---
