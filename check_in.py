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
        print("No user")
    else:
        for user in range(user_number):
            uid = uid_lib[user]
            token = token_lib[user]
            
            gs.set_cookie(ltuid = uid, ltoken = token)         
            # gs.set_cookie(ltuid=144088752, ltoken="axy7xNLcwx6aFvF0orVhMdBjbk4cCDQK6t0wEDdL")

            reward = gs.claim_daily_reward()
            if reward is not None:
                print(f"{user_lib[user]} Claimed daily reward - {reward['cnt']}x {reward['name']}")
            else:
                print(f"{user_lib[user]} have clames daily reward")
