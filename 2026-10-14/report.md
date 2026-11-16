# 10/14 arXiv 兴趣摘要（工作日）

扫了今天（美西 10/14，周三）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Wednesday, 14 October 2026**；新投稿量偏大：cond-mat 260、quant-ph 170、hep-th 50、math-ph 24（cs.LG 502、stat.ML 51 只看物理/量子相关；交叉与替换未计入）——与周一原住民日假期后积压一致。10/13 凌晨仍停在周一 10/12 批次（空窗）；本批已换新，并排除了 10/12 已荐的 12 篇。开放系统一侧有耗散时间晶体的涌现量子代数、测地线式耗散纠缠加速制备、非厄米动力学约束 scar/Krylov、非厄米统计几何、MPS 靶向非厄米本征态与非厄米角态双扭折操控；交错磁有准晶 Ammann–Beenker 精确基态、交叉电场自旋产生（含 V2Te2O）、Cr1/4NbS2 单晶候选；另有半 Dirac + Floquet 拓扑输运、可编程 Floquet 传感，以及神经网络 VMC 下的蜂窝电子–空穴晶体。按兴趣锚点筛了 **12 篇**（全部为新投稿；未收替换稿）。本地桌面当时未在线，**未做 Zotero 核对**。

**建议先翻这三篇：**
1. **Emergent quantum algebras in dissipative time crystals** —— Lindblad 下耗散时间晶体的渐近量子代数：集体自旋极限中非衰减振荡模的构造与淬火纠缠——开放系统 × Floquet/时间晶体。
2. **Geodesic steering for rapid dissipative entanglement distribution** —— 用测地线式最优控制沿瞬时稳态轨迹加速耗散制备，把近最大纠缠态的制备时间压低数个量级——开放系统态工程 × 纠缠分发。
3. **Altermagnetic Ground States on the Ammann--Beenker Tiling** —— 准晶 Ammann–Beenker 铺砌上经典 Heisenberg 模型的精确交错磁基态，并以 g 波对称自旋分辨输运确证——altermagnetism 推广到非周期系统。

---

### 1. Emergent quantum algebras in dissipative time crystals
Joseph Tindall · [arXiv:2610.16609](https://arxiv.org/abs/2610.16609) · quant-ph · new

**为何相关：** Lindblad 下耗散时间晶体的渐近量子代数：集体自旋极限中非衰减振荡模的构造与淬火纠缠——开放系统 × Floquet/时间晶体。

要点：强动力学对称为 Lindblad 方程中的持续振荡提供代数描述；有限维、满秩稳态时，这类对称是 Liouvillian 谱出现非衰减振荡模的充要条件。作者对集体自旋给出渐近对应：单自旋 S 处于磁场并经线性跳跃算符耗散时，给出场与耗散耦合使非衰减振荡在 S→∞ 出现的精确条件，并写出可作用于稳态以构造这些模的闭式“对称”算符（虚本征值，O(1/S) 修正）。第二个涌现守恒量补全代数，其慢弛豫决定量子噪声如何选定稳态。推广到共享公共库的一对相互作用自旋后，该量子代数使淬火过程中的纠缠可解析触及。

---

### 2. Geodesic steering for rapid dissipative entanglement distribution
Keshav Venkataraman, Pablo Martinez-Azcona, Marko Ljubotina, Adrian Parra-Rodriguez 等 · [arXiv:2610.16854](https://arxiv.org/abs/2610.16854) · quant-ph · new

**为何相关：** 用测地线式最优控制沿瞬时稳态轨迹加速耗散制备，把近最大纠缠态的制备时间压低数个量级——开放系统态工程 × 纠缠分发。

要点：作者提出加速复杂高纠缠多体态耗散制备的最优控制：类似孤立系统最优转向，控制脉冲引导开放系统沿瞬时稳态轨迹演化，同时最小化非绝热泄漏。许多情形下控制参量可解析导出，无需数值求解完整多体主方程。应用于耦合公共波导或分布式压缩库的比特系统制备双/多方纠缠：相对淬火后的裸弛豫，近最大纠缠态制备时间可缩短数个量级，使耗散纠缠分发与高保真量子信息处理时间尺度兼容，并更广地说明泄漏最小化可加速库工程。

---

### 3. Altermagnetic Ground States on the Ammann--Beenker Tiling
SeungBeom Hong, YunHo Kim, Moon Jip Park, GiBaik Sim · [arXiv:2610.18441](https://arxiv.org/abs/2610.18441) · cond-mat.str-el · new

**为何相关：** 准晶 Ammann–Beenker 铺砌上经典 Heisenberg 模型的精确交错磁基态，并以 g 波对称自旋分辨输运确证——altermagnetism 推广到非周期系统。

要点：作者利用母四维超立方格子的宇称结构，在 Ammann–Beenker 准晶铺砌上求得经典 Heisenberg 模型的精确交错磁基态：共面序由自旋群对称 [C_{2x}∥C_{8z}] 刻画。无平移对称时动量空间自旋劈裂不再直接可得，于是把自旋耦合到巡游电子，展示具有 g 波对称的自旋分辨输运，从而在非周期系统中确认交错磁本质。工作给出准晶中交错磁序的几何路径，把精确磁基态与自旋分辨输运签名连接起来。

---

### 4. Nontrivial topological properties from the cooperation of static perturbations and Floquet fields in type-II semi-Dirac semimetals
Wen-Hao Bian, Jing Wang · [arXiv:2610.16659](https://arxiv.org/abs/2610.16659) · cond-mat.mes-hall · new

**为何相关：** 静质量与双频正交偏振 Floquet 光协同，在 II 型半 Dirac 半金属中打开可调控 Chern 相与 Berry 曲率偶极——Floquet × 拓扑输运。

要点：对 II 型半 Dirac 半金属分别考察静对称破缺、双频正交偏振光（TFOPL）Floquet 驱动及其混合。静质量 m_z 打开体能隙并进入 Chern 绝缘体（C=±2 sgn(m_z)）；TFOPL 单独只移动 Dirac 点、不开满隙，但产生沿 x 的有限 Berry 曲率偶极。混合情形能隙关闭判据变为三次，可出现多重光可调能隙关闭点与一系列拓扑相变；BCD 在能隙关闭流形附近双峰增强并可整体反号。AHC/ATHC 的量子化平台标志 Chern 相，ANC 作为费米面探针可识别全局拓扑不变量未变时的光致能隙。

---

### 5. Krylov Complexity and Quantum Many-body Scars in Non-Hermitian Kinetically Constrained Models
Arkaprava Sil, Rudraksh Kaushik, Souvik Kundu, Prasant Mallik 等 · [arXiv:2610.17328](https://arxiv.org/abs/2610.17328) · quant-ph · new

**为何相关：** 非厄米 PXP/PPXPP 动力学约束模型中左右本征态系综的 Krylov 复杂度与 scar 结构分叉——非厄米 × 多体 scar。

要点：热化破缺在厄米动力学约束模型中已有大量研究，非厄米情形左右本征态系综不等价。作者考察非厄米推广的 PXP 与 PPXPP：随非厄米性增强，右系综 Krylov 复杂度保持周期渐长的持续振荡，左系综逐渐饱和；Arnoldi 系数的拱形轮廓在两系综中被不同地改写。非厄米 PXP 中右系综保留特征 scar，左系综则出现与真空大重叠、纠缠异常低的额外非 scar 本征态。结论强调刻画非厄米动力学约束系统时必须分开处理左右系综。

---

### 6. Non-Hermitian Statistical Geometry
Xi Hu, Yan-Qiong Ma, Su-Peng Kou · [arXiv:2610.18175](https://arxiv.org/abs/2610.18175) · cond-mat.str-el · new

**为何相关：** 放松厄米性后，二维粒子交换的编织/融合数据软化为谱与相对几何自由度更大的复空间——非厄米统计几何 × 拓扑。

要点：二维粒子交换超越玻色–费米二分，在分数量子霍尔、拓扑量子计算与强关联物态中居核心；常规拓扑相把微观交换几何压缩为刚性编织与融合数据。作者发展非厄米统计几何：放松厄米性后，交换数据软化为更大的谱与相对几何自由度复空间。对两个相邻编织生成元，单一射影参数即可连续插值统计相与相对几何；由此讨论非厄米设定下任意子交换、谱简并与几何相位的相互制约，为开放/增益损耗系统中的统计拓扑提供几何语言。

---

### 7. Crossed Electric Spin Generation in Multilayers
Xukun Feng, Wei Du, Jin Cao, Qian Niu 等 · [arXiv:2610.14668](https://arxiv.org/abs/2610.14668) · cond-mat.mtrl-sci · new

**为何相关：** 多层中交叉电场自旋产生：杂化 Berry 曲率给出全电自旋操控，并在铁磁 Fe3GeTe2 与交错磁 V2Te2O 中预言可观信号——altermagnetism × 自旋轨道。

要点：提出多层结构中的交叉电场自旋产生效应：结合面内场与栅极场操控自旋，并揭示准二维体系特有的杂化 Berry 曲率几何（自旋–层–轨道耦合）。结合第一性原理，预言二维铁磁 Fe3GeTe2 与交错磁 V2Te2O 中有可观自旋产生，为二维材料全电自旋操控开辟 Berry 曲率新路径。

---

### 8. Matrix-product-state GPLHR for non-Hermitian many-body eigenproblems
Xingyao Wu, Zhangyu Yang, Yanbin Chen, Yu Wang 等 · [arXiv:2610.15387](https://arxiv.org/abs/2610.15387) · cond-mat.str-el · new

**为何相关：** 把 GPLHR 嵌进 MPS，高效求非厄米多体算符在复平面指定移位附近的多个右本征态——非厄米多体 × 张量网络。

要点：非厄米多体算符的多本征态对激发谱、谱性质与开放系统弛豫动力学很重要，但本征向量一般非正交且维数指数增长。作者在 MPS 框架下表述广义预条件局部谐波残差（GPLHR），高效计算本征值落在复平面指定移位附近的多个目标右本征态，并用逐次随机压缩加速算符作用。在超关联/复 Hubbard 链、相互作用非厄米 SSH 链与 Liouvillian 模型上验证，显示可扩展到相互作用与开放量子系统中的靶向谱计算。

---

### 9. Non-Hermitian Two-Kink Control of Corner States in Twisted Chern Bilayers
Xiao-Ming Zhao, Su-Peng Kou · [arXiv:2610.15470](https://arxiv.org/abs/2610.15470) · cond-mat.other · new

**为何相关：** 非厄米层间质量相位扭折与虚动量扭折分工，实现对扭转 Chern 双层角态的谱/面内/层自由度分离操控——非厄米 × 拓扑角态。

要点：角态通常由边界质量缺陷锚定，空间与内部自由度受限。作者聚焦相反 Chern 数绝缘体组装的扭转双层：非厄米层间质量携带的质量相位扭折与独立的虚动量扭折，分别控制质量缺陷角态的谱、面内包络与层极化。质量相位扭折产生母角极并固定能量与本征衰减，定向层间隧穿编码层极化；虚动量织构则重塑闭合边界包络并在角之间重分配右态权重。扭转 Qi–Wu–Zhang 双层与 30° 扭转 Haldane 十二边形验证了该分工，包括凹边界上的有限能母态。

---

### 10. Programmable Floquet Response for Quantum Sensing
Dionisio Cendoya, Kang Xu, Lisandro Buljubasich, Carlos A. Meriles · [arXiv:2610.17156](https://arxiv.org/abs/2610.17156) · quant-ph · new

**为何相关：** 用可编程 Floquet 锁定把传感信息编进驱动布居弛豫而非相位积累，做直流与频率选择交流传感——Floquet × 量子传感。

要点：常规量子传感依赖相位积累，因而受相干时间束缚。作者提出基于周期驱动两能级系统中可编程 Floquet 锁定的替代范式：周期控制生成有效 Floquet 锁定场，其取向与幅度依赖全局失谐，信息编入驱动布居弛豫动力学而非积分相位。通过在不同 Floquet 锁定流形间受控转移，外扰可映射为驱动序列可编程的工程弛豫响应。数值演示了直流与频率选择交流传感，并显示响应的时间编码可在相干受限设定下提升精度。

---

### 11. Honeycomb Crystal in a Mass-Asymmetric Electron-Hole Bilayer
Shengdu Chai, Wangqian Miao, Yuqiang Li, Lei Wang 等 · [arXiv:2610.17030](https://arxiv.org/abs/2610.17030) · cond-mat.str-el · new

**为何相关：** 质量强不对称电子–空穴双层中，实空间神经网络 VMC 发现蜂窝电子–空穴晶体并给出异质结平台——NNQS × 强关联。

要点：均匀中和背景下的二维电子气低温形成三角 Wigner 晶体；质量强不对称电子–空穴双层中，局域重空穴提供非均匀正背景，使电子晶体可在高两个量级的密度稳定。作者用 Born–Oppenheimer 极限下固定空穴的实空间神经网络变分蒙特卡罗发现：升密度可驱动三角电子–空穴晶体到蜂窝晶体，最终熔化为与蜂窝/三角空穴格子共存的巡游电子。相对三角序，蜂窝序在电子动能与电子–空穴吸引增益压过更高层内库仑排斥时出现；蜂窝空穴格子还支持顺磁/反铁磁/条纹自旋态。并提议 BLG/hBN/WS2–WSe2 异质结作为实验可行平台（n∼10^11 cm^-2）。

---

### 12. Crystal growth, magnetic, and transport properties of the candidate altermagnet Cr$_{1/4}$NbS$_{2}$
Nashra Pistawala, Martin R. Lees, Geetha Balakrishnan, Daniel A. Mayoh · [arXiv:2610.17452](https://arxiv.org/abs/2610.17452) · cond-mat.mtrl-sci · new

**为何相关：** 候选交错磁 Cr1/4NbS2 高质量单晶生长及结构/热/磁/输运表征，Néel 点约 141 K——altermagnetism 实验候选。

要点：交错磁候选实验确认仍然稀少。Cr1/4NbS2 早被理论提出为有希望的交错磁，但此前缺单晶实验。作者成功生长高质量单晶，给出结构、热、磁与输运性质：单晶 XRD 确认六角对称（P6_3/mmc，交错磁判据之一）；电阻率与比热明确反铁磁 Néel 温度 T_N∼141 K；磁输运显示磁阻与霍尔响应中的非平凡特征。为该候选材料的后续光谱与自旋劈裂探测提供单晶基础。
