class incorrArr(Exception): pass

tests = [
   {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
    'answer': 3117
    },
   {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
   {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]




def appearance(intervals):
    def borders(arr, les): #удаляем все входы/выходы вне урока
        while(arr):
            if les[0] > arr[1]:
                arr = arr[2:]
            else:
                break
        while(arr):
            if les[-1] < arr[-2]:
                arr = arr[:-2]
            else:
               break
    
        if les[0] > arr[0]: #делаем общие границы начала/конца занятия для всех
            arr[0] = les[0]
        if les[-1] < arr[-1]:
            arr[-1] = les[-1]
        return arr
    
    def correct_arr(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                raise incorrArr()
        return arr


    try:          
        lesson = correct_arr( intervals['lesson'] )
        pupil = correct_arr( intervals['pupil'] )
        tutor = correct_arr( intervals['tutor'] )
    except incorrArr:
        print('incorrect array inconsistent array')
        exit()


    pupil = borders(pupil, lesson)
    tutor = borders(tutor, lesson)

    if pupil[0] > tutor[0]:  #для правильного вычисления пересечения множеств, смещаем границы начала/конца занятия
        lesson[0] = tutor[0]
    elif tutor[0] > pupil[0]:
        lesson[0] = pupil[0]

    if pupil[-1] < tutor[-1]:
        lesson[-1] = tutor[-1]
    elif tutor[-1] < pupil[-1]:
        lesson[-1] = pupil[-1]


    index = int(len(pupil) / 2) 
    p_sum = sum( [ (pupil[2*i+1] - pupil[2*i]) for i in range(index) ] ) #время ученика на занятии

    index = int(len(tutor) / 2)
    t_sum = sum( [ (tutor[2*i+1] - tutor[2*i]) for i in range(index) ] ) #время учителя на занятии

    l_sum = lesson[1] - lesson[0]
    return p_sum - (l_sum - t_sum)

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

