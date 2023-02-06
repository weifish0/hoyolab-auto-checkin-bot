import genshinstats as gs
import sys

def get_argv_list(a)-> str:
    a = a.split("_")
    return a
    
if __name__ == "__main__":
    uid_lib = get_argv_list(sys.argv[1])
    token_lib = get_argv_list(sys.argv[2])
    user_lib = get_argv_list(sys.argv[3])
    user_number = len(user_lib)
    
    if user_number == 0:
        print("找不到使用者")
    else:
        for user in range(user_number):
            uid = uid_lib[user]
            token = token_lib[user]
            
            gs.set_cookie(ltuid = uid, ltoken = token)         

            reward = gs.claim_daily_reward()
            if reward is not None:
                print(f"{user_lib[user]} 已經自動領取了獎勵 - {reward['cnt']}x {reward['name']}")
            else:
                print(f"{user_lib[user]} 今天已經領取過獎勵了")
