# 11/16 arXiv 兴趣摘要（工作日）

扫了今天（美西 11/16，周一）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Monday, 16 November 2026**：这是周末之后的常规周一批次，覆盖约周四 14:00 至周一 14:00 ET 的投稿窗口。新投稿：cond-mat 80、quant-ph 65、hep-th 24、math-ph 16、cs.LG 78、stat.ML 13（交叉与替换未计入）。已排除此前已荐的 414 篇。主题上交错磁 FeF$_2$ 中手性磁振子的畴调控与各向异性反转、量子几何所允许的窄带交错磁、非厄米复共振与光学留数（含例外点附近）、正则化神经网络波函数处理含 DM 相互作用的海森堡磁体、从哈密顿量直接生成张量网络波函数的基础模型、耗散作为高自旋媒介纯化与纠缠资源、耗散诱导的可积性、量子储备计算中的数据重上传、量子极限学习用于参数估计、驱动耗散系统中非平衡 Gibbs 态的快进协议、手性拓扑态的多项式键维 PEPS，以及开放系统极限环的 Liouvillian 轨道 $U(1)$ 结构较集中。按兴趣锚点筛了 **12 篇**（全部为新投稿；未收交叉或替换稿；跳过假阳性或弱相关如复 Schrödinger 桥的图像扩散、联邦/工程 PINN 与热场预测、EuCd$_2$As$_2$ 的压力 DFT 综评、界面粗糙度调控畴壁手性迁移率等；近邻但未再拉长名单的还有近邻化平面锗中高达 $C=4$ 的手性拓扑相、扭角 MoTe$_2$ 广义 Wigner 晶体的变分蒙特卡洛、无穷 MPS 的转移矩阵算法，以及变分线路可训练性/Krotov 优化等）。本日用户机 Zotero（DESKTOP-00O6NSD）离线，仅对缓存的 arXiv ID 列表（187，约 10/30）做只读核对：**短名单无同 ID**；主题近邻未逐条标注。

**建议先翻这三篇：**
1. **Controlled Magnon Chirality and Its Reversal by Anisotropy in Altermagnetic FeF$_2$** —— 在 FeF$_2$ 单晶中用场冷控制磁畴，并以半极化非弹性中子散射直接看到交错磁手性磁振子劈裂；在交换劈裂消失处，横向单离子各向异性把手性反转——交错磁 × 手性磁振子 × 实验。
2. **Narrow-Band Magnetism Allowed by Quantum Geometry: Altermagnetism and Beyond** —— 色散相同的窄带里，只有强量子几何才会从在位相互作用中投影出长程通道，从而稳定共线交错磁（弱几何则只出常规铁磁）——交错磁 × 量子几何 × 窄带关联。
3. **Quantum computational spectroscopy of complex resonances and optical residues** —— 用量子线路同时重建非厄米复共振极点与双正交光学留数，并分析例外点附近的灵敏度，在 IBM 硬件上演示耗散等离激元–分子光谱——非厄米本征结构 × 例外点 × 开放系统光谱。

---

### 1. Controlled Magnon Chirality and Its Reversal by Anisotropy in Altermagnetic FeF$_2$
E. M. Smith · V. O. Garlea · D. Lederman · J. M. Tranquada · I. A. Zaliznyak · J. Sears · [arXiv:2611.18182](https://arxiv.org/abs/2611.18182) · cond-mat.str-el · new

**为何相关：** 在交错磁 FeF$_2$ 中实现磁畴调控，并用中子散射直接分辨手性磁振子带的劈裂；在交换劈裂本应消失处，相对论性单离子各向异性使手性反转——交错磁 × 手性磁振子 × 畴控制。

要点：交错磁补偿子格子的交换对称允许自旋极化电子带与手性劈裂的磁振子带，而这些效应在时间反演相关的磁畴中符号相反，因此畴调控对观测与应用都关键。作者用半极化中子衍射表明，可通过场冷在 FeF$_2$ 单晶中制造磁畴不平衡，并与该材料已知的压磁效应相联系。半极化非弹性中子散射直接给出手性磁振子带的交错磁劈裂。出人意料的是，在 $\mathbf{Q}=(0.5,0.5,1)$ 附近——交错磁交换劈裂消失、非相对论交换模型预期没有手性——他们观测到明确的手性反转，可用单离子各向异性张量的横向分量解释：该分量在由晶体 $4_2$ 螺旋对称联系的 Fe 子格子之间转动。结果细化了 FeF$_2$ 的自旋哈密顿量，也表明对称性约束的相对论性各向异性可以重塑交错磁自旋动力学，并为畴与净手性响应的调控提供了途径。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 2. Narrow-Band Magnetism Allowed by Quantum Geometry: Altermagnetism and Beyond
Minxuan Wang · Pei-Han Lin · Yang Ge · Jiabin Yu · [arXiv:2611.17414](https://arxiv.org/abs/2611.17414) · cond-mat.str-el · new

**为何相关：** 在色散完全相同的窄带中，只有强量子几何才会让在位相互作用投影出较长程通道，从而稳定共线交错磁相；弱几何则只得到常规铁磁——交错磁 × 量子几何 × 窄带关联。

要点：量子几何对窄带关联相很重要，但它如何影响不同磁序——尤其是交错磁——的竞争，仍不够清楚。作者研究具有严格在位广义 Hubbard–Kanamori 相互作用的四极绝缘体模型，其中 Néel 反铁磁与交错磁都是对称性允许的。孤立最低窄带在色散相同的情况下，可以是受阻原子带（强量子几何）或平凡原子带（弱量子几何）。对最低带做部分填充的 Hartree–Fock 计算表明：弱几何情形只有常规铁磁；强几何情形则出现两个共线交错磁相以及向列相。差别来自投影相互作用的结构：强几何时出现可观的较长程通道，弱几何则由在位 Hubbard 通道主导。这说明，当晶体对称性不足以单独锁定磁序时，量子几何对窄带交错磁的出现是关键的。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 3. Quantum computational spectroscopy of complex resonances and optical residues
Payman Mahmoudi · Jiate Luo · Chonghao Zhai · Qiang Shi · Alexander Yosifov · Jinzhao Sun · [arXiv:2611.18388](https://arxiv.org/abs/2611.18388) · quant-ph · new

**为何相关：** 在统一的谱滤波与测量框架中，同时重建非厄米复共振极点及其双正交光学留数，并分析例外点附近的灵敏度——非厄米本征结构 × 例外点 × 开放系统光谱。

要点：耗散分子体系的光学谱既取决于复共振能量，也取决于每个共振与光学探针的耦合方式；在非厄米描述中，这些贡献由左右本征矢的复留数决定。作者提出一套量子协议：用厄米膨胀把左右本征矢嵌入零能子空间，再以幺正线路计算高斯滤波关联，并通过复非对角测量的比值得到留数，无需再对各个本征态做变分优化。他们在 IBM 量子硬件上对耗散等离激元–分子模型做了谱重建，分辨出探针依赖的模态贡献如何产生干涉双峰，或伴随共振能量的分离，并分析了例外点附近留数重建的灵敏度。协议把复光学留数变成可直接计算的输出，从而把非厄米本征结构与可测光学响应连起来。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 4. Regularized Neural Quantum States for Heisenberg Magnets
Stefan Liscak · Vladyslav M. Kuchkin · Andreas Michels · Thomas L. Schmidt · Andreas Haller · [arXiv:2611.18497](https://arxiv.org/abs/2611.18497) · cond-mat.str-el · new

**为何相关：** 以参考磁纹理选定自旋基，再用适应变分态流形几何的正则化黎曼梯度下降，稳定求解含 DM 相互作用的二、三维手性海森堡磁体——神经网络波函数 × 量子磁体。

要点：神经网络量子态求解有局域磁序的自旋体系时，基的选择与参数空间漂移都会妨碍收敛。作者先根据经典或量子参考态的磁纹理构造自旋基，再引入适配量子态几何的正则化黎曼梯度下降，以改善收敛并抑制漂移。二者结合后，可以稳定计算含 Dzyaloshinskii–Moriya 相互作用的二、三维手性自旋体系基态。所得变分能量与高保真 DMRG 相当；在周期与层状几何中，还能给出明显更紧的基态能量上界。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 5. Foundation Tensor Networks Generalize Across Quantum Lattice Systems
Ryan T. Grimm · Michael Lindsey · [arXiv:2611.17655](https://arxiv.org/abs/2611.17655) · cond-mat.stat-mech · new

**为何相关：** 针对神经网络波函数“基础模型”仍需大量采样的瓶颈，用神经网络直接从哈密顿量生成基态的张量网络表示，并在无序量子格子上做大规模平均——张量网络 × 神经网络波函数 × 无序多体。

要点：无序体系要求对每个无序实现都求基态，神经网络波函数与张量网络都因此很吃力；已有把哈密顿量映射到基态的神经网络基础模型，但仍需大量采样才能估可观测量。作者提出基础张量网络（FTN）：由神经网络从哈密顿量生成基态波函数的张量网络表示。为加快训练，他们发展基于迭代一维信念传播的 GridBP，把能量期望值的计算降到两次张量收缩。用 FTN 对量子 Edwards–Anderson 模型做有限尺寸标度，得到玻璃化转变的临界参数；再借助矩母函数以一次收缩计算序参量，从而对 50 万个无序实现做平均，给出高保真的临界参数估计。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 6. Dissipation as a Resource for Entanglement via High-Spin Mediator Purification
Ellen Martins Fernandes · Fabricio Macedo de Souza · [arXiv:2611.18489](https://arxiv.org/abs/2611.18489) · quant-ph · new

**为何相关：** 用 Lindblad 方程比较相干驱动与耗散通道对热混合高自旋媒介的纯化，表明耗散才是使两自旋比特稳健纠缠成为可能的资源——开放系统 × 耗散调控 × 纠缠。

要点：两个自旋比特通过单个热混合的高自旋（$S=5/2$）磁杂质产生纠缠。作者表明：任何再强、再共振的相干驱动都无法把媒介纯化到超过其热值——因为幺正演化严格保持纯度——而耗散通道可将其纯化到光泵浦循环所允许的上限 $\mathrm{Tr}[\rho_M^2]\approx 0.8$。用单锰自旋测得的光泵浦速率建模后，纠缠并不随泵浦强度单调增加，而是在有限速率处取峰：同一通道也会通过耦合把退相干漏到比特上。在实验泵浦速率下，单次 80 ns 脉冲即可纯化媒介，极化保持时间比纠缠动力学长三个数量级；12 K 时第一次复现的 negativity 从 0.18 升至 0.64，并在 30 K 仍高于 0.6。耗散在这里不是要被压掉的噪声，而恰恰是稳健纠缠生成的资源。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 7. Dissipation-induced integrability in a spin-1 chain and a Bose-Hubbard mixture
Kaixiang Lu · Mingdi Xu · Xiang-Ping Jiang · Lei Pan · [arXiv:2611.17928](https://arxiv.org/abs/2611.17928) · quant-ph · new

**为何相关：** 在非可积自旋-1 链上，通过每键一条耗散通道得到 Yang–Baxter 可积的无跃迁哈密顿量，并给出任意长度的完整 Liouvillian 谱——开放多体 × 耗散诱导可积性。

要点：作者构造一条非可积自旋-1 链，使其在每键一条耗散通道下获得 Yang–Baxter 可积的无跃迁（no-jump）哈密顿量。孤立周期体中能量是唯一非平凡的有限程守恒量；干涉抵消反向自旋转换后，剩下服从 nil-Coxeter 关系的定向移动，并在开链上生成程长递增的对易守恒量。他们得到任意链长的完整 Liouvillian 谱，并找到指数多的阻塞自旋组态，其叠加全部是稳态。分辨键输出并不改变无跃迁哈密顿量，两个组态有差别的每一键对它们的退相干贡献相同。在二分量 Bose–Hubbard 链中，相反的损失相位给出反向传播的两组分量；当种间吸引与种内排斥匹配时，运动与碰撞进入同一个转移矩阵。这种键上干涉为其他开放量子多体系统走向可积提供了一条路径。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 8. Data re-uploading in Quantum Reservoir Computing
Saud Čindrak · Kaito Kobayashi · Lara Giebeler · Kathy Lüdge · [arXiv:2611.17913](https://arxiv.org/abs/2611.17913) · quant-ph · new

**为何相关：** 把电路量子机器学习里已成常规的数据重上传引入物理量子储备计算，用以调控并增强高阶非线性处理能力——量子机器学习 × 量子储备计算 × 开放/耗散对照。

要点：数据重上传能扩大参数化量子线路的可学习函数空间，但在量子储备计算中的作用还很少被讨论。作者把它引入物理量子储备计算，表明重复编码输入显著增强对高阶非线性多项式的可学习性，并改善混沌时间序列预测。他们比较计算代价固定或递增的协议，并对照一种耗散协议，以区分重复编码与额外态覆盖的效果。在信息处理容量框架下，编码次数增加会把容量推向更高阶非线性，形成记忆–非线性权衡；相比之下，耗散协议并不能扩展可学习的非线性阶数，对任务表现的改进也有限。数据重上传因此成为调节并增强物理量子储备计算非线性处理的有效手段。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 9. Efficient Parameter Estimation through Quantum Extreme Learning
Dingwei Zhao · Srijon Ghosh · Victor Montenegro · Matteo G. A. Paris · Marco G. Genoni · Abolfazl Bayat · [arXiv:2611.18329](https://arxiv.org/abs/2611.18329) · quant-ph · new

**为何相关：** 用量子极限学习做参数估计，避免显式构造似然函数，并在横场 Ising 模型上优化询问时间、扩展到双时测量，且对退相干有稳健性——量子传感 × 量子极限学习。

要点：量子传感通常要用贝叶斯或最大似然等最优估计器，而这需要构造似然函数：动力学完全已知时经典构造仍可能很重，模型无关的实验构造则更耗资源。作者提出基于量子极限学习的框架，不必显式写出似然。以横场 Ising 模型估计外横场为例，只需少量训练点即可达到较高估计精度；他们还发展询问时间优化策略，在把采样涨落压在给定阈值以下的同时尽量减小估计误差，并进一步把两个时刻的测量结果并入特征空间，显著提高精度。精度随训练点数单调改善，增大系统尺寸通常也有帮助（但并非单调）；协议对退相干稳健，适合近期量子器件。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 10. Fast forward-and-backward creation of non-equilibrium Gibbs state in driven dissipative quantum systems
Katsuhiro Nakamura · Otabek Normukhamedov · Iwan Setiawan · Jasur Matrasulov · [arXiv:2611.17738](https://arxiv.org/abs/2611.17738) · quant-ph · new

**为何相关：** 在 GKSL/Lindblad 方程框架中，用快进（及其反向）协议为驱动耗散系统构造非平衡 Gibbs 态，并在周期驱动下得到极限环式的时间周期解——开放耗散动力学 × 周期驱动。

要点：作者把快进方法用到开放耗散量子系统的绝热演化。以谐振子与量子自旋为原型，在驱动场快速变化并与热库接触时，给出生成非平衡 Gibbs 态的协议：先在固定外场下准备 Gibbs 态，再绝热改变外场；为使准绝热 Gibbs 态仍是 GKSL 方程的解，他们反解出哈密顿量与耗散子的非绝热修正，再做快进–快退的时间重标度，得到修正后的哈密顿量以及耗散系数之间的细致平衡条件。该方案在周期驱动下生成时间周期的 Gibbs 态，如同改进 GKSL 方程的极限环解；得益于快进版细致平衡，系统的功与热流满足能量守恒，包含库在内的整体过程可逆。耗散系数的正定性限制了快进驱动的速度；低温下周期驱动的速度上限正比于 $\tilde{\beta}^{-1/2}\exp(a\tilde{\beta})$。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 11. Efficient representations by PEPS: critical free-fermion and chiral topological states
Ignacio Cirac · Rahul Trivedi · [arXiv:2611.17936](https://arxiv.org/abs/2611.17936) · quant-ph · new

**为何相关：** 为二维临界自由费米子以及手性拓扑态构造全局误差受控、键维随系统尺寸与 $1/\epsilon$ 多项式增长的 PEPS，并讨论 Gutzwiller 投影后的手性自旋液体——张量网络 × 手性拓扑。

要点：作者在二维格子上构造投影纠缠对态（PEPS）近似，使全局误差不超过 $\epsilon$，而键维对系统尺寸与 $1/\epsilon$ 只是多项式的；覆盖二维临界自由费米子模型以及手性拓扑态。对半填充最近邻紧束缚模型，他们把高斯小波变换、一维链的 MPS 近似与选定的费米子交换结合起来。对任意一致有隙、有限程的二次哈密顿量，则给出基于重复单粒子过滤的构造，可在任意空间维得到高斯 PEPS，并包括 $p+ip$ 模型与方格子陈绝缘体的显式例子。他们还证明：对固定数目、任意填充的自由费米子高斯 PEPS 做 Gutzwiller 投影，不会显著放大近似误差，从而为所得状态——包括常见的格子手性自旋液体——提供多项式键维的 PEPS 近似。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 12. Underlying orbital $U(1)$ symmetry in quantum limit cycles
Chong Chen · [arXiv:2611.17890](https://arxiv.org/abs/2611.17890) · quant-ph · new

**为何相关：** 即使没有物理转动对称，量子极限环的谐波 Liouvillian 谱仍具有轨道 $U(1)$ 结构，并与量子几何及有限尺寸相位扩散联系起来——开放系统 × Liouvillian 谱 × 量子几何。

要点：量子极限环具有谐波 Liouvillian 谱，但在缺乏物理转动对称时，其底层轨道 $U(1)$ 结构通常并不显然。作者通过相似变换，把谐波、不衰减的 Liouvillian 扇区映射到一个厄米角动量哈密顿量，从而构造轨道相位平移的幺正表示。所得相位态具有与物理轨道形状无关的均匀 Fubini–Study 几何；对理想量子极限环，相应密度矩阵还具有均匀的 Bures 几何。在有限尺寸下，相位扩散会阻尼缓慢的 Liouvillian 谐波，但有效轨道 $U(1)$ 对称仍然保持；相位态可区分性的下降与有效几何的收缩，可由微观的缓慢 Liouvillian 谱定量预言。工作把开放量子系统中的轨道相位对称、量子几何与有限尺寸相位扩散连在一起。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*
