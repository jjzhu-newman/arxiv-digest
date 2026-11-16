# 11/04 arXiv 兴趣摘要（工作日）

扫了今天（美西 11/04，周三）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Wednesday, 4 November 2026**；新投稿：cond-mat 100、quant-ph 68、hep-th 35、math-ph 11、cs.LG 148、stat.ML 9（交叉与替换未计入）。已排除此前已荐的 336 篇。主题上 Floquet/开放系统（浴耦合 Floquet 拓扑边缘的非线性抑耗散、Liouvillian Kramers 简并、同步 Mpemba、级联 vdP 量子传感）、交错磁（诱导高阶拓扑 Dirac 半金属、AM–TI 无场横向响应）与纠缠/NNQS（相干误差驱动长程纠缠临界、LaQX 工具库、Kagome Dirac 自旋液 NNQS）较集中；另有 PINN 学量子门与手性极限下量子度规的对称隔离。按兴趣锚点筛了 **11 篇**（全部为新投稿；未收替换稿；跳过假阳性如超声 Westervelt PINN、Mori–Zwanzig 生成式降阶 SciML、成分–结构推交换积分的宽泛材料 ML、纯 VO₂ 自旋波器件、石墨烯 VQA 能带演示、黑洞/生物/软物质与弱相关通用算子等）。本日用户机 Zotero（DESKTOP-00O6NSD）离线，仅对缓存的 arXiv ID 列表（187，约 10/30）做只读核对：**短名单无同 ID**；主题近邻未逐条标注。

**建议先翻这三篇：**
1. **Nonlinearity-Induced Suppression of Dissipation in Bath-Coupled Floquet Topological Insulators** —— 激光写入 Floquet 拓扑绝缘体周期耦合光子浴时，适度非线性因模混增强耗散，但最优强度下局域边缘孤子可显著抑制手性边缘输运耗散——Floquet × 开放系统 × 非线性控耗散。
2. **Altermagnetism-induced higher-order topological Dirac semimetals in two-dimensional nonsymmorphic systems** —— 三层非对称 Dirac 体系中外层 d 波交错磁序打开螺旋边缘态，仅保留高对称点 M 的对称保护 Dirac 交叉，并产生角态——交错磁诱导二维高阶拓扑 Dirac 半金属。
3. **Long-range entangled criticality from coherent errors** —— 相干误差可把干净表面码相推入扩展的长程纠缠临界区（Markov 长度发散）；并给出保高阶对称与非零相干信息时混合态长程纠缠的一般判据——纠缠 × 拓扑码 × 开放噪声。

---

### 1. Nonlinearity-Induced Suppression of Dissipation in Bath-Coupled Floquet Topological Insulators
Bhoomija Chaurasia · Sebabrata Mukherjee · [arXiv:2611.04752](https://arxiv.org/abs/2611.04752) · cond-mat.mes-hall · new

**为何相关：** 激光写入 Floquet 拓扑绝缘体周期耦合光子浴时，适度非线性因模混增强耗散，但最优强度下局域边缘孤子可显著抑制手性边缘输运耗散——Floquet × 开放系统 × 非线性控耗散。

要点：拓扑绝缘体的手性边缘态耦合外浴时会耗散能量。作者在激光写入、周期耦合光子浴的 Floquet 拓扑绝缘体中表明：非线性相互作用可全光调控边缘态耗散——中等非线性因模混增强耗散，而把非线性强度提到最优值后，高度局域的行进边缘孤子会大幅抑制耗散。工作把可工程的系统–浴耦合与非线性确立为抑制手性拓扑边缘输运耗散的路径。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 2. Altermagnetism-induced higher-order topological Dirac semimetals in two-dimensional nonsymmorphic systems
Lizhou Liu · Cheng-Ming Miao · Ying-Tao Zhang 等 · [arXiv:2611.04347](https://arxiv.org/abs/2611.04347) · cond-mat.mes-hall · new

**为何相关：** 三层非对称 Dirac 体系中外层 d 波交错磁序打开螺旋边缘态，仅保留高对称点 M 的对称保护 Dirac 交叉，并产生角态——交错磁诱导二维高阶拓扑 Dirac 半金属。

要点：作者提出以交错磁实现二维高阶拓扑 Dirac 半金属的路径：三层非对称 Dirac 系统中层间杂化保留体 Dirac 交叉并产生螺旋边缘态；外层 d 波交错磁序打开螺旋边缘，仅高对称点 M 的对称保护 Dirac 交叉保持无隙，从而得到存活的体 Dirac 点、有隙边缘谱与角态。精确的层–空间分解表明，这些特征来自无隙 Dirac 扇区与有隙 ℤ₂ 拓扑扇区的共存。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 3. Long-range entangled criticality from coherent errors
Amir-Reza Negari · Subhayan Sahu · Jan Behrends 等 · [arXiv:2611.03811](https://arxiv.org/abs/2611.03811) · quant-ph · new

**为何相关：** 相干误差可把干净表面码相推入扩展的长程纠缠临界区（Markov 长度发散）；并给出保高阶对称与非零相干信息时混合态长程纠缠的一般判据——纠缠 × 拓扑码 × 开放噪声。

要点：作者发现相干误差可诱导从干净表面码相到扩展长程纠缠临界区的转变，伴随发散的 Markov 长度。为此建立两条一般结果：一是把拓扑与量子信息联系到混合态纠缠——作用于拓扑码的噪声若保高阶对称且相干信息非零，则对通逻辑输入噪声态长程纠缠；二是把基于有限 Markov 长度的局域恢复构造推广到任意局域参数化族，涵盖局域 Lindblad 演化、相干误差后综合征退相干以及热态。应用于蜂窝表面码，得到量子临界的扩展长程纠缠区。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 4. LaQX: A JAX Toolkit for Neural Quantum State Simulations of Lattice Quantum Many-Body Models
Yuntian Gu · Chaohui Fan · Ruichen Li 等 · [arXiv:2611.04333](https://arxiv.org/abs/2611.04333) · cond-mat.str-el · new

**为何相关：** 基于 JAX 的开源神经量子态库 LaQX，统一哈密顿、采样、优化与加速器并行接口，并支持激发态、GFMC、绝热与实时 t-VMC——NNQS × 格点强关联工具链。

要点：神经量子态可为相互作用格点费米子与自旋提供高精度变分表示，但新 ansatz 落地需要哈密顿、采样、优化、观测量与加速器并行的协调实现。作者发布基于 JAX 的开源库 LaQX：通过统一函数接口组织上述组件；除基态变分蒙特卡洛外，支持激发态、Green 函数蒙特卡洛精修、绝热演化与含时变分蒙特卡洛。库汇集 Hubbard 与阻挫磁体等高精度 NNQS 研究中的方法，并已用于三角格子等问题的研究。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 5. Liouvillian Kramers Degeneracy
Kohei Kawabata · [arXiv:2611.03881](https://arxiv.org/abs/2611.03881) · cond-mat.mes-hall · new

**为何相关：** 时间反演†与宇称共同作用可在 Liouvillian 上强制 Kramers 简并，并给出对称分解多体耗散模型中辛类非厄米随机矩阵谱统计——开放系统 × Liouvillian 对称类。

要点：Kramers 定理保证半整数自旋、时间反演不变哈密顿量的谱简并；但有人认为作用于混合态的 Liouvillian 因 Hilbert 空间双结构而不具该简并。作者证明：时间反演对称†与宇称的共同作用可强制 Liouvillian 的 Kramers 简并，并显式构造展现该简并的相互作用费米子与自旋耗散多体模型；其复谱统计遵循对应辛对称类的非厄米随机矩阵。三类基本非厄米随机矩阵普适类中，辛类此前从未在对称分辨的多体 Liouvillian 中实现——本文给出显式实现与非可积性的谱指纹。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 6. Field-free transverse response in altermagnet and topological insulator heterojunctions
Bijay Kumar Sahoo · Abhiram Soori · [arXiv:2611.04937](https://arxiv.org/abs/2611.04937) · cond-mat.mes-hall · new

**为何相关：** AM–TI–AM 异质结在无外场下出现横向微分电导，并对 Néel 矢量取向与化学势对称性敏感——交错磁 × 拓扑绝缘体界面 × 无场自旋电子学。

要点：作者理论研究拓扑绝缘体夹在二维交错磁电极之间、无外磁场时的输运。利用交错磁内禀破时间反演，报告 AM–TI–AM 异质结中的无场横向微分电导：当 Néel 矢量有面外分量时横向响应有限；对称化学势下面内取向（θ=π/2）因 k_y 与 −k_y 通道对称恢复而严格消失；化学势不对称时可打破该对称，使面内 Néel 亦给出有限横向响应。纵向电导随 TI 化学势呈 Fabry–Pérot 振荡，横向呈反对称依赖；空间上横向电流贡献在 TI 区内指数衰减。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 7. High-fidelity quantum gate learning via physics-informed neural networks
Luis Fabra · Cristian E. Susa · Alcides Montoya 等 · [arXiv:2611.03851](https://arxiv.org/abs/2611.03851) · quant-ph · new

**为何相关：** 以含时薛定谔方程训练 PINN，在固定边界光滑控制场下学习单/双比特高保真量子门（Hadamard、CNOT），并用 Haar 随机态与平均门保真度独立验证——PINN × 量子控制。

要点：作者提出用于单比特与双比特高保真量子门学习的物理信息神经网络：以含时薛定谔方程训练 PINN，通过最小化含动力学、门误差、物理约束、正则化与多初值的损失，得到满足固定边界的光滑控制场。训练用相互无偏基对，独立验证结合 Haar 随机输入态与平均门保真度。幺正模拟中 Hadamard 平均门失真约 8.49×10⁻⁸，XX/YY/ZZ 相互作用下 CNOT 在 3.39×10⁻⁷ 至 4.96×10⁻⁶；并考察所学控制场对耦合、训练配置与可用局域场的依赖。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 8. Symmetry-protected isolation of the quantum metric in chiral type-II semi-Dirac semimetals
Wen-Hao Bian · Jing Wang · [arXiv:2611.04996](https://arxiv.org/abs/2611.04996) · cond-mat.mes-hall · new

**为何相关：** 手性极限下 type-II 半 Dirac 半金属由对称严格压灭 Berry 曲率及其偶极与移位电流，使量子度规及其偶极成为光/非线性霍尔响应的唯一来源——量子几何 × 拓扑输运可分离平台。

要点：量子几何含 Berry 曲率（BC）与量子度规（QM），支撑广泛拓扑与输运现象，但固态平台中二者信号常纠缠、难实验分离。作者表明 type-II 半 Dirac 半金属的手性极限提供对称保护机制以干净隔离 QM：自旋轨道隙 m_z=0 时，手性与 PT 对称严格压灭 BC、其偶极（BCD）与移位电流，仅留下 QM 及其偶极（QMD）作为光与非线性霍尔响应来源；纯 QM 区具有发散纵向光导与随参数奇异的 QMD 诱导非线性霍尔等实验指纹。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 9. Evidence for a Dirac Spin Liquid in the Kagome Heisenberg Antiferromagnet from High-Precision Neural-Network Quantum States
Zheng-Hang Sun · Christopher Roth · Ao Chen 等 · [arXiv:2611.05174](https://arxiv.org/abs/2611.05174) · cond-mat.str-el · new

**为何相关：** 几何感知消息传递卷积 NNQS 在至多 300 自旋环面上给出 Kagome 海森堡极低变分能，结构因子与标度支持 Dirac 自旋液而非磁序/价键序或 Z₂ 候选——NNQS × 量子自旋液。

要点：自旋-1/2 Kagome 海森堡反铁磁是量子自旋液的核心模型，基态性质仍未定论。作者用感知 Kagome 几何的消息传递卷积神经量子态，在含至多 300 自旋的二维环面上做大规模变分蒙特卡洛，取得极低变分能。自旋与二聚结构因子未见磁或价键长程序；主导对称分辨关联呈与 Dirac 自旋液涌现 SO(6) 单极子多重态一致的共同标度；优化 NNQS 与 Gutzwiller 投影平均场态的保真度随尺寸更偏向 Dirac 态而非竞争的 Z₂ 候选。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 10. Quantum sensing of a weak drive signal in cascaded quantum van der Pol oscillators
Dong Xie · Chungling Xu · [arXiv:2611.04895](https://arxiv.org/abs/2611.04895) · quant-ph · new

**为何相关：** 两量子 van der Pol 振子经相干+耗散非互易级联，把弱驱动从探针传到更易测的测量振子以读出驱动强度——量子传感 × 耗散耦合非互易。

要点：作者构造由两个量子 van der Pol（vdP）振子组成的传感系统：结合相干与耗散耦合建立子系统间的通用非互易耦合；待测弱驱动加在探针振子上，再经非互易耦合传到更易测量的测量振子，从而获取驱动强度信息。经典级联双 vdP 在完全非互易时灵敏度远高于单经典 vdP；量子情形下灵敏度一般不在零驱动力点发散。当仅有耗散耦合与双粒子损失时，系统在零驱动点具有暗模，可提升传感表现。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 11. Synchronization Mpemba Effect
Yan Li · Wenlin Li · Xingli Li · [arXiv:2611.04994](https://arxiv.org/abs/2611.04994) · quant-ph · new

**为何相关：** 耗散耦合量子 vdP 网络中提出同步 Mpemba 效应：更不同步的初态可追上更同步者，交叉时间由拉普拉斯谱隙与初模权重决定且与拓扑无关——开放系统 × Mpemba 型反常弛豫。

要点：作者引入同步 Mpemba 效应：更不同步的初态可追上更同步者，并在耗散耦合的量子 van der Pol 振子中演示。在图拉普拉斯框架下，两振子情形机制是慢衰变集体背景与快横向瞬态的竞争，等价于相对模位移与相位涨落误差的交换；同一分解推广到网络：同步误差拆成横向拉普拉斯模，由本征值间隔与初模权重给出闭合形式交叉时间及充分筛选判据。因只进入这些本征值，规则与拓扑无关：不同网络的交叉时间塌缩到同一谱隙线。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---
