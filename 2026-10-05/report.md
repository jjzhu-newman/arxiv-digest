# 10/5 arXiv 兴趣摘要（工作日）

扫了今天（美西 10/5，周一）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。新稿量：cond-mat 约 60、quant-ph 约 122、hep-th 约 18（另有交叉与替换未计入主计数）。按兴趣锚点筛了 **12 篇**（11 新投稿 + 1 交叉；未收替换稿）。核对了本地 Zotero 库（只读副本），12 篇都不在库里；其中 PINN 初始化那篇和库里已有的 Fourier 特征 PINN 工作（Arni & Blanco 2025）方向相近。

**建议先翻这三篇：**
1. **Complete Magnetic Hierarchy in Bichromatically Driven Unconventional Magnets** —— 双色 Floquet 驱动工程化交错磁及更高阶非常规磁体——altermagnetism × Floquet。
2. **Covertness as a resource constraint in quantum target sensing** —— 隐蔽性约束下的量子目标感知极限，TMSV 探针在强隐蔽下仍保有 O(M) 优势——量子雷达。
3. **Decohering Kitaev's Sixteenfold Way: A Holographic Approach** —— Kitaev 十六重道费米子退相干给出本征混合态拓扑序——开放系统混合态拓扑。

---

### 1. Complete Magnetic Hierarchy in Bichromatically Driven Unconventional Magnets
Pei-Hao Fu, Sayed Ali Akbar Ghorash · [2610.03461](https://arxiv.org/abs/2610.03461) · cond-mat.mes-hall · new

**为何相关：** 双色 Floquet 驱动下非常规磁体（含 d 波交错磁）的完整磁性层级——altermagnetism × Floquet 工程正中两条兴趣线。

要点：作者给出用双色（两频率可公度）驱动工程化非常规磁性的一般框架，并发现一条清晰层级：偶数频率比下，连续模型的领头 q 波磁体只能生成到 q−2 阶分量，缺失的 q−1、q 阶宇称需靠晶格高阶梯度项补齐。以圆–线偏振光照射的 d 波交错磁为例，驱动场的不对称性被转移到光修饰能带上，出现超出静态与单频极限的动量不对称色散；该不对称源自被驱动转化为动量奇项的晶格高梯度项。推广到更高阶非常规磁体后得到所有 q 宇称的完整层级，把双色 Floquet 驱动确立为动态构造混合宇称磁性的通用路线。

---

### 2. Covertness as a resource constraint in quantum target sensing
Yu Yang, Fengyu Guan, Shiping Guo, Ruifeng Liu 等 · [2610.03233](https://arxiv.org/abs/2610.03233) · quant-ph · new

**为何相关：** 把“隐蔽性”作为资源约束纳入量子目标感知的极限精度分析——量子雷达/量子照明方向的直接新进展。

要点：量子隐蔽目标感知要在热背景中探测低反射率目标又不被对手察觉，这限制了可用探测能量。作者建立统一框架，连接隐蔽目标判别与量子增强参数估计：先给出 ε-隐蔽性诱导的探测能量界（可用能量窗按 O(√(ε/M)) 收窄），再引入隐蔽约束量子 Fisher 信息（CCQFI）刻画反射率估计的终极精度。高斯分布相干态探针的 CCQFI 按 O(ε) 标度、在强隐蔽极限下消失，而双模压缩真空探针保留有限的 O(M) 项，显示明显的量子优势；光子计数可饱和前者，零差探测对后者可达性更高。

---

### 3. Decohering Kitaev's Sixteenfold Way: A Holographic Approach
Shuyu Zhang, Linhao Li, Zhen Bi, Tzu-Chieh Wei 等 · [2610.03610](https://arxiv.org/abs/2610.03610) · cond-mat.str-el · new

**为何相关：** 用 Walker–Wang 全息构造研究 Kitaev 十六重道中费米子退相干，得到本征混合态拓扑序——开放系统 × 拓扑物态。

要点：文章研究二维拓扑序的任意子退相干，以 Kitaev 十六重道中的费米子退相干为具体例子；其中的手性拓扑相被认为没有对易投影哈密顿量，直接研究很困难。作者猜想退相干诱导相变后的密度矩阵可分三步得到：先把拓扑序提升为 Walker–Wang 模型，再过渡到另一个 Walker–Wang 模型，最后对体自由度求迹，从而把二维拓扑序退相干与三维对应物的纯态相变联系起来。结论是对十六个态中任一个退相干费米子都会得到本征混合态拓扑序，因为对应三维体总是跃迁到三维费米 toric code。

---

### 4. Magnetic-Order-Driven Nonlinear Photocurrents in PT-Broken Antiferromagnetic MnS2 and Altermagnetic MnSe2
Fu Li, Rajyavardhan Ray, Xiaoxiong Liu, Babu Baijnath Prasad 等 · [2610.03450](https://arxiv.org/abs/2610.03450) · cond-mat.mtrl-sci · new

**为何相关：** 交错磁 MnSe₂ 与 PT 破缺反铁磁 MnS₂ 中由磁序驱动的非线性光电流与自旋光电流——altermagnetism × 自旋光电响应。

要点：非线性光电流通常需要空间反演破缺，这里破缺来自磁序而非结构。作者对两种黄铁矿型半导体计算有无自旋轨道耦合时线偏/圆偏光下的位移电流与注入电流，并用磁点群与自旋点群确定对称允许的张量分量：线偏位移电流与圆偏注入电流在两者中都允许；线偏注入与圆偏位移电流在 MnS₂ 中禁戒，而在 MnSe₂ 中只有计入 SOC 才出现。非相对论极限下 MnSe₂ 还支持线偏位移与圆偏注入自旋光电流，MnS₂ 则全部禁戒，表明补偿磁序诱导的反演破缺可用于产生和调控非线性光电流。

---

### 5. Correlated Metals, Metamagnetism, and Orbital Nematic Order in moiré Materials with Neural Quantum States
Wei Zhang, Ataç İmamoğlu, Tao Shi, Eugene A. Demler 等 · [2610.03145](https://arxiv.org/abs/2610.03145) · cond-mat.str-el · new

**为何相关：** 用消息传递神经网络量子态 + VMC 求解莫尔连续模型，发现关联金属、变磁与轨道向列序——NNQS 在真实关联体系的新应用。

要点：研究受三角周期势调制、长程库仑相互作用的二维电子在填充 ν=2 时的基态相图（随周期势强度与塞曼场）。非相互作用下应是普通能带绝缘体，但强关联会重塑绝缘态，并在部分区域以一级相变让位于关联金属。金属–绝缘体转变强烈依赖自旋极化：非极化系统在较弱势下形成 s 波分子绝缘体，完全极化系统需更深势并形成破缺对称的轨道向列分子晶体，由此带来不连续磁化曲线、变磁转变与多临界点。换成短程排斥（冷原子可实现）后相图定性不变。

---

### 6. Generalization of Transformer-Based Neural Quantum States via In-Context Learning
Zhen Qin, Qing Qu, Alfred O. Hero III · [2610.03463](https://arxiv.org/abs/2610.03463) · quant-ph · new

**为何相关：** 给 Transformer 神经网络量子态在上下文学习下的泛化误差建立严格理论界——NNQS 理论基础。

要点：Transformer 型 NQS 能刻画长程关联且经验上泛化良好，但缺乏理论理解。作者在上下文学习（in-context learning）框架下给出推断时泛化误差的严格 MSE 上界：逐点预测误差随上下文样本数与 Transformer 深度成反比下降，且达到该保证所需深度只随系统规模（连续体系的粒子数或离散体系的 qudit 数）线性增长。进一步推广到以秩一密度算符表示的完整量子态，在物理约束下给出连续与离散域的泛化界，并用数值模拟验证。

---

### 7. Reaching the Limits of Ground-State Metrology with Many-Body Probes
Erik L. André, Víctor Izquierdo, Ricard Puig, John Calsamiglia 等 · [2610.03653](https://arxiv.org/abs/2610.03653) · quant-ph · new

**为何相关：** 多体探针基态计量何时能饱和静态基态界与动态海森堡极限——量子传感 × 量子临界。

要点：讨论用短程或长程相互作用的多体探针，通过测其基态来估计 N 体哈密顿量参数时，如何达到量子 Fisher 信息的两个基本极限：静态基态界 F ≲ N²/Δ² 与动态海森堡极限 F ≲ N²τ²。短程系统要饱和静态界需能隙随 N 闭合，在二级量子临界点给出临界指数的普适条件 ν(d+z)=1（XXZ 链可任意逼近），一级相变处的猫态是另一路线；全连通模型在有隙区也能达到最优。达到动态界与基态制备时间紧密相关，最优的逆能隙剖面可由局域绝热协议获得。

---

### 8. Quantum Codeword Sensing
John Blue, Zachary E. Chin, Vlad S. Oros, Isaac L. Chuang · [2610.03659](https://arxiv.org/abs/2610.03659) · quant-ph · new

**为何相关：** 量子传感器配合持久量子存储识别弱相位编码的经典码字，严格优于只有经典存储的接收端——量子传感/通信感知新范式。

要点：设定是一串弱相位相互作用把经典码字逐比特写入一组传感量子比特（每比特控制一次角度 θ 的 Z 旋转），总比特预算 Q 内允许辅助比特与任意纠缠。在弱信号极限 Qθ→0 下，作者证明耦合持久量子存储的传感器识别码字比任何只有经典存储的同预算接收端更可靠，即使传输中有比特翻转。对 [n,k] 二元单纯形码，用 Q=Θ((t+1)log n) 可精确纠正至多 (k−2)/4 个传输错误，而经典存储接收端的平均成功率趋于零；独立翻转概率 p<1/16 时，用 O(log n log log n) 个比特即可使解码错误趋零。

---

### 9. Parity-Time Symmetry of Plasma Waves
Hong Qin · [2610.03433](https://arxiv.org/abs/2610.03433) · physics.plasm-ph · cross

**为何相关：** 证明磁化等离子体线性化 Vlasov–Maxwell 系统具有 PT 对称，并把多种动理学不稳定性解释为经 Krein 碰撞的自发 PT 破缺——非厄米/PT 物理的跨领域实例。

要点：均匀无碰撞磁化等离子体的极化率张量满足 PT 对称；作者说明这是底层动理学系统 PT 对称在约化响应空间中的体现，在电磁动理学本征模空间定义 P 与 T，证明线性化 Vlasov–Maxwell 哈密顿算符 PT 对称，Vlasov–Poisson 本征问题亦然。与非单调分布、环形、损失锥、共振高能粒子相关的许多动理学不稳定性本质上是自发 PT 破缺，且只能经由 Krein 碰撞实现。三个例子包括：定号回旋留数保护热 Bernstein 模、Dory–Guest–Harris 分布的不稳定阈值与增长率解析式，以及新近发现的模–极点共振不稳定性。

---

### 10. Emergent Dissipation from Fluctuating Quantum-Network Topology
Alireza Nourmandipour, Stefano Mancini · [2610.03194](https://arxiv.org/abs/2610.03194) · quant-ph · new

**为何相关：** 量子网络相互作用拓扑的时间涨落平均出 Markov 主方程，耗散结构由邻接矩阵协方差决定——开放系统耗散工程。

要点：考虑每隔短时间重画一次图的量子网络，平均动力学给出 Markov 主方程：平均网络决定相干部分，协方差决定耗散结构，其本征值给噪声强度、本征矢给集体算符。平均邻接矩阵和协方差谱相同但本征矢不同的两个系综，即使纯度相同也会产生不同动力学。一个可实现模型给出可解析预言的耗散能隙与准受保护动力学，说明涨落连通性可作为工程化耗散与保护的资源。

---

### 11. Operator-informed initialization for Fourier features physics-informed neural networks
Juan Molina, Paris Perdikaris, Mircea Petrache, Matías Courdurier 等 · [2610.03378](https://arxiv.org/abs/2610.03378) · cs.LG · new

**为何相关：** 在 NTK 区分析 Fourier 特征 PINN 的谱偏置，提出按 PDE 算符定制的初始化——PINN 训练动力学的实用改进。

要点：PINN 常有谱偏置，不同频率收敛快慢不一。作者在神经正切核区推导残差在频域的演化方程，表明各频率收敛速率主要由微分算符符号与初始化权重谱密度的乘积决定；据此提出按所解 PDE 定制初始权重分布的“算符感知”初始化，以平衡各频率收敛。线性与非线性 PDE 实验显示该初始化在不增加训练成本的前提下改善学习动力学与各频段精度。你的库里已有 Arni & Blanco 2025 的 Fourier 特征 + 注意力解码 PINN，可对照阅读。

---

### 12. The AI Theorist reveals excitonic structure in $α$-RuCl$_3$
Hongjian Zhou, Xianfan Nie, Sean Wu, Tarun Patel 等 · [2610.02417](https://arxiv.org/abs/2610.02417) · cs.LG · new

**为何相关：** 多智能体 AI 系统结合第一性原理与多体计算，自主为 α-RuCl₃ 光谱数据建立激子模型——AI × 量子材料的“自主理论家”尝试。

要点：作者提出 AI Theorist：由多个 AI 智能体完成假设生成、第一性原理计算与证据驱动修正，用于从实验观测自主发现物理模型。应用于 Kitaev 量子自旋液体候选材料 α-RuCl₃ 的光学与光电流谱，系统给出新解释，识别出光学选择定则与实空间分布截然不同的激子态。作者称这是首次由 AI 系统利用第一性原理电子结构与多体计算，为量子材料中未发表的实验观测自主构建物理模型。
