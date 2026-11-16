# 10/19 arXiv 兴趣摘要（工作日）

扫了今天（美西 10/19，周一）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Monday, 19 October 2026**；新投稿：cond-mat 86、quant-ph 47、hep-th 19、math-ph 4、cs.LG 126、stat.ML 15（交叉与替换未计入）。周末积压已放出，今日为常态周一批量。已排除 10/14–10/16 已荐的 34 篇。任意子/分数陈一侧有扭角 MoTe₂ FCI 中激子–e/3 准空穴束缚态、以及 AnyNet 神经波函数把连续 Abelian 任意子气体推到更大粒子数；开放/量子学习有组合经典–量子网络求解 Lindblad，以及 Liouville 空间非可逆对称；交错磁有 V₂Se₂O 族隐藏 η 型超导序与近邻工程转移非相对论自旋劈裂；Floquet/受监控有耗散 Dicke 二聚体中耦合离散时间晶体与逻辑门；Chern 带有张量网络下 FCI–手征超导–霍尔晶体竞争；另有 NV 手性分辨自旋波成像、Kagome 响应张量的物理信息机器学习，以及可编程拓扑纠缠态制备。按兴趣锚点筛了 **11 篇**（全部为新投稿；未收替换稿）。本地桌面当时未在线，**未做 Zotero 核对**。

**建议先翻这三篇：**
1. **Anyon bound states in MoTe$_2$ Fractional Chern Insulators** —— 扭角双层 MoTe₂ 分数陈绝缘体中偶极激子与 e/3 准空穴形成 meV 级束缚态，实空间可见局域电荷耗尽核与莫尔诱导八极结构——任意子 × 莫尔 FCI。
2. **Quantum-Classical Neural Networks for Solving Lindblad Master Equations** —— 经典神经网络 ⊕ 参数化量子线路的组合变分框架求解 Lindblad 主方程；纯化保证正定，并给出覆盖数上界与 barren plateau 联系——开放系统 × 量子机器学习。
3. **Anyonic Neural Network Wavefunctions** —— AnyNet 神经波函数精确施加任意子短距非解析行为，把连续 Abelian 任意子气体从 N=4 ED 推进到 N≈16–20——神经网络量子态 × 任意子。

---

### 1. Anyon bound states in MoTe$_2$ Fractional Chern Insulators
Tianhong Lu · Luiz H. Santos · [arXiv:2610.22473](https://arxiv.org/abs/2610.22473) · cond-mat.str-el · new

**为何相关：** 扭角双层 MoTe₂ 分数陈绝缘体中偶极激子与 e/3 准空穴形成 meV 级束缚态，实空间可见局域电荷耗尽核与莫尔诱导八极结构——任意子 × 莫尔 FCI。

要点：把任意子绑到光学活跃激子上，有望操控分数激发并暴露任意子内部空间结构。作者在扭角双层 MoTe₂ 分数陈绝缘体中，用连续相互作用模型的精确对角化，确立可动偶极激子与 e/3 准空穴的任意子束缚态：在合适的激子迁移率与激子–FCI 间距下，束缚能可达 meV 量级，且激子–准空穴纠缠强。空间关联给出激子周围约 e/3 电荷的局域耗尽核；准空穴除分数电荷外还呈现莫尔诱导的八极结构，层间隧穿各向异性强烈变形该结构而几乎不改包围电荷，把任意子内部轮廓与电子量子几何联系起来。工作给出莫尔异质结中稳健激子–任意子束缚条件，并说明这类复合体可触及超越总电荷的分数激发性质。

---

### 2. Quantum-Classical Neural Networks for Solving Lindblad Master Equations
Rafael Florencio Díaz · Julio Guerrero García · Elvira Romera Gutiérrez · [arXiv:2610.22691](https://arxiv.org/abs/2610.22691) · quant-ph · new

**为何相关：** 经典神经网络 ⊕ 参数化量子线路的组合变分框架求解 Lindblad 主方程；纯化保证正定，并给出覆盖数上界与 barren plateau 联系——开放系统 × 量子机器学习。

要点：变分量子算法模拟开放系统时，表达能力与可训练性仍不清楚。作者用残差代价最小化，把经典神经网络与参数化量子线路组成组合 ansatz；密度矩阵经扩大希尔伯特空间上的纯化表示，天然保证正定、厄米与单位迹，梯度由参数移位规则精确求取。进一步给出该组合模型覆盖数上界，并与纯量子神经网络比较：经典参数化扩大有效假设类、更细地控制复杂度，从而把表达力、覆盖数、有效维数与 barren plateau 现象联系起来。数值实验在代表性 Lindblad 方程上验证精度，并印证梯度集中的理论预言。工作为耗散量子动力学的组合量子机器学习模拟提供统一变分与理论框架。

---

### 3. Anyonic Neural Network Wavefunctions
Andres Perez Fadon · Pok Man Tam · Leyna Shackleton · [arXiv:2610.23815](https://arxiv.org/abs/2610.23815) · cond-mat.str-el · new

**为何相关：** AnyNet 神经波函数精确施加任意子短距非解析行为，把连续 Abelian 任意子气体从 N=4 ED 推进到 N≈16–20——神经网络量子态 × 任意子。

要点：无相互作用 Abelian 任意子气体的宏观行为悬而未决数十年；平面连续模型精确对角化此前最多做到 N=4。作者用神经网络波函数构建适合连续任意子气体的变分 ansatz，架构 AnyNet 能精确强制任意子统计诱导的短距非解析行为。N=4 与精确对角化高度一致；中间统计可到 N=16；近费米任意子可到 N=20，与微扰结果偏差约 0.4%。进一步考察谐振子阱中的任意子、任意子原子作为杂质束缚模型，并随统计参数扫描单粒子密度、对密度、角动量与多任意子聚并时的波函数标度。工作为理解任意子宏观相图（理论上已预言丰富相）打开数值大门。

---

### 4. Hidden Staggered Superconducting Order in V2Se2O-Family Altermagnets
Chun Yu Wan · Xiangxi Zhang · Fei Yang · Junwei Liu · [arXiv:2610.22935](https://arxiv.org/abs/2610.22935) · cond-mat.supr-con · new

**为何相关：** V₂Se₂O 族交错磁中谷对比自旋结构天然偏好 η 型交错超导序；建议用相位敏感约瑟夫森给出类 4e 响应——altermagnetism × 超导。

要点：η 配对指邻近元胞间序参量变号、幅度仍均匀的交错超导凝聚，自杨振宁提出近四十年仍缺稳定材料平台。作者指出交错磁虽对常规 BCS 配对破对，却在 V₂Se₂O 族中天然偏好 η 型配对：谷对比自旋结构给出分别以 X=(π,0)、Y=(0,π) 为中心、自旋极化相反且对称相关的谷，形成被公度动量 Q=(π,π) 分隔的自旋单态配对伙伴。自洽计算表明该 η 型态在化学势、跃迁与费米面拓扑大范围变化下仍稳健。探测上建议与均匀超导体的相位敏感约瑟夫森：相消干涉压制单库珀对隧穿而保留双库珀对过程，虽体凝聚仍是 2e 对，却呈现类 4e 约瑟夫森响应，作为隐藏交错序的直接相位指纹。

---

### 5. Engineering nonrelativistic spin splitting in semiconductors by altermagnetic proximity
Sing Lam Wong · Marcel Franz · [arXiv:2610.23773](https://arxiv.org/abs/2610.23773) · cond-mat.mes-hall · new

**为何相关：** 用近邻工程把 d 波交错磁的非相对论自旋劈裂经虚隧穿转移到常规半导体，相对论/非相对论分量随能带对齐定性不同——altermagnetism × 自旋电子学。

要点：交错磁兼具净磁化消失与动量依赖非相对论自旋劈裂，但同时满足交错磁对称、半导体能带与弱自旋轨道的材料稀缺。作者把这些要求拆到异质组分上：解析处理常规半导体耦合能隙 d 波交错磁，证明虚隧穿把交错磁自旋劈裂转移到半导体。关键是诱导的非相对论与相对论自旋劈裂对能带对齐的依赖定性不同——涉及价带的虚过程与导带通道行为可区分。近邻工程因此把“找齐全能材料”换成“选对界面与对齐”，为在常规半导体中工程化非相对论自旋劈裂提供可调路径。

---

### 6. Discrete time crystals and classical logic gates in coupled open Dicke models
Emmanuel D.G. U · Roy D. Jara Jr. · Jayson G. Cosme · [arXiv:2610.23043](https://arxiv.org/abs/2610.23043) · quant-ph · new

**为何相关：** 耗散 Dicke 二聚体中耦合离散时间晶体：强耦合不稳回正常相，短暂耦合可播种同步/反同步 DTC，并据此做 NAND/NOR——Floquet/时间晶体 × 开放系统。

要点：在带耗散的耦合 Dicke（Dicke 二聚体）中数值模拟耦合离散时间晶体（DTC）的平均场动力学：耦合使两 DTC 振荡振幅在瞬态弛豫后下降；耦合足够强时 DTC 失稳，系统弛豫到正常相（NP），临界附近弛豫时间发散，暗示连续相变。截断 Wigner 近似进一步看量子涨落如何改写动力学。若把 NP 短暂耦合到 DTC，可把 NP“播种”成相对原 DTC 同步或反同步的 DTC，并检验噪声下的稳健性。据此提出用三个 DTC 顺序耦合输入/输出位点实现 NAND、NOR；划出逻辑门架构仍成立的参数区，并讨论量子涨落下协议如何受损。

---

### 7. Attraction from repulsion in an interacting Chern band: chiral superconductivity, generalized Hall crystals, and competing fractional Chern insulators
Fabian Pichler · Clemens Kuhlenkamp · Ashvin Vishwanath · Michael Knap · [arXiv:2610.22498](https://arxiv.org/abs/2610.22498) · cond-mat.str-el · new

**为何相关：** 张量网络在可调 Chern 带中看排斥费米子：Jain 序列 FCI 随色散增强过渡到手征 p 波超导，半满出现广义霍尔晶体——分数陈 × 超导竞争。

要点：部分填充 Chern 带强关联实验里，分数陈绝缘体、超导体与拓扑晶体常紧邻出现，微观关系仍不清楚。作者用张量网络研究棋盘格可调拓扑带上排斥无自旋费米子：色散增强时 Jain 序列 FCI 在半满上下都过渡到手征 p 波超导；半满、耦合足够强时则形成霍尔电导量子化且元胞加倍的广义霍尔晶体。出人意料的是，从金属母态出发的弱耦合图像也能抓住中等耦合下有序相的本质——金属涨落经 RPA 产生更长程吸引，可复现配对对称性与库珀对径向形状因子；把该吸引并入 Hartree–Fock 可选出观测到的霍尔晶体。结论是“排斥中由涨落诱导吸引”是共用微观成分，张量网络则确立两有序相与 FCI 的直接竞争。

---

### 8. Chirality-resolved imaging of spin waves with a quantum spin
Enbo Zhang · Tiancheng Zheng · Bo-Yuan Yang · Shreyes Nallan 等 · [arXiv:2610.22867](https://arxiv.org/abs/2610.22867) · cond-mat.mes-hall · new

**为何相关：** 金刚石 NV 激发态两跃迁作手性通道，分辨成像 YIG 中双向 Damon–Eshbach 自旋波；反射反转手性使入射/反射同谱可分——量子传感 × 自旋波。

要点：自旋波把传播方向编码在圆偏振杂散场的手性里，标量磁强计读不到。面内磁化膜 Damon–Eshbach 表面波上方偶极场的旋转手性由传播方向固定。金刚石 NV 是本征偏振分析器：绕 NV 轴的右/左手场分别驱动不同自旋跃迁（基态与激发态皆然）。作者利用落在钇铁石榴石（YIG）自旋波带内的两条激发态跃迁作一对手性通道，双向成像 Damon–Eshbach 波；刻蚀边界反射反转手性，入射与反射在同一谱上成两条线并可分开成像。基态同样规则成立，所选场可驱动 Rabi 振荡，通向磁子对手性选择的 NV 自旋操控。读两个通道即可在单点判定自旋波方向、无需相位参考，推进手性分辨量子传感。

---

### 9. Liouvillian Non-Invertible Symmetry
Ying-Cheng Yang · Jhen-Dong Lin · Yueh-Nan Chen · [arXiv:2610.23111](https://arxiv.org/abs/2610.23111) · quant-ph · new

**为何相关：** 把希尔伯特空间非可逆对偶推广到开放系统的 Liouville 空间对偶；自对偶处 KW 缺陷对 Liouvillian Jordan 块施加动量分辨选择规则——开放系统 × 非可逆对称。

要点：非可逆对称超出群式变换，在量子场论与多体物理中重要，但开放系统仍缺一般框架。作者建立一般 Liouville 空间对偶，把希尔伯特空间非可逆对偶推广到开放系统：缺陷联系具对偶哈密顿与耗散参数的 Liouvillian，自对偶时成为精确对称。应用于周期横场伊辛链加上被 Kramers–Wannier（KW）对偶交换的两条集体 Lindblad 通道：强 ℤ₂ 对称把 Liouville 空间分成四个宇称扇区，缺陷仅在偶–偶扇区非平凡作用。自对偶处 KW 缺陷对 Liouvillian Jordan 块施加动量分辨选择规则——不同 Liouville 动量或缺陷本征值的模不能共处同一例外 Jordan 块。三格点链上全局 Rényi-2 KW 不对称可动力学识别自对偶条件；谱结构同时呈现半单简并与自对偶例外点及扰动选择响应。工作把非可逆对偶延伸到马尔可夫量子动力学。

---

### 10. Physics-Informed Machine Learning for Response Tensors in Crystalline Magnets: Application to Kagome Metals
Yu-Hsuan Lin · Joel E. Moore · [arXiv:2610.22642](https://arxiv.org/abs/2610.22642) · cond-mat.mtrl-sci · new

**为何相关：** 为任意晶体与磁织构构造完整对称不变描述符基，层级稳定的无相关序参量用于 Kagome 反常霍尔电导回归/分类——物理信息机器学习 × 自旋织构响应。

要点：从磁织构预测响应张量是非共线磁体的关键难题；既有描述符多限于一阶多极或简单磁结构。作者为任意晶体结构与磁织构构造完整对称不变描述符基，作为机器学习建模响应张量的可解释特征。改造标准主成分分析，导出层级稳定的无相关序参量：把序参量空间扩到更高阶自旋序时，新增序参量与先前的不相关。框架用于磁性 Kagome 格点反常霍尔电导（AHC）的回归与分类；在 AHC 可由对称不变序参量良好线性回归的体制，平方回归系数按幅度排序服从 Zipf 样幂律 β_r² ∝ r^{-α}。方法系统给出连接磁晶体对称与响应张量的、覆盖各自旋阶的可解释序参量。

---

### 11. Programmable Preparation of Topological Entangled States
M. Javad Zakeri · Alaric Pan · Darren D Hudson · Andrea Blanco-Redondo · [arXiv:2610.22738](https://arxiv.org/abs/2610.22738) · quant-ph · new

**为何相关：** 硅光子拓扑超晶格上反演设计非线性泵浦轮廓，可编程制备拓扑纠缠态并控制维数与模态结构，器件间相关可复现——拓扑光子 × 纠缠制备。

要点：可编程制备纠缠态是可扩展量子信息、网络与光子计算的中心需求。拓扑光子平台用对称保护光模编码，但纠缠态通常由晶格几何决定、缺少可编程性。作者通过对集成光子晶格非线性光学泵浦轮廓的反演工程，演示拓扑纠缠态的可编程制备：在保持拓扑特征的同时，确定性控制生成态的维数与模态结构。实验实现硅光子拓扑超晶格，非线性生成路径本身可经定制激发编程；超晶格承载共局域拓扑界面模的多带流形，相干控制输入在保护基内合成泵浦叠加。展示选择性寻址拓扑双光子本征态、调控关联以得到高维希尔伯特空间目标态，以及反演设计泵浦以生成目标 Schmidt 维数。位点分辨双光子关联在名义相同器件间可复现，显示对纳米加工无序的稳健性。

---
