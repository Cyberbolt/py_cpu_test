# Python CPU 性能测试工具及榜单

该工具用于测试不同环境、不同机器中 Python 的性能表现(基于纯 Python 的冒泡排序算法)。测试环境包括 Linux、macOS、Windows，机器包括但不限于 个人电脑(PC)、Mac、树莓派、服务器。本仓库旨在构建一个全平台的 Python 性能榜单，供 Python 开发者参考，也可由此为参考选购机器。

我们需要尽可能多的测试数据，以提供更全面的榜单。欢迎大家参加该测试，成为本仓库的贡献者之一。(注：为了提升测试数据的可信度，榜单中已有机器支持重复提交测试，我们会取不同贡献者测试数据的平均值，失真数据除外)让我们共同构建一个开源、可信的 Python 性能榜单！

### 测试方法

环境要求: Python 3.6 - Python 3.10 (请使用官方 CPython 解释器，为确保测试结果的准确性，不支持 Python 3.11 及以上的版本)

1.将本仓库 fork 至你的仓库，git clone 到本地，创建并进入一个新分支。

2.在项目根目录运行 `python3 app.py` 进行测试，完成后会生成 `result` 目录。

3.(可选)在 `result` 目录中创建 `remarks.txt` 文件，填写本次测试的备注信息或注意事项。

4.更改 `result` 目录的格式

若测试机器是实体主机，请将 `result` 目录更改为 `时间-测试人-系统 Python版本-CPU型号` 格式 (如:20220406-QuintinShaw-Linux Python 3.9.2-Intel(R) Core(TM) i7-4770 CPU @ 3.40GHz) ，并将此目录移动到 `test` 目录中。

若测试机器是云服务器，请将 `result` 目录更改为 `时间-测试人-系统 Python版本-服务器名称 CPU和内存配置 机房区域` 格式(如:20220406-Cyberbolt-Linux Python 3.8.2-阿里云轻量应用型 2核1G 新加坡) ，并将此目录移动到`test`目录中。

5.通过 git 上传到自己的仓库后，提交 pull request 请求。提交的请求经审核后将合并至本仓库。

### 总揽成绩

成绩按多核降序，单核成绩与多核成绩无关。

注：若仓库存在失真数据，请在 [issues](https://github.com/Cyberbolt/py_cpu_test/issues) 发起修复请求，非常感谢你的贡献！

![Python CPU 性能榜单](https://www.cyberlight.xyz/static/picture-bed/py_cpu_test/data_0.0.18.png)

### 源码参考

仅用于学习参考，性能测试无需关注该部分。代码的算法部分请参考项目根目录 `算法部分源码参考.py` 文件，点击可下载 [数据集](https://www.cyberlight.xyz/static/picture-bed/py_cpu_test/data.txt) 。
