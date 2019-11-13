需要做的事：
1、安装node.js
http://nodejs.cn/download/ node里包含了包管理工具npm

2、npm换成国内源
'''
# 查看版本
$ npm -v
# 2.3.0
npm config set registry https://registry.npm.taobao.org
# 配置后可通过下面方式来验证是否成功
npm config get registry
'''
3、下载vue脚手架
npm install -g vue-cli
//查看版本，应该是2.9.6
vue -V

4、运行vue项目
进入frontend文件夹，打开命令行
//安装需要的包
npm install
//编译项目并打包，文件放在frontend\dist下
npm run build
//运行前端检查
npm run dev

5、安装django
pip install django

6、运行后端
回到根目录
//运行自己的python
python manage.py runserver
