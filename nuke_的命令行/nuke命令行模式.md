# nuke的命令行模式

## 介绍  

Script Editor /PyCharm   
编辑和调试代码等等时候需要配置和操作  
nuke Python 解释器：  
可以后台运行并整合到pipeline工具中去  （主要是希望不打开nuke，直接以命令行的方式去运行）

-----   
### 一、nukePython调试代码  
1、nuke 的Python解释器是没有办法来运行pyside2的代码的，那么我们可以测试一下如下代码：
```python
import sys

from PySide2 import QtWidgets

app = QtWidgets.Qapplication(sys.argv)

w = QtWidgets.QWidget()
w.show()
sys.exit(app.exec_())

```

如果直接在pycharm中运行的话，会直接报错，那么只能运用其他的方法了。不过nuke的nuke.exe是支持Python的，那么可以直接用nuke  
来运行这个代码，例如：  
```python
"Y:\Program Files\Nuke10.0v1\Nuke10.0.exe" -t
```
在nuke的后面跟一个-t 就跟运行Python的解释器是差不多的。如果在后面直接加上Python代码的路径，那么就可以直接运行了。 
不过这里还是会遇到问题，也会报错，提示已经存在的实例对象，所以，这里还有一个解决方法，使得代码创建的是QApplication的  
实例，把—t改成--tg即可。因为-t会创建一个QCoreApplication的实例，是QApplication的父类。可以在nuke后面加上-help查看所有的帮助。  
------
### nuke的命令行模式的基本语法  

```python
Nuke<option> [<argv>] <script> [<range>]
```

* nuke:在这里表示的是nuke的主程序路径，后面的是选项的参数
* script：是python脚本，或者是nuke的脚本路径
* range：是可选的帧数范围

在这里要注意的是选项和参数（option，argv）可以有多个   
option的选项：--nukex，--nukeassist,--studio,--nc  

这里添加不同的选项，nuke就会启动不同的版本。
这样的写法太过于繁琐，所有还有一种简化方式，我们可以在cmd窗口中设置快捷命令，然后利用这个快捷命令来启动。  
* windows：doskey nukex = 'nuke path' --nukex
* mac Os: alias nukex = 'nuke path' --nukex
* linux: alias nukex = 'nuke path' --nukex  

如果要接受参数还要注意一个问题，如下：
在windows中：doskey nukex = 'nuke path' --nukex $*
这样就把原来很长的语句缩写了，具体实现方式如：  
```python
'nuke path' --nukex <option><argv><script><range>
这样长的语句换成
nukex <option><argv><script><range>
```
注意的是这里的doskey只能在当前窗口有效。如果要永久可以使用另外一种方式。
```python
（1）在C盘的根目录下有个隐藏的autoexec.bat文件，你输入以下内容：
@echo off
doskey netx=nuke的路径 $*
doskey net=1.bat $*
（2）开始-运行-输入regedit，打开注册表，依次展开：HKEY_CURRENT_USER\Software\Microsoft\Command Processor，
在右边的窗口新建字符串值AutoRun，双击，并把值更改为c:\autoexec.bat
说明：步骤(2)意思是当你打开cmd窗口时就会自动先运行c:\autoexec.bat文件，
如果你不想用这个文件也可以自己随意建立一个.bat文件，然后在AutoRun中设置正确的路径即可。

```


## **总结**
-------