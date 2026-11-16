# 10/28 arXiv 兴趣摘要（工作日）

扫了今天（美西 10/28，周三）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Wednesday, 28 October 2026**；新投稿：cond-mat 115、quant-ph 50、hep-th 37、math-ph 13、cs.LG 149、stat.ML 15（交叉与替换未计入）。已排除 10 月已荐的 197 篇。交错磁侧有 SOC 激活的额外自旋劈裂与自旋输运半角锁定；开放/非厄米侧有边界耗散重构 Chern 边缘态、Liouvillian EP 上的最优量子判别与传感标度极限、双正交动力学量子相变的 Fisher 零线反常，以及 CISS spinterface 中两种不可混用的近 EP 体制；纠缠与拓扑有双曲规范–Higgs 的测量诱导纠缠相（含“群岛”对称保护拓扑）与 SW-SSB 的 QFI 亏缺诊断；方法侧有环面连续 anyon 的 AnyFormer 神经变分波函数，以及使 TEMPO 内部键维与系统尺寸脱钩的张量网结构；自旋电子学还有 Kagome 平带金属 CoSn 中远超 Pt 的自旋–电荷转换，以及非共面反铁磁 CoTa₃S₆ 的零场自发拓扑二极管。按兴趣锚点筛了 **11 篇**（全部为新投稿；未收替换稿；跳过贝叶斯最快检测 QD-PINN、可持续合金 ML、纳米颗粒自组装学习、黑洞标量毛、UTe₂ 二极管等假阳性 PINN/NN 命中，以及纯 NISQ QAOA 噪声阈值、软物质朗之万耗散、宇宙学开放 EFT 讲义等弱相关）。已对本地 Zotero 库做只读核对：**短名单无同 arXiv ID**；2610.36521 与库内双正交非厄米 DQPT 条目主题高度相近，已在条目中注明。

**建议先翻这三篇：**
1. **Continuum neural wavefunctions for anyons on a torus** —— 提出 AnyFormer：环面连续 anyon 的神经变分波函数，显式纳入统计相互作用与整体绕数约束，可用 VMC 扩到 N=16——NNQS × 拓扑有序 × anyon 多体。
2. **Unconventional SOC-activated Altermagnetic Spin Splitting and Half-Angle Locking of Spin Transport** —— SOC 与交错交换可在非相对论贡献消失的动量面上“激活”额外自旋劈裂；α-MnTe 近 Γ 呈 d 波、自旋输运对 Néel 矢量呈近半角锁定——交错磁 × SOC × 自旋输运。
3. **Optimal quantum discrimination at Liouvillian exceptional points** —— 有限维 Lindblad 系统中 EP 不改善弱扰动探测时间对强度的标度，但可借提升 QFI 率缩短达预定精度的观测时间——非厄米传感 × Liouvillian EP × 计量。

---

### 1. Continuum neural wavefunctions for anyons on a torus
Ahmed Khalifa · Shubhayu Chatterjee · [arXiv:2610.36567](https://arxiv.org/abs/2610.36567) · cond-mat.str-el · new

**为何相关：** 提出 AnyFormer：环面连续 anyon 的神经变分波函数，显式纳入统计相互作用与整体绕数约束，可用 VMC 扩到 N=16——NNQS × 拓扑有序 × anyon 多体。

要点：作者引入 AnyFormer，面向环面上连续 anyon 的神经变分框架：构造光滑轨道标架以强制矩阵值环面边界条件，并以解析对因子保证碰撞正则行为；轨道几何与多体振幅由变分蒙特卡罗并行优化。对无外场、无相互作用势的 semion，框架可隔离纯由统计产生的关联：两 semion 能量与精确结果高度吻合，N=4、6 时变分能低于有限截断精确对角化；扩至 N=16（远超连续对角化），呈现显著关联空穴、长波密度涨落抑制，以及由平均间距设定的对环流反转；N=12、16 时环流出现阻尼空间振荡。工作为体 anyon 物质的微观关联与手性运动提供可扩展的 NNQS 路径。

---

### 2. Unconventional SOC-activated Altermagnetic Spin Splitting and Half-Angle Locking of Spin Transport
Weiwei Chen · Ziyu Zhou · Pan Gao · Yanan Pan 等 · [arXiv:2610.37367](https://arxiv.org/abs/2610.37367) · cond-mat.mtrl-sci · new

**为何相关：** SOC 与交错交换可在非相对论贡献消失的动量面上“激活”额外自旋劈裂；α-MnTe 近 Γ 呈 d 波、自旋输运对 Néel 矢量呈近半角锁定——交错磁 × SOC × 自旋输运。

要点：常规交错磁自旋劈裂来自交错交换与子格依赖的各向异性跃迁，无需 SOC。作者给出低能有效模型：SOC 与交错交换可在非相对论贡献为零的动量面上共同激活额外自旋劈裂。六角 α-MnTe 中，该 SOC 激活项在 Γ 附近产生出平面极化的 d 波自旋劈裂，其主导角依赖相对面内 Néel 矢量旋转呈半角反转。第一性原理自旋输运计算显示，Néel 取向与使纵向/横向自旋电导取极值的电场方向之间存在近似半角锁定；有效模型解析表明，锁定源于控制劈裂图案的同一动量–Néel 角耦合。工作把 SOC 激活的微观机制直接接到可探测的定向自旋流。

---

### 3. Optimal quantum discrimination at Liouvillian exceptional points
Aritra Ghosh · M. Bhattacharya · [arXiv:2610.37660](https://arxiv.org/abs/2610.37660) · quant-ph · new

**为何相关：** 有限维 Lindblad 系统中 EP 不改善弱扰动探测时间对强度的标度，但可借提升 QFI 率缩短达预定精度的观测时间——非厄米传感 × Liouvillian EP × 计量。

要点：非厄米传感的核心问题是：例外点（EP）是否真让弱扰动更易探测。作者证明：在具唯一稳态且弛豫隙非零的有限维 Lindblad 系统中，尽管谱响应增强，EP 并不改变可靠探测所需观测时间随扰动强度的标度。但若选择性选取能提升量子 Fisher 信息率的扰动，相对同衰减率的非 EP 参考，EP 仍可缩短达到预定探测精度的时间。以光力模型在 EP 处为例，可在更短时间内以同等可靠性通过腔输出探测弱力。结果厘清 EP 探测的基本极限，并指导光力腔、超导比特与阱离子上的更快非厄米传感器设计。

*Zotero：库中无同 ID；有 Liouvillian EP 相关条目（热机签名等），主题相邻。*

---

### 4. Reconstructing chiral edge states via boundary dissipation
Xin-Ran Ma · Kui Cao · Qian Du · Zheng Wei · Su-Peng Kou · [arXiv:2610.37164](https://arxiv.org/abs/2610.37164) · cond-mat.mes-hall · new

**为何相关：** 边界耗散可重构 Chern 绝缘体手性边缘态并决定弱/强损耗下的有效衰变率，强损耗下经虚耦合到阻尼亮通道——开放边界 × 拓扑边缘 × 例外点阈值。

要点：边界耗散会重塑 Chern 绝缘体拓扑边缘模的空间轮廓与衰变。作者建立微观边界通道框架：保留损耗外轨道与厄米内系统的归一化边缘态，识别直接耦合的亮边界通道，并用 Feshbach 自能纳入其余内态。Qi–Wu–Zhang 模型中，弱损耗衰变主导项由原边缘态在损耗边界上的概率权重决定，耦合修正自立方阶起；强损耗下，重构的内边缘态经虚耦合到阻尼亮通道衰变，速率正比于微观耦合平方、反比于裸损耗。Haldane 模型表明主导机制对另一类胞间跃迁仍成立，而矩阵值自能反馈会在有限损耗下修改边界谱并移动例外点阈值。工作给出边界态重构与衰变的统一微观描述，并指向光子/声子晶体与拓扑电路实验检验。

---

### 5. Measurement-induced entanglement phases in hyperbolic gauge-Higgs models
Cole Kelson-Packer · Hiroki Sukeno · Akimasa Miyake · [arXiv:2610.36528](https://arxiv.org/abs/2610.36528) · cond-mat.str-el · new

**为何相关：** 双曲格子上仅测量动力学的规范–Higgs 模型给出纠缠相图，并出现欧氏空间所无的“群岛”对称保护拓扑相——测量诱导纠缠 × 拓扑 × 双曲几何。

要点：平坦时空规范–Higgs 理论是区分纠缠结构的多相模版；双曲空间的广阔边界如何改写这些结构仍开放。作者研究双曲格子上仅由测量驱动的规范–Higgs 纠缠相：用拓扑纠缠熵与为双曲 Higgs 相定制的广义测量诱导纠缠绘制二维相图。借助对偶，发现欧氏空间所无的“群岛”相——体中分离的对称保护拓扑团簇；该相与邻接拓扑/平凡相之间的转变临界指数 δ 属平均场普适类。核心工具是受测量基量子计算启发的三维资源态，用第三纠缠方向模拟二维量子态的时空演化，从而把时空“海绵”映射到经典渗流并推断相界临界点。

---

### 6. Quantum Fisher Information Deficit as a Geometric Signature of Strong-to-Weak Spontaneous Symmetry Breaking
Zhang-Chi Yin · Wei Zheng · [arXiv:2610.37092](https://arxiv.org/abs/2610.37092) · quant-ph · new

**为何相关：** 强到弱自发对称破缺（SW-SSB）表现为对称中性对旋转下相对最大 QFI 的持续亏缺，并与保真度/Rényi-1 关联等价——开放系统相 × 量子 Fisher 信息。

要点：SW-SSB 已成为描述开放系统量子相的框架，但无法用常规带电两点关联刻画。作者证明：对具局域带电对合的强 ℤ₂ 对称态，SW-SSB 表现为在对称中性对旋转下相对最大量子 Fisher 信息的持续亏缺；模型无关不等式层级建立该亏缺与保真度、Rényi-1 关联作为渐近长程序诊断的等价性，并把有限角态重叠接到同一对生成轨道上的无穷小 Bures 几何约束。对称投影 Gibbs 态上进一步给出由对操作注入平均能量控制的亏缺下界；局域性使该能量代价在系统尺寸与端点间距上一致有界，从而在任意固定有限温度下保持相对最大 QFI 的有限隙。当普通带电长程序缺席时，这一持续几何约束为热 SW-SSB 提供可定量的信息几何刻画。

---

### 7. The TEMPO network can be made independent of the system size
Valentin Link · [arXiv:2610.37012](https://arxiv.org/abs/2610.37012) · quant-ph · new

**为何相关：** 在通常二阶时间步误差内，TEMPO 影响泛函张量网内部键维可压到仅依赖耦合通道数、与系统尺寸无关——开放系统 × 非马尔可夫 × 张量网。

要点：TEMPO 通过收缩表示时间离散 Feynman–Vernon 影响泛函的二维张量网，高效模拟非马尔可夫开放量子动力学；标准形式对系统尺寸标度不佳。作者证明：在通常二阶时间步误差内，所有内部网键维可降至 (2m+1)(m+1)，其中 m 为独立耦合通道数，且不依赖耦合算符相异本征值数目；系统尺寸仅进入网络最后边界层，从而使大系统对 TEMPO 可及。该结构在有指导的算法开发中被发现，直接放宽非马尔可夫开放系统数值模拟的尺寸瓶颈。

---

### 8. Spin-Charge Conversion in an Epitaxial Kagome Flat-Band Metal
Wenyi Zhou · Yuqing Zhu · Katherine Johnson · Hari Paudyal 等 · [arXiv:2610.36501](https://arxiv.org/abs/2610.36501) · cond-mat.mtrl-sci · new

**为何相关：** 外延 Kagome 平带金属 CoSn 中测得远超 Pt 的有效自旋霍尔角，并结合 DFT 阐明 Berry 曲率来源——自旋电子学 × Kagome 平带 × 自旋–电荷转换。

要点：Kagome 金属费米能级附近的拓扑平带引发广泛关注，电荷输运各向异性已较清楚，自旋输运则仍少探索。作者以 CoSn 为代表，用 STM 原子分辨与 dI/dV 谱确认平带特征，并在铁磁 Ni 与 c 面 CoSn 薄膜异质结上用磁光技术定量自旋轨道力矩（SOT）。测得 CoSn 层有效自旋霍尔角 θ_SH=0.484±0.005，显著高于对照 Ni/Pt 中 Pt 的 0.0436±0.0003；DFT 阐明本征自旋霍尔效应与动量空间 Berry 曲率来源。工作把平带 Kagome 金属确立为高效自旋–电荷转换与低功耗自旋电子学的候选平台。

---

### 9. Spontaneous topological diode effect induced by non-coplanar antiferromagnetic order
Nguyen Duy Khanh · Hirotaka Takagi · Rina Takagi 等 · [arXiv:2610.37003](https://arxiv.org/abs/2610.37003) · cond-mat.mtrl-sci · new

**为何相关：** 在手性格点非共面反铁磁 CoTa₃S₆ 中观测到零场自发拓扑二极管效应，非互易由反铁磁序参量主导且可无 SOC——反铁磁拓扑 × 非互易输运。

要点：非中心对称体中的二极管式非互易输运多来自相对论 SOC，幅度随外场或铁磁磁化标度；共线反铁磁零场通常缺席。理论预言非共面反铁磁序即便无 SOC、无净磁化、无外场亦可承载大非互易——自发拓扑二极管效应，可用于高效电读出反铁磁畴，但此前缺乏真实材料验证。作者在手性格点非共面反铁磁 CoTa₃S₆ 中观测到该效应：零场下沿 [001] 的非线性电阻率显示非互易，幅度超过典型铁磁体，并由反铁磁序参量而非磁化主导。第一性原理表明非共面反铁磁序在无 SOC 时即可诱导非对称能带色散，确立非相对论起源。工作为反铁磁畴电读出提供新机制，并突出非共面反铁磁作为不依赖 SOC/磁化即可实现类铁磁功能响应的材料平台。

*Zotero：库中无同 ID；有“共线反铁磁诱导的室温自发霍尔”等相邻主题条目（弱相似）。*

---

### 10. Anomalous Structures of Fisher Zero Lines in Biorthogonal Dynamical Quantum Phase Transitions
Wen-Hui Nie · Chong Li · Lin-Cheng Wang · [arXiv:2610.36521](https://arxiv.org/abs/2610.36521) · quant-ph · new

**为何相关：** 双正交框架解释非厄米淬灭 Loschmidt 振幅 Fisher 零线在复时间平面的发散、分离与轴束缚等反常结构——非厄米 × 动力学量子相变。

要点：非厄米淬灭中 Loschmidt 振幅的 Fisher 零线可在复时间平面呈现发散、分离，或整支/某支束缚于实/虚轴等反常结构。作者在双正交框架下揭示其起源：通过预/后淬灭归一化复 Bloch 矢量点积 m_k 给出临界动量条件；当 Fisher 零连续覆盖实时间轴时，进一步引入零点密度以识别临界时间。工作把非厄米动力学量子相变的几何图像落到可计算的动量判据上。

*Zotero：库中无同 ID；有高度主题相近条目《Biorthogonal dynamical quantum phase transitions in non-hermitian systems》(PRL 132, 220402) 等。*

---

### 11. Two Exceptional-Point Regimes in the Spinterface Model of Chirality-Induced Spin Selectivity
Seif Alwan · [arXiv:2610.37072](https://arxiv.org/abs/2610.37072) · cond-mat.mes-hall · new

**为何相关：** 手性诱导自旋选择（CISS）的 spinterface 模型支持两种代数上不可混用的近例外点体制（金电极级 / 分子链级）——例外点 × 自旋选择 × 开放电极。

要点：CISS 的 spinterface 模型存在两种代数上截然不同、不可混用的近例外点（EP）体制。金电极级近 EP：在反厄米、电极介导自旋翻转与自旋对称耗散展宽下，两个金自旋态近简并（方案 B）。分子链级近 EP：在厄米位上 Rashba 自旋翻转与自旋依赖展宽下，权重最大落在第一分子格点的两个分子本征态集体合并（方案 A）。若把一方案的对角相消与另一方案的非对角结构混用，判别式严格为负，不能形成真 EP。结果澄清 CISS 中 EP 讨论的代数前提，避免跨体制混用导致的伪结论。
