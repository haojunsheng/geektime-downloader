import json
import os

import requests

# 所有的课程
result = [];
# 所有的课程id
result_id=[];
# 本地已经有的课程
local_names = [];

def send_post_request(prev):
    # 请求的 URL
    url = 'https://time.geekbang.org/serv/v4/pvip/product_list'
    # 请求头，根据实际情况可调整
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https: // time.geekbang.org',
        'Referer': 'https://time.geekbang.org/resource',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'X-GEEK-REQ-ID': '210d1de966364032a2671506983a8ca6@1@web',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'Cookie':'LF_ID=2863039-63fd611-a99f338-eb1bab6; mantis5539=63a37da14b774d4fac06efbcbda82a8e@5539; MEIQIA_TRACK_ID=2dBGoILPNVzGZp6SfcS5mVupR6p; MEIQIA_VISIT_ID=2dBGoIOu39j2WnbkQCMMQU0dzZM; _ga=GA1.2.1780887489.1705816964; _tea_utm_cache_20000743={%22utm_source%22:%22geektime_search%22%2C%22utm_medium%22:%22geektime_search%22%2C%22utm_campaign%22:%22geektime_search%22%2C%22utm_term%22:%22geektime_search%22%2C%22utm_content%22:%22geektime_search%22}; gksskpitn=2b0e7aba-e02e-4845-9e37-33e56855c1a4; Hm_lvt_59c4ff31a9ee6263811b23eb921a5083=1736779403; HMACCOUNT=9D71B7919C7EAA4A; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1736779403; GCID=1046e15-314a477-4e2b98a-e8b1359; GRID=1046e15-314a477-4e2b98a-e8b1359; _gid=GA1.2.1095005062.1737171399; _ga_JW698SFNND=GS1.2.1737171404.20.1.1737171405.0.0.0; gk_process_ev={%22count%22:2%2C%22utime%22:1737171405981%2C%22referrer%22:%22https://time.geekbang.org/%22%2C%22target%22:%22page_geektime_login%22%2C%22referrerTarget%22:%22page_geektime_login%22}; GCESS=BgME_iGLZwIE_iGLZwUEAAAAAAYEonV2sggBAwQEAI0nAAwBAQoEAAAAAAsCBgANAQEHBELq4CQJAQEBCJP1HgAAAAAA; ERID=1626054-120f9db-1f7ac37-c32f546; _ga_WK6J6CS6FN=GS1.2.1737205388.3.0.1737205388.60.0.0; _gcl_au=1.1.261547143.1737205389; tfstk=geNo_g9pYmt_GqCGNnG5CzbKSKBxPbGICkdKvXnF3mofRvPRPBj3xkDL2yl-LHmqavw-v0nntyZGkGCO6zaSOfSOX1U_yuHZOD5KTth4-1HiuGCO6zJzkUkfX7EDIWiZ8XurYXkVo20eUXJyaZmq-V9e4krUuZ0S838yaX70umgETDrETZcqKVTq2kr7giqFX3pZjmPmrYmarOOetSAtEczrmBW3i4fEbzoDTBoyAGdY8kSH9fy_mWDaM6AjwP2qg2VC7pmnI8r-lkfMa0P0z7o8aid-47a4BWENDLnzI24TKl7pFqH3iu23oiJokrE7sbPGqQ3xGmk3QzSvnq24ySDY_GAnF-r7CvVdD1G8BPFIQ75kfmHs-oDTEGAubgz93dz-aBgVJSJBdYujochYzZ4iDcmBWZbDQRMrl45OoZvQnYujocQcod-mUqgP6; _ga_MTX5SQH9CV=GS1.2.1737205910.5.1.1737206131.0.0.0; Hm_lpvt_59c4ff31a9ee6263811b23eb921a5083=1737209506; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1737209506; _ga_03JGDGP9Y3=GS1.2.1737209024.50.1.1737209505.0.0.0; __tea_cache_tokens_20000743={%22web_id%22:%227459410736251535626%22%2C%22user_unique_id%22:%222028947%22%2C%22timestamp%22:1737209506031%2C%22_type_%22:%22default%22}; SERVERID=3431a294a18c59fc8f5805662e2bd51e|1737209509|1737200444'
    }
    print('prev:'+str(prev))
    # 请求体，根据你提供的内容设置
    data = {
        "tag_ids": [],
        "product_type": 1,
        "product_form": 1,
        "pvip": 0,
        "prev": prev,
        "size": 20,
        "sort": 8,
        "with_articles": False
    }
    # 发送 POST 请求
    response = requests.post(url, json=data, headers=headers)
    # 打印响应状态码
    # print("Response Status Code:", response.status_code)
    # 打印响应内容
    res=json.loads(response.content.decode('utf-8'));
    parse_products(res.get('data').get('products'));
    # print(json.dumps(res.get('data').get('products')))
    # my_list.extend(res.get('data').get('products'));
    # print(res.get('data').get('page').get('more'));
    return res.get('data').get('page').get('more');

def parse_products(data):
    for product in data:
        # 提取每个产品的 id 和 title 字段
        product_info = {
            "id": product.get("id"),
            "title": product.get("title").replace(" ", ""),
            "is_finish": product.get("column").get('is_finish'),
            "update_frequency": product.get("column").get('update_frequency')
        }
        if product.get("id") not in result_id:
            result_id.append(product.get("id"));
            result.append(product_info);

def find_uncompled_products_from_file(file_path):
    uncomple_result = []
    try:
        # 打开文件并读取数据
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for product in data:
                # 提取每个产品的 id 和 title 字段
                if product.get("is_finish") == False:
                    uncomple_result.append(product.get("title"));
            print('未完成的：'+uncomple_result);
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到，请检查文件路径是否正确。")
    except json.JSONDecodeError as e:
        print(f"文件 {file_path} 中的数据不是有效的 JSON 格式: {e}")
    except UnicodeDecodeError as e:
        print(f"文件 {file_path} 读取时发生 Unicode 解码错误: {e}")
    return json.dumps(result, ensure_ascii=False)

def find_undownload_products_from_file(file_path):
    try:
        # 打开文件并读取数据
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for product in data:
                # 提取每个产品的 id 和 title 字段
                if product.get("is_finish") == True and product.get("title") not in local_names:
                    print('未下载的课程：' + str(product))
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到，请检查文件路径是否正确。")
    except json.JSONDecodeError as e:
        print(f"文件 {file_path} 中的数据不是有效的 JSON 格式: {e}")
    except UnicodeDecodeError as e:
        print(f"文件 {file_path} 读取时发生 Unicode 解码错误: {e}")
    return json.dumps(result, ensure_ascii=False)

def get_all_folder_names(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for dir_name in dirs:
            local_names.append(dir_name);

if __name__ == '__main__':
    # 查询接口获取已购买的课程
    # boolean_true = True;
    # prev=0;
    # while boolean_true:
    #     boolean_true=send_post_request(prev);
    #     prev=prev+1;
    # print(json.dumps(result,ensure_ascii=False));
    # 未完成的课程
    # find_uncompled_products_from_file('Test.json')
    # 本地的课程
    get_all_folder_names("/Users/haojunsheng/learning/github/geektime");
    print(local_names)
    # 未下载的课程和 id
    find_undownload_products_from_file('Test.json')