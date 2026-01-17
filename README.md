# PCL整合包安装程序框架

## 项目概述

这是一个用于构建PCL（Plain Craft Launcher）整合包安装程序的框架，采用模块化设计，具备良好的可扩展性、可维护性和可测试性。

## 目录结构

```
v7/
├── src/                    # 源代码目录
│   ├── \_\_init\_\_.py         # 包初始化文件
│   ├── main.py             # 主程序入口
│   ├── core/               # 核心功能模块
│   │   └── installer.py    # 安装器核心逻辑
│   ├── config/             # 配置管理模块
│   │   └── \_\_init\_\_.py     # 配置变量定义
│   └── utils/              # 工具函数模块
│       ├── \_\_init\_\_.py     # 工具模块初始化
│       ├── file.py         # 文件操作工具
│       ├── logger.py       # 日志管理工具
│       ├── process.py      # 进程管理工具
│       └── resource.py     # 资源路径工具
├── assets/                 # 资源文件目录
│   └── modpack.mrpack      # 整合包文件
├── scripts/                # 脚本文件目录
│   └── build.bat           # Windows构建脚本
├── .github/                # GitHub配置目录
│   └── workflows/          # GitHub Actions工作流
│       └── build.yml       # 自动化构建配置
├── tests/                  # 测试目录
├── docs/                   # 文档目录
├── requirements.txt        # Python依赖列表
├── README.md               # 项目说明文档
└── .gitignore             # Git忽略文件
```

## 核心模块说明

### 1\. 主程序入口 (src/main.py)

* 使用Tkinter创建GUI界面
* 提供目录选择和安装按钮
* 调用核心安装器执行安装流程

### 2\. 安装器核心 (src/core/installer.py)

* 目录验证和权限检查
* 启动器检测
* 整合包文件复制和验证
* 启动器运行

### 3\. 配置管理 (src/config/**init**.py)

* 整合包文件名配置
* 启动器列表配置
* 日志级别配置
* 进程管理配置
* 文件操作配置

### 4\. 工具模块 (src/utils/)

* **logger.py**: 日志记录和管理
* **resource.py**: 资源路径获取，兼容PyInstaller打包
* **process.py**: PCL进程强制结束
* **file.py**: 文件复制和完整性验证

## 构建和使用

### 构建EXE文件

#### 方法1: 使用构建脚本（推荐）

1. 双击运行 `scripts/build.bat`
2. 按照提示操作
3. 构建完成后，EXE文件将生成在 `dist/` 目录下

#### 方法2: 手动构建

1. 安装依赖

```bash
   pip install -r requirements.txt
   ```

2. 执行打包命令

```bash
   pyinstaller --onefile --noconsole --add-data "assets/modpack.mrpack;assets" --name "PCL\_Installer" src/main.py
   ```

#### 方法3: GitHub Actions自动构建

1. 将代码推送至GitHub仓库
2. GitHub Actions会自动构建EXE文件
3. 构建产物将作为GitHub Release或构建工件提供下载

### 使用说明

1. **替换整合包**：将 `assets/modpack.mrpack` 替换为实际的整合包文件
2. **修改配置**：根据需要修改 `src/config/\_\_init\_\_.py` 中的配置变量
3. **构建EXE**：使用上述方法构建EXE文件
4. **运行程序**：双击生成的EXE文件，选择PCL启动器目录，点击安装按钮

## 配置自定义

### 修改整合包文件名

```python
# src/config/\_\_init\_\_.py
MODPACK\_FILENAME = "your\_modpack.mrpack"
OUTPUT\_MODPACK\_FILENAME = "your\_modpack.mrpack"
```

### 修改启动器列表

```python
# src/config/\_\_init\_\_.py
VALID\_LAUNCHERS = \["Your Launcher.exe", "Another Launcher.exe"]
```

### 修改日志级别

```python
# src/config/\_\_init\_\_.py
LOG\_LEVEL = "DEBUG"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
```

## 扩展开发

### 添加新功能模块

1. 在 `src/core/` 目录下创建新的模块文件
2. 在主程序或安装器中导入并使用

### 添加新工具函数

1. 在 `src/utils/` 目录下创建新的工具文件或扩展现有文件
2. 在需要的地方导入并使用

### 添加测试

1. 在 `tests/` 目录下创建测试文件
2. 使用pytest等测试框架编写测试用例

## 依赖管理

项目依赖已列出在 `requirements.txt` 文件中，包括：

* pyinstaller==6.17.0: 用于打包EXE文件
* psutil==7.1.3: 用于进程管理

## 许可证

本项目采用MIT许可证，可自由修改和分发。

## 最佳实践

1. **模块化设计**：将功能拆分为独立模块，提高代码复用性和可维护性
2. **配置集中管理**：所有配置变量集中在一个文件中，便于修改和维护
3. **完善的错误处理**：对可能出现的错误进行捕获和处理
4. **日志记录**：记录关键操作和错误信息，便于调试和问题排查
5. **文件完整性验证**：确保文件复制的完整性
6. **进程管理**：确保安装过程中相关进程已关闭
7. **清晰的文档**：为代码和功能提供详细的文档说明

## 故障排除

### 构建失败

* 确保已安装Python 3.14或更高版本
* 确保已安装所有依赖包
* 检查PyInstaller命令是否正确

### 运行时错误

* 检查日志文件 `installer.log` 获取详细错误信息
* 确保目标目录存在且有写入权限
* 确保整合包文件存在且完整
* 确保PCL启动器文件存在于目标目录中

## 贡献指南

1. Fork本仓库
2. 创建特性分支
3. 提交代码
4. 创建Pull Request

## 联系方式

如有问题或建议，请提交Issue或联系项目维护者。

