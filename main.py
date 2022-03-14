from os import access
import tweepy
import pandas as pd

API_KEY = "3hkfuhFRDpHDNAoUBgBjDO0KS"
API_Key_Secret = "9QaUEBXyerrcNJTvim2NOKL9wq6SBqawsclc3tTILlloSV17Eg"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKPJTgEAAAAAn0yfVU8LwmcbW1SiBjOytYE3YMA%3DNkdpV3Z3tkU1hkZKyx41OXDDtm12LWC7B4y07jFtXXurvYQaif"
ACCESS_TOKEN = "792026036716175360-2gJCdfKnMkjSDdkMuExXUAfxsW4BJUi"
ACCESS_TOKEN_SECRET = "k8fYKCKSRXc4dspOZTQr9jkG2nJInTPwkjd5H9n7uKy9q"

auth = tweepy.OAuthHandler(API_KEY, API_Key_Secret)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def clean(file):
    new_data = []
    with open(file, 'r+') as f:
        for each in f.readlines():
            if each != "\n":
                # if "*" in each:
                each = each.replace("*", "")
                new_data.append(each)

        f.truncate(0)
        for i in new_data:
            f.write(i)


def access_file(file):
    with open(file, 'r+') as f:
        arr = []
        for each in f.readlines():
            if each != "\n":
                each = each.replace("\n", "")
                arr.append(each)

    return arr


def create_profile_link(profile):
    profile = profile.replace("@", "")
    return f"https://twitter.com/{profile}"


def create_csv(user_array):
    names = []
    description = []
    profile_url = []
    website = []
    image = []
    for index, each in enumerate(user_array):
        try:
            user = api.get_user(each)
            names.append(user.name)
            description.append(user.description)
            profile_url.append(create_profile_link(each))
            website.append(user.url)
            image.append(user.profile_image_url)

        except:
            print("User has probably been suspended:", each)

    users = {"Name": names, "Bio": description,
             "Twitter Profile": profile_url, "Website": website, "Image":image}
    df = pd.DataFrame.from_dict(users)
    df.to_csv('users.csv', index=True, header=True)


create_csv(access_file("crypto_profiles.txt"))
# print(access_file("crypto_profiles.txt"))
