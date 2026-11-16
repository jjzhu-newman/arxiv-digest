# 10/30 arXiv 兴趣摘要（工作日）

扫了今天（美西 10/30，周五）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Friday, 30 October 2026**（周四 10/29 因 arXiv 数据库云迁移曾推迟公告，故周五批次偏重）；新投稿：cond-mat 178、quant-ph 128、hep-th 58、math-ph 24、cs.LG 213、stat.ML 24（交叉与替换未计入）。已排除 10 月已荐的 205 篇。非厄米/开放与 Floquet 侧有非互易 Floquet 自旋隧穿、带记忆的非 Bloch DQPT、以及耗散腔辅助的 Floquet 态稳定化；实验上圆偏振驱动石墨烯给出光致拓扑态的动量分辨指纹；交错磁侧有 AFM/AM 结磁子阀、元交错磁跃迁增强自旋劈裂、以及光致手性交错磁；NNQS/任意子有理想任意子气体的神经变分波函数与 FQHE 深度学波函数；另有结构浴制备多体纠缠稳态，以及 Kitaev 自旋液边缘的引力异常光谱读出。按兴趣锚点筛了 **11 篇**（10 篇新投稿 + 1 篇交叉；未收替换稿；跳过假阳性 PINN/NN 命中如二极管 PINN 代理、涡旋存储 Landauer 极限、软物质耗散动力学学习，以及纯数学 Floquet 模空间、黑洞 Schwinger–Keldysh、Gaenice 人工自旋冰耗散弛豫、弱相关 VQA/通用 QNN 与宽泛二维磁体综述等）。已对本地 Zotero 库做只读核对：**短名单无同 arXiv ID**；Floquet 石墨烯、交错磁与 non-Bloch/DQPT 方向库内有主题近邻条目，已在相关条目中注明。

**建议先翻这三篇：**
1. **Variational wavefunctions for ideal anyon gas: superfluid and skyrmion Hall crystal** —— 把复合玻色子/费米子与 parton 波函数接到球面上的神经网络关联，覆盖任意子超流与 skyrmion Hall 晶体——NNQS × 任意子统计 × FCI 相关多体。
2. **Observation of light-induced topological state in graphene** —— 圆偏振驱动石墨烯中用圆二色 trARPES/动量显微观测到泵浦诱导的近 Dirac 点光电子圆二色，符号随泵浦手性与 Dirac 能翻转——Floquet Chern × 实验拓扑态。
3. **Nonreciprocal Floquet tunneling dynamics of spin-orbit-coupled bosonic atoms in a non-Hermitian double-well potential** —— 非厄米双阱中自旋–轨道耦合玻色原子的非互易 Floquet 隧穿：增益损耗与非互易耦合协同扩大稳定自旋翻转区——非厄米 × Floquet × SOC。

---

### 1. Variational wavefunctions for ideal anyon gas: superfluid and skyrmion Hall crystal
Ya-Hui Zhang · [arXiv:2610.40657](https://arxiv.org/abs/2610.40657) · cond-mat.str-el · new

**为何相关：** 把复合玻色子/费米子与 parton 波函数接到球面上的神经网络关联，覆盖任意子超流与 skyrmion Hall 晶体——NNQS × 任意子统计 × FCI 相关多体。

要点：理想任意子气体的基态长期未决，并因分数量子霍尔/分数量子陈绝缘体实验再度升温。作者构造内建精确交换统计的变分波函数，并把理论引导的复合玻色子、复合费米子与 parton 态与球面上的神经网络关联结合。对无自旋与 SU(2) semion，确认配对任意子超流能量显著低于最佳晶体；θ=π/3 时无自旋情形液/晶更接近。对带 SU(3) 味的 θ=π/3 任意子，找到两类候选：skyrmion Hall 晶体（任意子在自旋织构等效磁场中形成整数量子霍尔态），以及六任意子团簇的手性色超导（超行列式而非 parton 行列式之积）；在所给变分 ansatz 下色超导优于晶体与对照液体。工作把 NNQS 直接接到任意子超流与拓扑晶体竞争。

---

### 2. Observation of light-induced topological state in graphene
Sotirios Fragkos · Ann Chantal Goutier · Umberto Dellasette 等 · [arXiv:2610.39695](https://arxiv.org/abs/2610.39695) · cond-mat.mtrl-sci · new

**为何相关：** 圆偏振驱动石墨烯中用圆二色 trARPES/动量显微观测到泵浦诱导的近 Dirac 点光电子圆二色，符号随泵浦手性与 Dirac 能翻转——Floquet Chern × 实验拓扑态。

要点：圆偏振光驱动石墨烯被预言在 Dirac 点开隙并诱导 Haldane 型赝自旋织构与 Berry 曲率，实现 Floquet Chern 绝缘体；既往输运/全光测量给出光致反常霍尔证据，但难同时在能量–动量空间分辨电子态，而线偏振 trARPES 虽见 Floquet–Bloch 边带却保持时间反演、不诱导拓扑相。作者结合圆二色时间分辨极紫外动量显微与第一性原理，观测到泵浦诱导的近 Dirac 点光电子圆二色：符号随泵浦手性翻转，并跨 Dirac 能变号，与计算的 Floquet 拓扑态一致。结果为光致拓扑态提供动量分辨的直接光谱指纹。

*Zotero：库中无同 ID。 库内有 Light-induced anomalous Hall effect in graphene、Towards Floquet Chern insulators of light 等近邻条目。*

---

### 3. Nonreciprocal Floquet tunneling dynamics of spin-orbit-coupled bosonic atoms in a non-Hermitian double-well potential
Limei Ju · Yingying Zhang · Jilei Liang 等 · [arXiv:2610.38597](https://arxiv.org/abs/2610.38597) · cond-mat.quant-gas · new

**为何相关：** 非厄米双阱中自旋–轨道耦合玻色原子的非互易 Floquet 隧穿：增益损耗与非互易耦合协同扩大稳定自旋翻转区——非厄米 × Floquet × SOC。

要点：非厄米体系中稳定隧穿与非互易耦合如何调控自旋输运，是开放量子器件的基本问题。作者把自旋–轨道耦合玻色原子置于含增益损耗的双阱，解析 Floquet 态与准能谱得到 PT 对称相图，并考察非互易耦合强度、增益损耗非厄米强度与周期驱动对稳定自旋翻转隧穿的协同调控。结果表明精确操控非互易与增益损耗可显著扩大稳定参数区；在平衡增益损耗的非互易系统中，稳定区连续或离散由驱动频率比 Ω/ω₀ 的奇偶性决定。工作把非厄米、Floquet 与 SOC 自旋隧穿接到同一可控平台。

---

### 4. Non-Bloch Dynamical Quantum Phase Transitions with Memory
Zhesen Yang · Wei-Wei Yang · Henning Schomerus · Jiangping Hu · [arXiv:2610.39994](https://arxiv.org/abs/2610.39994) · cond-mat.mes-hall · new

**为何相关：** 带记忆的衬底耦合使厄米链出现仅开放边界才有的非 Bloch DQPT，由投影传播子点隙绕数 W 决定——开放/记忆 × 非厄米拓扑 × DQPT。

要点：周期链的动力学量子相变通常由实 Bloch 动量决定。作者识别仅开放链才出现、由复动量决定的非 Bloch DQPT：它们出现在耦合到简单衬底、记忆被精确处理的厄米链中，并源于投影传播子的点隙绕数 W——当 W≠0 时，即便热力学极限下开放边界也会改变动力学自由能与临界时刻。二者均可由向复动量的解析延拓得到，且 W 可用粒子计数测量。结果揭示动力学体–边对应：非厄米拓扑可从带记忆的厄米动力学中涌现。

*Zotero：库中无同 ID。 库内有 non-Bloch / DQPT 相关条目，主题相邻。*

---

### 5. Nodal magnon spin current at an antiferromagnet/altermagnet junction
Koki Mizuno · [arXiv:2610.39206](https://arxiv.org/abs/2610.39206) · cond-mat.mes-hall · new

**为何相关：** d 波交错磁与反铁磁结的热驱动磁子自旋流：子格对称界面下 AFM/AM 结对畴平均保留 d 波角依赖并作磁子阀——交错磁 × 自旋电子学。

要点：作者研究 d 波交错磁（AM）与铁磁（FM）或反铁磁（AFM）结上热驱动的磁子自旋流：电流含与界面角无关分量及 d 波形角依赖分量。对子格对称界面，畴反转下两种结行为相反——FM/AM 的角依赖分量为奇并在畴平均后抵消；AFM/AM 的角无关分量由对称性消失，角依赖分量在固定 AFM Néel 矢量下可经畴平均存活。选择性隧穿使平行跨界面自旋对可传磁子、反平行则阻断，从而 AFM/AM 结成为磁子阀。各向异性隧穿可由 [310] 与 [130] 法向界面电流变号探测。

*Zotero：库中无同 ID。 库内交错磁主题条目较多，但本题为新机制/新结型。*

---

### 6. Meta-Altermagnetism and Enhanced Spin-Splitting
Bogeng Wen · Hae-Young Kee · [arXiv:2610.37754](https://arxiv.org/abs/2610.37754) · cond-mat.str-el · new

**为何相关：** 自旋劈裂 van Hove 奇点跨费米面可触发一级“元交错磁”跃迁，中间相八极矩与自旋劈裂电导反常增强——交错磁 × 自旋劈裂增强。

要点：交错磁是净磁化为零却有自旋劈裂能带的共线磁体。作者追问交错磁是否可发生不连续跃迁（元交错磁）：在二维中，磁有序诱导的能带重构把自旋劈裂 van Hove 奇点推过费米面即可触发。扩展 t–J 模型平均场显示，一级元交错磁跃迁给出中间交错磁区——交错磁化减弱，但磁八极矩与时间反演奇的自旋劈裂电导反而显著增强；一级线终止于量子临界端点，随化学势与各向异性跃迁强度给出丰富相图。自旋劈裂 vHS 被指认为增强自旋劈裂效应的通路。

*Zotero：库中无同 ID。 库内交错磁主题条目较多，但本题为新机制/新结型。*

---

### 7. Light-induced chiral altermagnets from conventional antiferromagnets
Jorge Cardenas-Gamboa · Devika Jayadeep · Aritz Leonardo 等 · [arXiv:2610.40410](https://arxiv.org/abs/2610.40410) · cond-mat.mtrl-sci · new

**为何相关：** 对称分析给出手性声子等畸变把常规反铁磁诱导为交错磁；Fe₂TeO₆ 中红外脉冲驱动瞬态手性结构并出现非相对论自旋劈裂——光控 × 交错磁。

要点：交错磁兼具补偿共线磁序与动量依赖非相对论自旋劈裂。作者提出经相干晶格调控光学诱导交错磁的路径：对称分析识别在保持连接相反自旋子格的转动对称性的同时抬起常规反铁磁自旋简并的声子畸变；其中几何手性声子把交错磁出现与结构手性相连。以 Fe₂TeO₆ 为原型，线偏振中红外脉冲可经红外活性声子与光学静默对称破缺模之间的负双二次耦合驱动结构不稳；第一性原理晶格动力学给出瞬态手性畸变，电子结构确认光致结构具交错磁特征的非相对论自旋劈裂。

*Zotero：库中无同 ID。 库内交错磁主题条目较多，但本题为新机制/新结型。*

---

### 8. Exploring Fractional Quantum Hall States with Deep Learning: From Abelian to Non-Abelian Phases
Xiangyu Ma · Kehuang Chen · Yuntian Gu 等 · [arXiv:2610.38533](https://arxiv.org/abs/2610.38533) · physics.comp-ph · cross

**为何相关：** 对称适应的神经网络波函数同时描述 Abel/非 Abel FQHE 并纳入全部朗道能级，有限尺寸重叠与纠缠谱支持 parton/反 Pfaffian 证据——NNQS × FQHE 拓扑序。

要点：分数量子霍尔体系竞争拓扑相近简并且朗道能级混合难处理。作者引入对称适应的神经网络波函数，可同时描述 Abel 与非 Abel 态并纳入全部朗道能级：方法准确捕捉复合费米液体及低填充下 Wigner 结晶的出现；第一朗道能级部分填充时，有限尺寸重叠与纠缠谱给出与 ν=4/3、7/5 处 parton 相相一致的证据，而 ν=3/2 呈现类反 Pfaffian 纠缠结构。神经网络波函数由此成为研究 FQHE 竞争拓扑序的灵活框架。

---

### 9. Resonance and Transition-Channel Competition in Cavity-Assisted Floquet-State Stabilization
Zhuocheng Ma · Hongzheng Zhao · Liang-You Peng · [arXiv:2610.39169](https://arxiv.org/abs/2610.39169) · quant-ph · new

**为何相关：** 耗散腔辅助 Floquet 本征态稳定在中等驱动频率下不只依赖共振，而由共振选择与腔诱导跃迁强度的竞争决定——开放系统 × Floquet 稳定化。

要点：静态耦合到耗散腔曾被提出可自主稳定 Floquet 本征态：腔在光子能量匹配准能差（模驱动量子）时提供能量选择弛豫通道。作者表明在中等驱动频率下，仅共振条件并不足以保证稳定——稳态由共振选择与腔诱导 Floquet 态间跃迁强度的协作/竞争共同控制，可导致成功稳定、共振下仍混合的稳态，以及 Floquet 区杂化附近的完全失效。同一机制可推广到多能级自旋-S 系统，给出静态耗散何时可靠稳定驱动量子态的一般框架。

---

### 10. Generating Multipartite Entanglement via Structured-Bath Engineering
Baptiste Debecker · Philipp Westhoff · Visal So 等 · [arXiv:2610.38807](https://arxiv.org/abs/2610.38807) · quant-ph · new

**为何相关：** 局域独立库在结构浴与 Abelian 强对称下可把时间关联转成多体纠缠稳态，并工程化谱以制备 GHZ-like 态——开放系统 × 多体纠缠制备。

要点：作者展示如何用彼此独立的局域库，借助 Abelian 强对称与浴的时间关联，耗散制备真正多体纠缠稳态。在相互作用 Ising 链中，平坦浴对广泛的系统–环境耦合会指数抹去 Ising 轴关联；结构浴则把时间关联转为经典空间关联，强对称再将其提升到量子域以实现全局多体纠缠。弱耦合理论下，尽管生成元非二次，强对称仍把稳态构造化约为任意 Ising 耦合上的经典问题，并揭示经典可区分性与纠缠的精确联系；进一步工程化浴谱可增大关联长度并从可分初态制备 GHZ-like 态，且在精确 Markov 嵌入与张量网模拟中得到检验。

---

### 11. Gravitational anomaly spectroscopy of a Kitaev spin liquid
Kumar Ghosh · [arXiv:2610.38704](https://arxiv.org/abs/2610.38704) · cond-mat.str-el · new

**为何相关：** 把手性中心荷 c 写成边缘光谱量：弱行波调制的吸收权重给出 C≡2D₂−4D₁=c，并可无标定提取 Ising anyon 共形自旋——Kitaev 自旋液 × 拓扑异常光谱。

要点：手性中心荷 c 度量二维拓扑相的引力异常并固定边缘热流，既往多靠声子干扰的热输运或需纯基态的波函数探针。作者证明 c 是边缘的光谱量：沿边缘行进的弱耦合调制按 Virasoro 代数被吸收；相对同一耦合的静态响应归一化后，吸收权重满足 D_n=2n⟨L_0⟩+(c/12)(n³−n)，从而对理想边缘理论任意（含热）态有 C≡2D₂−4D₁=c。体中有/无 vison 的谱线权重比 Λ=4h_σ/c 无需标定即可固定非 Abel Ising anyon 的共形自旋。Kitaev 蜂窝自旋液在 7168 自旋上得 C≈0.49999、h_σ=0.06250；用谱线自身位移标定时约 96 自旋即可把 c 收到约 1%。

