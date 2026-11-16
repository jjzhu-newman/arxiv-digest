# 9/25 arXiv 兴趣摘要（工作日）

扫了今天（美西 9/25，周五）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。新稿量：cond-mat 约 93、quant-ph 约 74（另有交叉与替换未计入主计数）。按兴趣锚点筛了 **11 篇**，全部为今日新投稿（未收替换稿；高分替换里有一篇交错磁 SOC 与一篇非厄米纠缠未挤进终选）。用户机器 DESKTOP-00O6NSD 在线，已对本地 Zotero 只读核对：**11 篇均未见于库中**。

**建议先翻这三篇：**
1. **Altermagnetic Kondo Logic via Floquet Symmetry Conversion** —— Floquet 对称性转换把交错磁动量依赖自旋劈裂做成局域可探测的 Kondo 通道，并引出对称控 Kondo 逻辑——altermagnetism × Floquet 的直接交叉。
2. **Nonequilibrium Dirac condensate in bosonic Kitaev chain** —— 玻色 Kitaev 链上非平衡 BEC 的 Bogoliubov 激发映射为非厄米 Dirac 哈密顿量，并出现例外 Majorana 玻色子——非厄米拓扑 × Kitaev。
3. **Nonorthogonal variational quantum simulation for quantum chemistry** —— 非正交变分量子模拟（NOVQS）用参数化量子态线性组合做实/虚时演化，对标张量网与神经量子态在动力学上的纠缠增长瓶颈——NNQS/QML 动力学线。

---

### 1. Altermagnetic Kondo Logic via Floquet Symmetry Conversion
Haojie Shen , Xinchen Zhou , Baigeng Wang , Rui Wang · [2609.28680](https://arxiv.org/abs/2609.28680) · cond-mat.str-el · new

**为何相关：** Floquet 对称性转换把交错磁动量依赖自旋劈裂做成局域可探测的 Kondo 通道，并引出对称控 Kondo 逻辑——altermagnetism × Floquet 的直接交叉。

要点：交错磁中动量依赖自旋劈裂在局域杂质谱上对称抵消，常规单杂质 Kondo 共振对 altermagnetic form factor 近乎“盲”。面内交流场实现 Floquet 对称性转换，把隐藏的交错磁自旋劈裂转为局域可探测的自旋依赖杂化通道，并被 Kondo 关联放大成新型交错磁 Kondo 效应。Kondo 劈裂随场取向非平凡变化，继承宿主晶体 form factor，可作交错磁自旋劈裂的 Kondo 层析；场控响应自然通向对称控 Kondo 逻辑门。

---

### 2. Nonequilibrium Dirac condensate in bosonic Kitaev chain
Kazuki Yamamoto , Youichi Yanase · [2609.29082](https://arxiv.org/abs/2609.29082) · cond-mat.mes-hall / cond-mat.quant-gas · new

**为何相关：** 玻色 Kitaev 链上非平衡 BEC 的 Bogoliubov 激发映射为非厄米 Dirac 哈密顿量，并出现例外 Majorana 玻色子——非厄米拓扑 × Kitaev。

要点：平均场下配对强度超过临界后出现玻色超流，序参量在偶/奇格点取交替相位，自发产生子晶格序。子晶格自由度映为赝自旋后，元激发由非厄米 Dirac 哈密顿量描述：边界附近有重入玻色 Andreev 束缚态。临界点处出现例外 Majorana 玻色子的宏观简并，把非平衡凝聚与非厄米例外谱结构绑在同一平台。

---

### 3. Nonorthogonal variational quantum simulation for quantum chemistry
Zongkang Zhang , Jiajun Ren , Xiao Yuan · [2609.29337](https://arxiv.org/abs/2609.29337) · quant-ph · new

**为何相关：** 非正交变分量子模拟（NOVQS）用参数化量子态线性组合做实/虚时演化，对标张量网与神经量子态在动力学上的纠缠增长瓶颈——NNQS/QML 动力学线。

要点：张量网与神经量子态在基态很成功，但纠缠增长限制动力学；近端硬件又不支持大规模 Trotter。NOVQS 把演化态写成多个参数化量子态的线性组合，设计面向二量化电子结构哈密顿量的浅层硬件友好 ansatz，并给出参数运动方程中矩阵/矢量的省资源测量协议。含误差分析与资源估计；氢链等数值表明可在固定浅层线路尺寸下推进实/虚时量子化学动力学。

---

### 4. Antisymmetric breathing in altermagnetic skyrmions
Yunxi Jiang , Chen Xuan , Xi Chen , Zhikai Wang , Qinfeng Zhu 等 · [2609.29190](https://arxiv.org/abs/2609.29190) · cond-mat.mes-hall · new

**为何相关：** d 波交错磁中 skyrmion 双子晶格椭圆织构的反对称呼吸模，把 altermagnetism 与拓扑自旋织构动力学接起来。

要点：d 波交错磁 skyrmion 由长轴正交的两个椭圆子晶格织构组成；有效半径 R_η=√(a_η b_η) 刻画各子晶格尺度。垂直磁场使一子晶格膨胀、另一收缩，产生半径差与净磁矩；单轴应变型交换调制在零场也可诱导半径差。因强弱交换方向在双子晶格上互换，同向交换变化使半径此消彼长，支撑反对称呼吸动力学，有别于常规铁磁 skyrmion。

---

### 5. Eigenoperator Entanglement Statistics in Local Lindbladians
Ze-Kai Hong , Xu Feng , Zhi-Cheng Yang · [2609.29215](https://arxiv.org/abs/2609.29215) · cond-mat.stat-mech / quant-ph · new

**为何相关：** 局域 Lindbladian 本征算符的算符纠缠统计：开放系统混沌是否伴随 Haar 典型本征算符——Liouvillian × 纠缠诊断。

要点：用 KL 散度检验近最大纠缠 Liouvillian 本征算符是否贴近 Haar；Ginibre 与 AI† 高斯系综可用随机矩阵描述。纯耗散随机 Lindbladian 中，跳跃算符局域性剧烈改变统计：非局域仍接近 Haar，局域则随尺寸偏离随机矩阵。与哈密顿系统不同，局域 Lindbladian 最高纠缠本征算符未必落在态密度最大区，因复本征谱呈团簇结构；并给出 σ-clipping 抽取高纠缠分布的方案。

---

### 6. Amplified Memory and Finite-Time Regularity in Driven Non-Hermitian Systems
H. Yavartanoo , R. Jafari , Alireza Akbari · [2609.29137](https://arxiv.org/abs/2609.29137) · cond-mat.stat-mech / hep-th / quant-ph · new

**为何相关：** 驱动非厄米费米子（失衡配对 Kitaev 链）中破缺谱区与例外点对有限时记忆放大与关联正则性的不同角色。

要点：用 Nambu 双正交关联矩阵追踪有限时驱动；瞬态穿过破缺谱区会放大制备记忆，即便终点回到实谱仍残留。扣除负失衡带来的静态非正谱基线后，超额由累积虚能作用量严格控制，并贯穿整个后斜坡时间窗。例外点物理不同：有限时传播子与子系统关联在例外终点附近仍完全正则，尽管准粒子能隙呈方根闭合。

---

### 7. Universal Counterdiabatic Quantum Sensing
Stewart Morawetz , Anatoli Polkovnikov · [2609.28631](https://arxiv.org/abs/2609.28631) · quant-ph · new

**为何相关：** 把灵敏度放在纠缠态制备过程本身，用普适反绝热驱动加速绝热制备，冲击标准量子极限——量子传感新路线。

要点：传统做法先制备脆弱纠缠再传感；本文主张传感增益来自制备纠缠态的过程本身。用对微观参数不确定更稳健的普适反绝热（universal counterdiabatic）加速绝热制备，相对常规 shortcut-to-adiabaticity 更抗失配。在玩具 Lipkin–Meshkov–Glick 模型上展示可超越标准量子极限的灵敏度。

---

### 8. Superconducting spin valve as a sensitive probe of spin-orbit coupling anisotropy
Pablo Tuero , Andreas Costa , Maria Varela , Yuan Lu , Jaroslav Fabian 等 · [2609.29244](https://arxiv.org/abs/2609.29244) · cond-mat.supr-con · new

**为何相关：** 外延超导自旋阀面内低偏电导各向异性，实验拆分 Rashba / Dresselhaus SOC——自旋轨道 × 超导自旋电子学探针。

要点：Rashba（结构反演破缺）与 Dresselhaus（体反演破缺）SOC 共同决定二维/拓扑体系中的自旋相干与操控，需可靠拆分。在 Fe/MgO/V/MgO/Fe/Co 外延结中测温度与磁场依赖的面内低偏电导各向异性，并用区分 R-SOC / D-SOC 的理论模型解读。实验–理论对比给出 D-SOC 约占总量 5%，归因于高分辨表征所见的界面周期失配缺陷，可作为 SOC 各向异性的灵敏探针。

---

### 9. Disorder-induced quantum Fisher information in topological quantum systems
Advay Burte , Keshav Das Agarwal , Leela Ganesh Chandra Lakkaraju , Aditi Sen De · [2609.30142](https://arxiv.org/abs/2609.30142) · quant-ph / cond-mat.dis-nn / cond-mat.str-el · new

**为何相关：** Kitaev toric code 本征态对无序不敏感，但非本征基探针动力学可把无序变成量子 Fisher 信息资源——拓扑 × 量子计量。

要点：toric code 星/面算符对易，基态流形与耦合强度无关，弱局域微扰下拓扑序稳健；这是本征态性质而非动力学性质。用初态可分探针在含无序 toric code 哈密顿量下幺正编码，估计三类破拓扑微扰（Castelnovo–Chamon 形变、近邻 Ising、水平边磁场）。淬灭平均 QFI 在合适微扰强度与编码时间下可超过有序对照，把“本征不敏感、动力学敏感”做成计量优势。

---

### 10. Exact solution of a boundary-driven transverse-field Ising model with hidden time-reversal symmetry
Xudong Liu , Shu Chen · [2609.28994](https://arxiv.org/abs/2609.28994) · quant-ph · new

**为何相关：** 单边耗散驱动的横场 Ising 因隐藏时间反演对称可精确构造 NESS（矩阵积形式）——可解开放多体平台。

要点：一类仅在单边界耗散的边界驱动 TFI 具有隐藏时间反演对称，从而可精确构造非平衡稳态。解取矩阵积表示并定义非平衡配分函数，可高效算稳态观测量；z 磁化与两点关联刻画微观结构。耗散边界局域场主导整条链的空间组织：典型为边界局域磁化与指数衰减关联；弱驱动极限下调边界场可使 NESS 重组为离域结构。

---

### 11. Variational Multi-Gaussian Quantum Trajectories
Zejian Li , Jacopo Tosca · [2609.30225](https://arxiv.org/abs/2609.30225) · quant-ph / cond-mat.stat-mech · new

**为何相关：** 变分多高斯量子轨迹把 TDVP 推广到量子态扩散/主方程轨迹，模拟相互作用玻色开放动力学——开放系统 × 变分方法。

要点：波函数 ansatz 为相干叠加的多个高斯波包，可解析组装变分运动方程，捕捉轨迹动力学与超越半经典的 Lindblad 演化。在 Bose–Hubbard 二聚体上系统基准，并推广到一维与二维扩展 Bose–Hubbard 晶格。二维晶格出现对称破缺相变，而一维链中缺席，展示方法对开放多体相图的分辨力。
