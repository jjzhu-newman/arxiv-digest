# 11/23 arXiv 兴趣摘要（工作日）

扫了今天（美西 11/23，周一）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Monday, 23 November 2026**：这是常规周一批次（周末窗口），覆盖约周五 14:00 至周一 14:00 ET 的投稿窗口。新投稿：cond-mat 88、quant-ph 51、hep-th 17、math-ph 8、cs.LG 96、stat.ML 7（交叉与替换未计入）。已排除此前已荐的 487 篇。主题上奇宇称磁体的电荷–自旋选择定则与时域/频谱分离（含 Floquet 工程的 MnPS$_3$）、含时非厄米 $T$ 对称体系中对称性破缺被禁止、量子机器学习中指数集中的控制、模型交错磁里自旋涨落对谱函数与输运的影响、交错磁 CrSb 不同生长路径的各向异性输运、$d$ 波声子角动量劈裂器、无自旋 TMD 中的纯轨道霍尔与轨道力矩、量子点阵列上的最小手性 $p$ 波超导、双曲 Kitaev 自旋液体的磁场响应、无需测量与经典反馈的自主量子机器学习、用物理信息核处理费米子符号问题，以及摇动光晶格中 $^6$Li$_2$ 凝聚体的 Floquet 能带较集中。按兴趣锚点筛了 **12 篇**（10 篇新投稿、2 篇交叉投稿；未收替换稿；跳过假阳性或弱相关如无人机最优控制 PINN、化工过程时空图网络、V$_2$O$_3$ 动力学冻结的关键词误匹配、机械超材料界面波、FeCr 位错、斜面滚动铁磁球、暖暴胀中的欧姆耗散、DeepONet 预条件子，以及核物理 Skyrme 变分（并非磁斯格明子）等；近邻但未再拉长名单的还有半手征对称保护的拓扑相、Reset 量子信道、竞争相互作用 XXZ 链中的长程纠缠、Janus MXene 中 hexameron 与拓扑磁振子、拓扑受阻的 Kondo 杂化、用收缩层增强量子神经网络、混合 SQUID 阵列磁强计，以及 Thouless 泵与 Majorana 相中的赝熵等）。本日用户机 Zotero（DESKTOP-00O6NSD）离线，仅对缓存的 arXiv ID 列表（187，约 10/30）做只读核对：**短名单无同 ID**；主题近邻未逐条标注。

**建议先翻这三篇：**
1. **General Transport Signatures of Odd-Parity Magnets: Charge--Spin Selection Rules and Temporal--Spectral Separation** —— 相对偶宇称交错磁中由晶体自旋霍尔效应实现的空间分离，给出奇宇称磁体普遍的时域与频谱电荷–自旋分离，并在 Floquet 工程的 MnPS$_3$ 等体系中验证；反幺正 $\mathcal{T}\tau$ 会反转贝里响应的选择定则，从而区分两种保护对称——奇宇称磁/交错磁 × Floquet × 自旋电子学。
2. **Forbidden T-symmetry breaking in time-dependent non-Hermitian systems with gain and loss** —— 一类含时、$T$ 对称且有增益损耗的非厄米体系中，通常的对称性破缺被禁止，增大增益损耗后系统仍保持 $T$ 对称相，即使增益损耗空间分布随机、也与调制周期无关——非厄米 × 开放系统。
3. **Practical insights into controlling exponential concentration in quantum machine learning** —— 在统一的可观测量方差框架下比较保真度量子核、投影量子核与量子极限学习中的指数集中，并讨论带宽缩放等抑制手段——量子机器学习。

---

### 1. General Transport Signatures of Odd-Parity Magnets: Charge--Spin Selection Rules and Temporal--Spectral Separation
Junxi Yu · Pu Zhang · Yichen Liu · Yongpan Li · Cheng-Cheng Liu · [arXiv:2611.27763](https://arxiv.org/abs/2611.27763) · cond-mat.mes-hall · new

**为何相关：** 相对偶宇称交错磁里由晶体自旋霍尔效应实现的电荷–自旋空间分离，给出奇宇称磁体普遍的时域与频谱电荷–自旋分离，并在 Floquet 工程的 MnPS$_3$ 等体系中验证——奇宇称磁/交错磁 × 自旋电子学 × Floquet。

要点：对具有幺正自旋翻转反演 $\mathcal{U}=[C_2^\perp\Vert P]$ 的共线与非共线奇宇称磁体，该对称把电荷响应限制在奇次、把 $z$ 极化自旋响应限制在偶次，不依赖微观机制，也不要求自旋守恒。对半周期后变号的交流驱动，电荷与自旋电流具有相反的半周期宇称，频谱上分别只含奇次电荷谐波与偶次自旋谐波，从而即使在纵向输运、超出弱场时，也可出现没有直流电荷对应的直流自旋整流。虽然反幺正 $\mathcal{T}\tau$ 也可强制奇宇称能带，但它会反转贝里曲率及其偶极响应的电荷–自旋选择，从而给出区分两种保护对称的输运指纹。选择定则在全部线性与二阶机制中得到验证，并在最小奇宇称模型、Floquet 工程的共线 MnPS$_3$ 以及平衡态非共线 VCl$_2$ 族中展示了谐波分离。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 2. Forbidden T-symmetry breaking in time-dependent non-Hermitian systems with gain and loss
Li Ge · [arXiv:2611.27600](https://arxiv.org/abs/2611.27600) · physics.optics / quant-ph · cross

**为何相关：** 指出一类含时、有增益与损耗的 $T$ 对称非厄米体系中，通常的对称性破缺被禁止，增强增益损耗后系统仍保持 $T$ 对称相——非厄米拓扑与开放系统。

要点：$PT$ 对称非厄米体系在增益损耗较弱时能级全实，增强后出现共轭复能级，标志 $PT$ 对称破缺；$RT$ 或 $T$ 对称非厄米体系通常也有类似图景。本文证明：在有限希尔伯特空间中，对一类含时、$T$ 对称且有增益损耗的体系，这一典型破缺被禁止——即使增益损耗的空间分布是随机的，增大其强度后系统仍停留在 $T$ 对称相，且该行为与时间调制的时长或周期无关。若把同样的体系改成 $PT$ 对称，则这种“禁止破缺”不再出现。结果表明含时与不含时非厄米系统可以有定性上不同的对称性破缺行为。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 3. Practical insights into controlling exponential concentration in quantum machine learning
Fernando Mondragon-Sampedro · Diego Alvarez-Estevez · [arXiv:2611.27486](https://arxiv.org/abs/2611.27486) · quant-ph · new

**为何相关：** 在统一的可观测量方差框架下，比较保真度量子核、投影量子核与量子极限学习中的指数集中，并讨论带宽缩放等抑制手段——量子机器学习。

要点：量子机器学习模型常受指数集中困扰：系统变大后，量子可观测量对输入变化逐渐不敏感。作者在基于期望值方差的统一框架中比较保真度量子核（FQK）、投影量子核（PQK）与量子极限学习（QEL）。全局保真度核的集中主要由希尔伯特空间维数驱动；局域可观测量方法能减轻但无法消除该效应。在 PQK 与 QEL 中，集中主要受纠缠与量子动力学表达能力控制，QEL 中储备深度是关键因素。他们进一步把带宽缩放作为控制编码表达能力的通用手段：在中等参数范围内，限制编码的有效表达能力能有效减弱集中，但在结构上已经高度表达的设定中，这一保护会减弱。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 4. Impact of spin fluctuations on spectral functions and transport in a model altermagnet
Sourav Chakraborty · Manoranjan Kumar · Arun Paramekanti · [arXiv:2611.26725](https://arxiv.org/abs/2611.26725) · cond-mat.str-el · new

**为何相关：** 在棋盘格子 Hubbard 模型中用费米子蒙特卡洛跟踪自旋涨落的空间结构，讨论交错磁从有序基态到高温顺磁相的自旋分辨谱函数与输运——交错磁 × 强关联。

要点：受强关联量子材料中发现交错磁的推动，作者研究棋盘格子 Hubbard 模型里自旋依赖输运随温度的演化，方法能跟踪自旋涨落的完整空间依赖。他们给出从有序基态进入高温无序顺磁相时，自旋分辨单粒子谱函数与输运的变化，并指出结果可用自旋分辨 ARPES，以及固态或超冷原子候选体系中的自旋输运来检验。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 5. Growth and anisotropic directional dependent transport properties of Altermagnetic CrSb
Resham Babu Regmi · Hari Bhandari · Sk Jamaluddin · Abhijeet Nayak · Ashok Chaudhary · Mohamed El Gazzah · Alex T. Sheardy · Maksym Zhukovskyi · Allen G. Oliver · Nirmal J. Ghimire · [arXiv:2611.27072](https://arxiv.org/abs/2611.27072) · cond-mat.mtrl-sci · new

**为何相关：** 系统比较三种生长路径得到的交错磁 CrSb 单晶的结构、磁性和各向异性输运，为取向依赖的自旋电子学测量提供选晶依据——交错磁 × 实验输运。

要点：CrSb 是室温以上反铁磁有序、具有大的动量依赖自旋劈裂的金属性交错磁。作者比较 Sb 自助熔剂、Bi 助熔剂与化学气相输运三种生长：形貌不同，磁化整体呈一致的反铁磁响应，但 Bi 助熔剂样品在低温有额外贡献。全部样品呈金属电阻，直到 9 T 仍有不饱和的正磁阻；Sb 助熔剂与 CVT 样品的剩余电阻率比和磁阻相近，Bi 助熔剂样品剩余电阻更高、磁阻显著减小，符合更强的载流子散射。霍尔信号强烈依赖场–电流构型，包括非线性场依赖以及不同晶向相反的霍尔极性。工作表明各向异性磁输运在不同生长路径上可复现，但载流子散射对生长条件敏感。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 6. Atomistic theory of the $d$-wave phonon angular momentum splitter effect
Daniel A. Bustamante Lopez · Dominik M. Juraschek · [arXiv:2611.27747](https://arxiv.org/abs/2611.27747) · cond-mat.mtrl-sci · new

**为何相关：** 在棋盘调制弹性耦合的反铁磁方格子中，建立与 $d$ 波交错磁自旋劈裂器类似的声子角动量劈裂器理论——交错磁类比 × 声子角动量输运。

要点：作者计算温度梯度驱动的声子角动量输运与积累，发现横向响应可分成霍尔贡献与 $d_{xy}$ 波劈裂器贡献。劈裂器贡献同时需要反铁磁序与棋盘弹性调制，并呈现特征性的 $d_{xy}$ 角依赖；霍尔贡献则近乎各向同性。二者结合可以定向控制边缘处的声子角动量积累。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 7. Pure Orbitronics: Hall Responses and Torques by Orbital Exchange in Spinless Transition-Metal Dichalcogenides
Mahmoud Zeer · Dongwook Go · Yuriy Mokrousov · [arXiv:2611.27391](https://arxiv.org/abs/2611.27391) · cond-mat.mes-hall · new

**为何相关：** 在无自旋极化、也不依赖自旋轨道耦合的单层 MoS$_2$ 中，用轨道交换场给出本征反常霍尔电导、轨道霍尔响应与电流诱导轨道力矩——轨道电子学 × 自旋电子学近邻。

要点：轨道交换场直接耦合轨道角动量，可来自纯轨道相互作用，也可由声子、磁振子等手性激发动态产生。作者在 H 相单层 MoS$_2$ 中引入类塞曼轨道交换场，只在轨道空间打破时间反演，而让自旋自由度保持不活跃。该扰动即使在没有自旋磁性、也没有自旋轨道机制时，仍诱导可观的本征反常霍尔电导；弱场下轨道霍尔响应保持稳健，更强交换下则因能带重构而显著改组。电流还能对轨道磁化产生可观的轨道力矩。结果表明纯轨道物理即可驱动霍尔输运与非平衡力矩。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 8. Minimal chiral $p$-wave superconductor
Fabian Hassler · Michael Wimmer · [arXiv:2611.27555](https://arxiv.org/abs/2611.27555) · cond-mat.mes-hall · new

**为何相关：** 把 Kitaev 链的自下而上思路推到二维，用量子点阵列加上 Rashba 自旋轨道与 Zeeman 场构造最小手性 $p$ 波超导体，并在很小的阵列中得到手性 Majorana 边缘模与涡旋零模——拓扑超导 × 自旋轨道。

要点：手性 $p$ 波超导的涡旋束缚 Majorana 零模、边缘携带手性 Majorana 模，但尚无材料被明确指认。作者提出由 Andreev 点耦合的量子点方阵列：势垒中的 Rashba 自旋轨道提供 $p$ 波绕数，Zeeman 场使量子点无自旋。在最佳工作点上，边缘态被限制在最外一排，因而在 $3\times3$ 与 $5\times5$ 阵列中即可出现手性热导，以及分裂不到百分之一的涡旋束缚 Majorana 零模。该设置可用现有的 InAs 与 Ge 量子点阵列实现。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 9. Magnetic-Field Response of a Hyperbolic Kitaev Spin Liquid
Tao Yang · Baigeng Wang · Rui Wang · Z. Y. Xie · [arXiv:2611.27819](https://arxiv.org/abs/2611.27819) · cond-mat.str-el · new

**为何相关：** 在 Kekulé 着色的双曲 $\{8,3\}$ 格子上，用无限 PEPS 研究超出现可解极限时，双曲 Kitaev 自旋液体对均匀与交错磁场的多体响应——Kitaev 自旋液体 × 纠缠/张量网络 × Majorana。

要点：双曲几何可给出具有不同通量结构与 Majorana 谱的 Kitaev 自旋液体。作者发展带通量分辨 loop-gas 初始化、并适配几何的张量网络收缩的无限投影纠缠对态方法。均匀 [111] 场在弱场就会引起竞争变分分支之间的急剧切换；交错场下极化与平均格点通量则在宽得多的场范围内缓慢演化。交换能竞争有助于解释两种响应尺度的差异，而固定通量背景下的三阶有效 Majorana 模型给出对比鲜明的低能谱。工作把可解双曲自旋液体中依赖几何的分数化结构，与破坏通量守恒的物理微扰下的多体响应联系起来。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 10. Autonomous quantum machine learning via Riemannian gradient-based optimization
Kasidit Srimahajariyapong · Thiparat Chotibut · Suwannachad Suwannajitt · Tithivich Paka · Ricard Puig · Yudai Suzuki · Marek Gluza · Zoë Holmes · Supanut Thanasilp · [arXiv:2611.27815](https://arxiv.org/abs/2611.27815) · quant-ph · new

**为何相关：** 提出在量子域内用黎曼梯度完成训练、无需测量与经典反馈的自主量子机器学习，并在物态分类等任务上展示可自动发现隐藏对称——量子机器学习 × 物态识别。

要点：常规量子机器学习训练依赖反复测量与经典优化，量子到经典的信息抽取成为可扩展性瓶颈。作者给出基于黎曼梯度的自主训练框架，优化完全在量子域内进行；他们导出一类广泛学习任务的更新规则，给出可完全自主实现的充分条件，并在步长足够小时证明对训练迭代的指数收敛，同时分析电路深度增长带来的训练代价。训练后的模型能在事先未指定的情况下自动发现训练数据中的隐藏对称。对量子相分类以及带隐藏对称的幺正学习，数值表明只需低电路深度和少量不同训练样本即可完成学习。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 11. Solving fermionic sign problems with physics-informed kernels
Kenji Fukushima · Friederike Ihssen · Renzo Kapust · Jan M. Pawlowski · [arXiv:2611.27768](https://arxiv.org/abs/2611.27768) · hep-lat · cross

**为何相关：** 把物理信息核的生成抽样推广到具有复权重、与费米子系统同类结构的模型，用以处理符号问题——物理信息方法 × 强关联/符号问题。

要点：关键步骤是用物理信息核（PIK）处理复高斯分布加权和的符号问题。第一步 PIKfan 把实正态映射到这种加权和，抽样代价与实正态相当；第二步再用另一个 PIK 把该加权和演化到目标理论的分布，从而把一类广泛的复系统抽样约化为高斯抽样，主要计算负担变成求解 PIK。作者以任意化学势下的单格点 Hubbard 模型及其 $\phi^4$ 变形推广为例说明该方法。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 12. Interaction and confinement effects for a ${}^6\mathrm{Li}_2$ condensate in a shaken lattice
Yang-Hao Lee · Duc Trong Le · John Karnosh · Colin V. Parker · [arXiv:2611.27849](https://arxiv.org/abs/2611.27849) · cond-mat.quant-gas · new

**为何相关：** 改进摇动光晶格中 $^6$Li$_2$ 分子凝聚体的 Floquet 能带加载，把可观测窗口延长到 10 ms 以上，并看到束缚与相互作用对双阱色散分叉的影响——Floquet × 超冷原子。

要点：一维摇动光晶格可以把基带与第一激发带杂化成双阱色散；加载到该带的分子 BEC 会在相反准动量处分成两簇，但以往簇寿命只有 2–3 ms。作者把晶格轴与阱对齐，并用多频摇动序列非绝热地加载到双阱极小，使实验时间尺度超过 10 ms。更长时间下，动量分布定性依赖于沿晶格方向的束缚：束缚较强时，布里渊区边界出现动量峰，摇动频率谱显示该布居大致均分在基带与第一激发带。更长寿命还允许把磁场从弱相互作用的 650 G 扫到靠近 Feshbach 共振的 800 G；相互作用增强后分叉减弱并消失，作者认为这与分子尺寸增大有关。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*
