from time import sleep


class TrafficLight:
    __color = "Red"

    def running(self):
        self.__color = "Red"
        print(f"\033[31m{self.__color}")
        sleep(2)
        self.__color = "Yellow"
        print(f"\033[33m{self.__color}")
        sleep(1)
        self.__color = "Green"
        print(f"\033[32m{self.__color}")
        sleep(3)


traff = TrafficLight()
traff.running()

