# Tinmorry Bambu Studio 耗材配置文件

*[English](README.md) | [Tiếng Việt](README.vi.md)*

Fork 自 [TINMORRY/Tinmorry-Bambu_BambuStudio](https://github.com/TINMORRY/Tinmorry-Bambu_BambuStudio)。

定制的耗材预设，按切片软件（slicer）、再按耗材品牌、再按 Bambu Lab 打印机型号分类整理。目前收录 **Bambu Studio** 的 `.bbsflmt` 文件包，品牌为 **TINMORRY** 和 **eSUN**；仓库结构已为后续加入其他切片软件（如 OrcaSlicer）和其他品牌（如 ELEGOO）做好准备，无需再次重组。

## ⚠️ 注意事项 — 下载与使用前请阅读

- 下表中标记为 **衍生** 的配置文件**不是品牌官方导出的原版文件**。它们是通过将该品牌较小的、按打印机分类的 delta 数据与另一个文件包的机器参数合并生成的（详见 `CLAUDE.md` / `REFERENCES.md`），**未经 TINMORRY 或 eSUN 打印验证**。
- 在使用任何 **衍生** 配置打印之前，请将喷嘴、热床/打印板、腔体温度与耗材实际卷标或厂商数据表进行核对 —— **尤其是 X2D 上的 PA-CF 和 PAHT-CF**，这两个配置继承了 PETG CF 的温度范围，而不是它们自身的范围（通常明显低于 PA-CF/PAHT-CF 实际所需的温度）。
- **H2D、H2S、P2S、X2D 上大多数 eSUN 配置只有 "Direct Drive Standard" 挤出机变体的真实 eSUN 数据。** eSUN 自己按打印机导出的数据几乎总是未指定 "Direct Drive High Flow"/"Bowden Standard"/"Bowden High Flow" 三个变体的喷嘴温度、流量比和最大体积速度，因此这三个变体会悄悄继承作为模板的 TINMORRY 文件包的数值，而不是 eSUN 自己的数值 —— 在这四款打印机上用 Direct Drive Standard 以外的配置打印 eSUN 耗材前，请对照 eSUN 官方数据表核实。
- 对于任何含碳纤维（CF）或玻璃纤维（GF）的耗材（PETG-CF、PLA-CF、PET-CF、PC GF、TPU GF、PA-CF、PAHT-CF、PP-CF、PA6-CF、PA12-CF、ABS-CF、ABS-GF），请使用硬化/耐磨喷嘴。
- 在正式打印前先小批量试印并观察前几层，尤其是在没有机箱的打印机上（A1、A1 mini、A2L）。
- **A1 的 PC GF 配置是一个值得特别说明的特例**：Bambu Studio 本身为（开放式机架、无机箱）A1 提供了 PC-GF 的系统配置，因此本仓库将其作为直接证据收录 —— 但这并不代表 ABS/ASA 在 A1 上同样安全，本仓库也刻意没有为 A1 生成这些配置。如果你在开放式 A1 上打印 PC GF，请确保良好通风，并预期比有机箱的打印机更容易翘边。
- 这些配置文件按"现状"提供，不附带任何保证。使用前请自行确认某个配置文件对你的打印机和耗材是否安全。

## 目录结构

配置文件数据存放在 `profiles/` 下，生成它们的工具链存放在 `src/` 下。在 `profiles/` 内，每个顶层文件夹对应一种切片软件/导出格式；其下是耗材品牌文件夹；再其下的子文件夹对应各个打印机型号（与每个配置文件中 `compatible_printers` 字段的值一致）。`X2D` 额外嵌套了一个 `0.4mm` 喷嘴子文件夹。`BambuStudio/TINMORRY/` 和 `BambuStudio/eSUN/` 目前都有配置文件——其他切片软件文件夹（OrcaSlicer）和其他品牌文件夹（ELEGOO）会在有数据后以同样方式出现。

```
profiles/
  BambuStudio/
    TINMORRY/
      A1/       Bambu Lab A1，0.4mm 喷嘴
      A1mini/   Bambu Lab A1 mini，0.4mm 喷嘴
      A2L/      Bambu Lab A2L，0.4mm 喷嘴
      H2C/      Bambu Lab H2C，0.4mm 喷嘴
      H2D/      Bambu Lab H2D，0.4mm 喷嘴
      H2S/      Bambu Lab H2S，0.4mm 喷嘴
      P1S/      Bambu Lab P1S，0.4mm 喷嘴
      P2S/      Bambu Lab P2S，0.4mm 喷嘴
      X2D/0.4mm/  Bambu Lab X2D，0.4mm 喷嘴
    eSUN/
      A1/、A1mini/、H2C/、H2D/、H2S/、P1S/、P2S/、X2D/0.4mm/  结构与 TINMORRY/ 相同
src/       生成新 bundle 的 Python 工具链（详见 CLAUDE.md）
```

## 可用配置文件

点击下方打印机型号查看对应的耗材列表。每一行的 **下载** 链接直接指向 `.bbsflmt` 文件 —— 右键点击并选择"链接另存为"即可下载（无需克隆本仓库或在 GitHub 上浏览文件）。

- **原版** = 品牌（TINMORRY 或 eSUN）官方导出的真实文件，未经修改。
- **衍生** = 并非品牌直接导出；由本仓库的脚本根据该品牌较小的按打印机分类 delta 数据生成（详见 `CLAUDE.md`）。使用"衍生"配置前请阅读上方的 **⚠️ 注意事项**，尤其是 X2D 上的 PA-CF/PAHT-CF，以及 H2D/H2S/P2S/X2D 上 Bowden 或 High-Flow 变体的任何 eSUN 配置。

部分 TINMORRY 耗材（PETG GF、PETG Marble、PETG Metallic、TPU 95A）在 `profiles/BambuStudio/TINMORRY/X2D/0.4mm/` 下共用同一个文件包，同时覆盖 P2S 打印机。

<!-- BEGIN GENERATED PROFILE TABLES -->

### BambuStudio

#### TINMORRY

<details>
<summary><strong>Bambu Lab A1 (22)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| TINMORRY PC GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20TPU.bbsflmt) |
| TINMORRY TPU 95a | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20TPU%2095a.bbsflmt) |
| TINMORRY TPU GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab A1 mini (20)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| TINMORRY PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU 95A | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab A2L (20)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| TINMORRY PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Rapid | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PLA%20Rapid.bbsflmt) |
| TINMORRY PLA Silk | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU 95A | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2C (25)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| TINMORRY ABS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20ABS.bbsflmt) |
| TINMORRY ASA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20ASA.bbsflmt) |
| TINMORRY ASA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Rapid | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PLA%20Rapid.bbsflmt) |
| TINMORRY PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20TPU.bbsflmt) |
| TINMORRY TPU 95a | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20TPU%2095a.bbsflmt) |
| TINMORRY TPU GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2D (23)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| TINMORRY ABS pro | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20ABS%20pro.bbsflmt) |
| TINMORRY ASA CF | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte， | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PLA%20Matte%EF%BC%8C.bbsflmt) |
| TINMORRY PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20TPU.bbsflmt) |
| TINMORRY TPU 95a | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20TPU%2095a.bbsflmt) |
| TINMORRY TPU GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2S (22)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| TINMORRY ABS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20ABS.bbsflmt) |
| TINMORRY ABS Pro | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20ABS%20Pro.bbsflmt) |
| TINMORRY ASA CF | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG ECO | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Rapid | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PLA%20Rapid.bbsflmt) |
| TINMORRY PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU 95A | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab P1S (26)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| TINMORRY ABS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20ABS.bbsflmt) |
| TINMORRY ABS Pro | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20ABS%20Pro.bbsflmt) |
| TINMORRY ASA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20ASA.bbsflmt) |
| TINMORRY ASA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20TPU.bbsflmt) |
| TINMORRY TPU 95a | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20TPU%2095a.bbsflmt) |
| TINMORRY TPU GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab P2S (24)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| TINMORRY ABS Pro | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20ABS%20Pro.bbsflmt) |
| TINMORRY ASA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20ASA.bbsflmt) |
| TINMORRY ASA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG ECO | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY PP-CF ` | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PP-CF%20%60.bbsflmt) |
| TINMORRY TPU 95A | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab X2D (22)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| TINMORRY ABS Pro | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20ABS%20Pro.bbsflmt) |
| TINMORRY ASA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY ASA basic | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20ASA%20basic.bbsflmt) |
| TINMORRY PA-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PA-CF.bbsflmt) |
| TINMORRY PAHT-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PAHT-CF.bbsflmt) |
| TINMORRY PC GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PETG CF | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG ECO | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY PLA matte | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PLA%20matte.bbsflmt) |
| TINMORRY TPU 95A | 原版 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

#### eSUN

<details>
<summary><strong>Bambu Lab A1 (37)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| eSUN PEBA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab A1 mini (37)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| eSUN PEBA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A1mini/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab A2L (37)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| eSUN PEBA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2C (51)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| eSUN ABS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ABS.bbsflmt) |
| eSUN ABS ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ABS%20ESD.bbsflmt) |
| eSUN ABS FR | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ABS%20FR.bbsflmt) |
| eSUN ABS HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ABS%20HS.bbsflmt) |
| eSUN ABS-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ABS-CF.bbsflmt) |
| eSUN ABS-GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ABS-GF.bbsflmt) |
| eSUN ASA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ASA.bbsflmt) |
| eSUN ASA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ASA%20LW.bbsflmt) |
| eSUN PA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PA.bbsflmt) |
| eSUN PA-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PA-CF.bbsflmt) |
| eSUN PA12-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PA12-CF.bbsflmt) |
| eSUN PA6-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PA6-CF.bbsflmt) |
| eSUN PC ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PC%20ESD.bbsflmt) |
| eSUN PC HT | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PC%20HT.bbsflmt) |
| eSUN PEBA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2D (51)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| eSUN ABS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ABS.bbsflmt) |
| eSUN ABS ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ABS%20ESD.bbsflmt) |
| eSUN ABS FR | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ABS%20FR.bbsflmt) |
| eSUN ABS HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ABS%20HS.bbsflmt) |
| eSUN ABS-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ABS-CF.bbsflmt) |
| eSUN ABS-GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ABS-GF.bbsflmt) |
| eSUN ASA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ASA.bbsflmt) |
| eSUN ASA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ASA%20LW.bbsflmt) |
| eSUN PA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PA.bbsflmt) |
| eSUN PA-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PA-CF.bbsflmt) |
| eSUN PA12-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PA12-CF.bbsflmt) |
| eSUN PA6-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PA6-CF.bbsflmt) |
| eSUN PC | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PC.bbsflmt) |
| eSUN PC ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PC%20ESD.bbsflmt) |
| eSUN PEBA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2S (51)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| eSUN ABS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ABS.bbsflmt) |
| eSUN ABS ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ABS%20ESD.bbsflmt) |
| eSUN ABS FR | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ABS%20FR.bbsflmt) |
| eSUN ABS HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ABS%20HS.bbsflmt) |
| eSUN ABS-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ABS-CF.bbsflmt) |
| eSUN ABS-GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ABS-GF.bbsflmt) |
| eSUN ASA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ASA.bbsflmt) |
| eSUN ASA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ASA%20LW.bbsflmt) |
| eSUN PA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PA.bbsflmt) |
| eSUN PA-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PA-CF.bbsflmt) |
| eSUN PA12-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PA12-CF.bbsflmt) |
| eSUN PA6-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PA6-CF.bbsflmt) |
| eSUN PC ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PC%20ESD.bbsflmt) |
| eSUN PC HT | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PC%20HT.bbsflmt) |
| eSUN PEBA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab P1S (46)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| eSUN ABS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ABS.bbsflmt) |
| eSUN ABS ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ABS%20ESD.bbsflmt) |
| eSUN ABS FR | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ABS%20FR.bbsflmt) |
| eSUN ABS HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ABS%20HS.bbsflmt) |
| eSUN ABS HT | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ABS%20HT.bbsflmt) |
| eSUN ASA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ASA.bbsflmt) |
| eSUN ASA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ASA%20LW.bbsflmt) |
| eSUN PC | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PC.bbsflmt) |
| eSUN PC ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PC%20ESD.bbsflmt) |
| eSUN PEBA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab P2S (51)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| eSUN ABS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ABS.bbsflmt) |
| eSUN ABS ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ABS%20ESD.bbsflmt) |
| eSUN ABS FR | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ABS%20FR.bbsflmt) |
| eSUN ABS HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ABS%20HS.bbsflmt) |
| eSUN ABS-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ABS-CF.bbsflmt) |
| eSUN ABS-GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ABS-GF.bbsflmt) |
| eSUN ASA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ASA.bbsflmt) |
| eSUN ASA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ASA%20LW.bbsflmt) |
| eSUN PA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PA.bbsflmt) |
| eSUN PA-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PA-CF.bbsflmt) |
| eSUN PA12-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PA12-CF.bbsflmt) |
| eSUN PA6-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PA6-CF.bbsflmt) |
| eSUN PC | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PC.bbsflmt) |
| eSUN PC ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PC%20ESD.bbsflmt) |
| eSUN PEBA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab X2D (50)</strong></summary>

| 耗材 | 来源 | 下载 |
|---|---|---|
| eSUN ABS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ABS.bbsflmt) |
| eSUN ABS ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ABS%20ESD.bbsflmt) |
| eSUN ABS FR | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ABS%20FR.bbsflmt) |
| eSUN ABS HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ABS%20HS.bbsflmt) |
| eSUN ABS-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ABS-CF.bbsflmt) |
| eSUN ABS-GF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ABS-GF.bbsflmt) |
| eSUN ASA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ASA.bbsflmt) |
| eSUN ASA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ASA%20LW.bbsflmt) |
| eSUN PA-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PA-CF.bbsflmt) |
| eSUN PA12-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PA12-CF.bbsflmt) |
| eSUN PA6-CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PA6-CF.bbsflmt) |
| eSUN PC | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PC.bbsflmt) |
| eSUN PC ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PC%20ESD.bbsflmt) |
| eSUN PEBA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | 衍生 | [下载](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU%20LW.bbsflmt) |

</details>

<!-- END GENERATED PROFILE TABLES -->

完整技术清单（bundle id、Studio 版本、精确的 compatible-printer 字符串）请参见 [REFERENCES.md](REFERENCES.md)。

## 安装配置文件

1. 在 Bambu Studio 中，进入 **文件 → 导入 → 导入配置**。
2. 选择你需要的耗材/打印机对应的 `.bbsflmt` 文件。
3. 该耗材预设将出现在对应打印机的耗材下拉列表中的 `TINMORRY` 或 `eSUN` 厂商分类下（取决于你导入的文件包）。

## 文件格式

每个 `.bbsflmt` 文件都是一个 zip 压缩包（Bambu Studio 的耗材配置文件包格式），包含：

- `bundle_structure.json` — 文件包元数据：bundle id、导出时使用的 Bambu Studio 版本、耗材名称，以及厂商/配置路径映射。
- `<品牌>/<耗材名称> @<打印机> 0.4 nozzle.json` — 每个兼容打印机对应一个耗材设置配置文件，包含 Bambu Studio 的完整耗材参数（温度、冷却、流量、回抽等）。

完整的文件包清单及元数据请参见 [REFERENCES.md](REFERENCES.md)。

## 已知问题

- 少数文件名中包含从原始导出继承下来的特殊字符（例如 `profiles/BambuStudio/TINMORRY/H2D/TINMORRY PLA Matte，.bbsflmt` 中的全角逗号，以及 `` profiles/BambuStudio/TINMORRY/P2S/TINMORRY PP-CF `.bbsflmt `` 中的反引号）。这些只是外观问题，不影响导入。
