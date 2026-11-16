# 11/11 arXiv 兴趣摘要（工作日）

扫了今天（美西 11/11，周三）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Wednesday, 11 November 2026**；新投稿：cond-mat 73、quant-ph 71、hep-th 28、math-ph 7、cs.LG 134、stat.ML 11（交叉与替换未计入）。已排除此前已荐的 391 篇。主题上无净磁化的交错磁弱拓扑绝缘体中的量子反常霍尔、$d_{xy}$ 交错磁诱导的几何选择高阶拓扑、非马尔可夫量子态扩散中的例外点、用 PINN 反演长自旋链哈密顿量、Floquet 高阶拓扑超导体综述、耦合非马尔可夫环境携带的关联、PT 对称原子线路 SQUID 的非互易约瑟夫森动力学、拓扑绝缘针尖端态隧穿与 $d$ 波交错磁的耦合、RuO$_2$ 界面隐藏磁性、由手性非厄米系统加倍而来的层级拓扑保护、以及规范不变 PEPS 在拓扑相变处的表达能力较集中。按兴趣锚点筛了 **11 篇**（10 篇新投稿、1 篇交叉稿；未收替换稿；跳过假阳性或弱相关如全息拖曳力与纠缠膜、二维 TQFT 纠缠切割、通用 PDE 的有限基物理信息网络、细胞趋化传感能耗、表面码相干误差解码、图像分类量子神经网络、QML 误差缓解策略选择、魔角石墨烯的“借用”普朗克耗散、Co 位局域电子结构、以及偏器件工艺的碳化硅空位斯塔克调谐等）。本日用户机 Zotero（DESKTOP-00O6NSD）离线，仅对缓存的 arXiv ID 列表（187，约 10/30）做只读核对：**短名单无同 ID**；主题近邻未逐条标注。

**建议先翻这三篇：**
1. **Magnetization-free quantum anomalous Hall effect in altermagnetic weak topological insulators** —— 用交错磁交换在弱拓扑绝缘体薄膜上选择性地打开 $Z$ 点 Dirac 锥能隙，得到无净磁化、$C=1$ 的量子反常霍尔相——交错磁 × 量子反常霍尔 × 弱拓扑绝缘体。
2. **Geometry-Selective Higher-order topological insulators induced by $d_{xy}$ altermagnet** —— 近邻 $d_{xy}$ 波交错磁使轴对齐边保持无能隙、对角边获得交替质量，从而在质量畴壁给出角态——交错磁 × 高阶拓扑 × 边界几何。
3. **Exceptional points in non-Markovian quantum-state diffusion: From coefficient dynamics to state signatures** —— 在精确非马尔可夫量子态扩散中澄清：系数方程的例外点不必在每一种量子态可观测量上留下同样的签名——例外点 × 非马尔可夫开放系统。

---

### 1. Magnetization-free quantum anomalous Hall effect in altermagnetic weak topological insulators
Yanmiao Han · Yu-Hao Wan · Peng-Yi Liu · Rundong Zhao · Qing-Feng Sun · [arXiv:2611.13508](https://arxiv.org/abs/2611.13508) · cond-mat.mes-hall · new

**为何相关：** 用交错磁交换在弱拓扑绝缘体薄膜上选择性地打开 $Z$ 点 Dirac 锥能隙，得到无净磁化、$C=1$ 的量子反常霍尔相——交错磁 × 量子反常霍尔 × 弱拓扑绝缘体。

要点：量子反常霍尔通常依赖铁磁或磁掺杂，材料选择受限，且往往迁移率低、对无序敏感、工作温度偏低。作者提出用交错磁交换作用在弱拓扑绝缘体（WTI）上实现无净磁化的 QAH：交错磁序选择性地把 $Z$ 点 Dirac 锥打开能隙，而 WTI 薄膜上下表面杂化在 $\Gamma$ 点打开平庸能隙，从而得到 Chern 数 $C=1$、单一手性边缘通道的相。他们用最小薄膜模型与 slab 几何验证拓扑转变，并计算相应的霍尔响应。鉴于交错磁与层状 WTI 均已有实验材料，这一表面工程路径有望在无需磁掺杂或全局磁化的情况下实现无耗散边缘输运。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 2. Geometry-Selective Higher-order topological insulators induced by $d_{xy}$ altermagnet
Siyuan Cheng · Yuee Xie · Xiaosen Yang · Yuanping Chen · [arXiv:2611.13438](https://arxiv.org/abs/2611.13438) · cond-mat.mes-hall · new

**为何相关：** 近邻 $d_{xy}$ 波交错磁使轴对齐边保持无能隙、对角边获得交替质量，从而在质量畴壁给出角态——交错磁 × 高阶拓扑 × 边界几何。

要点：作者表明，近邻 $d_{xy}$ 波交错磁是调控依赖边界几何的高阶拓扑相的有效途径：轴对齐的边缘态保持无能隙，而对角边获得符号交替的有效质量，从而在质量畴壁处形成四个角态。通过投影到边缘态子空间，他们导出不同边界几何下的有效边缘哈密顿量；在周期边界下引入 $\pi$ 通量缺陷，通量核处出现零能束缚态，作为无需物理边界的互补证据。Zeeman 场与交错磁序的竞争可在体隙保持打开的情况下，通过边缘隙的关闭与重开驱动拓扑转变。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 3. Exceptional points in non-Markovian quantum-state diffusion: From coefficient dynamics to state signatures
Yusui Chen · Hang Liu · Kaiqi Xiong · Quanzhen Ding · Eric Guo · [arXiv:2611.13221](https://arxiv.org/abs/2611.13221) · quant-ph · new

**为何相关：** 在精确非马尔可夫量子态扩散中澄清：系数方程的例外点不必在每一种量子态可观测量上留下同样的签名——例外点 × 非马尔可夫开放系统。

要点：记忆系数方程上的例外点，不必在每一种量子态可观测量上留下同样的签名。作者在精确非马尔可夫量子态扩散（NMQSD）框架中，沿同一算符闭合从系数动力学走到噪声平均后的非马尔可夫主方程：有限齐次提升用来识别因果初值所到达的 Jordan 链，再由态重建判断哪些贡献能在指定读出中存活。两个模型展示这一区分。对限制在零、一激发子空间的共浴量子比特，噪声无关的下降型 $O$ 算符给出封闭主方程，每个亏损衰减模将其完整极点阶数传到合适的无条件激发–参考相干；已知的三阶构型既给出二次–指数相干，也可在另一正交分量中消去最高阶项。对固定光子数光力扇区中位置耦合的振子，精确闭合含有标量噪声历史项；在所研究的正规可归一化分支上，两个二阶系数块使条件位移响应对 NMQSD 噪声历史出现双极点，而纯代数的系数尾在条件高斯宽度中被消去。完全噪声平均会改变主方程系数，并把条件宽度与态中心的加权散布合在一起。结论是：因果制备、态重建与平均，使系数例外点获得精确且依赖于读出的含义。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 4. PINNverse meets Jordan--Wigner: learning the Hamiltonian of long spin chains
Gubio G. De Lima · [arXiv:2611.14023](https://arxiv.org/abs/2611.14023) · quant-ph · new

**为何相关：** 用逆物理信息神经网络从局域观测量反演近邻自旋链哈密顿量，并以 Jordan–Wigner 把网络输出从指数降到 $N^2$——PINN × 自旋链反问题。

要点：逆物理信息神经网络（PINNverse）可从测量期望值学习量子哈密顿量参数，但网络输出随比特数 $N$ 按 $4^N$ 增长。作者证明：对近邻交换的自旋链，Jordan–Wigner 变换消除这一指数代价——动力学闭合在 $N\times N$ 的单体密度矩阵上，网络只需 $N^2$ 个输出，数据则是五个全局设置下测得的局域可观测量；寄生 $ZZ$ 串扰通过含时 Hartree–Fock 闭合纳入。用合成数据，同一网络先求解运动方程，再恢复多达 50 比特链的哈密顿参数，耦合学习精度优于 $0.1\%$；长链局域频率误差再用从网络估计出发的直接最小二乘拟合消除。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 5. Floquet first- and higher-order topological superconductors: A review
Debashish Mondal · Arnob Kumar Ghosh · Arijit Saha · Tanay Nag · [arXiv:2611.13804](https://arxiv.org/abs/2611.13804) · cond-mat.mes-hall · new

**为何相关：** 系统综述一阶到三阶拓扑超导体，并说明周期驱动即使在无驱动系统平庸时也能给出 Floquet 高阶拓扑超导与反常 Majorana $\pi$ 模——Floquet × 高阶拓扑超导 × Majorana。

要点：这篇综述从一阶到三阶系统梳理拓扑超导体，说明 Majorana 零模的空间维数如何逐步降低，以及高阶拓扑超导体如何在 $d>1$ 中调控其局域。重点是周期驱动：即便无驱动系统拓扑平庸，Floquet 工程仍可实现上述各相；并讨论自旋轨道耦合、磁场、磁杂质与对称性破缺质量项如何共同给出 Floquet 高阶拓扑超导相及其不变量。文中还较系统地讨论如何用拓扑不变量区分常规 Majorana 零模与只出现在驱动系统、分别处于两个准能量、没有静态对应的反常 Majorana $\pi$ 模。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 6. Correlations carried and controlled by coupled non-Markovian environments
Stuart Flannigan · [arXiv:2611.13900](https://arxiv.org/abs/2611.13900) · quant-ph · new

**为何相关：** 在模式自身会交换激发的空间关联非马尔可夫环境中，说明环境记忆可以把反馈效应传到远处自旋并控制纠缠——开放非马尔可夫系统 × 量子关联。

要点：环境可以保留量子信息并在空间分离的系统之间搬运。作者给出一套局域纯态层级，用以处理模式之间会交换激发、因而同时具有记忆与空间关联的非马尔可夫环境。在受腔 QED 启发的局域耦合 Rabi 自旋–腔链中，被消去的腔环境里的光子跳跃会在原本孤立的自旋之间产生关联与纠缠；对中间腔进行监测并把测量记录反馈到相应自旋，还能进一步增强并未直接接受反馈的端点自旋之间的关联。反馈开始时的延迟响应、以及停止后纠缠仍继续增长，支持相干环境动力学把较早反馈的效应传到端点自旋。对 XXZ 与海森堡链的张量网络模拟还表明，环境输运会改变多体关联图样。工作提供了数值精确的随机纯态框架。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 7. Nonreciprocal Josephson Dynamics of a $\mathcal{PT}$-Symmetric Atomtronic SQUID
Nalinikanta Pradhan · Rina Kanamoto · M. Bhattacharya · Pankaj K. Mishra · [arXiv:2611.14291](https://arxiv.org/abs/2611.14291) · cond-mat.quant-gas · new

**为何相关：** 在平衡增益–损耗的环形玻色凝聚体中构造 PT 对称原子线路 SQUID，用非厄米性调控非互易约瑟夫森输运并软化集体模至例外点——PT 对称 × 例外点 × 非互易约瑟夫森。

要点：在环形玻色–爱因斯坦凝聚体上设置平衡的原子增益与损耗区，并加入两道移动光势垒，构成原子线路量子干涉器件（AQUID）。平衡增益–损耗给出 PT 对称势同时打破空间反演，从而具备非互易约瑟夫森输运的基本要素；动力学由与凝聚体耦合的拉盖尔–高斯光束驱动的光力腔相位正交谱无损监测。增大局域增益–损耗强度会使 PT 对称集体模软化并趋向例外点（Bogoliubov–de Gennes 验证），相干布居交换还在腔输出谱中产生额外劈裂。对平移势垒，非厄米性成为调节临界电流的额外参数；势垒同时平移与旋转时，转动相位进一步调控反向电流干涉。周期调制下，本征 PT 对称集体模使 Shapiro 台阶更为显著。文中还提出用倾斜光晶格的厄米实现路径。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 8. End-state-assisted tunneling at a topological insulator STM tip
Rui Chen · Jie Zhou · Bin Zhou · Dong-Hui Xu · [arXiv:2611.14155](https://arxiv.org/abs/2611.14155) · cond-mat.mes-hall · new

**为何相关：** 量子自旋霍尔针尖的拓扑端态介导共振隧穿，并把定向通道耦合到 $d$ 波交错磁以给出自旋依赖干涉反差——拓扑端态 × 自旋霍尔针尖 × 交错磁。

要点：近期用拓扑绝缘体针尖做自旋敏感扫描隧道实验，促使人们从微观上理解针尖几何如何控制电流输送。作者表明，量子自旋霍尔针尖中，边缘杂化打开能隙后，拓扑端态可介导共振隧穿；不对称终止使相反自旋极化的螺旋通道具有不同的有效长度与共振宽度。在独立通道图像下，透射电流不平衡在匹配共振处消失、在偏离时出现；再把这些定向通道耦合到 $d$ 波交错磁，可得到自旋依赖的干涉反差。台阶状终止上的杂化端态还提供多个隧穿共振。工作把端态介导隧穿确立为强受限拓扑针尖 STM 的一种输运机制。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 9. Hidden interfacial magnetism in RuO$_2$ heterostructures revealed by a superconducting spin switch
Tetsuma Mandokoro · Hisakazu Matsuki · Shutaro Karube 等 · [arXiv:2611.13579](https://arxiv.org/abs/2611.13579) · cond-mat.mtrl-sci · new

**为何相关：** 用超导自旋开关在 Nb/RuO$_2$ 界面探测隐藏磁性，并将其归因于夺氧形成的薄 RuO$_x$ 层——交错磁候选 RuO$_2$ × 界面磁性 × 超导自旋开关。

要点：RuO$_2$ 曾是交错磁的旗舰候选，目前多认为体相非磁，但表面与界面会出现弱、静态且空间不均匀的磁性。作者在 Nb/RuO$_2$ 界面用超导自旋开关来追问磁性所在位置与稳定机制：GdN/Nb/RuO$_2$ 三层中，界面交换场取向可调控 Nb 的超导转变温度，从而探测常规磁测量难以触及的界面磁性。开关揭示出一个隐藏磁子系统，被归因于 Nb 从 RuO$_2$ 夺氧形成的薄 RuO$_x$ 氧化还原层，表现为带有空位诱导各向异性的弱而磁硬的铁磁体。超流还会放大开关效率，使探针灵敏度可原位调节。工作把超导自旋开关确立为探测埋藏界面隐藏磁性的定量低温探针，并对 RuO$_2$ 磁性争论给出界面化学起源的实验约束。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 10. Hierarchical Topological Protection and Subsymmetry-Driven Edge-State Switching
Shu Long · Rijia Lin · Hui-Qiang Liang · Linhu Li · [arXiv:2611.13839](https://arxiv.org/abs/2611.13839) · cond-mat.mes-hall · new

**为何相关：** 对手性非厄米系统做加倍得到厄米模型，揭示结构与继承手性对称的层级保护，并在子对称下切换边缘零模——非厄米拓扑 × 对称性约化 × 边缘态调控。

要点：作者揭示一种层级化的拓扑保护：多种对称性及其约化形式为边缘态提供不同的保护机制。在对手性非厄米系统做加倍得到的厄米哈密顿量中，结构手性对称与继承手性对称提供互补的保护通道；选择性地打破其中之一，可区分它们对边缘零模的不同作用，从而在对称性约化下给出不同层级的保护。更有意思的是，即便两个完整手性对称都被打破，固定的子对称约束仍允许受保护零模在未破缺系统的拓扑相边界两侧改变所在边缘与数目。这为通过约化对称约束来调控边缘态构型提供了一条路径。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 11. Assessing the expressive power of a gauge-invariant PEPS ansatz across a topological phase transition
Etsuko Itou · Tsuyoshi Okubo · [arXiv:2611.13852](https://arxiv.org/abs/2611.13852) · hep-lat · cross

**为何相关：** 用确定性 Grassmann 张量网络检验规范不变费米 PEPS 在 $\mathbb{Z}_2$ 规范理论拓扑相变处的表达能力，能量与拓扑纠缠熵均可准确描述——张量网络波函数 × 拓扑相变 × 变分方法。

要点：规范高斯费米 PEPS（GGFPEPS）是 $(2+1)$ 维格点规范理论的显式规范不变张量网络试探态，此前多用变分蒙特卡洛，统计误差使变分参数难以精确确定、表达能力不易准确检验。作者把计算改写成 Grassmann 张量网络，用高阶张量重正化群（HOTRG）做到线性尺寸 $L=34$，并用角转移矩阵重正化群（CTMRG）处理无限体积极限。仅含八个复变分参数的试探态即可准确描述纯 $\mathbb{Z}_2$ 规范理论（包括拓扑相变区），不仅能量、拓扑纠缠熵也对得上；由它们磁化率峰得到的临界耦合与连续时间量子蒙特卡洛预言定量一致。靠近转变点时，该试探态还走出构造时所假设的、在强/弱耦合极限之间简单插值的 plaquette 乘积态族。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*
