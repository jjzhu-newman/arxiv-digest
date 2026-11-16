# 10/9 arXiv 兴趣摘要（工作日）

扫了今天（美西 10/9，周五）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。新投稿量：cond-mat 99、quant-ph 74、hep-th 40、math-ph 6（cs.LG 178、stat.ML 30 只看物理/量子相关；交叉与替换未计入）。今天交错磁特别扎堆：光诱导奇/混合宇称磁序、光子拖曳读畴、CrSb Josephson 长程超流、赤铁矿亚皮秒磁振子脉冲，以及 CuF₂“名义交错磁”的反例澄清；开放系统一侧有耗散构造大 DFS 与非马尔可夫态扩散的确定性数值法，另有 Gen-PINNs 与缓解贫瘠高原的 Q-Capsule。按兴趣锚点筛了 **12 篇**（全部为新投稿，未收替换稿）。核对了本地 Zotero 库（只读副本），12 篇都不在库里；交错磁/CrSb、DFS、PINN、NV 磁强计方向库里已有不少相关文献，相应条目里有标注。

**建议先翻这三篇：**
1. **Photoinduced Odd- and Mixed-Parity Magnetism in Collinear Antiferromagnets** —— 用圆/椭圆偏振光与 Floquet 第一性原理在共线反铁磁中诱导奇宇称与混合宇称自旋劈裂，并伴随反常霍尔——Floquet × altermagnetism 延伸。
2. **Constructing Large and Structured Decoherence-Free Subspaces in Hybrid Quantum Systems** —— 耗散玻色模对量子物质施加全局约束，在长时间极限选出 null 态，构造带涌现对称的大退相干自由子空间——开放系统 / Liouvillian × 多体。
3. **Reading Altermagnetic Domains with Photon Drag** —— 光子拖曳二阶光电流的角依赖可同时读出交错磁对称类型与 Néel 畴——altermagnetism 畴读出方案。

---

### 1. Photoinduced Odd- and Mixed-Parity Magnetism in Collinear Antiferromagnets
Jin-Yang Li, Ruo-Yu Ning, Ying Zhang, Qiu-Qiu Li 等 · [2610.11807](https://arxiv.org/abs/2610.11807) · cond-mat.mtrl-sci · new

**为何相关：** 用圆/椭圆偏振光与 Floquet 第一性原理在共线反铁磁中诱导奇宇称与混合宇称自旋劈裂，并伴随反常霍尔——Floquet × altermagnetism 延伸。

要点：交错磁以实空间补偿共线磁矩与偶宇称动量依赖自旋劈裂著称，但在完全补偿共线磁体中实现奇宇称/混合宇称磁序仍难。作者以单层 CoS、CoSe 为代表，结合 Floquet 理论与第一性原理计算表明：圆偏振光可诱导奇宇称 f 波自旋劈裂，椭圆偏振光诱导奇宇称 p 波劈裂；单轴应变叠加圆偏振亦可通向 p 波态。电场与圆/椭圆偏振联用则把劈裂变成混合宇称形式。光诱导破坏 PT 对称，再叠加自旋–轨道耦合可给出有限反常霍尔响应。工作把光场调控定位为在补偿反铁磁中工程化奇/混合宇称自旋劈裂、通向光控电子与磁现象的通用策略。库里已有“Odd-parity magnetism driven by antiferromagnetic exchange”等，这篇强调光驱动 Floquet 路径。

---

### 2. Constructing Large and Structured Decoherence-Free Subspaces in Hybrid Quantum Systems
Catalin-Mihai Halati, Tony Jin, Roderich Moessner · [2610.12348](https://arxiv.org/abs/2610.12348) · cond-mat.quant-gas · new

**为何相关：** 耗散玻色模对量子物质施加全局约束，在长时间极限选出 null 态，构造带涌现对称的大退相干自由子空间——开放系统 / Liouvillian × 多体。

要点：作者给出在混合量子系统中构造大且有结构的退相干自由子空间（DFS）的框架：量子物质耦合到耗散玻色模，耗散在长时间极限选出物质 null 态，从而施加全局约束。这些 DFS 可呈现完整 Liouvillian 动力学所没有的异量子性质与涌现对称。借助李代数表示论系统构造带有物理兴趣 null 态的多体算符，并按代数结构选型。显式例子是有损耗光学腔耦合一维粒子的定向隧穿算符：DFS 对称来自 sl(2,C)，给出指数多稳态；对费米与玻色粒子用解析与数值刻画 null 态，其中一类呈现源自无自旋 η 配对代数的强对称。时依矩阵积态模拟显示，长时态的非平凡性质可从一般初态的耗散动力学中涌现。框架为耗散工程复杂量子关联与可控利用非互易打开路径。你库里有若干经典 DFS 计算条目，这篇是多体混合系统方向的当代延伸。

---

### 3. Reading Altermagnetic Domains with Photon Drag
Sayed Ali Akbar Ghorashi, Andrew M. Rappe · [2610.10970](https://arxiv.org/abs/2610.10970) · cond-mat.mes-hall · new

**为何相关：** 光子拖曳二阶光电流的角依赖可同时读出交错磁对称类型与 Néel 畴——altermagnetism 畴读出方案。

要点：有限光子动量使中心对称空间群中也可出现二阶光电流（常规体光伏效应被禁）。作者研究交错磁的光子拖曳响应，表明其角依赖同时揭示磁序对称与样品 Néel 畴：当晶体旋转互换两畴时，畴偶与畴奇电流落在不同角谐波上（四方 d 波交错磁分别为 4n 与 4n+2），单畴上两次相差 90° 的测量即可分离畴奇电流。微观贡献的畴宇称还依赖偏振：线偏振下仅 shift 项畴奇，圆偏振下畴奇通道切换到 injection、费米面与接触主值项。镜像对称固定各谐波角相位，并区分 d_{x²−y²}、d_{xy} 与 g 波序。常规共线反铁磁无畴奇光子拖曳电流。由此给出一种光学、非破坏读出交错磁畴与对称的方案。

---

### 4. Strain-engineered long-distance supercurrent in an altermagnetic CrSb based-Josephson junction
Yifan Gao, Jin Yan, Junjie Wei, Yifan Zhang 等 · [2610.11341](https://arxiv.org/abs/2610.11341) · cond-mat.supr-con · new

**为何相关：** 应变外延 CrSb 交错磁 Josephson 结中观测到跨越 150 nm 的无耗散超流，远超常规自旋单态相干长度——altermagnetism × 超导自旋电子学。

要点：交错磁零净磁化与动量依赖自旋劈裂的组合，有望在无宏观杂散场下实现非常规超导态。作者在应变交错磁 CrSb 外延薄膜上构筑横向 Josephson 结，观测到跨越 150 nm 间隔的无耗散超流，比常规自旋单态相干长度大约两个数量级，并伴随清晰的磁场诱导量子干涉图样，直接证据表明真实 Josephson 耦合。结果把交错磁定位为无需宏观磁杂散场即可产生长程超流的平台，对超导自旋电子学有应用意义。你库里有多篇 CrSb 交错磁条目（含外延薄膜能带劈裂等），这篇补上超导结输运实验。

---

### 5. Demonstration of ultrafast coherent sub-picosecond magnon pulses
Peter Kubaščík, Miina Leiviskä, Martin Bušina, Zdenek Kašpar 等 · [2610.11550](https://arxiv.org/abs/2610.11550) · cond-mat.mtrl-sci · new

**为何相关：** 在交错磁绝缘体 α-Fe₂O₃（赤铁矿）中用太赫兹自旋–轨道力矩发射 0.4 ps 相干磁振子脉冲并观测弹道非色散传播——altermagnetism × 超快磁振子学。

要点：超快磁振子学追求用太赫兹磁振子脉冲替代电子做信息处理，关键是高速、长程传播同时保持窄波形。作者利用相邻铂层的宽带太赫兹自旋–轨道力矩，在交错磁绝缘体 α-Fe₂O₃（赤铁矿）中发射 0.4 皮秒磁振子脉冲；相位分辨太赫兹透射显示这些亚皮秒脉冲以恒定速度 23 nm/ps 弹道、相干、非色散传播，在约 160 nm 距离上输运角动量并保持时间波形，推断弛豫长度达数百纳米或更长。工作不仅把赤铁矿确立为超快磁振子学优良平台，也给出一种台式高分辨方法，可直接提取高波矢色散并探索交错磁等材料中的太赫兹磁振子动力学。库里有“Terahertz spin current dynamics in antiferromagnetic hematite”等可对照。

---

### 6. Magnon band splitting without altermagnetism in CuF2
Ioannis Rousochatzakis, Oleg Janson, Alexander A. Tsirlin · [2610.11838](https://arxiv.org/abs/2610.11838) · cond-mat.str-el · new

**为何相关：** 对“预测交错磁”CuF₂ 的计算+实验表明：实际单斜结构与层间超交换压掉交错磁带劈裂，DM 引起的磁振子劈裂亦非手性——强调不能只靠对称性判据。

要点：确证交错磁态不能只靠对称性论证。作者对列入预测交错磁名单的类金红石 CuF₂ 做第一性原理、线性自旋波与磁化测量：实验单斜结构可用弱耦合方格子层的自旋-1/2 模型描述（面内 J₁≈115 K，两协同反铁磁层间耦合分别为 J₁ 的 4% 与 8%）。长程超交换驱动的斜向层间耦合使磁有序态原胞加倍，从而有效压制交错磁带劈裂；同时存在很强的 Dzyaloshinskii–Moriya 相互作用（|D|/J₁≈0.3），导致自旋倾角，并与 order-by-disorder 一起把 Néel 矢量钉在晶轴 b；DM 各向异性可促进磁振子带劈裂，但能带保持非手性。结论强调即使在具有交错磁对称的 3d 磁体中，相对论效应与真实结构细节仍至关重要。

---

### 7. Magnonic cavity-enhanced quantum magnetometry with nitrogen-vacancy centre ensembles
Nikhil Kumar · [2610.11350](https://arxiv.org/abs/2610.11350) · cond-mat.mes-hall · new

**为何相关：** 用 YIG/CoFeB 磁振子晶体缺陷腔增强 NV 系综磁强计，Lindblad/Tavis–Cummings 描述混合耦合——量子传感 × 磁振子学。

要点：NV 系综是领先的室温磁强计，但灵敏度通常来自单共振线，并依赖外部微波与偏置场硬件。作者提出以一维 YIG/CoFeB 磁振子晶体为核心的芯片级方案：单个结构缺陷形成被动磁振子腔，集成永磁提供偏置。微磁学模拟给出磁振子带隙（2.5–3.0 GHz）内、距 NV 零场劈裂约 40 MHz 的缺陷局域自旋波模（2.910 GHz），带结构与独立平面波计算一致。Tavis–Cummings/Lindblad 模型中微波经该模到达 NV 系综，预言仅在模线宽内才有强的超精细分辨光探测磁共振谱。工作把“磁振子腔 + NV”定位为少依赖外部微波硬件的片上量子磁强计路线。库里有 NV 系综与非厄米 NV 拓扑等条目可对照。

---

### 8. Gen-PINNs: Generative Adversarial Physics Informed Neural Networks for solving partial differential equations
Muhammad M. Akmal, Kamy Sepehrnoori, Michael J. Pyrcz · [2610.10897](https://arxiv.org/abs/2610.10897) · cs.LG · new

**为何相关：** 针对标准 PINN 的谱偏置、损失失衡与优化停滞，提出残差–对抗统一的 Gen-PINNs 确定性框架——PINN / SciML。

要点：PINN 是无数据求解 PDE 的常用机器学习方法；GAN 在复杂数据驱动问题上表现强，但在确定性物理信息 PDE 求解中应用仍有限。作者先梳理标准 PINN 局限（谱偏置、损失失衡、优化停滞），再提出 Generative Adversarial Physics-Informed Neural Networks（Gen-PINNs）：统一的确定性残差–对抗框架，用对抗学习改善残差满足与解的质量。在若干基准 PDE 上相对标准 PINN 显示精度与稳定性改进。对你关心的物理信息神经求解器是直接可跟的方法论文。库里已有 PINN 综述与多种变体（约二十余篇 Physics-informed neural…）。

---

### 9. Q-Capsule: A Localized Capsule-Based Quantum Neural Architecture for Barren Plateau Mitigation
Awal Ahmed Fime, Tasfia Zaman Samiha, Saika Zaman, Dimitris Pados 等 · [2610.11261](https://arxiv.org/abs/2610.11261) · quant-ph · new

**为何相关：** 用寄存器分区、局域读出与稀疏囊间耦合的量子胶囊网络缓解贫瘠高原，并以 QFIM 引导自适应加深——QML 可训练性。

要点：变分量子算法常受贫瘠高原困扰：线路规模与深度增大时梯度消失，量子神经网络难训。作者提出 Q-Capsule：局域胶囊式量子神经架构，通过寄存器分区、局域读出、稀疏囊间耦合、可训练数据重上传，以及量子 Fisher 信息矩阵（QFIM）引导的自适应深度增长来缓解该问题。把每个可观测量的主要支撑限制在小胶囊内并控制囊间纠缠，既保留有用梯度信号，又维持局域量子表示之间的通信。随寄存器规模增大，数值显示梯度范数衰减显著慢于全局纠缠的对照线路。工作把“局域化胶囊 + 信息几何深度调度”作为缓解贫瘠高原的一条架构路径。

---

### 10. Symmetric Mode Ansatz: Theory of Magnon Collective Modes in Chern Insulators
Miguel Gonçalves, Jonah Herzog-Arbeitman, Juan Felipe Mendez-Valderrama, Andreas Feuerpfeil 等 · [2610.10706](https://arxiv.org/abs/2610.10706) · cond-mat.str-el · new

**为何相关：** 提出对称模 ansatz（SyMA）描述莫尔 Chern 绝缘体中的低能磁振子谱与能隙起源——拓扑 × 磁振子集体模。

要点：莫尔材料中由平带铁磁自发破缺时间反演可宿主整数与分数量子 Chern 绝缘体。扭角 MoTe₂ 中异于量子霍尔之处在于相反自旋携带相反陈数，实现带有能隙磁振子激发的 Ising 铁磁；澄清这些集体模的本质与磁振子能隙起源，对理解 Chern 磁体稳定性至关重要。作者发展广义单模近似——对称模 ansatz（SyMA）——描述低能磁振子谱，在整数填充与数值计算高度一致，并用于分析能隙来源与相互作用投影细节。工作把 SyMA 确立为研究莫尔 Chern 磁体中磁振子集体模的解析工具。

---

### 11. A deterministic polynomial chaos Galerkin method for non-Markovian quantum state diffusion
Quanhui Zhu, Zhenning Cai · [2610.12070](https://arxiv.org/abs/2610.12070) · quant-ph · new

**为何相关：** 用浴关联低秩分解 + 多项式混沌 Galerkin，把非马尔可夫量子态扩散变成单次确定性求解，成本约等于一条随机层级轨迹——开放系统数值方法。

要点：非马尔可夫量子态扩散的通用数值方法长期是开放系统模拟难点。作者提出确定性多项式混沌 Galerkin 方案：对浴关联做低秩分解，再投影到多项式混沌基，得到与标准 PDE 求解器兼容的确定性表述。约化密度矩阵由单次确定性求解得到，成本与计算一条随机层级轨迹相当；相对 N_traj 条轨迹可约降 N_traj 倍成本并消除统计采样误差。基准显示在更低成本下误差更小；非二次势、衍射干涉与耦合三维动力学等应用展示处理难题的能力。可与你关心的 TEMPO/HEOM 等开放系统数值路线对照。

---

### 12. Engineering Quantum Interactions: From Effective Models to Validated Physical Predictions
Sinara S. Dourado, Ciro Micheletti Diniz, Gabriel P. L. M. Fernandes, Rogério J. de Assis 等 · [2610.10763](https://arxiv.org/abs/2610.10763) · quant-ph · new

**为何相关：** 统一投影、Schrieffer–Wolff、Magnus、绝热消除与 Floquet 等工具，约束有效模型的构造与验证边界——Floquet / 开放有效理论方法论。

要点：有效模型通过只保留与给定物理问题相关的态、过程与时间尺度使复杂量子动力学可处理，但其预测力取决于保留流形、初态、可观测量、微运动、耗散通道与被消除自由度是否一致处理。作者用投影方法、Schrieffer–Wolff 变换、Magnus 展开、绝热消除、小旋转、时间粗粒化与 Floquet 理论，建立构造并验证有效描述的统一框架；以量子 Rabi 模型及其色散极限为反复基准，识别控制参数、失效诊断与可验证物理预测。文章偏方法/教育向，但对做 Floquet 与开放有效模型的人是有用的“核对清单”。
