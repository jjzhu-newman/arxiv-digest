# 9/23 arXiv 兴趣摘要（工作日）

扫了今天（美西 9/23，周三）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。新稿量：cond-mat 约 161、quant-ph 约 148。按兴趣锚点筛了 **12 篇**（含 1 篇早前投稿、今日交叉上架的 MnTe 交错磁实验）。只读对照了本地 Zotero：这 12 篇的 arXiv 编号在库中均未命中，无高相似旧条，可放心当新发现看。

**建议先翻这三篇：**
1. **Nonlinear Spin Polarization Enables Néel Order Switching in Centrosymmetric Altermagnets** —— 中心对称交错磁里线性电流自旋极化被禁，本文用非线性通道 + SOC 给出可开关 Néel 序的电控路径，直接补 altermagnetism 器件缺口。
2. **Quantum Fisher information of driven-dissipative systems from Keldysh path integrals** —— 把驱动–耗散多体传感的量子 Fisher 信息接到 Keldysh 路径积分与半经典展开，开放系统 × Floquet × 量子传感一条线打通。
3. **Hyperbolic Restricted Boltzmann Machine Neural Quantum State** —— 非欧几里得非自回归 NQS，在体积律纠缠的量子 SK 模型上系统压过欧氏 RBM，并把纠缠谱复原到十几个数量级。

---

### 1. Nonlinear Spin Polarization Enables Néel Order Switching in Centrosymmetric Altermagnets
Sunit Das, Sayan Sarkar, Amit Agarwal · [2609.26709](https://arxiv.org/abs/2609.26709) · cond-mat.mes-hall · new

**为何相关：** 中心对称交错磁不能靠线性电流写 Néel 序；非线性自旋极化 + SOC 打开的横向分量，正好是你关心的 altermagnetism / 自旋电子学可操控性。

要点：自旋群对称分析表明，非相对论极限下非线性自旋极化被约束在 Néel 方向，10 个非平凡自旋–Laue 群中有 8 个允许交错响应；该分量本身不产生力矩，但有限 SOC 可额外生成垂直于 Néel 的均匀分量。以 \(d\)-波 FeSb₂ 最小模型做 LLG 宏自旋模拟，展示可实现确定性 Néel 翻转。

---

### 2. Quantum Fisher information of driven-dissipative systems from Keldysh path integrals
Malik Jirasek, Igor Lesanovsky, Viktoria Noel · [2609.26462](https://arxiv.org/abs/2609.26462) · quant-ph / quant-gas · new

**为何相关：** 驱动开放系统要做量子增强传感，QFI 是判据；本文给出可扩展到多体自由度的场论计算路线。

要点：把 QFI 写成 Keldysh 路径积分，再对“量子场”做受控展开得到半经典公式。在驱动–耗散谐振子、临界与更复杂多体设定上做基准，说明何时相关性能帮助突破标准量子极限。把开放动力学、驱动与计量学收进同一框架。

---

### 3. Hyperbolic Restricted Boltzmann Machine Neural Quantum State
H. L. Dao · [2609.26032](https://arxiv.org/abs/2609.26032) · quant-ph / dis-nn · new

**为何相关：** 神经网络量子态（NQS）与体积律纠缠是你长期关注的交叉；本文把双曲几何嵌进非自回归 RBM。

要点：在量子 Sherrington–Kirkpatrick 模型上，系统尺寸 \(N=14\to24\)（希尔伯特空间增大约 512 倍）时，双曲 RBM 在基态能量优化以及 Renyi-2 / von Neumann 纠缠熵绝对误差上都压过欧氏 RBM。更能把整个纠缠谱从最大本征值复原到尾部约 15 个数量级，展示更强表达力。

---

### 4. Measure-zero delocalization in the complex plane: exact mobility arcs in a non-Hermitian off-diagonal quasiperiodic lattice
Fu-Xi Zhong, Yi-Cai Zhang · [2609.25877](https://arxiv.org/abs/2609.25877) · 非厄米准周期 · new

**为何相关：** 复能平面上的迁移率边/弧是非厄米安德森局域化的核心几何；本文给出精确 Lyapunov 指数与完整相图。

要点：把近期 Hermitian mosaic 模型延拓到非厄米非对角准周期无序。用 Avila 全局理论得到精确 Lyapunov 与复平面相图：除封闭 mobility ring 外，发现一类新的开放“迁移率弧”——退局域化只占据零测度集合（弧或线），稍有偏离即局域，与围出有限面积退局域区的 ring 形成鲜明对照。

---

### 5. When Quantum Meets AI: Quantum Methods for Machine Learning and Machine Learning Methods for Quantum Systems
Tak Hur · [2609.25641](https://arxiv.org/abs/2609.25641) · quant-ph / cs.AI · new（学位论文）

**为何相关：** 量子机器学习 ↔ 用机器学习表征量子系统，双向都落在你的 QML / 神经网络量子方向。

要点：Neural Quantum Embedding 拉大类间嵌入的迹距离，降低经验风险上界，并在含噪硬件上改善分类；基于 Hilbert–Schmidt 内积的目标推广到 DQC1，在 NMR 处理器上演示。margin 分析把量子神经网络泛化接到态区分。另一方向用机器学习方法处理量子系统。适合当一篇总览式入口。

---

### 6. Neural Network Backflow with Low-Rank Multi-Determinant Updates
Tianshu Huang, Xiaowei Ou, Vidvuds Ozolins · [2609.26544](https://arxiv.org/abs/2609.26544) · cond-mat.str-el · new

**为何相关：** 把 deep learning 与变分蒙特卡罗接到费米子强关联，是 PINN/NNQS 线在凝聚态的直接落地。

要点：以神经网络 backflow 为中心的变分框架，配合低秩移位的多行列式展开，捕捉非局域关联与复杂符号结构。二维 Hubbard 在半满时能量距辅助场 QMC 约 \(0.45\%\)；\(1/8\) 掺杂下能抓住电荷–自旋条纹交织。强调可扩展与可解释的费米子变分路线。

---

### 7. From Effective Temperature to Non-Boltzmann State Selection in Driven-Dissipative Quantum Criticality
Tiago Jorge, Jens Paaske, Pedro Ribeiro · [2609.25242](https://arxiv.org/abs/2609.25242) · cond-mat.str-el / quant-ph · new

**为何相关：** 电压偏置驱动–耗散临界态能否用有效温度描述，是开放量子临界的标准问题。

要点：在电子版 Lipkin–Meshkov–Glick（集体自旋耦合金属电极）上做受控大 \(N\) 分析，得到过阻尼开放量子临界区，与封闭模型不同。临界扇由温度与电压组织，涨落可由 \(T_{\rm eff}\) 刻画；强偏置下经三临界点变为一级相变，且同一 \(T_{\rm eff}\) 在序参量景观上空间变化，稳态由非 Boltzmann 选择规则决定，一级相界相对平衡位置发生移动。

---

### 8. Measurement-Induced Phase Transitions and Logical-Space Localization in Floquet Monitored Clifford Circuits
Hyunsoo Ha, David A. Huse · [2609.25201](https://arxiv.org/abs/2609.25201) · quant-ph · new

**为何相关：** Floquet 重复测量电路里，纠缠转变与纯化转变可否分离——直接连到驱动 + 测量诱导纠缠相变。

要点：空间局域、每 Floquet 周期层数固定的 monitored Clifford 电路中，空间随机的门与 Pauli 测量在时间上精确重复。稀有空间结构在重复下持久，打断常规时空随机电路里纠缠–纯化的对应：一维中初态为积态时晚期纠缠仍面积律，而初态极大混合时系统在热力学极限保持广泛混合；二维及以上出现体积律–面积律纠缠转变，但转变两侧系统仍保持混合。

---

### 9. Realization of quantum spin Hall insulator superlattice with emergent multigap-like helical edge states
Hui Guo, Xianghe Han, Fang Qin 等 · [2609.25732](https://arxiv.org/abs/2609.25732) · cond-mat.mtrl-sci · new

**为何相关：** 可开关螺旋边通道是拓扑自旋电子学的器件目标；实验实现带能隙化边态的 QSHI 超晶格。

要点：外延单层 HfTe₅ 中观测到重构诱导的周期超晶格调制，STM/STS 揭示类多带隙的螺旋边态。时间反演保护下的边通道若能被确定性开/关，就朝可编程拓扑电路迈进一步。和你关心的拓扑物态 / 自旋 Hall 平台实验侧对齐。

---

### 10. Probing quantum spin liquids with multiple quantum coherences
Lukas Homeier, Simon Linsel, Lode Pollet, Ana Maria Rey · [2609.25193](https://arxiv.org/abs/2609.25193) · quant-ph / str-el · new

**为何相关：** 量子模拟器上的 \(\mathbb{Z}_2\) 自旋液体难用局域探针认证；多量子相干（MQC）作为非局域、相敏诊断，连到纠缠与拓扑序。

要点：在扩展 toric code 上用大规模 QMC，把基本 anyon 激发与不同 MQC 扇区权重对应起来；anyon 凝聚在相变处留下对涨落更稳健的特征。子系统分辨的 MQC 还可作二分纠缠见证，区分经典 loop gas 与量子相干闭圈气。并给出基于绝热往返保真度的可执行协议。

---

### 11. Time-reversal-odd Transport in Odd-Parity Magnets
Ling Bai, Si Li, Libor Šmejkal, Yugui Yao, Wanxiang Feng · [2609.25919](https://arxiv.org/abs/2609.25919) · cond-mat.mtrl-sci · new

**为何相关：** 奇宇称磁体 / 非常规补偿磁与 altermagnetism 同属“零净磁矩 + 自旋劈裂 + 反常输运”家族；Šmejkal 等参与，框架性强。

要点：用自旋群对称分析给出二维/三维共面非共线反铁磁中奇宇称自旋劈裂的一般条件；指出一类相对论对应会禁止时间反演奇输运，打破后在 SOC 下允许反常霍尔等。紧束缚验证，并筛选三维磁材料库与二维异质结，给出可观的自旋取向依赖反常霍尔与磁光平台。

---

### 12. Thermally-driven reorientation of the Néel vector in altermagnetic MnTe（交叉上架）
Thomas J. Hicken 等 · [2507.14710](https://arxiv.org/abs/2507.14710) · cond-mat.mtrl-sci / str-el · cross

**为何相关：** 六角 MnTe 是原型交错磁；Néel 矢量的温度驱动重取向直接关系到实验可观测的 altermagnetic 响应各向异性。

要点：讨论 MnTe 中与理论预期一致的反常霍尔、能带劈裂等性质后，报告 Néel 矢量相对 \(a\) 轴在约 \(260\,\mathrm{K}\) 附近的热驱动重取向，归因于依赖温度晶格参数的单离子各向异性。为理解交错磁有序方向如何随温度拧动提供实验锚点。
