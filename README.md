# zyt_auto_tools

[![PyPI Version](https://img.shields.io/pypi/v/zyt_auto_tools.svg)](https://pypi.org/project/zyt_auto_tools/)
[![License](https://img.shields.io/pypi/l/zyt_auto_tools.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/pypi/pyversions/zyt_auto_tools.svg)](https://www.python.org/downloads/)

**`zyt_auto_tools`** 是一个 Python 工具集，旨在帮助开发者自动化常见的项目任务。它包含以下工具：

1. **自动生成 `__init__.py` 文件**：根据指定目录下的指定部分文件，自动生成 `__init__.py` 文件。
2. **自动创建 Python 文件**：快速生成带有标准模板的 Python 文件。
3. **自动更新文件修改时间**：更新项目中今天修改过的 `.py` 文件的 `Update` 日期。
4. **自动生成项目结构图**：生成项目的目录结构图，支持文本和 `.gitignore` 规则。
5. **自动创建 Python 项目文件夹**：快速生成指定类型的 Python 项目架构文件夹。

> 📌 当前版本：`v0.4.1` ｜ 🆕 [查看更新日志 »](#更新日志)

---

## 安装

你可以通过 `pip` 安装这个工具集：

```bash
pip install zyt-auto-tools
```

---

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

#### ③ 你还可以通过 '**-t**' 或 '**--type**' 来选择生成的内容（public:非_开头的顶层类和函数;all:全部顶层类和函数;star:通配导入,默认public）：

```bash
auto-generate-init --type public
```
###### or
```bash
auto-generate-init --type all
```
###### or
```bash
auto-generate-init --type star
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

### 4. 自动生成项目结构图

在项目根目录下运行以下命令，生成项目的目录结构图（默认输出到控制台）：

```bash
auto-create-structure
```

#### ① 你还可以通过 '**-d**' 或 '**--dir**' 指定目标目录：

```bash
auto-create-structure --dir ./my_project
```

#### ② 你还可以通过 -o 或 --output 指定输出文件路径：

```bash
auto-create-structure --output project_structure.txt
```

#### ③ 你还可以通过 -i 或 --ignore 指定额外忽略的目录/文件（支持通配符）：

```bash
auto-create-structure --ignore *.log tests/
```

#### ④ 你还可以通过 --use-gitignore 使用 .gitignore 文件中的规则替换默认忽略列表：

```bash
auto-create-structure --use-gitignore
```

### 5. 自动创建 Python 项目文件夹

使用以下命令快速创建指定类型的 Python 项目文件夹（默认在项目根目录下，默认本作者, 默认类型为标准的python文件夹）：

```bash
auto-init-python-dir
```

#### ① 你还可以通过 '**-t**' 或 '**--type**' 指定项目类型(支持None, software, crawler, spiders)：

```bash
auto-init-python-dir --type software
```

#### ② 你还可以通过 '**-d**' 或 '**--dir**' 指定目标目录：

```bash
auto-init-python-dir --dir ./my_project
```

#### ③ 你还可以通过 '**-a**' 或 '**--author**' 指定作者：

```bash
auto-init-python-dir --author your_name
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

---

## 更新日志

### V0.4.1

### 2025-07-07

### ⚙️ 功能优化

**1. `auto-init-python-dir` 命令**  
  - ①优化生成crawler项目初始化内容:
    - 新增`plugins`文件夹（启动器扩展功能模块）,移动原`proxy_test.py`
    - 新增`utils`文件夹（通用函数与log记录函数）,移动原`utils.py`
    - 新增`settings`文件夹（配置文件夹）,移动原`lake`文件夹
    - 新增`logger.py`（日志配置）
    - 新增`start_crawler.py`（爬虫系统启动代码）
    - 优化`config.py`
    - 优化`spiders/example.py`
  - ②优化生成software项目初始化内容:
    - 优化`network/server_connect.py`函数导入顺序

**2. `auto-generate_init` 命令**  
  - ①优化导入内容生成，现在会只包含顶层的类与函数
  - ②优化type参数，新增选择是否导入以 `_` 开头的顶层类或函数
  - ③优化type参数名:
    - public:非_开头的顶层类和函数(默认参数)
    - all:全部顶层类和函数
    - star:通配导入

### 📜 完整更新日志

 **点此查看所有历史版本和详细改动说明：**  
🔗[查看完整更新日志 »](CHANGELOG.md)

---

## 贡献

欢迎贡献代码！

## 许可证

本项目基于 [MIT 许可证](LICENSE) 开源。

## 作者

- **ZhangYuetao** - 项目开发者
- 邮箱: zhang894171707@gmail.com