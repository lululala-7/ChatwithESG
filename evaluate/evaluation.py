from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
import json
from evaluate.models import ReportContent, RespondContent
from zhipuai import ZhipuAI
def evaluate_content(request):
    if request.method == 'GET':
        return render(request,'interaction.html')
    elif request.method == 'POST':
        request.params = json.loads(request.body)
        report = request.params.get('report', None)
        if report is not None:
            if len(report)>800:
                data = {"ret": 1, "msg": "超过最大字数限制"}
                return JsonResponse(data)
            dt = timezone.now()
            request_type = 'E'#请求为智能评估
            ReportContent.objects.create(report=report,request_type = request_type,input_time=dt)

            text = "请按照ESG报告的标准评估下面这段文字报告的质量，不要求给出改进建议：" + str(report)
            msg = evaluate_opt(text)

            dt = timezone.now()
            RespondContent.objects.create(responds=msg, request_type=request_type, output_time=dt)

            json_data ={
                "data":{"ret": 0},
                "msg":msg
            }
            return JsonResponse(json_data)
        else:
            data = {"ret": 1,"msg": "未提供有效输入"}
            return JsonResponse(data)

def optimize_content(request):
    if request.method == 'GET':
        return render(request,'interaction.html')
    elif request.method == 'POST':
        request.params = json.loads(request.body)
        report = request.params.get('report', None)
        if report is not None:
            if len(report)>800:
                data = {"ret": 1, "msg": "超过最大字数限制"}
                return JsonResponse(data)

            dt = timezone.now()
            request_type = 'O'#请求为智能优化
            ReportContent.objects.create(report=report,request_type = request_type,input_time=dt)

            text = "请按照ESG报告的标准给出下面这段文字报告优化方案，如果这段文字在很大程度上和ESG报告不相关，则不需要给出优化方案，并给出提示信息：" + str(report)
            msg = evaluate_opt(text)
            dt = timezone.now()
            RespondContent.objects.create(responds=msg, request_type=request_type, output_time=dt)

            json_data ={
                "data":{"ret": 0},
                "msg":msg
            }
            return JsonResponse(json_data)
        else:
            data = {"ret": 1, "msg": "超过最大字数限制"}
            return JsonResponse(data)
def evaluate_opt(text):

    client = ZhipuAI(api_key="1377e2c81f0422a87858bcfdd83a6fe8.1LEDeVsroD5arFEY")  # 有限个token
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[
            {"role": "user",
            "content": text
            },
        ],
        tools=[
            {
                "type": "web_search",
                "web_search":{
                    "enable": True,
                    "search_query":"""撰写ESG报告环境、社会及管治报告须包括：
                    陈述公司在环境、社会及管治事宜方面的管治情况；
                    阐释汇报范围及陈述订定汇报范围的过程；
                    陈述公司如何应用若干汇报原则（「重要性」、「量化」及「一致性」）；
                    就每项「不遵守就解释」条文作出汇报；
                    （主要针对强制性披露的条款）独立验证(如适用)；
                    及公司拟向投资者及其他利益相关方传达的主要信息（对未来的展望等）。
                    """
                }
            }
        ],
        stream=True,
    )

    all_responses = [chunk.choices[0].delta.content for chunk in response]
    complete_response = ''.join(all_responses)
    #print(complete_response)
    return complete_response
