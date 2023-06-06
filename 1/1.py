import pandas as pd
from user_agents import parse
import geoip2.database

def is_bot(user_agent):
    bot_signals = ['bot', 'crawl', 'spider', 'slurp', 'archiver', 'load test', 'monitoring']
    return any(bot_signal in user_agent.lower() for bot_signal in bot_signals)
def get_country(ip):
    try:
        print(reader.country(ip).country.iso_code)
        return reader.country(ip).country.iso_code
    except geoip2.errors.AddressNotFoundError:
        print(reader.country(ip).country.iso_code)
        return 'Not found'

df = pd.read_csv('access.log',
                 sep=' ',
                 header=None,
                 usecols=[0, 3, 11,12,13,14,15,16,17,18],
                 names=['ip', 'time', 'user_agent','user_agent1','user_agent2','user_agent3','user_agent4','user_agent5','user_agent6','user_agent7'],
                 na_values='-',
                 keep_default_na=False,
                 quoting=3)
print(df)

df["user_agent"] = df["user_agent"].astype(str) + " " + df["user_agent1"].astype(str).str.zfill(6)+" "+df["user_agent2"].astype(str)+" "+df["user_agent3"].astype(str)+\
                   " "+df["user_agent4"].astype(str)+" "+df["user_agent5"].astype(str)+" "+df["user_agent6"].astype(str)+" "+df["user_agent7"].astype(str)
print(df["user_agent"])

df['time'] = df['time'].str.strip('[]')
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')


df['os'] = df['user_agent'].apply(lambda ua: parse(ua).os.family)
df['browser'] = df['user_agent'].apply(lambda ua: parse(ua).browser.family)
df['is_bot'] = df['user_agent'].apply(is_bot)


reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
df['country'] = df['ip'].apply(get_country)


daily_users = df.groupby(df.time.dt.date).size()


user_agent_rank = df['browser'].value_counts()


os_rank = df['os'].value_counts()


country_rank = df['country'].value_counts()


bots = df[df['is_bot'] == True]
print("=== Загальна інформація про файл ===")
print(f"Розмір датафрейму: {df.shape}")
print(f"Перелік стовпців: {df.columns.tolist()}")
print(f"Кількість унікальних IP-адрес: {df['ip'].nunique()}")
print(f"Період часу в даних: від {df['time'].min()} до {df['time'].max()}")

print("\n=== Кількість користувачів за днями ===")
print(daily_users)

print("\n=== Ранжування користувачів за User-Agent ===")
print(user_agent_rank)

print("\n=== Ранжування користувачів за операційними системами ===")
print(os_rank)

print("\n=== Ранжування користувачів за країною запиту ===")
print(country_rank)

print("\n=== Інформація про ботів ===")
print(f"Загальна кількість ботів: {bots.shape[0]}")
print(bots['ip'].value_counts())
