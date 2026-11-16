# 11/13 arXiv 兴趣摘要（工作日）

扫了今天（美西 11/13，周五）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Friday, 13 November 2026**：这是 Veterans Day（周三 11/11）顺延后、周四晚间放出的批次，覆盖约周二 14:00 至周四 14:00 ET 的投稿窗口，体量明显大于平日。新投稿：cond-mat 169、quant-ph 120、hep-th 60、math-ph 17、cs.LG 186、stat.ML 16（交叉与替换未计入）。已排除此前已荐的 402 篇。主题上二维受挫非厄米平带的非布洛赫拓扑与趋肤效应、从长时间动力学读取 Lindbladian 非厄米拓扑、准晶中由 $d_{x^2-y^2}$ 交错磁诱导的高阶拓扑、Aharonov–Casher 带上神经网络变分蒙特卡洛对分数量子陈绝缘体与 Wigner 晶体的竞争、里德伯微系综阵列中的高阶例外点传感、$g$/$i$ 波交错磁的非局域多极自旋积累、$\mathrm{Sr}_2\mathrm{CoTeO}_6$ 中的 Kitaev 交换与交错磁、监测准周期超导体中的临界纠缠与 Zeno 局域、手性声子驱动的 Floquet 反常霍尔、准周期驱动的几何分类、耗散 Ising 上的量子数据分类，以及开放共线磁体中的磁振子手性选择较集中。按兴趣锚点筛了 **12 篇**（全部为新投稿；未收交叉或替换稿；跳过假阳性或弱相关如自引力自旋介子管、流体管网的神经网络基方法、以交错磁结为候选平台但主线是超导 qudit 保护的电路、手性分子调控斯格明子扩散、中性原子纠缠门的运动关联、偏器件的畴壁射频驱动等；近邻但未再拉长名单的还有量子磁体 Dirac 量子几何的偏振拉曼读出、从动力学结构因子学习哈密顿量、光力纠缠的反馈与神经网络预测、有限 Majorana 线反射零点处的例外点，以及 $p$ 波磁体中的单态–三重态超导等）。本日用户机 Zotero（DESKTOP-00O6NSD）离线，仅对缓存的 arXiv ID 列表（187，约 10/30）做只读核对：**短名单无同 ID**；主题近邻未逐条标注。

**建议先翻这三篇：**
1. **Non-Bloch Topology of Frustrated Non-Hermitian Flat Bands** —— 二维受挫非厄米格子中的精确平带，会被其他能带诱导出与基无关的趋肤效应，并用非布洛赫环面上的不可收缩环态给出体边对应——非厄米拓扑 × 非布洛赫平带 × 趋肤效应。
2. **Detecting non-Hermitian topology from long-time dynamics** —— 从协方差矩阵的长时间弛豫读取开放高斯系统 Lindbladian 谱上的非厄米拓扑不变量，即使 Liouvillian 趋肤效应掩盖边缘模仍然适用——非厄米拓扑 × 开放 Lindblad 动力学。
3. **Higher-order topology induced by altermagnetism in quasicrystals** —— 在 Thue–Morse 与 Ammann–Beenker 准晶中，$d_{x^2-y^2}$ 波交错磁打开边隙并诱导零能角态，而常规反铁磁与 $d_{xy}$ 波则不能——交错磁 × 高阶拓扑 × 准晶。

---

### 1. Non-Bloch Topology of Frustrated Non-Hermitian Flat Bands
Fan Yang · Jiong-Hao Wang · Hui Liu · Emil J. Bergholtz · [arXiv:2611.15863](https://arxiv.org/abs/2611.15863) · cond-mat.mes-hall · new

**为何相关：** 在二维受挫非厄米格子中构造精确平带，揭示平带可被其他能带诱导出与基无关的非布洛赫趋肤效应，并用非布洛赫环路上的不可收缩环态给出体边对应——非厄米拓扑 × 非布洛赫平带 × 趋肤效应。

要点：从厄米到非厄米，能带结构会被趋肤效应剧烈改写，二维情形仍不够清楚。作者构造一类具有精确平带的二维受挫非厄米模型（呼吸 Kagome 与棋盘格子），可用非布洛赫能带论描述。平带会因其他能带而获得与基选择无关的趋肤效应；在呼吸 Kagome 中，这一效应恰好出现在平带进入色散带周期边界谱所张成的区域内。平带在能带交叉处若本征矢出现不可移去的不连续，则变为奇异平带——在非厄米系统中该奇异性对边界条件敏感，并不被带的平坦本身保护。相应的非布洛赫体边对应表现为：体中出现奇异带接触，边界上出现稳健的平带趋肤模；该边界模可由紧致局域趋肤模的宏观叠加几何地构造，拓扑起源是非布洛赫环面上两个线性无关的不可收缩环态。他们还用零能角模的双正交极化定义不变量，并在放松精确平坦后实现近乎平坦的非布洛赫陈数能带。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 2. Detecting non-Hermitian topology from long-time dynamics
Antonio D'Abbruzzo · Rosario Fazio · [arXiv:2611.16745](https://arxiv.org/abs/2611.16745) · cond-mat.stat-mech · new

**为何相关：** 从协方差矩阵的长时间弛豫读取开放高斯系统 Lindbladian 谱上的非厄米拓扑不变量，即使 Liouvillian 趋肤效应掩盖边缘模仍然适用——非厄米拓扑 × 开放 Lindblad 动力学 × 探测协议。

要点：手征对称开放高斯系统的 Lindbladian 谱带有非厄米拓扑不变量，但边缘模常被 Liouvillian 趋肤效应掩盖，不易直接分离。作者提出：看协方差矩阵的长时间弛豫即可读取该不变量，不必工作在短时或隔离边缘通道的设定。以库诱导非互易的 Kitaev 链为例，他们先解析给出此前未知的完整拓扑相图，再表明该协议能可靠区分所有不同相。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 3. Higher-order topology induced by altermagnetism in quasicrystals
Xingmin Huo · Xingchuan Zhu · Xingyu Ma · Shiping Feng · Huaiming Guo · [arXiv:2611.15139](https://arxiv.org/abs/2611.15139) · cond-mat.str-el · new

**为何相关：** 在 Thue–Morse 与 Ammann–Beenker 准晶中，$d_{x^2-y^2}$ 波交错磁与二维拓扑绝缘体耦合打开边隙并诱导零能角态，而常规反铁磁与 $d_{xy}$ 波则不能——交错磁 × 高阶拓扑 × 准晶。

要点：交错磁的动量依赖自旋劈裂在没有平移对称的准晶中如何理解，仍不够清楚。作者把 $d$ 波准晶交错磁序耦合到二维拓扑绝缘体，研究 Thue–Morse 与 Ammann–Beenker 准晶中的高阶拓扑相。结果显示 $d_{x^2-y^2}$ 波交错磁具有类似铁磁的一面：打开边隙并诱导零能高阶拓扑角态；常规反铁磁与 $d_{xy}$ 波构型则无法诱导高阶段隙。这说明交错磁对称性及其与格子角的对齐，是实现高阶拓扑的关键；高阶拓扑相的出现也可作为识别非周期体系中交错磁序的签名。与 11/11 那篇近邻 $d_{xy}$ 波在晶体中诱导几何选择高阶拓扑形成对照：这里恰恰是 $d_{x^2-y^2}$ 在准晶中起作用。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 4. A neural quantum state variational Monte Carlo study of Aharonov-Casher bands
Conor Smith · Nicolás Morales-Durán · Jingtian Shi · Andrew J. Millis · Miguel A. Morales · Shiwei Zhang · [arXiv:2611.17144](https://arxiv.org/abs/2611.17144) · cond-mat.str-el · new

**为何相关：** 用神经网络变分蒙特卡洛，在摩尔材料的连续 Aharonov–Casher 模型中比较分数量子陈绝缘体与广义 Wigner 晶体，并进入强带混合、其他方法难以到达的尺寸——神经网络波函数 × 分数量子陈绝缘体。

要点：作者引入受磁通附着启发的变分波函数来捕捉分数化相，并与描述晶格相的 Slater–Jastrow 试探态比能量，从而在分数填充、强带混合下给出相图。非均匀量子几何所编码的离散平移对称，对 $\nu=1/3$ 与 $\nu=2/3$ 的分数化态影响不同；带混合还可以稳定非公度晶体基态。工作揭示了拓扑相与非拓扑晶体相之间相当精细的竞争。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 5. Higher-Order Exceptional Point Sensing with Rydberg Micro-Ensemble Arrays
Jun Zhang · Ya-Jun Wang · Zi-Han Li · Jin-Hang Fang · Luan-Yi Wei · Qing Li · Guang-Can Guo · Bang Liu · Li-Hua Zhang · Dong-Sheng Ding · Bao-Sen Shi · [arXiv:2611.14893](https://arxiv.org/abs/2611.14893) · cond-mat.quant-gas · new

**为何相关：** 在冷里德伯气体的微系综阵列中，用空间排布把有效非厄米维数做大，实现高阶例外点，并以相界移动达到超越标准量子极限的微波电场灵敏度——高阶例外点 × 量子传感。

要点：高阶例外点来自多个本征值与本征态同时聚合，对微扰有更强的谱响应，但在相互作用多体系统中实现与调控并不容易。作者在冷里德伯气体中构造空间结构的微系综阵列，长程相互作用与空间连接扩大有效非厄米维数，从而通过改变位点排布实现不同阶的例外点。位点间相互作用还能提高量子 Fisher 信息；高阶例外点给出愈发非线性的相界响应，并可由测量时间与原子数进一步调控。追踪相界移动，他们达到 $0.47(10)\,\mathrm{nV\,cm^{-1}\,Hz^{-1/2}}$ 的灵敏度，超越标准量子极限。该平台把高阶非厄米临界性、多体动力学与微波传感连在一起。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 6. Nonlocal multipolar spin accumulation in altermagnets beyond d-wave
J. W. Gonzalez · [arXiv:2611.15438](https://arxiv.org/abs/2611.15438) · cond-mat.mes-hall · new

**为何相关：** 在自旋守恒的 $g$、$i$ 波交错磁中，均匀纵向电导没有自旋奇分量，但点注入的非局域自旋积累能读出费米速度的更高偶极矩及其角谐波——交错磁 × 自旋积累 × 超越 $d$ 波。

要点：Boltzmann 理论预言，第一个非零自旋奇速度矩的阶数 $m=2,4,6$ 分别决定主导角谐波、渐近径向依赖 $r^{2-m}$，以及固定距离与注入电流下振幅随散射时间按 $\tau^{m-3}$ 标度。对 $g$ 波，四阶矩给出四次角谐波与 $r^{-2}$ 尾巴。量子输运模拟在不拟合振幅的情况下支持有限几何 Boltzmann 的径向剖面；三种对称性下量子振幅比基于 Born 散射时间的 Boltzmann 预言高出 15–65%。在双接触条带中，他们在预选径向窗口、独立的 1800 个无序样本上以 $6.8\sigma$ 检出 $g$ 波四次谐波，其振幅随交错磁劈裂减小而下降。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 7. Kitaev Exchange and Altermagnetism in the Double Perovskite Sr$_2$CoTeO$_6$: An Ab Initio Study
Alexey V. Ushakov · Sergey V. Strelsov · [arXiv:2611.15152](https://arxiv.org/abs/2611.15152) · cond-mat.str-el · new

**为何相关：** 第一性原理表明双钙钛矿 $\mathrm{Sr}_2\mathrm{CoTeO}_6$ 同时具有可观的铁磁 Kitaev 交换与相当大的非相对论自旋劈裂，因而兼具 Kitaev 材料与交错磁——交错磁 × Kitaev 交换。

要点：DFT 给出近邻铁磁 Kitaev 交换 $|K|\sim J/3$，与面心立方格子一起造成显著的交换阻挫，使该材料进入中等 Kitaev 强度的材料之列。与此同时，体系是交错磁，具有可观的非相对论自旋劈裂，可导致横向压磁效应与非平庸磁光响应。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 8. Symmetry-Controlled Criticality and Zeno Localization in a Monitored Quasiperiodic Superconductor
Pinaki Singha · Marcin Szyniszewski · Nilanjan Roy · Auditya Sharma · [arXiv:2611.16912](https://arxiv.org/abs/2611.16912) · quant-ph · new

**为何相关：** 连续监测带配对的准周期自由费米子，用拓扑纠缠熵看到 $(\ln L)^2$ 临界相与面积律相的转变，并在深 Zeno 区给出轨迹的有效非厄米 BdG 描述——监测开放系统 × 纠缠标度 × 非厄米局域。

要点：测量诱导的自由费米子转变强烈依赖对称性，但其与准周期局域、超导配对的交织仍少有研究。准周期性既调控局域，也改变被监测场论的对称类。在量子态扩散模拟中，以拓扑纠缠熵为探针，他们找到临界相（冯诺依曼熵按 $(\ln L)^2$ 标度）与面积律相之间的转变；干净极限下则无转变，这与相应的 DIII 与 D 非线性 sigma 模型一致。转变线具有强多重分形，并对准周期性呈非单调依赖，作者将其联系到对称类交叉。在深 Zeno 区，他们为单条轨迹导出有效非厄米 Bogoliubov–de Gennes 描述，并得到与数值定量符合的闭式局域长度。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 9. Chiral-phonon-induced anomalous Hall effect in bilayer MoSe$_2$
Omer Yaniv · Swati Chaudhary · Carolina Paiva · Dominik M. Juraschek · [arXiv:2611.15761](https://arxiv.org/abs/2611.15761) · cond-mat.mtrl-sci · new

**为何相关：** 光驱动手性声子在非磁、有中心对称的双层 $\mathrm{MoSe}_2$ 中产生圆偏振动力学 Rashba 自旋轨道耦合，使两个谷携带同号 Berry 曲率并给出符号随声子手性翻转的反常霍尔——Floquet × 自旋轨道 × 反常霍尔。

要点：对 $E_u$ 声子的圆偏振激发产生圆偏振的动力学 Rashba 耦合；由此得到的 Floquet 能带在两个谷携带同号 Berry 曲率，霍尔响应的符号跟随声子手性。对实验可及的光脉冲，他们估计 $\sigma_{xy}\sim 10^{-2}$–$0.21\,e^2/(2\pi\hbar)$。手性声子因此提供了一条在超快时间尺度上调控电子 Berry 曲率与输运的路径。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 10. Geometric Theory of Quasiperiodically Driven Systems
Chengzhi Ye · Marin Bukov · [arXiv:2611.16683](https://arxiv.org/abs/2611.16683) · quant-ph · new

**为何相关：** 用反向绝热驱动构造任意准周期驱动的动力学不变空间（Floquet 态的推广），并按几何与拓扑分成（非）阿贝尔、（非）扭转四类，其中阿贝尔非扭转类把 Floquet 定理直接推广到不可公度驱动——Floquet 推广 × 准周期驱动 × 几何分类。

要点：准周期驱动缺少一套像 Floquet 那样用有效与时无关哈密顿量及其本征态来描述演化的通用理论。作者基于反向绝热驱动，用精确的有效平均能量算符与相应规范势分解幺正演化，并在频率格子算符空间用变分原理计算规范势。按动力学不变空间的几何与拓扑，驱动被分成（非）阿贝尔与（非）扭转四类：阿贝尔非扭转类允许把 Floquet 定理直接推广到不可公度准周期驱动；他们进一步给出非阿贝尔推广。还提出一种以动力学不变本征空间聚并来标志的遍历性，类比经典混合相空间中遍历性的出现。该框架原则上也可用于超出准周期驱动的情形。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 11. Ergodicity breaking for data classification in a dissipative Ising model with competing two- and four-body interactions
Simon Kochsiek · Mario Boneberg · Igor Lesanovsky · [arXiv:2611.17036](https://arxiv.org/abs/2611.17036) · quant-ph · new

**为何相关：** 把一类量子神经网络映射到 Lindblad 演化的耗散量子 Ising 模型，用竞争的二体与四体相互作用设计定态流形，实现带非线性判决边界的多类量子数据分类——量子机器学习 × 耗散开放系统。

要点：涌现非线性会带来非遍历动力学：落在不同吸引盆的初态演化到可区分的定态，这正是量子数据分类的机制。作者考虑具有竞争二体与四体相互作用的 Ising 模型，结合平均场与小尺寸精确数值表明，定态流形可以被设计以支持多类分类，其吸引盆结构允许带非线性判决边界的量子态分类。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 12. Magnon Chirality Selection at Equal Linewidths in Open Collinear Magnets
Dinghui Wang · Lulu Liu · [arXiv:2611.15113](https://arxiv.org/abs/2611.15113) · cond-mat.mes-hall · new

**为何相关：** 在开放共线磁体中，即使各共振线宽相同，空间关联损耗与相干交换仍可选择一种磁振子手性，并在更强损耗下到达例外轮廓——开放磁体 × 非厄米手性选择 × 磁振子。

要点：作者构造被动共线模式网络：空间关联损耗与相干交换使相反角动量具有不同存活概率。初始未极化的混态可达到 26.9% 的极化，同时保留 29.9% 的布居；等谱的正规对照则没有极化。自旋与晶体的联合转动会反转信号，并交换更强损耗下到达的例外轮廓。他们用非厄米共线自旋空间小群在手性与复频率上的作用，整理允许的极点配对；第二种实现即使总卷绕数为零，也能把共轭手性扇区分到对角相对的两边。两种读出分别约束极点，以及制备、本征矢与物理库。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*
