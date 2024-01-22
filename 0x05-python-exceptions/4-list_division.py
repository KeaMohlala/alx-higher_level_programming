#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    temp_result = []
    for i in range(list_length):
        try:
            temp_result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            temp_result.append(0)
            print("division by 0")
        except IndexError:
            temp_result.append(0)
            print("out of range")
        except (TypeError, ValueError):
            temp_result.append(0)
            print("wrong type")
        finally:
            result = temp_result
    return result
