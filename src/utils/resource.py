import os
import sys


def get_resource_path(relative_path):
    """获取资源文件的绝对路径，兼容PyInstaller打包
    
    Args:
        relative_path: 资源文件的相对路径
        
    Returns:
        str: 资源文件的绝对路径
    """
    try:
        # PyInstaller打包后的临时目录
        base_path = sys._MEIPASS
    except Exception:
        # 正常运行时的目录
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
