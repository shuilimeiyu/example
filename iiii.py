from urllib import request
import json
import pymysql
def input(title,citd,image,Tourism_name,Tourism_city,Tourism_Number,Tourism_introduce,Tourism_Price,Tourism_by_Region_id):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "", "tuiwenbang")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句 bt,ctid,image_path,bt,'三亚市','100','三亚市'
    sql = " INSERT INTO tourism(title,citd,image,Tourism_name,Tourism_city,Tourism_Number,Tourism_introduce,Tourism_Price,Tourism_by_Region_id) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}','{6}','{7}','{8}')".format(title,citd,image,Tourism_name,Tourism_city,Tourism_Number,Tourism_introduce,Tourism_Price,Tourism_by_Region_id)
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        print(title)

list3_ctid = []
with open('demo1.json', 'r',encoding="utf-8") as f:
    data = json.load(f)
    list1 = list(data)
    for list2 in list1:
        id,bt,ctid,image = list2['id'],list2['bt'],list2['ctid'],'https://www.explorehainan.com/'+list2['image']
        path = './static/image/'
        list3_ctid.append(ctid)
        image_path=path+image.split('/')[-1]
        # request.urlretrieve(image,image_path)
        if 16 <= int(ctid) and int(ctid)<=37:
            if int(list2['ctid']) == 16:
                input(bt, ctid, image_path, bt, '海口', '100', '暂时没有详细的介绍', '100元人民币不等', '173')
            if int(list2['ctid']) == 17:
                input(bt,ctid,image_path,bt,'三亚市','100','暂时没有详细的介绍','100元人民币不等','174')
            if int(list2['ctid']) == 19:
                input(bt, ctid, image_path, bt, '五指山', '100', '暂时没有详细的介绍', '100元人民币不等', '177')
            if int (list2['ctid']) ==20 :
                input(bt, ctid, image_path, bt, '琼海', '100', '暂时没有详细的介绍', '100元人民币不等', '179')
            if int (list2['ctid']) ==36 :
                input(bt, ctid, image_path, bt, '澄迈', '100', '暂时没有详细的介绍', '100元人民币不等', '184')
            if int (list2['ctid']) ==22 :
                input(bt, ctid, image_path, bt, '万宁', '100', '暂时没有详细的介绍', '100元人民币不等', '180')
            if int (list2['ctid']) ==31 :
                input(bt, ctid, image_path, bt, '儋州', '100', '暂时没有详细的介绍', '100元人民币不等', '176')
            if int (list2['ctid']) ==21 :
                input(bt, ctid, image_path, bt, '文昌', '100', '暂时没有详细的介绍', '100元人民币不等', '178')
            if int (list2['ctid']) ==19 :
                input(bt, ctid, image_path, bt, '五指山', '100', '暂时没有详细的介绍', '100元人民币不等', '177')
            if int (list2['ctid']) ==37 :
                input(bt, ctid, image_path, bt, '屯昌', '100', '暂时没有详细的介绍', '100元人民币不等', '183')
            if int (list2['ctid']) ==29 :
                input(bt, ctid, image_path, bt, '白沙', '100', '暂时没有详细的介绍', '100元人民币不等', '186')




