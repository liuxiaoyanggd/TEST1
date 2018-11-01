'''
需求
员工A,B对象-->上班期间玩游戏
前台的菇凉-->看着老板
如果老板来了
前台-通知->员工A，B。。。

提示定义

定义观察者类 StockObserver
定义一个观察者集合用来注册监听者

定义一个通知的方法

Receptionist
A,B
定义接受到消息立马停止玩游戏
'''
class StockObserver:
    def __init__(self,notice):
        self.notice=notice
    def message(self):
        if self.notice==False:
            print('老板没来,放心玩')
            Receptionist.playgame(self)
        if self.notice==True:
            print('老板来了')
            Receptionist.work(self)
        return self.notice


class Receptionist:
    def playgame(self):
        print('A,B:么么哒,我们打团呢')
    def work(self):
        print('A,B都在兢兢业业的撸码')

jiao=StockObserver(False)
jiao.message()







