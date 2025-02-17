def solution(todo_list, finished):
    answer = []
    dict = {todo_list[i]:finished[i] for i in range(len(todo_list))}
    for i in dict:
        if dict[i]==0:
            answer.append(i)
            
    return answer