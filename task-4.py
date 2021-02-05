def most_frequent(str):
  freq = {}  

  for ele in str:  
      if ele in freq:  
          freq[ele] += 1
      else:  
          freq[ele] = 1
 
  srt = sorted(freq.items(), key=lambda x: x[1], reverse=True)
  for i in srt:
    print(i[0], " - ", i[1])
string = input("Enter the string : ")

most_frequent(string)
