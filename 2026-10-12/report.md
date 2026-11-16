# 10/12 arXiv 兴趣摘要（工作日）

扫了今天（美西 10/12，周一）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。新投稿量：cond-mat 71、quant-ph 63、hep-th 31、math-ph 6（cs.LG 146、stat.ML 23 只看物理/量子相关；交叉与替换未计入）。周一交错磁仍不少：α-MnTe 场致取向去孪、alter-exciton、电荷-4e 超导相控制、二维有机金属格子 100% 自旋极化；开放系统一侧有耗散 Majorana 链的异常/非可逆对称、耗散制备的局域性–时间权衡、非马尔可夫耗散 Ising 精确解，以及信道级例外点操作理论；另有 Floquet Dynamical Freezing、PINN 解 fRG，以及 NV 连续波百 MHz AC 磁强计与多几何神经 VMC。按兴趣锚点筛了 **12 篇**（新投稿 9、交叉 3；未收替换稿）。核对了本地 Zotero 库（只读副本），12 篇都不在库里；交错磁/MnTe、Majorana/Lindblad、耗散制备、PINN、NV 方向库里已有相关文献，相应条目里有标注。

**建议先翻这三篇：**
1. **Magnetic-field-induced detwinning of orientational domains in altermagnet α-MnTe** —— 单晶中子衍射显示面内场可把六畴 α-MnTe 几乎对齐到单一取向畴，饱和约 2 T——altermagnetism 畴操控 × 磁振子手性测量前序。
2. **Dissipative Majorana Chain---Anomalies and Non-Invertible Symmetries** —— 把 Lindblad 动力学的耗散 Majorana 链映射为加倍空间非厄米算符，诊断强/弱对称与 mod-8 异常，并导出带非可逆 Kramers–Wannier 对称的 Ising Lindbladian——开放系统 × 拓扑异常。
3. **Locality-Preparation Time Tradeoffs in Dissipative Quantum Systems** —— 对二次费米子给出耗散制备中“跳跃算符局域性 ↔ 制备时间”的精确权衡，并以 Kitaev 链区分临界与拓扑能隙相——开放系统态制备 × 拓扑。

---

### 1. Magnetic-field-induced detwinning of orientational domains in altermagnet α-MnTe: A single-crystal neutron diffraction study
Feihao Pan, Yishui Zhou, Sabreen Hammouda, Yinghao Zhu 等 · [2610.13444](https://arxiv.org/abs/2610.13444) · cond-mat.mtrl-sci · new

**为何相关：** 单晶中子衍射显示面内场可把六畴 α-MnTe 几乎对齐到单一取向畴，饱和约 2 T——altermagnetism 畴操控 × 磁振子手性测量前序。

要点：交错磁零净磁化与动量依赖自旋劈裂兼备，但宏观响应常被畴平均抹掉。六角 α-MnTe 有三个对称相关的面内 Néel 取向及其时间反演副本，共六种磁畴，既妨碍磁结构精修，也干扰手性磁振子信号。作者用单晶中子衍射证明：沿 [-1,1,0] 施加面内场可诱导共同取向，约 2 T 饱和；2 K、2 T 下 61 个核/磁反射约束精修给出 M∥[1,1,0]、有序矩 4.62(8) μ_B/Mn，取向畴占比约 0.97:0.03:0，接近完全取向对齐。60–88 K 区间部分反射异常温依，作者在本征压磁/磁弹性效应框架内讨论。未极化衍射无法区分畴重布与 Néel 连续转动，也不能分辨时间反演反相畴，故场制备态是近单取向而非真单畴。相对应变与场冷，这是一种非接触畴控制，便于为体相 α-MnTe 准备更干净的磁态。库里已有 MnTe / 交错磁条目十余篇可作背景。

---

### 2. Dissipative Majorana Chain---Anomalies and Non-Invertible Symmetries
Hung-Hsuan Teh, Tokiro Numasawa · [2610.12607](https://arxiv.org/abs/2610.12607) · quant-ph · new

**为何相关：** 把 Lindblad 动力学的耗散 Majorana 链映射为加倍空间非厄米算符，诊断强/弱对称与 mod-8 异常，并导出带非可逆 Kramers–Wannier 对称的 Ising Lindbladian——开放系统 × 拓扑异常。

要点：作者研究 Lindblad 动力学下耗散 Majorana 链的对称与异常：算符–态映射把 Lindbladian 写成加倍 Hilbert 空间上的非厄米算符；ket/bra 轮廓各自带强费米宇称与强平移，对角组合给出弱对称。偶长与奇链长，通过有无弱费米宇称缺陷时的对称代数对比诊断异常：代数保留闭链 mod-8 异常的格子前驱，并出现开放系统特有的强费米宇称–弱平移、弱费米宇称–强平移之间的投射关系。进一步建立格子对称代数与加倍 Majorana CFT 四个自旋扇区的红外对应，并做耗散链的格子玻色化：偶长加集体能量退相干，合并缺陷/无缺陷扇区并施加 GSO 投影，得到带非可逆 Kramers–Wannier 对称的 Ising Lindbladian；奇长则构造互相可对易的 ket/bra 自旋算符，得到带 KW 对偶缺陷的 Ising Lindbladian。工作把格子异常与非可逆对称系统地推广到开放量子系统。库里 Majorana / Lindblad / 非厄米文献很厚。

---

### 3. Locality-Preparation Time Tradeoffs in Dissipative Quantum Systems
Philipp Westhoff, Sara Murciano, Mattia Moroder · [2610.13784](https://arxiv.org/abs/2610.13784) · quant-ph · new

**为何相关：** 对二次费米子给出耗散制备中“跳跃算符局域性 ↔ 制备时间”的精确权衡，并以 Kitaev 链区分临界与拓扑能隙相——开放系统态制备 × 拓扑。

要点：耗散态制备把多体态工程为开放系统稳态；所需耗散的空间力程既决定模拟实现可行性，也决定数字实现的连通与控制复杂度，但局域性如何定量约束制备时间此前不清楚。作者对二次费米子系统建立精确的局域性–制备时间关系，并给出在保持目标态的同时优化耗散局域性的构造。应用到 Kitaev 链：临界相中若压掉跳跃算符的代数尾巴，制备时间必须随系统尺寸代数增长；平凡与拓扑能隙相则允许指数局域耗散，热力学极限下制备时间仍有限。结论划清了“快制备与局域控制兼容”与“临界性施加不可避免动力学代价”的边界。库里已有 dissipative preparation of Chern insulators 等可对照。

---

### 4. Alter-excitons in Altermagnets: Symmetry, Splitting and Dispersion
Yuanfan Xiong, Liangyu Wang, Xuan Wu, Wei Hu 等 · [2610.12900](https://arxiv.org/abs/2610.12900) · physics.comp-ph · cross

**为何相关：** 交错磁自旋空间群对称在激子谱中可内禀抬起电子能带的简并，预言无需 SOC 的自旋劈裂“alter-exciton”——altermagnetism × 多体激子。

要点：自旋空间群（SSG）理论把交错磁定位为非相对论共线磁体中自旋依赖电子结构独特的一类。作者指出：准粒子与两体哈密顿量虽共享同一 SSG，但电子能带中受对称保护的简并可在特定动量的激子谱中被内禀抬起；劈裂仅来自激子的多体本性，无需自旋–轨道耦合或非共线磁序。结合对称分析与多体微扰论，预言一类自旋劈裂激子准粒子（alter-exciton）及其特征色散，把激子确立为探测隐藏自旋空间对称的灵敏探针。交叉投稿，材料/计算物理主线。

---

### 5. Altermagnetic Control of Charge-4e Superconductivity
Yan-Guang Yue, Jie Lou, Yan Chen · [2610.13584](https://arxiv.org/abs/2610.13584) · cond-mat.supr-con · new

**为何相关：** 在交错磁结耦合的二维常规超导阵列中，首次理论实现独立的电荷-4e 相——altermagnetism × 非常规超导相干。

要点：作者给出（据称）首次在二维经典超导阵列中、经交错磁结耦合实现独立电荷-4e 相的理论方案：调节交错磁劈裂压低主导单对隧穿谐波，同时保留强双对耦合，从而在交错与均匀电荷-2e 态之间打开有限的电荷-4e 区域。完整温依微观 Josephson 谱显示：普通对关联短程，而“Cooper 对之对”呈代数相干；BKT 标度与半通量响应进一步指认该相。工作把交错磁定位为在普通与复合超导相干之间做微观选择的手段。

---

### 6. Realizing Two-Dimensional Altermagnets with 100% Spin Polarization along the [110] Direction in Ambidentate-Ligand Based Square Organometallic Lattices
Qing-Bo Liu, Xin-Yi Chen, Xiangyang Li, Xingxing Li 等 · [2610.12791](https://arxiv.org/abs/2610.12791) · cond-mat.mtrl-sci · new

**为何相关：** 用两性配体构筑方形有机金属格子，提出可实验跟进的二维交错磁设计，并实现 [110] 方向价/导带边 100% 自旋极化——altermagnetism 材料设计。

要点：交错磁零净矩与非相对论自旋劈裂兼得，但简单可实验的设计路径、以及价/导带沿特定方向 100% 自旋极化仍具挑战。作者基于紧束缚模型，提出用两性配体构筑有机金属交错磁的化学策略；在这些格子中，交错磁自旋劈裂的色散带与平带共存，可使 [110] 方向带边出现方向依赖的 100% 自旋极化——平带抑制一自旋通道输运、色散带承载另一通道。方向偏实验可行的二维材料设计，与库里“二维交错磁各向异性自旋流”等条目同线。

---

### 7. Exact solutions of non-Markovian dissipative Ising models
Mohammad Maghrebi · [2610.12546](https://arxiv.org/abs/2610.12546) · quant-ph · new

**为何相关：** 给出一类带非马尔可夫动力学与马尔可夫耗散的多体 Ising 精确可解模型——开放系统 / 非马尔可夫。

要点：量子器件与模拟器既要准确刻画动力学，也要理解环境噪声；部分噪声可建模为马尔可夫耗散，但与谐振腔或振动模耦合常带来非马尔可夫动力学，多体时尤难。作者识别出一类同时具有非马尔可夫动力学与马尔可夫耗散的精确可解多体量子系统：自旋耦合到有损耗玻色模、由后者介导 Ising 型相互作用；不含横场，但允许与相互作用不对易的局域自旋耗散（退相干、弛豫、抽运乃至产生相干的过程）。借助精确随机表示解耦玻色模，得到可解析推进的随机有效自旋动力学。为开放多体噪声刻画提供可严格对标的基准。库里有非马尔可夫量子轨迹与耗散半经典动力学等经典条目。

---

### 8. Engineering Ergodicity-Breaking and Stable Emergent Conservation Laws in a Generic Quantum Many-body System Under Strong Periodic Drive
Sagnik Chaudhuri, Anirban Das, Asmi Haldar, Arnab Das · [2610.12551](https://arxiv.org/abs/2610.12551) · quant-ph · new

**为何相关：** 在强周期驱动下识别遍历破缺条件，并用局域工程稳定 Dynamical Freezing，同时对比 Floquet 有效哈密顿量的非局域/准局域结构——Floquet × 多体。

要点：参数同量级时，周期驱动多体系统通常按遍历假说趋向局域无穷温；驱动超过阈值后，一类系统可出现 Dynamical Freezing（DF）：涌现永久记忆初值的局域算符而破缺遍历。近期有工作指出 DF 的例外。本文识别强驱动下遍历破缺的条件，并说明如何通过精确的局域工程稳定 DF；进一步表明：非 DF 系统中按自旋翻转排序的 Floquet 哈密顿量 H_eff=(i/T)ln[U(T)] 非局域，而在 DF 系统中变为准局域。对关心 Floquet 工程与加热抑制的读者是直接可跟的理论文。

---

### 9. Operational signatures of exceptional quantum channels
Paulo A. Brandão · [2610.13622](https://arxiv.org/abs/2610.13622) · quant-ph · new

**为何相关：** 不依赖哈密顿量或主方程，直接从 CPTP 量子信道的 Jordan 链定义“例外信道”，并把例外点与可测概率的多项式–指数时间结构挂钩——例外点 / 开放系统操作表述。

要点：例外点通常作为非厄米哈密顿量（或开放系统中 Liouvillian）的缺陷简并引入。作者给出不调用哈密顿量或主方程的操作理论：原初对象是完全正、保迹（CPTP）信道 Φ 的整数次迭代，物理数据是态与可观测量的概率序列。通过 Φ 的非平凡 Jordan 链定义例外信道，并证明阶为 m 的 Jordan 块产生最高次数 m−1 的离散多项式–指数项，从而把例外点物理与实验可直接测量的量对接。相对 Liouvillian EP 文献，这篇强调信道级、可操作的签名。库里有 Liouvillian EP 与非马尔可夫例外点等条目。

---

### 10. Utilizing Neural Networks for Solving Functional Renormalization Group Flow Equations
J. Gurzó, G. Fejős · [2610.13754](https://arxiv.org/abs/2610.13754) · hep-ph · cross

**为何相关：** 用 PINN 求解有限温度 O(N) 模型的函数重整化群流方程，不依赖大 N 近似——PINN / SciML × 多体场论。

要点：作者提出基于物理信息神经网络（PINN）求解函数重整化群（fRG）流方程的新方法，并在不依赖大 N 近似的情况下研究 O(N) 模型有限温度相变；论证此前类似大 N 解不易推广到更复杂对称。技术上串联小场/大场近似与神经网络 ansatz，在全场范围内给出高精度逼近；与传统网格 Runge–Kutta 对照，显示网络可成功学习局域势近似下有效势对温度、场与标度的依赖。对你关心的 PINN 物理求解器是直接可跟的方法交叉稿。库里 PINN≈28，另有神经网络–重整化群交叉条目。

---

### 11. Continuous-wave AC magnetometry up to hundreds of megahertz using nitrogen-vacancy centers under a strong transverse magnetic field
Ryusei Okaniwa, Rui Suzuki, Yuichiro Matsuzaki, Norio Tokuda 等 · [2610.13153](https://arxiv.org/abs/2610.13153) · quant-ph · new

**为何相关：** 强横向偏置下用连续波 ODMR 实现 NV 百 MHz 量级可调 AC 磁强计，规避高功率脉冲动力学解耦——量子传感 / NV。

要点：NV 是领先的 AC 磁场量子传感器，但传统动力学解耦在高频下要求越来越短、功率越来越高的微波脉冲。作者改用连续波光探测磁共振（CW-ODMR）：沿垂直于 NV 轴施加强静磁场，把相关电子自旋能级间距调到与目标射频共振，形成 RF 缀饰态，从而无需高功率脉冲序列。可探测频率由偏置场强度调节；实验实现 14.4–632 MHz 可调探测，灵敏度在 14.4 MHz 为 0.558 μT/√Hz、632 MHz 为 24.4 μT/√Hz。大横向场下对比度与线宽劣化是高频灵敏度的主要限制。给出一种简单、宽调谐的 CW RF 磁传感路线。库里有 NV 退相干与磁强计相关条目。

---

### 12. NucleoNet: A Nuclear-Aware Determinant Ansatz for Multi-Geometry Neural Variational Monte Carlo
Qiao Gao, Yang Huang, Enze Hou, Yuzhi Liu 等 · [2610.12985](https://arxiv.org/abs/2610.12985) · physics.chem-ph · cross

**为何相关：** 核–电子统一表示的神经波函数 ansatz（NucleoNet），单模型覆盖多几何的变分蒙特卡洛——NNQS / 神经 VMC。

要点：神经变分蒙特卡洛可高精度求解电子薛定谔方程，但许多神经波函数只针对单一核构型优化，势能面需反复重训。NucleoNet 把电子与核当作统一粒子集，经共享的电子–核骨干联合演化单体与两体表示；核携带可学习表示并条件化轨道构造，反对称性仅由电子行列式施加。平衡小分子基准上精度可比既有神经波函数基线而参数更少；对每个分子体系，单一模型联合优化即可描述 N₂ 解离曲线、LiCN 中 Li 位移，以及乙烷/甲酰胺键解离最小能量路径。稀疏几何训练可泛化到未见几何（N₂、LiCN），消融显示核流对插值帮助显著。交叉投稿，偏化学物理，但对 NNQS 多几何泛化是清楚信号。
