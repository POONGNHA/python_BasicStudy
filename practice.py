# keyword args
def personal_info():
    inputdata = input("이름을 입력하세요 : ")
    customer_dict = { 'name' : 'chanwoo' , 'age' : 27, 'address' : "60-24"}
    if inputdata in customer_dict['name']:
        print("이름 : %s" % customer_dict['name'])
        print("나이 : %s" % customer_dict['age'])
        print("주소 : %s" % customer_dict['address'])
personal_info()