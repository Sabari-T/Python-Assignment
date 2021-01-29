import pandas as pd
states={"Andhra Pradesh":[49577103,7],"Assam":[31205576,16],
        "Arunachal Pradesh":[1383727,14],"Bihar":[104099452,12],
        "Chhattisgarh":[25545198,9],"Goa":[1458545,28],
        "Gujarat":[60439692,5],"Haryana":[25351462,20],
        "Himachal Pradesh":[6864602,17],"Jharkhand":[32988134,15],
        "West Bengal":[91276115,13],"Karnataka":[61095297,6],
        "Kerala":[33406061,21],"Madhya Pradesh":[72626809,2],
        "Maharashtra":[112374333,3],"Manipur":[2855794,23],
        "Meghalaya":[2966889,22],"Mizoram":[1097206,24],
        "Nagaland":[1978502,25],"Orissa":[41974218,8],
        "Punjab":[27743338,19],"Rajasthan":[68548437,1], 
        "Sikkim":[610577,27],"Tamil Nadu":[72147030,10],
        "Telangana":[35193978,11],"Tripura":[3673917,26],
        "Uttaranchal":[10086292,18],"Uttar Pradesh":[199812341,4]}
result=pd.DataFrame.from_dict(states,orient="index",
                              columns=["Population","Rank Based on Area"])
print(result)
result.to_csv("D:\\states.csv")