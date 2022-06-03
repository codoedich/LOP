from Lekser import Lekser
from AbstractSyntaxTree import SignNod, OpNod, WhileNod, IfNod, LinkListNod, PrintNod, LinkListOperNod
import Errors


class Parc:

    def __init__(self, kod):
        self.kod = kod
        self.node_list = list()

    def parse(self):
        # for line in self.kod:
        for v in range(len(self.kod)):
            line = self.kod[v]

            if line[-1].TypeToken() != "SEMICOLON":
                raise Errors.NotSemicolon(v + 1)

            if line[0].TypeToken() == "VAR" and line[1].TypeToken() == "ASSIGNMENT":
                self.node_list.append(self.setAssign(line))
            elif line[0].TypeToken() == "PRINT_TRIGGER":
                self.node_list.append(self.setPrint(line))
            elif line[0].TypeToken() == "IF_TRIGGER":
                self.node_list.append(self.setIf(line))
            elif line[0].TypeToken() == "WHILE_TRIGGER":
                self.node_list.append(self.setWhile(line))
            elif line[0].TypeToken() == "LINKED_LIST_TRIGGER":
                self.node_list.append(self.setLinkedList(line))
            elif line[1].TypeToken() == "LL_INSERT_END":
                self.node_list.append(self.setLLInsertAtEnd(line))

            elif line[1].TypeToken() == "LL_INSERT_HEAD":

                self.node_list.append(self.setLLInsertAtHead(line))
            elif line[1].TypeToken() == "LL_DELETE":

                self.node_list.append(self.setLLDelete(line))
            elif line[1].TypeToken() == "LL_DELETE_HEAD":

                self.node_list.append(self.setLLDeleteAtHead(line))
            elif line[1].TypeToken() == "LL_SEARCH":

                self.node_list.append(self.setLLSearch(line))
            elif line[1].TypeToken() == "LL_IS_EMPTY":

                self.node_list.append(self.setLLIsEmpty(line))
            else:
                raise Errors.FalseKod(line[1].Value(), v + 1)
        return self.node_list

    def setAssign(self, line):
        name_variable = line[0].Value()
        value = line[2:len(line) - 1]
        if len(value) == 1:
            type_token = value[0].TypeToken()
            if type_token == "INT":
                return SignNod("Assign", name_variable, value, type_token)
            if type_token == "VAR":
                return SignNod("Assign", name_variable, value, type_token)
        else:
            if len(value) == 3:
                return SignNod("Assign", name_variable, self.setOperation(value), "Operation")
            else:
                return SignNod("Assign", name_variable, self.setOperation(value), "OperationHard")

    def setPrint(self, line):
        value = line[2:len(line) - 2]
        if len(value) == 1:
            type_value = value[0].TypeToken()
            if type_value == "INT":
                return PrintNod("Print", int(value), type_value)
                # self.node_list.append(PrintNode("Print", value, type_value))
            elif type_value == "VAR":
                return PrintNod("Print", value, type_value)
                # self.node_list.append(PrintNode("Print", value, type_value))
            else:
                pass
        else:
            pass

    def setIf(self, line):
        z = 1
        condition = list()
        loop = list()
        line_kod = list()
        for elem in line:
            if z == 1 and elem.Value() == "(":
                z = 2
            elif z == 2:
                if elem.Value() == ")":
                    z = 3
                    continue
                condition.append(elem)
            elif z == 3 and elem.Value() == "{":
                z = 4
            elif z == 4:
                if elem.Value() == "}":
                    z = 5
                    continue

                line_kod.append(elem)
                if elem.Value() == ";":
                    loop.append(line_kod)
                    line_kod = list()
        ready_loop = list()
        for line in loop:
            if line[0].TypeToken() == "VAR" and line[1].TypeToken() == "ASSIGNMENT":
                ready_loop.append(self.setAssign(line))
            elif line[0].TypeToken() == "PRINT_TRIGGER":
                ready_loop.append(self.setPrint(line))
            else:
                print("ERROR")

        # print([elem.Value() for elem in condition])
        # print(ready_loop[0].Value()[0].Value())
        return IfNod("If", condition, ready_loop)

    def setWhile(self, line):
        z = 1
        condition = list()
        loop = list()
        line_kod = list()
        for elem in line:
            if z == 1 and elem.Value() == "(":
                z = 2
            elif z == 2:
                if elem.Value() == ")":
                    z = 3
                    continue
                condition.append(elem)
            elif z == 3 and elem.Value() == "{":
                z = 4
            elif z == 4:
                if elem.Value() == "}":
                    z = 5
                    continue

                line_kod.append(elem)
                if elem.Value() == ";":
                    loop.append(line_kod)
                    line_kod = list()
        ready_loop = list()
        # print([elem.Value() for elem in loop[0]])
        for line in loop:
            if line[0].TypeToken() == "VAR" and line[1].TypeToken() == "ASSIGNMENT":
                ready_loop.append(self.setAssign(line))
            elif line[0].TypeToken() == "PRINT_TRIGGER":
                ready_loop.append(self.setPrint(line))
            else:
                print("ERROR")

        # print([elem.Value() for elem in condition])
        # print(ready_loop[1])
        return WhileNod("While", condition, ready_loop)

    def setOperation(self, value):
        if len(value) == 3:
            left_operand = value[0]
            sign = value[1]
            right_operand = value[2]
            return OpNod("Operation", left_operand, right_operand, sign, final=True)
        else:
            condition = [elem.Value() for elem in value]
            return OpNod("Operation", value, None, None, final=False)

    def setLinkedList(self, line):
        name_linked_list = line[1].Value()
        values = line[4:len(line) - 2]
        new_values = list()
        for elem in values:
            if elem.TypeToken() != "VIRGULE":
                new_values.append(elem)
        return LinkListNod("LinkedList", name_linked_list, new_values)

    def setLLInsertAtEnd(self, line):
        name_variable = line[0].Value()
        value = line[3]
        return LinkListOperNod("LinkedListOperationNode", "setLLInsertAtEnd", name_variable, value)

    def setLLInsertAtHead(self, line):
        name_variable = line[0].Value()
        value = line[3]
        return LinkListOperNod("LinkedListOperationNode", "setLLInsertAtHead", name_variable, value)

    def setLLDelete(self, line):
        name_variable = line[0].Value()
        value = line[3]
        return LinkListOperNod("LinkedListOperationNode", "setLLDelete", name_variable, value)

    def setLLDeleteAtHead(self, line):
        name_variable = line[0].Value()
        return LinkListOperNod("LinkedListOperationNode", "setLLDeleteAtHead", name_variable, None)

    def setLLSearch(self, line):
        name_variable = line[0].Value()
        value = line[3]
        return LinkListOperNod("LinkedListOperationNode", "setLLSearch", name_variable, value)

    def setLLIsEmpty(self, line):
        name_variable = line[0].Value()
        return LinkListOperNod("LinkedListOperationNode", "setLLIsEmpty", name_variable, None)

    def NodList(self):
        return self.node_list
