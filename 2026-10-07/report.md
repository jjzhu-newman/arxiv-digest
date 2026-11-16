# 10/7 arXiv 兴趣摘要（工作日）

扫了今天（美西 10/7，周三）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。新投稿量：cond-mat 85、quant-ph 64、hep-th 30、math-ph 12（cs.LG 196、stat.ML 28 只看物理/量子相关；交叉与替换未计入）。今天非厄米拓扑本身偏少，交错磁和 Floquet/拓扑序比较出彩。按兴趣锚点筛了 **12 篇**（全部为新投稿，未收替换稿）。核对了本地 Zotero 库（只读副本），12 篇都不在库里；RuO₂、MnTe 交错磁和 Z_N parafermion 方向库里已有不少相关文献，相应条目里有标注。

**建议先翻这三篇：**
1. **Chiral Parafermions in Floquet $\mathbb{Z}_N$ Topological Order** —— Z_N Kitaev 模型里的 Floquet 拓扑序与手性 parafermion 边缘模（Knap、Pollmann 组）——Floquet × 拓扑序。
2. **Geometric Photon-drag Effect in Unconventional Magnets** —— p 波磁体与 d 波交错磁中直流非线性光电流完全来自光子拖曳——altermagnetism × 量子几何。
3. **Neural Correlation Learning for Quantum-Enhanced Sensing with Time-Independently Driven Rydberg Atom Arrays** —— Rydberg 阵列不靠特定纠缠态，用神经网络从测量关联中提取信息实现超 SQL 传感——AI × 量子传感。

---

### 1. Chiral Parafermions in Floquet $\mathbb{Z}_N$ Topological Order
Melissa Will, Harald Schmid, Jan Egger, Adam Gammon-Smith 等 · [2610.07156](https://arxiv.org/abs/2610.07156) · cond-mat.str-el · new

**为何相关：** 在三步周期驱动的 Z_N 时钟型 Kitaev 蜂窝模型里实现 Floquet 拓扑序，边界出现手性 parafermion 边缘模——Floquet × 拓扑序 × 任意子。

要点：作者用三步周期驱动在带时钟自由度的推广 Kitaev 蜂窝模型中实现 Z_N Floquet 拓扑序，体系可涌现地描述为与守恒 Z_N 规范场耦合的受约束 parafermion。边界上驱动产生手性 parafermion Floquet 边缘模，作者用关联函数追踪其传播，用 radical chiral unitary index 刻画分数量子信息输运，并借其动力学探测交换统计；体内则用非平衡环序参量研究动力学任意子嬗变。在驱动恰为 Clifford 的“甜点”可用稳定子模拟直接访问这些现象，偏离该点的短时 MPS 模拟表明手性边缘响应在可及时间内仍然存在，指向基于 qudit 处理器的实验实现。你库里有几篇 Z_N/Z_3 parafermion 链与 Fibonacci 任意子的工作，可作背景对照，但 Floquet 拓扑序方向库里还没有。

---

### 2. Geometric Photon-drag Effect in Unconventional Magnets
Bristi Ghosh, Vivek Pandey, Malay Bandyopadhyay, Pankaj Bhalla 等 · [2610.08767](https://arxiv.org/abs/2610.08767) · cond-mat.mes-hall · new

**为何相关：** 在 p 波磁体与 d 波交错磁（加 Rashba 自旋轨道耦合）中推导光子拖曳光伏流，发现非线性直流光电流完全由光子动量驱动——altermagnetism × 量子几何 × 非线性光学。

要点：作者在速度规范的密度矩阵框架下计入有限光子动量引起的非竖直跃迁，推导出光子拖曳光伏响应的非线性注入电导与位移电导。关键结论是：虽然反演对称性被破缺，常规（q=0）光伏响应在布里渊区积分后在两种非常规磁相中都恒为零，因此直流非线性光电流完全来自光子拖曳。两类磁体的响应由对称性区分：p 波磁体只支持线偏振注入与圆偏振位移电导，而同时破缺时间反演与反演的 d 波交错磁允许全部线偏与圆偏分量。作者据此把交错磁定位为对称性选择性非线性光电流和量子几何光伏的平台。

---

### 3. Neural Correlation Learning for Quantum-Enhanced Sensing with Time-Independently Driven Rydberg Atom Arrays
Tao Zhang, Xiaotian Nie, Linghui Chen · [2610.06961](https://arxiv.org/abs/2610.06961) · quant-ph · new

**为何相关：** 不制备特定纠缠态，只让乘积态在 Rydberg 阵列原生哈密顿量下演化，再用神经网络从测量图样关联中提取参数信息，达到超越标准量子极限的灵敏度——AI × 量子传感。

要点：量子增强传感通常依赖难以在大规模多体系统中稳健制备的特定纠缠态。作者指出，乘积态在 Rydberg 原子阵列不含时原生哈密顿量下演化即可产生复杂多体关联，原则上可支持逼近海森堡极限的参数估计，难点转移到如何从测量图样的空间关联中提取计量信息。为此提出“神经关联学习”框架：用校准数据训练神经网络并结合贝叶斯推断，在“校准–传感”两阶段协议中数值上饱和经典 Fisher 信息给出的 Cramér–Rao 界，实现超越 SQL 的灵敏度。学到的估计器对实际噪声稳健，缺少稀有测量图样时仍保持准确。

---

### 4. Open-System Probe Selection and Optimal Measurements for Dispersive Coupling Metrology
Achal Vinod, Da-Wei Luo, Ting Yu · [2610.07221](https://arxiv.org/abs/2610.07221) · quant-ph · new

**为何相关：** 腔–量子比特色散耦合强度估计中，光子损耗与环境记忆（非马尔可夫）如何改变最优探针与测量——开放系统 × 纠缠 × 量子计量。

要点：作者用密度算符与量子态扩散方法，计算可分与纠缠初态在马尔可夫与非马尔可夫情形下估计色散耦合强度的量子 Fisher 信息。结果表明封闭系统生成元方差并不能单独决定开放系统中的表现，参数敏感相干的存活与环境记忆同样关键；在所考察的单光子制备中，可分探针甚至可以优于所选纠缠态族。等平均光子数下比较相干态与压缩真空态，展示了光子数统计与比特制备的影响；有限环境记忆可增强并延长灵敏度，甚至让马尔可夫下 QFI 为零的探针获得非零 QFI。作者还数值找到一个固定厄米可观测量，在马尔可夫情形下其误差传播不确定度在给定耦合区间内贴近量子 Cramér–Rao 界。

---

### 5. Conditions for Altermagnetism in RuO2
Himanshu Mavani, Zhonglin He, Evgeny Y. Tsymbal · [2610.07494](https://arxiv.org/abs/2610.07494) · cond-mat.mtrl-sci · new

**为何相关：** 系统梳理 RuO₂ 是否真是交错磁的争议，并用第一性原理指出外延应变是稳定交错磁态的首要因素——altermagnetism 材料现实性。

要点：RuO₂ 的磁基态至今有争议。作者结合对已有实验与理论的批判性评估和第一性原理计算（外延应变、点缺陷、掺杂、界面），指出文献中体敏感测量与非磁基态一致，而薄膜中的磁性信号强烈依赖结构环境，并不必然代表均匀的交错磁序。计算表明衬底施加的外延应变是所考察条件中最有利于交错磁的因素，并预言若干稳定交错磁基态的衬底–取向组合；均匀空穴掺杂增强磁性倾向，Ru 空位作用不大甚至因局域畸变削弱磁性，Cr/Mn 替代则增强 Ru 磁矩并进一步稳定应变诱导的交错磁相。你库里已有几十篇 RuO₂ 相关条目（含“Revisiting altermagnetism in RuO2”等），这篇适合作为争议的综述性更新。

---

### 6. Odd-parity magnon spin polarization from chiral four-spin exchange in a honeycomb antiferromagnet
Bektur Murzaliev, Mikhail Titov · [2610.07291](https://arxiv.org/abs/2610.07291) · cond-mat.str-el · new

**为何相关：** 补偿蜂窝反铁磁中手性四自旋交换在零场下产生动量奇宇称的磁振子自旋，并可由温度梯度诱导自旋密度——奇宇称（p 波类）磁振子自旋电子学。

要点：作者表明，在零磁场的补偿蜂窝反铁磁中，手性四自旋交换会产生依赖动量的磁振子自旋：当 Néel 矢量偏离层法向 θ₀ 时，该相互作用在谐波阶就贡献子格间磁振子配对，幅度 ∝ cosθ₀ sin²θ₀。双轴各向异性混合两个纵向自旋扇区，产生非量子化、对动量为奇的模式自旋，而子格交换关系使磁振子能谱保持互易。温度梯度通过重新分布磁振子占据在 Néel 轴方向诱导自旋密度，反转四自旋耦合会反转该自旋密度与模式自旋而不改变能谱。MnPS₃ 提供了磁结构动机，但实现该相互作用需要满足对称性假设的结构修饰。库里有“P-wave magnetism in a metal”“Odd-parity magnetism driven by antiferromagnetic exchange”等，可对照阅读。

---

### 7. Charging Dicke and Tavis--Cummings quantum batteries with a $\mathcal{PT}$-symmetric lossy--gain cavity pair
Shiqing Tang, Qing Yu, Ying Li, Cuilu Zhai 等 · [2610.07921](https://arxiv.org/abs/2610.07921) · quant-ph · new

**为何相关：** 把 Dicke/Tavis–Cummings 量子电池耦合到 PT 对称增益–损耗腔对，分析例外点两侧的充电能量、功率与可提取功——非厄米 EP × 开放系统。

要点：作者先给出集体基态原子在腔中充电时激发数随时间平方增长、Tavis–Cummings 储能存在由总激发数守恒给出的严格上限，并说明反旋转项在超强耦合下略微越过该上限。随后在增益–损耗腔对中各放一个相同电池以保持 PT 对称，闭合矩方程把例外点定在损耗率处。用批量蒙特卡洛波函数求解完整 Lindblad 方程发现：在破缺相中增益侧电池储能、功率与 ergotropy 分别提高约 39%、26%、28%，深入未破缺相则分别下降约 65%、35%、65%，损耗侧电池反超；反旋转项只增加一个两倍跃迁频率的无功振荡，使瞬时功率峰值近乎翻倍但可回收比例从约 98% 降到约 90%。最优点位于破缺一侧、靠近但不在例外点上。

---

### 8. Chiral Central Charge from Real-Space Twist Operator Correlator
Yunlong Zang · [2610.08788](https://arxiv.org/abs/2610.08788) · cond-mat.str-el · new

**为何相关：** 用多副本扭转算符关联函数的相位直接给出二维带隙体系的手性中心荷——纠缠结构 × 手性拓扑相的实空间判据。

要点：作者针对二维有隙量子体系提出基于扭转算符关联 Z_{g,h} 的手性中心荷实空间公式：在 N 副本态上，扭转算符按置换 g 在区域内重排副本，对满足“球面条件”的 (g,h)，关联函数相位由手性中心荷 c₋ 决定，即 (θ_g θ_h/θ_{gh})^{c₋}，其中 θ_g 是扭转缺陷的拓扑自旋。该构造对玻色与费米体系均适用，在一定假设下由场论推导，并在微观格点模型上数值检验，为直接在格点上刻画手性拓扑相提供了基于纠缠结构的系统框架。

---

### 9. Connectivity Controls Variational Accessibility in Symmetry-Preserving Quantum Circuits
Sahinur Reja · [2610.07173](https://arxiv.org/abs/2610.07173) · quant-ph · new

**为何相关：** 保对称 VQE 线路的生成元连通性决定其动力学李代数能否覆盖完整对称扇区，一处次近邻连接即可让 XXZ 的可及性“重建”——变分量子算法 × 多体物理。

要点：作者指出即使是保对称的变分线路也未必能访问完整的多体对称扇区：以自旋 1/2 XXZ 与 Hubbard 模型为例，受哈密顿量启发的最近邻保对称线路只生成受限的动力学李代数，在自由费米极限附近尚能表示基态，但相互作用一开就暴露出不可达的多体方向，深线路也无济于事。对生成元连通性做极小修改即可在所有相关扇区重建完整正交 DLA：XXZ 只需增加一个保对称次近邻单激发连接，Hubbard 则需保对称关联双激发，说明关键连通性可从实空间晶格延伸到多体组态空间。重建后切空间扩大，VQE 基态保真度接近 1；作者由此提出“找极小保对称生成元扩大可及空间，而非一味加深线路”的设计原则。

---

### 10. Soft Contrastive Learning for Unsupervised Discovery of Phases of Matter
Vít Beneš, Pavel Baláž, Dmytro Bohdanov, Jiří Hlinka · [2610.08116](https://arxiv.org/abs/2610.08116) · cond-mat.dis-nn · new

**为何相关：** 把物理描述符与对比表示学习结合、并以梯度优化生成稠密数据，实现未知相结构体系的无监督相图构建——机器学习 × 凝聚态相变。

要点：作者提出一个面向相结构未知的凝聚态体系的机器学习相图构建框架：先用蒙特卡洛模拟退火生成稀疏构型训练对比神经网络得到低维嵌入，再以代表性相构型为初值在稠密参数网格上做梯度优化，高效生成精细数据集以构建高分辨率相图。作者还考察了以导出描述符作软标签的对比目标变体，并在 PbZrO₃ 启发的耦合序参量场模型上演示。你库里有 Carrasquilla 等的“Machine learning phases of matter”，这篇可看作无监督、物理信息化的延伸。

---

### 11. $\mathcal{PT}$-symmetry as Effective Time Reversal Symmetry for Anderson Localization in a Collinear Antiferromagnet
Kim-Khuong Huynh, Takuma Ogasawara, Motoi Kimata, Sofie Søby Leiszner 等 · [2610.06951](https://arxiv.org/abs/2610.06951) · cond-mat.other · new

**为何相关：** 实验显示反铁磁 BaMn₂Bi₂ 中 PT 对称充当 Anderson（弱）局域化的有效时间反演对称——反铁磁对称性 × 量子输运。

要点：作者在长程磁序已破缺普通时间反演的反铁磁 BaMn₂Bi₂ 中发现，PT 对称扮演控制 Anderson 局域化的有效时间反演对称。磁电导遵循通过载流子与矢势轨道耦合破缺时间反演的规律，但破缺程度受稳定 PT 相关子格的磁晶各向异性调制：横向磁场容易使 PT 相关磁子格倾斜，显著削弱量子干涉与跳跃振幅，而沿子格方向的纵向场对局域化影响很小。由此 PT 保护简并的稳健性由交换与磁晶相互作用决定，而非由任意有限场都会破坏的整体哈密顿量严格 PT 对称决定。注意这里的 PT 指反铁磁中的空间–时间联合对称，不是非厄米 PT。

---

### 12. Unraveling hidden Raman modes in $α$-MnTe: Effects of long-range dipole-dipole interactions on phonon bands
Susmita Jana, Rajib Sarkar, Dhavala Suri, B.R.K Nanda · [2610.08221](https://arxiv.org/abs/2610.08221) · cond-mat.mtrl-sci · new

**为何相关：** 计入长程偶极–偶极相互作用后重新计算交错磁 α-MnTe 的声子能带与拉曼谱，解释几处有争议的拉曼峰——altermagnetism 候选材料的谱学细节。

要点：针对交错磁 α-MnTe 实验与理论拉曼谱的不一致，作者指出必须计入长程偶极–偶极相互作用才能准确得到声子能带并重现全部实验拉曼特征。长程修正显著改变高频光学模及其群论表示：对争议较大的约 175 cm⁻¹ 峰，除拉曼沉默的 B₁u 模外，还引入拉曼活性的纵光学 A′、A₁ 与横光学 A₁ 模，这些模在纯净体系中强度较弱、特定畸变可增强。约 140 cm⁻¹ 峰被归为布里渊区非中心贡献的高阶拉曼过程，约 120 cm⁻¹ 峰则兼有区中心与非中心贡献。你库里有十来篇 MnTe 交错磁相关条目，这篇偏声子与谱学细节。
