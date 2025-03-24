class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        #The total days available: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        # The meeting days: {1, 2, 3, 5, 6, 7,9,10}
        # The days without meetings: {4,8}
        # The count of such days: 2

        # busy_days = []
        # busy_days = set()
        
        # for start , end in meetings:
        #     for day in range(start , end + 1):
        #         if day not in busy_days:
        #             busy_days.add(day)
        # print(busy_days)
        # days_count = 0 
        # for i in range(1, days+1):
        #     if i not in busy_days:
        #         days_count+= 1
        # return days_count 
    
        #Sort the meetings
        meetings.sort(key=lambda x: x[0]) #[[1,3],[5,7],[9,10]]
        merged_meetings = []               

        for start, end in meetings:
            if not merged_meetings or merged_meetings[-1][1] < start:  #we add [1,3] since the list is empty. After that we moved to 
            # [5,7]: Does [5,7] overlap [1,3] no. because 3 < 5 so we add the list to merged meetings. moving to [9,10]
            # 9 < 7 sp we add it too 

                merged_meetings.append([start, end])
            else:       #for case like in test case 2 : When we add [1,3] in the list and move to second thats [2,4] 3 > 2 so we merge the  the list as
            #max(3, 4) =  4 [1, 4]
                merged_meetings[-1][1] = max(merged_meetings[-1][1], end)

        free_days = 0 
        prev_end = 0 
        for start, end in merged_meetings:
            free_days += start - prev_end - 1 # free_days = 0 + 1 - 0-1 = 0
            prev_end = end                     #prev_end = 4 
        free_days += days - prev_end            # 0 + 5 - 4 = 1     
        return free_days






            