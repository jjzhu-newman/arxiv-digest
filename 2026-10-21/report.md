# 10/21 arXiv 兴趣摘要（工作日）

扫了今天（美西 10/21，周三）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Wednesday, 21 October 2026**；新投稿：cond-mat 96、quant-ph 65、hep-th 28、math-ph 9、cs.LG 134、stat.ML 16（交叉与替换未计入）。已排除 10 月已荐的 150 篇。交错磁一侧有推广自旋群对含 SOC 磁子输运的对称分类，以及 d 波交错磁量子环的相干自旋滤波；Floquet 有几何 Floquet 基态序与 MPS 算法，以及 Weyl 中 OAM 驱动的局域 Floquet 涡旋态；非厄米/开放有 SSH 杂质重布拓扑临界、截断 Wigner 开放自旋长程序，以及紧凑 dressed 哈密顿量强耦合动力学；另有任意子凝聚相变场论、真实材料 DMFT 变分量子杂质求解、层赝自旋量子几何与三维 Chern 矢量集体霍尔。按兴趣锚点筛了 **11 篇**（全部为新投稿；未收替换稿；跳过气象/ECG/地震 PINN、文本图像奖励模型、卫星式纠缠组网调度、AdS/规范全息等假阳性）。本地桌面当时未在线，**未做 Zotero 核对**。

**建议先翻这三篇：**
1. **Floquet ground state order** —— 几何 Floquet 理论给出平均能量算符基态上的稳定量子序（异于预热），并发展 MPS 变分算法，在 >100 自旋非可积驱动链见能隙、面积律纠缠的 Floquet 基态与时间晶体序——Floquet × 张量网络 × 多体非平衡。
2. **Generalized Spin Groups and Applications to Magnons** —— 把含 SOC 的 DM/Gamma/单离子各向异性纳入推广自旋群对称分类（6 个自旋-only + 161 个非平凡自旋群），并用于磁子热导与自旋电导张量；文中明确覆盖交错磁中的相对论磁子输运——altermagnetism × 磁子拓扑/自旋电子学对称。
3. **Ballistic transport and crystallographic control in altermagnetic quantum rings** —— 有限宽 d 波交错磁量子环的相干双端输运：Aharonov–Bohm 精确 h/e 周期与半磁通透射零点，晶轴旋转翻转透射自旋，亚特斯拉场可达 |P_T|>0.99——altermagnetism × 介观干涉自旋滤波。

---

### 1. Floquet ground state order
Suman Mondal · Paul M. Schindler · Marin Bukov · [arXiv:2610.28336](https://arxiv.org/abs/2610.28336) · quant-ph · new

**为何相关：** 几何 Floquet 理论给出平均能量算符基态上的稳定量子序（异于预热），并发展 MPS 变分算法，在 >100 自旋非可积驱动链见能隙、面积律纠缠的 Floquet 基态与时间晶体序——Floquet × 张量网络 × 多体非平衡。

要点：干净相互作用周期驱动系统通常热化到无特征无穷高温态，难以形成稳定有序。作者将演化分解为几何与平均能量动力学，用几何 Floquet 理论定义 Floquet 基态，并导出可计算大体系 Floquet 基态的变分原理与矩阵乘积态算法。在百自旋以上非可积驱动链中，数值给出扩展参数区内有能隙、面积律纠缠的 Floquet 基态：既可承载修饰后的平衡序（如 Floquet 反铁磁），也可承载固有非平衡序（如基态时间晶体）。该序由有限平均能量能隙保护，能隙闭合对应相变。作者把 Floquet 物态拆为平衡与非平衡要素：固定时刻的 Floquet 基态属平衡相，非平衡内容全由驱动的几何 holonomy 产生；并指出准局域反绝热驱动可抑制加热，论证 Floquet 基态何以规避本征态热化假说。

---

### 2. Generalized Spin Groups and Applications to Magnons
Xinhai Tu · Di Wang · Yuxuan Mu · Xiangang Wan · [arXiv:2610.28024](https://arxiv.org/abs/2610.28024) · cond-mat.other · new

**为何相关：** 把含 SOC 的 DM/Gamma/单离子各向异性纳入推广自旋群对称分类（6 个自旋-only + 161 个非平凡自旋群），并用于磁子热导与自旋电导张量；文中明确覆盖交错磁中的相对论磁子输运——altermagnetism × 磁子拓扑/自旋电子学对称。

要点：自旋群是各向同性 Heisenberg 模型中自旋与晶格可分离时的自然对称框架，已广泛用于电子能带、磁子带拓扑与输运。真实磁子哈密顿量还含自旋轨道耦合诱导的各向异性项（DM、Gamma、单离子各向异性），并出现于交错磁的相对论磁子输运；这类体系常被简化为常规磁群描述。作者系统建立面向磁子的推广自旋群：先分类 Heisenberg/DM/Gamma/SIA 对称性，得到 6 个自旋-only 群与共 161 个非平凡自旋群；磁有序相的对称性再由自旋哈密顿量母群自发破缺得到，并枚举有序态下的大量非平凡自旋群。最后将框架用于磁子热导与自旋电导张量，给出全部对称允许形式，统一有无 SOC 情形下的磁子响应约束。

---

### 3. Ballistic transport and crystallographic control in altermagnetic quantum rings
Edilberto O. Silva · [arXiv:2610.27173](https://arxiv.org/abs/2610.27173) · cond-mat.mes-hall · new

**为何相关：** 有限宽 d 波交错磁量子环的相干双端输运：Aharonov–Bohm 精确 h/e 周期与半磁通透射零点，晶轴旋转翻转透射自旋，亚特斯拉场可达 |P_T|>0.99——altermagnetism × 介观干涉自旋滤波。

要点：作者研究非磁导线耦合的有限宽 d 波交错磁量子环相干输运。受限 Aharonov–Bohm 磁通保持精确 h/e 周期；对称单模几何下给出精确半磁通透射零点。垂直场按有效面积移动干涉图案，交错磁劈裂把共同零点拆成自旋依赖节点。旋转晶体取向可翻转透射自旋，而 θ_A=π/4 镜面取向精确自旋简并。对 50 nm 参考环，亚特斯拉场即可给出 |P_T|>0.99 窗口，其中最易实现的仅需均匀场、无需受限磁通。有限偏压、温度、无序、Zeeman 与自旋守恒电压探针计算表明，极化度比单个相干共振振幅更稳健。结果把干涉节点位置、磁通周期与晶控自旋极化标为交错磁介观干涉仪的可用实验指纹。

---

### 4. Steering of topological criticality in the Su-Schrieffer-Heeger chain via non-Hermitian substitutional impurities
Juan A. Cañas · Guo-Qing Zhang · A. Martín-Ruiz · [arXiv:2610.27436](https://arxiv.org/abs/2610.27436) · cond-mat.mes-hall · new

**为何相关：** 有限浓度非厄米替位杂质通过打破非互易跃迁内部对称，确定性地宏观平移 SSH 拓扑临界点，并可扩展/压缩拓扑相；伴随实→复谱跃迁与非厄米趋肤效应——非厄米 × 拓扑临界。

要点：作者研究一维 SSH 链在有限浓度非厄米替位杂质下的拓扑相。核心机制是：引入位点依赖的非互易胞内/胞间跃迁后，打破杂质非互易跃迁的内部结构对称，可把临界点做定向宏观位移，从而仅靠局域缺陷不对称就能受控扩展或压缩拓扑相区。有限尺寸标度给出关联长度临界指数 ν≈1.455（对称）与 ν≈1.397（不对称），确认偏离纯净 SSH 普适类，且高缺陷密度下指数发散。文中还报告杂质诱导的实→复谱跃迁，并由非厄米趋肤效应几何刻画。结论是孤立非厄米不对称可协同、确定性地平移宏观拓扑保护边界。

---

### 5. Systematic Truncated Wigner Approximation for Open Spin Systems Reveals Long-Range Order Far from Equilibrium
Igor Timofeev · Dawid A. Hryniuk · Marzena H. Szymańska · [arXiv:2610.27462](https://arxiv.org/abs/2610.27462) · quant-ph · new

**为何相关：** 由 Lindblad 方程的精确 Stratonovich–Weyl 演化系统导出连续 SU(2) 协变截断 Wigner 框架，可处理任意自旋 S 的开放自旋系统，并在 400 格点二维耗散各向异性 XY 中揭示远离平衡长程序——开放系统 × 非平衡多体。

要点：长程相互作用可保护耗散序免受涨落破坏，但二维何时成立对既有多体方法仍困难。作者发展连续 SU(2) 协变截断 Wigner 框架：把问题映射为每格点一个 Bloch 球的随机动力学；由 Lindblad 方程的精确 Stratonovich–Weyl 演化系统导出，为任意自旋 S 同时生成漂移与库噪声。相对精确对角化与张量网络基准，该方法能可靠描述非平衡动力学与稳态。应用于 400 格点二维耗散各向异性 XY 晶格，揭示远离平衡的长程序何时被长程相互作用保护。

---

### 6. Dynamical Mean-Field Theory for Real Materials using Variational Quantum Compressed Time Evolution on a Quantum Computer
Stefan Wolf · Johannes Selisko · Timo Eckstein 等 · [arXiv:2610.28231](https://arxiv.org/abs/2610.28231) · quant-ph · new

**为何相关：** DFT+DMFT 杂化流程用变分量子压缩时间演化作杂质求解器，在 IBM Heron 上算 CaCuO₂ 时域 Green 函数并提取态密度特征；自洽精度仍超现有 NISQ——量子 ML/变分量子 × 强关联材料。

要点：作者设计面向真实材料的杂化量子–经典流程：结合 DFT 与动力学平均场，用基于变分量子压缩时间演化的量子算法作杂质求解器，在 IBM Heron 器件上计算时依赖 Green 函数。借助误差缓解与 Lehmann 表象拟合，从可及时间窗口提取态密度，并成功分辨谱函数特征峰。然而达到完整 DMFT 自洽所需数值精度仍超出当前硬件能力，表明实用材料级 DMFT 应用仍有待后 NISQ 硬件。

---

### 7. Field theories and critical excitations at anyon condensation transitions
Luisa Eck · Xie Chen · [arXiv:2610.28148](https://arxiv.org/abs/2610.28148) · cond-mat.str-el · new

**为何相关：** 从母拓扑序与凝聚子范畴数据出发，给出任意子凝聚相变的两类互补刻画：适配 SymTFT 的 2+1D Ginzburg–Landau 构造，以及连续转变上哪些点/环激发临界的判据——任意子凝聚 × 拓扑相变。

要点：任意子凝聚相变（尤其非阿贝尔）仍难刻画。作者提出两套互补方案，从母拓扑序与凝聚子的范畴数据提取转变信息。其一把 SymTFT 设定下 1+1D 的 Ginzburg–Landau 程序推广到 2+1D 任意子凝聚，适用于凝聚任意子具有整数量子维数的情形。其二给出连续转变上临界点/环激发的判据：先确定哪些任意子环在全程保持凝聚，其余环变临界；点激发若与每个凝聚环编织平凡则亦临界。文中在若干阿贝尔与非阿贝尔例子上演示两套方案。

---

### 8. Capturing Open Quantum System Dynamics with Compact Dressed Hamiltonians
Zachary Giles · Dvira Segal · [arXiv:2610.28358](https://arxiv.org/abs/2610.28358) · quant-ph · new

**为何相关：** 反应坐标 + 极化子变换后再截断集体玻色模的紧凑 dressed 哈密顿量，以更小 Hilbert 空间逼近强耦合结构库动力学，并可直接读 Liouvillian 谱与慢模——开放系统 × 强耦合主方程。

要点：作者推进紧凑 dressed 哈密顿量（CDH）框架，用于强耦合结构玻色环境中的开放系统动力学。先做反应坐标映射与极化子变换，把强系统–环境杂化纳入 dressed 表象，再截断集体玻色模，从而用远少于原表象的态数捕获动力学；残余环境用弱耦合马尔可夫主方程处理。对单自旋、耦合自旋与自旋系综的自旋–玻色型模型，在共振/失谐与弱到强耦合下与 HEOM 及收敛反应坐标结果对比，显示 CDH 能系统逼近振荡频率、弛豫与长时间布居，并捕获库介导相互作用、自旋同步与集体发射迹象。此外可直接访问 Liouvillian 谱与本征模，慢动力学模在 CDH 中收敛快，便于不依赖拟合时间观测量即识别弛豫时标。

---

### 9. Orbital-angular-momentum control of localized Floquet states and photocurrents in Weyl semimetals
Kyle S. Netherwood · Juan I. Aranzadi · Nils Jacobsen 等 · [arXiv:2610.28396](https://arxiv.org/abs/2610.28396) · cond-mat.mes-hall · new

**为何相关：** 涡旋光束的轨道角动量在 Weyl 半金属中产生高度局域的 Floquet 涡旋态与环流光电流；连续 BdG 径向方程与 Wilson 格点计算一致支持 OAM 作为局域载流态的可调旋钮——Floquet × 拓扑 Weyl × 结构光。

要点：结构光不仅可通过偏振、还可通过空间剖面与轨道角动量（OAM）调控量子材料。作者建立涡旋光束驱动 Weyl 半金属的实空间理论，表明光学 OAM 可生成高度局域的 Floquet 涡旋态并伴强环流光电流。利用柱对称导出类似 BdG 的径向方程，按角动量分辨态并追踪其在光修饰 Weyl 锥之间的演化；对 Laguerre–Gaussian 束，空间变化驱动导致局域涡旋态与体态强杂化。Wilson 格点表述保留完整二维空间结构，可直接算局域光电流：两方法一致确认束轴附近的 OAM 诱导涡旋态，且低角动量、最局域涡旋模携带显著强于扩展表面态的环流电流密度。

---

### 10. Zeeman Quantum Geometry of the Layer Pseudo-spin
Bingxuan Jiang · Shihao Zhang · [arXiv:2610.26982](https://arxiv.org/abs/2610.26982) · cond-mat.mes-hall · new

**为何相关：** 定义层赝自旋的量子几何（带间 Berry 联络与层矩阵元混合张量），给出与普通自旋不同的选择定则；扭曲双层 MoTe₂ 上量化局域偶极调制与整流/螺旋/三次谐波净响应——量子几何 × 莫尔层自由度。

要点：位置依赖层间隧穿耦合的二维层可把层赝自旋极化当作可控内禀自由度。作者引入该层赝自旋的量子几何：由带间 Berry 联络与层矩阵元构成的混合张量，支配对振荡面内电场的响应。因层赝自旋在三重旋转下是 Ising 型标量不变量，其选择定则不同于赝矢量自旋。最小两带模型中层赝自旋量子度规与 Zeeman–Berry 曲率非零，但布里渊区积分消失；故面内驱动在线性阶不改变空间平均极化，却印上可被层分辨隧穿成像的莫尔周期胞内图案。对扭曲双层 MoTe₂，文中量化局域偶极调制，并指出更高阶出现净响应的整流、螺旋奇与三次谐波通道。

---

### 11. Collective Hall quantization in 3D Chern vector systems
Zhi-Qiang Zhang · Shuguang Cheng · Hongfang Liu 等 · [arXiv:2610.27802](https://arxiv.org/abs/2610.27802) · cond-mat.mes-hall · new

**为何相关：** 预测由 Chern 矢量 C=(0,m,n) 保护的三维量子霍尔：全局拓扑强制 mL_y+nL_z 集体量子化，霍尔电导 G_xy=±(mL_y+nL_z)e²/h——三维 Chern 矢量拓扑 × 量子霍尔。

要点：三维量子霍尔由 Chern 矢量而非单一陈数刻画；以往量子化输运多讨论仅一个非零分量的特殊情形，更一般 Chern 矢量态如何保护量子化仍是问题。作者预言由 C=(0,m,n) 保护的三维量子霍尔效应：对尺寸 L_y、L_z 的样品，全局拓扑强制 mL_y+nL_z 集体量子化，尽管单个边缘模对无序脆弱。这表明稳健量子化可作为统一手性网络的整体性质出现。集体响应表现为霍尔电导 G_xy=±(mL_y+nL_z)e²/h，同时依赖 Chern 矢量分量与样品尺寸；并讨论候选材料以利实验观测。
