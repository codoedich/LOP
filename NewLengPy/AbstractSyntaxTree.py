import Errors


class NOD:

    def __init__(self, type_nod):
        self.type_nod = type_nod

    def TypeNod(self):
        return self.type_nod


class SignNod(NOD):

    def __init__(self, type_node, name_variable, value, type_value):
        super().__init__(type_node)
        self.name_variable = name_variable
        self.value = value
        self.type_value = type_value

    def NameVariable(self):
        return self.name_variable

    def Value(self):
        return self.value

    def TypeValue(self):
        return self.type_value


class OpNod(NOD):

    def __init__(self, type_nod, l_operand, r_operand, signature, final):
        super().__init__(type_nod)
        self.l_operand = l_operand
        self.r_operand = r_operand
        self.signature = signature
        self.final = final
        self.dict_main = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def LeftOperand(self):
        return self.l_operand

    def RightOperand(self):
        return self.r_operand

    def Sign(self):
        return self.signature

    def Final(self):
        return self.final

    def Operation(self, coord, GOLDexp):
        right = int(GOLDexp.pop(coord + 1))
        sign = GOLDexp.pop(coord)
        left = int(GOLDexp.pop(coord - 1))
        result = 0

        if sign == "+":
            result = left + right
        elif sign == "-":
            result = left - right
        elif sign == "*":
            result = left * right
        elif sign == "/":
            result = int(left / right)

        GOLDexp.insert(coord - 1, str(result))
        return GOLDexp

    def funct(self, GOLDexp):
        GOLDexp = self.count(GOLDexp)
        z = 2
        v = 0
        while True:
            element = GOLDexp[v]
            if type(element) != list:
                if element in self.dict_main and self.dict_main[element] == z:
                    if type(GOLDexp[v - 1]) == list:
                        GOLDexp[v - 1] = self.funct(GOLDexp[v - 1])
                    if type(GOLDexp[v + 1]) == list:
                        GOLDexp[v + 1] = self.funct(GOLDexp[v + 1])
                    GOLDexp = self.Operation(v, GOLDexp)
                    v = 0
                else:
                    v += 1
            else:
                v += 1
            if v == len(GOLDexp):
                z -= 1
                v = 0

            if z == 0:
                break
        return GOLDexp[0]

    def count(self, line):
        count_line = list()
        v = 0
        while v <= len(line):
            if line[v] == "(":
                ind = len(line) - 1 - line[::-1].index(")")
                count_line.append(self.count(line[v + 1:ind]))
                v = ind + 1
            else:
                count_line.append(line[v])
                v += 1
            if v == len(line):
                break
        return count_line

    def runOperationHard(self):
        values = self.l_operand
        new_values = [elem.Value() for elem in values]
        return int(self.funct(new_values)[0])


class WhileNod(NOD):

    def __init__(self, type_node, condition, loop):
        super().__init__(type_node)
        self.condition = condition
        self.loop = loop

    def Condition(self):
        return self.condition

    def Loop(self):
        return self.loop


class IfNod(NOD):

    def __init__(self, type_node, condition, loop):
        super().__init__(type_node)
        self.condition = condition
        self.loop = loop

    def Condition(self):
        return self.condition

    def Loop(self):
        return self.loop


class PrintNod(NOD):

    def __init__(self, type_node, value, type_value):
        super().__init__(type_node)
        self.value = value
        self.type_value = type_value

    def Value(self):
        return self.value

    def TypeValue(self):
        return self.type_value


class LinkListNod(NOD):

    def __init__(self, type_node, name, values):
        super().__init__(type_node)
        self.name = name
        self.values = values

    def Name(self):
        return self.name

    def Values(self):
        return self.values


class LinkListOperNod(NOD):

    def __init__(self, type_node, type_operation, name_variable, values):
        super().__init__(type_node)
        self.type_operation = type_operation
        self.name_variable = name_variable
        self.values = values

    def TypeOperation(self):
        return self.type_operation

    def NameVariable(self):
        return self.name_variable

    def Values(self):
        return self.values
