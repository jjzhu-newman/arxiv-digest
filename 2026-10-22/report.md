# 10/22 arXiv 兴趣摘要（工作日）


扫了今天（美西 10/22，周四）新上线的 `cond-mat`、`quant-ph`、`hep-th`、`math-ph`，以及 `cs.LG` / `stat.ML` 里偏物理信息或量子的条目。公告页标注 **Thursday, 22 October 2026**；新投稿：cond-mat 77、quant-ph 47、hep-th 21、math-ph 10、cs.LG 137、stat.ML 13（交叉与替换未计入）。已排除 10 月已荐的 161 篇。非厄米/纠缠侧有多比特纠缠能带与无增益损耗例外点，以及边界 EP 驱动的 SSH 边态手性开关；交错磁×张量有 quantics 张量列车上的多圈 fRG 杂质计算；拓扑有部分潜伏对称保护的近似拓扑绝缘体（含非厄米实验），以及星格点手性 Kitaev 自旋液体的 PSG/Klein 对偶稳定窗口；另有 TRSB 超导本征光学反常霍尔的量子几何理论、双栅 vdW 自旋织构电控、量子斯格明子磁子约瑟夫森结、开放系统完全弛豫代数判据与非马尔可夫量子模拟，以及 Hofstadter–Hubbard 中轨道磁通稳定的手性自旋液体分数化。按兴趣锚点筛了 **11 篇**（全部为新投稿；未收替换稿；跳过软物质胶体/电解质、连续介质热传导、Petri 网消息传递、临床可穿戴差分隐私 QML、纯光学平带边模交叉稿、气象类 PINN 等假阳性）。本地桌面当时未在线，**未做 Zotero 核对**。

**建议先翻这三篇：**
1. **An entanglement band structure for general multiqubit states** —— 把多比特纠缠不变量写成球面上的非厄米本征值“能带”，无增益/损耗即可出现例外点；绕 EP 交换两带形成黎曼面，五比特时可有限歧义地标定纠缠类——纠缠 × 非厄米拓扑。
2. **Boundary exceptional point driven chiral switch of topological edge states** —— 有限 SSH 链两端局域非厄米势诱导边界例外点，解析给出 Γ_EP；动力学环绕可实现手性、近乎完美保真度的拓扑边态对端转移，且不扰动体带——非厄米 × 拓扑边态操控。
3. **Quantics tensor trains for multiloop fRG in multiorbital impurities** —— 把多圈 fRG 直接写在 quantics 张量列车上，保留三独立顶点频率且免显式高频参数化；并在补偿交错磁环境下展示轨道劈裂诱导的局域自旋响应——张量网络 × 强关联 × altermagnetism。

---

### 1. An entanglement band structure for general multiqubit states
Chon-Fai Kam · [arXiv:2610.30040](https://arxiv.org/abs/2610.30040) · quant-ph · new

**为何相关：** 把多比特纠缠不变量写成球面上的非厄米本征值“能带”，无增益/损耗即可出现例外点；绕 EP 交换两带形成黎曼面，五比特时可有限歧义地标定纠缠类——纠缠 × 非厄米拓扑。

要点：Majorana 曾用 Bloch 球上的点刻画对称多比特态。本文对一般态只投影一个比特，其余子系统的纠缠不变量成为方向依赖的非厄米矩阵本征值，并在球面上形成“纠缠能带”。例外点在无增益/损耗处出现，标志其余子系统纠缠族的切换；环绕 EP 使两带交换，故能带组成单一黎曼面。在五比特情形，该结构可在有限歧义内固定纠缠类。工作把纠缠分类与非厄米能带/例外点语言直接对接。

---

### 2. Boundary exceptional point driven chiral switch of topological edge states
Bikashkali Midya · Barsa Rani Sahu · [arXiv:2610.29316](https://arxiv.org/abs/2610.29316) · quant-ph · new

**为何相关：** 有限 SSH 链两端局域非厄米势诱导边界例外点，解析给出 Γ_EP；动力学环绕可实现手性、近乎完美保真度的拓扑边态对端转移，且不扰动体带——非厄米 × 拓扑边态操控。

要点：作者研究两端带增益/损耗的有限 SSH 链：利用有限尺寸下两条 mid-gap 边态杂化，解析得到边界诱导例外点坐标 Γ_EP=±i v^N/w^{N-1}，此处边态合并。动力学环绕边界 EP 可实现鲁棒手性边态转移：依环绕取向，一端局域边态或以近乎完美保真度转到对端，或经双切换回到起点。非厄米性严格限于边界，故手性输运不改体带谱。框架最小、可实验检验，适合边界驱动的大规模拓扑手性开关。

---

### 3. Quantics tensor trains for multiloop functional renormalization group in multiorbital impurity models
Hyun-Yong Lee · Naoki Kawashima · [arXiv:2610.29341](https://arxiv.org/abs/2610.29341) · cond-mat.str-el · new

**为何相关：** 把多圈 fRG 直接写在 quantics 张量列车上，保留三独立顶点频率且免显式高频参数化；并在补偿交错磁环境下展示轨道劈裂诱导的局域自旋响应——张量网络 × 强关联 × altermagnetism。

要点：多轨道杂质的全频率相互作用数值昂贵。作者将多圈函数重整化群直接置于 quantics 张量列车表示，在宽频率范围保留三个独立顶点频率，无需显式高频参数化；解析张量算子完成频率变换与内求和，避免稠密顶点中间量。多圈修正改善与独立参考的顶点/响应符合，并复现低能 NRG 自能。低温计算分辨解析延拓散射率的二次频率贡献。简并双轨道杂质在固定 Hund 耦合下呈现不同自旋/轨道/电荷响应；在补偿交错磁环境中，轨道能级劈裂即使未扰杂质磁化为零也可诱导局域自旋响应，增大 Hund 抑制轨道响应却增强自旋极化——单粒子重整化传播无法复现该强极化依赖。

---

### 4. Ubiquitous topological materials protected by hidden partial symmetries
Lumen Eek · Xuelong Chen · Malte Röntgen · Wenlong Gao 等 · [arXiv:2610.29028](https://arxiv.org/abs/2610.29028) · cond-mat.mes-hall · new

**为何相关：** 提出“部分潜伏对称”：只需在有效哈密顿量某些能标近似成立即可保护近似量子化拓扑与稳健边态，并实验实现厄米/非厄米弱对称 SSH、BBH 样模型——拓扑保护条件的弱化 × 非厄米。

要点：传统拓扑相要求对称性在整个系统成立。作者引入 partial latent symmetries：只需在有效哈密顿量的特定能标近似不变。据此构造 SSH 与 Benalcazar–Bernevig–Hughes 的弱对称版本：行为类似常规对应物并承载稳健边态，但拓扑不变量仅近似量子化。文末实验实现厄米与非厄米近似拓扑绝缘体并探测边态。工作提示可用弱对称要求替代强对称约束，拓宽可实现拓扑材料范围。

---

### 5. Chirality, Klein duality, and the stability of Kitaev spin liquids on the star lattice
Harsh Raj · Yasir Iqbal · [arXiv:2610.29278](https://arxiv.org/abs/2610.29278) · cond-mat.str-el · new

**为何相关：** 星格点 Yao–Kivelson 手性 Kitaev 自旋液体的 PSG 与 Klein 对偶分析：自旋–规范锁定下必须破时间反演；并解释 AF 相对 FM Kitaev 侧 Heisenberg 扰动稳定窗口窄得多——Kitaev/任意子序 × 拓扑自旋液体。

要点：星格点承载 Yao–Kivelson 手性自旋液体，恰可解 Kitaev 点依耦合比可为非阿贝尔或阿贝尔。先前 DMRG 显示加 Heisenberg 后 FM Kitaev 稳定窗宽、AF 侧极窄。作者用费米部分子投影对称群证明：只要 π 自旋转动对部分子作用与精确解相同（自旋–规范锁定），时间反演对称平均场在任意程三角形上振幅为零，故该格点上 Kitaev 型自旋液体必须破时间反演。两种符号的阿贝尔/非阿贝尔液体共享同一手性 PSG，其间转变是能带反转。Klein 对偶反转 Heisenberg 并置换 PSG，锁定类不变；映到自身的 Z₂ 自旋液体相若连通则含 Kitaev 点。关于 Kitaev 点的二阶微扰定位不对称：三角形响应两边相同，而三角形间键上两非对角 Heisenberg 项产生相同四 vison 并在 AF 侧相长、FM 侧近相消，使低能四 vison 在 AF 侧混入强约 82 倍。另分类 352 个含自旋轨道振幅的 Z₂ PSG。

---

### 6. Theory of the intrinsic optical anomalous Hall responses in time-reversal symmetry breaking superconductors
Jia-Long Zhang · Wen Huang · [arXiv:2610.28786](https://arxiv.org/abs/2610.28786) · cond-mat.supr-con · new

**为何相关：** 统一处理破时间反演多带超导体的本征光学反常霍尔：证明其为量子几何效应，厘清幺正/非幺正配对方、带间配对与 SOC 的必要条件——拓扑超导 × Berry/量子几何 × 自旋霍尔类响应。

要点：破时间反演（含拓扑 p_x+ip_y）超导期望光学反常霍尔，但干净极限微观要件未清。作者对具空间反演的 TRSB 多带超导建立统一理论，把本征光学霍尔确立为量子几何现象。区分幺正与非幺正 TRSB；图示两类过程——单电子隧穿与库珀对隧穿——皆至少含一次由带间速度（关联带间 Berry 联络）驱动的带间隧穿。严格证明：幺正态要产生本征霍尔必须有带间配对；非幺正态则非绝对必要，仅带内配对也可经单电子隧穿产生霍尔（需 SOC）。积出空穴自由度的有效理论复现上述结论，并说明配对如何赋予电子有效 Berry 曲率。对称分析还表明：近超导能隙边的本征共振在非幺正态允许、在幺正态禁戒，可作配对候选鉴别指南。

---

### 7. Electric-field tunable spin texture in dual-gated HfS$_2$/graphene van der Waals heterostructures
Haozhe Yang · Zhendong Chi · Eoin Dolan · Josep Ingla-Aynés 等 · [arXiv:2610.29739](https://arxiv.org/abs/2610.29739) · cond-mat.mes-hall · new

**为何相关：** 双栅 HfS₂/石墨烯异质结实验：垂直电场重组有效自旋织构，把自旋–电荷转换从出平面自旋霍尔主导调到含 Rashba–Edelstein 面内分量——自旋轨道 × 自旋电子学电控。

要点：自旋–电荷转换可含多种自旋极化方向分量，反映底层自旋织构。石墨烯范德华异质结界面 SOC 可托管多通道。作者在双栅 HfS₂/石墨烯中独立调控载流子密度与垂直电场，以区分静电掺杂与电场诱导自旋轨道效应。非局域自旋进动显示：近零垂直场时转换以出平面自旋的自旋霍尔分量为主；增大垂直场增强 Rashba–Edelstein 型面内自旋分量（含平行与垂直于电流方向）。实验证据表明垂直电场可重构有效自旋织构并调控各转换分量，实现自旋轨道功能的电学可调。

---

### 8. Two quantum skyrmions form a magnon Josephson junction
R. L. Silva · [arXiv:2610.28854](https://arxiv.org/abs/2610.28854) · cond-mat.other · new

**为何相关：** 阻挫自旋-1/2 磁体中两个量子斯格明子束缚成“分子”，相对螺旋度与转移磁子数构成磁子约瑟夫森结 H=E_C n²−W cosθ——斯格明子 × 磁子相干/量子自旋电子学。

要点：两个量子斯格明子在阻挫自旋-1/2 磁体中束缚成分子，分子充当磁子约瑟夫森结：相对螺旋度 θ 与其间转移的磁子数 n 满足 H=E_C n²−W cosθ。在 J₁–J₂ 三角格点上 DMRG 给出 E_C 为自然尺寸（七个翻转自旋）处斯格明子能量曲率；测得的螺旋度相干定出 W≃0.02 J₁，约为斯格明子–反斯格明子隧穿劈裂之半且与各向异性无关。并排放置的两个螺旋度量子比特因而被自身相互作用强耦合。

---

### 9. Algebraic criteria for complete relaxation in autonomous and periodically driven open quantum systems
Paul Menczel · Kay Brandner · [arXiv:2610.29084](https://arxiv.org/abs/2610.29084) · cond-mat.stat-mech · new

**为何相关：** 对有限维 GKSL 开放系统给出保证“完全弛豫”（与初态无关收敛到唯一稳态）的代数判据，并新增周期驱动情形的判据——开放系统 × 周期驱动/Floquet 主方程。

要点：作者推导保证开放量子动力学完全弛豫（长期态唯一且与初态无关）的充分判据，聚焦有限维 Hilbert 空间上的 GKSL 主方程，论证只用初等数学。对自治系统复现三条已知判据，表述为 Lindblad 算子与哈密顿量的代数条件。对周期驱动系统给出新判据：类似代数条件外加时依赖 GKSL 生成元的局部连续性要求，并蕴含早先文献判据。文中亦讨论对周期调制经典主方程的含义，以及无周期性约束驱动系统的推广。

---

### 10. Quantum Simulation of Non-Markovian Open Quantum Systems via Low-Rank Kernel Compression and Coupling Dilution
Hengzhun Chen · Zhenning Cai · [arXiv:2610.29372](https://arxiv.org/abs/2610.29372) · quant-ph · new

**为何相关：** 高斯环境非马尔可夫开放动力学的量子模拟：用相关核低秩压缩得到等效有限玻色浴，并引入耦合稀释以控制局域维数，给出约化态误差界与多项式线路资源——开放系统 × 量子模拟。

要点：对线性耦合、零均值高斯环境，浴对约化动力学的影响完全由双时相关核决定，故可用同核等效浴替换微观环境。有限模拟区间上核的秩-N 近似给出 N 个时依赖耦合玻色模。编码到量子比特时先截断各模到最低 d 能级；强耦合导致高占据时引入耦合稀释：用多个更弱耦合副本替换单模并保持相关核，以更多模换更小局域维数。文中给出约化态误差界，并在谱衰减与耦合正则性假设下建立模拟时间与精度倒数的多项式线路宽度/深度（若基本幺正可多项式实现）。

---

### 11. Stabilizing and detecting electron fractionalization in the Hofstadter-Hubbard model
Jiahao Yang · Zeyu Han · Gang v. Chen · [arXiv:2610.29916](https://arxiv.org/abs/2610.29916) · cond-mat.str-el · new

**为何相关：** 三角格 Hofstadter–Hubbard 半填充：增大轨道磁通稳定并拓宽 Mott 区 U(1)₂ 手性自旋液体，电子分裂为带隙 spinon/chargon，谱函数给出可测指纹——拓扑序/分数化 × 莫尔 Chern 绝缘体动机。

要点：受莫尔关联 Chern 绝缘体进展启发，作者研究半填充三角格 Hofstadter–Hubbard 模型中的电子分数化。在多种竞争非磁态中，增大轨道磁通可在 Mott 区稳定并拓宽 U(1)₂ 手性自旋液体。该区电子分裂为带隙 spinon 与带隙 chargon，有效能带与轨道磁通相连；窄 spinon 带与带隙 chargon 激发的卷积在电子谱函数与态密度中产生丰富可辨结构。结果把轨道磁通标为调控分数化细节与 Mott 转变性质的参数，并为 ARPES/STM 提供关联区本征拓扑序相对自由粒子能带拓扑的关键谱学特征。
