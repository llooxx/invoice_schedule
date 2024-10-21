# 发票整理程序

这是一个用 Python 编写的发票整理程序，旨在帮助用户自动识别和整理发票 PDF 文件中的内容，并生成统一命名的文件。在 macos，win10 正常运行。

## 技术栈

- **GUI 框架**：PySide6
- **PDF 内容识别**：pdfplumber
- **条形码识别**：pyzbar

## 功能

- **自动识别**：识别发票 PDF 文件中的详细信息。
- **内容整理**：将识别的内容整理成清单。
- **文件命名**：生成统一的文件命名规则。

## 使用方法

1. 确保安装了 Python 环境。
2. 安装所需的依赖库：
   ```bash
   pip install -r requriements.txt
   ```
3. 运行 main.py
   ```bash
   python main.py
   ```
