import tkinter as tk
from tkinter import filedialog, messagebox
from src.core.installer import PCLInstaller
from src.utils.logger import setup_logger

# 配置日志
logger = setup_logger()

class PCLInstallerApp:
    def __init__(self, root):
        self.root = root
        self.installer = PCLInstaller()
        self.setup_ui()
    
    def setup_ui(self):
        """设置GUI界面"""
        self.root.title("PCL整合包安装程序")
        self.root.geometry("450x200")
        self.root.resizable(False, False)
        
        # 标题标签
        title_label = tk.Label(self.root, text="PCL整合包安装程序", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)
        
        # 路径选择区域
        path_frame = tk.Frame(self.root)
        path_frame.pack(fill="x", padx=20, pady=10)
        
        path_label = tk.Label(path_frame, text="选择PCL启动器目录:")
        path_label.pack(anchor="w")
        
        path_input_frame = tk.Frame(path_frame)
        path_input_frame.pack(fill="x", pady=5)
        
        self.path_entry = tk.Entry(path_input_frame, width=40)
        self.path_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        browse_btn = tk.Button(path_input_frame, text="浏览...", command=self.browse_directory)
        browse_btn.pack(side="right")
        
        # 安装按钮
        install_btn = tk.Button(self.root, text="一键安装并启动PCL", command=self.install, 
                              bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), padx=20, pady=5)
        install_btn.pack(pady=20)
    
    def browse_directory(self):
        """浏览选择目录"""
        directory = filedialog.askdirectory(title="选择PCL启动器所在目录")
        if directory:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, directory)
    
    def install(self):
        """执行安装流程"""
        target_dir = self.path_entry.get().strip()
        if not target_dir:
            messagebox.showerror("错误", "请先选择PCL启动器目录")
            return
        
        try:
            result = self.installer.install_and_run(target_dir)
            if result:
                messagebox.showinfo("成功", "整合包安装完成，并已启动PCL启动器")
                self.root.destroy()
        except Exception as e:
            messagebox.showerror("安装失败", f"发生错误: {str(e)}")
            logger.error(f"安装失败: {str(e)}")

def main():
    """程序入口"""
    root = tk.Tk()
    app = PCLInstallerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()