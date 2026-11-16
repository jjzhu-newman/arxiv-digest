# 9/29 arXiv 兴趣摘要（工作日）

扫了今天（美西 9/29，周二）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。新稿量：cond-mat 约 134、quant-ph 约 123（另有交叉与替换未计入主计数）。按兴趣锚点筛了 **11 篇**，全部为今日新投稿（未收替换稿；交叉里高分的 Rydberg 耗散时间晶体微波转导未挤进终选）。用户机器 DESKTOP-00O6NSD 在线，已对本地 Zotero 只读核对：**11 篇均未见于库中**。

**建议先翻这三篇：**
1. **Dynamical transition in non-Hermitian Chern insulator** —— 非厄米 Chern 绝缘体中拓扑局域与趋肤效应竞争，边缘波包可穿透体态——非厄米拓扑 × 动力学相变。
2. **Symmetry-guided Design Principles for Spin Splitting and Hall Transport in Orthorhombic Altermagnetic Perovskites** —— 正交钙钛矿交错磁的对称性统一框架：自旋劈裂平面、弱铁磁倾斜与反常霍尔张量——altermagnetism × 输运设计。
3. **Microsecond-Programmable Synthetic Quantum Matter: Circumventing the Adiabatic Bottleneck for Heisenberg-Limited Metrology** —— 非绝热 Floquet 协议在腔 BEC 中合成双轴扭转，绕开绝热瓶颈做海森堡计量——Floquet × 纠缠计量。

---

### 1. Dynamical transition in non-Hermitian Chern insulator
Zhi-Qiang Zhang, Yuan-Hang Ren, Ming Lu, Hua Jiang · [2609.35492](https://arxiv.org/abs/2609.35492) · cond-mat.mes-hall · new

**为何相关：** 非厄米 Chern 绝缘体中边缘波包演化不再只由 Chern 数决定，而是拓扑局域与非厄米趋肤效应的竞争——NHSE × 拓扑动力学的直接交汇。

要点：与厄米 Chern 绝缘体不同，边缘出发的波包既可能沿边界传播，也可能穿透进入体态。归因于常规拓扑局域与非厄米趋肤效应的竞争：前者占优则沿边界；后者占优则向体扩散。广义布里渊区可预测拓扑相变，但本身不足以指定这类动力学转变。

---

### 2. Symmetry-guided Design Principles for Spin Splitting and Hall Transport in Orthorhombic Altermagnetic Perovskites
Rasmita Kumari, Bishal Das, Aftab Alam · [2609.33130](https://arxiv.org/abs/2609.33130) · cond-mat.mtrl-sci · new

**为何相关：** 正交 Pbnm 钙钛矿共线反铁磁的统一对称性框架，直接给出交错磁自旋劈裂、弱铁磁倾斜与反常霍尔张量——altermagnetism 材料设计原则。

要点：磁序的不可约表示唯一决定动量空间中支持交错磁自旋劈裂的平面、有效低能哈密顿量形式、SOC 诱导弱铁磁倾斜方向及允许的 AHC 张量分量。在八种已实现正交钙钛矿氧化物上验证；如 LaTiO3、CaCrO3 等给出可观自旋劈裂与霍尔响应。

---

### 3. Microsecond-Programmable Synthetic Quantum Matter: Circumventing the Adiabatic Bottleneck for Heisenberg-Limited Metrology
Soi-Chan Lei · [2609.34559](https://arxiv.org/abs/2609.34559) · quant-ph · new

**为何相关：** 单腔 BEC 上非绝热 Floquet 协议动态合成双轴扭转（TAT），绕开绝热临界穿越的慢动力学与退相干——Floquet 工程 × 海森堡极限计量。

要点：快速旋转与相位跳变把原生纵向耦合合成为有效 TAT。用有限态自动机矩阵积算符（MPO）编码，虚维严格 O(1)，支持大规模精确 DMRG/TDVP。在 N=10³ 系综跟踪非平衡 Floquet TAT 与环境退相干，表明猝灭可快速生成宏观纠缠并逼近海森堡计量。

---

### 4. Computational symmetry hierarchy of time-reversal-even and -odd spin Hall conductivity tensors in altermagnets
Dameul Jeong, Seoung-Hun Kang, Young-Kyun Kwon · [2609.33631](https://arxiv.org/abs/2609.33631) · cond-mat.mtrl-sci · new

**为何相关：** 把交错磁自旋霍尔电导张量拆成时间反演偶/奇通道，用对称性 + 第一性原理给出完整响应层级——altermagnetism × 自旋霍尔输运。

要点：偶通道服从晶体学选择定则，与 Berry 曲率费米海起源一致；奇通道由磁对称性设定，可被螺旋转/滑移相关的反幺正操作重塑。动量分辨分析把偶响应与 SOC 打开的避免交叉、奇响应与费米面附近各向异性自旋流织构联系起来；覆盖六种不同晶体类代表化合物。

---

### 5. Topological chiral edge modes in the continuum of a trivial bulk
Li Ge · [2609.34000](https://arxiv.org/abs/2609.34000) · cond-mat.mes-hall / physics.optics · new

**为何相关：** 在拓扑平凡二维体系中，用虚磁通（边缘非对称耦合）诱导“连续谱中的手性边缘模”（CEMIC）——非厄米开放边界与拓扑边缘模的新机制。

要点：CEMIC 位于体带连续谱内而非带隙。虽有非对称耦合，其边缘局域并不来自典型的非厄米趋肤效应，而是非对称耦合结点处与环境的能量交换。较强耦合给出优先环流方向；为平凡体中工程手性边缘通道提供开放系统路径。

---

### 6. On Embedding Design in Quantum Physics-Informed Neural Networks
Ban Q. Tran, Nahid Binandeh Dehaghani, Susan Mengel 等 · [2609.33700](https://arxiv.org/abs/2609.33700) · quant-ph · new

**为何相关：** 系统讨论量子物理信息神经网络（QPINN）中坐标→量子态嵌入的设计准则——PINN × 量子机器学习的直接交叉。

要点：把嵌入表述为塑造变分线路可用特征表示的函数变换，并提出两种：LQNN-TE-QPINN 用辅助量子线路生成数据依赖特征再与坐标相加；AdaFreq-QPINN 把 arccos-Chebyshev 编码的频率缩放因子提升为可训练参数。在 PDE 残差训练设定下比较嵌入选择对表达能力与收敛的影响。

---

### 7. Counterdiabatic quasi-Floquet control for the generation of entangled BICs using giant atoms
Alexis R. Legón, Pedro Orellana, Ariel Norambuena · [2609.32125](https://arxiv.org/abs/2609.32125) · quant-ph · new

**为何相关：** 双编织巨原子波导 QED 中，准 Floquet 调制 + 受限反绝热辅助制备高保真纠缠连续谱束缚态——Floquet 控制 × 开放波导纠缠保护。

要点：对有效原子–波导耦合做准 Floquet 调制，并用独立相位控制的原子交换提供受限反绝热辅助。无损耗有效模型中全态 BIC 保真度可达 0.99992，无条件原子 Bell 保真度 0.99588；有限模微观模拟与静态校准误差扫描给出控制容差，并讨论弛豫/退相干下的鲁棒性。

---

### 8. Gauge freedom and efficient algorithms for Lindbladian learning
Steven T Flammia, Savar D Sinha, Yu Tong · [2609.35265](https://arxiv.org/abs/2609.35265) · quant-ph · new

**为何相关：** 在 SPAM 噪声下学习局域 Lindbladian：刻画规范自由度导致的不可观测量，并给出对规范不变量的鲁棒学习算法——开放系统 × 量子学习。

要点：SPAM 可使不同 Lindbladian 实验上不可区分，从而使部分分量根本不可学。对有界度局域 Lindbladian，识别与可信单比特控制对易的局域规范变换族，并据此分类分量。对泛规范依赖分量可构造 Ω(1) 与系统尺寸无关的不确定性；对普遍规范不变量给出 SPAM 鲁棒可扩展学习算法。

---

### 9. Mobile-impurity dynamics in a non-Hermitian Stark-localised bath
Muhammad S. Hasan, Hsiang-Hua Jen, Jhih-Shih You · [2609.33275](https://arxiv.org/abs/2609.33275) · cond-mat.quant-gas · new

**为何相关：** 干净可动杂质耦合到带线性 Stark 势与非对称跃迁的一维浴：共振隧穿、记忆擦除与趋肤效应——非厄米开放多体 × NHSE。

要点：当相互作用强度匹配 Stark 势时，杂质介导浴中共振隧穿并抹去浴初态记忆。非厄米非对称不移动共振位置，但方向性重塑共振，并通过趋肤效应破坏 Stark 诱导的记忆。杂质仅在中等倾斜强度下局域：弱倾斜无法俘获，强倾斜下浴冻结为近周期 CDW 并部分局域杂质。

---

### 10. Apparent Compression, Real Stability: The Intrinsic Dimension of Learning a Quantum Wavefunction
Lu Wei, Yufeng Wang, Chenfeng Cao, Haibin Ling · [2609.33193](https://arxiv.org/abs/2609.33193) · cs.LG / quant-ph · new

**为何相关：** 在变分蒙特卡罗（VMC）神经网络量子态训练中测量权重空间本征维——NNQS / 量子多体机器学习的参数效率诊断。

要点：本征维定义为仍能达到目标精度的最少随机训练方向数。对 VMC（自采样、梯度噪声大、答案可精确评分）用冻结随机映射把小潜向量扩成网络权重。发现“小本征维”可能具有误导性，但其带来的稳定性是真实的；在具有困难符号结构的磁体上，不能表示正确符号的网络即便维数再小也学不会。

---

### 11. Piezo-Hall effect in RbCr₂Se₂O
San-Dong Guo, Shi-Hao Zhang, Feng-Ren Fan · [2609.33026](https://arxiv.org/abs/2609.33026) · cond-mat.mtrl-sci · new

**为何相关：** 以 d 波交错金属为原型，论证应变把禁戒净磁矩/AHE 的磁空间群变为允许 AHE 的新群——altermagnetism × 压电/应变霍尔调控。

要点：压电霍尔效应：原始 MSG 禁止净磁矩并压制 AHE，应变后新 MSG 允许净磁矩从而开启 AHE。机制包括应变诱导磁电子态转变与磁化方向调控。第一性原理在 RbCr₂Se₂O 上验证：沿 x/y 施加相同单轴应变时，反常霍尔电导符号相反、幅度相等。并推广到压磁光、电霍尔与温度霍尔等外场变体。

---
