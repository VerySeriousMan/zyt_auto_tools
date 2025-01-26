# Zyt Auto Tools

[![PyPI Version](https://img.shields.io/pypi/v/zyt_auto_tools.svg)](https://pypi.org/project/zyt_auto_tools/)
[![License](https://img.shields.io/pypi/l/zyt_auto_tools.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/pypi/pyversions/zyt_auto_tools.svg)](https://www.python.org/downloads/)

**Zyt Auto Tools** 是一个 Python 工具集，旨在帮助开发者自动化常见的项目任务。它包含以下工具：

1. **自动生成 `__init__.py` 文件**：根据指定目录下的指定部分文件，自动生成 `__init__.py` 文件。
2. **自动创建 Python 文件**：快速生成带有标准模板的 Python 文件。
3. **自动更新文件修改时间**：更新项目中今天修改过的 `.py` 文件的 `Update` 日期。

## 安装

你可以通过 `pip` 安装这个工具集：

```bash
pip install zyt_auto_tools
```

## 使用方法

### 1. 自动生成 `__init__.py` 文件

在项目根目录下运行以下命令，自动生成指定目录下的 `__init__.py` 文件（默认utils下全部文件）：

```bash
auto-generate-init
```

#### ① 你还可以通过 '**-d**' 或 '**--dir**' 指定目标目录（默认utils）：

```bash
auto-generate-init --dir ./my_project
```

#### ② 你还可以通过 '**-i**' 或 '**--include**' 指定所包含的文件名（默认选择包含以.py结尾的文件）：

```bash
# 例如选择文件名中含有xxx的文件
auto-generate-init --include *xxx*
```

#### ③ 你还可以通过 '**-t**' 或 '**--type**' 来选择生成的内容（func:全部函数;file:只包含文件,默认func）：

```bash
auto-generate-init --type file
```
###### or
```bash
auto-generate-init --type func
```

#### ④ 你还可以通过 '**-a**' 或 '**--author**' 指定作者：

```bash
auto-generate-init --author your_name
```

###### 作者名可以通过环境变量 DEFAULT_AUTHOR 设置：
```bash
# Linux
export DEFAULT_AUTHOR=your_name
```
###### or
```bash
# Windows
$env:DEFAULT_AUTHOR = "your_name"
```

### 2. 自动创建 Python 文件

使用以下命令快速创建一个带有标准模板的 Python 文件（默认在项目根目录下，默认本作者）：

```bash
auto-init-python-file my_script.py
```

#### ① 你还可以通过 '**-d**' 或 '**--dir**' 指定目标目录：

```bash
auto-init-python-file my_script.py --dir ./my_project
```

#### ② 你还可以通过 '**-a**' 或 '**--author**' 指定作者：

```bash
auto-init-python-file my_script.py --author your_name
```

###### 作者名可以通过环境变量 DEFAULT_AUTHOR 设置：
```bash
# Linux
export DEFAULT_AUTHOR=your_name
```
###### or
```bash
# Windows
$env:DEFAULT_AUTHOR = "your_name"
```

### 3. 自动更新文件修改时间

在项目根目录下运行以下命令，更新全部根目录下今天修改过的 `.py` 文件的 `Update` 日期：

```bash
auto-update-ctime
```

#### ① 你还可以通过 '**-d**' 或 '**--dir**' 指定目标目录：

```bash
auto-update-ctime --dir ./my_project
```

## 贡献

欢迎贡献代码！

## 许可证

本项目基于 [MIT 许可证](LICENSE) 开源。

## 作者

- **ZhangYuetao** - 项目开发者
- 邮箱: zhang894171707@gmail.com
- GitHub: [https://github.com/VerySeriousMan](https://github.com/VerySeriousMan)

## 致谢

感谢所有为这个项目做出贡献的人！