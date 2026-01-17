import os
from src.config import BUFFER_SIZE


def copy_with_verification(src, dest):
    """复制文件并验证完整性
    
    Args:
        src: 源文件路径
        dest: 目标文件路径
        
    Raises:
        FileNotFoundError: 源文件不存在时抛出
        PermissionError: 没有读写权限时抛出
        ValueError: 文件复制不完整时抛出
    """
    # 检查源文件是否存在
    if not os.path.exists(src):
        raise FileNotFoundError(f"源文件不存在: {src}")
    
    # 执行文件复制
    with open(src, 'rb') as src_file, open(dest, 'wb') as dest_file:
        while True:
            buffer = src_file.read(BUFFER_SIZE)
            if not buffer:
                break
            dest_file.write(buffer)
    
    # 验证文件完整性
    src_size = os.path.getsize(src)
    dest_size = os.path.getsize(dest)
    
    if src_size != dest_size:
        # 清理不完整的文件
        if os.path.exists(dest):
            os.remove(dest)
        raise ValueError(f"文件复制不完整，源文件大小: {src_size} bytes，目标文件大小: {dest_size} bytes")


def get_file_hash(file_path, hash_algorithm="sha256"):
    """获取文件的哈希值，用于文件完整性验证
    
    Args:
        file_path: 文件路径
        hash_algorithm: 哈希算法，默认为sha256
        
    Returns:
        str: 文件的哈希值
    """
    import hashlib
    
    hash_obj = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as f:
        while True:
            buffer = f.read(BUFFER_SIZE)
            if not buffer:
                break
            hash_obj.update(buffer)
    
    return hash_obj.hexdigest()
