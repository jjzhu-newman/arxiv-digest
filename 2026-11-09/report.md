# 11/09 arXiv 兴趣摘要（工作日）

扫了今天（美西 11/09，周一）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Monday, 9 November 2026**；新投稿：cond-mat 66、quant-ph 65、hep-th 31、math-ph 10、cs.LG 121、stat.ML 9（交叉与替换未计入）。已排除此前已荐的 369 篇。主题上开放系统时间晶体的 go/no-go（无需外部热力学资源）、量子例外点与 Liouvillian 赝谱、交错磁（RuO2 太赫兹转换中自旋/轨道通道的实验拆分、双色光对 Rashba 多极磁体 Néel 矢量的 Floquet 力矩）、耗散量子相变的对称性分辨临界性、图态量子 Fisher 信息的拓扑签名、退相位下 Z₂ 拓扑存活的局域判据、驱动–耗散多体量子电池、扭转铜基双层中与反铁磁共存的拓扑超导、DSSYK 时间纠缠的非厄米密度核、以及斯格明子拓扑纹理对激子的设计较集中。按兴趣锚点筛了 **11 篇**（全部为新投稿；未收替换稿；交叉稿中 HEOM 的多层 MCTDH 传播、核内非局域魔法等未纳入短名单；跳过假阳性如聚合物链缠结模量、MnSe 点缺陷 DFT、通用 PINN 评测/风电预测/气候模拟/坐标变换 PINN 与 Adam 任务平衡、机器学习原子间势、网络安全异常检测 QML、共形缺陷谱解析界、双自旋黑洞环 double copy、阳极氧化铝忆阻器、高通量结构预测实验评估、活性物质量子力学表述、星系剧烈弛豫等）。本日用户机 Zotero（DESKTOP-00O6NSD）离线，仅对缓存的 arXiv ID 列表（187，约 10/30）做只读核对：**短名单无同 ID**；主题近邻未逐条标注。

**建议先翻这三篇：**
1. **Open Quantum Time Crystals without External Thermodynamic Resources: Go and No-Go Theorems** —— 在满足细致平衡与时间平移协变的 Lindblad 动力学下，给出无需外部功/相干资源即可由环境激活时间晶体的显式模型与 no-go 定理——开放系统 × 时间晶体。
2. **Dynamics and pseudospectra around quantum exceptional points** —— 在完整 Lindblad 演化（而非有效非厄米哈密顿）下，用长时平均与赝谱刻画 Liouvillian 例外点的谱与动力学响应——非厄米 × 例外点 × 开放量子晶格。
3. **Disentangling Spin and Orbital Contributions in the Search for Altermagnetic Terahertz Conversion in RuO2** —— 用太赫兹发射谱首次实验拆分 RuO2 异质结中的自旋/轨道–电荷转换通道，并指出界面调制的各向异性自旋霍尔而非逆交错磁自旋劈裂效应——交错磁 × 轨道输运 × 自旋霍尔。

---

### 1. Open Quantum Time Crystals without External Thermodynamic Resources: Go and No-Go Theorems
Yuri Ogami · Hiroyasu Tajima · [arXiv:2611.09540](https://arxiv.org/abs/2611.09540) · quant-ph · new

**为何相关：** 在满足细致平衡与时间平移协变的 Lindblad 动力学下，给出无需外部功/相干资源即可由环境激活时间晶体的显式模型与 no-go 定理——开放系统 × 时间晶体。

要点：时间晶体已在孤立短程系统的基态与 Gibbs 态被排除，却可在 Floquet 与开放系统中出现；既有开放系统方案通常需外部功或能量相干等热力学资源。作者追问：仅与环境耦合、不额外供给资源，能否激活孤立系统所无的时间晶体。他们构造满足（i）哈密顿与跳跃算符均不显含时、（ii）时间平移协变、（iii）细致平衡的 Lindblad 模型，并证明环境耦合可在定态中激活时间晶体；给出零温 Gibbs 环境、不显含时且能量守恒的相互作用、以及短程哈密顿的若干实现，其一精确再现时间晶体周期。随之证明 no-go：在（i）–（iii）下，激活只能来自环境诱导的哈密顿项，而不能来自耗散本身。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 2. Dynamics and pseudospectra around quantum exceptional points
Georgios E. Pavlou · Ioannis Kiorpelidis · Georgios K. Simopoulos 等 · [arXiv:2611.09464](https://arxiv.org/abs/2611.09464) · quant-ph · new

**为何相关：** 在完整 Lindblad 演化（而非有效非厄米哈密顿）下，用长时平均与赝谱刻画 Liouvillian 例外点的谱与动力学响应——非厄米 × 例外点 × 开放量子晶格。

要点：例外点在经典光子学中已有充分研究，但量子情形下耗散与量子涨落并存，完整 Lindblad 演化与有效非厄米描述可以显著不同。作者用适当归一的长时平均与 imbalance 探查 Liouvillian 例外点的谱与动力学签名，并在有损耗 Bose–Hubbard 晶格与耗散双自旋两个范式模型中，分析量子跳跃与相互作用对 Liouvillian 谱（含复的、结构化的赝谱）的作用。结果展示非厄米现象如何在现实量子晶格中出现，为经典例外点物理与可实验探测的开放量子系统之间架桥。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 3. Disentangling Spin and Orbital Contributions in the Search for Altermagnetic Terahertz Conversion in RuO2
Jiahao Liu · Yuxiao Mo · Tongyang Guan 等 · [arXiv:2611.09098](https://arxiv.org/abs/2611.09098) · cond-mat.mes-hall · new

**为何相关：** 用太赫兹发射谱首次实验拆分 RuO2 异质结中的自旋/轨道–电荷转换通道，并指出界面调制的各向异性自旋霍尔而非逆交错磁自旋劈裂效应——交错磁 × 轨道输运 × 自旋霍尔。

要点：金红石 RuO2 是突出的交错磁候选，但其电荷–角动量转换的微观起源未定，轨道输运可能占主导。作者以 Fe 作为主要自旋流注入源、以 Ni 与坡莫合金作为主要轨道流注入源：在受控自旋流注入下未观测到逆交错磁自旋劈裂效应，所见各向异性更符合强烈受近界面环境调制的各向异性逆自旋霍尔响应；轨道流注入下各向异性明显更弱，表明 RuO2 中轨道–电荷转换大体各向同性。工作强调在把各向异性归因于交错磁性之前，须先拆分自旋、轨道与界面贡献。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 4. Bichromatic light-induced electronic torques on the Néel vector in Rashba magnetic multipoles from $p$-wave magnets to $i$-wave altermagnets
Mohsen Yarmohammadi · [arXiv:2611.08761](https://arxiv.org/abs/2611.08761) · cond-mat.mtrl-sci · new

**为何相关：** 用双色光在 Rashba 耦合磁多极（从 p 波磁体到 i 波交错磁）中产生垂直于 Néel 矢量的电子力矩，并以精确 Floquet 响应验证——交错磁 × Floquet 光控磁。

要点：对具有面外序参量的二维磁体，逆法拉第场与 Néel 矢量共线，无法提供横向力矩。作者表明双色 $(\omega,b\omega)$ 光可在 Rashba 耦合的磁多极中产生垂直于 $\boldsymbol N$ 的电子力矩；除高频有效场外，还计算了指定占据下的精确 Floquet 响应与每占据电子的广义力矩。动量依赖的交换项主导 Fermi 海力矩，并消除与振幅比无关的领头阶零点。面外 $\boldsymbol N$ 的横向力矩仅在反旋/同旋光束分别满足 $\mathrm{gcd}(n,b\pm 1)=1$ 时被转动对称允许；面内 $\boldsymbol N$ 时 Fermi 海还可给出动量无关场所不能产生的 $z$ 方向力矩。工作按频率标度与起源（周期平均 vs 振荡交换）对 $n=1,\ldots,6$、$b=1,\ldots,7$ 的活跃通道分类，并强调有限动量占据态物理对非常规磁体光驱动力矩的必要性。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 5. Symmetry-Resolved Criticality in Dissipative Quantum Phase Transitions
Xingli Li · Yan Li · Jinghui Pi 等 · [arXiv:2611.09450](https://arxiv.org/abs/2611.09450) · quant-ph · new

**为何相关：** 把强弱对称层次用作耗散临界性的操作探针，在二维耗散 XYZ 模型中连接半经典相空间、轨迹动力学与系综标度——开放多体 × 耗散相变 × 对称性。

要点：混合态对称破缺具有丰富的强–弱层次，但对称性作为耗散临界性的操作探针仍少被使用。作者发展连接半经典相空间、轨迹层动力学与系综响应的框架，并在二维耗散 XYZ 模型上示范：对称破缺在半经典体现为 Husimi-Q 分布的分岔，在动力学上体现为轨迹层对称残差的突变；系综层面对微扰对称算符的弱对称敏感度呈现显著有限尺寸标度，从而估计耗散临界点。还提出基于轨迹的量子线路算法，以中途测量条件化量子跳跃，从而从线路可观测量提取这些指标。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 6. Exploring topological signatures of quantum Fisher information scaling in graph states
Majid Hassani · Patrick Emonts · Jordi Tura · [arXiv:2611.08593](https://arxiv.org/abs/2611.08593) · quant-ph · new

**为何相关：** 追问图的 clique 复形 Betti 数能否刻画图态量子 Fisher 信息是否超越标准量子极限，并给出拓扑优化生成计量有用图态的路径——量子计量 × 拓扑不变量 × 图态。

要点：图态是量子计量的灵活资源，其 QFI 可写成图中具有相同邻域的顶点对数，但何种全局结构决定 QFI 超越 SQL 仍不清楚。作者数值检验 clique 复形的 Betti 数：在平衡完全多部图上随机加/删边，加边最终同时破坏计量优势与非平凡拓扑，删边时高阶 Betti 数在 QFI 已降至 SQL 之后仍可长期存活；从通常不超越 SQL 的 Erdős–Rényi 随机图出发，用蒙特卡罗最大化某一 Betti 数，则驱动图走向近极值多部结构且 QFI 显著超越 SQL。结果表明拓扑优化可通向计量有用的图态，但单靠 Betti 数并不能决定 QFI。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 7. Local Correlations Determine the Dephasing Threshold of $\mathbb{Z}_2$ Topology
Rishith Reddy V · Ashutosh Dubey · Partha Sarathi 等 · [arXiv:2611.09668](https://arxiv.org/abs/2611.09668) · cond-mat.mes-hall · new

**为何相关：** 在 Kane–Mele $\mathbb{Z}_2$ 拓扑绝缘体中，用与单粒子关联相同的辅助哈密顿能隙关闭（关联纯度隙）判定退相位下拓扑不变量的存活——拓扑 × 退相位/开放系统。

要点：作者讨论能带拓扑在退相位下如何存活，并以 Kane–Mele $\mathbb{Z}_2$ 拓扑绝缘体为例。他们构造一个在单粒子层面给出相同关联的单粒子哈密顿，把拓扑到平庸的转变等同于该关联哈密顿的能隙关闭，并与纯度隙相联系；直接计算不变量，并以该辅助哈密顿的相干两端电导在非平庸区量子化为互补诊断（这并不等同于退相位下的物理电导）。结果给出在指定噪声通道下单粒子拓扑结构存活的可预测局域判据。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 8. Optimal performance of driven-dissipative many-body quantum batteries beyond complete nonreciprocity
Vimal Sreekanth · Chandrima B. Pushpan · Amit Kumar Pal · [arXiv:2611.09434](https://arxiv.org/abs/2611.09434) · quant-ph · new

**为何相关：** 指出相互作用量子比特电池的最优充电一般并不落在完全非互易点，而由相干耦合与局域/集体耗散率的更细致权衡决定——驱动–耗散 × 开放系统 × 量子电池。

要点：既有非互易量子电池方案常把相干耦合与库介导耦合平衡的完全非互易点视为增强充电的工作点。作者表明，对由相互作用量子比特构成的电池，该点通常并非最优：最优设计取决于相干耦合与局域、集体耗散率的更复杂交织。他们考虑由驱动多体充电器充电、各量子比特耦合局域浴并共同浸于共享工程库的设定；弱驱动两量子比特情形下证明 Dzyaloshinskii–Moriya 相互作用为最优耦合，电池容量在由局域与集体耗散率共同决定的耦合强度处最大，仅在二者特定配比时才与完全非互易重合。共享库可在耦合弱于或强于两局域耗散率时增强容量，甚至在降低容量处仍可增加可提取功；强驱动下容量以 $1/2$ 为界。星形网络等有限尺寸标度也得到讨论。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 9. Coexistence of antiferromagnetism and topological $s+d+id$ superconductivity in twisted cuprate bilayers
Javier Castro Luaces · Manuel Fernández López · Jorge Bravo-Abad 等 · [arXiv:2611.09469](https://arxiv.org/abs/2611.09469) · cond-mat.str-el · new

**为何相关：** 在近 $45^\circ$ 扭转铜基双层的微观 $t$–$J$ 模型中给出与反铁磁共存的拓扑 $s+d+id$ 超导，并指出其两条 Majorana 边缘模的实验指纹——拓扑超导 × 反铁磁共存 × Majorana 边模。

要点：作者表明 $\theta\sim 45^\circ$ 扭转可在铜基双层的微观 $t$–$J$ 型模型中诱导拓扑 $s+d+id$ 超导，并在低空穴掺杂下与反铁磁序稳健共存；该配对在过掺杂区、现实层间耦合下即可物理可达。它在 ARPES 中呈现竞争的破时间反演 $d+id$ 或 $s+id$ 态所没有的特征二重旋转对称；$45^\circ$ 扭转下有限 Josephson 效应，以及扫描隧道谱中两条 Majorana 边缘模的签名，可唯一标识该拓扑 $s+d+id$ 态。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 10. Density kernel and temporal quantum information probes in double-scaled SYK
Johanna Erdmenger · Maximilian Gaschler · Jonathan Karl 等 · [arXiv:2611.08592](https://arxiv.org/abs/2611.08592) · hep-th · new

**为何相关：** 在双标度 SYK 的精确弦 Hilbert 空间中构造来自时间关联的非厄米密度核，用以诊断跨时间的量子信息与记忆损失——非厄米密度核 × 时间纠缠 × 多体量子信息。

要点：纠缠通常定义在固定时间切片的 Hilbert 空间二分上；近期工作通过由时间关联函数构造的非厄米密度核，把该观念推广到多个时刻，以编码因果响应、时间非经典性与量子动力学。作者在 DSSYK 的精确弦 Hilbert 空间中构造该核：弦空间的直和结构自然引入粗粒化并去除不同弦扇区之间的相干，相应核度量刻画信息如何在弦空间子区域间动态传递。减小 $\lambda$ 会增强时间关联跨扇区的传播以及固定扇区内的记忆损失，这种加速的时间动力学与半经典引力描述的出现相一致；特征传播时间可由 Krylov 空间中由 DSSYK Lanczos 系数决定的位置依赖跳跃的波前来捕捉。工作为在量子与半经典引力区间探测时间量子关联提供可控设定。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*

---

### 11. Exciton design via topological spin textures
Karim Rezouali · Selcuk Sözeri · Samir Lounis · [arXiv:2611.09800](https://arxiv.org/abs/2611.09800) · cond-mat.mes-hall · new

**为何相关：** 把电子与空穴作为各自带自旋轨道耦合的组分，证明斯格明子拓扑仅在交换超过相关自旋轨道劈裂时传递给激子，从而以拓扑荷决定光学选择定则并实现电流驱动输运——自旋电子学 × 斯格明子 × 激子拓扑。

要点：激子不带电荷地输运能量与信息，因而难以导向；磁斯格明子则可由小电流驱动。作者发展激子与斯格明子相互作用的理论：仅当交换耦合超过相关自旋轨道劈裂时，斯格明子拓扑才传递给激子，使其感受整整一个通量量子、并在两个谷中符号相反。自旋纹理的量子度规形成环状势垒以束缚激子，而拓扑荷决定被俘获态的角动量及其光学选择定则。势阱随斯格明子移动，从而可用电流脉冲输运激子；小尺寸斯格明子可容纳单个激子，为把拓扑磁比特与光激发交织的混合信息器件提供可能路径。

*Zotero：本日无法访问实时库；缓存 ID 列表中无同 ID。*
