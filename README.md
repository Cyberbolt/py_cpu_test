# Python CPU 性能测试工具及榜单

该工具用于测试不同环境、不同机器中 Python 的性能表现(基于纯 Python 的冒泡排序算法)。测试环境包括 Linux、macOS、Windows，机器包括但不限于 个人电脑(PC)、Mac、树莓派、服务器。本仓库旨在构建一个全平台的 Python 性能榜单，供 Python 开发者参考，也可由此为参考选购机器。

我们需要尽可能多的测试数据，以提供更可靠的榜单。欢迎大家参加该测试，成为本仓库的贡献者之一。(注：本仓库会采纳每个 CPU 型号前 5 名测试者[时间顺序]) 请大家踊跃提交测试，让我们共同构建一个开源、可信的 Python 性能榜单！

### 测试方法

环境要求: Python 3.6+ (请使用官方 CPython 解释器)

将本仓库 fork 至你的仓库，git clone 到本地，创建并进入一个新分支。运行 python app.py 进行测试，完成后会生成 result 目录，将 result 目录更改为`时间-用户名-系统 Python版本-CPU型号`格式【如:20220406-Cyberbolt-Linux Python 3.8.12-Intel Core i7-8750H Processor】，并将此目录移动到`test`目录中。通过 git 上传到自己的仓库后，提交 pull request 请求。提交的请求经审核后将合并至本仓库。

### 总揽成绩

同一型号的 CPU 成绩取不同贡献者测试的平均值（可能会排除部分异常值）。

![alt 属性文本](https://www.cyberlight.xyz/static/picture-bed/py_cpu_test/data.png)
