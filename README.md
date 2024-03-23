#ChatwithESG

ChatwithESG是一个创新性的项目，由LLMs和Django打造成一个对话伙伴。它接受用户输入的ESG文字报告，并使用智谱清言提供的GLM-4 API产生回复，从而加速评估和优化ESG报告的工作。

#特性

用户友好界面，操作简单易懂。
与智谱清言的GLM-4集成，以处理用户请求。
使用数据库进行文本存储。

#注意

请将ChatwithESG\evaluate\evaluation.py下evaluate_opt函数中的api_key替换为自己的api_key

#安装

首先，克隆存储库：

https://github.com/lululala-7/ChatwithESG.git

cd ChatwithESG

安装相关包：

sudo apt-get install python3-dev python3-venv libcurl4-openssl-dev gcc libssl-dev -y

创建并激活虚拟环境：

python3 -m venv venv

. venv/bin/activate

安装所需的Python包：

pip install -r requirements.txt

在 settings.py 中配置您的数据库，然后应用迁移：

python manage.py makemigrations

python manage.py migrate

启动Django开发服务器：

python manage.py runserver

访问url：

http://127.0.0.1:8000/report/

