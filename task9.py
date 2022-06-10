class main:
    def __init__(self):
        self.d = {
            'A': {'B': 0, 'G': 1},
            'B': {'G': 3, 'C': 2},
            'C': {'E': 5, 'D': 4},
            'D': {'E': 6, ' ': None},
            'E': {'F': 7, ' ': None},
            'F': {'G': 8, 'D': 9},
            'G': {'H': 10, 'C': 11},
        }
        self.char = 'A'
        self.num = 0

    def jump(self):
        for key, value in self.d.get(self.char).items():
            if isinstance(value, int):
                self.char = key
                self.num = value
            else:
                raise KeyError
            break
        return self.num

    def roam(self):
        i = 0
        for key, value in self.d.get(self.char).items():
            if i == 1:
                if isinstance(value, int):
                    self.char = key
                    self.num = value
                else:
                    raise KeyError
                break
            i += 1
        return self.num


o = main()
o.jump() # 0
o.roam() # 2
o.jump() # 5
o.jump() # 7
o.jump() # 8
o.roam() # 11
o.roam() # 4
o.jump() # 6
print(o.roam()) #   KeyError
o.jump() # 7
o.roam() # 9
o.jump() # 6
o.jump() # 7
o.jump() # 8
print(o.jump()) # 10