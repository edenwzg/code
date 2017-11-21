# Git
- git@github.com:edenwzg/PythonHardWay.git
- git config --global user.email "you@example.com"
- git config --global user.name "Your Name"
- ssh-keygen -t rsa -C "youremail@example.com"
- git clone https://github.com/vnpy/vnpy.git
- git stage -A  // 提交所有变化
- git stage -u  // 提交被修改(modified)和被删除(deleted)文件，不包括新文件(new)
- git stage .   // 提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件
- git status
- git commit -m "Describe Text"
- checkout 此命令是最常用的命令之一，同时也是一个很危险的命令，因为这条命令会重写工作区。
    git checkout //这条命令把 当前目录所有修改的文件 从HEAD中签出并且把它恢复成未修改时的样子。注意：在使用 git checkout 时，如果其对应的文件被修改过，那么该修改会被覆盖掉。
