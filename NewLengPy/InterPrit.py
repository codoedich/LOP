from Lekser import Lekser
from Parc import Parc


class InterPrit:

    def __init__(self, node_list):
        self.node_list = node_list
        self.variables_values = dict()
        self.linkedlist_values = dict()

    def ORDER66(self):
        for node in self.node_list:
            node_type = node.TypeNod()
            if node_type == "Print":
                self.exePrint(node)
            elif node_type == "If":
                self.exeIf(node)
            elif node_type == "While":
                self.exeWhile(node)
            elif node_type == "Assign":
                self.exeAssign(node)
            elif node_type == "LinkedList":
                self.exeLinkList(node)
            elif node_type == "LinkedListOperationNode":
                self.exeLinkListOp(node)
            else:
                print("ERROR")

    def exeAssign(self, node):
        name_variable = node.NameVariable()
        type_value = node.TypeValue()

        if type_value == "INT":
            value = node.Value()[0].Value()
            self.variables_values[name_variable] = value
        elif type_value == "VAR":
            # print(value)
            value = node.Value()[0].Value()
            self.variables_values[name_variable] = self.variables_values[value]
        elif type_value == "Operation":
            value = self.exeOperation(node.Value())
            self.variables_values[name_variable] = value
        elif type_value == "OperationHard":
            value = node.Value()
            values = value.LeftOperand()
            value = self.exeHARDOperation(value)
            self.variables_values[name_variable] = value

    def exePrint(self, node):
        type_value = node.TypeValue()
        if type_value == "INT":
            value = node.Value()
            print(value[0].Value())
        elif type_value == "VAR":
            name_variable = node.Value()[0].Value()
            if name_variable in self.variables_values:
                value = self.variables_values[name_variable]
                print(value)
            else:
                print("ERROR")
        elif type_value == "Operation":
            pass
        else:
            print("ERROR")

    def exeIf(self, node):
        condition = node.Condition()
        loop = node.Loop()
        value_one = condition[0]
        sign = condition[1]
        value_two = condition[2]

        if value_one.TypeToken() == "VAR":
            value_one_condition = self.variables_values[value_one.Value()]
        else:
            value_one_condition = value_one.Value()

        if value_two.TypeToken() == "VAR":
            value_two_condition = self.variables_values[value_two.Value()]
        else:
            value_two_condition = value_two.Value()

        value_sign = sign.Value()
        type_sign = sign.TypeToken()
        if type_sign == "SIGN_GREATER":
            if int(value_one_condition) > int(value_two_condition):
                for node_loop in loop:
                    node_type = node_loop.TypeNod()
                    if node_type == "Print":
                        self.exePrint(node_loop)
                    elif node_type == "Assign":
                        self.exeAssign(node_loop)

        elif type_sign == "SIGN_LESS":
            if int(value_one_condition) < int(value_two_condition):
                for node_loop in loop:
                    node_type = node_loop.TypeNod()
                    if node_type == "Print":
                        self.exePrint(node_loop)
                    elif node_type == "Assign":
                        self.exeAssign(node_loop)

        elif type_sign == "EQUALS":
            if int(value_one_condition) == int(value_two_condition):
                for node_loop in loop:
                    node_type = node_loop.TypeNod()
                    if node_type == "Print":
                        self.exePrint(node_loop)
                    elif node_type == "Assign":
                        self.exeAssign(node_loop)

    def exeWhile(self, node):
        while True:
            condition = node.Condition()
            loop = node.Loop()
            value_one = condition[0]
            sign = condition[1]
            value_two = condition[2]

            if value_one.TypeToken() == "VAR":
                value_one_condition = self.variables_values[value_one.Value()]
            else:
                value_one_condition = value_one.Value()

            if value_two.TypeToken() == "VAR":
                value_two_condition = self.variables_values[value_two.Value()]
            else:
                value_two_condition = value_two.Value()
            type_sign = sign.TypeToken()

            if type_sign == "SIGN_GREATER":
                if int(value_one_condition) > int(value_two_condition):
                    for node_loop in loop:
                        node_type = node_loop.TypeNod()
                        if node_type == "Print":
                            self.exePrint(node_loop)
                        elif node_type == "Assign":
                            self.exeAssign(node_loop)
                else:
                    break
            elif type_sign == "SIGN_LESS":

                if int(value_one_condition) < int(value_two_condition):
                    for node_loop in loop:
                        node_type = node_loop.TypeNod()
                        if node_type == "Print":
                            self.exePrint(node_loop)
                        elif node_type == "Assign":
                            self.exeAssign(node_loop)
                else:
                    break
            elif type_sign == "EQUALS":
                if int(value_one_condition) == int(value_two_condition):
                    for node_loop in loop:
                        node_type = node_loop.TypeNod()
                        if node_type == "Print":
                            self.exePrint(node_loop)
                        elif node_type == "Assign":
                            self.exeAssign(node_loop)
                else:
                    break

    def exeOperation(self, node):
        left = node.LeftOperand()
        right = node.RightOperand()
        if left.TypeToken() == "VAR":
            left_operand = self.variables_values[left.Value()]
        else:
            left_operand = left.Value()

        if right.TypeToken() == "VAR":
            right_operand = self.variables_values[right.Value()]
        else:
            right_operand = right.Value()
        sign = node.Sign()
        final = node.Final()
        value = 0
        if final:
            if sign.TypeToken() == "PLUS_SIGN":
                value = int(left_operand) + int(right_operand)
            if sign.TypeToken() == "MINUS_SIGN":
                value = int(left_operand) - int(right_operand)
            if sign.TypeToken() == "MULTIPLY_SIGN":
                value = int(left_operand) * int(right_operand)
            if sign.TypeToken() == "DIVIDE_SIGN":
                value = int(left_operand) / int(right_operand)
        else:
            pass
        return int(value)

    def exeHARDOperation(self, node):
        values = node.LeftOperand()
        GOLDexp = [elem.Value() for elem in values]
        value = node.funct(GOLDexp)
        return value

    def exeLinkList(self, node):
        name = node.Name()
        values = node.Values()
        new_values = [elem.Value() for elem in values]
        self.linkedlist_values[name] = new_values

    def exeLinkListOp(self, node):
        type_operation = node.TypeOperation()

        if type_operation == "setLLInsertAtEnd":
            name_variable = node.NameVariable()
            value = node.Values()
            value_type = value.TypeToken()
            value = value.Value()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                values.append(value)
                self.linkedlist_values[name_variable] = values
            else:
                print("ERROR")

        elif type_operation == "setLLInsertAtHead":
            name_variable = node.NameVariable()
            value = node.Values()
            value_type = value.TypeToken()
            value = value.Value()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                values = [value] + values
                self.linkedlist_values[name_variable] = values
            else:
                print("ERROR")

        elif type_operation == "setLLDelete":
            name_variable = node.NameVariable()
            value = node.Values()
            value_type = value.TypeToken()
            value = value.Value()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                result = values.pop(int(value))
                self.linkedlist_values[name_variable] = values
                print(f"Element is deleted: {result}")
            else:
                print("ERROR")

        elif type_operation == "setLLDeleteAtHead":
            name_variable = node.NameVariable()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                result = values.pop(0)
                self.linkedlist_values[name_variable] = values
                print(f"Element is deleted: {result}")
            else:
                print("ERROR")

        elif type_operation == "setLLSearch":
            name_variable = node.NameVariable()
            value = node.Values()
            value_type = value.TypeToken()
            value = value.Value()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                print(f"Element on position {value}: {values[int(value)]}")
            else:
                print("ERROR")

        elif type_operation == "setLLIsEmpty":
            name_variable = node.NameVariable()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                if len(values) == 0:
                    print("LinkedList is empty.")
                else:
                    print("LinkedList is NOT empty.")
            else:
                print("ERROR")

        else:
            pass
