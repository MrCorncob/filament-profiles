# Cấu hình sợi in TINMORRY cho Bambu Studio

*[English](README.md) | [中文](README.zh.md)*

Được fork từ [TINMORRY/Tinmorry-Bambu_BambuStudio](https://github.com/TINMORRY/Tinmorry-Bambu_BambuStudio).

Bộ cấu hình sợi in (filament) tùy chỉnh, sắp xếp theo phần mềm cắt lớp (slicer), rồi đến hãng sợi in, rồi đến từng dòng máy in Bambu Lab. Hiện tại có bundle `.bbsflmt` của **Bambu Studio** cho sợi in **TINMORRY**, **eSUN** và **BING3D**; cấu trúc repo được thiết kế để sau này bổ sung thêm các slicer khác (ví dụ OrcaSlicer) và hãng sợi khác (ví dụ ELEGOO) mà không cần tổ chức lại lần nữa.

## ⚠️ Lưu ý — đọc trước khi tải về và sử dụng

- Các cấu hình có nhãn **Được tạo** trong bảng bên dưới **không phải là file xuất gốc từ hãng**. Chúng được tạo ra bằng cách kết hợp dữ liệu delta nhỏ theo từng máy in của hãng với thông số máy in lấy từ một bundle khác (xem `CLAUDE.md` / `REFERENCES.md`), và **chưa được TINMORRY, eSUN hay BING3D in thử kiểm chứng**.
- Trước khi in với bất kỳ cấu hình **Được tạo** nào, hãy đối chiếu lại nhiệt độ đầu phun (nozzle), bàn in (bed/plate) và buồng in (chamber) với thông tin thực tế trên nhãn cuộn sợi hoặc datasheet của nhà sản xuất — **đặc biệt là PA-CF và PAHT-CF trên X2D**, vì hai cấu hình này đang dùng tạm khoảng nhiệt độ của PETG CF thay vì khoảng nhiệt độ riêng của chúng (thường thấp hơn đáng kể so với mức PA-CF/PAHT-CF thực sự cần).
- **Hầu hết cấu hình eSUN trên H2D, H2S, P2S và X2D chỉ có dữ liệu thật của eSUN cho biến thể đầu đùn "Direct Drive Standard".** Dữ liệu xuất theo từng máy in của eSUN gần như luôn để trống nhiệt độ đầu phun, tỷ lệ đùn (flow ratio) và tốc độ thể tích tối đa cho ba biến thể còn lại ("Direct Drive High Flow"/"Bowden Standard"/"Bowden High Flow"), nên ba biến thể đó âm thầm kế thừa giá trị từ bundle TINMORRY dùng làm mẫu thay vì giá trị riêng của eSUN — hãy đối chiếu với datasheet chính thức của eSUN trước khi in cấu hình eSUN trên bất kỳ cấu hình nào khác ngoài Direct Drive Standard của bốn máy in này.
- **Các cấu hình BING3D PETG LS được xây dựng từ nhãn cuộn sợi, không phải từ datasheet.** BING3D không phát hành file xuất Bambu Studio cũng như datasheet sản phẩm, nên chỉ những nhiệt độ in trên nhãn cuộn (đầu phun 205–225 °C, bàn in 0–50 °C) là dữ liệu riêng của BING3D — tỷ lệ đùn, tốc độ thể tích tối đa, làm mát và rút sợi đều mượn từ một bundle PETG của TINMORRY. Lưu ý đây là loại PETG *nhiệt độ thấp*: 215 °C đầu phun và 50 °C bàn in thấp hơn nhiều so với cấu hình PETG thông thường, và dùng cấu hình PETG chung cho loại sợi này sẽ làm nó quá nhiệt. Hãy chạy hiệu chỉnh (calibration) lưu lượng/nhiệt độ trước khi in một sản phẩm dài.
- Dùng đầu phun (nozzle) chống mài mòn (hardened) cho bất kỳ loại sợi có pha sợi carbon (CF) hoặc sợi thủy tinh (GF) nào (PETG-CF, PLA-CF, PET-CF, PC GF, TPU GF, PA-CF, PAHT-CF, PP-CF, PA6-CF, PA12-CF, ABS-CF, ABS-GF).
- Nên in thử một mẫu nhỏ và theo dõi các lớp in đầu tiên trước khi in một sản phẩm hoàn chỉnh, đặc biệt với các máy in không có buồng bao kín (A1, A1 mini, A2L).
- **Cấu hình PC GF của A1 là một trường hợp đặc biệt cần lưu ý**: bản thân Bambu Studio có cung cấp sẵn cấu hình hệ thống cho PC-GF trên máy A1 (loại máy khung hở, không có buồng bao kín), nên cấu hình này được đưa vào đây dựa trên bằng chứng trực tiếp đó — nhưng điều này không có nghĩa là ABS/ASA cũng an toàn trên A1, và repo này cố tình không tạo cấu hình ABS/ASA cho A1. Nếu in PC GF trên A1 (khung hở), hãy đảm bảo thông gió tốt và lường trước khả năng cong vênh nhiều hơn so với máy có buồng bao kín.
- Các cấu hình này được cung cấp "nguyên trạng" (as-is), không có bảo hành. Bạn tự chịu trách nhiệm kiểm tra xem một cấu hình có an toàn cho máy in và loại sợi của mình trước khi sử dụng hay không.

## Cấu trúc thư mục

Dữ liệu cấu hình sợi in nằm trong `profiles/`, còn bộ công cụ tạo ra chúng nằm trong `src/`. Bên trong `profiles/`, mỗi thư mục cấp cao nhất là một slicer/định dạng xuất; bên trong đó là thư mục hãng sợi in; bên trong đó là các thư mục con tương ứng với từng dòng máy in (theo đúng giá trị trong trường `compatible_printers` của từng cấu hình). Riêng `X2D` có thêm thư mục con `0.4mm` cho đầu phun 0.4mm. `BambuStudio/TINMORRY/`, `BambuStudio/eSUN/` và `BambuStudio/BING3D/` hiện đã có cấu hình — các thư mục slicer khác (OrcaSlicer) và hãng khác (ELEGOO) sẽ xuất hiện theo cùng cách khi có dữ liệu.

```
profiles/
  BambuStudio/
    TINMORRY/
      A1/       Bambu Lab A1, đầu phun 0.4mm
      A1mini/   Bambu Lab A1 mini, đầu phun 0.4mm
      A2L/      Bambu Lab A2L, đầu phun 0.4mm
      H2C/      Bambu Lab H2C, đầu phun 0.4mm
      H2D/      Bambu Lab H2D, đầu phun 0.4mm
      H2S/      Bambu Lab H2S, đầu phun 0.4mm
      P1S/      Bambu Lab P1S, đầu phun 0.4mm
      P2S/      Bambu Lab P2S, đầu phun 0.4mm
      X2D/0.4mm/  Bambu Lab X2D, đầu phun 0.4mm
    eSUN/
      A1/, A1mini/, H2C/, H2D/, H2S/, P1S/, P2S/, X2D/0.4mm/  cấu trúc giống TINMORRY/
    BING3D/
      A1/0.4mm/, A1mini/0.4mm/, A2L/, H2C/, H2D/, H2S/, P1S/, P2S/, X2D/0.4mm/  mỗi máy một bundle PETG LS
src/       Bộ công cụ Python tạo ra các bundle mới (xem CLAUDE.md)
```

## Danh sách cấu hình hiện có

Bấm vào tên máy in bên dưới để xem danh sách sợi in tương ứng. Mỗi dòng có link **Tải xuống** dẫn thẳng đến file `.bbsflmt` — chuột phải vào link rồi chọn "Save Link As" để tải về (không cần clone repo hay vào GitHub duyệt file). Muốn tải toàn bộ máy in của một hãng cùng lúc? Trang [Releases](https://github.com/MrCorncob/filament-profiles/releases) có sẵn file zip đóng gói theo từng hãng (ví dụ `BambuStudio-TINMORRY.zip`), bên trong đã sắp xếp theo thư mục máy in/đầu phun.

- **Nguyên bản** = file xuất thật, chưa chỉnh sửa, trực tiếp từ hãng (TINMORRY hoặc eSUN).
- **Được tạo** = không phải file xuất trực tiếp từ hãng; được tạo ra từ dữ liệu delta nhỏ theo từng máy in của hãng bằng các script trong repo này (xem `CLAUDE.md`) — riêng BING3D thì tạo từ nhãn cuộn sợi. Hãy đọc mục **⚠️ Lưu ý** ở trên trước khi dùng cấu hình loại "Được tạo", đặc biệt là PA-CF/PAHT-CF trên X2D, bất kỳ cấu hình eSUN nào trên biến thể Bowden hoặc High-Flow của H2D/H2S/P2S/X2D, và mọi cấu hình BING3D.

Một số loại sợi TINMORRY (PETG GF, PETG Marble, PETG Metallic, TPU 95A) dùng chung một bundle duy nhất trong `profiles/BambuStudio/TINMORRY/X2D/0.4mm/`, chứa cấu hình cho cả máy P2S lẫn X2D.

<!-- BEGIN GENERATED PROFILE TABLES -->

### BambuStudio

#### TINMORRY

<details>
<summary><strong>Bambu Lab A1 (22)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20TPU.bbsflmt) |
| TINMORRY TPU 95a | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20TPU%2095a.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.4mm/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab A1 (0.2mm nozzle) (11)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.2mm/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.2mm/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.2mm/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.2mm/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.2mm/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.2mm/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.2mm/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.2mm/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.2mm/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.2mm/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1/0.2mm/TINMORRY%20PLA%20Silk.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab A1 mini (20)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU 95A | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.4mm/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab A1 mini (0.2mm nozzle) (11)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.2mm/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.2mm/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.2mm/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.2mm/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.2mm/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.2mm/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.2mm/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.2mm/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.2mm/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.2mm/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A1mini/0.2mm/TINMORRY%20PLA%20Silk.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab A2L (20)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Rapid | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PLA%20Rapid.bbsflmt) |
| TINMORRY PLA Silk | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU 95A | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/A2L/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2C (25)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY ABS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20ABS.bbsflmt) |
| TINMORRY ASA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20ASA.bbsflmt) |
| TINMORRY ASA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Rapid | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PLA%20Rapid.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20TPU.bbsflmt) |
| TINMORRY TPU 95a | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20TPU%2095a.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2C/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2D (23)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY ABS pro | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20ABS%20pro.bbsflmt) |
| TINMORRY ASA CF | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte， | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PLA%20Matte%EF%BC%8C.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20TPU.bbsflmt) |
| TINMORRY TPU 95a | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20TPU%2095a.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2D/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2S (22)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY ABS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20ABS.bbsflmt) |
| TINMORRY ABS Pro | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20ABS%20Pro.bbsflmt) |
| TINMORRY ASA CF | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Rapid | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PLA%20Rapid.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU 95A | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/H2S/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab P1S (26)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY ABS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20ABS.bbsflmt) |
| TINMORRY ABS Pro | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20ABS%20Pro.bbsflmt) |
| TINMORRY ASA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20ASA.bbsflmt) |
| TINMORRY ASA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF PP | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20CF%20PP.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20TPU.bbsflmt) |
| TINMORRY TPU 95a | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20TPU%2095a.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P1S/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab P2S (24)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY ABS Pro | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20ABS%20Pro.bbsflmt) |
| TINMORRY ASA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20ASA.bbsflmt) |
| TINMORRY ASA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PET CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PET%20CF%20GF.bbsflmt) |
| TINMORRY PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG CF GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20CF%20GF.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PLA.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PLA%20Matte.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY PP-CF ` | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20PP-CF%20%60.bbsflmt) |
| TINMORRY TPU 95A | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/P2S/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab X2D (22)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY ABS Pro | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20ABS%20Pro.bbsflmt) |
| TINMORRY ASA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20ASA%20CF.bbsflmt) |
| TINMORRY ASA basic | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20ASA%20basic.bbsflmt) |
| TINMORRY PA-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PA-CF.bbsflmt) |
| TINMORRY PAHT-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PAHT-CF.bbsflmt) |
| TINMORRY PC GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PC%20GF.bbsflmt) |
| TINMORRY PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PET%20CF.bbsflmt) |
| TINMORRY PETG CF | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20CF.bbsflmt) |
| TINMORRY PETG ECO | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG GF | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20GF.bbsflmt) |
| TINMORRY PETG Galaxy | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PLA%20CF.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY PLA matte | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20PLA%20matte.bbsflmt) |
| TINMORRY TPU 95A | Nguyên bản | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20TPU%2095A.bbsflmt) |
| TINMORRY TPU GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.4mm/TINMORRY%20TPU%20GF.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab X2D (0.2mm nozzle) (12)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| TINMORRY ABS Pro | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.2mm/TINMORRY%20ABS%20Pro.bbsflmt) |
| TINMORRY ASA basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.2mm/TINMORRY%20ASA%20basic.bbsflmt) |
| TINMORRY PETG ECO | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.2mm/TINMORRY%20PETG%20ECO.bbsflmt) |
| TINMORRY PETG Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.2mm/TINMORRY%20PETG%20Galaxy.bbsflmt) |
| TINMORRY PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.2mm/TINMORRY%20PETG%20HS.bbsflmt) |
| TINMORRY PETG Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.2mm/TINMORRY%20PETG%20Marble.bbsflmt) |
| TINMORRY PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.2mm/TINMORRY%20PETG%20Matte.bbsflmt) |
| TINMORRY PETG Metallic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.2mm/TINMORRY%20PETG%20Metallic.bbsflmt) |
| TINMORRY PETG Sparkly | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.2mm/TINMORRY%20PETG%20Sparkly.bbsflmt) |
| TINMORRY PLA Galaxy | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.2mm/TINMORRY%20PLA%20Galaxy.bbsflmt) |
| TINMORRY PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.2mm/TINMORRY%20PLA%20Silk.bbsflmt) |
| TINMORRY PLA matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/TINMORRY/X2D/0.2mm/TINMORRY%20PLA%20matte.bbsflmt) |

</details>

#### eSUN

<details>
<summary><strong>Bambu Lab A2L (37)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| eSUN PEBA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/A2L/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2C (51)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| eSUN ABS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ABS.bbsflmt) |
| eSUN ABS ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ABS%20ESD.bbsflmt) |
| eSUN ABS FR | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ABS%20FR.bbsflmt) |
| eSUN ABS HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ABS%20HS.bbsflmt) |
| eSUN ABS-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ABS-CF.bbsflmt) |
| eSUN ABS-GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ABS-GF.bbsflmt) |
| eSUN ASA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ASA.bbsflmt) |
| eSUN ASA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20ASA%20LW.bbsflmt) |
| eSUN PA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PA.bbsflmt) |
| eSUN PA-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PA-CF.bbsflmt) |
| eSUN PA12-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PA12-CF.bbsflmt) |
| eSUN PA6-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PA6-CF.bbsflmt) |
| eSUN PC ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PC%20ESD.bbsflmt) |
| eSUN PC HT | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PC%20HT.bbsflmt) |
| eSUN PEBA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2C/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2D (51)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| eSUN ABS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ABS.bbsflmt) |
| eSUN ABS ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ABS%20ESD.bbsflmt) |
| eSUN ABS FR | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ABS%20FR.bbsflmt) |
| eSUN ABS HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ABS%20HS.bbsflmt) |
| eSUN ABS-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ABS-CF.bbsflmt) |
| eSUN ABS-GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ABS-GF.bbsflmt) |
| eSUN ASA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ASA.bbsflmt) |
| eSUN ASA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20ASA%20LW.bbsflmt) |
| eSUN PA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PA.bbsflmt) |
| eSUN PA-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PA-CF.bbsflmt) |
| eSUN PA12-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PA12-CF.bbsflmt) |
| eSUN PA6-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PA6-CF.bbsflmt) |
| eSUN PC | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PC.bbsflmt) |
| eSUN PC ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PC%20ESD.bbsflmt) |
| eSUN PEBA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2D/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2S (51)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| eSUN ABS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ABS.bbsflmt) |
| eSUN ABS ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ABS%20ESD.bbsflmt) |
| eSUN ABS FR | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ABS%20FR.bbsflmt) |
| eSUN ABS HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ABS%20HS.bbsflmt) |
| eSUN ABS-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ABS-CF.bbsflmt) |
| eSUN ABS-GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ABS-GF.bbsflmt) |
| eSUN ASA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ASA.bbsflmt) |
| eSUN ASA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20ASA%20LW.bbsflmt) |
| eSUN PA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PA.bbsflmt) |
| eSUN PA-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PA-CF.bbsflmt) |
| eSUN PA12-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PA12-CF.bbsflmt) |
| eSUN PA6-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PA6-CF.bbsflmt) |
| eSUN PC ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PC%20ESD.bbsflmt) |
| eSUN PC HT | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PC%20HT.bbsflmt) |
| eSUN PEBA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/H2S/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab P1S (46)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| eSUN ABS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ABS.bbsflmt) |
| eSUN ABS ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ABS%20ESD.bbsflmt) |
| eSUN ABS FR | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ABS%20FR.bbsflmt) |
| eSUN ABS HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ABS%20HS.bbsflmt) |
| eSUN ABS HT | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ABS%20HT.bbsflmt) |
| eSUN ASA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ASA.bbsflmt) |
| eSUN ASA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20ASA%20LW.bbsflmt) |
| eSUN PC | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PC.bbsflmt) |
| eSUN PC ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PC%20ESD.bbsflmt) |
| eSUN PEBA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P1S/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab P2S (51)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| eSUN ABS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ABS.bbsflmt) |
| eSUN ABS ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ABS%20ESD.bbsflmt) |
| eSUN ABS FR | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ABS%20FR.bbsflmt) |
| eSUN ABS HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ABS%20HS.bbsflmt) |
| eSUN ABS-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ABS-CF.bbsflmt) |
| eSUN ABS-GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ABS-GF.bbsflmt) |
| eSUN ASA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ASA.bbsflmt) |
| eSUN ASA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20ASA%20LW.bbsflmt) |
| eSUN PA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PA.bbsflmt) |
| eSUN PA-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PA-CF.bbsflmt) |
| eSUN PA12-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PA12-CF.bbsflmt) |
| eSUN PA6-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PA6-CF.bbsflmt) |
| eSUN PC | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PC.bbsflmt) |
| eSUN PC ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PC%20ESD.bbsflmt) |
| eSUN PEBA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/P2S/eSUN%20TPU%20LW.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab X2D (50)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| eSUN ABS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ABS.bbsflmt) |
| eSUN ABS ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ABS%20ESD.bbsflmt) |
| eSUN ABS FR | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ABS%20FR.bbsflmt) |
| eSUN ABS HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ABS%20HS.bbsflmt) |
| eSUN ABS-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ABS-CF.bbsflmt) |
| eSUN ABS-GF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ABS-GF.bbsflmt) |
| eSUN ASA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ASA.bbsflmt) |
| eSUN ASA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20ASA%20LW.bbsflmt) |
| eSUN PA-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PA-CF.bbsflmt) |
| eSUN PA12-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PA12-CF.bbsflmt) |
| eSUN PA6-CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PA6-CF.bbsflmt) |
| eSUN PC | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PC.bbsflmt) |
| eSUN PC ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PC%20ESD.bbsflmt) |
| eSUN PEBA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PEBA.bbsflmt) |
| eSUN PEBA 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PEBA%2085A.bbsflmt) |
| eSUN PEBA 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PEBA%2090A.bbsflmt) |
| eSUN PEBA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PEBA%20LW.bbsflmt) |
| eSUN PET CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PET%20CF.bbsflmt) |
| eSUN PETG | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG.bbsflmt) |
| eSUN PETG Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG%20Basic.bbsflmt) |
| eSUN PETG CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG%20CF.bbsflmt) |
| eSUN PETG ESD | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG%20ESD.bbsflmt) |
| eSUN PETG HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG%20HS.bbsflmt) |
| eSUN PETG Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG%20Luminous.bbsflmt) |
| eSUN PETG Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PETG%20Matte.bbsflmt) |
| eSUN PLA | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA.bbsflmt) |
| eSUN PLA Basic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Basic.bbsflmt) |
| eSUN PLA CF | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20CF.bbsflmt) |
| eSUN PLA Clear | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Clear.bbsflmt) |
| eSUN PLA HS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20HS.bbsflmt) |
| eSUN PLA LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20LW.bbsflmt) |
| eSUN PLA Lite | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Lite.bbsflmt) |
| eSUN PLA Luminous | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Luminous.bbsflmt) |
| eSUN PLA Magic | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Magic.bbsflmt) |
| eSUN PLA Marble | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Marble.bbsflmt) |
| eSUN PLA Matte | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Matte.bbsflmt) |
| eSUN PLA Metal | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Metal.bbsflmt) |
| eSUN PLA Rock UV | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Rock%20UV.bbsflmt) |
| eSUN PLA ST | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20ST.bbsflmt) |
| eSUN PLA Silk | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Silk.bbsflmt) |
| eSUN PLA Twinkle | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Twinkle.bbsflmt) |
| eSUN PLA Wood | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20PLA%20Wood.bbsflmt) |
| eSUN TPE 83A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPE%2083A.bbsflmt) |
| eSUN TPU | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU.bbsflmt) |
| eSUN TPU 64D | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU%2064D.bbsflmt) |
| eSUN TPU 80A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU%2080A.bbsflmt) |
| eSUN TPU 85A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU%2085A.bbsflmt) |
| eSUN TPU 90A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU%2090A.bbsflmt) |
| eSUN TPU 95A | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU%2095A.bbsflmt) |
| eSUN TPU LW | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/eSUN/X2D/0.4mm/eSUN%20TPU%20LW.bbsflmt) |

</details>

#### BING3D

<details>
<summary><strong>Bambu Lab A1 (1)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| BING3D PETG LS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/BING3D/A1/0.4mm/BING3D%20PETG%20LS.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab A1 mini (1)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| BING3D PETG LS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/BING3D/A1mini/0.4mm/BING3D%20PETG%20LS.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab A2L (1)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| BING3D PETG LS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/BING3D/A2L/BING3D%20PETG%20LS.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2C (1)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| BING3D PETG LS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/BING3D/H2C/BING3D%20PETG%20LS.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2D (1)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| BING3D PETG LS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/BING3D/H2D/BING3D%20PETG%20LS.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab H2S (1)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| BING3D PETG LS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/BING3D/H2S/BING3D%20PETG%20LS.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab P1S (1)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| BING3D PETG LS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/BING3D/P1S/BING3D%20PETG%20LS.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab P2S (1)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| BING3D PETG LS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/BING3D/P2S/BING3D%20PETG%20LS.bbsflmt) |

</details>

<details>
<summary><strong>Bambu Lab X2D (1)</strong></summary>

| Sợi in | Nguồn gốc | Tải xuống |
|---|---|---|
| BING3D PETG LS | Được tạo | [tải về](https://raw.githubusercontent.com/MrCorncob/filament-profiles/main/profiles/BambuStudio/BING3D/X2D/0.4mm/BING3D%20PETG%20LS.bbsflmt) |

</details>

<!-- END GENERATED PROFILE TABLES -->

Xem [REFERENCES.md](REFERENCES.md) để biết đầy đủ thông tin kỹ thuật (bundle id, phiên bản Studio, chuỗi compatible-printer chính xác).

## Cách cài đặt một cấu hình

1. Trong Bambu Studio, vào **File → Import → Import Configs**.
2. Chọn file `.bbsflmt` tương ứng với loại sợi/máy in bạn cần.
3. Cấu hình sợi sẽ xuất hiện trong danh sách filament của đúng máy in đó, dưới mục vendor `TINMORRY`, `eSUN` hoặc `BING3D` (tùy bundle bạn đã nhập).

## Định dạng file

Mỗi file `.bbsflmt` là một file nén zip (định dạng bundle cấu hình filament của Bambu Studio) chứa:

- `bundle_structure.json` — thông tin metadata của bundle: bundle id, phiên bản Bambu Studio khi xuất file, tên filament, và bảng ánh xạ vendor/đường dẫn cấu hình.
- `<Hãng>/<tên filament> @<máy in> 0.4 nozzle.json` — một file cấu hình filament cho mỗi máy in tương thích, gồm đầy đủ các thông số của Bambu Studio (nhiệt độ, làm mát, lưu lượng, rút sợi, v.v.).

Xem [REFERENCES.md](REFERENCES.md) để biết danh sách đầy đủ các bundle và metadata của chúng.

## Một số điểm cần lưu ý

- Một vài tên file có ký tự lạ còn sót lại từ lần xuất gốc (ví dụ dấu phẩy toàn chiều rộng trong `profiles/BambuStudio/TINMORRY/H2D/TINMORRY PLA Matte，.bbsflmt`, hoặc dấu backtick trong `` profiles/BambuStudio/TINMORRY/P2S/TINMORRY PP-CF `.bbsflmt ``). Đây chỉ là vấn đề thẩm mỹ, không ảnh hưởng đến việc import.
