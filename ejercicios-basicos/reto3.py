# -*- coding: utf-8 -*-


classCar:
    _carro = ["El carro se prendió", "El carro se apagó",
              "El carro está andando a: ", "El carro está detenido"]
    def__init__(self, is_turned_on, state):
        self._is_turned_on = is_turned_on
        self._is_moving = state
    defturn_on(self):
        self._is_turned_on = True
        self._display_on()
    defturn_off(self):
        self._is_turned_on = False
        self._display_on()
    defmoving(self, velocity):
        self._is_moving = True
        self._display_move(velocity)
    defstop_auto(self):
        self._is_moving = False
        velocity = 0
        self._display_move(velocity)
    def_display_on(self):
        if self._is_turned_on:
            print(self._carro[0])
        else:
            print(self._carro[1])
    def_display_move(self, velocity):
        if self._is_moving:
            print(self._carro[2]+str(velocity)+(" Km/h"))
        else:
            print(self._carro[3])


defrun():
    car = Car(is_turned_on=False, state=False)

    whileTrue:
        command = str(raw_input('''¿Qué deseas hacer?
		[p]render
		[a]pagar
		[m]overse
		[d]etenerse
		[s]alir
		'''))
        if command == 'p':
            car.turn_on()
        elif command == 'a':
            car.turn_off()
        elif command == 'm':
            velocity = input("A qué velocidad desea ir?: ")
            car.moving(velocity)
        elif command == 'd':
            car.stop_auto()
        else:
            break


if __name__ == '__main__':
    run()
