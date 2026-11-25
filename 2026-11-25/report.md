# 11/25 arXiv 兴趣摘要（工作日）

扫了今天（美西 11/25，周三）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Wednesday, 25 November 2026**：这是常规周三批次，覆盖约周二 14:00 至周三 14:00 ET 的投稿窗口。新投稿：cond-mat 109、quant-ph 66、hep-th 45、math-ph 11、cs.LG 144、stat.ML 9（交叉与替换未计入）。已排除此前已荐的 511 篇。主题上交错磁 $\alpha$-MnTe 的第一性原理自旋哈密顿量、非线性边界下非厄米趋肤效应延展模的恢复、神经网络量子态的隐式增强虚时演化、PT 对称腔光力学磁强计、可覆盖玻色相变的参数化网络波函数、用自由费米子代理做量子机器学习基准、平衡态手性量子团簇、周期驱动在 Ising 量子临界点的动态标度、驱动开放系统的转移张量、自旋轨道耦合磁体中的 $d$ 波纠缠，以及 NV 探测 Kitaev 自旋液体、开放系统多激发束缚态等较集中。按兴趣锚点筛了 **12 篇**（11 篇新投稿、1 篇交叉投稿；未收替换稿；跳过假阳性或弱相关如 Navier–Stokes 的工程 PINN、知识追踪、乳房数据上的量子核、钓鱼/DNA 等应用杂交量子网络、弹性介质中的奇异点带隙、高分子共价焊接等；近邻但未再拉长名单的还有自旋轨道耦合超导薄膜中 Néel 壁的磁电响应、金刚石链中退相位协助的 Aharonov–Bohm 笼释放、自旋空间群分类、朗道能级中的拓扑安德森超导体，以及补偿亚铁磁中自旋群与磁群对非线性光电流的不同选择定则等）。本日用户机 Zotero 离线，仅对缓存的 arXiv ID 列表（187）做只读核对：**短名单无同 ID**；主题近邻未逐条标注。

**建议先翻这三篇：**
1. **Spin Hamiltonian, magnetic anisotropy and excitation spectrum in altermagnetic $\alpha$-MnTe from first principles** —— 从第一性原理给出六角交错磁 $\alpha$-MnTe 的完整低能自旋哈密顿量，解释易面各向异性、$\Gamma$ 点磁振子能隙与异常巨磁致伸缩，并把第十近邻交换的交错磁劈裂与中子散射对齐——交错磁材料微观理论。
2. **Recovery of Extended Modes from the Non-Hermitian Skin Effect Due to Local Nonlinearity on a Boundary** —— 指出边界上单键非线性即可从非厄米趋肤效应中恢复延展模，并给出可在光子平台上观测的最小模型——非厄米拓扑 $\times$ 非线性。
3. **Augmented Imaginary-Time Evolution of Neural Quantum States with Implicit Time Steps** —— 把增强虚时演化与隐式欧拉/Galerkin 投影结合，得到可用于神经网络量子态的隐式随机重构方案，并在有限步下保持近二次收敛——神经网络波函数方法。

---

### 1. Spin Hamiltonian, magnetic anisotropy and excitation spectrum in altermagnetic $\alpha$-MnTe from first principles
Matteo Costa · Dario Fiore Mosca · Cesare Franchini · Leonid V. Pourovskii · [arXiv:2611.31548](https://arxiv.org/abs/2611.31548) · cond-mat.str-el · new

**为何相关：** 从第一性原理给出六角交错磁 $\alpha$-MnTe 的完整低能自旋哈密顿量，解释易面各向异性、$\Gamma$ 点磁振子能隙与异常巨磁致伸缩，并把第十近邻交换的交错磁劈裂与中子散射对齐——交错磁材料微观理论。

要点：DFT+DMFT 结合力定理得到完整各向异性交换、单离子项与经典偶极耦合。各向同性交换（含第十近邻的交错磁劈裂）与非弹性中子散射一致。易面各向异性与 $\Gamma$ 点磁振子能隙由经典偶极–偶极相互作用主导，使区心劈裂增大约三倍并与实验定量符合；Dzyaloshinskii-Moriya 项虽不小但并不关键。同一哈密顿量再现反节点方向的手性磁振子劈裂（对应电子自旋劈裂），并由超交换的体积依赖定量解释巨磁体积耦合。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 2. Recovery of Extended Modes from the Non-Hermitian Skin Effect Due to Local Nonlinearity on a Boundary
Kazuki Sone · Tomonari Mizoguchi · Yasuhiro Hatsugai · [arXiv:2611.32783](https://arxiv.org/abs/2611.32783) · cond-mat.mes-hall · new

**为何相关：** 指出边界上单键非线性即可从非厄米趋肤效应中恢复延展模，并给出可在光子平台上观测的最小模型——非厄米拓扑 $\times$ 非线性。

要点：连续谱中的趋肤局域通常被归为体带非平凡拓扑，但非线性下的稳健性仍未澄清。一维紧束缚最小模型仅在边界跃迁上引入非线性相位，即可恢复延展模。作者还提出光子学装置，把非线性诱导的延展模作为稳态来动态观测。这表明趋肤效应对非线性边界条件敏感，并不单纯由体拓扑决定。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 3. Augmented Imaginary-Time Evolution of Neural Quantum States with Implicit Time Steps
Maksymilian Kliczkowski · Thomas D. Kühne · Fedor Šimkovic IV · Prachi Sharma · Carlos L. Benavides-Riveros · Werner Dobrautz · [arXiv:2611.32236](https://arxiv.org/abs/2611.32236) · quant-ph · new

**为何相关：** 把增强虚时演化与隐式欧拉/Galerkin 投影结合，得到可用于神经网络量子态的隐式随机重构方案，并在有限步下保持近二次收敛——神经网络波函数方法。

要点：常规虚时演化多为渐近收敛，且显式积分在 NQS 流形上步长受限。增强虚时演化原则上可在有限虚时到达基态；本文先用隐式欧拉加 Galerkin 投影推出可取大步长的隐式随机重构，再给出隐式 AITE。变分投影与有限步积分下加速仍然成立，能量误差渐近二次收敛；有限采样时隐式方案持续优于常规方法。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 4. Magnetometry and slow light in PT-symmetric cavity optomechanics
Yuguo Su 等 · [arXiv:2611.32215](https://arxiv.org/abs/2611.32215) · physics.optics · cross

**为何相关：** 在 PT 对称腔光力学中研究二阶级边与快慢光，并提出基于级边的磁强计，理论灵敏度达皮特斯拉量级——非厄米/PT 对称 $\times$ 量子传感。

要点：PT 对称结构、外磁场与光子隧穿可灵活调控二阶级边效率，以及慢光/快光的展宽与切换。工作在 PT 对称保护相时，基于二阶级边的磁强计理论灵敏度优于以往光力学方案，为磁场传感与光传输控制提供新思路。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 5. Parametric neural-network wavefunctions across a bosonic phase transition
Daniil S. Antonenko · Liang Fu · Leonid I. Glazman · [arXiv:2611.33150](https://arxiv.org/abs/2611.33150) · cond-mat.quant-gas · new

**为何相关：** 提出面向玻色统计的注意力网络波函数 Boseformer，一次训练即可作为覆盖超流–晶体量子相变的参数化基础模型——神经网络波函数。

要点：模型按哈密顿量参数生成波函数，经变分蒙特卡罗优化后无需对每个参数点重新训练。在二维 $1/r^3$ 排斥玻色子上演示，可同时描述超流与晶体相及其之间的量子相变。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 6. A fermionic framework for quantum machine learning benchmarks
Jérémie Gince · Ayana Sarkar · Stefanos Kourtis · [arXiv:2611.31458](https://arxiv.org/abs/2611.31458) · cond-mat.str-el · new

**为何相关：** 用可经典高效模拟的自由费米子线路，构造与量子机器学习模型同架构的费米子代理，用以在同等前提下判别所谓量子优势是否来自经典不可及资源——量子机器学习基准。

要点：FermiML 框架可覆盖核方法与神经网络，用于分类与回归，并可扩展到真实数据。费米子代理复用（参数化）比特转动与纠缠门，从而在相同归纳偏置下作为 QML 模型的可模拟对照。作者在五个分类数据集的 31 组配置上，把量子 kitchen sinks、IQP 与通用参数化线路与相近的费米子对照进行同等比较。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 7. Ground-State Chiral Quantum Clusters
Matteo Massaro · Adolfo del Campo · [arXiv:2611.31370](https://arxiv.org/abs/2611.31370) · quant-ph · new

**为何相关：** 提出平衡态下带持久电流的自束缚基态“手性量子团簇”，并在环上吸引 anyonic Lieb-Liniger 模型中给出精确实现——时间晶体的平衡对照。

要点：非平衡时间晶体已由周期驱动实现，平衡版本仍难寻。最小场论之外，微观精确实现中基态密度–密度关联呈 Talbot 效应：孤子样轮廓周期弥散并复活，同时沿环持续漂移，实现平衡态下的持久运动。并讨论可能的实验探测。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 8. Dynamic scaling behaviors induced by periodic drivings at continuous Ising quantum transitions
Andrea Pelissetto · Davide Rossini · Ettore Vicari · [arXiv:2611.32301](https://arxiv.org/abs/2611.32301) · cond-mat.stat-mech · new

**为何相关：** 在连续量子相变附近建立周期驱动的动态标度理论，并区分破缺与保持 $\mathbb{Z}_2$ 对称的协议——Floquet / 周期驱动 $\times$ 量子临界。

要点：以纵向周期场下的量子 Ising 链，以及周期化学势下的 Kitaev 链（等价于横向周期场 Ising）为范例。重整化群给出驱动振幅与周期的标度变量，并对有限系统与热力学极限分别成立。两类驱动由相应扰动的 RG 维度决定不同幂律；数值验证了光滑单频与方波等协议。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 9. Transfer tensor description of driven inhomogeneous quantum systems
Ferdos Fessahaye · Rajesh Dutta · Michelle Anderson · Chern Chuang · [arXiv:2611.32189](https://arxiv.org/abs/2611.32189) · quant-ph · new

**为何相关：** 把转移张量方法推广到时间非齐次与周期驱动的开放系统，用以分析驱动下的记忆核与动力学局域——开放系统 $\times$ 周期驱动。

要点：标准转移张量方法依赖动力学映射的时间平移不变性，驱动会破坏它。引入双时间层次后，对周期 $t_0$ 做亚频闪采样即可恢复块平移不变性。应用到旋转波近似之外的非均匀展宽二能级系综，以及 Dunlap–Kenkre 条件下的驱动紧束缚链：干净链在频闪下冻结，亚频闪张量显示动力学局域由与周期匹配的延迟再聚焦执行，中等无序会打破再聚焦并扩大有限扩散范围。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 10. Entanglement between distant spins in a polarized magnet forms a $d$-wave clover
Alan Zhang · Ye Zhou · [arXiv:2611.32190](https://arxiv.org/abs/2611.32190) · quant-ph · new

**为何相关：** 自旋轨道耦合使极化磁体成为虚自旋翻转对的源，从而使远处自旋纠缠呈 $d$ 波三叶草图案——自旋轨道 $\times$ 量子关联。

要点：对自旋 $1/2$ 方格子铁磁体，在领头阶证明 $d$ 波反平方律（振幅为自旋波的 $1.376$ 倍）、三叶草状纠缠区、无需 Dzyaloshinskii-Moriya 项即精确成立，且每个自旋的纠缠完全是成对的。四个量子比特即可在现有误差水平下检验 $d$ 波符号。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 11. Signatures of Kitaev quantum spin liquid states in $\alpha$-RuCl$_3$ revealed by nitrogen-vacancy spin-noise spectroscopy
Jitender Kumar 等 · [arXiv:2611.33085](https://arxiv.org/abs/2611.33085) · cond-mat.str-el · new

**为何相关：** 用金刚石 NV 自旋噪声谱在纳米尺度非侵入探测 $\alpha$-RuCl$_3$ 中的 Kitaev 量子自旋液体迹象——量子传感 $\times$ 量子自旋液体。

要点：在厚度 $8$–$150$ nm 的纳米片上、于 $4.3$–$250$ K 测量。约 $100$ K 以下近邻 NV 的 $T_1$ 明显下降，对应 GHz 磁涨落增强，该温标与 Kitaev 相互作用能标（约 $8$ meV）及低能分数激发的出现一致。$50$ K 以下，较厚（$>90$ nm）样品的弛豫呈不同的双指数行为。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 12. Exact approach to double- and triple-excitation bound state in open quantum systems
X. S. Sun · H. T. Cui · Y. A. Yan · H. Z. Shen · [arXiv:2611.31779](https://arxiv.org/abs/2611.31779) · quant-ph · new

**为何相关：** 给出开放量子系统中双/三激发束缚态的精确封闭方程，并确定其出现条件及与单激发束缚态的关系——开放量子系统。

要点：导出相互作用量子发射体耦合环境时双/三激发动力学的封闭方程，由此识别多激发束缚态出现的临界条件及其与单激发束缚态的关系。这表明这类束缚态在开放发射体系统中具有普遍性，并指出可经多激发束缚态介导发射体之间的相互作用。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*
