# RongMC V7 自研安装程序 By 7uoki

一个面向新手的PCL整合包快速安装工具，支持自动检测和启动PCL启动器。

## 功能特点

- 单EXE文件，无需安装Python环境
- 友好的图形界面，操作简单
- 支持选择PCL启动器目录
- 自动检测并结束PCL相关进程
- 优先检测`Plain Craft Launcher 2.exe`，如不存在则检测`PCL2_CE_Release_x64.exe`
- 自动复制整合包文件到启动器目录
- 一键启动PCL启动器
- 完善的错误处理和权限检查
- 文件传输完整性验证

## 文件结构

```
RongMC_V7_Installer/
├── src/                    # 源代码目录
│   └── pcl_installer.py    # 主程序代码
├── assets/                 # 资源文件目录
│   └── modpack.mrpack      # 整合包文件
├── scripts/                # 脚本文件目录
│   └── build.bat           # Windows构建脚本
├── .github/                # GitHub配置目录
│   └── workflows/          # GitHub Actions工作流
│       └── build.yml       # 自动化构建配置
├── requirements.txt        # Python依赖列表
├── README.md               # 项目说明文档
├── LICENSE                 # 许可证文件
└── .gitignore             # Git忽略文件
```

## 准备工作

1. **替换整合包文件**：将 `assets/modpack.mrpack` 替换为你实际的整合包文件
2. **修改配置**：如果需要修改配置，请编辑 `src/pcl_installer.py` 中的配置变量

## 构建EXE文件

### 方法1：使用自动化构建脚本（推荐）

1. 双击运行 `scripts/build.bat`
2. 按照提示操作
3. 构建完成后，EXE文件将生成在 `dist/` 目录下

### 方法2：手动构建

#### 步骤1：安装依赖

打开命令提示符（CMD），运行以下命令：

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 步骤2：执行打包命令

在项目目录下，运行以下命令：

```bash
pyinstaller --onefile --noconsole --add-data "assets/modpack.mrpack;." --name "RongMC_V7_Installer" src/pcl_installer.py
```

### 方法3：使用GitHub Actions自动构建

1. Fork本项目到你的GitHub账户
2. 推送代码到main分支
3. GitHub Actions会自动构建EXE文件
4. 构建产物将作为GitHub Release或构建工件提供下载

## 使用说明

1. **运行程序**：双击 `RongMC_V7_Installer.exe` 运行
2. **选择目录**：点击"浏览..."按钮，选择PCL启动器所在的目录
3. **安装并启动**：点击"一键安装并启动PCL"按钮
4. **完成**：程序会自动结束PCL进程，复制整合包文件，并启动PCL启动器

## 自定义修改

### 修改整合包文件名

在 `src/pcl_installer.py` 中修改：

```python
MODPACK_FILENAME = "modpack.mrpack"  # 整合包文件名
OUTPUT_MODPACK_FILENAME = "modpack.mrpack"  # 输出到目标目录的整合包文件名
```

### 修改启动器文件名

在 `src/pcl_installer.py` 中修改：

```python
VALID_LAUNCHERS = ["Plain Craft Launcher 2.exe", "PCL2_CE_Release_x64.exe"]  # 有效启动器列表
```

### 修改窗口标题

在 `src/pcl_installer.py` 中修改：

```python
root.title("RongMC V7自研安装程序 By 7uoki")
```

## 故障排除

### 问题：程序提示找不到文件

- 检查整合包文件是否存在于 `assets/` 目录中
- 检查启动器文件是否存在于目标目录中
- 检查文件名是否与配置一致

### 问题：程序提示没有写入权限

- 以管理员身份运行程序
- 选择其他有写入权限的目录

### 问题：启动器无法启动
（我们不会修改启动器文件，启动器无法启动请优先分析启动器的问题）

- 检查启动器文件是否完整
- 检查启动器文件是否与配置中的文件名匹配

### 问题：程序崩溃或报错

- 确保使用Python 3.14或更高版本构建
- 检查依赖是否正确安装
- 查看 `build/` 目录下的日志文件获取详细错误信息

## 许可证

本程序采用MIT许可证，可自由修改和分发。
