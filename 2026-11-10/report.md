# 11/10 arXiv 兴趣摘要（工作日）

扫了今天（美西 11/10，周二）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Tuesday, 10 November 2026**；新投稿：cond-mat 156、quant-ph 56、hep-th 20、math-ph 13、cs.LG 182、stat.ML 13（交叉与替换未计入）。已排除此前已荐的 380 篇。主题上 d 波交错磁 Chern 相的光子自旋霍尔探测、交错磁语境下自旋电导的微扰表述、开放系统谱拓扑与细致平衡的关系、例外点与拓扑束缚于连续谱态的实验构造、有界测量噪声稳定的离散时间晶体、驱动扩展 SSH 中的 Thouless 泵浦与 Haldane 拓扑、驱动–耗散系统中纠缠促成的自组织、自旋哈密顿量纠缠见证的 AI 发现、STM 对自旋纠缠的成像、强关联 CeAuAl$_3$ 中的 Kondo–Kramers 节线、以及超流调控的磁振子输运较集中。按兴趣锚点筛了 **11 篇**（10 篇新投稿、1 篇交叉稿；未收替换稿；跳过假阳性或弱相关如非厄米全息/PT 对称宇宙学与黑洞振铃例外点、电网与通用 PDE 的物理信息神经算子、模糊球面 CFT 单值缺陷、宏观 QED 在活性介质中的微观模型、编织与玻璃拓扑、量子直接通信、VQE 测量开销与参数迁移、引力波量子计量、Floquet 腔-BEC 连续变量计算硬件、纳米超导量子技术路线图等）。本日用户机 Zotero（DESKTOP-00O6NSD）离线，仅对缓存的 arXiv ID 列表（187，约 10/30）做只读核对：**短名单无同 ID**；主题近邻未逐条标注。

**建议先翻这三篇：**
1. **Probing Chern Topology through Hall-Sensitive Photonic Spin Hall Shifts in a d-wave Altermagnet** —— 在二维 Rashba 耦合的 d 波交错磁 Chern 体系中，用光子自旋霍尔位移的纵向分量对光学霍尔电导（及相反 Chern 相）的奇性来探测拓扑——交错磁 × Chern 拓扑 × 自旋霍尔。
2. **Holonomy, Spectral Topology, and Detailed Balance in Classical and Open Quantum Systems** —— 用和乐把能带拓扑、缺陷几何与马尔可夫网络的循环亲和统一起来，澄清谱拓扑可以排除细致平衡、却不能定量耗散——非厄米谱拓扑 × 开放系统 × 细致平衡。
3. **Discrete time crystals stabilized by bounded measurement noise** —— 在干净长程自旋链中，用有界测量噪声把连续弱测量从“典型轨迹热化”拉回到可稳定周期加倍的时间晶体——测量动力学 × 离散时间晶体。

---

### 1. Probing Chern Topology through Hall-Sensitive Photonic Spin Hall Shifts in a d-wave Altermagnet
Mahnoor Sajid · Maha Siddiqui · Muzamil Shah · [arXiv:2611.10706](https://arxiv.org/abs/2611.10706) · cond-mat.mes-hall · new

**为何相关：** 在二维 Rashba 耦合的 d 波交错磁 Chern 体系中，用光子自旋霍尔位移的纵向分量对光学霍尔电导（及相反 Chern 相）的奇性来探测拓扑——交错磁 × Chern 拓扑 × 自旋霍尔。

要点：作者考虑垂直交换场下的二维 d 波交错磁，高对称点处 Dirac 质量由交换与交错磁跃迁共同决定，能带反转给出平凡相 $C=0$ 与 Chern 绝缘相 $C=\pm 1$。用 Kubo 光学电导与衬底上导电薄层的反射矩阵，计算反射高斯光束的螺旋度依赖有限束腰位移。光学响应呈现最小带间吸收阈、Van Hove 型谱特征，以及因交换场动量依赖而来的 $X/Y$ 点不同跃迁。在给定霍尔张量与偏振约定下，纵向螺旋度半分离对光学霍尔电导反转呈奇，并在相反 Chern 相之间变号；横向半分离则为偶。最大自旋劈裂出现在伪布鲁斯特反射极小附近，纵向劈裂的谱变化反映 $d$ 波交错磁导致的不等价带间跃迁。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 2. Holonomy, Spectral Topology, and Detailed Balance in Classical and Open Quantum Systems
Alvan Hunt · [arXiv:2611.12514](https://arxiv.org/abs/2611.12514) · cond-mat.stat-mech · new

**为何相关：** 用和乐把能带拓扑、缺陷几何与马尔可夫网络的循环亲和统一起来，澄清谱拓扑可以排除细致平衡、却不能定量耗散——非厄米谱拓扑 × 开放系统 × 细致平衡。

要点：文章以教程式综述追问：线性生成元的谱数据能对细致平衡说些什么。反复出现的三种和乐是能带 Berry 相、位错的 Burgers 矢量，以及马尔可夫网络循环亲和（联络 $\ln(W_{ij}/W_{ji})$ 的和乐）。细致平衡等价于在定态所固定内积下的自伴性，因而马尔可夫生成元的非实本征值、例外点或非零点隙绕数即可排除细致平衡并迫使熵产生 $\sigma>0$；但实且可对角化的谱并不能一般地保证细致平衡。在虽正规却有复谱的 Hatano–Nelson 环上，绕数固定时 $\sigma$ 仍可扫过 $(0,\infty)$。例外点需另作动力学判定：在含时间反演宇称的广义细致平衡下，例外点仅能通过时间反演奇的动力学与平衡相容。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 3. Discrete time crystals stabilized by bounded measurement noise
Pallabi Chatterjee · Tanay Nag · Ranjan Modak · [arXiv:2611.12400](https://arxiv.org/abs/2611.12400) · cond-mat.stat-mech · new

**为何相关：** 在干净长程自旋链中，用有界测量噪声把连续弱测量从“典型轨迹热化”拉回到可稳定周期加倍的时间晶体——测量动力学 × 离散时间晶体。

要点：周期驱动的干净相互作用系统通常会加热并破坏离散时间晶体。作者在连续监测局域占据的长程自旋链上追问弱测量能否稳定该序。测量会诱导体律到面律的纠缠转变，但低纠缠并不足够：典型量子轨迹仍落到无次谐波响应的平庸态；抑制测量涨落后的最大概率轨迹则呈现稳健的周期加倍。他们引入把测量涨落限制在有限窗口的有界噪声协议：窄窗口保持周期加倍，中等窗口出现时间晶体与非时间晶体轨迹共存且前者逐条逃逸（序长寿但有限），宽窗口则破坏该序。结论是，有界测量噪声（丢弃大偏差轨迹）可为干净系统中的时间晶体提供一条路径，而测量诱导的面律相是必要但非充分条件。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 4. Exceptional Topological Bound States in the Continuum
Luohong Liu · Qicheng Zhang · Shuaishuai Tong · Chunyin Qiu · [arXiv:2611.10077](https://arxiv.org/abs/2611.10077) · cond-mat.mes-hall · new

**为何相关：** 把拓扑相、例外点与连续谱束缚态三者合并为“例外拓扑 BIC”，并在可电调损耗的声学平台上同时观测本征能量与本征态的聚合——非厄米 × 例外点 × 拓扑束缚态。

要点：这三类奇异性的两两组合已有许多工作，三重合并的例外拓扑 BIC（ET-BIC）此前尚未被探索。作者提出由四条耦合拓扑链构成的通用构造：$y$ 方向镜像堆叠产生成对的拓扑 BIC，再沿 $z$ 方向堆叠并加入偏置损耗，使原先分属不同子空间的成对模式在临界损耗处坍缩为 ET-BIC。实验上用可电学调控损耗的声学平台，同时直接观测到本征能量与本征态的聚合，从而完整验证 ET-BIC 的形成。这类三重协同模式或可为同时需要鲁棒性、灵敏度与 BIC 局域的波动器件提供思路。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 5. Quantum entanglement as a resource for self-organization and stabilization
Kazuki Ikeda · [arXiv:2611.11175](https://arxiv.org/abs/2611.11175) · quant-ph · new

**为何相关：** 在驱动–耗散玻色晶格中证明瞬时局域纠缠可促成并稳定宏观 Turing 图案，而图案在纠缠消失后仍可存续——开放 Lindblad 动力学 × 纠缠资源。

要点：作者追问纠缠能否在其本身消失之后仍留下宏观序。在驱动–耗散玻色晶格中，局域纠缠使输运得以放大空间涨落并形成扩展的 Turing 图案。对带噪声与无序的全非线性动力学，他们给出所有可允许可分演化（含任意经典关联）下图案强度的严格有限时间上界；量子动力学在形成与噪声下的稳定阶段都超出这些上界，超出量还给出超出可分极限的累积输运贡献下界。进一步引入对新兴序作出响应的环境：压制局域相干并激活经典输运后，图案在局域纠缠丧失后仍然存续，且两个阶段来自同一个不含时 Lindblad 方程。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 6. AI-Driven Discovery of Entanglement Witness in Spin Hamiltonians
Jiwei Tian · Mouyang Cheng · Mingda Li · [arXiv:2611.11935](https://arxiv.org/abs/2611.11935) · quant-ph · cross

**为何相关：** 用可迁移的 AI 模型从低阶自旋关联中发现紧凑的多体纠缠见证，并可在不同尺寸与哈密顿家族间转移——量子纠缠 × 自旋模型 × AI。

要点：从实验可及的可观测量判断多体混合态是否纠缠仍然困难。作者提出 EntNet：在短程自旋-$1/2$ 链上，把可测 Pauli 关联整理成局域幺正不变特征，稀疏选出 16 个不变通道，再用带旋转位置编码的 Transformer 学习其空间结构。仅用这些低阶期望值，模型对已认证纠缠态的召回率超过 98%，对可分态的假阳性接近零；并在不同系统尺寸以及受挫、无序等不同哈密顿家族间具有可迁移性。模型还揭示对关联的选择性空间组织，其有限温度判决边界追踪 Jordan–Wigner 准粒子激发隙，从而给出可解释的数据驱动纠缠见证。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 7. Imaging spin entanglement with a scanning tunneling microscope
J. C. G. Henriques · B. Viña-Bausá · I. Brihuega · J. Fernández-Rossier · [arXiv:2611.10946](https://arxiv.org/abs/2611.10946) · cond-mat.mes-hall · new

**为何相关：** 把扫描隧道谱的谱矩与自旋-$1/2$ 体系的纠缠见证、并存度及空间成像联系起来，并与纳米石墨烯自旋链实验对照——自旋纠缠 × 扫描探针。

要点：表面组装的人工自旋阵列为原子尺度量子关联研究提供了平台。作者建立自旋非弹性隧道谱（IETS）与自旋-$1/2$ 纠缠之间的层级关系：二聚体中谱学活跃跃迁的数目本身即可作为纠缠见证；针尖置于格点 $i$ 时，电导谱矩与量子关联直接相关——零阶矩探测有能隙非简并基态的 one-tangle，对旋转不变海森堡系统一阶矩给出热自旋关联 $\langle\boldsymbol{S}(i)\cdot\boldsymbol{S}(j)\rangle$，从而重建近邻并存度并空间成像自旋链中的纠缠，同时也给出内能与磁比热这两种可用的见证。将该方法用于纳米石墨烯自旋链的实验 IETS，与理论符合良好；并讨论二阶矩对更长程关联、以及三聚体中真三体纠缠与谱权重的关系。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 8. Spin Conductivity: Insight From Perturbation Theory
Xu Chen · Mingbo Dou · Yu Sui 等 · [arXiv:2611.11077](https://arxiv.org/abs/2611.11077) · cond-mat.other · new

**为何相关：** 在交错磁材料中备受关注的自旋电导问题上，用微扰论给出与 Kubo 及量子动理学一致的时间反演偶/奇表达式，并澄清其波函数修正阶数——交错磁 × 自旋–电荷转换。

要点：交错磁中的自旋电导研究正在迅速展开。作者在微扰论框架下给出一种初等推导：时间反演偶的自旋电导表达式与 Kubo 线性响应及量子动理学完全一致；清洁极限下时间反演奇的表达式也与已有结果吻合。他们进一步指出，时间反演奇（偶）自旋电导分别来自波函数的零阶（一阶）修正，从而为磁性材料中的电荷–自旋转换机制提供更直观的微扰论图像。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 9. Thouless pumping and Haldane-model topology in a driven extended SSH chain
Zhen Dong · Xin-Lei Zhao · Yi Zheng · [arXiv:2611.10507](https://arxiv.org/abs/2611.10507) · cond-mat.quant-gas · new

**为何相关：** 在可调次近邻跃迁的扩展 SSH 链中构造 Thouless 泵浦，并把 Haldane 模型映射到该驱动一维链，从而用一维泵浦读出二维 Chern 数——驱动拓扑 × Thouless 泵浦 × Haldane。

要点：Thouless 泵浦可通过一维晶格中的量子化运动探测 Chern 拓扑。作者在可调次近邻跃迁的扩展 SSH 模型中，用 Bloch 空间的图示构造泵浦方案：Bloch 矢量描出随时间演化的闭合环路，合成带的 Chern 数由该环路的运动决定。他们分别在填满的能带与由 Bloch 振荡驱动的玻色波包上演示量子泵浦，并表明用泵浦时间替换一个准动量即可把 Haldane 模型映射到驱动扩展 SSH 链。量子化的电荷泵表明，二维模型的 Chern 数可以从一维泵浦协议中读出，为光子与冷原子平台探测高维拓扑提供了一条较易实现的路径。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 10. Discovery of Kondo-Kramers Nodal Line Topological State in strongly correlated material CeAuAl$_3$
Hari Bhandari · Kevin Allen · Kuan-Sen Li 等 · [arXiv:2611.10368](https://arxiv.org/abs/2611.10368) · cond-mat.str-el · new

**为何相关：** 在非中心对称、非手性的 Kondo 晶格 CeAuAl$_3$ 中实验确认由 Kondo 关联把 Kramers 节线拉到费米面，并观测到与之相伴的本征反常霍尔效应——强关联拓扑 × 反常霍尔。

要点：Kramers 节线（KNL）被预言存在于所有非手性、非中心对称晶体，但实验实现很少，且几乎都在弱关联体系。作者结合磁输运、热力学、DFT 与紧束缚玩具模型，发现 CeAuAl$_3$ 在 $\Gamma$–$Z$ 与 $X$–$P$ 方向承载由时间反演与镜像保护的 KNL；打破这些晶体对称性并经由自旋极化打破时间反演后，节线简并解除并产生 Berry 曲率，从而给出本征反常霍尔效应。更重要的是，大的反常霍尔并不只出现在磁有序温度 $T_N$ 以下，而是在 Kondo 温度以下即已出现，表明是 Kondo 关联把节线带到费米面，而非出现在偶然能量。工作把 CeAuAl$_3$ 视为首个被明确指认的 Kondo–Kramers 节线关联拓扑态，并给出寻找同类体系的路径。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 11. Supercurrent-controlled magnon transport via suppression of the superconducting gap
Tetsuma Mandokoro · Yoichi Shiota · Hisakazu Matsuki 等 · [arXiv:2611.11781](https://arxiv.org/abs/2611.11781) · cond-mat.supr-con · new

**为何相关：** 在铁磁/超导异质结中用超流抑制超导能隙、增强磁振子向超导侧 Bogoliubov 准粒子的耗散，从而无焦耳热地调控磁振子输运——磁振子自旋电子学 × 超导。

要点：磁振子与超导凝聚体是两类宏观量子态，它们的相互作用仍少被直接实验揭示。作者在铁磁/超导异质结中观察到磁振子输运信号随超流增大而下降：超流压低超导能隙，从而增强磁振子经 Bogoliubov 准粒子向超导侧的耗散。该调控依赖超流而非电荷电流，因而可避免焦耳热，为通过超导控制磁振子、走向低能耗磁振子器件提供了实验路径。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*
