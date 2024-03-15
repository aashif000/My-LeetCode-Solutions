select w1.Id from weather w1, weather w2 where datediff(w1.RecordDate, w2.RecordDate)=1 and w1.Temperature > w2.Temperature; 
