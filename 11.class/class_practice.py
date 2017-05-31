from class_sample import Shop, PCroom
from class_sample import User,Food,Something,Drink

xeno = PCroom('제노','PC방','신사역','1300')
lotteria = Shop('Lotteria','패스트푸드','서울시 강남구')
xeno.shop_info()
lotteria.shop_info(1)
# lotteria.change_type('롯데리아는 화장실만 쓴다')
# lotteria.shop_info()

# lotteria.__shop_type = 'sdfsdfsdf'
# lotteria.shop_type ='학원'
# print(lotteria.shop_type)

user = User('홍동현')
something = Something("잘모르는것")
food = Food('돼지불백')
drink =Drink("레드불")

user.eat_something(something)
user.eat_something(food)
user.eat_something(drink)

