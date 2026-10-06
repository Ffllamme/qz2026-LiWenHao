import json
def analyze_log(filepath:str)->dict :
    result = {"total": 0, "by_level":{}, "by_user":{}, "last_error": None
              }
    try:
        with open(filepath,"r",encoding="utf-8") as f :
            for line in f:
                line = line.strip()#清理这一行的前后多的符号
                if not line:
                    continue
            try:
                d = json.loads(line)
                result["total"] += 1#统计条数
                level = d["level"]
                user = d["user"]
                message = d["message"]#找出并放入对应值
                if level  in result["by_level"]:
                    result["by_level"][level] += 1
                else:
                    result["by_level"][level] = 1#计数
                if user in result["by_user"]:
                    result["by_user"][user] += 1
                else:
                    result["by_user"][user] = 1
                if level == "ERROR":
                    result["last_error"] = message
            except Exception as e:
                pass
    except FileNotFoundError:
        pass# 错误直接显示空的
    return result
