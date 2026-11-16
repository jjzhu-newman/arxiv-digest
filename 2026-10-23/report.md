# 10/23 arXiv 兴趣摘要（工作日）


扫了今天（美西 10/23，周五）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Friday, 23 October 2026**；新投稿：cond-mat 77、quant-ph 47、hep-th 44、math-ph 11、cs.LG 117、stat.ML 13（交叉与替换未计入）。已排除 10 月已荐的 172 篇。交错磁/补偿磁侧有铁弹开关反向磁子热霍尔（中间交错磁相响应消失）与氧化物超晶格界面催生的 d 波自旋劈裂，以及对称允许的 piezo-Kerr；非厄米侧有 ROQJ 工程的 PT 对称 Bose–Hubbard 例外点结构与手性态转移，以及量子行走中单缺陷诱导的标度无关局域化；开放/Floquet 有局域退相干维持的连续时间晶体、reset 增强的耗散计量，以及噪声驱动下的离散时间液体；另有双量子自旋霍尔边的玻色边相 DMRG 证实，以及神经张量网络/backflow 在掺杂 Hubbard 上揭示的条纹–超导近简并。按兴趣锚点筛了 **11 篇**（全部为新投稿；未收替换稿；跳过干旱胁迫光谱、声学可制造结构、结构动力学 VQE、气象/多模态成像类 PINN、纯光学/超音速降阶等假阳性）。本地桌面当时未在线，**未做 Zotero 核对**。

**建议先翻这三篇：**
1. **Ferroelastic Reversal Magnon Thermal Hall Effect in a Fully Compensated Ferrimagnet** —— 完全补偿亚铁磁中铁弹开关可反向磁子热霍尔：两正交变体符号相反，中间交错磁相响应为零；并给出单层 V₂SSe 候选——交错磁/补偿磁 × 磁子 Berry × 非易失操控。
2. **Exceptional point structure and chiral state transfer in a rate-operator-engineered $\mathcal{PT}$-symmetric Bose-Hubbard dimer** —— 用速率算符量子跳跃（ROQJ）工程三粒子 Bose–Hubbard 二聚体的非厄米 PT 演化，刻画例外线/四点结构与手性态转移——非厄米/例外点 × 开放系统连续测量。
3. **Quantum Fokker-Planck solvers as trainable generative models** —— 把 Langevin 势参数化，经厄米化 Fokker–Planck + QSVT 余弦算子组合做成可训练量子生成模型，分布族内可凸优化且可扩展——量子 ML × 物理信息归纳偏置。

---

### 1. Ferroelastic Reversal Magnon Thermal Hall Effect in a Fully Compensated Ferrimagnet
Yingxi Bai · Zihan Chen · Chengwang Niu · Ming Yang · [arXiv:2610.30733](https://arxiv.org/abs/2610.30733) · cond-mat.mes-hall · new

**为何相关：** 完全补偿亚铁磁中铁弹开关可反向磁子热霍尔：两正交变体符号相反，中间交错磁相响应为零；并给出单层 V₂SSe 候选——交错磁/补偿磁 × 磁子 Berry × 非易失操控。

要点：零净磁化体系中，磁子热霍尔的可逆、非易失调控仍是难题。作者用最小 Heisenberg–Dzyaloshinskii–Moriya 模型表明，铁弹开关可重定向晶格各向异性，从而重构手性分辨的磁子能带与 Berry 曲率分布。由 [C₂‖C₄z] 关联的两个正交完全补偿亚铁磁变体给出符号相反的磁子热霍尔响应，而中间交错磁相中该响应消失。第一性原理进一步指出单层 V₂SSe 是实现铁弹调控横向磁子输运的候选材料；铁弹开关可同时驱动磁子与电子能带重构，实现磁子热霍尔的非易失反转，并伴随各向异性轨道霍尔与不同的磁光响应。

---

### 2. Exceptional point structure and chiral state transfer in a rate-operator-engineered $\mathcal{PT}$-symmetric Bose-Hubbard dimer
Jaakko Luomala · Federico Settimo · Kimmo Luoma · Iiro Vilja 等 · [arXiv:2610.30836](https://arxiv.org/abs/2610.30836) · quant-ph · new

**为何相关：** 用速率算符量子跳跃（ROQJ）工程三粒子 Bose–Hubbard 二聚体的非厄米 PT 演化，刻画例外线/四点结构与手性态转移——非厄米/例外点 × 开放系统连续测量。

要点：速率算符量子跳跃（ROQJ）把开放系统主方程拆成随机纯态轨迹；对无跳跃分支做后选即得非厄米哈密顿量生成的演化，且可通过不同连续测量方案改写该非厄米动力学。作者将 ROQJ 用于环境非局域退相干下的开放三粒子 Bose–Hubbard 二聚体，构造带一般双参数 PT 对称虚对角项的非厄米哈密顿量，推广熟知的增益–损耗二聚体。文中对不同在位相互作用刻画谱的对称结构：无相互作用时，未破缺 PT 区由不同性质的二阶例外线与四个四阶例外点围成（其中两点不见于常规增益–损耗模型）；并讨论虚部简并区与手性态转移。工作把例外点几何与开放系统连续测量调控直接对接。

---

### 3. Quantum Fokker-Planck solvers as trainable generative models
Tariq Mahassen · Marcin Jastrzebski · Oleksandr Kyriienko · [arXiv:2610.31330](https://arxiv.org/abs/2610.31330) · quant-ph · new

**为何相关：** 把 Langevin 势参数化，经厄米化 Fokker–Planck + QSVT 余弦算子组合做成可训练量子生成模型，分布族内可凸优化且可扩展——量子 ML × 物理信息归纳偏置。

要点：常见做法用分层变分线路与参数化旋转做生成模型；本文改为参数化 Langevin 过程的势。相应 Fokker–Planck 方程经厄米化后，用量子奇异值变换实现的余弦算子线性组合求解；编码稳态密度平方根后，可在计算基测量采样，并由块编码对角势的系数高效控制。作者在 FP 方程描述的分布族内训练以匹配经验分布，并演示多元分布的参数恢复。关键是模型在规模上仍可训练：物理信息归纳偏置使分布内目标可用样本高效的凸优化，且与问题维数无关。文中给出线路构造、主要组件的高效块编码与资源分析。

---

### 4. Emergent altermagnetism in (LaVO$_3$)$_n$/(LaNiO$_3$)$_m$ superlattices from interfacial charge transfer and octahedral tilts
Gustavo H. Cassemiro · Walber H. Brito · [arXiv:2610.30371](https://arxiv.org/abs/2610.30371) · cond-mat.str-el · new

**为何相关：** 氧化物超晶格中界面电荷转移与八面体倾转共同催生 d 波自旋劈裂（无需 SOC）；(1,1) 绝缘超晶格 DFT+U 劈裂可达约 118 meV——界面工程 × 交错磁。

要点：第一性原理计算表明，(LaVO₃)ₙ/(LaNiO₃)ₘ 超晶格在 (n,m)=(1,1)、(2,2)、(2,4) 可由界面电荷转移与八面体倾转共同产生交错磁。电荷转移把体系推向 V⁴⁺/Ni²⁺，使原本顺磁的镍酸盐层变为磁活性子晶格。所得 C 型反铁磁序结合 a⁻b⁺c⁻ 或 a⁻b⁻c⁻ 倾转，使相反自旋子晶格仅通过非对称操作相连，从而在无自旋轨道耦合下给出 d 波自旋劈裂。DFT+U 下，绝缘 (LVO)₁/(LNO)₁ 超晶格的劈裂可达约 118 meV，约为体相 LaVO₃ 计算值的两倍，并随镍酸盐层增厚而减小。

---

### 5. Local Dephasing Sustains Continuous Time Crystals in a Spin-1/2 Ensemble
Zhen-huan Yang · Dan-Bo Zhang · [arXiv:2610.31230](https://arxiv.org/abs/2610.31230) · quant-ph · new

**为何相关：** 全连接铁磁自旋-1/2 系综中，局域纯退相干反而维持连续时间晶体：退相干抬高相互作用能，有限时标能量弛豫转为延迟反馈——耗散 × 连续时间晶体。

要点：局域纯退相干通常抑制单自旋相干，但作者证明：在带局域衰变的全连接铁磁自旋-1/2 系综中，它可维持连续时间晶体序。精确算符恒等式揭示机制——退相干抬高相互作用能，而有限时标上的能量弛豫把这种“充电”转为延迟反馈。齐次平均场下可证明：该模型中退相干对周期运动必不可少，且反馈在每个周期精确平衡横向阻尼。平均场之外，该恒等式固定振荡 Liouvillian 模中能量与纵向磁化的相对振幅与相位；谱与稳态双时关联表明衰减率随系统尺寸代数减小、频率逼近非零平均场值。半经典轨迹还显示在极限环区与两个对称相关定态区之间的反复切换。

---

### 6. Reset-Enhanced Dissipative Quantum Metrology
Silan Li · Qingjun Tong · Ruicheng Bao · [arXiv:2610.31249](https://arxiv.org/abs/2610.31249) · quant-ph · new

**为何相关：** 仅加简单 reset 通道即可作最小耗散控制，统一提升开放探针的稳态与瞬态量子 Fisher 信息，无需改哈密顿量或连续相干驱动——开放系统量子计量。

要点：量子计量精度不仅取决于测量，也取决于制备与维持探针的耗散动力学；此前缺少同时增强稳态与瞬态精度的一般机制。作者表明加入简单 reset 通道即可：reset 作为最小耗散控制，无需修改本征哈密顿量或施加连续相干驱动。文中导出统一的量子 Fisher 信息（QFI）–reset 率响应恒等式，说明 reset 如何增强稳态与瞬态估计，并揭示瞬态上的尖锐区分：对角动力学中的静态参数估计，reset 不改变短时 QFI 的首导项；而对经过时间估计，它可立即产生短时上随 reset 率二次标度的漂移贡献。频率估计的增强则主要由真正的量子本征矢贡献主导。

---

### 7. Discrete time liquids
Zuo Wang · Paul M. Schindler · Marin Bukov · Marios H. Michael · [arXiv:2610.30266](https://arxiv.org/abs/2610.30266) · cond-mat.str-el · new

**为何相关：** 在有限温腔噪声驱动的二维自旋中识别“离散时间液体”：时间孤子破坏长程时间相干，却保留局域倍周期——Floquet/时间晶体之外的时空序。

要点：离散时间晶体以稳健的次谐波振荡自发破缺周期驱动的离散时间平移对称；是否存在其他时间多体序一直受关注。作者识别离散时间液体：由时间孤子导致的短程时间相干所刻画的新型时空序。他们研究耦合到有限温腔的二维自旋系统——腔涨落提供仅有有限时间相干的噪声、近似周期驱动。尽管如此，自旋仍在宽参数区形成具稳健倍周期动力学的亚稳态。与时间晶体不同，该态仅有有限时间相干：单条轨迹在倍周期响应的两个对称相关时间构型间随机切换。这些切换被鉴定为时间孤子——时间序中的拓扑缺陷，保留局域倍周期却破坏长程时间相干，从而产生时间液体。文中并提出可复现该现象的最小模型。

---

### 8. Nature of the bosonic edge phase in a double quantum spin Hall insulator
Andreas Feuerpfeil · Ronny Thomale · Trithep Devakul · Nicolas Regnault 等 · [arXiv:2610.30251](https://arxiv.org/abs/2610.30251) · cond-mat.mes-hall · new

**为何相关：** 用嵌入体态的柱面 segment DMRG 数值证实双量子自旋霍尔绝缘体边可进入仅保留玻色（成对费米）无能隙模的相互作用驱动相——拓扑边态 × 相互作用。

要点：场论分析曾预言双量子自旋霍尔绝缘体（DQSHI）的边可在相互作用驱动下从费米边模相进入仅有玻色模的相：单费米边激发全部打开能隙，但费米子对比保持无能隙，带来可区分的实验指纹。作者数值模拟相互作用 DQSHI 边并证实该玻色边相的存在。由于电荷与 S^z 守恒之间的混合反常，计算需要显式的体嵌入；他们因此在无限二维柱面上做 segment DMRG，把 DQSHI 体建模为两份自旋向上最低朗道能级及其时间反演副本。结果表明相互作用可在 DQSHI 边打开单费米能隙，同时保留成对通道的无能隙特征，与场论图像一致。

---

### 9. Piezo-Kerr effect in altermagnets and noncollinear antiferromagnets
Yuqi Liu · Qiu-Shi Huang · Xinfeng Chen · Yilin Han 等 · [arXiv:2610.30929](https://arxiv.org/abs/2610.30929) · cond-mat.mtrl-sci · new

**为何相关：** 把“表示匹配”从序参量共轭场推广到响应张量：枚举 122 个磁点群，找出 16 个零应变禁戒 Kerr、线性应变可激活的 piezo-Kerr 群（多为交错磁/非共线反铁磁）——对称设计 × 交错磁磁光。

要点：对称通常被视为对物理响应的约束，也可用来设计控制场。作者把用于识别序参量共轭场的表示匹配原则推广到响应张量：当控制场某分量（或组合）与所选响应分量属于同一磁点群不可约表示时，允许线性耦合，从而可做符号开关控制。应用于磁光 Kerr，得到 piezo-Kerr 效应——特定应变组合可激活无应变时被禁戒的 Kerr 响应。枚举全部 122 个磁点群后，识别出 16 个群：无应变 Kerr 禁戒，但线性应变诱导贡献允许；这些群由净磁化被对称强制为零的交错磁与非共线反铁磁实现。活性应变通道与一阶符号反转直接由对称给出；并对体相 MnTe₂、CoF₂ 等做了第一性原理计算。

---

### 10. Scale-free localization in pseudo-Hermitian quantum walk
Haiting Zhang · Lei Xiao · Cui-Xian Guo · Quan Lin 等 · [arXiv:2610.31067](https://arxiv.org/abs/2610.31067) · quant-ph · new

**为何相关：** 一维量子行走中单个非厄米缺陷即可诱导标度无关局域化，并与赝厄米相变/束缚态涌现联动；二维同样成立——非厄米缺陷物理 × 新型局域态。

要点：标度无关局域化是非厄米系统的特有现象：所谓标度无关局域态的局域长度随系统尺寸线性标度。作者表明，一维量子行走中单个非厄米缺陷即可诱导该现象。在非厄米性驱动下，系统经历赝厄米相变，赝厄米对称破缺伴随标度无关局域化出现；进一步增强非厄米性触发第二次相变，出现两对束缚态。关键是可用局域化性质定位两次转变的临界点。工作还推广到二维量子行走：单个非厄米缺陷同样诱导标度无关局域化，显示该现象的普适性，为非厄米缺陷物理与新型局域态提供视角。

---

### 11. Extreme competition between stripes and superconductivity in the hole-doped Hubbard model
Ao Chen · Johnnie Gray · Si-Jing Du · Garnet Kin-Lic Chan · [arXiv:2610.30321](https://arxiv.org/abs/2610.30321) · cond-mat.str-el · new

**为何相关：** 神经张量网络与神经 backflow 变分把掺杂 Hubbard 推到 1024 格点级精度，揭示 1/8 掺杂附近均匀 d 波、超导条纹与非超导条纹近简并——NNQS × 强关联超导。

要点：二维 Hubbard 模型曾被当作铜氧化物均匀 d 波超导的最小模型，但在相关参数与现实掺杂下，近期计算常得到其他基态，且不同方法的固有偏差使结论仍不确定。作者以大规模 GPU 支撑的神经张量网络与神经 backflow 态模拟，在最多 1024 格点上达到空前变分精度。在纯 Hubbard 以及与空穴掺杂铜氧化物相关的次近邻跃迁下，1/8 掺杂处揭示低能均匀 d 波态、超导条纹与非超导条纹态之间的近简并。结果强调条纹与超导的极端竞争，并为神经网络量子态在强关联格点模型中的高精度应用提供范例。
