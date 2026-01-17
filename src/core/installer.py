import os
import shutil
import subprocess
import sys
import psutil
from src.config import *
from src.utils.resource import get_resource_path
from src.utils.process import force_close_pcl_processes
from src.utils.file import copy_with_verification

class PCLInstaller:
    """PCL整合包安装器类"""
    
    def __init__(self):
        """初始化安装器"""
        self.resource_path = get_resource_path(MODPACK_FILENAME)
    
    def validate_directory(self, target_dir):
        """验证目标目录的有效性
        
        Args:
            target_dir: 目标目录路径
            
        Raises:
            ValueError: 目录无效时抛出
        """
        if not os.path.isdir(target_dir):
            raise ValueError(f"无效的目录: {target_dir}")
        
        # 检查写入权限
        test_file = os.path.join(target_dir, ".test_write.txt")
        try:
            with open(test_file, "w") as f:
                f.write("test")
            os.remove(test_file)
        except PermissionError:
            raise ValueError(f"没有目标目录的写入权限: {target_dir}")
    
    def find_launcher(self, target_dir):
        """在目标目录中查找有效的启动器
        
        Args:
            target_dir: 目标目录路径
            
        Returns:
            str: 找到的启动器路径，未找到则返回None
        """
        for launcher in VALID_LAUNCHERS:
            launcher_path = os.path.join(target_dir, launcher)
            if os.path.exists(launcher_path):
                return launcher_path
        return None
    
    def install_and_run(self, target_dir):
        """执行安装并运行启动器
        
        Args:
            target_dir: 目标目录路径
            
        Returns:
            bool: 安装成功返回True，失败返回False
        """
        # 1. 验证目录
        self.validate_directory(target_dir)
        
        # 2. 强制关闭PCL进程
        force_close_pcl_processes()
        
        # 3. 复制整合包文件
        dest_file = os.path.join(target_dir, OUTPUT_MODPACK_FILENAME)
        copy_with_verification(self.resource_path, dest_file)
        
        # 4. 查找启动器
        launcher_path = self.find_launcher(target_dir)
        if not launcher_path:
            raise ValueError("未检测到有效的启动器文件，您是否选择了错误的文件夹或修改了启动器的默认名称？")
        
        # 5. 运行启动器
        subprocess.Popen([launcher_path], cwd=target_dir)
        
        return True
