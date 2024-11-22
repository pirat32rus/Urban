class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    
    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        
    def get_model(self) -> str:
        return f"Модель: {self.__model}"
        
    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"
        
    def get_color(self) -> str:
        return f"Цвет: {self.__color}"
        
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")
       
    def set_color(self, new_color: str):
        if new_color.lower() in (color.lower()
            for color in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")
                
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    
    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        super().__init__(owner, model, color, engine_power)
        
if __name__ == "__main__":
    Vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
    
    Vehicle1.print_info()
    
    Vehicle1.set_color('Pink')
    Vehicle1.set_color('BLACK')
    Vehicle1.owner = 'Vasyok'
    Vehicle1.print_info()