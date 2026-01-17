import psutil
from src.config import PROCESS_TIMEOUT


def force_close_pcl_processes():
    """强制结束所有PCL相关进程
    
    Returns:
        int: 结束的进程数量
    """
    pcl_processes = []
    
    # 遍历所有正在运行的进程
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # 获取进程名
            proc_name = proc.info['name'].lower()
            # 检查进程名是否包含PCL相关关键词
            if 'pcl' in proc_name or 'plain craft launcher' in proc_name:
                pcl_processes.append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    
    # 结束所有PCL进程
    killed_count = 0
    if pcl_processes:
        for proc in pcl_processes:
            try:
                proc.terminate()
                # 等待进程结束
                proc.wait(timeout=PROCESS_TIMEOUT)
                killed_count += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
            except psutil.TimeoutExpired:
                # 超时后强制结束
                try:
                    proc.kill()
                    proc.wait(timeout=PROCESS_TIMEOUT)
                    killed_count += 1
                except Exception:
                    continue
    
    return killed_count
