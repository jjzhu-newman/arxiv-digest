# 10/8 arXiv 兴趣摘要（工作日）

扫了今天（美西 10/8，周四）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。新投稿量：cond-mat 79、quant-ph 64、hep-th 19、math-ph 5（cs.LG 202、stat.ML 27 只看物理/量子相关；交叉与替换未计入）。今天非厄米 Chern、交错磁（磁振子偏振 / CrSb 二维极限 / Landau 推广）和连续空间神经量子态比较扎眼，Floquet 堆叠 SSH 与开放系统数值方法也有好货。按兴趣锚点筛了 **12 篇**（全部为新投稿，未收替换稿）。核对了本地 Zotero 库（只读副本），12 篇都不在库里；交错磁与 CrSb、非厄米 Chern、parafermion/Fibonacci 方向库里已有不少相关文献，相应条目里有标注。

**建议先翻这三篇：**
1. **Non-Hermitian Cooperation Induced Chern Insulator** —— 损耗与非互易耦合协同诱导 Chern 绝缘体与手性边缘态——非厄米 × 拓扑。
2. **Magnon Polarization Textures and Transport in Antiferromagnets and Altermagnets** —— 反铁磁/交错磁中磁振子偏振织构与极端各向异性弛豫——altermagnetism × 自旋电子学。
3. **From continuum neural quantum states to effective lattice models** —— 连续 NQS 基态读出到有效格点模型（莫尔 Wigner 分子）——NNQS × 强关联。

---

### 1. Non-Hermitian Cooperation Induced Chern Insulator
Weiwei Zhu, Bingbing Wang, Mengxiang Xie, Hong-yu Zou 等 · [2610.09413](https://arxiv.org/abs/2610.09413) · quant-ph · new

**为何相关：** 静态晶格不靠磁场或规范场，仅靠 on-site 损耗与非互易耦合的协同就能打开拓扑隙、得到非零陈数手性边缘态——非厄米 × Chern 拓扑。

要点：常规 Chern 绝缘体依赖破缺时间反演的磁场或人工规范场。作者提出另一条路径：静态晶格在没有任何规范场的情况下，只要同时具备格点损耗与非互易耦合，二者协同即可打开拓扑隙并产生稳健手性边缘态、给出非零陈数；任一单独效应都不够。机制上，损耗位点形成非厄米手性“分子”，其动力学主导模携带轨道角动量，绝热消除快衰减自由度后等效产生人工磁通。由此把“非厄米协同”定位为在开放经典/量子体系中、不依赖外场或时间调制即可诱导 Chern 拓扑的通用资源。库里已有“Non-hermitian Chern bands”等，这篇强调损耗与非互易必须联手这一新范式。

---

### 2. Magnon Polarization Textures and Transport in Antiferromagnets and Altermagnets
Konstantin S. Denisov, Igor Žutić · [2610.09035](https://arxiv.org/abs/2610.09035) · cond-mat.other · new

**为何相关：** 系统分析共线反铁磁与交错磁中磁振子偏振织构与输运，预言交错磁中偏振弛豫的极端各向异性——altermagnetism × 磁振子自旋电子学。

要点：反铁磁中的磁振子可呈现子格磁化动力学的完全圆偏振、椭圆偏振与线偏振。作者从理论上梳理共线反铁磁与交错磁在动量空间中的磁振子偏振织构及其输运：偏振织构对动量方向的敏感程度决定两类动力学——Dyakonov–Perel 弛豫，或异步 Larmor 进动引起的退相位。对易轴反铁磁，Néel 矢量平行磁场可抑制磁偶极相互作用诱导的 Dyakonov–Perel 弛豫，并伴随磁振子自旋扩散长度增大及其随温度反常增长；垂直取向则因 Larmor 进动增强圆偏振弛豫。对交错磁或含 Dzyaloshinskii–Moriya 相互作用的反铁磁，则预言磁振子偏振弛豫的极端各向异性。你库里有“Magnon orbital Nernst effect in altermagnets”等磁振子–交错磁条目，可对照。

---

### 3. From continuum neural quantum states to effective lattice models: Fluctuating Wigner molecules in moiré superlattices
Ahmed Khalifa, Shubhayu Chatterjee · [2610.08955](https://arxiv.org/abs/2610.08955) · cond-mat.str-el · new

**为何相关：** 用连续空间神经量子态直接找基态，再读出格点电荷/自旋统计，让有效自由度从微观波函数涌现——NNQS × 莫尔超晶格。

要点：当动能、晶格势与相互作用竞争、能标分离失效时，既不知道微观态也不知道有效描述。连续空间神经量子态（NQS）可不预设能带/轨道/自旋直接求基态，但微观波函数难用有效变量解读。作者引入波函数读出，把连续 NQS 映射到格点分辨的电荷与自旋统计，使有效自由度从微观解中涌现。以填充 ν=3 的莫尔过渡金属硫族化合物为例，NQS 给出低自旋基态，低于自旋极化 Wigner 分子铁磁晶体；电荷密度虽保留三角分子图案，读出却显示经由束缚近邻 doublon–hole 对的显著电荷涨落。每个分子电荷态有惰性自旋单态核，边缘电子携带自旋，电荷与自旋涨落纠缠，并呈现格点间反铁磁自旋关联，从而动机化为带自旋的双轨道 Hubbard 模型。总体给出“从连续波函数到有效格点模型”的一条路线。库里几乎没有 neural quantum state 相关条目，这篇值得收。

---

### 4. Correspondence between Asymptotic Quantum Many-Body Scars in Closed Systems and Diffusive Nambu-Goldstone Modes in Open Systems
Masaya Kunimi, Taiki Haga, Masaya Nakagawa · [2610.09662](https://arxiv.org/abs/2610.09662) · cond-mat.stat-mech · new

**为何相关：** 把封闭系统中彩虹量子多体疤痕与开放系统中强到弱对称破缺下的扩散 Nambu–Goldstone 模建立谱对应——开放系统 × 弱遍历破缺。

要点：开放量子多体系统的流体力学弛豫可用与强到弱自发对称破缺（SWSSB）相联系的扩散 Nambu–Goldstone 模理解。作者找到封闭系统弱遍历破缺与开放系统扩散流体力学的共同结构：建立彩虹量子多体疤痕（RQMBS）母哈密顿量与具有强 U(1) 对称及局域电荷退相位 Lindblad 算符的强耗散开放系统有效 Lindbladian 之间的谱对应。对广泛的自旋、费米与玻色系统构造渐近 RQMBS，在扩大疤痕子空间内母哈密顿量具有局域 Rokhsar–Kivelson 型无阻挫分解；单模变分给出最低激发 O(k²) 上界。矢量化下 RQMBS 映射为固定电荷扇区的无穷温度极大混合态，并在有限密度下呈现长程 SWSSB 序。均匀跃迁率时两算符成比例、本征模重合，从而精确二次母哈密顿量分支直接映射为扩散 NG 模。

---

### 5. Landau Theory for Non-relativistic Magnetism Beyond Altermagnetism
Hana Schiff, Judit Romhányi, Paul McClarty, Jeffrey G. Rau · [2610.10523](https://arxiv.org/abs/2610.10523) · cond-mat.str-el · new

**为何相关：** 把非相对论磁体的唯象 Landau 理论从共线推广到共面/非共面序，并显式连到自旋空间群与原子交错磁——altermagnetism 理论框架。

要点：作者将非相对论磁系统的唯象 Landau 理论从共线情形推广到共面与非共面序，聚焦由晶体点群单一不可约表示描述的 k=0 磁序，对所有可能的多维不可约序参量通道构造到四次项的对称允许自由能，并区分四方、三角/六方与立方对称下的不同 Landau 理论。类似自旋向列流体，自然结果要么塌缩为低对称共线相，要么形成自旋空间中相互正交的真正共面/非共面序（令人联想到 ³He 的 A/B 相）。该对称破缺相实现与序参量空间表示相联系、且与顺磁母空间群相同的自旋空间群，从而直接桥接 Landau 与自旋空间群路径。作者用该框架计算净磁化、自旋电导、多极矩与压磁等观测量，并讨论低对称共线相与通常共线自旋群、原子交错磁、超流 ³He 与电子向列相的联系。库里有“Landau theory of altermagnetism”(2024)，这篇是向共面/非共面的自然延伸。

---

### 6. Construction-Dependent Floquet Topology in Circularly Driven $N$-Stacked Su-Schrieffer-Heeger Chains
Aayushi Agrawal, Jayendra N. Bandyopadhyay · [2610.09925](https://arxiv.org/abs/2610.09925) · cond-mat.mes-hall · new

**为何相关：** 静态极限下幺正等价的两种 SSH 堆叠构造，在圆偏振驱动下因 Peierls 相位不同而给出截然不同的 Floquet 拓扑——Floquet × 拓扑。

要点：作者研究由 SSH 链堆叠形成的二维晶格中依赖构造的 Floquet 拓扑。解耦链极限下两种构造：I 中组成 SSH 链为绕数 w=0 的平凡相，II 中为 w=1 的非平凡相。二者在静态极限幺正等价，但圆偏振驱动会区分它们，因为变换所关联的跳跃过程对应于不同物理键矢、因而获得不同 Peierls 相位。用 Floquet–Sambe 形式得到准能谱与以低带陈数 C_L、定向 Zak 相表示的相图，包括低频下 C_L=−3、−4 等相。由于陈数不能分别分辨两个准能隙的拓扑，作者进一步计算动力学绕数 W₀、W_π 并验证手性边缘态：在相同驱动参数下两种构造可有相同 C_L=−2，但隙分辨绕数分别为 (0,+2) 与 (−2,0)。时间平均光学霍尔电导的直流值由 C_L e²/h 决定。结论是组成链的物理构造虽不影响静态体谱，却可决定 Floquet 拓扑结构。

---

### 7. Coherent consensus for the estimation and classification of phases
Roberto Ruiz, Alessandro Luongo, Sergi Ramos-Calderer, José Ignacio Latorre · [2610.09865](https://arxiv.org/abs/2610.09865) · quant-ph · new

**为何相关：** 用 GHZ 态把多个独立量子分类器的相位相干汇总，相对多数表决把采样误差压低 √n——量子计量启发的 QML × 机内传感。

要点：受量子计量启发，作者提出“相干共识”原语以增强独立量子分类器在决策边界处的协作表现：在 n 个量子比特上制备 GHZ 态，把每个分类器输出编码为相对相位，再撤销 GHZ 制备把相位汇集到第一比特。信号放大 n 倍，相对非相干多数表决把采样误差压低 √n。该原语适用于一般相位估计与分类；作者给出相对多数表决的资源保证，并在离子阱量子计算机上用一组不完美相位门实现，观察到相干共识预期的 √n 精度增益（最大 n 处多余色散与器件漂移一致）。作者把相干共识理解为“量子计算机内部的传感”。

---

### 8. Numerically exact simulation of open quantum networks with strong system-bath couplings using tensor network path integrals
Quentin W. Richter, Moritz Cygorek · [2610.10259](https://arxiv.org/abs/2610.10259) · quant-ph · new

**为何相关：** 提出 CTEMPO 张量网络路径积分方案，在强系统–浴耦合下仍保持小键维，并求解 7 位点 FMO 等非马尔可夫网络——开放系统数值方法。

要点：非马尔可夫开放量子网络同时承受多体状态空间指数膨胀与结构化环境强耦合带来的长记忆。既有 TEMPO/过程张量等方法在强耦合时键维过大。作者设计 CTEMPO 方案，使单点问题键维特别小，再推广为演化对应 comb 张量网络以模拟非马尔可夫量子网络。自旋–玻色模型基准显示相对既有方法有数量级改进；多点算法求解谱密度含 62 个峰的 7 位点 Fenna–Matthews–Olson 光合复合体这一著名难题，并用于探索各自耦合超欧姆声子浴的至多 N=20 量子点超辐射标度。该方法可作为非马尔可夫量子网络的“即用”方案，并兼容更一般张量网络拓扑。库里有 HEOM 等开放系统数值综述，可作方法对照。

---

### 9. Vanishing Altermagnetism and Emergent Ferromagnetism at the Two-Dimensional Limit of CrSb
Yunlong Liu, Zixuan Wu, Qinxi Liu, Yupeng Zhi 等 · [2610.09664](https://arxiv.org/abs/2610.09664) · cond-mat.mtrl-sci · new

**为何相关：** 分子束外延生长双层极限 CrSb，发现一层双层室温铁磁、两层磁性消失，相对体相交错磁出现维度诱导的磁序转变——altermagnetism 二维极限。

要点：交错磁把自旋劈裂电子态与零净磁化结合，但维数降低如何重塑其磁序仍不清楚。作者在 SrTiO₃(001) 上用分子束外延直接生长双层厚度的 CrSb(0001) 薄膜，发现意外的厚度依赖磁转变：一层双层膜呈现室温铁磁与强垂直磁各向异性，两层双层膜铁磁消失，与体相 CrSb 的交错磁基态形成鲜明对照。第一性原理计算表明暴露的 Cr 表面引起轨道重排，增强层内铁磁交换并压制竞争的层间反铁磁耦合，从而驱动从交错磁到铁磁的维度交叉。由此把维数与表面终止定位为调控磁序的有力旋钮。你库里有多篇 CrSb 交错磁条目（含外延薄膜能带劈裂、Néel 矢量依赖反常输运等），这篇补上二维极限的实验图景。

---

### 10. Zero Mode Operators and Charge-Conjugation Defects in Non-Abelian Fractional Quantum Hall-Superconductor Heterostructures
Junyi Cao, Eduardo Fradkin · [2610.08907](https://arxiv.org/abs/2610.08907) · cond-mat.str-el · new

**为何相关：** 把非阿贝尔分数量子霍尔–超导异质结中电荷共轭缺陷束缚零模的局域算符代数一般化，覆盖 parafermion 与 Fibonacci 结构——拓扑序 × 任意子缺陷。

要点：作者研究由阿贝尔与非阿贝尔分数量子霍尔态构筑的 FQH–超导异质结中束缚于电荷共轭缺陷的零模。虽可用 G-交叉辫子张量范畴描述缺陷，局域算符刻画通常未知。作者把束缚零模算符的体–边构造推广到非阿贝尔母拓扑序，将折叠理论中的体 Wilson 算符映射为一维 FQH–SC 理论中的局域零模算符，区分零模任意子与作用于缺陷希尔伯特空间的局域零模算符，并给出广义零模代数；同时决定隧穿的熔合通道依赖。应用上恢复填充 ν=1/m 费米 Laughlin FQH–SC 的 Z_{2m} parafermion 零模结构，得到广义 Moore–Read 的 Z₂⁽ⁿ⁾×Z_N 结构，以及 k=3 Read–Rezayi 的 Fib×Z_N 结构；在 Read–Rezayi 情形，零模算符隧穿与直接零模任意子转移在中性熔合通道间给出不同普适振幅比。库里有若干 Z_N/Z₃ parafermion 与 Fibonacci 任意子条目，可作背景。

---

### 11. Characterizing Fermionic Non-Gaussianity in the Sachdev-Ye-Kitaev Model via Replica Twist Entropy
Ning Sun, Pengfei Zhang · [2610.10123](https://arxiv.org/abs/2610.10123) · quant-ph · new

**为何相关：** 用可调角度的副本扭转熵刻画费米子非高斯性，并在大 N SYK 热场双态动力学中画出新的动力学相图——纠缠资源 × SYK。

要点：在费米子系统中，非高斯性是纠缠之外刻画相对自由费米态偏离的重要量子资源。作者提出用副本扭转熵（副本旋转算符期望值，角度 α 可调）作为纯费米态非高斯性的自然探针，先给出典型多体态行为，再建立大 N 可解 SYK 模型中的一般分析框架。应用于热场双态动力学，在 α–演化时间 t 参数空间中揭示新的动力学相图：在 α=π/4 处出现自发 Z₂ 对称破缺，长时间区段对 α 呈现普适尖点。工作为强关联费米系统中的非高斯性研究铺路，并揭示由非高斯性探针标定的一类动力学转变。

---

### 12. Magnetic Order from First-Principles Linear Response
Yaroslav Zhumagulov, Emiliano Cruz-Aranda, Denis Kochan, Oleg V. Yazyev · [2610.10412](https://arxiv.org/abs/2610.10412) · cond-mat.mtrl-sci · new

**为何相关：** 从顺磁态自洽磁化响应的主导本征模直接读出序波矢与磁矩图案，无需预设候选构型，并在交错磁候选 KV₂Se₂O 等上验证——第一性原理磁序搜索。

要点：材料磁序通常靠比较试探自旋构型能量来预言，既无法触及候选集之外的序，也随磁位点数迅速不可行。作者表明可直接从顺磁态识别：在原胞内任意波矢并计入自旋–轨道耦合，自洽磁化响应的主导本征模同时给出序波矢与磁矩图案，无需候选构型。在无先验假设下，方法正确再现交错磁候选 KV₂Se₂O 的 G 型堆叠与面外磁矩、Cu₂OSeO₃ 的 3:1 亚铁磁四面体，以及单层 NiI₂ 的非公度螺旋不稳定性。由此把顺磁态响应确立为无偏预测磁序、系统搜索复杂磁体的路径。
