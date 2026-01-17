import logging
import os
from src.config import LOG_LEVEL, LOG_FILE


def setup_logger():
    """设置日志配置
    
    Returns:
        logging.Logger: 配置好的日志记录器
    """
    # 创建日志记录器
    logger = logging.getLogger("PCLInstaller")
    logger.setLevel(getattr(logging, LOG_LEVEL))
    
    # 清除已有的处理器
    if logger.handlers:
        logger.handlers.clear()
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, LOG_LEVEL))
    
    # 创建文件处理器
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(getattr(logging, LOG_LEVEL))
    
    # 创建日志格式化器
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    # 应用格式化器
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    # 添加处理器到记录器
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger
