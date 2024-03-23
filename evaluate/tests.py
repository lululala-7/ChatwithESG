from django.test import TestCase
import requests,pprint

# Create your tests here.

text = """
2021年5月10日至13日，全国信
息安全标准化技术委员会（TC260，
简称全国信安标委）2021年第一次
工作组“会议周”在武汉举行，包括
百度及多家OASES智能终端安全生
态工作委员会（简称OASES）成员
在内的逾600家工作组单位参加了
会议，并展开了网络安全国家标准立
项项目及在研标准项目的推进工作。
本次“会议周”期间，百度参与了多
个议题的讨论和审议工作，覆盖AI
安全、黑产打击、App隐私合规、
智能终端安全、应用软件安全、车联
网安全、云安全、数据安全及隐私保
护等方面。其中，由百度参与编制的
12项标准项目已顺利推进到下一阶
段；由百度参与新立项申报的10项
标准中，已有8项标准制定项目通
过立项，1项标准制定申报转为研究
课题，1项标准研究课题通过立项。
同时，由百度牵头申报的标准研究
课题《信息安全技术——物联网安
全管理指南》也在本次“会议周”
期间成功通过立项。该标准研究课
题由百度牵头，联合中国电子标准
化研究院、中国移动及中电长城共
同推进，旨在针对物联网的特点，
在通用的信息安全管理体系（ISMS）
基础上，为物联网终端、边缘计算、
物联网服务端的通信和操作管理、
访问控制，系统采集、开发和维护，
提供相应的安全等级、控制措施和
评估方法。未来，这一标准研究课
题将填补国内在物联网安全管理方
面的空白。
此外，百度结合自身业务经验和实
践成果，参与全国信安标委2021年
《5G网络安全标准化白皮书》的编
撰工作，为5G网络安全标准框架和
重点标准研制、5G技术安全应用、
5G与产业融合安全的有序发展提供
了有力指导和技术支撑。
未来，百度将继续与OASES的成
员一道，以专利共享、核心开源、
标准驱动、产业共赢为理念，与全
国信安标委及工作组单位加强合作，
共同推动网络安全领域的实践创新。"""


def evaluate_test():
    payload ={
        "action": "智能分析",
        "report":{
            "report": text
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/evaluate/",json=payload)
    pprint.pprint(response.json())

def optimize_test():
    payload ={
        "action": "智能优化",
        "report":{
            "report": text
        }
    }
    response = requests.post("http://127.0.0.1:8000/report/optimize/",json=payload)
    pprint.pprint(response.json())

if __name__ == '__main__':
    #evaluate_test()
    optimize_test()

