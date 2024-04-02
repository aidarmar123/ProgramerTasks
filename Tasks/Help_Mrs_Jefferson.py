def shortest_arrang(n):
    list_student = []
    sum_two_num = 0
    if n%2==0:
        sum_two_num=int(n/2)
    else:
        list_student.append(n//2)
        list_student.append(n//2+1)
        return sorted(list_student,reverse=True)
    list_student =sorted(list(range(1,n+1)))
    for i in list_student:
        two_num = sum_two_num-i
        if two_num in list_student:

            if sum(list(range(i,two_num+1))) == n:
                list_student = sorted(list(range(i,two_num+1)),reverse=True)
                return list_student

        if list_student[i-1]+list_student[-i]==sum_two_num:
            list_student=list(range(i,list_student[-i]))
            return list_student


    list_student=[-1]
    return list_student

print(shortest_arrang(24))