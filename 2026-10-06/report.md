# 10/6 arXiv 兴趣摘要（工作日）

扫了今天（美西 10/6，周二）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。新稿量：cond-mat 约 120、quant-ph 约 218、hep-th 约 29（另有交叉与替换未计入主计数）。按兴趣锚点筛了 **12 篇**（11 新投稿 + 1 交叉；未收替换稿）。核对了本地 Zotero 库（只读副本），12 篇都不在库里；其中 QAH 拓扑环行器那篇与库里的片上微波量子霍尔环行器（Mahoney 等，PRX）器件思路相近，单向 Bose–Hubbard 那篇与库里 Rassaert 等 2025 年的驱动耗散 Bose–Hubbard 非厄米拓扑工作方向相近。

**建议先翻这三篇：**
1. **Electron-phonon control of obstructed and quantum spin Hall topology in an altermagnet** —— 交错磁嵌入 QSH 绝缘体诱导受阻原子绝缘相，电声耦合可再切回螺旋边缘态——altermagnetism × 拓扑。
2. **Probing Quantum Anomalous Hall Transport Under Microwave Irradiation Using a Topological Circulator** —— QAH 拓扑环行器上的微波泵浦–探测，例外点附近响应约翻倍——非厄米 EP × 拓扑 × 传感。
3. **State-selective entanglement and point-gap topology in the unidirectional Bose-Hubbard chain** —— 单向 Bose–Hubbard 链中态选择性纠缠与多体点能隙拓扑——非厄米拓扑 × 纠缠。

---

### 1. Electron-phonon control of obstructed and quantum spin Hall topology in an altermagnet
Kuntal Bhattacharyya, Bilal Tanatar, Saurabh Basu · [2610.04684](https://arxiv.org/abs/2610.04684) · cond-mat.mes-hall · new

**为何相关：** 把 d 波交错磁嵌入 BHZ 型量子自旋霍尔绝缘体，并用电声耦合在受阻原子绝缘体与 QSH 拓扑之间切换——altermagnetism × 拓扑相 × 自旋电子学。

要点：作者理论研究 d_{x²−y²} 波交错磁（零净磁化、非相对论自旋劈裂能带）嵌入 BHZ 型量子自旋霍尔绝缘体后的拓扑相。交错磁序超过临界强度时，母体 QSH 态被重构为受阻原子绝缘体（OAI）：体极化非平庸、角电荷分数量子化并伴随带隙内边界态，而自旋陈数归零。引入足够强的电声耦合后，极化子修饰会重排 Wannier 中心和有效边缘拓扑，削弱交错磁诱导的 OAI 相并恢复螺旋 QSH 边缘态；更强的电声耦合最终把体系推向平庸绝缘体。文章由此给出交错磁中拓扑不同绝缘相之间的可控切换机制，指向声子调控的自旋电子学功能。

---

### 2. Probing Quantum Anomalous Hall Transport Under Microwave Irradiation Using a Topological Circulator
Athul Ashok, Frank Jin, Nick Du, Luis A. Martinez 等 · [2610.06245](https://arxiv.org/abs/2610.06245) · quant-ph · new

**为何相关：** 在量子反常霍尔拓扑环行器上研究微波辐照对边缘磁等离子体输运的扰动，并利用耦合模的非厄米杂化在例外点附近放大响应——拓扑 × 非厄米 EP × 微波传感。

要点：边缘磁等离子体（EMP）是探测拓扑材料中手性电荷动力学与非互易微波输运的平台，但其在常规微波散射测量中的信号往往很弱。作者用量子反常霍尔拓扑环行器做泵浦–探测测量，发现响应强烈依赖频率：在若干泵浦频率下 EMP 透射被显著改变，而在包括 4 GHz 和 7 GHz 在内的特定频率几乎不变。进一步利用 EMP–谐振腔耦合系统的非厄米模式杂化探测例外点附近的响应，EP 附近泵浦引起的透射幅度变化约为远离 EP 时的两倍。结果展示了手性 EMP 输运、微波光子扰动与非厄米动力学的相互作用，把拓扑环行器定位为增强微波谱学与传感的平台。你的库里有 Mahoney 等的片上微波量子霍尔环行器（PRX），可作为器件背景对照。

---

### 3. State-selective entanglement and point-gap topology in the unidirectional Bose-Hubbard chain
Chuan-Fu Lin, Yu-Chin Tzeng, Po-Yao Chang · [2610.04331](https://arxiv.org/abs/2610.04331) · cond-mat.str-el · new

**为何相关：** 单向 Bose–Hubbard 链中相互作用对趋肤模、纠缠与多体点能隙拓扑的影响，区分基态与“稳态”本征态——非厄米拓扑 × 纠缠。

要点：作者研究排斥相互作用对单向（非互易）Bose–Hubbard 模型中趋肤模与纠缠的影响。该可积模型的基态经历超流–Mott 转变且趋肤聚集被抑制，但纠缠如何变化取决于所选多体态：16 格点单位填充下，基态密度趋于均匀、纠缠向 Mott 极限减小，而稳态（零动量扇区中虚部能量最大的本征态）呈非单调纠缠交叉；U/t=10 时其二阶 Rényi 熵出现四个空间极大，可由四个双占–四个空穴的主导组态流形中竞争的子系统粒子数扇区解释。强相互作用下投影到一个双占–一个空穴流形即可重现熵分布及两个边缘峰；多体绕数在强相互作用下仍非零，两格点精确例子显示它在 U/t→∞ 的奇异投影极限变得无定义。你的库里有 Rassaert 等 2025 PRL 关于手性驱动耗散 Bose–Hubbard 模型中涌现非厄米拓扑的工作，方向相近。

---

### 4. Emergent magnetic nonanalyticity in Dirac altermagnets
Xizhi Fu, Zhenqiao Huang, Fei Yang, Mengli Hu 等 · [2610.04496](https://arxiv.org/abs/2610.04496) · cond-mat.mtrl-sci · new

**为何相关：** Dirac 交错磁中 C 配对自旋极化 Dirac 锥被打破后出现非解析的压磁响应——altermagnetism 中超越对称性分析的奇异磁响应。

要点：作者指出对称性允许的响应未必真正出现，这在对称性相关的无能隙 Dirac 费米子中尤其明显：移动 Dirac 点的微扰会驱动 Lifshitz 重构，产生内禀非解析的有效势。在 Dirac 交错磁中，C 配对的自旋极化 Dirac 锥在 C 对称性被打破后简并解除，Lifshitz 重构转化为巡游磁化，于是压磁效应变为非线性、非解析的 M∝sgn(ε)ε²，而对称性允许的线性响应反而缺席。这意味着领头响应无法从基于 Neumann 原理和解析 Landau 展开的传统范式推出；第一性原理计算给出单层 Fe₂S 作为候选材料。

---

### 5. Exact Temporal Criticalities of Entanglement and Negativity in Gaussian and Non-Gaussian Dissipative Kitaev Chains
Shrey Chowdhary, Sanket Chirame, Stephan Haas, Rishabh Jha · [2610.03889](https://arxiv.org/abs/2610.03889) · quant-ph · new

**为何相关：** 耗散 Kitaev 链中纠缠谱与负性谱能隙闭合的“时间临界性”精确分析，对比弱对称（增益/损耗）与强对称（退相位）开放动力学——开放系统 × 纠缠 × 拓扑链。

要点：当纠缠谱或负性谱的两个最大本征值相遇时，对应纠缠/负性哈密顿量能隙闭合而熵保持光滑，作者称之为时间临界性，并考察开放费米系统中它何时、以何顺序出现、是否早于负性开始下降的几何退相干时间。比较只在平均意义上保持费米宇称（弱对称、保持高斯性）的损耗与增益和每次跳跃都保持宇称（强对称、非高斯）的密度退相位后发现，决定判据的是高斯性而非对称性：高斯态中子系统纠缠能隙恰在两宇称扇区权重相等时闭合，负性临界性从不晚于纠缠临界性；均匀平衡增益损耗对任意二次哈密顿量都不移动临界点。对退相位，作者在键项对易点精确求解非高斯动力学：弱退相位推迟两种临界性，接近临界阻尼时临界性退到无穷远，强退相位下负性在能隙收缩前很久就开始下降。

---

### 6. Origin and classification of fractional dynamical topology in non-Hermitian quantum systems
Zimiao Zhang, Li Chen, Weilun Jiang, Heng Shen · [2610.05262](https://arxiv.org/abs/2610.05262) · quant-ph · new

**为何相关：** 非厄米两带模型中动力学拓扑序参量半整数跳变的起源与分类——非厄米拓扑 × 动力学量子相变。

要点：动力学量子相变（DQPT）已被推广到非厄米体系，动力学拓扑序参量的半整数跳变在厄米与非厄米体系中都可能出现，但在非厄米情形下的起源尚不清楚。作者在两带非厄米模型中证明这类分数跳变源自复能谱的不连续，并与淬火哈密顿量的稳态相图内在关联，据此对 DQPT 的出现进行分类。分析进一步推广到多带哈密顿量与二维模型，给出分数动力学拓扑特征的统一理解。

---

### 7. From Ground State to Electronic and Vibronic Spectra via Memory Kernel Coupling Theory and Neural Quantum States
Xinchen He, Wenjie Dou · [2610.04315](https://arxiv.org/abs/2610.04315) · physics.chem-ph · cross

**为何相关：** 把神经网络量子态与连分式记忆核耦合理论结合，从变分基态直接重构分子电子谱与振动电子谱——NNQS 从基态走向谱学。

要点：作者提出 Aurora 方法，将神经网络量子态（NQS）与连分式记忆核耦合理论（CF-MKCT）结合：把零温 Liouvillian 响应层级映射为对偶极制备态反复作用平移哈密顿量，从而无需显式激发态或时间演化即可由变分基态重构吸收谱。实现上结合了变分蒙特卡洛、隐式重启 Lanczos 辅助的 NQS 优化、免矩阵哈密顿作用与自适应递归控制；对可处理分子，电子谱与全组态相互作用及常规 MKCT 结果吻合。对电声哈密顿量，方法用 Huang–Rhys 模式选择与局域 SVD 声子编码器压缩，H₂ 基准保留主振动包络，并给出 C₆H₆ 与 C₁₀H₈（10 电子 10 轨道活性空间）的振动电子谱。

---

### 8. The superb supersinglet
Gabriele Cobucci, Armin Tavakoli, Alexander Bernal, Shishir Khandelwal · [2610.06183](https://arxiv.org/abs/2610.06183) · quant-ph · new

**为何相关：** 高维多体全反对称态（supersinglet）的纠缠鲁棒性、见证方法及其在梯度传感中达到海森堡标度——纠缠 × 量子传感。

要点：全反对称态（supersinglet）是高维多体系统中量子比特无法实现的一类纠缠态，在任意集体局域幺正变换下不变。作者用凸优化表明其核心纠缠特征对噪声非常鲁棒，在某些松弛条件下明显优于几种典型纠缠态；并基于集体自旋测量或随机测量发展见证方法，可认证其纠缠深度与纠缠维数。最后作者把 supersinglet 确定为高维梯度传感的天然资源，并证明其可实现海森堡标度。

---

### 9. Floquet dressing of bulk metallic bands in 2H-NbSe2
Cong Li, Qirui Cui, Maciej Dendzik, Magnus H. Berntsen 等 · [2610.04958](https://arxiv.org/abs/2610.04958) · cond-mat.str-el · new

**为何相关：** 用时间与角分辨光电子能谱在 2H-NbSe₂ 的体金属能带中识别 Floquet 修饰——Floquet 工程从拓扑表面态推广到体金属。

要点：Floquet 修饰此前主要在拓扑绝缘体表面态、半导体与二维 Dirac 半金属中实现，强屏蔽与快速散射使其在体金属中的可行性长期受怀疑，且光电子修饰（Volkov）会干扰识别。作者用 trARPES 在 2H-NbSe₂ 交叠的体能带中识别出 Floquet 修饰：稀疏未占据态窗口中的光子移位复本保留母带色散，且只在泵浦–探测重叠期间出现；在固定探测偏振下旋转泵浦线偏振会在动量空间分支间重新分配复本权重。考虑固体内外光场的模型用同一组参数，以相干 Floquet–Volkov 干涉比任一单独通道或非相干叠加更好地重现这种重分配，无需依赖杂化能隙即可确认体金属能带的 Floquet 修饰。

---

### 10. Imaginary magnetic fields for ultracold atoms
Saulius Alminas, Domantas Burba, Gediminas Juzeliūnas · [2610.06793](https://arxiv.org/abs/2610.06793) · cond-mat.quant-gas · new

**为何相关：** 用 Raman 耦合加态依赖粒子损耗为冷原子构造均匀“虚磁场”——非厄米合成规范场的新方案。

要点：作者提出一个四能级方案：通过 Raman 耦合与态依赖粒子损耗，先消去两个有损辅助态，再投影到剩余两个 Raman 缀饰态之一，原子运动便受到旋度为常数的虚矢势作用，即空间均匀的虚合成磁场。文中解析推导了此类合成磁场中高斯波包的动力学，并研究了非厄米体系特有的、依赖波包宽度的输运。两能级非厄米哈密顿量与绝热投影描述的数值结果一致，验证了后者的适用性。

---

### 11. Shaping double descent in quantum extreme learning through model design
Sabri Meyer, Ege Yilmaz, Aurelien Lucchi, Francesco Tacchino 等 · [2610.06581](https://arxiv.org/abs/2610.06581) · quant-ph · new

**为何相关：** 解析刻画相关特征下的双下降曲线，并给出量子极限学习机（QELM）避免泛化恶化的设计原则——量子机器学习理论。

要点：双下降在独立特征下已被充分理解，而相关特征下其形状由特征协方差谱决定，现有分析多只给出隐式方程。作者先对经典线性回归闭合这一缺口，用特征总体协方差的条件数与一个关联强度谱测度两个量解析刻画整条风险曲线；再将理论应用于量子极限学习机，表明编码强度、输入重上传与测量次数三个可调旋钮都会正则化 QELM 输出协方差，并给出插值阈值保持稳定的条件，有限测量次数的散粒噪声可用于保证这一稳定性。数值实验验证了各项预测，给出 QELM 越过插值区后仍良好泛化的具体设计原则。

---

### 12. Transformer-Based Time-Series Inference of Lindblad Dynamics in Open Quantum Systems
Julian Guam, Jianqing Liu · [2610.05647](https://arxiv.org/abs/2610.05647) · quant-ph · new

**为何相关：** 用直接读入 Pauli 期望值原始时间序列的 Transformer 联合反演 Lindblad 耗散率与哈密顿参数——AI × 开放量子系统辨识/环境感知。

要点：当系统哈密顿量与耗散率部分未知或显含时间时，传统解析反演与系统辨识方法难以处理；已有 Transformer 方法依赖手工统计特征且条件理想化。作者提出直接输入 ⟨σx(t)⟩、⟨σy(t)⟩、⟨σz(t)⟩ 完整轨迹的原始时间序列 Transformer，充分利用自注意力做时间建模，并扩展到联合学习未知哈密顿参数、处理多耗散通道以及在真实测量噪声下稳健工作。各测试场景下重建精度都很高且无需人工特征工程，作者将其定位为真实开放量子系统中可扩展的量子环境感知框架。
